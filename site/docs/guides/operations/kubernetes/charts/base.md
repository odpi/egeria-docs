<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# Base Egeria (egeria-base)

This is a simple deployment of Egeria which will just deploy a basic Egeria environment
which is ready for you to experiment with. Specifically it sets up:

- A single Egeria platform which hosts
    - An Egeria metadata server with a persistent graph store (JanusGraph).
    - A new server to support the UI.
- A UI to allow browsing of types, instances & servers.
- Apache Kafka & Zookeeper (using Strimzi).

It does not provide access to our lab notebooks, the Polymer based UI, nor is it preloaded with any data.

This chart may also be useful to understand how to deploy Egeria within kubernetes. In future we anticipate providing
an [operator](https://github.com/odpi/egeria-k8s-operator) which will be more flexible.

## Prerequisites

In order to use the chart, you'll first need to have the following installed:

- A [Kubernetes cluster](/guides/operations/kubernetes/k8s) at 1.15 or above with the `kubectl` tool in your path.
- [Helm](/guides/operations/kubernetes/helm) 3.0 or above, configured with the Egeria repository.

No configuration of the chart is required to use defaults, but information is provided below

## Installation

```shell
helm repo add egeria https://odpi.github.io/egeria-charts
helm repo update
helm install [-f overrides.yaml] <name> egeria/egeria-base
```
where <name> is whatever you want to call your installed chart, and the -f is optional, if you have overriding values to supply.

**THE INSTALL WILL TAKE SEVERAL MINUTES** to complete in the background, after the chart has deployed.

This is because it is not only creating the required
objects in Kubernetes to run the platforms, but also is configuring egeria itself - which involves waiting
for everything to startup before configuring Egeria via REST API calls.

Once installed the configured server is set to start automatically, storage is persisted, and so if your pod gets moved/restarted, egeria should come back automatically with the same data as before.

Wait until all pods are showing ready status from
```console
kubectl get pods
```
### Additional Install Configuration

This section is optional - skip over if you're happy with defaults - a good idea to begin with.

Refer to the comments in `values.yaml` for further information on what can be configured - this includes:
- server, organization, cohort names
- storage options - k8s storage class/size
- Egeria version
- Kubernetes service setup (see below also)
- roles & accounts
- timeouts
- names & repositories for docker images used by the chart
- Kafka specific configuration (setup in the Bitnami chart we use)

## Accessing Egeria

When this chart is installed, an initialization job is run to configure the Egeria metadata server and UI.

For example looking at kubernetes jobs will show something like:
```console
$ kubectl get pods
NAME                                            READY   STATUS      RESTARTS   AGE
base-strimzi-entity-operator-6c89df6d84-glk9d   3/3     Running     0          2m45s
base-strimzi-kafka-0                            1/1     Running     0          5m1s
base-strimzi-zookeeper-0                        1/1     Running     0          7m32s
egeria-base-config-48v58                        0/1     Completed   0          8m59s
egeria-base-platform-0                          1/1     Running     0          8m59s
egeria-base-presentation-76997fb899-vfqpp       1/1     Running     0          8m59s
strimzi-cluster-operator-7d96cbff57-l6b7c       1/1     Running     0          8m59s
```

You should wait until that first **egeria-base-config** job completes, it will then disappear from the list.
This job issues REST calls against the Egeria servers to configure them for this simple environment (see scripts directory).

The script will not run again, since we will have now configured the servers with persistent storage, and for the platform
to autostart our servers. So even if a pod is removed and restarted, the egeria platform and servers should return in the same state.

We now have Egeria running within a Kubernetes cluster, but by default no services are exposed externally - they are all of type `ClusterIP` - we can see these with

```console
$ kubectl get services                                                                                  [13:07:51]
NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP                         PORT(S)                      AGE
base-platform                   ClusterIP      172.21.196.41    <none>                              9443/TCP                     10m
base-presentation               ClusterIP      172.21.250.121   <none>                              8091/TCP                     10m
base-strimzi-kafka-bootstrap    ClusterIP      172.21.31.140    <none>                              9091/TCP,9092/TCP            6m22s
base-strimzi-kafka-brokers      ClusterIP      None             <none>                              9090/TCP,9091/TCP,9092/TCP   6m22s
base-strimzi-zookeeper-client   ClusterIP      172.21.35.112    <none>                              2181/TCP                     8m53s
base-strimzi-zookeeper-nodes    ClusterIP      None             <none>                              2181/TCP,2888/TCP,3888/TCP   8m53s
```

The **base-presentation** service is very useful to expose as this provides a useful UI where you can explore
types and instances. Also **egeria-platform** is the service for Egeria itself. 
In production you might want this only exposed very carefully to other systems - and not other users or the internet, but for experimenting with Egeria let's assume you do.

How these are exposed can be somewhat dependent on the specific kubernetes environment you are using.

In the [lab chart](chart_lab.md) we provided an example of using `kubectl port-forward`. Here we use RedHat OpenShift in IBM Cloud, where you can expose these services via a LoadBalancer using

```console
kubectl expose service/egeria-presentation --type=LoadBalancer --port=8091 --target-port=8091 --name pres  
kubectl expose service/egeria-platform --type=LoadBalancer --port=9443 --target-port=9443 --name platform   
```

If I run these, and then look again at my services I see I now have 2 additional entries (modified for obfuscation):
```console
platform                    LoadBalancer   172.21.218.241   3bc644c3-eu-gb.lb.appdomain.cloud   9443:30640/TCP               25h
pres                        LoadBalancer   172.21.18.10     42b0c7f5-eu-gb.lb.appdomain.cloud   8091:30311/TCP               22h
```

So I can access them at their respective hosts. Note that where hosts are allocated dynamically, it can take up to an hour or more for DNS caches to refresh. Waiting up to 5 minutes then refreshing a local cache has proven sufficient for me, but your experience may differ.

In the example above, the Egeria UI can be accessed at `https://42b0c7f5-eu-gb.lb.appdomain.cloud:8091/org/` . Replace the hostname accordingly, and also the `org` is the organization name from the `Values.yaml` file we referred to above

Once logged in, you should be able to login using our demo userid/password of `garygeeke/admin` & start browsing types and instances within Egeria.

You can also issue REST API calls against egeria using a base URL for the platform of `https://3bc644c3-eu-gb.lb.appdomain.cloud` - Other material
covers these REST API calls in more detail, but a simple api doc is available at `https://3bc644c3-eu-gb.lb.appdomain.cloud/swagger-ui.html`

## Cleaning up / removing Egeria

To delete the deployment, simply run this for Helm3:

```console
$ helm delete egeria
```

In addition, the Egeria chart makes use of persistent storage. To remove these use
```console
$ kubectl get pvc
NAME                                        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS                 AGE
data-egeria-kafka-0                         Bound    pvc-d31e0012-8568-4e6f-ae5d-94832ebcd92d   10Gi       RWO            ibmc-vpc-block-10iops-tier   48m
data-egeria-zookeeper-0                     Bound    pvc-90739fce-dce0-422b-8738-a38293d8fdfb   10Gi       RWO            ibmc-vpc-block-10iops-tier   48m
egeria-egeria-data-egeria-base-platform-0   Bound    pvc-197ba47e-a6d5-4f35-a7d8-7b7ec1ed1df3   10Gi       RWO            ibmc-vpc-block-10iops-tier   48m
```
Identify those associated with egeria - which should be obvious from the name and then delete with
```console
kubectl delete pvc <id>
```

See the section on Configuration for more details

---8<-- "snippets/abbr.md"
