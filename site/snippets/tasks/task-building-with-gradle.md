<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The [Gradle :material-dock-window:](https://gradle.org/){ target=gradle } processing works through the project modules. Each module has a `build.gradle` file that defines the artifact, its dependencies and any special processing that the module builds. The top-level `build.gradle` file at the root of the repository's source code directory structure controls the overall process. It runs the build in parallel threads to speed up the process of the build, but may take many cycles of your machine's capacity.  When it is running, it may be a good time for a break!

!!! tip "Maven repositories"
    This processing includes locating and downloading external libraries and dependencies, typically from an online open source repository called Maven Central and our snapshot repository on https://oss.sonatype.org, so make sure you are online when you run the build.

No gradle installation is required, as we use the 'gradle wrapper' which will automatically install gradle if needed. This reduces the setup steps, and ensure everyone runs the same version of gradle.

=== "Rebuild a project with Gradle"
    This is a regular incremental build, but will also run all tests and generate javadoc.
    ```shell
    ./gradlew build
    ```

=== "Quick build"
    The quick build skips generation of javadoc, and tests
    ```shell
    ./gradlew build -x test -x javadoc
    ```

=== "Full clean build"
     We avoid any use of cache, and ensure a full clean build. This may be needed when you want to recheck something that has no changed sources, but needs a rebuild -- for example to review compiler warning messages (not errors)
    ```shell
    ./gradlew clean build --no-build-cache
    ```

=== "Flexible platform option (egeria.git only)"
    This build option creates an [OMAG Server Platform](/concepts/omag-server-platform) where the [registered services](/concepts/omag-subsystem/#registered-services) are optional.  The OMAG Server Platform loads the registered services it finds on the loader path specified with the `-Dloader.path={directoryName}` option of its startup command.  Use this option if you want to remove the registered services that you are not using, or you would like introduce your own registered services.

    ```shell
    ./gradlew -PadminChassisOnly build 
    ```

The build will typically take from seconds to 10 minutes depending on the speed of your machine and the number of projects that need to be built.

```text
BUILD SUCCESSFUL in 4m 51s
3290 actionable tasks: 3172 executed, 118 up-to-date
```


