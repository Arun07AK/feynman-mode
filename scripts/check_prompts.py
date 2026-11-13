#!/usr/bin/env python3
"""Check built thread prompts.

Usage: python3 check_prompts.py <folder of .txt prompts> [--template FILE] [--base URL]

Each .txt file is one full prompt: the scope block, then the teaching template.
Errors make the exit code 1. Warnings do not.
"""
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import quote

HEADINGS = ["WHAT TO TEACH", "WHERE TO START", "WHEN THE TOPIC IS DONE"]
BLOCK_MAX = 1900
URL_MAX = 16000


def numbered(text):
    return len(re.findall(r"^\s*\d+\.\s", text, flags=re.M))


def check(prompt, template, base):
    errors, warnings = [], []
    at = prompt.find(template)
    if at < 0:
        errors.append("teaching template is missing or not word for word")
        block = prompt
    else:
        block = prompt[:at].strip()
        if prompt[at + len(template):].strip():
            errors.append("text found after the teaching template")

    positions = [block.find(h) for h in HEADINGS]
    for heading, pos in zip(HEADINGS, positions):
        if pos < 0:
            errors.append(f"heading missing: {heading}")
    if all(p >= 0 for p in positions):
        if positions != sorted(positions):
            errors.append("headings are out of order")
        teach = block[positions[0]:positions[1]]
        done = block[positions[2]:]
        n_teach, n_done = numbered(teach), numbered(done)
        if n_teach == 0:
            errors.append("no numbered concepts under WHAT TO TEACH")
        elif not 4 <= n_teach <= 8:
            warnings.append(f"{n_teach} concepts (usual range is 4 to 8)")
        if n_done == 0:
            errors.append("no numbered items under WHEN THE TOPIC IS DONE")
        elif not 2 <= n_done <= 4:
            warnings.append(f"{n_done} done items (usual range is 2 to 4)")
        if "complete, and stop" not in done:
            warnings.append("done section does not end with the stop instruction")

    if len(block) > BLOCK_MAX:
        errors.append(f"scope block is {len(block)} characters (limit {BLOCK_MAX})")
    url_len = len(base) + len(quote(prompt, safe=""))
    if url_len > URL_MAX:
        errors.append(f"launch URL is {url_len} characters (limit {URL_MAX})")
    return errors, warnings, len(block), url_len


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--template", default=str(here.parent / "assets" / "teaching-template.txt"))
    ap.add_argument("--base", default="https://chatgpt.com/?q=")
    args = ap.parse_args()

    template = Path(args.template).read_text(encoding="utf-8").strip()
    files = sorted(Path(args.folder).glob("*.txt"))
    if not files:
        sys.exit(f"no .txt prompts in {args.folder}")

    failed = 0
    for f in files:
        errors, warnings, block_len, url_len = check(
            f.read_text(encoding="utf-8").strip(), template, args.base)
        status = "FAIL" if errors else "ok"
        failed += bool(errors)
        print(f"{status:4}  {f.name}  block {block_len}  url {url_len}")
        for e in errors:
            print(f"      error: {e}")
        for w in warnings:
            print(f"      warning: {w}")
    print(f"\n{len(files) - failed} of {len(files)} prompts pass")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
