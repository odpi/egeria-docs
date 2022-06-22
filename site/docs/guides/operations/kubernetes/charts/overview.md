<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Introduction to the Egeria Helm Charts

This set of charts has been built to assist in learning & demonstration activities, testing, and may also form a basis for production deployments.

See [Helm](../helm.md) for information on configuring Helm to be able to access these charts via a repository.

## Available Charts

* [base](base.md) - creates a simple Egeria environment with a single metadata server. Includes the Ecosystem UI so that metadata can be searched, browsed.
* [odpi-egeria-lab](lab.md) - Demo scenario for 'Coco Pharmaceuticals'. Multiple platorms, metadata repositories, cohorts. Demonstration script via Juypter notebooks. Includes both the Ecosystem UI & business UI .
* [cts](cts.md) - Supports testing repository connectors using our Conformance Test Suite. Can be configured to support other repositories via simple values.
* [pts](pts.md) - Performance test suite to aid in measuring the performance of repository connectors.

## Caveat: Strimzi: permissions and co-existance

When any of the above charts are deployed, they include the install of the Strimzi operator (for kafka). However Strimzi deploys some cluster-scoped resources which has two implications:

* Admin level to the cluster permissions are needed - since cluster resources need to be deployed. Without these permissions the Charts will not work.
* As the resources are cluster-level you cannot install a second chart - or additional install of the same chart as clashes will be seen on these resources. So no testing, debug in parallel or shared k8s clusters for multiple developers.

To address this, the charts all have the option to NOT install Strimzi. If this is done
* You can install multiple charts (recommended 1 per namespace) for the same, or different, user.
* You do not need such high permissions to install the Egeria chart.

To skip the install add the following to the install: `--set strimzi.enabled=false` ie:
```
helm install base egeria-base --set strimzi.enabled=false
```

You DO need Strimzi already installed by an admin:

* See Strimzi docs for information for [installing Strimzi via Helm](https://strimzi.io/blog/2018/11/01/using-helm/) or alternatively install another way, such as via the operator catalog.
* Ensure the strimzi operator is configured to [watch all namespaces](https://strimzi.io/docs/operators/latest/full/configuring.html#deploying-cluster-operator-to-watch-whole-cluster-str) (or at least includes the ones you want to use).

---8<-- "snippets/abbr.md"
