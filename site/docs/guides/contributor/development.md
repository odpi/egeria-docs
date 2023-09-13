<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Tools for code contributors

## Git and GitHub

--8<-- "docs/education/tutorials/git-and-git-hub-tutorial/git-introduction.md"
--8<-- "docs/education/tutorials/git-and-git-hub-tutorial/egeria-git-repositories.md"

!!! education "Further information"
    Interested to learn more?

    - GitHub provides some [great introductory guides to git :material-dock-window:](https://guides.github.com/introduction/git-handbook/){ target=gh }.
    - Egeria provides specific tutorials for [working with Egeria's git repositories](/education/tutorials/git-and-git-hub-tutorial/overview).

## IntelliJ IDEA

[*IntelliJ IDEA* :material-dock-window:](https://www.jetbrains.com/idea/){ target=intellij } by JetBrains is the Interactive Development Environment (IDE) used by most of the Egeria developers. The community edition is free to use and covers all the function needed by an Egeria developer.

We provide [our own tutorial for IntelliJ](/education/tutorials/intellij-tutorial/overview).

## Build tools

The build process takes the source files from the git repository and creates executable libraries needed to run Egeria. When you download (clone) the contents of a git repository from GitHub, a new directory is created that is named after the repository that you cloned. For example, the directory created when the main `egeria.git` repository is cloned is called `egeria`.  This directory contains all the source and the build scripts.

The project uses three main build technologies:

* [Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is the primary build tool for the Egeria repositories.
* [Apache Maven :material-dock-window:](https://maven.apache.org/){ target=maven } is an alternative build tool to Gradle and is being phased out.
* [npm :material-dock-window:](https://www.npmjs.com){ target=npm } is used for Javascript repositories associated with the User Interfaces.

The build scripts that use these technologies ensure the software is built in the correct order.

##### Building with Gradle

--8<-- "snippets/tasks/task-building-with-gradle.md"

??? tip "Gradle development"
    For egeria [Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is a replacement build tool to Maven and offers:

    - better support for parallel builds
    - more flexibility for build tasks
    - breaking the link between directory structure and maven artifacts
    - extremely fast incremental builds

    As of version 4, Egeria can only be built using gradle.

##### Building with Maven

If building a version of Egeria prior to version 4, the maven instructions can be found below:

--8<-- "snippets/tasks/task-building-with-maven.md"


--8<-- "snippets/abbr.md"
