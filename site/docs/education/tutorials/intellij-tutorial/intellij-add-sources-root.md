<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

You need to change what is called the *Sources Root* of your project to allow Maven to correctly build your code.

Right-mouse click on `src` and select `Mark Directory as` then `Unmark Sources Root` on the sub menu.  The folder icon of `src` goes grey.

![Step 1](/education/tutorials/intellij-tutorial/intellij-unmark-as-sources-root.png)

Right-mouse click on `src` again and select `New` then `Directory`.  
![Step 2](/education/tutorials/intellij-tutorial/intellij-add-directory-1.png)

A pop-up box appears asking for the name of the directory. Enter the directory name of `main/java`.
![Step 3](/education/tutorials/intellij-tutorial/intellij-add-directory-2.png)

Navigate down the tree to the new `java` directory.  Right-mouse click on `java` and select `Mark Directory as` then `Sources Root` on the sub menu.  The folder icon of `java` goes blue.
![Step 4](/education/tutorials/intellij-tutorial/intellij-mark-as-sources-root.png)


