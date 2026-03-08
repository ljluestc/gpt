# Question
What delivery methods do you use for software?

# Category
devops / beginner

# Keywords
delivery, artifact, packaging, container

# Answer

Typical delivery methods: archive (e.g., tar), OS package (e.g., RPM, deb), and image (VM or container image). Archive: simple distribution but weak dependency management and install consistency. OS package: good for traditional servers; easier install, upgrade, uninstall. Image delivery: best for modern cloud-native and scale; runtime dependencies are baked in; better for consistency and elasticity. Many teams move toward 'artifact repository + container image + orchestration platform.'

# Key Points

- Archive: simple, weak dependency
- OS package: traditional servers
- Image: cloud-native, consistency

# Example

Modern: artifact → Docker image → registry → Kubernetes deployment.

# Related Concepts

Containers, CI/CD, Artifact Management
