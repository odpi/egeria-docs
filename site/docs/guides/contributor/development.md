<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Tools for code contributors

## Git and GitHub

--8<-- "docs/education/tutorials/git-and-git-hub-tutorial/git-introduction.md"
--8<-- "docs/education/tutorials/git-and-git-hub-tutorial/egeria-git-repositories.md"

!!! education "Further information"
    Interested to learn more?

    - GitHub provides some [great introductory guides to git :material-dock-window:](https://guides.github.com/introduction/git-handbook/){ target=gh }.
    - Egeria provides specific tutorials for [working with Egeria's git repositories](/egeria-docs/education/tutorials/git-and-git-hub-tutorial/overview).

## IntelliJ IDEA

[*IntelliJ IDEA* :material-dock-window:](https://www.jetbrains.com/idea/){ target=intellij } by JetBrains is the Interactive Development Environment (IDE) used by most of the Egeria developers. The community edition is free to use and covers all the function needed by an Egeria developer.

We provide [our own tutorial for IntelliJ](/egeria-docs/education/tutorials/intellij-tutorial/overview).

## Apache Maven and Gradle

[Apache Maven :material-dock-window:](https://maven.apache.org/){ target=maven } is the tool that supports our project build. This includes the code compilation, running unit tests, validating dependencies and Javadoc as well as build our distribution archive.

Maven 3.5 or higher is required to build Egeria. 3.6.x or above is recommended.

[Gradle :material-dock-window:](https://gradle.org/){ target=gradle } is an alternative build tool to Maven and offers:

- better support for parallel builds
- more flexibility for build tasks
- breaking the link between directory structure and maven artifacts
- extremely fast incremental builds

Our direction is for a Gradle build to replace Maven; however, [that work is still underway :material-dock-window:](https://github.com/odpi/egeria/issues/3370){ target=gh }. As such, our supported build environment remains [Maven](#apache-maven)

The [building Egeria tutorial](/egeria-docs/education/tutorials/building-egeria-tutorial/overview) covers more details on the build process.

--8<-- "snippets/abbr.md"
