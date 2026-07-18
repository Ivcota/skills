export const meta = {
  name: 'distill-to-skill',
  description: 'Orchestrate extraction, reference expansion, and rubric revision for distill-to-skill',
  phases: [
    { title: 'Extract', detail: 'run structure, application, and guardrails workers in parallel' },
    { title: 'Expand', detail: 'draft and verify one reference file per item' },
    { title: 'Review', detail: 'score the staged skill against the canonical rubric' },
    { title: 'Revise', detail: 'apply surgical fixes to deficient sections' },
  ],
}

const WORK_RESULT_SCHEMA = {
  type: 'object',
  properties: {
    status: { type: 'string', enum: ['completed', 'blocked'] },
    path: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['status', 'path', 'summary'],
  additionalProperties: false,
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    ship: { type: 'boolean' },
    scores: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          category: { type: 'string' },
          score: { type: 'number' },
          target: { type: 'number' },
          rationale: { type: 'string' },
        },
        required: ['category', 'score', 'target', 'rationale'],
        additionalProperties: false,
      },
    },
    revision_targets: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          target: { type: 'string' },
          files: { type: 'array', items: { type: 'string' } },
          issues: { type: 'array', items: { type: 'string' } },
        },
        required: ['target', 'files', 'issues'],
        additionalProperties: false,
      },
    },
  },
  required: ['ship', 'scores', 'revision_targets'],
  additionalProperties: false,
}

function parseInput(value) {
  if (typeof value === 'string') {
    try {
      return JSON.parse(value)
    } catch {
      throw new Error('args must be an object or valid JSON string')
    }
  }
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new Error('args must be an object')
  }
  return value
}

function requireString(input, key) {
  const value = input[key]
  if (typeof value !== 'string' || !value.trim()) {
    throw new Error(`args.${key} must be a non-empty string`)
  }
  return value
}

function requireAbsolutePath(input, key) {
  const value = requireString(input, key)
  const absolute = value.startsWith('/') || /^[A-Za-z]:[\\/]/.test(value)
  if (!absolute) throw new Error(`args.${key} must be an absolute path`)
  return value.replace(/[\\/]$/, '')
}

function scopeFor(sourceScope, key) {
  if (typeof sourceScope === 'string' && sourceScope.trim()) return sourceScope
  if (sourceScope && typeof sourceScope === 'object') {
    const scoped = sourceScope[key] || sourceScope.default
    if (typeof scoped === 'string' && scoped.trim()) return scoped
  }
  return 'full source'
}

function validateExtractionScope(sourceScope, estimatedSourceTokens) {
  if (!estimatedSourceTokens || estimatedSourceTokens <= 100000) return
  const keys = ['structure', 'application', 'guardrails']
  const scoped = sourceScope && typeof sourceScope === 'object'
    && keys.every(key => typeof sourceScope[key] === 'string' && sourceScope[key].trim())
  if (!scoped) {
    throw new Error('sources over 100k tokens require explicit structure, application, and guardrails scopes')
  }
}

function summarizeResults(results) {
  const present = results.filter(Boolean)
  return {
    completed: present.filter(result => result.status === 'completed').length,
    blocked: present.filter(result => result.status === 'blocked'),
  }
}

function reviewPasses(evaluation) {
  return Boolean(
    evaluation
    && evaluation.scores.length >= 10
    && evaluation.revision_targets.length === 0
    && evaluation.scores.every(score => score.score >= score.target),
  )
}

function validateSections(value) {
  if (!Array.isArray(value) || value.length === 0) {
    throw new Error('args.sections must be a non-empty array for the expand stage')
  }
  return value.map((section, index) => {
    if (!section || typeof section !== 'object') {
      throw new Error(`args.sections[${index}] must be an object`)
    }
    const name = typeof section.name === 'string' ? section.name.trim() : ''
    const slug = typeof section.slug === 'string' ? section.slug.trim() : ''
    if (!name || !/^[a-z0-9_-]+$/.test(slug)) {
      throw new Error(`args.sections[${index}] requires name and a safe lowercase slug`)
    }
    return { type: 'section', name, slug, path: `references/${slug}.md` }
  })
}

