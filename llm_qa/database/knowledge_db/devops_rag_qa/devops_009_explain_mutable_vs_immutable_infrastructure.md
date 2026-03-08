# Question
Explain mutable vs. immutable infrastructure

# Category
devops / beginner

# Keywords
infrastructure, mutable, immutable, iac

# Answer

Mutable infrastructure: patch and modify config on existing servers. Ansible, Puppet, Chef lean toward mutable. Immutable infrastructure: create new instances to replace old ones on each change. Terraform is an example of immutable thinking. Mutable is flexible and quick to start but prone to config drift. Immutable favors consistency, rollback, and audit because 'server broken = rebuild, don't patch.' Modern cloud-native often prefers immutable infrastructure—images, containers, ASGs, and Kubernetes rolling updates.

# Key Points

- Mutable: patch in place
- Immutable: replace on change
- Immutable reduces drift
- Cloud-native favors immutable

# Example

Mutable: SSH and edit config. Immutable: new image, new container, roll forward.

# Related Concepts

Infrastructure as Code, Configuration Drift, Containers
