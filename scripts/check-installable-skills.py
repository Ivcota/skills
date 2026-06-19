#!/usr/bin/env python3
"""Validate categorized skill install paths."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "build-products",
    "learn-think",
    "focus-execute",
    "write-communicate",
    "win-customers",
    "run-business",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def skill_name(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    match = re.search(r"^name:\s*([^\n]+)\s*$", text, re.MULTILINE)
    if not match:
        fail(f"missing frontmatter name in {skill_file.relative_to(ROOT)}")
    return match.group(1).strip().strip('"\'')


def main() -> int:
    root_skill_files = sorted(
        p for p in ROOT.glob("*/SKILL.md") if p.parent.name not in CATEGORIES
    )
    if root_skill_files:
        fail(
            "root-level SKILL.md files remain: "
            + ", ".join(str(p.relative_to(ROOT)) for p in root_skill_files)
        )

    skill_files = sorted(p for category in CATEGORIES for p in (ROOT / category).glob("*/SKILL.md"))
    if not skill_files:
        fail("no categorized skills found")

    names = [skill_name(p) for p in skill_files]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        fail("duplicate skill frontmatter names: " + ", ".join(duplicates))

    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    marketplace_paths = []
    for plugin in marketplace.get("plugins", []):
        for path in plugin.get("skills", []):
            normalized = path.removeprefix("./")
            marketplace_paths.append(normalized)
            if not (ROOT / normalized / "SKILL.md").is_file():
                fail(f"marketplace path missing SKILL.md: {path}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_paths = re.findall(r"npx skills@latest add Ivcota/skills/([^\s`]+)", readme)
    concrete_readme_paths = [p for p in readme_paths if not p.startswith("<")]
    for path in concrete_readme_paths:
        if not (ROOT / path / "SKILL.md").is_file():
            fail(f"README install path missing SKILL.md: {path}")

    categorized_skill_paths = sorted(str(p.parent.relative_to(ROOT)) for p in skill_files)
    readme_missing = sorted(set(categorized_skill_paths) - set(concrete_readme_paths))
    if readme_missing:
        fail("categorized skills missing README install command: " + ", ".join(readme_missing))

    marketplace_missing = sorted(set(categorized_skill_paths) - set(marketplace_paths))
    if marketplace_missing:
        fail("categorized skills missing marketplace entry: " + ", ".join(marketplace_missing))

    print(f"OK: {len(skill_files)} categorized skills are installable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