function normalizeRevisionFile(file, stagingDir) {
  if (typeof file !== 'string' || !file.trim()) return null
  const root = stagingDir.replace(/\\/g, '/').replace(/\/$/, '')
  const candidate = file.trim().replace(/\\/g, '/')
  let relative = candidate
  if (candidate.startsWith(`${root}/`)) relative = candidate.slice(root.length + 1)
  else if (candidate.startsWith('/') || /^[A-Za-z]:\//.test(candidate)) return null
  relative = relative.replace(/^\.\//, '')
  if (!relative || relative.split('/').includes('..')) return null
  return `${root}/${relative}`
}

function mergeRevisionTargets(targets, stagingDir) {
  const groups = []
  for (const target of targets) {
    const files = [...new Set(target.files
      .map(file => normalizeRevisionFile(file, stagingDir))
      .filter(Boolean))].sort()
    if (files.length === 0) {
      throw new Error(`review target "${target.target}" did not provide a safe staged file path`)
    }
    const overlapping = groups.filter(group => files.some(file => group.files.includes(file)))
    const untouched = groups.filter(group => !overlapping.includes(group))
    if (overlapping.length === 0) {
      groups.push({ ...target, files })
      continue
    }
    groups.length = 0
    groups.push(...untouched, {
      target: [target.target, ...overlapping.map(group => group.target)].join(' + '),
      files: [...new Set([...files, ...overlapping.flatMap(group => group.files)])].sort(),
      issues: [...new Set([...target.issues, ...overlapping.flatMap(group => group.issues)])],
    })
  }
  return groups
}

function extractionPrompt(job, skillDir, stagingDir, sourceScope, estimatedSourceTokens) {
  return `You are the ${job.label} extraction worker for distill-to-skill.

Read these canonical instructions before working:
- ${skillDir}/references/extraction-jobs.md — follow only Universal boilerplate and ${job.heading}
- ${skillDir}/references/citation-rules.md
- ${stagingDir}/sources.md

Source scope: ${sourceScope}
Estimated source size: ${estimatedSourceTokens || 'unknown'} tokens
Output file: ${stagingDir}/${job.output}

Use the source locations recorded in sources.md. Do not read outside the assigned scope. Every extracted item must carry a source pointer and quote. Omit unsupported claims; never fill gaps from training data. Keep the result under 10k tokens (roughly 40k characters). Write only the assigned output file and do not modify any other artifact. If the source or scope is inaccessible, do not invent a substitute: return status "blocked" and explain why.

After writing or determining that you are blocked, return the required compact status object.`
}

function expansionPrompt(item, skillDir, stagingDir) {
  if (item.type === 'section') {
    return `Draft the reference file for framework section "${item.name}".

Read:
- ${stagingDir}/SKILL.md
- ${stagingDir}/sources.md
- ${stagingDir}/notes-structure.md
- ${stagingDir}/notes-application.md
- ${stagingDir}/notes-guardrails.md
- ${skillDir}/references/template.md
- ${skillDir}/references/citation-rules.md
- ${skillDir}/references/review-rubric.md

Write only ${stagingDir}/${item.path}. Target roughly 100-300 lines. Include the sourced Core concept, Why it works, Key insights, Application table, Copy patterns, and Ethical boundary when the source contains one. Preserve the source's voice and order. Every claim, row, example, and pattern needs a citation. Do not invent missing contexts, numbers, or ethics. Ensure the parent references directory exists. Return the required compact status object when done.`
  }

  if (item.type === 'case-studies') {
    return `Create ${stagingDir}/${item.path} from the staged extraction notes and source manifest. Include only case studies and worked examples actually present in the sources, grouped by sourced context, with a citation on every example. Read ${skillDir}/references/citation-rules.md and ${skillDir}/references/review-rubric.md first. Do not modify any other file. Ensure the parent references directory exists. Return the required compact status object when done.`
  }

  return `Create ${stagingDir}/${item.path} as an actionable checklist derived only from the staged SKILL.md, extraction notes, and cited source material. Preserve the author's sequence, cite each substantive action, and do not invent thresholds or steps. Read ${skillDir}/references/citation-rules.md and ${skillDir}/references/review-rubric.md first. Do not modify any other file. Ensure the parent references directory exists. Return the required compact status object when done.`
}

function verificationPrompt(item, skillDir, stagingDir, draftResult) {
  return `Verify and, only if necessary, surgically fix ${stagingDir}/${item.path}.

The drafting worker reported:
${JSON.stringify(draftResult)}

Read the file plus ${stagingDir}/sources.md, the three notes files, ${skillDir}/references/citation-rules.md, and ${skillDir}/references/review-rubric.md. Check citation coverage, source fidelity, required elements, line-depth target, invented numbers, and invented ethical guidance. Make focused corrections in this file only; do not rewrite compliant material and do not touch other artifacts. If source evidence is insufficient, remove the unsupported content rather than fabricating it. Return the required compact status object.`
}

function reviewPrompt(skillDir, stagingDir, priorRound) {
  const roundNote = priorRound === 0
    ? 'This is the initial review.'
    : `This is re-score round ${priorRound} after targeted revisions.`
  return `Score the staged skill at ${stagingDir} against ${skillDir}/references/review-rubric.md. ${roundNote}

Read SKILL.md, sources.md, all notes-*.md files, and every references/*.md file. Do not edit files. Return every rubric category with score, target, and concise evidence. Hard-rule categories require 10. For anything below target, return revision_targets grouped by target file or framework section: list files relative to ${stagingDir}, aggregate all issues for the same files into one target, and never repeat a file in multiple targets. Set ship=true only when every category meets its target.`
}

function revisionPrompt(target, skillDir, stagingDir) {
  return `Apply a surgical revision for this rubric target:
${JSON.stringify(target)}

Read ${skillDir}/references/review-rubric.md, ${skillDir}/references/extraction-jobs.md, ${skillDir}/references/citation-rules.md, and the staged source/notes files before editing. Modify only the files listed in target.files. Resolve every listed issue without regenerating unrelated content. Re-extract or verify against sources when needed; if a claim cannot be cited, remove it. Never invent numbers, examples, contexts, or ethical guidance. Return the required compact status object with path set to the comma-separated files you inspected.`
}

const input = parseInput(args)
const stage = requireString(input, 'stage').toLowerCase()
const allowedStages = ['validate', 'extract', 'expand', 'review']
if (!allowedStages.includes(stage)) {
  throw new Error(`args.stage must be one of: ${allowedStages.join(', ')}`)
}

if (stage === 'validate') {
  return { valid: true, stages: allowedStages.filter(value => value !== 'validate') }
}

const skillDir = requireAbsolutePath(input, 'skillDir')
const stagingDir = requireAbsolutePath(input, 'stagingDir')

if (stage === 'extract') {
  phase('Extract')
  const jobs = [
    { key: 'structure', label: 'Structure', heading: 'Job 1 — Structure', output: 'notes-structure.md' },
    { key: 'application', label: 'Application', heading: 'Job 2 — Application', output: 'notes-application.md' },
    { key: 'guardrails', label: 'Guardrails', heading: 'Job 3 — Guardrails', output: 'notes-guardrails.md' },
  ]
  const estimatedSourceTokens = Number.isFinite(input.estimatedSourceTokens)
    ? input.estimatedSourceTokens
    : null
  validateExtractionScope(input.sourceScope, estimatedSourceTokens)
  const results = await parallel(jobs.map(job => () => agent(
    extractionPrompt(
      job,
      skillDir,
      stagingDir,
      scopeFor(input.sourceScope, job.key),
      estimatedSourceTokens,
    ),
    {
      label: `extract:${job.key}`,
      phase: 'Extract',
      schema: WORK_RESULT_SCHEMA,
    },
  )))
  return { stage, ...summarizeResults(results), results }
}

if (stage === 'expand') {
  phase('Expand')
  const items = [
    ...validateSections(input.sections),
    { type: 'case-studies', name: 'Case studies', slug: 'case-studies', path: 'references/case-studies.md' },
    { type: 'checklist', name: 'Checklist', slug: 'checklist', path: 'references/checklist.md' },
  ]
  const results = await pipeline(
    items,
    item => agent(expansionPrompt(item, skillDir, stagingDir), {
      label: `draft:${item.slug}`,
      phase: 'Expand',
      schema: WORK_RESULT_SCHEMA,
    }),
    (draftResult, item) => draftResult && draftResult.status === 'blocked'
      ? draftResult
      : agent(verificationPrompt(item, skillDir, stagingDir, draftResult), {
        label: `verify:${item.slug}`,
        phase: 'Expand',
        schema: WORK_RESULT_SCHEMA,
      }),
  )
  return {
    stage,
    files: items.map(item => item.path),
    ...summarizeResults(results),
    results,
  }
}

phase('Review')
const requestedRounds = Number.isInteger(input.maxRevisionRounds) ? input.maxRevisionRounds : 3
const maxRevisionRounds = Math.max(0, Math.min(requestedRounds, 5))
let revisionRounds = 0
let evaluation = await agent(reviewPrompt(skillDir, stagingDir, revisionRounds), {
  label: 'review:initial',
  phase: 'Review',
  schema: REVIEW_SCHEMA,
})

while (!reviewPasses(evaluation) && evaluation.revision_targets.length > 0 && revisionRounds < maxRevisionRounds) {
  revisionRounds += 1
  const revisionTargets = mergeRevisionTargets(evaluation.revision_targets, stagingDir)
  phase('Revise')
  log(`Revision round ${revisionRounds}/${maxRevisionRounds}: ${revisionTargets.length} non-overlapping target(s)`)
  await pipeline(
    revisionTargets,
    target => agent(revisionPrompt(target, skillDir, stagingDir), {
      label: `revise:${target.target}`,
      phase: 'Revise',
      schema: WORK_RESULT_SCHEMA,
    }),
  )
  phase('Review')
  evaluation = await agent(reviewPrompt(skillDir, stagingDir, revisionRounds), {
    label: `review:round-${revisionRounds}`,
    phase: 'Review',
    schema: REVIEW_SCHEMA,
  })
}

if (!reviewPasses(evaluation) && revisionRounds >= maxRevisionRounds) {
  log(`Stopped after ${maxRevisionRounds} revision round(s); unresolved targets are returned to the caller.`)
}

return {
  stage,
  ship: reviewPasses(evaluation),
  revisionRounds,
  scores: evaluation ? evaluation.scores : [],
  unresolvedTargets: evaluation ? evaluation.revision_targets : [],
}
