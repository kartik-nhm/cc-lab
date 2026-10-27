# Kubernetes Lab Execution Record

Lab based on: `Kubernetes_Lab_on_Windows_Manual.pdf`  
Execution Date: 2026-10-27

---

## Part 1 & 2: Environment & Tool Verification

- **Docker Version**: 29.8.0 (Docker Desktop Linux engine running)
- **kubectl Version**: v1.36.1
- **kind Version**: v0.33.0
- **Docker Hello-World Test**: PASSED

---

## Part 3: Cluster Configuration

- **Lab Folder**: `k8s-lab` (Git initialized)
- **Configuration File**: [`kind-config.yaml`](./kind-config.yaml)
  ```yaml
  kind: Cluster
  apiVersion: kind.x-k8s.io/v1alpha4
  nodes:
  - role: control-plane
  - role: worker
  - role: worker
  ```

---

## Part 4: Three-Node Cluster Build

- **Command**: `kind create cluster --config kind-config.yaml`
- **Context Set**: `kind-kind`
- **Node Status**:
  ```text
  NAME                 STATUS   ROLES           AGE   VERSION
  kind-control-plane   Ready    control-plane   32s   v1.37.0
  kind-worker          Ready    <none>          18s   v1.37.0
  kind-worker2         Ready    <none>          18s   v1.37.0
  ```
- **Containers**:
  - `kind-control-plane`
  - `kind-worker`
  - `kind-worker2`
- **System Pods**:
  - `coredns`, `etcd`, `kindnet`, `kube-apiserver`, `kube-controller-manager`, `kube-proxy`, `kube-scheduler` all `Running`.

---

## Part 5: Deploy NGINX Web Application

- **Command**: `kubectl create deployment web --image=nginx --replicas=3`
- **Replicas Status**: `3/3 Ready`
- **Pod Distribution**:
  - `web-5fc9f4bf66-4tr8n`: `kind-worker` (IP: 10.244.2.2)
  - `web-5fc9f4bf66-8wgsr`: `kind-worker` (IP: 10.244.2.3)
  - `web-5fc9f4bf66-k4mmv`: `kind-worker2` (IP: 10.244.1.2)

---

## Part 6: Scale the Pods and Test Self-Healing

1. **Scale Replicas to 6**:
   - `kubectl scale deployment web --replicas=6`
   - Distribution:
     - `kind-worker`: 3 Pods (`4tr8n`, `8wgsr`, `qsp52`)
     - `kind-worker2`: 3 Pods (`2vdxw`, `cfcrp`, `k4mmv`)
2. **Self-Healing Test**:
   - Deleted Pod: `web-5fc9f4bf66-2vdxw` (`kubectl delete pod web-5fc9f4bf66-2vdxw`)
   - Outcome: ReplicaSet detected 5 running pods and immediately scheduled replacement pod `web-5fc9f4bf66-n9t24` on `kind-worker2` (status: `Running`, age: 9s). Total running pods remained at 6.
