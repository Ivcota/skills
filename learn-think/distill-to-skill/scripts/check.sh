#!/usr/bin/env bash
# Validate final deliverables. Requires Python 3; semantic review is separate.
set -eu
if [[ $# -ne 1 || ! -d "$1" ]]; then
  echo "usage: $0 <output-directory>" >&2
  exit 2
fi
python3 - "$1" <<'PY'
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]).resolve()
errors = []
def fail(message):
    errors.append(message)
    print(f'FAIL: {message}')

required = ['SKILL.md', 'sources.md', 'references/case-studies.md', 'references/checklist.md']
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text().strip():
        fail(f'{name} missing or empty')

skill = root / 'SKILL.md'
if skill.is_file():
    text = skill.read_text()
    if len(text.splitlines()) > 100:
        fail('SKILL.md exceeds 100 lines')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not front:
        fail('SKILL.md requires YAML frontmatter')
    else:
        metadata = front.group(1)
        if not re.search(r'^name:\s*[a-z0-9]+(?:-[a-z0-9]+)*\s*$', metadata, re.M):
            fail('frontmatter requires a kebab-case name')
        description = re.search(r'^description:[ \t]*(.*(?:\n[ \t]+[^\n]*)*)', metadata, re.M)
        value = description.group(1).strip() if description else ''
        value = re.sub(r'^[|>][-+]?[ \t]*\n', '', value)
        value = ' '.join(line.strip() for line in value.splitlines()).strip('\'"')
        if 'Use when' not in value:
            fail('frontmatter description requires Use when triggers')
        if len(value) > 1024:
            fail('description exceeds 1024 characters')
    targets = re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
    paths = {target.split('#')[0] for target in targets}
    for name in required[1:]:
        if name not in paths:
            fail(f'SKILL.md must link {name}')
    sections = {name for name in paths if name.startswith('references/') and name.endswith('.md')} - set(required[2:])
    if not sections:
        fail('SKILL.md must link at least one framework reference')

# Check local file links in every final Markdown artifact, including aggregate files.
# Heading anchors are not validated; source locations may be plain text in sources.md.
for path in sorted(root.rglob('*.md')):
    content = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content):
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        local = target.split('#')[0]
        resolved = (path.parent / local).resolve()
        if not resolved.is_relative_to(root):
            fail(f'{path.relative_to(root)}: nonportable local link {target}')
        elif not resolved.is_file() or not resolved.stat().st_size:
            fail(f'{path.relative_to(root)}: missing or empty link target {target}')

if errors:
    print(f'{len(errors)} structural issue(s).')
    sys.exit(1)
print('Final artifact checks passed. Source fidelity and coverage require semantic review.')
PY
