<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Helm

!!! quote "[Official description](https://helm.sh){ target=helm }"
    Helm is the best way to find, share, and use software built for Kubernetes.

## Deploying apps in Kubernetes

In Kubernetes, resources such as pods (to run code) or services (for network accessibility) are defined in YAML. One or more documents can be submitted at a time.

So we might have one YAML file that defines our pod - with information about which container images to run, and another to setup a network service. Finally, we may have another that describes our storage requirements (a persistent volume claim).

## What does Helm do?

Helm provides a way of bundling YAML files together into an archive, together with a templating mechanism to allow reuse of common patterns and ensure different YAMLs are consistent and can reference each other.

These archives are known as *charts* and can be hosted in a known format as a *chart repository*. The archives are versioned.

Helm is basically focussed on creating YAML documents that are submitted to Kubernetes - it is not involved in the runtime of a Kubernetes environment. Once a Helm app is installed, interaction is just with the regular kubernetes objects.

[Helm commands :material-dock-window:](https://helm.sh/docs/helm/helm/){ target=helm } include options to:

- install
- uninstall
- list
- search
- upgrade
- rollback

!!! attention "Helm under microk8s"
    microk8s qualifies the Helm command `helm` in that you need to use `microk8s helm3` so either:

    - When docs refer you to type `helm` then just use `microk8s helm3`
    - Add a shell alias such as `alias helm='microk8s helm3'` into `~/.zshrc` or equivalent shell startup script - if this doesn't clash with your other usage of k8s.

    If using this approach you not need to explicitly install Helm.

## Installing Helm

Some Kubernetes environments may install Helm as part of their client tooling, refer to the docs to see if this is the case, and run `helm version` to check - expect to use v3 or above. If so, install can be skipped.

### MacOS

If using MacOS with HomeBrew installed, Helm can be simply installed with:

!!! cli "Installing Helm on MacOS"
    ```shell
    brew install helm
    ```

### Other platforms (Linux, Windows)

See the [Installation Guide :material-dock-window:](https://helm.sh/docs/intro/install/){ target=helm } for more ways to install Helm.

## Accessing the Egeria charts repository

Our Helm charts for Egeria are stored [in a repository hosted on GitHub :material-github:](https://github.com/odpi/egeria-charts){ target=gh }, and as charts are updated they are automatically published to a GitHub pages website.

Start by adding this repository to Helm:

!!! cli "Add this repository"
    ```shell
    helm repo add egeria https://odpi.github.io/egeria-charts
    ```

Before searching or installing, always update your local copy of the repository to ensure you have the latest version of the charts:

!!! cli "Update charts"
    ```shell
    helm repo update egeria
    ```

You can now list the charts:

!!! cli "List released charts"
    ```shell
    helm search repo egeria
    ```

!!! cli "List charts that are still in development"
    ```shell
    helm search repo egeria --devel
    ```

And you can then install (deploy) a chart:

!!! cli "Install (deploy) a chart"
    ```shell
    helm install egeria/<chart>
    ```

---8<-- "snippets/abbr.md"
