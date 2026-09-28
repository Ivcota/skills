---
name: manage-skills
description: |
  Inventory, activate, and deactivate local agent skills across Codex, Claude Code, Pi, OpenCode, and Cursor at project or global scope. Use when the user asks which skills are active, wants to turn a skill on or off, or wants to move skills between discovered and non-discovered directories. Preserve existing symlinks and show every affected agent before changing files.
---

# Manage skills

Manage filesystem-based skills for all supported agents together. Do not ask the user to pick an agent unless they specifically want to narrow the operation. A skill may be visible to several agents through one shared directory, or may remain visible through another directory after one entry is moved.

## Discovery roots

Check these default locations for the requested project and scope. `PROJECT` is the chosen project root, not necessarily the agent's current working directory. Check applicable ancestor and nested project directories when inventorying a specific working directory or package.

| Agent | Project roots | Global roots |
| --- | --- | --- |
| Codex | `PROJECT/.agents/skills` | `~/.agents/skills` |
| Claude Code | `PROJECT/.claude/skills` | `~/.claude/skills` |
| Pi | `PROJECT/.agents/skills`, `PROJECT/.pi/skills` | `~/.agents/skills`, `~/.pi/agent/skills` |
| OpenCode | `PROJECT/.agents/skills`, `PROJECT/.claude/skills`, `PROJECT/.opencode/skills` | `~/.agents/skills`, `~/.claude/skills`, `~/.config/opencode/skills` |
| Cursor | `PROJECT/.agents/skills`, `PROJECT/.cursor/skills`, `PROJECT/.claude/skills`, `PROJECT/.codex/skills` | `~/.agents/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills` |

`PROJECT/.agents/skills` and `~/.agents/skills` are the preferred multi-agent destinations for a skill that has no previous active location. They serve Codex, Pi, OpenCode, and Cursor, but not Claude Code; do not imply that activating there enables Claude Code. Other roots still count: never claim a skill is off without checking the relevant alternate locations. Check configured additional sources when present, including OpenCode `skills` entries, Pi resource settings and packages, and directories added to Claude Code for the session. Account for configured overrides to default global paths. Report sources that cannot be verified; do not promise that filesystem moves disable built-in, plugin, synced, or remote skills.

Use the supported agents' current documentation to verify discovery behavior before relying on a non-default path or agent-specific behavior. In particular, skill directories may be scanned recursively, so the inactive store must never be placed under a discovery root.

## Inactive storage

- Project: `PROJECT/.skill-manager/inactive/<original-root-relative-to-project>/<skill-entry>`.
- Global: `~/.local/share/skill-manager/inactive/<original-root-relative-to-home>/<skill-entry>`.

The directory structure records the original active location so activation restores the entry to exactly that location. For a new entry with no original location, prefer `.agents/skills` at the requested scope and disclose that Claude Code does not discover it there. If the original location cannot be represented safely under the inactive store (for example, an active root outside the project or home), ask before choosing a holding path and record the exact source so it can be restored. Do not put inactive skills under `.agents/skills`, `.claude/skills`, `.pi/skills`, `.opencode/skills`, `.cursor/skills`, or any configured discovery root.

## Inventory

1. Establish the project root and whether the user means project, global, or both. If unspecified, inspect the current project and relevant global roots; show scope separately.
2. Inspect active discovery roots and inactive stores without following symlinks while listing entries. For each entry, distinguish a real directory, a symlink to a directory, and a broken symlink. Read `SKILL.md` only to identify and validate the skill; never execute bundled scripts as part of inventory.
3. For each symlink, record the exact link text and resolved target. Group entries by skill identity, but retain every path and symlink separately; entries with the same name may contain different skills.
4. Show the skill, scope, active path or inactive path, entry type, target if linked, and agents that discover each active path. Use `active`, `active elsewhere`, `inactive`, `broken link`, or `uncertain` as appropriate. Treat duplicate names and configured sources as potential overrides, not proof that a particular definition loads.

## Change a skill's state

1. Identify the exact entry to move. If there are multiple entries with the same name, ask which entry the user means. Confirm the skill has a valid `SKILL.md`; do not move a whole shared skills root.
2. Preview the source, destination, entry type, and every agent affected. Check whether another active path still exposes the skill. Explain that disabling one entry does not necessarily disable the skill everywhere.
3. Check the destination does not already exist and that the source has not changed since inventory. Never overwrite, merge, delete, or replace an existing entry. If an existing symlink points into a directory being moved, warn that moving the directory may break that link.
4. Ask for confirmation before changing files. For project moves, show the Git status of affected paths so the user knows whether a tracked skill will appear removed or moved. Do not stage or commit unless asked.
5. Move the directory or symlink entry, not the symlink target. Preserve the exact symlink text. A relative symlink may appear broken while stored inactive; check its target again from the restored active path. Never rewrite an absolute or relative target without a separate request.
6. Re-inventory the relevant roots and report the actual resulting state. If the move fails, stop and report which entry is at which path; do not attempt a destructive cleanup.

Do not deactivate this managing skill while using it unless the user explicitly asks; if asked, make that the final operation and explain that a new session may be needed to use it again. Never modify managed, built-in, plugin-installed, account-synced, or otherwise externally controlled skills as though they were ordinary local entries.
