<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021. -->

# Egeria Setup


In this section you will set up the prerequisites that we are going to use to get
Egeria up and running.

We are going to setup:

  * A Kubernetes runtime where Egeria & other components will execute within containers
  * An application to help making REST API calls to Egeria.

## Prerequisite Hardware and Operating System

You will need **either**:

  * System running macOS (8GB RAM, 12GB disk free)
    - Monterey has been tested, recent versions from the last year or two should work.
    - Only Intel CPU architecture has been tested. However all the required pieces should work on m1. If you experience issues, report via the slack channel & your instructor.
  * System running Windows 10 or 11 (8GB RAM, 12GB disk free)
    - Only Intel architecture CPUs have been tested and are likely to work.

!!! note "Advanced environments"
    The tutorials require a Kubernetes runtime. If you have a cloud environment, or are running on another system such as a raspberry pi with suitable ram, or you
    just want to use a different Kubernetes distribution to that documented, you
    should be able to work through the tutorials, but you may need to configure the Kubernetes environment yourself, or modify the network addressed used
    if you run the desktop client (Postman) elsewhere. You could even use `curl` directly.


## Setting up a Kubernetes runtime

!!! note "Kubernetes already?"
    If you already have access to a Kubernetes runtime you can skip this section

We will use Kubernetes as the runtime environment for running Egeria.

Follow these steps from our [Kubernetes Documentation](/egeria-docs/guides/operations/kubernetes):

  * [Setting up Kubernetes](/egeria-docs/guides/operations/kubernetes/k8s) - follow the instruction for **Rancher Desktop**
  * [Setting up Helm](/egeria-docs/guides/operations/kubernetes/helm)

## Setting up Postman

Follow these steps to setup Postman

  * [Setting up Postman](/egeria-docs/education/tutorials/postman-tutorial/overview)

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

--8<-- "snippets/abbr.md"
