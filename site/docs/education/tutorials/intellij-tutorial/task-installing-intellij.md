<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Installing Intellij 

Link to the [download](https://www.jetbrains.com/idea/download/) page and follow the instructions.

Start up IntelliJ.

??? tip "Set up Java ..."
    Validate that the project is set up with the right level of Java - you need Java 17.  Select `File` and then `Project Structure...`.  When the wizard opens select `Project` and ensure the SDK is Java 17.

    ![Set Java level](/education/tutorials/intellij-tutorial/intellij-set-java-level.png)

??? tip "Set up Maven ..."
    Set up Maven to the version that you downloaded by selecting `Preferences ...` from the `IntelliJ IDEA` menu and then `Build, Execution, Deployment` followed by `Build Tools` followed by `Maven` in the left-hand menu of the resulting wizard. Ensure the `Maven Home Directory` points to a level of Maven that is at least version `3.5.0`.

    ![Set up Maven level](/education/tutorials/intellij-tutorial/intellij-set-maven-level.png) 

    The three dots after the directory name enables you to select your Maven install directory.

??? tip "Ensure you have enough memory ..."
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-memory-settings.md"

??? tip "Check your lombok setup"
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-lombok-plugin.md"

---8<-- "snippets/abbr.md"
