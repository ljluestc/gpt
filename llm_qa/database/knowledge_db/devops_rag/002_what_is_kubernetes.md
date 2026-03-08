# Question
What are the core components of Kubernetes architecture?

# Category
Kubernetes Architecture

# Keywords
kubernetes, control plane, kube-apiserver, etcd, kubelet

# Answer
Kubernetes architecture consists of two main layers: the Control Plane and Worker Nodes.

The Control Plane manages the cluster state and scheduling decisions, while Worker Nodes run application containers.

Control Plane components include:
- kube-apiserver
- etcd
- kube-scheduler
- kube-controller-manager

Node components include:
- kubelet
- kube-proxy
- container runtime

# Key Points
Control Plane responsibilities:
- API access
- cluster state management
- scheduling pods

Node responsibilities:
- running containers
- network proxy
- node monitoring

# Example
User → kubectl → API Server → Scheduler → Node → kubelet → container runtime → Pod running

# Related Concepts
Pods
Deployments
Services
etcd

# Interview Tip
Always mention: API Server → Scheduler → Controller Manager → Worker Node components.
