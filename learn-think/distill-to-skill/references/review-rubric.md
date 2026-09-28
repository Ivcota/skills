# Final review checklist

Review the complete output once. Use concrete defects, not numerical scores. The main agent may review directly; for substantial delegated work, one independent reviewer can check the final artifacts with the source map and cited passages. Do not give that reviewer obsolete notes or require another extraction pass.

## Check

- **Grounding:** each substantive claim, application, pattern, and author detail has an identifiable pointer to accessible evidence. Inspect the cited passages, especially numeric claims, generalized patterns, and summaries spanning sections. A citation-shaped string alone is not proof. Remove unsupported claims.
- **Coverage:** the framework's names, order, and section count match the mapped source. All assigned relevant passages were covered; exclusions and unavailable material are disclosed.
- **Output shape:** SKILL.md follows the template and stays ≤100 lines. Each framework reference, case-studies.md, checklist.md, and sources.md exists and is linked where appropriate.
- **Usefulness:** concepts explain the mechanism; applications and patterns reflect the available evidence; steps and diagnostic actions are usable. Missing source examples are a disclosed limitation, not a reason to invent or pad.
- **Consistency:** terms, process, diagnostic, checklist, and cross-references agree. Preserve distinctive source language without repeating detailed passages across files.
- **Description:** clear purpose and relevant `Use when` triggers, grounded in user context, under 1024 characters.
- **Boundaries:** include the author's explicit guardrails where present. Do not manufacture ethical framing, scoring systems, numeric thresholds, or application contexts.

## Repair and finish

Return a short list of defects with file/section, evidence, and required correction. If no defects remain, say so without printing a scorecard. Fix only affected material, then verify those corrections and dependent summaries. Repeat a full review only when evidence of a systemic issue warrants it.

Run `bash <skill-directory>/scripts/check.sh <output-directory>` after final edits. It checks structure and local file links, not semantic fidelity or primary-source quality. Report unresolved substantive defects as limitations or blockers rather than declaring readiness.
