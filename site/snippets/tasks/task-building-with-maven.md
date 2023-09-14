<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Prior to V4.0 Maven is used to build the following repositories:

* egeria.git - main Egeria libraries.
* egeria-samples.git - coded samples of using Egeria.
* egeria-dev-projects.git - utilities and connectors for developers to use and develop further.

The Maven processing organizes the modules into a hierarchy. Each module has a `pom.xml` file (called the *pom file*) that defines the artifact, its parent / children, dependencies and any special processing that the module builds. The *top-level pom file* is the `pom.xml` file at the root of the repository's source code directory structure.

When the Maven command is run, it passes through the hierarchy of modules multiple times. Each pass processes a particular lifecycle phase of the build (to ensure, for example, Java source files are compiled before the resulting object files are packaged into a jar file).

!!! tip "Maven repositories"
    This processing includes locating and downloading external libraries and dependencies, typically from an online open source repository called Maven Central. The directory where these external dependencies is stored locally is called `.m2`.

??? tip "Installing Maven"
    --8<-- "snippets/tasks/task-installing-maven.md"

!! cli "Rebuild a module with Maven"
    From the module's directory issue command:
    ```shell
    mvn clean install
    ```

=== "egeria.git"

    The `egeria.git` repository has a top-level pom file so all of the modules can be built using one `mvn clean install` command from the top-level `egeria` directory.  There is also a quick build option for people just wishing to use Egeria rather than make changes - enter `mvn clean install -P quick -D skipFVT`

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


