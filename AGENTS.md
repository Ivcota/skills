# Agent Instructions

## Skill lookup

- When discussing skills, check this repository first before looking at global skills.

## Commit style

- Commit only when the user explicitly asks for a commit.
- Before committing, run `git status --short` and review the staged diff with `git diff --staged`.
- Stage only files related to the requested change; do not sweep in unrelated work.
- Prefer one logical change per commit.
- Use concise, imperative commit subjects with a conventional prefix:
  - `feat:` for a new user-facing capability or skill
  - `fix:` for bug fixes or corrections
  - `docs:` for documentation-only changes
  - `refactor:` for behavior-preserving code restructuring
- Examples:
  - Good: `docs: add missing skills to README index`
  - Good: `docs: document commit style for agents`
  - Good: `fix: correct skill install command`
  - Good: `refactor: simplify skill discovery script`
  - Avoid: `updated files`, `fix stuff`, `changes`, `WIP`
- Keep the full subject under ~72 characters when practical.
- Do not include AI/tool attribution in commit messages unless the user requests it.
- Do not amend, rebase, squash, or force-push unless the user explicitly asks.
- After committing, report the short commit hash and subject.
