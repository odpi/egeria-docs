<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Lab - Coco Pharmaceuticals (odpi-egeria-lab)

This example is intended to replicate the metadata landscape of a hypothetical company, Coco Pharmaceuticals, and allow you to understand a little more about how Egeria can help, and how to use it. This forms our 'Hands on Lab'.

The Helm chart will deploy the following components, all in a self-contained environment,
 allowing you to explore Egeria and its concepts safely
and repeatably:

- Multiple Egeria servers
- Apache Kafka (and its Zookeeper dependency)
- Example Jupyter Notebooks
- Jupyter runtime
- Egeria's React based UI

## Prerequisites

In order to use the labs, you'll first need to have the following installed:

- Kubernetes 1.15 or above
- Helm 3.0 or above
- Egeria chart repository configured & updated

6GB RAM minimum is recommended for your k8s environment.

You no longer need a git clone of this repository to install the chart.

## Installation

```shell
helm repo add egeria https://odpi.github.io/egeria-charts
helm repo update
helm install [-f overrides.yaml] <name> egeria/odpi-egeria-lab
```
where <name> is whatever you want to call your installed chart, and the -f is optional, if you have overriding values to supply.

Example output: 
```console
$ helm install lab egeria/odpi-egeria-lab
NAME: lab
LAST DEPLOYED: Tue Aug 10 11:47:19 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
ODPi Egeria lab tutorial
---
```
Some additional help text is also output, which is truncated for brevity.

It can take a few seconds for the various components to all spin-up. You can monitor
the readiness by running `kubectl get all` -- when ready, you should see output like the following:

```console
$ kubectl get all
NAME                                                   READY   STATUS    RESTARTS   AGE
pod/lab-odpi-egeria-lab-ui-74cc464575-cf8rm            1/1     Running   0          126m
pod/lab-odpi-egeria-lab-datalake-0                     1/1     Running   0          126m
pod/lab-odpi-egeria-lab-nginx-7b96949b4f-7dff4         1/1     Running   0          126m
pod/lab-odpi-egeria-lab-presentation-bd9789747-rbv69   1/1     Running   0          126m
pod/lab-kafka-0                                        1/1     Running   0          126m
pod/lab-zookeeper-0                                    1/1     Running   0          126m
pod/lab-odpi-egeria-lab-dev-0                          1/1     Running   0          126m
pod/lab-odpi-egeria-lab-uistatic-7b98d4bf9b-sf9bj      1/1     Running   0          126m
pod/lab-odpi-egeria-lab-core-0                         1/1     Running   0          126m
pod/lab-odpi-egeria-lab-factory-0                      1/1     Running   0          126m
pod/lab-odpi-egeria-lab-jupyter-77b6868c4-9hnlp        1/1     Running   0          126m

NAME                                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/kubernetes                    ClusterIP   10.152.183.1     <none>        443/TCP                      20h
service/lab-kafka-headless            ClusterIP   None             <none>        9092/TCP,9093/TCP            126m
service/lab-zookeeper-headless        ClusterIP   None             <none>        2181/TCP,2888/TCP,3888/TCP   126m
service/lab-zookeeper                 ClusterIP   10.152.183.25    <none>        2181/TCP,2888/TCP,3888/TCP   126m
service/lab-jupyter                   ClusterIP   10.152.183.172   <none>        8888/TCP                     126m
service/lab-core                      ClusterIP   10.152.183.248   <none>        9443/TCP                     126m
service/lab-nginx                     ClusterIP   10.152.183.155   <none>        443/TCP                      126m
service/lab-datalake                  ClusterIP   10.152.183.191   <none>        9443/TCP                     126m
service/lab-dev                       ClusterIP   10.152.183.122   <none>        9443/TCP                     126m
service/lab-kafka                     ClusterIP   10.152.183.79    <none>        9092/TCP                     126m
service/lab-odpi-egeria-lab-factory   ClusterIP   10.152.183.158   <none>        9443/TCP                     126m
service/lab-uistatic                  ClusterIP   10.152.183.156   <none>        80/TCP                       126m
service/lab-presentation              ClusterIP   10.152.183.61    <none>        8091/TCP                     126m
service/lab-ui                        ClusterIP   10.152.183.186   <none>        8443/TCP                     126m

NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/lab-odpi-egeria-lab-presentation   1/1     1            1           126m
deployment.apps/lab-odpi-egeria-lab-nginx          1/1     1            1           126m
deployment.apps/lab-odpi-egeria-lab-ui             1/1     1            1           126m
deployment.apps/lab-odpi-egeria-lab-uistatic       1/1     1            1           126m
deployment.apps/lab-odpi-egeria-lab-jupyter        1/1     1            1           126m

NAME                                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/lab-odpi-egeria-lab-presentation-bd9789747   1         1         1       126m
replicaset.apps/lab-odpi-egeria-lab-nginx-7b96949b4f         1         1         1       126m
replicaset.apps/lab-odpi-egeria-lab-ui-74cc464575            1         1         1       126m
replicaset.apps/lab-odpi-egeria-lab-uistatic-7b98d4bf9b      1         1         1       126m
replicaset.apps/lab-odpi-egeria-lab-jupyter-77b6868c4        1         1         1       126m

NAME                                            READY   AGE
statefulset.apps/lab-odpi-egeria-lab-dev        1/1     126m
statefulset.apps/lab-zookeeper                  1/1     126m
statefulset.apps/lab-kafka                      1/1     126m
statefulset.apps/lab-odpi-egeria-lab-core       1/1     126m
statefulset.apps/lab-odpi-egeria-lab-datalake   1/1     126m
statefulset.apps/lab-odpi-egeria-lab-factory    1/1     126m
```

