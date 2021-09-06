<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# What is an Operator?

- An operator is a way of extending [Kubernetes](k8s.md) with application specific capababilities. 
- The notion of 'operator' comes from managing an application through it's lifecycle, just as a human operator would, but here we do it automatically.

Operator functionality could include:
 - deploying an application
 - upgrading an applications, perhaps migrating data
 - taking backups
 - mapping application specific behaviour into more standard kubernetes commands
 
## Custom Resources

Kubernetes has many standard resource definitions, such as for pods, services, deployments. Instances of each define the intended state of the object it represents.

[Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-resources) Definitions (**CRD**s) extend Kubernetes to allow anything to be represented, such as the intended state of an application stack.  They are defined in yaml. 

Resource definitions include:
 - apiVersion - consider this the namespace
 - metadata - useful for searching, selecting
 - spec - the intended state we are describing
 - status - used to capture current state
 
An instance of a CRD is known as a Custom Resource (**CR**)

## Controller

There is no intrinsic behaviour associated with a custom resource - it is purely a document with a defined schema. The behaviour is defined by the [Controller](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-controllers), which is code running within the Kubernetes cluster.

The controller's objective is to make reality match the configured Custom Resource. It will watch particular resource types - the primary being the CRD above - and as changes are observed will do whatever is needed to configure application to match the desired intent. It is primarily a reconcilation loop.

The controller will likely use a combination of Kubernetes APIs, perhaps defining and updating other resources, as well as interacting directly with application code within, or external to the cluster.

## Further information
* [Operator Pattern (Docs, kubernetes.io)](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* Kubernetes Operator 101 (Blog, Red Hat) - [Part1](https://developers.redhat.com/articles/2021/06/11/kubernetes-operators-101-part-1-overview-and-key-features) | [Part2](https://developers.redhat.com/articles/2021/06/22/kubernetes-operators-101-part-2-how-operators-work#)
* [Kubernetes Operator (Video, IBM)](https://www.youtube.com/watch?v=i9V4oCa5f9I)
* [Operators over easy: an introduction to Kubernetes Operators (Video, Red Hat)](https://www.redhat.com/en/blog/operators-over-easy-introduction-kubernetes-operators)

# How does it differ from Helm?

[Helm](helm.md) is a popular way of installing an application stack through charts, and sometimes upgrading. However at it's core, Helm is a templating engine. It takes templates, runs them through a processor to expand variables (across multiple documents). It then submits the documents to the Kubernetes API server just the same as if they'd be created standalone.

Helm charts can be stored in a repository, and make putting together a complex stack relatively easy. (we already use them successfully for Egeria). More complex behaviour can be done by deploying additional containers, jobs etc.

This is **very** different to an operator. Rather than create standard Kubernetes resources, with an operator we are trying to model our application, define it's intended state, and then have active code **always** running to monitor and achieve this. Operators are thus much more sophisticated, but also complex.

Operators and custom resources can themselves be deployed using Helm - so we don't think of the Operators are replacing Helm, rather they are very complementary techniques which can be used together. For example, whist an operator might focus on a single application, a helm chart may deploy a demonstation environment.

# Operator Lifecycle Manager

The [Operator Lifecycle Manager](https://github.com/operator-framework/operator-lifecycle-manager) (**OLM**) is an optional extension that can be used alongside operators to manage them. OLM allows for operator discovery and manages dependencies between operators.

OLM is [standard in Red Hat OpenShift](https://docs.openshift.com/container-platform/4.8/operators/understanding/olm/olm-understanding-olm.html)

**OLM is not necessary to use operators** - and unlike operators themselves, the framework **is not present in all Kubernetes distibutions**.

# Catalogs

A catalog of operators can be found on [OperatorHub](https://operatorhub.io) and authors can [submit their own operator](https://operatorhub.io/contribute) to help with findability.

# Building an operator

# Egeria Operator

The Egeria operator is being developed at https://github.com/odpi/egeria-k8s-operator - see here for
* [Issues](https://github.com/odpi/egeria-k8s-operator)
* prereqs/dependencies
* feedback, getting involved
* build and install instructions

## Design considerations

### Must be able to handle complex Egeria configurations

Custom Resource definitions allow for a very detailed specification of what we want our Egeria deployment to be. However Egeria itself already has a sophisticated approach to configuration - some elements of which are still evolving.

It could be possible to try and fully expose this configuration as a CRD. However due to the complexity, fluidity, and duplication the Operator instead will add k8s deployment specific information around existing Egeria configurations.

### Support scaling & failover

###Server authoring should be independent from deployment of a server

## Operator Development

As of September 2021, the current operator: 
 - defines a custom CRD (EgeriaPlatform) from which instances can be created
 - can deploy Egeria platforms with a list of servers
 - uses Kubernetes ConfigMaps to store individual server configuration
 - requires the user to use repositories capable of supporting replication (like crux)

Still to do
 - Helm chart to deploy a complete demo environment (possible coco pharma) with Egeria operator
 - working through the full server authoring lifecycle (alongside Server Author UI & View Services) - including templating of connections which contain host:ip from the authoring environment
 - Evaluating alternative stores of server configuration (at a minimum may need to be a secret)
 - Automated testing & packaging (to both a full k8s cluster & using a test framework)
 - Operator Lifecycle Manager integration
 - publish on Operator Hub
 - consideration of more detailed mapping between Egeria Concepts and operator


----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
