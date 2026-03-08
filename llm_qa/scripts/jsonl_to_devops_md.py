#!/usr/bin/env python3
"""Convert DevOps RAG JSONL to markdown files for llm_qa ingestion.

Usage:
    python scripts/jsonl_to_devops_md.py data/devops_rag_answered.jsonl -o database/knowledge_db/devops_rag
"""

import argparse
import json
import re
from pathlib import Path


def slug(s: str) -> str:
    """Create filesystem-safe slug from string."""
    s = re.sub(r"[^\w\s-]", "", s.lower())
    return re.sub(r"[-\s]+", "_", s).strip("_")[:60]


def entry_to_md(entry: dict) -> str:
    """Convert one JSONL entry to markdown."""
    parts = []
    q = entry.get("question") or entry.get("question_zh", "")
    if not q:
        return ""
    parts.append(f"# Question\n{q}\n")
    cat = entry.get("category", "DevOps")
    parts.append(f"# Category\n{cat}\n")
    kw = entry.get("keywords") or entry.get("keywords_zh", [])
    if isinstance(kw, list):
        kw = ", ".join(str(k) for k in kw)
    parts.append(f"# Keywords\n{kw}\n")
    ans = entry.get("detailed_answer") or entry.get("detailed_answer_zh") or entry.get("short_answer") or entry.get("short_answer_zh", "")
    if ans:
        parts.append(f"# Answer\n{ans}\n")
    kp = entry.get("key_points") or entry.get("key_points_zh", [])
    if isinstance(kp, list) and kp:
        parts.append("# Key Points\n" + "\n".join(f"* {p}" for p in kp) + "\n")
    elif isinstance(kp, str) and kp:
        parts.append(f"# Key Points\n{kp}\n")
    ex = entry.get("example") or entry.get("example_zh", "")
    if ex:
        parts.append(f"# Example\n{ex}\n")
    rel = entry.get("related_topics") or entry.get("related_concepts", [])
    if isinstance(rel, list) and rel:
        parts.append("# Related Concepts\n" + "\n".join(str(r) for r in rel) + "\n")
    src = entry.get("source", "")
    if src:
        parts.append(f"# Source\n{src}\n")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Convert DevOps JSONL to markdown")
    parser.add_argument("input", type=Path, help="Input JSONL file")
    parser.add_argument("-o", "--output", type=Path, default=Path("database/knowledge_db/devops_rag"), help="Output directory")
    parser.add_argument("--prefix", default="", help="Filename prefix (e.g. devops_)")
    args = parser.parse_args()

    out_dir = args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    with open(args.input, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            md = entry_to_md(entry)
            if not md:
                continue
            eid = entry.get("id", f"q{i+1:03d}")
            q = entry.get("question") or entry.get("question_zh", "question")
            fname = f"{args.prefix}{eid}_{slug(q)}.md"
            out_path = out_dir / fname
            out_path.write_text(md, encoding="utf-8")
            count += 1

    print(f"Wrote {count} markdown files to {out_dir}")


if __name__ == "__main__":
    main()
