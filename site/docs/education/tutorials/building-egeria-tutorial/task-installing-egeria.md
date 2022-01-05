<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Installing Egeria

The [egeria build process](/egeria-docs/education/tutorials/building-egeria-tutorial/overview) creates the
distribution files for Egeria in the **open-metadata-distribution** module.
The assemblies are located from the egeria build directory as follows:

```bash
$ cd open-metadata-distribution/open-metadata-assemblies/target
$ ls
ls
archive-tmp					egeria-3.3-SNAPSHOT-sources.tar.gz
egeria-3.3-SNAPSHOT-distribution		maven-archiver
egeria-3.3-SNAPSHOT-distribution.tar.gz		open-metadata-assemblies-3.3-SNAPSHOT.jar
egeria-3.3-SNAPSHOT-omag-server			rat.txt
egeria-3.3-SNAPSHOT-omag-server.tar.gz
```
The files in this list will change as Egeria develops. For this exercise it is the files including 'distribution' that are important.

The name of the files is determined by the release level of the code that you
[downloaded from GitHub](/egeria-docs/education/tutorials/git-and-git-hub-tutorial/overview/#downloading-the-egeria-source-from-github).  In this example,
the release is **egeria-3.3-SNAPSHOT**.

Create a directory for the install and copy the tar file into it.
The two commands shown below create an install directory at the same level in the
file system as the **egeria** build library and then copies the egeria distribution file into it.

```bash
$ mkdir ../../../../egeria-install
$ cp egeria*-distribution.tar.gz ../../../../egeria-install
```

These next commands change to the new directory and lists its contents.

```bash
$ cd ../../../../egeria-install
$ ls
egeria-3.3-SNAPSHOT-distribution.tar.gz
```

It is now possible to unpack the tar file.

```bash
$ tar -xf egeria-3.3-SNAPSHOT-distribution.tar.gz
$ ls
egeria-3.3-SNAPSHOT-distribution.tar.gz	egeria-omag-3.3-SNAPSHOT
```

A new directory is created called **egeria-omag-3.3-SNAPSHOT**.  Change to this
new directory and list its contents as shown below.

```bash
$ cd egeria-omag-3.3-SNAPSHOT
$ ls
LICENSE			clients			server
NOTICE			conformance-suite	user-interface
```

As before, you may notice different files as Egeria evolves.

Under **server** is a directory for the
[OMAG Server Platform](/egeria-docs/concepts/omag-server-platform) that is used to run
open metadata and governance services.

```bash
$ ls server
$ resources				server-chassis-spring-3.3-SNAPSHOT.jar
```

--8<-- "snippets/abbr.md"
