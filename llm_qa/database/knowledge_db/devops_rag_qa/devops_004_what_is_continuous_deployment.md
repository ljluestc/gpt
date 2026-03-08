# Question
What is Continuous Deployment?

# Category
devops / beginner

# Keywords
continuous deployment, cd, automation

# Answer

Continuous Deployment (CD) means code that passes automated build, tests, and quality gates is automatically deployed to production without manual approval. It is a step beyond Continuous Delivery. Prerequisites include mature testing, release strategy, and rollback. Otherwise, automation can push problems to production faster. Production typically combines canary releases, blue-green deployments, health checks, error rate monitoring, and automatic rollback.

# Key Points

- Automatic deployment to production
- No manual approval step
- Requires strong automated testing
- Often combined with canary and rollback

# Example

Commit → build → tests → security scan → automatic production deployment.

# Related Concepts

Continuous Integration, Continuous Delivery
