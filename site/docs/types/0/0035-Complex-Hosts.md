<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0035 Hosts

The host entity provides a simple model for the IT infrastructure (nodes, computers, etc) that data resources are hosted on.
In today's systems, hardware is managed to get the maximum use out of it. Therefore, the concept of a *host* is typically virtualized to allow a single computer to be used for many hosts and for multiple computers to collectively support a single host.

![UML](0035-Complex-Hosts.svg)

## Host entity

The concept of a *Host* is abstracted to describe a deployment environment that has access to hardware and has a basic software stack, typically including the operating system.

The host can be linked to its location through the [AssetLocation](/types/0/0025-Locations/#assetlocation) relationship.

## DeployedOn relationship

The *DeployedOn* relationship shows where IT Infrastructure is deployed to.

## BareMetalComputer entity

A *BareMetalComputer* describes a connected set of physical hardware. The open metadata types today do not attempt to model hardware in detail but this could be easily added if a contributor with the appropriate expertise was willing to work on it.

## VirtualMachine entity

A *VirtualMachine* provides virtualized hardware through a hypervisor that allows a single physical bare metal computer to run multiple virtual machines.

## VirtualContainer entity

A *VirtualContainer* provides the services of a host to the [software servers](/types/0/0040-Software-Servers) deployed on it. When the server makes requests for storage, network access, and other resources, the *VirtualContainer* delegates the requests to the equivalent services of the actual host it is deployed on.

*VirtualContainer*s can be hosted on other *VirtualContainer*'s, but to actually run they need to ultimately be deployed onto a real physical [Host](/types/0/0030-Hosts-and-Platforms/#host).

### Examples

*VirtualContainer* provides the type for the popular container type called [docker :material-dock-window:](https://www.docker.com/){ target=docker }.

## HostCluster entity

A *HostCluster* describes a collection of hosts that together are providing a service. Clusters are often used to provide horizontal scaling of services.

Within the host cluster there may be a special host (node) that is controlling the execution of the other members. This host is modelled with a [SoftwareServerPlatform](/types/0/0037-Software-Server-Platforms/#softwareserverplatform) that describes the cluster management platform, and optional [SoftwareServer](/types/0/0040-Software-Servers/#softwareserver) assets.  [SoftwareCapabilities](/types/0/0042-Software-Capabilities/#softwarecapability) needed to manage the cluster are linked to these [ITInfrastructure](/types/0/0030-Hosts-and-Platforms/#itinfrastructure) using the [ServerAssetUse](/types/0/0045-Servers-and-Assets/#serverassetuse) relationship.

### Examples 

For example, *HostCluster* can describe a [Hadoop cluster :material-dock-window:](https://hadoop.apache.org/){ target=apache } that uses multiple bare metal computers/virtual machines to manage big data workloads.

Similarly, *HostCluster* can describe a [Kubernetes cluster :material-dock-window:](https://kubernetes.io/){ target=k8s } that manages containerized applications across multiple bare metal computers/virtual machines.

The containerized applications managed by Kubernetes are represented as *VirtualContainer*'s.

## HostClusterMember relationship

The host cluster is linked to the hosts it is managing using the *HostClusterMember* relationship.  The properties help to clarify how the member in the cluster is used.

* *memberRole* describes the role of the member in a cluster.  For example, in a kubernetes cluster there are two membership roles: the *pods* and the *hosts*.  The *membershipRole* can be set up to show which hosts are the containers running as pods and which are providing the processing location as *hosts*.  The pods and the hosts are then linked together using the *deployedOn* relationship to show where the various pods have been deployed.
* *additionalProperties* provides a place to add additional information about the membership of the cluster such as configuration properties.

--8<-- "snippets/abbr.md"
