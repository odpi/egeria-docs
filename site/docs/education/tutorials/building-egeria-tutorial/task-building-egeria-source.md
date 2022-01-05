<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Building the Egeria Source

The build process takes the source files from the git repository and creates executable libraries needed to run Egeria.  

#### Supported Platforms

Egeria currently supports building on *nix, Linux & Linux-like operating systems such as MacOS.
     
Our official build pipelines are based on x86_64 architecture, but it is expected the build will run on other architectures, subject to the availability of the required tools and interpreters/jvms/runtimes on that platform (for example Java, Python, Docker/containerd/k8s etc).
     
On Windows, you should use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) Version 2 or above, and install a Linux distribution such as Ubuntu. This avoids issues we have seen with path separators, symbolic links, slow I/O performance, long pathnames. 
     
Some IDEs such as JetBrains IntelliJ and Microsoft VisualCode will run the GUI in Windows natively, and then use a linux environment (via WSL2 - which uses a real Linux kernel) to perform build and execution

#### Running the build

When you download the egeria source from GitHub a new directory called `egeria` is created that contains all of the source and the build scripts.

The build scripts use [Apache Maven](https://maven.apache.org) to ensure the software is built in the correct order.  If you change into the `egeria` directory, you will see
a file called `pom.xml`.  This is the file that controls the build.

Issue the following command from the `egeria` directory.

```bash
$ mvn clean install
``` 

The build can take 15-60 minutes depending on the speed and load on your machine.  However eventually you will see the message:

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


--8<-- "snippets/abbr.md"
