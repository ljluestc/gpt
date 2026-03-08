# Question
What is your view on CI/CD best practices?

# Category
devops / beginner

# Keywords
ci/cd, best practices, automation

# Answer

CI/CD best practices include: small commits, automated validation, pipeline-as-code, immutable artifacts, consistent environments, observability, and rollback. More concretely: every commit triggers build and tests; Jenkinsfile/GitHub Actions/CI config lives in version control; one artifact is reused across dev/staging/prod; containers or IaC ensure environment consistency; gates for security scans, coverage, and policy checks; support for canary and rollback on release; and monitoring of pipeline metrics (build time, failure rate, deployment success).

# Key Points

- Pipeline-as-code
- Immutable artifacts
- Environment consistency
- Gate checks and rollback

# Example

Jenkinsfile in repo, Docker image built once, Terraform for environments.

# Related Concepts

Automation, Infrastructure as Code, Monitoring
