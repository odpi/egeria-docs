<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# What is Kubernetes?

!!! quote "[Official description](https://kubernetes.io){ target=k8s }"
    Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.

This is how the [official website describes :material-dock-window:](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/){ target=k8s } it. It's effectively a standardized way of deploying applications in a very scalable way - from everything such as development prototyping through to massive highly available enterprise solutions.

In this document I'll give a very brief summary that should help those of you new to Kubernetes to make your first steps with Egeria.

## What are the key concepts in Kubernetes?

These are just some of the concepts that can help to understand what's going on. This isn't a complete list.

### API

Kubernetes using a standard [API :material-dock-window:](https://kubernetes.io/docs/concepts/overview/kubernetes-api/){ target=k8s } which is oriented around manipulating Objects. The commands are therefore very standard, it's all about the objects.

### "Making it so"

The system is always observing the state of the system through these objects, and where there are discrepancies, taking action to *"make it so"* as Captain Picard would say. The approach is imperative. So we think of these [objects :material-dock-window:](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/){ target=k8s } as describing the *desired state* of the system.

### Namespace

A [`namespace` :material-dock-window:](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/){ target=k8s } provides a way of separating out Kubernetes resources by users or applications as a convenience. It keeps names more understandable, and avoids global duplicates.

For example a developer working on a k8s cluster may have a namespace of their own to experiment in.

### Container

A [`container` :material-dock-window:](https://kubernetes.io/docs/concepts/containers/){ target=k8s } is what runs stuff. It's similar to a Virtual Machine in some ways, but much more lightweight. Containers use code Images which may be custom-built, or very standard off-the-shelf reusable items. Containers are typically very focussed on a single need or application. 

### Pod

A [`pod` :material-dock-window:](https://kubernetes.io/docs/concepts/workloads/pods/){ target=k8s } is a single group of one or more containers. Typically, a single main container runs in a pod, but this may be supported by additional containers for log, audit, security, initialization etc. Think of this as an atomic unit that can run a workload.

Pods are disposable - they will come and go. Other objects are concerned with providing a reliable service.

### Service

A [`service` :material-dock-window:](https://kubernetes.io/docs/concepts/services-networking/service/){ target=k8s } provides network accessibility to one or more pods. The service name will be added into local Domain Name Service (DNS) for easy accessibility from other pods. Load can be shared across multiple pods

### Deployment 

A [`deployment` :material-dock-window:](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/){ target=k8s } keeps a set of pods running - including replica copies, ie restarted if stopped, matching resource requirements, handling node failure .

### StatefulSet

A [`statefulset` :material-dock-window:](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/){ target=k8s } goes further than a deployment in that it keeps a well known identifier for each identical replica. This helps in allocating persistent storage and network resources to a replica

### ConfigMap

A [`configmap` :material-dock-window:](https://kubernetes.io/docs/concepts/configuration/configmap/){ target=k8s } is a way of keeping configuration (exposed as files or environment variables) separate to an application.

### Secret

A [`secret` :material-dock-window:](https://kubernetes.io/docs/concepts/configuration/secret/){ target=k8s } is used to keep information secret, as the name might suggest ... This might be a password or an API key and the data is encoded to avoid being directly read as plain text.

### Custom Objects

In addition to this list -- and many more covered in the official documentation -- Kubernetes also supports custom resources. These form a key part of Kubernetes [Operators :material-dock-window:](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/){ target=k8s }. 

### Storage

Pods can request storage - which is known as a persistent volume claim (PVC), which are either manually or automatically resolved to a persistent volume.

See the k8s docs [Persistent Volumes :material-dock-window:](https://kubernetes.io/docs/concepts/storage/persistent-volumes/){ target=k8s }

### Accessing applications in your cluster

!!! education "Further information"
See [the Kubernetes docs :material-dock-window:](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-services/){ target=k8s }.


#### Port-forward

This can be run at a command line, and directly sets up forwarding from local ports into services running in your cluster. It requires no additional configuration beforehand, and lasts only as long as the port forwarding is running. For this reason it is the approach
taken in our tutorials.

See [port forwarding :material-dock-window:](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/){ target=k8s } for more information.

#### NodePort

In the sample charts provided an option to use a [`NodePort` :material-dock-window:](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport){ target=k8s } is usually provided.

This is often easiest when running k8s locally, as any of the ip addressable worker nodes in your cluster can service a request on the port provided without needing to leave a proxy running. This is why it's named a *node port* i.e. a port on your node. Some of the egeria charts have direct support for
specifying nodeports.

#### Ingress

Ingress rules define how traffic directed at your k8s cluster is directed. Their definition tends to vary substantially between different k8s implementations but often is the easiest approach when running with a cloud service. Ingress definitions will often
use highly available load balancers. 

See [Ingress :material-dock-window:](https://kubernetes.io/docs/concepts/services-networking/ingress/){ target=k8s } for more information.

## Why are we using Kubernetes?

 All sizes of systems can run Kubernetes applications - from a small raspberry pi through desktops and workstations through to huge cloud deployments. 

Whilst the details around storage, security, networking etc do vary by implementation, the core concepts, and configurations work across all.

Some may be more concerned about an easy way to play with development code, try out new ideas, whilst at the far end of the spectrum enterprises want something super scalable and reliable, and easy to monitor.

For Egeria we want to achieve two main things

- Provide easy to use demos and tutorials that show how Egeria can be used and worked with without requiring too much complex setup. 
- Provide examples that show how Egeria can be deployed in k8s, and then adapted for the organization's needs.

Other alternatives that might come to mind include

- Docker -- whilst simple, this is more geared around running a single container, and building complex environment means a lot of work combining application stacks together, often resulting in something that isn't usable. We do of course still have container images, which are essential to k8s, but these are simple and self-contained.
- docker-compose -- this builds on docker in allowing multiple containers and servers to be orchestrated, but it's much less flexible and scalable than Kubernetes.


---8<-- "snippets/abbr.md"
