<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


### Building egeria.git

??? attention "Check your lombok setup"
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-lombok-plugin.md"

Maven is accessed from a sidebar menu in IntelliJ.

![Maven Sidebar](/education/tutorials/intellij-tutorial/intellij-maven-sidebar-menu.png)

When you click on the **Maven** label, a panel opens with the list of modules in the git repository is displayed.

Chose the build option for your work ...

=== "Full Project Build"
    The `egeria.git` repository has a top-level pom file so all of the modules can be built using one command.
 
    Select the **M** button at the top of the maven panel for `Execute Maven Goal`.

    ![Maven build opens](/education/tutorials/intellij-tutorial/intellij-run-maven-option.png)

    Then the `Execute Maven Goal` dialog box opens to enter your command `clean install` command.  
    
=== "Quick Build"
    The `egeria.git` repository has a top-level pom file so all of the modules can be built using one command.
 
    Select the **M** button at the top of the maven panel for `Execute Maven Goal`.

    ![Maven build opens](/education/tutorials/intellij-tutorial/intellij-run-maven-option.png)

    Then the `Execute Maven Goal` dialog box opens to enter your command `clean install -P quick -D skipFVT`.  This skips all of the verification of the project files and running tests.  It is suitable for development projects (such when running the dojo).  However, if you are experiencing problems with building this repository, use the full build option to verify the project directories.

=== "Building a single Egeria module"
    If you are making small changes, you may wish to simply rebuild a single module.

    Goto the maven sidebar panel and find the module you are interested in.  Open up the content for the module and then the lifecycle folder.

    ![Maven module options](/education/tutorials/intellij-tutorial/intellij-maven-module-lifecycle-values.png)

     First double-click on `clean` and the build of that module runs.

     Once the clean is complete, double-click on `install` and the build of that module starts.

     Note: this option does not rebuild the assembly and so if you are using the OMAG Server Platform from the assembly to test your changes, you may need to do a full build to incorporate your change into the platform. 


The build kicks off in a new pane (typically at the bottom of your intelliJ window).  

The build can take 15 minutes to over an hour depending on the speed/load on your machine.  However eventually you will see the message:

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
