#!/usr/bin/env bash
# check.sh — mechanically validate distill-to-skill phase exit gates.
# Usage: ./check.sh <staging-or-skill-dir> [--phase N]
# Exits non-zero on any failure. Prints pass/fail per gate.

set -u

DIR="${1:-}"
ONLY_PHASE="${3:-}"
[[ "${2:-}" == "--phase" ]] || ONLY_PHASE=""

if [[ -z "$DIR" || ! -d "$DIR" ]]; then
  echo "usage: $0 <dir> [--phase N]" >&2
  exit 2
fi

FAIL=0
pass() { printf "  \033[32m✓\033[0m %s\n" "$1"; }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; FAIL=1; }
skip() { printf "  \033[90m–\033[0m %s\n" "$1"; }
phase() { [[ -z "$ONLY_PHASE" || "$ONLY_PHASE" == "$1" ]]; }

# Phase 1: description-brief.md exists
if phase 1; then
  echo "Phase 1 — Intake"
  [[ -f "$DIR/description-brief.md" ]] \
    && pass "description-brief.md exists" \
    || fail "description-brief.md missing — Phase 1 not complete (run description interview)"
fi

# Phase 2: sources.md exists with ≥1 cited line
if phase 2; then
  echo "Phase 2 — Ingest"
  if [[ -f "$DIR/sources.md" ]]; then
    pass "sources.md exists"
    # Count lines that look like citations (URL, ISBN, page ref, or quoted)
    CITES=$(grep -cE 'https?://|ISBN|p\.[0-9]+|^> |"[^"]{20,}"' "$DIR/sources.md" 2>/dev/null || echo 0)
    [[ "$CITES" -ge 1 ]] \
      && pass "sources.md has $CITES citation-shaped line(s)" \
      || fail "sources.md has no URL/ISBN/page-ref/quoted citations"
  else
    fail "sources.md missing"
  fi
fi

# Phase 3: three extraction notes, each ≤10k tokens (~40k chars rough proxy)
if phase 3; then
  echo "Phase 3 — Extract"
  for job in structure application guardrails; do
    F="$DIR/notes-$job.md"
    if [[ -f "$F" ]]; then
      CHARS=$(wc -c < "$F" | tr -d ' ')
      if [[ "$CHARS" -le 40000 ]]; then
        pass "notes-$job.md exists (${CHARS} chars, ~$((CHARS/4)) tokens)"
      else
        fail "notes-$job.md too large (${CHARS} chars, >40k char proxy for 10k tokens)"
      fi
    else
      fail "notes-$job.md missing"
    fi
  done
fi

# Phase 4: SKILL.md exists and ≤100 lines
if phase 4; then
  echo "Phase 4 — Synthesize"
  if [[ -f "$DIR/SKILL.md" ]]; then
    LINES=$(wc -l < "$DIR/SKILL.md" | tr -d ' ')
    if [[ "$LINES" -le 100 ]]; then
      pass "SKILL.md is $LINES lines (≤100)"
    else
      fail "SKILL.md is $LINES lines — over the 100-line cap (push section detail to references/)"
    fi
    # Description sanity check
    grep -q "Use when" "$DIR/SKILL.md" \
      && pass "description contains 'Use when' trigger phrase" \
      || fail "description missing 'Use when' trigger phrase"
  else
    fail "SKILL.md missing"
  fi
fi

# Phase 5: every references/*.md linked from SKILL.md resolves
if phase 5; then
  echo "Phase 5 — Expand"
  if [[ -f "$DIR/SKILL.md" ]]; then
    BROKEN=0
    # Extract markdown links to references/*.md
    while IFS= read -r REF; do
      if [[ ! -f "$DIR/$REF" ]]; then
        fail "broken link: $REF (referenced in SKILL.md, file missing)"
        BROKEN=$((BROKEN+1))
      fi
    done < <(grep -oE '\(references/[a-z0-9_-]+\.md\)' "$DIR/SKILL.md" 2>/dev/null | tr -d '()' | sort -u)
    [[ "$BROKEN" -eq 0 ]] && pass "all references/*.md links resolve"
  else
    skip "SKILL.md missing — cannot check references"
  fi
fi

# Phase 6: rubric scoring (cannot automate semantic judgment)
if phase 6; then
  echo "Phase 6 — Review"
  skip "rubric scoring requires human/agent judgment; see references/review-rubric.md"
fi

echo
if [[ "$FAIL" -eq 0 ]]; then
  printf "\033[32mAll checked gates passed.\033[0m\n"
  exit 0
else
  printf "\033[31mOne or more gates failed.\033[0m Fix and re-run.\n"
  exit 1
fi
