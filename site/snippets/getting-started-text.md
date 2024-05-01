<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


There are a number of options available to you:

**Running Egeria natively on your local machine**

The [Getting Started with Egeria](https://getting-started-with-egeria.pdr-associates.com/introduction.html) blog provides a step-by-step guide to building, installing, configuring and running Egeria on your machine.

**Running Egeria in IntelliJ**

See [Setting up IntelliJ to develop components for Egeria](https://egeria-project.org/education/tutorials/developer-intellij-tutorial/overview/).

**Running Egeria in Kubernetes**

* There is a *base* helm chart that includes a single [platform](/concepts/omag-server-platform) with a [metadata server](/concepts/metadata-access-store).  This provides a simple way to experiment with Egeria's [APIs](/services) and [User Interfaces](/user-interfaces).  Link to instructions for [starting the *base* helm chart](/guides/operations/kubernetes/charts/base).

* There is a *lab* help chart that provides a more complex multi-platform environment that is integrated with a variety of third party technologies.  This chart is designed to support the [Open Metadata Labs](/education/open-metadata-labs/overview) which provide a rich set of demonstrations of many features of Egeria.  The Open Metadata Labs are a good option if you would like a guided tour of Egeria. Link to instructions for [starting the *lab* helm chart](/guides/operations/kubernetes/charts/lab).


    
