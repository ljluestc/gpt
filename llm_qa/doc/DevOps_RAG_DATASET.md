# DevOps RAG Dataset — Production-Ready Format for llm_qa Ingestion

This document describes the **DevOps RAG dataset structure** and how to ingest it into the llm_qa Chroma vector database for interview prep and technical Q&A.

---

## 1. Recommended Folder Structure

Use **one document per question** under `database/knowledge_db/devops_rag/`:

```
database/knowledge_db/
├── cpp_txt/           # Existing C++ knowledge
├── cpp_md/            # Existing C++ markdown
└── devops_rag/        # DevOps / Kubernetes / Cloud Q&A
    ├── 001_what_is_devops.md
    ├── 002_what_is_kubernetes.md
    ├── 003_continuous_integration.md
    ├── 004_continuous_delivery.md
    ├── 005_continuous_deployment.md
    ├── kubernetes/
    │   ├── 101_k8s_architecture.md
    │   ├── 102_kube_apiserver.md
    │   └── 103_kube_scheduler.md
    ├── docker/
    │   ├── 201_docker_architecture.md
    │   └── 202_docker_vs_vm.md
    └── cloud/
        ├── 301_iaas_paas_saas.md
        └── 302_load_balancer.md
```

**Benefits:**
- Smaller chunks
- Better vector retrieval
- Easier metadata filtering by category

---

## 2. Document Format (Markdown)

Each file follows this structure:

```markdown
# Question
What is DevOps?

# Category
DevOps Fundamentals

# Keywords
devops, ci/cd, automation, collaboration

# Answer
DevOps is a set of practices and cultural philosophies that combine software development (Dev) and IT operations (Ops) to shorten the software development lifecycle while delivering high-quality software.

DevOps focuses on automation, continuous integration, continuous delivery, infrastructure as code, and monitoring.

# Key Points
* DevOps integrates development and operations teams
* Automation of build, test, and deployment pipelines
* Continuous delivery of software
* Infrastructure automation
* Monitoring and observability

# Example
Typical DevOps workflow:
Developer commit → CI pipeline → Automated tests → Build artifact → Deploy to Kubernetes → Monitor with Prometheus

# Related Concepts
Continuous Integration
Continuous Delivery
Infrastructure as Code

# Interview Tip
DevOps is not only tools — it is primarily a **culture of collaboration and automation**.
```

---

## 3. Ingestion into llm_qa

The existing `create_db.py` supports markdown via `UnstructuredMarkdownLoader`. To ingest the DevOps RAG dataset:

### Option A: Add devops_rag to default path

Edit `gradio_gui.py` or `create_db.py` to include `database/knowledge_db/devops_rag` in the file path when creating the vector DB.

### Option B: Create DB with multiple paths

```python
from database.create_db import create_db

# Include both C++ and DevOps knowledge
create_db(
    files=["database/knowledge_db/cpp_md", "database/knowledge_db/devops_rag"],
    persist_directory="database/vector_devops_db",
    embeddings="zhipuai"  # or "openai"
)
```

### Option C: CLI

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

---

## 4. Chunking Settings (Recommended for DevOps)

In `create_db.py`, `RecursiveCharacterTextSplitter` uses:

- `chunk_size = 500` — suitable for structured Q&A
- `chunk_overlap = 150` — preserves context across chunks

For DevOps docs, 400–700 tokens per chunk works well because answers are structured and smaller chunks improve retrieval accuracy.

---

## 5. Scaling the Dataset

For a full DevOps knowledge base, include:

| Category    | Topics                                      |
|------------|---------------------------------------------|
| DevOps     | CI/CD, GitOps, Observability, SRE          |
| Kubernetes | architecture, scheduling, networking, storage |
| Docker     | container runtime, image layers, security  |
| Cloud      | AWS, load balancing, autoscaling           |
| Linux      | namespaces, cgroups, process management    |
| Networking | TCP/IP, DNS, load balancing                |

**Target size:** 400–800 questions for interview training RAG.

---

## 6. JSONL Alternative Format

For bulk import from JSON/JSONL (e.g. from aliaskov/devops-interview-questions), use this schema:

```json
{
  "id": "devops_001",
  "category": "devops",
  "difficulty": "beginner",
  "question": "What is DevOps?",
  "short_answer": "DevOps combines Dev and Ops for faster delivery.",
  "detailed_answer": "...",
  "key_points": ["...", "..."],
  "example": "...",
  "related_topics": ["CI", "CD"],
  "source": "https://github.com/aliaskov/devops-interview-questions"
}
```

Convert JSONL to markdown with a script, then ingest via `create_db.py`, or add a JSONL loader to `create_db.py`.

---

## 7. RAG Chat UI (Tiny-A2A)

The RAG Chat page at `http://localhost:12000/rag` queries the Kubernetes RAG API (`POST /query`). To use llm_qa as the backend instead:

1. Expose llm_qa via FastAPI with a `/query` endpoint.
2. Set `RAG_API_URL` to that API URL.
3. The UI expects: `{"answer": "...", "citations": [{"source": "...", "passage": "..."}]}`.

---

## 8. References

- [aliaskov/devops-interview-questions](https://github.com/aliaskov/devops-interview-questions) — 413 DevOps interview questions
- [wdndev/tiny-a2a](https://github.com/wdndev/tiny-a2a) — A2A UI with RAG Chat page
- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Chroma Vector Store](https://docs.trychroma.com/)
