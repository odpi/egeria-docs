<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021. -->

# Installing Egeria for the first time

For this next exercise we will install a very simple ready-made Egeria environment.

This will help ensure that your environment is working properly, and helm explain some of
the egeria concepts before we get you to create your own environment.

## Checking Kubernetes is working

In the previous steps you installed Kubernetes and Helm.

First we'll check that you still have the correct environment setup. If you get any errors, check back with the
[Kubernetes documentation](/egeria-docs/guides/operations/kubernetes/)

You may only have a single node if running a simple environment, but these commands should
confirm you have connectivity to your Kubernetes cluster.

!!! Warning
    If you have not installed 'microk8s', but are using a regular
    Kubernetes environment, you need to modify the commands accordingly.

    
    For example:

    `kubectl` becomes `microk8s kubectl` becomes `kubectl`
    
    `helm` becomes `microk8s helm3` becomes `helm`

```
jonesn:~/ $ microk8s kubectl get all                                                                                                             [10:51:49]
NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.152.183.1   <none>        443/TCP   2d15h
jonesn:~/ $ microk8s kubectl get nodes                                                                                                           [10:51:52]
NAME          STATUS   ROLES    AGE     VERSION
microk8s-vm   Ready    <none>   2d15h   v1.22.4-3+adc4115d990346
jonesn:~/ $ microk8s helm3 list                                                                                                                  [10:52:00]
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/2695/credentials/client.config
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
jonesn:~/ $
```

!!! Info
    The warning about the configuration file is normal with current versions of
    microk8s (at least on macOS, via Homebrew). There's no need to take action in a test emvironment.
## Checking which egeria charts are available

We need to ensure your Kubernetes environment can access the egeria chart repository.
You may have performed this step previously, but it is harmless to repeat, and is included
here just in case you missed the instruction earlier.
```
jonesn:~/ $ microk8s helm3 repo add egeria https://odpi.github.io/egeria-charts                                                                  [10:56:05]
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/2695/credentials/client.config
"egeria" already exists with the same configuration, skipping
```

First we'll look at what charts are available:

```
jonesn:~/ $ microk8s helm3 search repo egeria                                                                                                    [10:57:17]
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/2695/credentials/client.config
NAME                  	CHART VERSION	APP VERSION	DESCRIPTION
egeria/egeria-base    	3.4.0        	3.4        	Egeria simple deployment to Kubernetes
egeria/egeria-cts     	3.4.0        	3.4        	Egeria Conformance Test Suite deployment to Kub...
egeria/egeria-pts     	3.4.0        	3.4        	Egeria Performance Test Suite deployment to Kub...
egeria/odpi-egeria-lab	3.4.0        	3.4        	Egeria lab environment
```

This list will change as the Egeria team continue to develop these charts

!!! Advanced
    You can add `--devel` to the helm commands to access pre-release versions
    of the charts. Only do this if directed to by the Egeria team, or if you experience
    problems.
    ```
    jonesn:~/ $ microk8s helm3 search repo egeria --devel                                                                                            [10:57:49]
    WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/2695/credentials/client.config
    NAME                  	CHART VERSION     	APP VERSION	DESCRIPTION
    egeria/egeria-base    	3.4.1-prelease.2  	3.4        	Egeria simple deployment (platform, react UI)
    egeria/egeria-cts     	3.4.0             	3.4        	Egeria Conformance Test Suite deployment to Kub...
    egeria/egeria-pts     	3.4.0             	3.4        	Egeria Performance Test Suite deployment to Kub...
    egeria/odpi-egeria-lab	3.4.1-prerelease.4	3.4        	Egeria lab environment
    ```

    The following commands use this flag, as the dojo is still being developed
    and written (Dec 2020/Jan 2021)
## Installing a simple egeria environment
We'll now install a simple Egeria configuration:

```
jonesn:~/ $ microk8s helm3 install base egeria/egeria-base --devel                                                                               [12:12:21]
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /var/snap/microk8s/2695/credentials/client.config
NAME: base
LAST DEPLOYED: Thu Dec 23 12:12:49 2021
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

```
jonesn:~/ $ microk8s kubectl get pods                                                                                                            [12:12:52]
NAME                                        READY   STATUS              RESTARTS   AGE
egeria-base-config--1-kp28v                 0/1     Init:0/2            0          93s
egeria-base-presentation-76997fb899-jhkml   1/1     Running             0          93s
strimzi-cluster-operator-86cdffd6d7-tsmjx   1/1     Running             0          93s
base-strimzi-zookeeper-0                    0/1     ContainerCreating   0          32s
egeria-base-platform-0                      0/1     Running             0          93s
```

We can see from this output, that not all of our pods are ready. Before we continue, we need to ensure 
all the pods are in READY state - this may take up to 10 minutes ie wait until
everything is ready. After several minutes (up to 5), the output should look
like this:
```
jonesn:~/ $ microk8s kubectl get pods                                                                                                            [12:16:21]
NAME                                            READY   STATUS      RESTARTS   AGE
egeria-base-presentation-76997fb899-jhkml       1/1     Running     0          5m18s
strimzi-cluster-operator-86cdffd6d7-tsmjx       1/1     Running     0          5m18s
egeria-base-platform-0                          1/1     Running     0          5m18s
base-strimzi-zookeeper-0                        1/1     Running     0          4m17s
base-strimzi-kafka-0                            1/1     Running     0          3m21s
base-strimzi-entity-operator-5b64ff6774-brstt   3/3     Running     0          2m53s
egeria-base-config--1-kp28v                     0/1     Completed   0          5m18s
```

## Explanation of what has been installed

The install has created the following egeria content:
 * egeria-base-presentation : a react UI for Egeria
 * egeria-base-platform : the core Egeria platform
 * egeria-base-config : A script that configures egeria. Runs once, then exits

We also have several 'strimzi' pods. These provide Kafka support, which
is needed for different parts of the Egeria platform to communicate.

Egeria has been setup with a default configuration as a demonstration.

Later in this tutorial we will walk through defining your own configuration, but this
first step helps to ensure your environment is working correctly.

## Testing the installation



--8<-- "snippets/abbr.md"
