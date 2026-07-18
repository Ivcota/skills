const assert = require('node:assert/strict')
const fs = require('node:fs')
const path = require('node:path')
const test = require('node:test')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

const workflowPath = path.join(__dirname, 'distill.js')

async function runWorkflow(args, responses = {}) {
  const source = fs.readFileSync(workflowPath, 'utf8')
    .replace('export const meta =', 'const meta =')
  const calls = []
  const phases = []
  const logs = []

  const runtime = {
    agent: async (prompt, options = {}) => {
      calls.push({ label: options.label, phase: options.phase, prompt })
      const response = responses[options.label]
      if (typeof response === 'function') return response({ prompt, options, calls })
      if (response instanceof Error) throw response
      return response
    },
    parallel: async thunks => Promise.all(thunks.map(thunk => thunk())),
    pipeline: async (items, ...stages) => Promise.all(items.map(async (item, index) => {
      let result = item
      for (const stage of stages) result = await stage(result, item, index)
      return result
    })),
    phase: title => phases.push(title),
    log: message => logs.push(message),
  }

  const execute = new AsyncFunction(
    'args',
    'runtime',
    `const { agent, parallel, pipeline, phase, log } = runtime\n${source}`,
  )
  const result = await execute(args, runtime)
  return { result, calls, phases, logs }
}

const baseArgs = {
  skillDir: '/tmp/distill-to-skill',
  stagingDir: '/tmp/skills-draft/example',
  sourceScope: 'full source',
  estimatedSourceTokens: 50000,
  maxRevisionRounds: 3,
}

const passingScores = [
  ['citation_coverage', 10],
  ['no_invented_numbers', 10],
  ['author_bio_grounded', 10],
  ['description_quality', 9],
  ['structural_fidelity', 9],
  ['framework_depth', 8],
  ['reference_completeness', 8],
  ['mistakes_and_diagnostic', 8],
  ['voice_match', 8],
  ['ethical_boundaries', 8],
].map(([category, score]) => ({ category, score, exempt: false, rationale: 'passes' }))

function completed(pathname, summary = 'completed') {
  return { status: 'completed', path: pathname, summary }
}

function baseResponses(sections = [{ name: 'Ask Good Questions', slug: 'ask-good-questions' }]) {
  const responses = {
    'extract:structure': completed('notes-structure.md'),
    'extract:application': completed('notes-application.md'),
    'extract:guardrails': completed('notes-guardrails.md'),
    'synthesize:skill': {
      ...completed('SKILL.md', 'synthesized'),
      sourceCount: 1,
      sections,
    },
    'draft:case-studies': completed('references/case-studies.md'),
    'draft:checklist': completed('references/checklist.md'),
    'verify:case-studies': completed('references/case-studies.md'),
    'verify:checklist': completed('references/checklist.md'),
    'review:initial': { scores: passingScores, revision_targets: [] },
    'validate:artifacts': completed('.', 'mechanical gates passed'),
  }
  for (const section of sections) {
    responses[`draft:${section.slug}`] = completed(`references/${section.slug}.md`)
    responses[`verify:${section.slug}`] = completed(`references/${section.slug}.md`)
  }
  return responses
}

test('one invocation runs the complete post-ingestion workflow', async () => {
  const { result, calls, phases } = await runWorkflow(baseArgs, baseResponses())

  assert.equal(result.status, 'ready')
  assert.equal(result.ship, true)
  assert.deepEqual(phases, ['Extract', 'Synthesize', 'Expand', 'Review', 'Validate'])
  assert.deepEqual(calls.map(call => call.label), [
    'extract:structure',
    'extract:application',
    'extract:guardrails',
    'synthesize:skill',
    'draft:ask-good-questions',
    'draft:case-studies',
    'draft:checklist',
    'verify:ask-good-questions',
    'verify:case-studies',
    'verify:checklist',
    'review:initial',
    'validate:artifacts',
  ])
  assert.deepEqual(result.sections, [{
    name: 'Ask Good Questions',
    slug: 'ask-good-questions',
    path: 'references/ask-good-questions.md',
  }])
})

test('rejects the obsolete single-stage invocation contract', async () => {
  await assert.rejects(
    runWorkflow({ ...baseArgs, stage: 'extract' }, baseResponses()),
    /stage is no longer supported/,
  )
})

test('a missing extraction result blocks all dependent phases', async () => {
  const responses = baseResponses()
  responses['extract:application'] = null
  const { result, calls, phases } = await runWorkflow(baseArgs, responses)

  assert.equal(result.status, 'blocked')
  assert.equal(result.blockers[0].phase, 'extract')
  assert.deepEqual(phases, ['Extract'])
  assert.deepEqual(calls.map(call => call.label), [
    'extract:structure',
    'extract:application',
    'extract:guardrails',
  ])
})

