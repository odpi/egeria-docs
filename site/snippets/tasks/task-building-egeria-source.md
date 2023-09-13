<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Building the Egeria Source

When you download (clone) the contents of the egeria.git repository from GitHub, a new directory is created that is named after the repository that you cloned. So the directory created when the main `egeria.git` repository is cloned is called `egeria`.  This directory contains all the source and the build scripts.

Change to the egeria directory:
```bash
cd egeria
```
The build scripts creates executable libraries needed to run Egeria using the source files from the git repository. They ensure the software is built consistently, in the correct order.

???+ education "Building with Gradle (V4.0 and beyond)"
    --8<-- "snippets/tasks/task-building-with-gradle.md"

??? education "Building with Maven (Before V4.0)"
    If building a version of Egeria prior to version 4, the maven instructions can be found below:

    --8<-- "snippets/tasks/task-building-with-maven.md"

Once the build is complete, the executable files you need can be found under `open-metadata-distribution`.  Change to this directory and list the files.

```bash
cd open-metadata-distribution
```
```bash
ls
```

The directories that you see will depend on the release of Egeria.  Look in the `README.md` for a description of the different distributions that have been built.

```bash
more README.md  
```


