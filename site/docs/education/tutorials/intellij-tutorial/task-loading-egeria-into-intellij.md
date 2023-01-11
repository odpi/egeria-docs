<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Loading Egeria into IntelliJ IDEA

Once you have a copy of a git repository on your local disk you can load the contents into IntelliJ.

Go to the **File** menu and select **Open**

![File->Open menu](/education/tutorials/intellij-tutorial/intellij-file-open.png)

Then select the top-level directory that was created when you cloned the git repository.

![Select clone directory](/education/tutorials/intellij-tutorial/intellij-select-clone-directory.png)

You may be warned about loading egeria in which case select `Trust Project`:

![Trust Project](/education/tutorials/intellij-tutorial/intellij-trust-project.png)

If asked which build approach to use, select Maven:

![Import Maven Project](/education/tutorials/intellij-tutorial/intellij-import-maven-project.png)

IntelliJ will then start reading the git repository and creating a project. This may take a few minutes so be patient.

Validate that the project is set up with the right level of Java - you need Java 11.  Select `File` and then `Project Structure...`.  When the wizard opens select `Project` and ensure the SDK is Java 11.

![Set Java level](/education/tutorials/intellij-tutorial/intellij-set-java-level.png)


---8<-- "snippets/abbr.md"