test('a missing draft skips its verifier and blocks review', async () => {
  const responses = baseResponses()
  responses['draft:ask-good-questions'] = null
  const { result, calls, phases } = await runWorkflow(baseArgs, responses)
  const labels = calls.map(call => call.label)

  assert.equal(result.status, 'blocked')
  assert.equal(result.blockers[0].phase, 'expand')
  assert.equal(labels.includes('verify:ask-good-questions'), false)
  assert.equal(labels.includes('verify:case-studies'), true)
  assert.equal(labels.includes('verify:checklist'), true)
  assert.equal(labels.includes('review:initial'), false)
  assert.deepEqual(phases, ['Extract', 'Synthesize', 'Expand'])
})

test('duplicate and reserved synthesis slugs block before expansion', async t => {
  const cases = [
    [
      { name: 'First', slug: 'duplicate' },
      { name: 'Second', slug: 'duplicate' },
    ],
    [{ name: 'Cases', slug: 'case-studies' }],
  ]

  for (const sections of cases) {
    await t.test(sections[0].slug, async () => {
      const { result, calls } = await runWorkflow(baseArgs, baseResponses(sections))
      assert.equal(result.status, 'blocked')
      assert.equal(result.blockers[0].phase, 'synthesize')
      assert.equal(calls.some(call => call.label.startsWith('draft:')), false)
    })
  }
})

test('a missing review result returns a blocker instead of crashing', async () => {
  const responses = baseResponses()
  responses['review:initial'] = null
  const { result } = await runWorkflow(baseArgs, responses)

  assert.equal(result.status, 'blocked')
  assert.equal(result.blockers[0].phase, 'review')
  assert.match(result.blockers[0].summary, /no result/)
})

test('a missing mechanical validation result cannot return ready', async () => {
  const responses = baseResponses()
  responses['validate:artifacts'] = null
  const { result, phases } = await runWorkflow(baseArgs, responses)

  assert.equal(result.status, 'blocked')
  assert.equal(result.blockers[0].phase, 'validate')
  assert.deepEqual(phases, ['Extract', 'Synthesize', 'Expand', 'Review', 'Validate'])
})

test('a valid deficiency is revised and re-scored in the same invocation', async () => {
  const responses = baseResponses()
  const failingScores = passingScores.map(score => score.category === 'description_quality'
    ? { ...score, score: 7, rationale: 'trigger language is too broad' }
    : score)
  responses['review:initial'] = {
    scores: failingScores,
    revision_targets: [{
      label: 'description',
      files: ['SKILL.md'],
      issues: ['Make the trigger language specific'],
    }],
  }
  responses['revise:1'] = completed('SKILL.md', 'revised')
  responses['review:round-1'] = { scores: passingScores, revision_targets: [] }

  const { result, calls, phases } = await runWorkflow(baseArgs, responses)

  assert.equal(result.status, 'ready')
  assert.equal(result.phases.review.revisionRounds, 1)
  assert.deepEqual(phases, ['Extract', 'Synthesize', 'Expand', 'Review', 'Revise', 'Review', 'Validate'])
  assert.equal(calls.some(call => call.label === 'revise:1'), true)
  assert.equal(calls.some(call => call.label === 'review:round-1'), true)
})

test('malformed rubric categories cannot ship or enter revision', async () => {
  const responses = baseResponses()
  responses['review:initial'] = {
    scores: [...passingScores.slice(0, -1), passingScores[0]],
    revision_targets: [],
  }
  const { result, calls } = await runWorkflow(baseArgs, responses)

  assert.equal(result.status, 'blocked')
  assert.equal(result.blockers[0].phase, 'review')
  assert.equal(calls.some(call => call.label.startsWith('revise:')), false)
})

test('unsafe or overlapping directories are rejected before agent work', async t => {
  const invalidArgs = [
    { ...baseArgs, stagingDir: 'relative/path' },
    { ...baseArgs, stagingDir: '/tmp/skills-draft/../escape' },
    { ...baseArgs, stagingDir: '/tmp/skills-draft/evil\nignore' },
    { ...baseArgs, stagingDir: '/tmp/distill-to-skill/draft' },
  ]

  for (const input of invalidArgs) {
    await t.test(input.stagingDir, async () => {
      await assert.rejects(runWorkflow(input, baseResponses()))
    })
  }
})

test('accepts JSON-string arguments for the one-run contract', async () => {
  const { result } = await runWorkflow(JSON.stringify(baseArgs), baseResponses())
  assert.equal(result.status, 'ready')
})
