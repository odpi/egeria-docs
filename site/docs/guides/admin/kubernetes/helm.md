<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# Helm

_Helm is the best way to find, share, and use software built for Kubernetes._ - https://helm.sh

## Deploying apps in Kubernetes

In Kubernetes, resources such as pods (to run code) or services (for network accessibility) are defined in yaml. One or more documents can be submitted at a time.

So we might have one yaml file that defines our pod - with information about which container images to run, and another to setup a network service. finally we may have another that describes our storage requirements (a persistent volume claim
)

## What does Helm do?

Helm provides a way of bunding yaml files together into an archive, together with a templating mechanism to allow reuse of common patterns & ensure different yamls are consistent and can reference each other.

These archives are known as 'Charts' and can be hosted in a known format as a 'chart repository'. The archives are versioned.

Helm is basically focussed on creating yaml documents that are submitted to Kubernetes - it is not involved in the runtime of a Kubernetes environment. Once a helm app is installed, interaction is just with the regular kubernetes objects.

[Helm Commands](https://helm.sh/docs/helm/helm/) include options to
* install
* uninstall
* list
* search
* upgrade
* rollback

## helm under microk8s

microk8s qualifies the Helm command `helm` in that you need to use `microk8s helm3` so either
* When docs refer you to type `helm` then just use `microk8s helm3`
* add a shell alias ie `alias helm='microk8s helm3'` into ~/.zshrc or equivilent shell startup script - if this doesn't clash with your other usage of k8s.

If using this approach you not need to explicitly install Helm.

## Installing Helm

Some Kubernetes environments may install helm as part of their client tooling, refer to the docs to see if this is the case, and run `helm version` to check - expect to use v3 or above. If so, install can be skipped.

### MacOS

If using macOS with HomeBrew installed, helm can be simply installed with
```shell
brew install helm
```

### Other platforms (Linux, Windows)

See the [Installation Guide](https://helm.sh/docs/intro/install/) for more ways to install Helm

## Accessing the egeria charts repository

Our helm charts for Egeria are stored in a repository hosted on GitHub. The source for these is at https://github.com/odpi/egeria-charts , and as charts are updated they are automatically published to a GitHub pages Website (in fact this one!)

Run the following to add this repository
```shell
helm repo add egeria https://odpi.github.io/egeria-charts
```

Before searching or installing, always update your local copy of the repository
```shell
helm repo update egeria
```
You can now list released charts:
```shell
helm search repo egeria
```

or development charts (being worked on, or using code from master)
```shell
helm search repo egeria --devel
```
and install a chart that looks interesting - 
```shell
helm install egeria/<chart>
```
----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
