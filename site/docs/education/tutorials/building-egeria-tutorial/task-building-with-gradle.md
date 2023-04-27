<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

[Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is used to build the following repositories:

* egeria.git - main Egeria libraries.
* egeria-dev-projects.git - utilities and connectors for developers to use and develop further.

The Gradle processing works through the project modules. Each module has a `build.gradle` file that defines the artifact, its dependencies and any special processing that the module builds. The top-level `build.gradle` file at the root of the repository's source code directory structure controls the overall process.

Gradle runs the build in parallel threads so be sure any test cases are independent of one another.

!!! tip "Maven repositories"
    This processing includes locating and downloading external libraries and dependencies, typically from an online open source repository called Maven Central and our snapshot repository on https://oss.sonatype.org, so make sure you are online when you run the build.

No gradle installation is required, as we use the 'gradle wrapper' which will automatically install gradle if needed. This reduces the setup steps, and ensure everyone runs the same version of gradle.

=== "Rebuild a project with Gradle"
    ```shell
    ./gradlew build
    ```

=== "Quick build"
    The quick build skips generation of javadoc, and tests
    ```shell
    ./gradlew build -x test -x javadoc
    ```

=== "Flexible platform option (egeria.git only)"
    This build option creates an [OMAG Server Platform](/concepts/omag-server-platform) where the [registered services](/concepts/omag-subsystem/#registered-services) are optional.  The OMAG Server Platform loads the registered services it finds on the loader path specified with the `-Dloader.path={directoryName}` option of its startup command.  Use this option if you want to remove the registered services that you are not using, or you would like introduce your own registered services.

    ```shell
    ./gradlew -PadminChassisOnly build 
    ```

The build can take 15 minutes to over an hour depending on the repository and on the speed/load on your machine.  However eventually you will see the message:

```text
BUILD SUCCESSFUL in 10s
3 actionable tasks: 1 executed, 2 up-to-date
```


