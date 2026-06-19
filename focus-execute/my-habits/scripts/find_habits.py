#!/usr/bin/env python3
"""Find and rank habit cards in an Obsidian vault.

No external dependencies. Designed for pi prompt template `/my-habits`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

SKIP_DIRS = {".git", ".obsidian", ".smart-env", ".smart-connections", ".agents", ".pi", "node_modules"}
DAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def strip_inline_comment(value: str) -> str:
    in_single = False
    in_double = False
    for i, ch in enumerate(value):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            return value[:i].rstrip()
    return value.strip()


def scalar(value: str) -> Any:
    value = strip_inline_comment(value.strip())
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [scalar(part.strip()) for part in inner.split(",")]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].splitlines()
    body = text[end + len("\n---") :].lstrip("\n")
    return parse_frontmatter(raw), body


def parse_frontmatter(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    cards: list[dict[str, Any]] = []

    for raw in lines:
        if not raw.strip():
            continue

        if not raw.startswith(" ") and ":" in raw:
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key

            if key == "habit_cards":
                data[key] = cards
            elif value:
                data[key] = scalar(value)
                current_key = None
            else:
                data[key] = []
            continue

        stripped = raw.strip()
        if stripped.startswith("- ") and current_key:
            item = stripped[2:].strip()
            if current_key == "habit_cards":
                card: dict[str, Any] = {}
                if ":" in item:
                    key, value = item.split(":", 1)
                    card[key.strip()] = scalar(value.strip())
                cards.append(card)
                data["habit_cards"] = cards
            else:
                data.setdefault(current_key, [])
                if isinstance(data[current_key], list):
                    data[current_key].append(scalar(item))
            continue

        if current_key == "habit_cards" and cards and ":" in stripped:
            key, value = stripped.split(":", 1)
            cards[-1][key.strip()] = scalar(value.strip())

    return data


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value]
    return [str(value).strip()]


def is_habit_note(frontmatter: dict[str, Any], body: str) -> bool:
    tags = " ".join(listify(frontmatter.get("tags"))).lower()
    return (
        "habit" in tags
        or "habit_status" in frontmatter
        or "habit_cards" in frontmatter
        or "# Habit Cards" in body
    )


def extract_section(body: str, heading: str) -> str:
    pattern = re.compile(rf"^###\s+{re.escape(heading)}\s*$", re.I | re.M)
    match = pattern.search(body)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^###\s+|^##\s+", body[start:], re.M)
    end = start + next_heading.start() if next_heading else len(body)
    return body[start:end].strip()


def clean_section_text(text: str) -> str:
    text = re.sub(r"^[-*]\s+", "", text, flags=re.M)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.M)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fallback_cards(frontmatter: dict[str, Any], body: str) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    headings = list(re.finditer(r"^##\s+(?:\d+\.\s*)?(.+)$", body, re.M))
    for i, heading in enumerate(headings):
        title = heading.group(1).strip()
        if title.lower() in {"quick view", "weekly review", "later"}:
            continue
        start = heading.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        section = body[start:end]
        cue = clean_section_text(extract_section(section, "Cue"))
        action = clean_section_text(extract_section(section, "Action"))
        if cue or action or "habit" in title.lower():
            cards.append(
                {
                    "id": re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"),
                    "title": title,
                    "status": frontmatter.get("habit_status", "active"),
                    "priority": frontmatter.get("priority", 50),
                    "schedule": frontmatter.get("schedule", ""),
                    "cue": cue,
                    "action": action,
                    "_section": section,
                }
            )
    return cards


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS or part.startswith(".") for part in path.parts):
            continue
        yield path


def status_of(card: dict[str, Any], file_status: str) -> str:
    status = str(card.get("status") or file_status or "active").lower().strip()
    if status in {"archive", "archived", "inactive"}:
        return "archived"
    return "active"


def mentions_today(text: str, today: dt.date) -> tuple[bool, str]:
    lower = text.lower()
    weekday = today.strftime("%A").lower()
    if weekday in lower:
        return True, f"mentions {weekday.title()}"
    if today.isoformat() in lower:
        return True, f"mentions {today.isoformat()}"
    month_day = today.strftime("%B %-d").lower() if hasattr(today, "strftime") else ""
    if month_day and month_day in lower:
        return True, f"mentions {month_day.title()}"
    return False, ""


def schedule_relevance(text: str, today: dt.date) -> tuple[int, list[str]]:
    lower = text.lower()
    score = 0
    reasons: list[str] = []

    matches, reason = mentions_today(text, today)
    if matches:
        score += 200
        reasons.append(reason)

    weekday = today.weekday()  # Monday=0
    if any(term in lower for term in ["daily", "every day", "everyday"]):
        score += 80
        reasons.append("daily")
    if "weekday" in lower and weekday < 5:
        score += 80
        reasons.append("weekday")
    if "weekend" in lower and weekday >= 5:
        score += 80
        reasons.append("weekend")
    if "today" in lower:
        score += 60
        reasons.append("mentions today")

    return score, reasons


def habit_records(root: Path, today: dt.date) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in iter_markdown_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        fm, body = split_frontmatter(text)
        if not is_habit_note(fm, body):
            continue

        cards = fm.get("habit_cards") if isinstance(fm.get("habit_cards"), list) else []
        if not cards:
            cards = fallback_cards(fm, body)

        file_status = str(fm.get("habit_status") or fm.get("status") or "active")
        for card in cards:
            title = str(card.get("title") or card.get("id") or path.stem)
            cue = str(card.get("cue") or "").strip()
            action = str(card.get("action") or "").strip()
            schedule = str(card.get("schedule") or "").strip()
            status = status_of(card, file_status)
            try:
                priority = int(card.get("priority", fm.get("priority", 50)) or 50)
            except ValueError:
                priority = 50

            combined = "\n".join([title, cue, action, schedule, str(card.get("_section", ""))])
            relevance, reasons = schedule_relevance(combined, today)
            score = priority + relevance + (25 if status == "active" else -100)

            records.append(
                {
                    "title": title,
                    "status": status,
                    "priority": priority,
                    "score": score,
                    "schedule": schedule,
                    "cue": cue,
                    "action": action,
                    "why": reasons,
                    "source": str(path),
                }
            )
    return records


def filter_records(records: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    if not args.include_archived:
        status = args.status or "active"
        records = [r for r in records if r["status"] == status]
    elif args.status:
        records = [r for r in records if r["status"] == args.status]

    if args.query:
        q = args.query.lower()
        records = [r for r in records if q in json.dumps(r, ensure_ascii=False).lower()]

    return sorted(records, key=lambda r: (r["score"], r["priority"], r["title"]), reverse=True)


def print_markdown(records: list[dict[str, Any]], today: dt.date) -> None:
    print(f"# My Habits - {today.strftime('%A, %Y-%m-%d')}\n")
    if not records:
        print("No matching habit cards found.")
        return

    for i, r in enumerate(records, 1):
        why = ", ".join(r["why"]) if r["why"] else f"priority {r['priority']}"
        print(f"## {i}. {r['title']}")
        print(f"- **Cue:** {r['cue'] or '(not specified)'}")
        print(f"- **Action:** {r['action'] or '(not specified)'}")
        print(f"- **Status:** {r['status']}")
        if r.get("schedule"):
            print(f"- **Schedule:** {r['schedule']}")
        print(f"- **Why surfaced:** {why}")
        print(f"- **Source:** {r['source']}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Find habit cards in this vault")
    parser.add_argument("--root", default=".", help="Vault root")
    parser.add_argument("--include-archived", action="store_true", help="Include archived habits")
    parser.add_argument("--status", choices=["active", "archived"], help="Filter by status")
    parser.add_argument("--query", help="Filter by text")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    today = dt.date.today()
    records = filter_records(habit_records(Path(args.root), today), args)
    if args.json:
        print(json.dumps(records, indent=2, ensure_ascii=False))
    else:
        print_markdown(records, today)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
