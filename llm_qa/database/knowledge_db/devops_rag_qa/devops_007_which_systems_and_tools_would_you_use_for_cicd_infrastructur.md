# Question
Which systems and tools would you use for CI/CD, infrastructure, config management, monitoring, logging, code review, coverage, and testing?

# Category
devops / beginner

# Keywords
devops, tools, cicd, monitoring

# Answer

CI/CD: Jenkins, CircleCI, Travis, GitHub Actions; Infrastructure: Terraform, CloudFormation; Config management: Ansible, Puppet, Chef; Monitoring: Prometheus, Nagios; Logging: Logstash, Graylog, Fluentd; Code review: Gerrit, Review Board, GitHub/GitLab PR; Coverage: Cobertura, Clover, JaCoCo, coverage.py; Testing: Robot, Serenity, Gauge. In interviews, add reasoning: e.g., Jenkins/GitHub Actions for CI/CD; Terraform for IaC; Ansible for config; Prometheus + Alertmanager + Grafana for monitoring; Fluent Bit/Fluentd + Elasticsearch for logs; JaCoCo/coverage.py for coverage; unit/integration/e2e for tests.

# Key Points

- CI/CD: Jenkins, GitHub Actions
- IaC: Terraform
- Config: Ansible
- Monitoring: Prometheus + Grafana

# Example

Typical stack: GitHub Actions + Terraform + Ansible + Prometheus + Grafana + Fluent Bit.

# Related Concepts

Automation, Infrastructure as Code, Observability
