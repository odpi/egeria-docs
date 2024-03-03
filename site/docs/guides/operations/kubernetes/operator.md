<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# What is an Operator?

- An operator is a way of extending [Kubernetes](k8s.md) with application specific capabilities. 
- The notion of 'operator' comes from managing an application through its lifecycle, just as a human operator would, but here we do it automatically.

Operator functionality could include:

 - deploying an application
 - upgrading an applications, perhaps migrating data
 - taking backups
 - mapping application specific behaviour into more standard kubernetes commands

A summary of some interesting operators can be found [here](https://github.com/odpi/egeria-k8s-operator/blob/main/doc/research/PopularOperatorCapabilities.md)
 
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

The controller's objective is to make reality match the configured Custom Resource. It will watch particular resource types - the primary being the CRD above - and as changes are observed will do whatever is needed to configure application to match the desired intent. It is primarily a reconciliation loop.

The controller will likely use a combination of Kubernetes APIs, perhaps defining and updating other resources, as well as interacting directly with application code within, or external to the cluster.

## Further information
* [Operator Pattern (Docs, kubernetes.io)](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
* Kubernetes Operator 101 (Blog, Red Hat) - [Part1](https://developers.redhat.com/articles/2021/06/11/kubernetes-operators-101-part-1-overview-and-key-features) | [Part2](https://developers.redhat.com/articles/2021/06/22/kubernetes-operators-101-part-2-how-operators-work#)
* [Kubernetes Operator (Video, IBM)](https://www.youtube.com/watch?v=i9V4oCa5f9I)
* [Operators over easy: an introduction to Kubernetes Operators (Video, Red Hat)](https://www.redhat.com/en/blog/operators-over-easy-introduction-kubernetes-operators)

# How does it differ from Helm?

[Helm](helm.md) is a popular way of installing an application stack through charts, and sometimes upgrading. However, at it's core, Helm is a templating engine. It takes templates, runs them through a processor to expand variables (across multiple documents). It then submits the documents to the Kubernetes API server just the same as if they'd be created standalone.

Helm charts can be stored in a repository, and make putting together a complex stack relatively easy. (we already use them successfully for Egeria). More complex behaviour can be done by deploying additional containers, jobs etc.

This is **very** different to an operator. Rather than create standard Kubernetes resources, with an operator we are trying to model our application, define it's intended state, and then have active code **always** running to monitor and achieve this. Operators are thus much more sophisticated, but also complex.

Operators and custom resources can themselves be deployed using Helm - so we don't think of the Operators are replacing Helm, rather they are very complementary techniques which can be used together. For example, whist an operator might focus on a single application, a helm chart may deploy a demonstration environment.

# Operator Lifecycle Manager

The [Operator Lifecycle Manager](https://github.com/operator-framework/operator-lifecycle-manager) (**OLM**) is an optional extension that can be used alongside operators to manage them. OLM allows for operator discovery and manages dependencies between operators.

OLM is [standard in Red Hat OpenShift](https://docs.openshift.com/container-platform/4.8/operators/understanding/olm/olm-understanding-olm.html)

**OLM is not necessary to use operators** - and unlike operators themselves, the framework **is not present in all Kubernetes distributions**.

# Catalogs

A catalog of operators can be found on [OperatorHub](https://operatorhub.io) and authors can [submit their own operator](https://operatorhub.io/contribute) to help others locate their work.

# Building an operator

Operators can be built in any language than can support making API calls to Kubernetes. For example, it would be possible to write a Java based operator. This is complex, and uses low level APIs, with few examples published. 

The [Operator Framework](https://operatorframework.io) is a toolkit to make it easier to develop an operator by including higher level APIs, and tools for code generation. It supports:

* [Helm](https://helm.sh) - this wraps up a Helm chart as an operator, but as such it only delivers install/upgrade capability. They can be managed and catalogued as an operator.
* [Ansible](https://www.ansible.com) - an ansible operator can respond to events & run ansible scripts accordingly. This makes them significantly more flexible
* [Go](https://www.golangprograms.com) - These are full 'native' operators with full access to the Kubernetes API. Kubernetes itself is written in Go. They are therefore very flexible, though more complex to develop. They do however represent the majority of development in this area, providing also the best scope for help from peers.

A more detailed comparison can be found in this [blog](https://cloud.redhat.com/blog/build-your-kubernetes-operator-with-the-right-tool)

For another project aiming to support java see https://github.com/java-operator-sdk/java-operator-sdk

Egeria is implementing a Go operator, using the Operator Framework. This is the most established & flexible approach.

# Egeria Operator Development

The Egeria operator is being developed at https://github.com/odpi/egeria-k8s-operator - see here for

* [Issues](https://github.com/odpi/egeria-k8s-operator)
* Prerequisites/dependencies
* Feedback, getting involved
* Build, install, and usage instructions

## Design considerations

### Egeria configurations

Custom Resource definitions allow for a very detailed specification of what we want our Egeria deployment to be. However, Egeria itself already has a sophisticated approach to configuration - some elements of which are still evolving.

It could be possible to try and fully expose this configuration as a CRD. However, due to the complexity, fluidity, and duplication the Operator instead will add k8s deployment specific information around existing Egeria configurations.

It's therefore imperative we keep the **Authoring** of server configuration distinct from **Deployment**. The deployment environment will be different in a Kubernetes environment (hostnames, service names, etc.)

Initially the egeria config document will be used verbatim, however if processing is needed, an [Admission Webhook](https://sdk.operatorframework.io/docs/building-operators/golang/webhook/) could be used to validate ([validating](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)) & convert ([mutating](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)) the config before storing in k8s. This approach could also be used for CR validation.

[Example server configuration documents](https://github.com/odpi/egeria-k8s-operator/tree/main/samples/server)


### Scaling & failover

Kubernetes is a useful container solution that scales from a raspberry pi to huge cloud deployments. As such it may be used for anything from development to full enterprise production - and this is a strong part of its appeal. So the operator must support everything from a small development environment, through to a scalable, reliable cloud environment. 

#### Egeria Platform

The [OMAG Server Platform](/concepts/omag-server-platform) is a java process that is launched and acts as a platform for
running OMAG Servers (below). In itself it has relatively little configuration but does include:

- TLS configuration ie passwords, keys, certs
- Spring configuration (security, plugins, debug logging)

It offers an administration interface for defining OMAG Servers (below) and starting/stopping them.

The platform's connectors define the store for OMAG Server configuration and authorization checks when using the platform's services.

#### Egeria Servers

The [OMAG Server](/concepts/omag-server) is a logical concept that executes code within an OMAG Server Platform.  Each platform can run many servers.  Each server's operation is isolated by the platform.

#### So how do we scale?

Three main options are:

 * Model both servers and platforms as different Kubernetes resources. This provides the most accurate mapping, but would require the operator to manage 'scheduling' servers on platforms, and allowing for this to change dynamically as workload & requirements change. This would also require having logical URLs unique to each server.
 * Define servers, and automatically create platforms as needed, resulting in a 1:1 relationship between server and platform. This is simple, though server configuration would need to be overloaded with platform configuration (like ssl keys). This would also lead to creating many more platforms which comes at a resource cost (ram, cpu), as this is a process. Servers however are just logical constructs and have minimal overhead.
 * Handle replication at the level of platform only. This is close to how Kubernetes works with most apps. 

Whilst initially pursuing the first option, due to complexity, the last of these has now been chosen for simplicity.

This has also resulted in the OMAG Server Platform being the first-class resource we focus on defining for the operator, at least initially. 

### Stateful set vs Deployment 

A Deployment manages scaling of a set of containers (such as egeria platform) across multiple pods. A *Statefulset* extends this to provide a unique identity which can be used for unique service definitions, or for maintaining an association with dedicated storage.

In the current Egeria helm chart we use a stateful set that that persistent storage can be allocated uniquely to each
pod & retained across restarts.

However, the assumption in the operator environment is that Egeria is stateless (beyond the config & CR), and that any persistent state is managed
via the connections to metadata storage etc., and that a unique service address is not needed. This latter point may need to be revisited if the Egeria operator needs to actively interact with the individual replicas for control/config, but this is not yet the case, hence the choice of a simpler deployment initially.

### Configuration updates


* If a server's [configuration document](/concepts/configuration-document) is changed, the platform will be restarted. 
* Later we will try to just restart/stop the modified server and/or perform a rolling change. Care will need to be taken if the config change leads to a conflict.

### Admin requests

* The operator has no knowledge of the state of egeria servers, discovery engines etc.
* Attempts to perform any admin ops should be blocked (via security plugins to both platform & server)
* To refine this will require modeling those concepts in the operator

### Metadata repositories

The only metadata repository that offers a suitable HA/remote environment &  supported by the Egeria open source project is [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb }, using the [Egeria XTDB connector](/connectors/xtdb). 

Note: At this point, the deployment of XTDB itself is outside the scope of the operator.

### Connectors

Much of the capability in Egeria is pluggable. For example, we have a connector to the message bus, which could be kafka, but equally
may be RabbitMQ (if a connector were written). We have connectors that understand data sources such as for Postgres. These are
implemented as java jars, and are added into the classpath of the egeria platform. Thus, the platform can provide a certain capability
with these additional connectors, but it is the server which defines which ones to use (and refers to the class name to locate)

An Egeria server configuration document therefore contains many references to connectors. The references libraries must be available in the runtime environment ie platform. This is done by ensuring they are pointed to within the spring loader's 'LOADER_PATH' environment variable.

Several approaches are possible:
* Build a custom container image based on the [Egeria docker image](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-deployment/docker/egeria) including the desired connectors, and either placing the required additional files into /deployments/server/lib, or placing them elsewhere in the image and ensuring LOADER_PATH is set
* Dynamically download or mount the required libraries - and dependencies - when the server platform is set up by the operator, for example through an init job.

Currently, the operator takes the former, simpler approach. Therefore, specifying a custom container image as part of the platform configuration will often be required.

Connectors also often tend to refer to endpoints - for example the location of a Kafka message bus, a server's own address. Currently, the server configuration document
passed to the operator must have correct addresses. As yet there is no manipulation or templating of these addresses, though this may change in the future.

## Operator Development

### Prerelease 

 - deploy Egeria platforms with a list of servers
 - uses Kubernetes [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) to store individual server configuration
 - requires the user to use repositories capable of supporting replication (like XTDB)

### Still to do for an initial release

 - Helm chart to deploy a complete demo environment (coco pharma) with Egeria operator & XTDB backend.
 - working through the full server authoring lifecycle (alongside Server Author UI & View Services) - including templating of connections which contain host:ip from the authoring environment
 - Evaluating alternative stores of server configuration (at a minimum may need to be a [secret](https://kubernetes.io/docs/concepts/configuration/secret/) as we include auth info - but decided to use ConfigMaps initially for clarity during initial design)
 - Automated testing & packaging (to both a full k8s cluster & using a test framework)
 - Further end-user docs on using the operator
 - publish on [Operator Hub](https://operatorhub.io)


### Future enhancements

 - [Operator Lifecycle Manager](https://github.com/operator-framework/operator-lifecycle-manager) integration
 - publish on [Operator Hub](https://operatorhub.io)
 - refinement of configurations (consolidation, admission webhooks)
 - consideration of more detailed mapping between Egeria Concepts and operator
 - rolling platform restart (config update, upgrade etc)
 - Handling upgrades/migration between egeria versions
 - Integration with [Prometheus](https://prometheus.io)


---8<-- "snippets/abbr.md"
