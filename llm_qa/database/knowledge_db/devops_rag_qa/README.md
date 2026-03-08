# DevOps RAG Q&A — Markdown for llm_qa Ingestion

DevOps interview Q&A in markdown format, ready for ingestion into the llm_qa RAG pipeline.

---

## Format

Each `.md` file follows this structure (compatible with `UnstructuredMarkdownLoader`):

```markdown
# Question
What is DevOps?

# Category
devops / beginner

# Keywords
devops, ci/cd, automation, collaboration

# Answer

DevOps integrates development, testing, operations...

# Key Points

- Connects development, testing, operations
- Emphasizes collaboration and automation

# Example

Typical DevOps workflow: Developer commit → CI build...

# Related Concepts

CI/CD, Infrastructure as Code, Monitoring
```

---

## Ingestion

### Option 1: Python

```bash
cd llm_qa
python -c "
from database.create_db import create_db
create_db('database/knowledge_db/devops_rag_qa', persist_directory='database/vector_devops_db')
"
```

### Option 2: Gradio UI

In the "知识库" tab, set the path to `database/knowledge_db/devops_rag_qa`.

### Option 3: Full knowledge_db

The `create_db` loader walks `database/knowledge_db` by default. Ensure `devops_rag_qa/` is under that path.

---

## Regenerating from JSONL

```bash
cd llm_qa
python scripts/jsonl_to_markdown.py \
  -i /path/to/devops_rag_answered_full_405_regenerated.jsonl \
  -o database/knowledge_db/devops_rag_qa/
```

---

## Source

- [devops-interview-questions](https://github.com/aliaskov/devops-interview-questions)
- [RAG devops_rag_kb](https://github.com/ljluestc/RAG) — kubernetes_rag/data/devops_rag_kb/
