# Question
What are DevOps anti-patterns?

# Category
devops / beginner

# Keywords
devops, anti-patterns, silos, manual deployment

# Answer

DevOps anti-patterns are practices that appear to adopt DevOps but do not change delivery. Common examples: introducing Jenkins, Docker, or Kubernetes without changing org structure—development, testing, and operations remain siloed and releases remain manual. Typical anti-patterns include creating a separate DevOps team instead of integrating; manual production config changes causing drift; infrequent large releases; pushing automated deployment without automated tests; prioritizing speed over monitoring, rollback, and stability; and relying on hero culture instead of platform capabilities.

# Key Points

- Tools without process change
- Separate DevOps team creates new silos
- Manual config changes cause drift
- Infrequent releases and lack of automation

# Example

Bad: Developers hand off to ops, who manually deploy. Good: Shared ownership, automated pipelines, and platform self-service.

# Related Concepts

CI/CD, Configuration Drift, Automation
