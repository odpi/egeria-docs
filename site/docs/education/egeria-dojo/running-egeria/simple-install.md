<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# Installing Egeria for the first time

For this next exercise we will install a very simple ready-made Egeria environment.

This will help ensure that your environment is working properly, and explain some of
the Egeria concepts before you create your own environment.

## Checking Kubernetes is working

In the previous steps you installed Kubernetes and Helm.

First we'll check that you still have the correct environment setup. If you get any errors, check back with the
[Kubernetes documentation :material-dock-window:](/guides/operations/kubernetes/){ target=docs } .

You will likely only have single node if running a simple environment, but these commands should
confirm you have connectivity to your Kubernetes cluster.

!!! Warning
    Most Kubernetes environments will use the commands `kubectl` and `helm`. However if you
    are using **microk8s** remember that you always need to use slightly different commands.
    
    For example:

    `kubectl` becomes `microk8s kubectl` 
    
    `helm` becomes `microk8s helm3` 

```console
$ kubectl get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.43.0.1    <none>        443/TCP   2d19h
$ kubectl get nodes
NAME                   STATUS   ROLES                          AGE     VERSION
lima-rancher-desktop   Ready    builder,control-plane,master   2d19h   v1.22.5+k3s1
$ helm list
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
$
```

!!! Info
    If using **microk8s** you may see a warning about the configuration file. This is normal with current versions of
    microk8s (at least on macOS, via Homebrew). There's no need to take action in a test emvironment.

## Checking which egeria charts are available

We need to ensure your Kubernetes environment can access the Egeria chart repository. In this repository we have
charts - effectively application bundles - setup with the code you need to run the server-side aspects of the tutorial.

You may have performed this step previously, but it is harmless to repeat, and is included
here just in case you missed the instruction earlier.
```console
$ helm repo add egeria https://odpi.github.io/egeria-charts 
"egeria" already exists with the same configuration, skipping
$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "egeria" chart repository
Update Complete. ⎈Happy Helming!⎈
```

First we'll look at what charts are available:

!!! Info
    If you need to check out the very latest charts we are developing, you can add `--devel` on these commands. This retrieves the very latest, unreleased, versions of our charts.

```console
$ helm search repo egeria 
NAME                  	CHART VERSION     	APP VERSION	DESCRIPTION
egeria/egeria-base    	3.4.1           	3.4        	Egeria simple deployment (platform, react UI)
egeria/egeria-cts     	3.4.0             	3.4        	Egeria Conformance Test Suite deployment to Kub...
egeria/egeria-pts     	3.4.0             	3.4        	Egeria Performance Test Suite deployment to Kub...
egeria/odpi-egeria-lab	3.4.1           	3.4        	Egeria lab environment
$
```

This list will change as the Egeria team continue to develop these charts

## Installing a simple Egeria environment

We'll now install a simple Egeria configuration:

```console
$ helm install base egeria/egeria-base 
NAME: base
LAST DEPLOYED: Tue Jan 11 18:44:18 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
ODPi Egeria
---

Egeria base environment has now been deployed to Kubernetes.
It may take a minute or so for everything to start up.

Use 'helm show values egeria/egeria-base' if installed direct from repo to see all
configurable values

By default a single platform is created using the latest release of Egeria, with a single
metadata server 'mds1' and a view server 'view1'. The UI organization name is 'org'.
A job is started to perform this configuration and may take up to 10 minutes to complete.

Please provide any feeback via a github issue at https://github.com/odpi/egeria or
join us on slack via https://http://slack.lfai.foundation

- The ODPi Egeria team
```

## Checking what is running in the simple environment

We can see what pods we are running:

```console
$ kubectl get pods
NAME                                        READY   STATUS              RESTARTS   AGE
egeria-base-presentation-76997fb899-r2fkj   0/1     ContainerCreating   0          3s
egeria-base-platform-0                      0/1     ContainerCreating   0          3s
strimzi-cluster-operator-7d96cbff57-k98kw   0/1     Running             0          3s
egeria-base-config--1-s8l6n                 0/1     Init:0/2            0          3s
```

We can see from this output, that not all of our pods are ready. Before we continue, we need to ensure 
all the pods are in **Running** state - this may take up to 10 minutes ie wait until
everything is ready. After several minutes (up to 5), the output should look
like this:
```console
$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
egeria-base-presentation-76997fb899-r2fkj       1/1     Running   0          2m27s
base-strimzi-zookeeper-0                        1/1     Running   0          115s
strimzi-cluster-operator-7d96cbff57-k98kw       1/1     Running   0          2m27s
egeria-base-platform-0                          1/1     Running   0          2m27s
base-strimzi-kafka-0                            1/1     Running   0          84s
egeria-base-config--1-s8l6n                     1/1     Running   0          2m27s
base-strimzi-entity-operator-869bf86ff4-c4n79   3/3     Running   0          53s
$
```

## Explanation of what has been installed

The install has created the following Egeria content:

 * egeria-base-presentation : a [Ecosystem UI for Egeria :material-dock-window:](https://github.com/odpi/egeria-react-ui){ target=gh }.
 * egeria-base-platform : the [core Egeria platform :material-dock-window:](https://github.com/odpi/egeria){ target=gh }.
 * egeria-base-config : A [script :material-dock-window:](https://github.com/odpi/egeria-charts/blob/main/charts/egeria-base/scripts/config-egeria.sh){ target=gh } that configures Egeria. Runs once, then exits.

We also have several [Strimzi :material-dock-window:](https://strimzi.io){ target=strimzi } pods. These provide [Kafka :material-dock-window:](https://kafka.apache.org){ target=strimzi } support, which
is needed for different servers running on the Egeria platform to communicate.

Egeria has been set-up with a default configuration as a demonstration.

Later in this tutorial we will walk through defining your own configuration, but this
first step helps to ensure your environment is working correctly.

## Testing the installation

As long as all the pods are ready, we know that:
 - charts can be retrieved and installed
 - Kubernetes is working
 - Egeria is running
 - Configuration of Egeria (which includes bringing up egeria servers) is successful.

## Next step

Let's move on to the [Egeria UIs](/education/egeria-dojo/running-egeria/user-interfaces/ui-introduction)

--8<-- "snippets/abbr.md"
