<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Building utilities with Egeria

To create a Java utility that calls Egeria's OMAG Server Platform:

* To configure it or the OMAG Servers that run on it - using the administration services clients, such as `MetadataAccessStoreConfigurationClient` and `ViewServerConfigurationClient`.
* To start or stop servers - using `PlatformServicesClient` (`activateWithStoredConfig`, `shutdownServer`, ...).
* To query the status of the platform and its servers - using `PlatformServicesClient` and `ServerOperationsClient`.
* To retrieve or update metadata - using the [Open Metadata Framework (OMF)](/frameworks/omf/overview) handlers and the `EgeriaOpenMetadataStoreClient`.

it is necessary to create a Java program with a `main()` method that includes the appropriate clients and API modules from Egeria and is packaged in a jar file.  The clients are described in [Java clients](/guides/developer/java-clients/overview).  If your utility is not written in Java, call the [REST APIs](/guides/developer/rest-apis) of the view services directly, or use the [python client](/guides/developer/python-clients/overview).

The sections that follow take you through the common tasks involved in building a utility using the IntelliJ IDEA IDE and Apache Maven.  Egeria's own build uses Gradle, and the published Egeria libraries work equally well from a Gradle build - see the tip at the end of [Creating a Maven POM file](#creating-a-maven-pom-file).

### Creating a new project

The project manages the files for your utility.

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-new-project.md"

### Creating a new java package

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-package.md"

### Creating a new java class

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-class.md"

### Creating a Maven POM file

---8<-- "docs/guides/developer/building-utilities/creating-pom-file-in-intellij.md"

---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-as-maven-project.md"

### Configuring logging and certificate checking

Most utilities also need a logging destination and, in a development environment, a way to accept the platform's self-signed certificate:

* [Configuring Logback](/guides/developer/logback/overview)
* [Using HTTP Helper](/guides/developer/http-helper/overview)


--8<-- "snippets/abbr.md"