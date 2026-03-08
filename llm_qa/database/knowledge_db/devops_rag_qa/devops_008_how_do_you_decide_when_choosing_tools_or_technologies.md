# Question
How do you decide when choosing tools or technologies?

# Category
devops / beginner

# Keywords
devops, tool selection, architecture

# Answer

Evaluation dimensions include: maturity vs. cutting-edge, community size, and architecture (agent vs. agentless, master vs. masterless). In interviews: first assess whether the problem really needs the tool; then whether the team can operate it; then ecosystem maturity, scalability, security, integration, learning curve, and TCO. Example: Ansible's agentless model fits quick onboarding; Terraform's declarative model fits IaC; Jenkins has strong plugins but governance cost. Choose what fits the organization's stage, not what is trendiest.

# Key Points

- Problem fit first
- Team ability to operate
- Ecosystem and integration
- TCO over trendiness

# Example

Ansible for agentless config; Terraform for IaC; Jenkins for plugin-rich CI.

# Related Concepts

Automation, Infrastructure as Code
