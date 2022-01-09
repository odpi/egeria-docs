<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021. -->

# Manually configuring and operating a server

In the previous exercise we used a demo environment where an Egeria server was setup
automatically by scripts that ran after you deployed the Helm chart. This provides a quick-start
to understand more about Egeria, and be able to experiment with the API and interfaces more easily,
but isn't representative of a typical deployment since the configuration is fixed.

In this session we are going to configure the servers via the Egeria platform's REST API.

## Re-installing the simple demo environment

We are first going to clean up the Egeria environment you have already created:

```
jonesn:~/ $ helm list                                                                                                        [15:19:08]
NAME	NAMESPACE	REVISION	UPDATED                             	STATUS  	CHART                             	APP VERSION
lab 	default  	1       	2022-01-06 17:58:06.108272 +0000 UTC	deployed	odpi-egeria-lab-3.4.1-prerelease.2	3.4
jonesn:~/ $ helm list                                                                                                                  [15:19:17]
NAME	NAMESPACE	REVISION	UPDATED                             	STATUS  	CHART                             	APP VERSION
lab 	default  	1       	2022-01-06 17:58:06.108272 +0000 UTC	deployed	odpi-egeria-lab-3.4.1-prerelease.2	3.4
jonesn:~/ $ helm delete lab                                                                                                            [15:19:19]
release "lab" uninstalled
jonesn:~/ $ helm list                                                                                                                  [15:19:37]
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
jonesn:~/ $ kubectl get pods                                                                                                           [15:19:40]
NAME                                           READY   STATUS        RESTARTS      AGE
strimzi-cluster-operator-86cdffd6d7-2z7d5      1/1     Terminating   1 (17m ago)   21h
lab-strimzi-zookeeper-0                        1/1     Terminating   1 (17m ago)   21h
lab-strimzi-kafka-0                            1/1     Terminating   2 (17m ago)   21h
lab-strimzi-entity-operator-6f4d5f4f74-vn4d6   3/3     Terminating   5 (14m ago)   21h
```
Keep repeating this last command until we finally see no pods remaining (may take a minute or two):
```
jonesn:~/ $ kubectl get pods                                                                                                           [15:19:43]
No resources found in default namespace.
```

Now we'll install the same demo again, but this time we are going to set a parameter
which prevents the servers being automatically configured, so that we can walk through
this in the tutorial:
```
jonesn:~/ $ helm install base egeria/egeria-base --devel --set egeria.config=false                                                     [16:36:09]
NAME: base
LAST DEPLOYED: Fri Jan  7 16:36:20 2022
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
As before, we must check everything is running ok before we continue, so repeat getting
the status of the pods until all the pods are ready:
```
jonesn:~/ $ kubectl get pods                                                                                                           [16:38:23]
NAME                                       READY   STATUS    RESTARTS      AGE
egeria-base-presentation-d4c97645d-gm925   1/1     Running   0             2m12s
egeria-base-platform-0                     1/1     Running   0             2m12s
base-zookeeper-0                           1/1     Running   0             2m12s
base-kafka-0                               1/1     Running   1 (14s ago)   2m12s
```
You'll notice that this time we have no 'Completed' job - this was the script that configured our servers,
so now we'll do it by issuing REST API calls to configure.

## Configuring Egeria servers

Our starting point here is that we have 4 containers running
 * A single egeria platform (egeria-base-platform-0 in the above example)
 * A UI (egeria-base-presentation)
 * Kafka (used to communicate between servers)
 * Zookeeper (used by Kafka)



--8<-- "snippets/abbr.md"
