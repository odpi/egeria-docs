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

--8<-- "docs/education/tutorials/building-egeria-tutorial/task-building-with-maven.md"


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
