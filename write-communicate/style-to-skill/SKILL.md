---
name: style-to-skill
description: Package an existing STYLE_PROFILE.md into a personal, invokable Claude Code skill (like `write-like-me`) so the user can apply their voice anywhere without pointing at the source file. Use when the user says "package my style profile into a skill", "make a write-like-me skill", "turn my STYLE_PROFILE.md into a skill", "bundle my voice as a skill", or "I want a skill that writes like me". Distinct from the generic `style-profile` skill (which extracts a profile from samples) and from `write-a-skill` (general skill creation) — this is the narrow profile→skill packager.
---

# Style → Skill

Package a user's existing style profile into two installable artifacts:

1. A self-contained, globally invokable skill at `~/.claude/skills/<name>/` (for Claude Code).
2. A `<name>.zip` next to it, ready to upload to **claude.ai → Settings → Capabilities → Skills** (for the Claude app).

## Quick start

1. **Locate the source profile.** Check the cwd for `STYLE_PROFILE.md`. If absent, ask the user for the path. Read it in full.
2. **Pick a skill name.** Default to `write-like-me`. If that already exists at `~/.claude/skills/write-like-me/`, ask the user for an alternate (e.g. `write-like-<handle>`). Lowercase, hyphens only.
3. **Create the skill directory** at `~/.claude/skills/<name>/`.
4. **Bundle the profile** by copying the source `STYLE_PROFILE.md` into the skill directory. (Offer a symlink alternative if the user wants the skill to track the canonical profile — see Sync below. Note: symlinks won't survive the zip step — see Zip section.)
5. **Write `SKILL.md`** using the template below. Tailor the description's trigger phrases and the register list to whatever the bundled profile actually covers (casual only, casual + technical, fiction, etc.).
6. **Build the upload zip** — see the Zip section below. Produces `~/.claude/skills/<name>.zip`.
7. **Verify** by listing the new directory + zip and confirming the user can invoke it. Report both paths (skill dir for Claude Code, zip for the Claude app upload).

## SKILL.md template for the generated skill

```md
---
name: <skill-name>
description: Write, rewrite, or critique text in <Owner>'s personal voice using the bundled STYLE_PROFILE.md. Use when the user says "<trigger phrases tailored to owner>", or asks for <media types from the profile> that should match their personal writing style. Distinct from the generic `style-profile` skill — this one is pre-loaded with <Owner>'s profile and skips extraction.
---

# <Skill Title>

Apply <Owner>'s writing voice to a draft, generation, or rewrite task. The style profile is bundled at [STYLE_PROFILE.md](STYLE_PROFILE.md).

## Quick start

1. **Read [STYLE_PROFILE.md](STYLE_PROFILE.md)** in full before drafting.
2. **Pick the register** based on what the user is writing:
   <list the registers the profile actually covers — e.g. tweet/reply, long-form, note, EDD>
3. **Draft, then check against the profile's "Things to avoid" list** before returning.

## Workflows

### Generate from scratch
Ask the register if not obvious. Draft per the profile's openings/argument-flow/closings rules.

### Rewrite existing text
Identify what's off (per the profile's avoid list) and fix in-place. Preserve user's intent.

### Critique a draft
Sentence by sentence. Reference the profile section by name.

## Checklist before returning

<extract 5-8 high-signal rules from the profile — e.g. connector vs fragment, vocabulary preferences, formatting taboos, register-specific moves>

## Notes

<carry forward any "Distinctive quirks to preserve" and "Things to avoid" highlights from the profile, plus any user-specific feedback memories about how to handle profile updates>
```

## Customization rules

- **Description triggers** must be specific to the owner. Generic "write like me" is fine, but also include the owner's name or handle if known so it doesn't compete with other personal-voice skills.
- **Register list** must reflect what the profile actually documents. Don't list "EDD" if the profile only covers casual writing.
- **Checklist** should pull the highest-signal, easiest-to-violate rules — not every rule. 5-8 items max.
- **Memory-derived rules**: if the user has feedback memories about the profile (e.g. "don't auto-update STYLE_PROFILE.md"), surface them in the Notes section so the generated skill respects them.

## Zip: produce the Claude app upload artifact

The Claude app (claude.ai) installs skills from a zip archive whose **top-level entry is a single folder** matching the skill name, containing `SKILL.md` (and any bundled resources like `STYLE_PROFILE.md`).

After writing the skill directory, build the zip:

```bash
cd ~/.claude/skills && zip -r <name>.zip <name> -x "*.DS_Store"
```

Notes:
- Run from `~/.claude/skills/` so the archive's top-level entry is the `<name>/` folder, not an absolute path. The Claude app rejects zips that unpack to loose files at root.
- If the user chose the **symlink** option for `STYLE_PROFILE.md`, replace it with a real copy before zipping — `zip` follows symlinks by default but the resulting archive is fragile. Safer: `cp -L` the symlink target into place, zip, then restore the symlink if desired.
- Verify the zip's structure before reporting:

  ```bash
  unzip -l ~/.claude/skills/<name>.zip
  ```

  Expect: `<name>/SKILL.md`, `<name>/STYLE_PROFILE.md`. No extra leading paths, no `__MACOSX/`.

Tell the user how to install it: **claude.ai → Settings → Capabilities → Skills → Upload skill → select the zip**.

## Sync: copy vs symlink

Default to **copy** — the skill works even if the source repo moves or gets deleted, and stays stable.

Offer **symlink** if the user wants the bundled profile to track the canonical source automatically:

```bash
ln -sf <absolute-path-to-source>/STYLE_PROFILE.md ~/.claude/skills/<name>/STYLE_PROFILE.md
```

Trade-off: symlink stays current but breaks if the source is moved or unmounted. Mention both, let the user pick.

## Checklist before returning

- [ ] Source profile read in full (not skimmed)
- [ ] Skill name doesn't collide with existing `~/.claude/skills/` entries
- [ ] Profile bundled (copied or symlinked per user choice)
- [ ] `SKILL.md` description includes specific trigger phrases, not generic "writing"
- [ ] Register list matches what the profile covers
- [ ] Checklist pulls actual rules from the profile, not template placeholders
- [ ] Relevant feedback memories surfaced in Notes
- [ ] Zip built at `~/.claude/skills/<name>.zip` with `<name>/` as the single top-level entry
- [ ] `unzip -l` output confirms `<name>/SKILL.md` and `<name>/STYLE_PROFILE.md`, no `__MACOSX/`
- [ ] Both paths reported to user (skill dir for Claude Code, zip for the Claude app upload)

## Notes

- The generated skill is purely instructional — no scripts needed. The profile + SKILL.md is the entire payload.
- If the source profile has both casual and technical registers (like Iverson's), make sure the generated checklist doesn't conflate them — note which rules apply to which register.
- Don't auto-update the source `STYLE_PROFILE.md` from this packaging step. Bundling is read-only.
