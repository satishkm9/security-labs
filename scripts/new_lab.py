#!/usr/bin/env python3
"""Create a draft lab entry and add it to the Markdown index. No dependencies."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {"learning": "learning-note.md", "soc": "soc-report.md", "vapt": "vapt-report.md"}


def slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise argparse.ArgumentTypeError("Use lowercase letters, numbers and single hyphens.")
    return value


def iso_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use a valid YYYY-MM-DD date.") from exc


def title(value: str) -> str:
    if not value.strip() or any(char in value for char in "\r\n"):
        raise argparse.ArgumentTypeError("Supply a non-empty, single-line title.")
    return value.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", choices=["soc", "vapt", "dfir", "foundations"], required=True)
    parser.add_argument("--platform", type=slug, required=True, help="e.g. tryhackme, hackthebox, homelab")
    parser.add_argument("--slug", type=slug, required=True, help="Short topic name for the folder")
    parser.add_argument("--title", type=title, required=True)
    parser.add_argument("--type", choices=list(TEMPLATES), default="learning", help="Default: learning")
    parser.add_argument("--date", type=iso_date, default=date.today().isoformat())
    args = parser.parse_args()

    if args.platform == "tryhackme" and args.type != "learning":
        parser.error("Use a learning reflection for TryHackMe. For a detailed public SOC/VAPT report, recreate the concept in your own homelab and use --platform homelab.")

    target = ROOT / "labs" / args.track / args.platform / f"{args.date}-{args.slug}"
    if target.exists():
        parser.error(f"Entry already exists; no files changed: {target}")

    template = (ROOT / "templates" / TEMPLATES[args.type]).read_text(encoding="utf-8")
    # Escape characters that would create Markdown links, HTML, or a table delimiter.
    safe_title = args.title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for char in ("\\", "[", "]", "|", "*", "_", "`", "#"):
        safe_title = safe_title.replace(char, "\\" + char)
    for key, value in {"TITLE": safe_title, "DATE": args.date, "TRACK": args.track.upper(), "PLATFORM": args.platform}.items():
        template = template.replace("{{" + key + "}}", value)

    index = ROOT / "labs" / "INDEX.md"
    old = index.read_text(encoding="utf-8")
    link = target.relative_to(ROOT / "labs").as_posix() + "/README.md"
    row = f"| {args.date} | {args.track.upper()} | {args.platform} | [{safe_title}]({link}) | Draft |\n"
    updated = old.replace("No entries have been added yet. The first lab can be created with `scripts/new_lab.py` or by copying a template.", "Entries are listed below. Status reflects the report, not a certification or employment record.")
    target.mkdir(parents=True)
    try:
        (target / "README.md").write_text(template, encoding="utf-8")
        (target / "evidence").mkdir()
        (target / "evidence" / ".gitkeep").touch()
        index.write_text(updated.rstrip() + "\n" + row, encoding="utf-8")
    except Exception:
        # Restore the index if writing failed, and remove this newly created entry.
        index.write_text(old, encoding="utf-8")
        import shutil
        shutil.rmtree(target)
        raise
    print(f"Created draft: {target / 'README.md'}")
    print("Fill in your observations and review publication rights before publishing.")


if __name__ == "__main__":
    main()
