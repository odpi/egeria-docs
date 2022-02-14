<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Building Egeria in IntelliJ IDEA

The build process is different for each git repository.  Click on the table for the repository that you are building:

=== "egeria.git"
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-git.md"
    
=== "egeria-samples.git" 
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-samples-git.md"

=== "egeria-dev-projects.git"
    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-dev-projects-git.md"


#### Using maven rather than using the IntelliJ build?

While you are working on code in IntelliJ, it will be continuously rebuilding
your code so that it is discovering syntax other coding errors as you type.
This is useful in getting a first pass of your code.

However, IntelliJ does not understand the egeria structure - only Maven
does, so the Maven build is important to to verify your changes are
OK at the project level.

---8<-- "snippets/abbr.md"