All of the `pod/...` listed at the top have `Running` as their `STATUS` and `1/1` under `READY`.)

## Accessing the Jupyter notebooks

We now need to get connectivity to the interesting pods, such as that running the Jupyer notebook server, as this is where you'll get to the examples.

Since k8s implementations vary one simple approach for local testing is to use `kubectl port-forward` to connect to the relevant service.

If you look in the list of services above (`kubectl get services`) we have one named 'service/lab-jupyter' so let's try that (with microk8s):
```console
$ kubectl port-forward service/lab-jupyter 8888:8888
Forwarding from 127.0.0.1:8888 -> 8888
Forwarding from [::1]:8888 -> 8888
```
This command will not return - the port forwarding is active whilst it's running. In this example we're forwarding all requests to local port 8888 to the k8s service for jupyter

At this point you should be able to access your notebooks by going to this forwarded port ie 'http://localhost:8888'

## Accessing the React UI

We repeat the port forwarding above, this time for another service
```console
$ kubectl port-forward service/lab-presentation 8091:8091
Forwarding from 127.0.0.1:8091 -> 8091
Forwarding from [::1]:8091 -> 8091
```
As before, you can define an Ingress, or use nodeports instead if preferred.

Now go to https://localhost:8091/coco to access the React UI. Login as 'garygeeke',password 'admin'.

## Accessing the Egeria UI

The same applies to the service exposing Egeria UI

```console
$ kubectl port-forward service/lab-uistatic 8443
Forwarding from 127.0.0.1:8443 -> 8443
Forwarding from [::1]:8443 -> 8443
```
Now you can go to https://localhost:8443 to access Egeria UI.

## Starting over

Because the environment is entirely self-contained, you can easily start over the labs simply
by deleting the deployment and running the installation again. This will wipe out all of the
metadata across the lab Egeria servers, remove all messages from the Kafka bus used in the cohort,
reset the Jupyter notebooks to their original clean state, etc.

To delete the deployment, simply run this:

```console
$ helm delete lab
```

Where `lab` is the name you used in your original deployment. (You can see what it's called by first running `helm list` and reviewing the output.)

(Then just re-run the last command in the Installation section above to get a fresh environment.)

## Overriding Configuration

The chart is configured to use a default set of parameters.  You can override these by creating a file such as `lab.yaml` with the  contents of any values you wish to modify, for example:

```console
service:
  type: NodePort
  nodeport:
    jupyter: 30888
    core: 30080
    datalake: 30081
    dev: 30082
    factory: 30083
    ui: 30443
```

Refer to the existing values file for additional ports in this section that may reflect new components as added

You can then deploy using
`helm install lab odpi-egeria-lab -f lab.yaml` which will override standard defaults with your choices

## Adding additional connectors

Additional connectors can be loaded into the egeria platform containers during initalization.

These need to be specified as url/name pairs, for example create a file '~/etc/connectors.yaml' with the following contents:
```
extralibs:
  - url: https://search.maven.org/remotecontent?filepath=org/odpi/egeria/egeria-connector-integration-jdbc/1.0/egeria-connector-integration-jdbc-1.0.jar
    filename: egeria-connector-integration-jdbc.jar
  - url: https://search.maven.org/remotecontent?filepath=org/odpi/egeria/egeria-connector-resource-jdbc/1.0/egeria-connector-resource-jdbc-1.0.jar
    filename: egeria-connector-resource-jdbc.jar
  - url: https://jdbc.postgresql.org/download/postgresql-42.5.2.jar
    filename: postgresql.jar
```
The url can be any that is valid for use with `curl` such as http, https, ftp etc.

Then add `-f ~/etc/connectors.yaml` to the helm install command line

All files will be copied into /deployments/server/extralibs in the running container, and will on the CLASSPATH, so loadable as a connector

Examples can be found under https://github.com/odpi/egeria-charts/tree/main/config/values

## Enabling persistence

Support has been added to use persistence in these charts. See 'values.yaml' for more information on this option.
You may also wish to refer to the 'egeria-base' helm chart which is a deployment of a single, persistent, autostart server with UI.

Note however that since this will save the state of your configuration done from
the tutorial notebooks it may be confusing - as such this is disabled by default. It may be useful if you are modifying the charts for your own use.

You will also need to delete all storage associated with the chart manually if you want to cleanup/reset - for example
```console
kubectl delete pvc --all
kubectl delete pv --all
```
---8<-- "snippets/abbr.md"

