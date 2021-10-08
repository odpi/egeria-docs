<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Development Tools

## Git and GitHub

*git* is an open source version control system. It is what we use to:

- Store all of our source code, documentation and other file-based resources.
- Track changes to the underlying Egeria code as the project evolves.
- Track issues and enhancements, and link these back to the code changes that resolve them.
- Collaborate on and review the issues, enhancements and code changes.

As a result, it gives us a definitive source for the latest and greatest source code for Egeria itself, its history, and the rationale behind various decisions that are made over time.

The Egeria project's git repositories are located on [GitHub :material-dock-window:](https://github.com/odpi){ target=gh }. GitHub is a free, public git service for sharing code and related files. It has a web interface to make it easier for the Egeria community to monitor the activity in the project and process new content.

### Repositories

| Repository | Purpose |
|---|---|
| [`egeria` :material-github:](https://github.com/odpi/egeria){ target=gh } | contains the core Egeria function along with samples, tutorials and documentation. |
| [`egeria-connector-xtdb` :material-github:](https://github.com/odpi/egeria-connector-xtdb){ target=gh } | contains a plugin repository connector to use [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb } as a pluggable back-end for an Egeria [metadata server](/egeria-docs/concepts/metadata-server). |
| [`egeria-connector-hadoop-ecosystem` :material-github:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=gh } | contains connectors to integrate technologies from the Hadoop ecosystem into the open metadata ecosystem. |
| [`egeria-connector-ibm-information-server` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=gh } | contains connectors to integrate IBM Information Server into the open metadata ecosystem. |
| [`data-governance` :material-github:](https://github.com/odpi/data-governance){ target=gh } | contains Egeria's Guidance on Governance (GoG) as well as large media files such as presentations and movies. |
| [`egeria-dev-projects` :material-github:](https://github.com/odpi/egeria-dev-projects){ target=gh } | contains fun projects for developers to help them learn about the Egeria technology. |
| [`egeria-palisade` :material-github:](https://github.com/odpi/egeria-palisade){ target=gh } | contains content from the collaboration between the Egeria project and the [Palisade :material-dock-window:](https://github.com/gchq/palisade){ target=palisade } project. |

All of these repositories are publicly visible; however, if you want to contribute new content then you need
to create a GitHub account. This can be done from [the top of the GitHub home page :material-dock-window:](https://github.com){ target=gh }.

!!! education "Further information"
    Interested to learn more?

    - GitHub provides some [great introductory guides to git :material-dock-window:](https://guides.github.com/introduction/git-handbook/){ target=gh }.
    - Egeria provides specific tutorials for [working with Egeria's git repositories](/egeria-docs/getting-started/tutorials/git-and-git-hub-tutorial).

## IntelliJ IDEA

[*IntelliJ IDEA* :material-dock-window:](https://www.jetbrains.com/idea/){ target=intellij } by JetBrains is the Interactive Development Environment (IDE) used by most of the Egeria developers. The community edition is free to use and covers all the function needed by an Egeria developer.

We provide [our own tutorial for IntelliJ](/egeria-docs/getting-started/tutorials/intellij-tutorial).

### Lombok Plugin

Egeria makes use of [Project Lombok :material-dock-window:](https://projectlombok.org){ target=lombok }. If using JetBrains IntelliJ IDEA ensure it has [the required plugin configured :material-dock-window](https://projectlombok.org/setup/intellij){ target=lombok }.

!!! attention "Don't detect generated sources"
    Also, before running a Maven build please choose **Don't detect** from the **Generated sources folders** dropdown in **Preferences** -> **Build, Execution, Deployment** -> **Build Tools** -> **Maven** -> **Importing**. This will avoid triggering a duplicate classes build error caused by the `delombok`ed sources folders being added as source folders for the Maven module.

    If this wasn't set when your project was initially setup, you may find that `delombok` directories are already present in IntelliJ's source path for some modules, leading to errors with duplicate classes.

    To check for any modules still refering to `delombok` you can run this at the command line, from your top-level source tree:

    !!! cli "Find any existing delombok source entries in IntelliJ"
        ```shell
        find . -name '*.iml' | xargs -n50 grep -y delombok
        ```

    If you find any hits such as:

    ```
    ./open-metadata-implementation/access-services/data-engine/data-engine-api/data-engine-api.iml:      <sourceFolder url="file://$MODULE_DIR$/target/delombok" isTestSource="false" />
    ```

    then either remove those lines **without** IntelliJ running, or go into **File** -> **Project Structure** -> **Modules**, and remove `target/delombok` from the **Source Folders** list

    Explanation: in addition to importing module defintions from the Maven `pom.xml`, IntelliJ also tries to look for any generated source. It finds the `delombok` directory, causing duplicates: in fact we only use this directory for generating Javadoc of lombok-enabled modules. Switching the setting / removing these source folders prevents these duplicate classes.

## Apache Maven

[Apache Maven :material-dock-window:](https://maven.apache.org/){ target=maven } is the tool that supports our project build. This includes the code compilation, running unit tests, validating dependencies and Javadoc as well as build our distribution archive.

Maven 3.5 or higher is required to build Egeria. 3.6.x or above is recommended.

The Maven processing organizes the modules into a hierarchy. Each module has a `pom.xml` file (called the *pom file*) that defines the artifact, its parent / children, dependencies and any special processing that the module builds. The *top-level pom file* is the `pom.xml` file at the root of the repository's source code directory structure.

When the Maven command is run, it passes through the hierarchy of modules multiple times. Each pass processes a particular lifecycle phase of the build (to ensure, for example, Java source files are compiled before the resulting object files are packaged into a jar file).

!!! tip "Maven repositories"
    This processing includes locating and downloading external libraries and dependencies, typically from an online open source repository called Maven Central. The directory where these external dependencies is stored locally is called `.m2`.

!!! cli "Rebuild the project with Maven"
    ```shell
    mvn clean install
    ```

The [building Egeria tutorial](/egeria-docs/getting-started/tutorials/building-egeria-tutorial) covers more details on the build process.

!!! cli "Check if Maven is installed"
    ```shell
    mvn --version
    ```

Install Maven using:

=== "MacOS"

    !!! cli "Install Maven through [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew install maven
        ```

=== "RedHat"

    !!! cli "Install through `yum`"
        ```shell
        yum install maven
        ```

=== "Debian"

    !!! cli "Install through `apt-get`"
        ```shell
        apt-get install maven
        ```

=== "Windows"

    On Windows, you should use [Windows Subsystem for Linux :material-dock-window:](https://docs.microsoft.com/en-us/windows/wsl/){ target=ms } Version 2 or above, install an appropriate Linux distribution, and follow the instructions for that Linux distribution.

Ensure you are using version 3.5.0 or higher in order to build Egeria.

## Gradle

[Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is an alternative build tool to Maven and offers:

- better support for parallel builds
- more flexibility for build tasks
- breaking the link between directory structure and maven artifacts
- extremely fast incremental builds

Our direction is for a Gradle build to replace Maven; however, [that work is still underway :material-dock-window:](https://github.com/odpi/egeria/issues/3370){ target=gh }. As such, our supported build environment remains [Maven](#apache-maven)

As of release 3.0, most components are building with gradle, but artifacts are not being created, and verification has not been done. Contributions to this work are welcome, as are issue reports!

No gradle installation is required, as we use the 'gradle wrapper' which will automatically install gradle if needed. This reduces the setup steps, and ensure everyone runs the same version of gradle (currently 7.02 in Release 3.0).

!!! cli "Rebuild the project with Gradle"
    ```shell
    ./gradlew build
    ```

--8<-- "snippets/abbr.md"
