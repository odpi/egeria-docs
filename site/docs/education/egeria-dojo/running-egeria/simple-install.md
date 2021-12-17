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

If you are using microk8s:
```
jonesn:~/ $ microk8s.kubectl get pods                                                                                                                                                  [17:19:57]
No resources found in dojo namespace.
jonesn:~/ $ microk8s.kubectl get nodes                                                                                                                                                 [17:20:02]
NAME         STATUS   ROLES           AGE   VERSION
10.242.0.5   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.6   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.7   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.8   Ready    master,worker   31h   v1.21.6+81bc627
jonesn:~/ $ microk8s.helm list                                                                                                                                                         [17:21:10]
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
jonesn:~/ $
```
If you are running another k8s:
```
jonesn:~/ $ kubectl get pods                                                                                                                                                  [17:19:57]
No resources found in dojo namespace.
jonesn:~/ $ kubectl get nodes                                                                                                                                                 [17:20:02]
NAME         STATUS   ROLES           AGE   VERSION
10.242.0.5   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.6   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.7   Ready    master,worker   31h   v1.21.6+81bc627
10.242.0.8   Ready    master,worker   31h   v1.21.6+81bc627
jonesn:~/ $ helm list                                                                                                                                                         [17:21:10]
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
jonesn:~/ $
```

## Checking which egeria charts are available

First we'll look at what charts are available:

For microk8s:
```
jonesn:~/ $ microk8s.helm3 repo update                                                                                                                                                  [17:23:17]
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "strimzi" chart repository
...Successfully got an update from the "egeria" chart repository
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
jonesn:~/ $ microk8s.helm3 search repo egeria                                                                                                                                           [17:25:39]
NAME                  	CHART VERSION	APP VERSION	DESCRIPTION
egeria/egeria-base    	3.4.0        	3.4        	Egeria simple deployment to Kubernetes
egeria/egeria-cts     	3.4.0        	3.4        	Egeria Conformance Test Suite deployment to Kub...
egeria/egeria-pts     	3.4.0        	3.4        	Egeria Performance Test Suite deployment to Kub...
egeria/odpi-egeria-lab	3.4.0        	3.4        	Egeria lab environment
jonesn:~/ $
```

For other k8s:
```
jonesn:~/ $ helm repo update                                                                                                                                                  [17:23:17]
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "strimzi" chart repository
...Successfully got an update from the "egeria" chart repository
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
jonesn:~/ $ helm search repo egeria                                                                                                                                           [17:25:39]
NAME                  	CHART VERSION	APP VERSION	DESCRIPTION
egeria/egeria-base    	3.4.0        	3.4        	Egeria simple deployment to Kubernetes
egeria/egeria-cts     	3.4.0        	3.4        	Egeria Conformance Test Suite deployment to Kub...
egeria/egeria-pts     	3.4.0        	3.4        	Egeria Performance Test Suite deployment to Kub...
egeria/odpi-egeria-lab	3.4.0        	3.4        	Egeria lab environment
jonesn:~/ $
```

This list will change as the Egeria team continue to develop these charts

## Installing a simple egeria environment
We'll now install a simple Egeria configuration:

microk8s:
```
jonesn:~/ $ microk8s.helm3 install simple egeria/egeria-base                                                                                                                            [17:29:29]
NAME: simple
LAST DEPLOYED: Fri Dec 17 17:29:40 2021
NAMESPACE: dojo
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
jonesn:~/ $ microk8s.helm3 list                                                                                                                                                         [17:42:38]
NAME  	NAMESPACE	REVISION	UPDATED                           	STATUS  	CHART            	APP VERSION
simple	dojo     	1       	2021-12-17 17:29:40.3691 +0000 UTC	deployed	egeria-base-3.4.0	3.4
```

Non microk8s
```
jonesn:~/ $ helm install simple egeria/egeria-base                                                                                                                            [17:29:29]
NAME: simple
LAST DEPLOYED: Fri Dec 17 17:29:40 2021
NAMESPACE: dojo
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
ODPi Egeria
jonesn:~/ $ helm list                                                                                                                                                         [17:42:38]
NAME  	NAMESPACE	REVISION	UPDATED                           	STATUS  	CHART            	APP VERSION
simple	dojo     	1       	2021-12-17 17:29:40.3691 +0000 UTC	deployed	egeria-base-3.4.0	3.4
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
jonesn:~/ $
```
## Checking what is running in the simple environment
We can see what pods we are running:

For microk8s:
```
jonesn:~/ $ microk8s.kubectl get pods                                                                                                                                                  [17:29:42]
NAME                                       READY   STATUS     RESTARTS   AGE
egeria-base-config-z6f58                   0/1     Init:0/2   0          2m1s
egeria-base-platform-0                     0/1     Running    0          2m1s
egeria-base-presentation-5d9bdc854-br22v   1/1     Running    0          2m1s
simple-kafka-0                             1/1     Running    1          2m1s
simple-zookeeper-0                         1/1     Running    0          2m1s
```
For non-microk8s
```
jonesn:~/ $ kubectl get pods                                                                                                                                                  [17:29:42]
NAME                                       READY   STATUS     RESTARTS   AGE
egeria-base-config-z6f58                   0/1     Init:0/2   0          2m1s
egeria-base-platform-0                     0/1     Running    0          2m1s
egeria-base-presentation-5d9bdc854-br22v   1/1     Running    0          2m1s
simple-kafka-0                             1/1     Running    1          2m1s
simple-zookeeper-0                         1/1     Running    0          2m1s
```

We can see from this output, that not all of our pods are ready. Before we continue, we need to ensure 
all the pods are in READY state - this may take up to 10 minutes ie:


--8<-- "snippets/abbr.md"
