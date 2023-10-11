<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Egeria Server Starter chart (egeria-server)

Egeria Server Starter helm chart defines minimal deployment resources to demonstrate simple single OMAG Server Kubernetes deployment scenario.

It produces following resources:

- Deployment resource to describe the containers and related resources such as volumes;
- Configuration resources to describe environment configuration and application configuration files;
- Volumes to mapping configuration files to the container;
- Service that exposes the container port for external consumption.

The chart can be used as a base to build more complex deployment topologies.

## Configuration

The container application is configured using standard deployment and config map resources customized by setting the values in 'app' map. See [values.yaml](https://github.com/odpi/egeria-charts/blob/main/charts/egeria-server/values.yaml){ target=gh }

``````yaml
app:
  jarPath: "/deployments/server"
  jarName: "omag-server"
  loaderPath: "/deployments/server/lib"
  configPath: "/deployments/server/conf"
  configName: "cocoMDS1.yml"
  livenessProbe: "/actuator/health/livenessState"
  readinessProbe: "/actuator/health/readinessState"
``````

| Name | Description |
|------|-------------|
|`app.jarPath` | The path where the boot jar application is located inside the image.|
|`app.jarName` | The name of the boot jar available on the `app.jarPath` location in the image. |
|`app.loaderPath` | The spring boot application `LOADER_PATH`. This is the classpath location for Egeria connector libraries and additional third party libraries to be loaded at runtime. |
|`app.configPath` | The location where configuration files will be located. Note this location is used as volume mount path inside the container. |
|`app.configName` | The name of the configuration file (json or yaml) that will be loaded from `app.configPath` by the OMAG server instance on start-up. |
|`app.livenessProbe` and `app.readinessProbe` | Standard kubernetes pod [probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/){ target=_blank } representing liveness and readiness states respectively. |

For demo purpose, the chart contains example configuration files located in the [files](https://github.com/odpi/egeria-charts/tree/main/charts/egeria-server/files){ target=gh } directory. The files placed here will be always copied as config map resources and mounted inside the container at location defined by `app.configPath`. From here, the server is trying to load the file defined by `app.configName` value.

For more technical details check out the [config.yaml](https://github.com/odpi/egeria-charts/blob/main/charts/egeria-server/templates/config.yaml){ target=gh } and [deployment.yaml](https://github.com/odpi/egeria-charts/blob/main/charts/egeria-server/templates/deployment.yaml){ target=gh } resources.

The container is configured to use Egeria main docker image. By modifying the default container entry point variable we are able to create new runtime environment similar to the standard OMAG platform deployment. The main [docker image](/guides/operations/kubernetes/container-images/) contains full egeria project assembly making it convenient for demo and testing.

## Installation

From helm repository:

```bash
helm repo add egeria https://github.com/odpi/egeria-charts.git
helm repo update
helm install mds1 egeria/egeria-server 
```

or locally, using git clone:

```bash
git clone https://github.com/odpi/egeria-charts.git
cd egeria-charts
helm install mds1 charts/egeria-server -f charts/egeria-server/values.yaml
```

If installation for application instance with name `mds1` is successful, helm produces following output:

```bash
NAME: mds1
LAST DEPLOYED: Thu Sep 21 10:55:30 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Egeria project.

1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=egeria-server,app.kubernetes.io/instance=mds1" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```

!!! tip "Copy/paste the output above to your bash terminal to create port-forwarding rule to the container port instantly"

To uninstall run:

```bash
helm uninstall mds1
```

## Accessing the OMAG Server

To access the OMAG server via HTTP in a local kubernetes deployment, you can leverage `kubectl port-forward` steps described in the output info above.

Or following the example steps:

```bash
> kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
mds1-egeria-server-56fd5cb898-nzdx5   0/1     Running   0          8s
```

```bash
> kubectl port-forward mds1-egeria-server-56fd5cb898-nzdx5 8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

At this point, the OMAG server should already be responding via HTTP host address/port:

```bash
> curl http://localhost:8080/actuator/health
{"status":"UP","components":{"livenessState":{"status":"UP"},"readinessState":{"status":"UP"}},"groups":["liveness","readiness"]}
```

For real production deployments, depending on what is available for your K8S environment you will probably leverage different mechanism to expose the service like ingress or static routes.
