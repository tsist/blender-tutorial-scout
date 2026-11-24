# SPDX-License-Identifier: GPL-3.0-or-later
"""Verify AGENTS.md XML validity, skill frontmatter, local markdown links, Python syntax, and zero private leaks."""
from __future__ import annotations

import ast
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]\n]+\]\(([^\n)]+)\)")
PRIVACY_PATTERNS = [
    re.compile("173" + "99"),
    re.compile(r"(?i)(?<![A-Za-z0-9_])[CF]:[/\\]+(?:Users|Blender)"),
    re.compile(r"wm-20\d\d-\d\d-\d\d", re.I),
    re.compile(r"runtime[/\\]+audit[/\\]+(?!<)[a-zA-Z0-9_.-]", re.I),
    re.compile(r"\.dsh[/\\]+memory-lancedb-pro", re.I),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"(?<![A-Za-z0-9_-])(?:sk-(?:proj-|svcacct-)?[A-Za-z0-9]{24,}|(?:AKIA|ASIA)[A-Z0-9]{16})"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def verify() -> dict:
    errors: list[str] = []
    checked_files = 0
    checked_links = 0

    agents_md = ROOT / "AGENTS.md"
    if agents_md.is_file():
        try:
            ET.fromstring(agents_md.read_text(encoding="utf-8"))
        except ET.ParseError as exc:
            errors.append(f"AGENTS.md invalid XML: {exc}")

    skip = {".git", "__pycache__", "dist", "test-output", ".venv"}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or (set(path.relative_to(ROOT).parts) & skip):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in {".pyc", ".blend", ".blend1", ".exe", ".dll"}:
            errors.append(f"forbidden binary: {rel}")
            continue
        if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".json", ".ps1", ".txt"}:
            continue
        checked_files += 1
        text = path.read_text(encoding="utf-8-sig")
        if path.name != "verify_public_hygiene.py":
            for pat in PRIVACY_PATTERNS:
                m = pat.search(text)
                if m:
                    errors.append(f"privacy pattern in {rel}: {m.group(0)!r}")
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=rel)
            except SyntaxError as exc:
                errors.append(f"python syntax error in {rel}: {exc}")
        if path.suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"json parse error in {rel}: {exc}")
        if path.suffix == ".md":
            for match in LINK_RE.finditer(text):
                target = match.group(1).strip().strip("<>").split()[0]
                if not target or target.startswith("#") or urlsplit(target).scheme in {"http", "https", "mailto"}:
                    continue
                if urlsplit(target).scheme:
                    errors.append(f"unsupported link scheme in {rel}: {target}")
                    continue
                local_path = unquote(target.split("#", 1)[0])
                if not local_path:
                    continue
                resolved = (path.parent / local_path).resolve()
                checked_links += 1
                if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                    errors.append(f"broken relative link in {rel}: {target}")

    for skill_md in sorted(ROOT.rglob("SKILL.md")):
        txt = skill_md.read_text(encoding="utf-8-sig")
        if not txt.startswith("---\n") or not re.search(r"^name:\s+[a-z0-9-]+\s*$", txt, re.M):
            errors.append(f"invalid frontmatter in {skill_md.relative_to(ROOT).as_posix()}")

    return {
        "ok": not errors,
        "checked_files": checked_files,
        "checked_links": checked_links,
        "errors": errors,
    }


if __name__ == "__main__":
    res = verify()
    print(json.dumps(res, ensure_ascii=False, indent=2))
    sys.exit(0 if res["ok"] else 1)
