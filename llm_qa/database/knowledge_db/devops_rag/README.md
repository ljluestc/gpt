# DevOps RAG Knowledge Base

DevOps / Kubernetes / Cloud interview Q&A in RAG-ready markdown format.

## Format

Each `.md` file contains:
- `# Question` — the interview question
- `# Category` — topic (DevOps, Kubernetes, Docker, etc.)
- `# Keywords` — for retrieval
- `# Answer` — detailed answer
- `# Key Points` — bullet summary
- `# Example` — code or workflow example
- `# Related Concepts` — follow-up topics
- `# Interview Tip` — practical advice

## Ingestion

See `doc/DevOps_RAG_DATASET.md` for full ingestion instructions.

Quick start:
```bash
cd llm_qa
python -c "
from database.create_db import create_db
create_db(
    files='database/knowledge_db/devops_rag',
    persist_directory='database/vector_devops_db',
    embeddings='zhipuai'
)
"
```

## Source

Based on [aliaskov/devops-interview-questions](https://github.com/aliaskov/devops-interview-questions).
