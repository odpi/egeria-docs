<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


### Installing Intellij

Go to 
```
https://www.jetbrains.com/idea/
```
and watch the **Take a Tour** video if you are not familiar with IntelliJ.
You can download IntelliJ from this site:
```
https://www.jetbrains.com/idea/download/index.html
```

#### Setting up Lombok Plugin

Egeria makes use of [Project Lombok :material-dock-window:](https://projectlombok.org){ target=lombok }. If using JetBrains IntelliJ IDEA ensure it has [the required plugin configured :material-dock-window;](https://projectlombok.org/setup/intellij){ target=lombok }.

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

---8<-- "snippets/abbr.md"
