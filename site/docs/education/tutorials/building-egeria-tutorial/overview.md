<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Downloading and Building Egeria Tutorial

Egeria is an open source project that is delivered both as source code as well as [Maven Central Repository](https://search.maven.org/) libraries.

This tutorial will guide you through the process of downloading the ODPi Egeria source code from [GitHub](https://github.com/) and building it so that you can run it on your local machine.  

Once you have [downloaded Egeria](#downloading-the-egeria-source-from-github), you can also use
[Kubernetes](/egeria-docs/education/tutorials/lab-infrastructure-guide/running-kubernetes/overview) to 
start the lab infrastructure for the [Hands-on Labs](../../open-metadata-labs).
This does not require you to build Egeria.

Already lost, or are the instructions below not detailed enough? Check out the [Egeria Dojo](../../egeria-dojo),
or consider jumping straight to the [Hands-on Labs](../../open-metadata-labs), which provide a pre-built environment
for you and guided instructions on how to use different APIs.
 
## Prerequisite Technology for Building Egeria

You will need a **Java Development Kit (JDK)** installed on your machine in order to build Egeria.
There are various JDKs available, and you may even have one pre-installed on your system. You can check
if java is already installed by running the command `java -version` from the command-line.

Java can be installed by:

1. Downloading the **OpenJDK 11 (LTS) HotSpot** JVM from [Adoptium](https://adoptopenjdk.net).
5. Running the installer that is downloaded.

Maven is the tool used to run the Egeria build.
You can check if Maven installed by running the command `mvn --version` from the command-line.
Ensure you are using version 3.5.0 or higher in order to build Egeria.

Maven can be installed:

- On MacOS, by first installing the [HomeBrew](https://brew.sh) package manager and then running
`brew install maven` from the command-line.
- On Linux operating systems, by using your distribution's package manager (`yum install maven`, `apt-get install maven`, etc).
- On Windows, you should use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) Version 2 or above, install an appropriate Linux distribution, and follow
  the instructions for Linux.
  
**Git** is an open source version control system used to store and manage Egeria's files.
You need it installed on your machine to work with Egeria's git repositories stored on
[GitHub](https://github.com/odpi/egeria).
You can check whether it is installed on your system by running `git --version` from the command-line.


## Tutorial tasks

1. [Downloading the Egeria source from GitHub](#downloading-the-egeria-source-from-github)
2. [Building the Egeria source with Apache Maven](#building-egeria-source.md)

## Downloading the Egeria Source from GitHub

The Egeria source is extracted from GitHub using the following `git` command:

```bash
$ git clone https://github.com/odpi/egeria.git
Cloning into 'egeria'...
remote: Enumerating objects: 38, done.
remote: Counting objects: 100% (38/38), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 50419 (delta 8), reused 29 (delta 7), pack-reused 50381
Receiving objects: 100% (50419/50419), 36.35 MiB | 5.23 MiB/s, done.
Resolving deltas: 100% (31704/31704), done.
Checking out files: 100% (6669/6669), done.
```

A new directory has been created with the ODPi Egeria source code.
Change to the `egeria` directory.

```bash
$ cd egeria
```

You are now ready to [build the egeria source](#building-and-downloading-egeria-source).

Alternatively you can [use Kubernetes](../lab-infrastructure-guide/running-kubernetes.md)
to set up the infrastructure to run the [Open Metadata Labs](../../open-metadata-labs).

If you are working on the Dojo return to [Day 1](../../egeria-dojo/egeria-dojo-day-1-3-2-4-second-server.md)

## Building the Egeria Source

When you [download the egeria source from GitHub](task-downloading-egeria-source.md)
a new directory called `egeria` is created that contains all of the source and the build scripts.

The build scripts use [Apache Maven](https://maven.apache.org) to ensure the software is
built in the correct order.  If you change into the `egeria` directory, you will see
a file called `pom.xml`.  This is the file that controls the build.

Issue the following command from the `egeria` directory.

```bash
$ mvn clean install
``` 

The build can take 15-30 minutes depending on the speed and load on your machine.  However eventually you will see the message:

```text
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 14:54 min
[INFO] Finished at: 2020-01-29T09:33:17Z
[INFO] Final Memory: 171M/3510M
[INFO] ------------------------------------------------------------------------

Process finished with exit code 0
```

This means you have completed this tutorial and are ready to [choose the next step](..).

## What next?

* [Run the hands on labs to get experience with using Egeria](../../open-metadata-labs)
or
* [Learn about installing Egeria in your own environment](../installing-egeria-tutorial)
or
* [Jump to the Egeria dojo to learn how to make a contribution to Egeria](/egeria-docs/education/egeria-dojo/egeria-dojo-day-2-3-contribution-to-egeria.md)

----
* Return to [Egeria Dojo](../../egeria-dojo)

----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
