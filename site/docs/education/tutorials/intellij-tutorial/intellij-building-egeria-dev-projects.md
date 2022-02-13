<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


### Building egeria-dev-projects.git

Maven is accessed from a sidebar menu in IntelliJ.

![Maven Sidebar](/education/tutorials/intellij-tutorial/intellij-maven-sidebar-menu.png)

When you click on the **Maven** label, a panel opens with the list of modules in the git repository is displayed.  The maven:

The `egeria-dev-projects.git` repository has a top-level pom file so all of the modules can be built using one command.  

Select the **M** button at the top of the maven panel for `Execute Maven Goal`.
    
![Maven build opens](/education/tutorials/intellij-tutorial/intellij-run-maven-option.png)
    
Then the `Execute Maven Goal` dialog box opens to enter your command `clean install` and press `Execute`.

The build kicks off in a new pane (typically at the bottom of your intelliJ window).  

The build can take a few minutes depending on the speed/load on your machine.  However eventually you will see the message:

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


#### Using maven rather than using the IntelliJ build?

While you are working on code in IntelliJ, it will be continuously rebuilding
your code so that it is discovering syntax other coding errors as you type.
This is useful in getting a first pass of your code.

However, IntelliJ does not understand the egeria structure - only Maven
does, so the Maven build is important to to verify your changes are
OK at the project level.

### Building egeria-samples.g

Maven is accessed from a sidebar menu in IntelliJ.

![Maven Sidebar](/education/tutorials/intellij-tutorial/intellij-maven-sidebar-menu.png)

When you click on the **Maven** label, a panel opens with the list of modules in the git repository is displayed.  The maven:

The `egeria-samples.git` repository does not have a top-level pom file.  Each sample is built separately. 
    
Go to the module of the sample that you are interested in. Open up the content for the module and then the lifecycle folder.

![Maven module options](/education/tutorials/intellij-tutorial/intellij-maven-module-lifecycle-values.png)

First double-click on `clean` and the build of that module runs.

Once the clean is complete, double-click on `install` and the build of that module starts.


The build kicks off in a new pane (typically at the bottom of your intelliJ window).  

The build takes a few minutes  depending on the the speed/load on your machine.  However eventually you will see the message:

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

---8<-- "snippets/abbr.md"
