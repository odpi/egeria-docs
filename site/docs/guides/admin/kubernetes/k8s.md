<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# What is Kubernetes?

_Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications._ - https://kubernetes.io

This is how the [official website](https://kubernetes.io/) [describes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) it. It's effectively a standardized way of deploying applications in a very scalable way - from everything such as development prototyping through to massive highly available enterprise solutions.


In this document I'll give a very brief summary that should help those of you new to Kubernetes to make your first steps with Egeria.


# What are the key concepts in Kubernetes?

These are just some of the concepts that can help to understand what's going on. This isn't a complete list.

## Api

Kubernetes using a standard [API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) which is oriented around manipulating Objects. The commands are therefore very standard, it's all about the objects.



## Making it so
The system is always observing the state of the system through these objects, and where there are discrepancies, taking action to 'Make it So' as Captain Picard would say. The approach is imperitive. So we think of these [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) as describing the _desired state_ of the system.

## Namespace

A [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) provides a way of seperating out kubernetes resources by users or applications as a convenience. It keeps names more understandable, and avoids global duplicates.

For example a developer working on a k8s cluster may have a namespace of their own to experiment in.

## Container

A [Container](https://kubernetes.io/docs/concepts/containers/) is what runs stuff. It's similar to a Virtual Machine in some ways, but much more lightweight. Containers use code Images which may be custom built, or very standard off-the-shelf reusable items. Containers are typically very focussed on a single need or application. 

## Pod

A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) is a single group of one or more containers. Typically a single main container runs in a pod, but this may be supported by additional containers for log, audit, security, initialization etc. Think of this as an atomic unit that can run a workload.

Pods are disposeable - they will come and go. Other objects are concerned with providing a reliable service.

## Service

A [service](https://kubernetes.io/docs/concepts/services-networking/service/) provides network accessibility to one or more pods. The service name will be added into local Domain Name Service (DNS) for easy accessibility from other pods. Load can be shared across multiple pods

## Ingres

Think of [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)  as the entry point to Kubernetes services from an external network perspective - so it is these addresses external users would be aware of.

## Deployment 

A [deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) keeps a set of pods running - including replica copies, ie restarted if stopped, matching resource requirements, handling node failure .

## Stateful Set

A [stateful set](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) goes further than a deployment in that it keeps a well known identifier for each identical replica. This helps in allocating persistent storage & network resources to a replica

## ConfigMap

A [config map](https://kubernetes.io/docs/concepts/configuration/configmap/) is a way of keeping configuration (exposed as files or environment variables) seperate to an application.

## Secret

A [secret](https://kubernetes.io/docs/concepts/configuration/secret/) is used to keep information secret, as the name might suggest ... This might be a password or an API key & the data is encrypted

## Custom Objects

In addition to this list -- and many more covered in the official documentation -- Kubernetes also supports custom resources. These form a key part of Kubernetes [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). 

## Storage

Pods can request storage - which is known as a persistent volume claim (PVC), which are either manually or automatically resolved to a persistent volume.

See the k8s docs [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)


# Why are we using Kubernetes?

 All sizes of systems can run kubernetes applications - from a small raspberry pi through desktops and workstations through to huge cloud deployments. 

Whilst the details around storage, security, networking etc do vary by implementation, the core concepts, and configurations work across all.

Some may be more concerned about an easy way to play with development code, try out new ideas, whilst at the far end of the spectrum enterprises want something super scalable and reliable, and easy to monitor.

For egeria we want to achieve two main things
* Provide easy to use demos and tutorials that show how Egeria can be used and worked with without requiring too much complex setup. 
* Provide examples that show how Egeria can be deployed in k8s, and then adapted for the organization's needs.

Other alternatives that might come to mind include
 * Docker -- whilst simple, this is more geared around running a single container, and building complex environment means a lot of work combining application stacks together, often resulting in something that isn't usable. We do of course still have container images, which are essential to k8s, but these are simple & self contained.
 * docker-compose -- this builds on docker in allowing multiple containers and servers to be orchestrated, but it's much less flexible & scalable than kubernetes.

# How do I get access to Kubernetes?

[Getting Started](https://kubernetes.io/docs/setup/) provides links to setting up Kubernetes in many environments. Below we'll take a quick look at some of the simpler examples, especially for new users.

## microk8s (Linux, Windows, macOS)

**[Official microk8s site](https://microk8s.io)**

4GB is recommended as a minimum memory requirement.

As with most k8s implementations, when running some ongoing cpu will be used, so if running on your laptop/low power device it's recommended to refer to the relevant docs & stop k8s when not in use.

When running on a separate server or a cloud service this isn't a concern.

When using microk8s, note that the standard k8s commands are renamed to avoid clashes, so use the microk8s ones in the remainder of the Egeria documentation

kubectl -> microk8s kubectl
helm -> microk8s helm

They can also be aliased on some platforms.

### MacOS
The [macos install](https://microk8s.io/#tab-three__content) docs cover the steps needed to install microk8s.

Most of the Egeria development team use MacOS, so the instructions are elaborated and qualified here:

* The recommended approach uses [HomeBrew](https://brew.sh). This offers a suite of tools often found on linux which are easy to setup on macOS. See [install docs](https://docs.brew.sh/Installation)
* IMPORTANT: Before installing, go into System Preferences->Security & Privacy. Click the lock to get into Admin mode. Then ensure Firewall Options->Enable Stealth Mode is NOT enabled (no tick). **If it is, microk8s will not work properly**. [More](https://github.com/ubuntu/microk8s/issues/2509)
* If you are concerned over the firewall change, or homebrew requirement, refer back to the official k8s documentation & choose another k8s implementation that works for you.
* Ensure you turn on the following services: storage, dns, helm3 . 
* dashboard is also useful to understand more about k8s and what is running. However it is currently failing as described in [issue 2507](https://github.com/ubuntu/microk8s/issues/2507)

As an example, the following commands should get you set up, but always check the official docs for current details

```shell
brew install ubuntu/microk8s/microk8s
microk8s install
microk8s status --wait-ready
microk8s enable dns storage helm3
microk8s kubectl get all --all-namespaces
```
Kubernetes is now running.

### Windows

Follow the [official instructions](https://microk8s.io/#tab-two__content) (untested)

### Linux

Follow the [official instructions](https://microk8s.io/#tab-one__content) (untested)

### kubectl command under microk8s

microk8s qualifies the core k8s command `kubectl` in that you need to use `microk8s kubectl` so either
* When docs refer you to type `kubectl` then just use `microk8s kubectl`
* add a shell alias ie `alias kubectl='microk8s kubectl'` into ~/.zshrc or equivilent shell startup script


## Docker Desktop (Windows, macOS)

[Docker Desktop](https://www.docker.com/products/docker-desktop) supports Kubernetes

After installing, go into Docker Desktop 'settings and select 'Kubernetes'. Make sure 'Enable Kubernetes' is checked. Also under resources ensure at least 4GB is allocated to Docker

## Cloud

Many cloud providers offer Kubernetes deployments which can be used for experimentation or production. This include

* [Redhat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it) on multiple cloud providers including on [IBMCloud](https://www.ibm.com/uk-en/cloud/openshift)
* [Kubernetes on IBMCloud](https://www.ibm.com/cloud/kubernetes-service?p1=Search&p4=43700058232060428&p5=e&gclid=*&gclsrc=aw.ds)
* [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/)
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE)

In addition to a cloud install, ensure you have installed the relevant cloud provider's tooling to manage their k8s environment, including having access to the standard kubernetes command `kubectl`.

Note that in the team's testing we mostly are running Redhat OpenShift on IBMCloud as a managed service. We welcome feedback of running our examples on other environments, especially as some of the specifics around ingress rules, storage, security can vary.

## Accessing applications in your cluster

See also [kubernetes docs](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-services/)

### NodePort

In the sample charts provided an option to use a [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport) is usually provided.

This is often easiest when running k8s locally, as any of the ip addressible worker nodes in your cluster can service a request on the port provided. This is why it's named a 'node port' ie a port on your node..

### kubectl port-forward

This can be run at a command line, and directly sets up forwarding from local ports into services running in your cluster. It requires no additional configuration beforehand, and lasts only as long as the port forwarding is running.

See [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) for more info

### Ingress

Ingress rules define how traffic directed at your k8s cluster is directed. Their definition tends to vary substantially between different k8s implementations but often is the easiest approach when running with a cloud service.

* [microk8s ingress](https://microk8s.io/docs/addon-ingress) 
----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
