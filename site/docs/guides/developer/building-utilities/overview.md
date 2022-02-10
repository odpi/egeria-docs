<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Building utilities with Egeria

To create a utility that calls Egeria's OMAG Server Platform:

* To Configure it or OMAG Servers to run on it
* To start or stop servers
* To query the status of the platform and its servers
* To retrieve or update metadata

it is necessary to create a Java program with a `main()` method that includes the appropriate clients and API modules from Egeria and is packaged in a jar file.  

The sections that follow take you through the common tasks involved in building a utility using the IntelliJ IDEA IDE.

### Creating a new project

The project manages the files for your utility.

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-new-project.md"

### Creating a new java package

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-package.md"

### Creating a new java class

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-class.md"

### Creating a Maven POM file


--8<-- "snippets/abbr.md"