<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# Helm

!!! quote "[Official description](https://helm.sh){ target=helm }"
    Helm is the best way to find, share, and use software built for Kubernetes.

## Deploying apps in Kubernetes

In Kubernetes, resources such as pods (to run code) or services (for network accessibility) are defined in YAML. One or more documents can be submitted at a time.

So we might have one YAML file that defines our pod - with information about which container images to run, and another to set up a network service. Finally, we may have another that describes our storage requirements (a persistent volume claim).

## What does Helm do?

Helm provides a way of bundling YAML files together into an archive, together with a templating mechanism to allow reuse of common patterns and ensure different YAMLs are consistent and can reference each other.

These archives are known as **charts** and can be hosted in a known format as a **chart repository**. The archives are versioned.

Helm is basically focussed on creating YAML documents that are submitted to Kubernetes - it is not involved in the runtime of a Kubernetes environment. Once a Helm app is installed, interaction is just with the regular kubernetes objects.

[Helm commands :material-dock-window:](https://helm.sh/docs/helm/helm/){ target=helm } include options to perform the following actions on these charts (application packages):

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

For example if you followed the instructions earlier to install **Rancher Desktop** or **microk8s** Helm will already be installed, and no action is needed.


### MacOS

If using MacOS with HomeBrew installed, Helm can be simply installed with:

!!! cli "Installing Helm on MacOS"
    ```console
    brew install helm
    ```

### Other platforms (Linux, Windows)

See the [Installation Guide :material-dock-window:](https://helm.sh/docs/intro/install/){ target=helm } for more ways to install Helm.

## Useful Helm commands

This section covers some useful commands for Helm. Do not run these now, but they
may be useful to refer to as you use the Egeria Helm charts.

It's also worth remember that Helm is primarily a packaging tool to deploy applications to Kubernetes,
so these commands relate mostly to installing and removing applications.

To actual monitor the details of what has been created - what is running, the network services etc, then you 
would use the Kubernetes command `kubectl`

Our Helm charts for Egeria are stored [in a repository hosted on GitHub :material-github:](https://github.com/odpi/egeria-charts){ target=gh }, and as charts are updated they are automatically published to a GitHub pages website.

Start by adding this repository to Helm. This is essential to be able to access them.

!!! cli "Add this repository"
    ```console
    helm repo add egeria https://odpi.github.io/egeria-charts
    ```

Before searching or installing, always update your local copy of the repository to ensure you have the latest version of the charts:

!!! cli "Update charts"
    ```console
    helm repo update egeria
    ```

You can now list the charts:

!!! cli "List released charts"
    ```console
    helm search repo egeria
    ```

!!! cli "List charts that are still in development"
    ```console
    helm search repo egeria --devel
    ```

And you can then install (deploy) a chart:

!!! cli "Install (deploy) a chart"
    ```console
    helm install <release> egeria/<chart>
    ```
    release here refers to a user-defined label which is used as part of the naming for many of the resources
    created

!!! cli "List installed charts"
    ```console
    helm list
    ```

    
!!! cli "Delete an installed helm chart"
    ```console
    helm delete <release>
    ```
  
  In a helm chart the configuration that has been externalised by the chart writer is specified in the `values.yaml` file which you can find in this directory. However rather than edit this file directly, it's recommended you create an additional file with the required overrides.

As an example, in `values.yaml` we see a value 'serverName' which is set to mds1. If I want to override this I could do

!!! cli "Install a chart with additional properties set"
    ```console
    helm install --set-string egeria.serverName=myserver <release> egeria/<chart>
    ```

However, this can get tedious with multiple values to override, and you need to know the correct types to use.

Instead, it may be easier to create an additional file. For example let's create a file in my home directory `~/egeria.yaml` containing:
```yaml
egeria:
  serverName: metadataserver
  viewServerName: presentationview
```

!!! cli "Install a chart with additional properties in a modified yaml"
    ```console
    helm install -f ~/egeria.yaml metadataserver egeria/egeria-base
    ```

You can find out all the configurable values for a chart by running:

!!! cli "List configurable values for chart"
    ```shell
    helm inspect values <chart>
    ```
---8<-- "snippets/abbr.md"
