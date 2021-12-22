<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021. -->

# Egeria Setup


In this section you will set up the prerequisites that we are going to use to get
Egeria running, and to be able to make use of it's API.

We are going to setup:

  * A Kubernetes runtime where Egeria & other components will execute
  * An application to help making REST API calls to Egeria

!!! note "Apple M1 / ARM cpu support"
    At this time we do not fully support ARM processors including Apple Macs using m1 processors, nor raspberry pi. Addressing this is currently
    work in progress. The remaining instructions will work for Intel based macOS, Windows & Linux.


## Setting up a Kubernetes runtime

!!! note "Kubernetes already?"
    If you already have access to a Kubernetes runtime you can skip this section

We will use Kubernetes as the runtime environment for running Egeria.

Follow these steps from our [Kubernetes Documentation](/egeria-docs/guides/operations/kubernetes):

  * [Setting up Kubernetes](/egeria-docs/guides/operations/kubernetes/k8s)
  * [Setting up Helm](/egeria-docs/guides/operations/kubernetes/helm)

## Setting up Postman

Follow these steps to setup Postman

  * [Setting up Postman](/egeria-docs/tools/postman/overview)

## Test yourself

??? question "Test yourself"

* What is Kubernetes?
* What is Helm?
* What does Postman let you do?
* What's a Postman collection?
* What's a Postman environment?

## Finished

This concludes the setup of the environment that we will use to run the tutorials.

--8<-- "snippets/abbr.md"
