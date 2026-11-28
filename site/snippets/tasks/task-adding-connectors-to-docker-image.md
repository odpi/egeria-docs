<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Adding connectors to a docker image

The [OMAG Server Platform](/concepts/omag-server-platform) in Egeria's docker image loads the implementations of [connectors](/concepts/connector) from the directories listed in the `LOADER_PATH` environment variable.  Its default value is `/deployments/lib,/deployments/extra`:

- `/deployments/lib` contains the connectors that are shipped with Egeria.
- `/deployments/extra` contains no connectors.  It is where connectors from other repositories (including those that you write yourself) are added.  The connectors available for Egeria are listed in the [Connector Catalog](/connectors).

A connector needs its own jar file plus the jar files of any third-party libraries that it uses that are not already part of the platform.  Some connectors are packaged with these libraries included in a single jar file - often with `jar-with-dependencies` in its name.  Do not add Egeria's own libraries since they are already part of the platform, and duplicate copies at a different release can cause unpredictable errors.  This is why connectors are built with a [`compileOnly` (Gradle) or `provided` (Maven) dependency](/guides/developer/integration-connectors/integration-connector-interface#dependencies) on Egeria's libraries.

There are two ways to add these jar files to a docker container: build a new docker image that includes them, or mount them into the container when it starts.

#### Building a docker image that includes additional connectors

Using Egeria's published `odpi/egeria-platform` image as the base for a new image creates a self-contained image that can be used wherever the original image is used, such as in a Kubernetes cluster.

Create a new directory and, inside it, a directory called `connectors` that holds the jar files for your connectors and their dependent libraries.  Then add a file called `Dockerfile` to the new directory with the following content, where `<release>` is the release of Egeria that your connectors are built for, such as `6.3`.

!!! example "Dockerfile"
    ```dockerfile linenums="1"
    FROM odpi/egeria-platform:<release>

    # Add the connectors, and the libraries they depend on, to the platform's class path
    COPY connectors/ /deployments/extra/
    ```

Since `/deployments/extra` is already listed in `LOADER_PATH`, there is no need to change it.  The platform runs as user `185` so the jar files must be readable by this user.  This is the case for files that are readable by all users on your machine.  Otherwise, change line 4 of the `Dockerfile` to `COPY --chmod=644 connectors/ /deployments/extra/`.

Build the image from the new directory, where `<tag>` is a tag name for your image:

!!! cli "Build a docker image that includes your connectors"
    ```shell
    docker build -t my-egeria-platform:<tag> .
    ```

The new image is started in the same way as Egeria's image:

!!! cli "Start a container from the new image"
    ```shell
    docker run -p 7443:7443 my-egeria-platform:<tag>
    ```

#### Mounting additional connectors into a docker container

During development, it is often quicker to keep the jar files on your machine and mount their directory into the container.  The value of `LOADER_PATH` is replaced to add the mounted directory to the platform's class path.  It is a comma-separated list, and must still include `/deployments/lib` because this directory holds the libraries that the platform needs to run.  The command below is issued from the directory that contains the `connectors` directory.

!!! cli "Start Egeria's image with the connectors mounted into the container"
    ```shell
    docker run -p 7443:7443 \
      -v "$(pwd)/connectors:/deployments/connectors:ro" \
      -e LOADER_PATH=/deployments/lib,/deployments/extra,/deployments/connectors \
      odpi/egeria-platform:<release>
    ```

As with a new image, the jar files must be readable by user `185`.  The same approach is used with *docker compose* and Kubernetes, where the jar files are supplied through a volume.

#### Checking the connectors are on the class path

The directories and jar files that are on the platform's class path are listed when the platform starts if the `loader.debug` property is set.  Since setting `JAVA_OPTS_APPEND` replaces its default value, the default (`-XX:MaxMetaspaceSize=1g`) is repeated in the example below.

!!! cli "Start a container that lists the platform's class path"
    ```shell
    docker run -p 7443:7443 \
      -e JAVA_OPTS_APPEND="-XX:MaxMetaspaceSize=1g -Dloader.debug=true" \
      my-egeria-platform:<tag>
    ```

Look for the `LOADER:` message that includes `Using class path URLs`.  It lists every jar file loaded from the directories in `LOADER_PATH`, so your connectors' jar files should be listed under `/deployments/extra` (or the directory you mounted).

Once the platform is running, the [getConnectorType](/services/platform-services/overview#supported-connectors) platform service confirms that a connector's provider class can be found on the platform's class path.
