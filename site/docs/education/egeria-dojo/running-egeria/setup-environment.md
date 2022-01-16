<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# Egeria Setup


In this section you will set up the prerequisites that we are going to use to get
Egeria up and running.

We are going to setup:

  * A Kubernetes runtime where Egeria & other components will execute within containers.
  * An application to help making REST API calls to Egeria.

Egeria does not need to run in a container. The main application we run is a Java application we refer to as the 'server chassis'. In later days we will show you examples of running this directly, but for this first day we use Kubernetes to create a more reproducible environment that is easy to configure, especially with several moving parts.

## Prerequisite Hardware and Operating System

You will need a system with **either**:

  * macOS (8GB RAM, 12GB disk free)
    - Monterey has been tested, recent versions from the last year or two should work.
    - Only Intel CPU architecture has been tested. However all the required pieces should work on m1. If you experience issues, report via the slack channel & your instructor.
  * Windows 10 or 11 (8GB RAM, 12GB disk free)
    - Only Intel architecture CPUs have been tested and are likely to work.
  * Linux (8GB RAM, 12 GB free)
    - x86_64 or arm64 architecture

!!! note "Advanced environments"
    The tutorials require a Kubernetes runtime. If you have a cloud environment, or are running on another system such as a raspberry pi with suitable ram, or you
    just want to use a different Kubernetes distribution to that documented, you
    should be able to work through the tutorials, but you may need to configure the Kubernetes environment yourself, or modify the network addresses used 
    if you run the desktop client (Postman) elsewhere. You could even use `curl` directly, but will need to read the postman data files directly.


## Setting up a Kubernetes runtime

!!! note "Kubernetes already?"
    If you already have access to a Kubernetes runtime you can skip this section

We will use Kubernetes as the runtime environment for Egeria.

Follow these steps from our [Kubernetes Documentation :material-dock-window:](/egeria-docs/guides/operations/kubernetes){ target=docs }:

  * [Understanding Kubernetes :material-dock-window:](/egeria-docs/guides/operations/kubernetes/k8s-install/){ target=docs } - read this for some background information.
  * [Setting up Kubernetes :material-dock-window:](/egeria-docs/guides/operations/kubernetes/k8s){ target=docs } - follow the instruction to install **Rancher Desktop**.
  * [Useful Kubernetes commands :material-dock-window:](/egeria-docs/guides/operations/kubernetes/k8s-install/){ target=docs } - a useful reference. You don't need to issue these commands now, but this may be useful later.
  * [Setting up Helm :material-dock-window:](/egeria-docs/guides/operations/kubernetes/helm){ target = docs } - read about Helm, but you do not need to install it as it comes with **Rancher Desktop**.

**Do not continue in the above sections & install any of the charts at this point** - we will do this later.

## Setting up Postman

Follow these steps to setup Postman

  * [Setting up Postman :material-dock-window:](/egeria-docs/education/tutorials/postman-tutorial/overview){ target=docs }

## Test yourself

??? question "Test yourself"

    * What is Kubernetes?
    * What is Helm?
    * What does Postman let you do?
    * What's a Postman collection?
    * What's a Postman environment?
  

## Completion of setup

This concludes the setup of the environment that we will use to run the tutorials.

Take a look over your environment, discuss with your fellow attendees & take a break before we continue.


## Next step

Let's move on to a [Simple Egeria setup](/egeria-docs/education/egeria-dojo/running-egeria/simple-install)

--8<-- "snippets/abbr.md"
