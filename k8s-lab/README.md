# Kubernetes Lab (3-Node Kind Cluster)

This repository contains the configuration, manifests, and documentation for setting up a local 3-node Kubernetes cluster using [kind](https://kind.sigs.k8s.io/) and testing deployments, scaling, and self-healing.

Based on the **Kubernetes Lab Manual**.

---

## Architecture

- **Control Plane**: 1 node (`kind-control-plane`) running API server, scheduler, etcd, controller manager
- **Workers**: 2 nodes (`kind-worker`, `kind-worker2`) running workloads (e.g. NGINX Pods)

---

## Lab Steps Overview

1. **Prerequisites & Tooling**:
   - Docker / Docker Desktop
   - `kubectl`
   - `kind`
2. **Cluster Configuration (`kind-config.yaml`)**:
   ```yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
   - role: control-plane
   - role: worker
   - role: worker
   ```
3. **Cluster Creation**:
   ```bash
   kind create cluster --config kind-config.yaml
   ```
4. **Verification**:
   ```bash
   kubectl cluster-info --context kind-kind
   kubectl get nodes
   docker ps
   kubectl get pods -n kube-system -o wide
   ```
5. **Deploy NGINX Web Application**:
   ```bash
   kubectl create deployment web --image=nginx --replicas=3
   kubectl get deployments
   kubectl get pods -o wide
   ```
6. **Scaling & Self-Healing**:
   ```bash
   kubectl scale deployment web --replicas=6
   kubectl get pods -o wide
   kubectl delete pod <pod-name>
   kubectl get pods
   ```
