<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Resolve external dependencies

Once the pom.xml file is imported into the IntelliJ project, IntelliJ uses its information to resolve the package names of the Egeria classes included in your code.  Classes that have an unknown package are shown in red.  

Go to your Java class in the editor and click on a class name shown in red.  If IntelliJ has located the class in the dependent modules, it adds an underline to the class name and the hover text shows the suggested class. 

![Select class](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-1.png)

Use Option plus Return keys to add the package name to the top if the class.  The class name is shown in white. 

![Accept recommendation](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-2.png)

The package name of the class is added as an import statement at the top of the file.

![See new import statement](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-3.png)

Repeat this process until all classes are resolved.


