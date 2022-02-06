<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Building the Egeria Source

The build process takes the source files from the git repository and creates executable libraries needed to run Egeria.  

#### Supported Platforms

Egeria currently supports building on *nix, Linux & Linux-like operating systems such as MacOS.
     
Our official build pipelines are based on x86_64 architecture, but it is expected the build will run on other architectures, subject to the availability of the required tools and interpreters/jvms/runtimes on that platform (for example Java, Python, Docker/containerd/k8s etc).
     
On Windows, you should use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) Version 2 or above, and install a Linux distribution such as Ubuntu. This avoids issues we have seen with path separators, symbolic links, slow I/O performance, long path names. 
     
Some IDEs such as JetBrains IntelliJ and Microsoft VisualCode will run the GUI in Windows natively, and then use a linux environment (via WSL2 - which uses a real Linux kernel) to perform build and execution

#### Running the build

When you download (clone) the contents of a git repository  from GitHub, a new directory is created that is named after the repository that you cloned. For example, the directory created when the main `egeria.git` repository is cloned is called `egeria`.  This directory contains all of the source and the build scripts.

The project uses three main build technologies:

* [Apache Maven :material-dock-window:](https://maven.apache.org/){ target=maven }
* [Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is an alternative build tool to Maven and is the future direction for Egeria.
* [npm](https://www.npmjs.com){ target=npm } is used for Javascript repositories associated with the User Interfaces.

The build scripts that use these technologies ensure the software is built in the correct order.  

##### Building with Maven

Maven is used to build the following repositories:

* egeria.git
* egeria-samples.git
* egeria-dev-projects.git

The Maven processing organizes the modules into a hierarchy. Each module has a `pom.xml` file (called the *pom file*) that defines the artifact, its parent / children, dependencies and any special processing that the module builds. The *top-level pom file* is the `pom.xml` file at the root of the repository's source code directory structure.

When the Maven command is run, it passes through the hierarchy of modules multiple times. Each pass processes a particular lifecycle phase of the build (to ensure, for example, Java source files are compiled before the resulting object files are packaged into a jar file).

!!! tip "Maven repositories"
    This processing includes locating and downloading external libraries and dependencies, typically from an online open source repository called Maven Central. The directory where these external dependencies is stored locally is called `.m2`.

!! cli "Rebuild a module with Maven"
    From the module's directory issue command:
    ```shell
    mvn clean install
    ```

=== "egeria.git"

    The `egeria.git` repository has a top-level pom file so all of the modules can be built using one `mvn clean install` command from the top-level `egeria` directory.  

=== "egeria-samples.git"

    The `egeria-samples.git` repository does not have a top-level pom file.  Each sample is built separately. When you want to build a sample, change to the sample's directory where the `pom.xml` file is located and issue `mvn clean install`.  

=== "egeria-dev-projects.git"

    The `egeria-dev-projects.git` repository has a top-level pom fileo all of the modules can be built using one `mvn clean install` command from the top-level `egeria-dev-projects` directory.  

The build can take 15 minutes to over an hour depending on the repository and on the speed/load on your machine.  However eventually you will see the message:

```text
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 54:54 min
[INFO] Finished at: 2020-01-29T09:33:17Z
[INFO] Final Memory: 171M/3510M
[INFO] ------------------------------------------------------------------------

Process finished with exit code 0
```

##### Building with Gradle

[Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is an alternative build tool to Maven and offers:

- better support for parallel builds
- more flexibility for build tasks
- breaking the link between directory structure and maven artifacts
- extremely fast incremental builds

Our direction is for a Gradle build to replace Maven; however, [that work is still underway :material-dock-window:](https://github.com/odpi/egeria/issues/3370){ target=gh }. As such, our supported build environment remains [Maven](#building-with-maven)

As of release 3.0, most components are building with gradle, but artifacts are not being created, and verification has not been done. Contributions to this work are welcome, as are issue reports!

No gradle installation is required, as we use the 'gradle wrapper' which will automatically install gradle if needed. This reduces the setup steps, and ensure everyone runs the same version of gradle (currently 7.02 in Release 3.0).

!!! cli "Rebuild a project with Gradle"
    ```shell
    ./gradlew build
    ```



--8<-- "snippets/abbr.md"
