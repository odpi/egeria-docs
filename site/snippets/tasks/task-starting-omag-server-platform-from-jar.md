<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### Starting the OMAG Server Platform

The OMAG Server Platform's `assembly/platform` directory contains a Java Archive (Jar) file for the [OMAG Server Platform](/concepts/omag-server-platform) itself along with a directory of libraries.

The name of the Java Archive (Jar) file will depend on the release of Egeria that you have installed.  In this example, the release is **5.2**.

```bash
$ cd platform
$ ls
ls
LICENSE                         application.properties          extra                           lib                             omag-server-platform-5.2.jar
NOTICE                          content-packs                   keystore.p12                    loading-bay                     truststore.p12
README.md                       data                            landing-area                    logs

```

The OMAG Server Platform is started with the `java` command.

??? tip "Checking your Java installation"
    Ensure you have a Java runtime at Version 17 or above installed on your machine. Check the version of Java you have with the command **java -version** and [install the appropriate version](/education/tutorials/building-egeria-tutorial/task-installing-java) if needed. You only need the JRE but select the JDK if you expect to also write some Java code.

??? danger "MacOS users - XTDB hang, or platform exit due to mismatch crypto library"
    On the latest level of the MacOs operating system we have experienced hangs during server startup, or the OMAG Server Platform exiting with a message complaining about the unsafe load of a cryptographic library.  A question has been raised with the XTDB community to find out more about this library. In the meantime, there is a workaround if you see this issue: set the following environment variables before starting your OMAG Server Platform.  This switches XTDB to using its own cryptography libraries.

    ```properties
    export XTDB_DISABLE_LIBCRYPTO=True
    export XTDB_ENABLE_BYTEUTILS_SHA1=True
    ```

Start the OMAG server platform with the following command:

```bash
java -Dloader.path=lib,extra -jar omag-server-platform*.jar
```

This starts the platform listening on port `9443`.  Add the `-Dserver.port` parameter before the `-jar` parameter if you wish the platform to listen on a different port. For example, the following command starts the platform listening on port `9444`.  Multiple instances of the same OMAG Server Platform may run in a single machine (or in the same container).  However, they each need to listen on a different port.

```bash
java -Dloader.path=lib,extra -Dserver.port=9444 -jar omag-server-platform*.jar
```

When the OMAG Server Platform starts up, it displays the `OMAG Server Platform` banner and then details of its configuration.

```text
 Project Egeria - Open Metadata and Governance
    ____   __  ___ ___    ______   _____                                 ____   _         _     ___
   / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
  / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
 / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
 \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/

 :: Powered by Spring Boot (v3.1.4) ::

18:22:43.638 [main] INFO  o.o.o.p.s.OMAGServerPlatform - Starting OMAGServerPlatform using Java 17.0.9 with PID 68372 (/egeria-release-5.2/egeria/open-metadata-distribution/omag-server-platform/build/unpacked/egeria-platform-5.2-distribution.tar.gz/assembly/platform/omag-server-platform-5.2.jar started by egeriauser in /egeria-release-5.2/egeria/open-metadata-distribution/omag-server-platform/build/unpacked/egeria-platform-5.2-distribution.tar.gz/assembly/platform)
18:22:43.639 [main] INFO  o.o.o.p.s.OMAGServerPlatform - No active profile set, falling back to 1 default profile: "default"
18:22:45.987 [main] INFO  o.s.b.w.e.tomcat.TomcatWebServer - Tomcat initialized with port(s): 9443 (https)
18:22:47.639 [main] INFO  o.o.o.p.s.OMAGServerPlatform - Working directory is: /egeria-release-5.2/egeria/open-metadata-distribution/omag-server-platform/build/unpacked/egeria-platform-5.2-distribution.tar.gz/assembly/platform
18:22:47.639 [main] WARN  o.o.o.p.s.OMAGServerPlatform - Option strict.ssl is set to false! Invalid certificates will be accepted for connection!
18:22:47.641 [main] WARN  o.o.o.p.s.OMAGServerPlatform - Java trust store 'javax.net.ssl.trustStore' is null - this is needed by Tomcat - using 'server.ssl.trust-store'
18:22:49.135 [main] INFO  o.s.b.w.e.tomcat.TomcatWebServer - Tomcat started on port(s): 9443 (https) with context path ''
18:22:49.144 [main] INFO  o.o.o.p.s.OMAGServerPlatform - Started OMAGServerPlatform in 5.901 seconds (process running for 6.311)
```

When you see the `Started OMAGServerPlatform in xxxx seconds (process running for yyyy)` message, it means the OMAG Server Platform has completed its start-up, and it is ready to use.  Typically the `application.properties` file lists a set of default servers to start up automatically.  These servers will start up at this point.

If you get an error that the port is in use, check for any applications using the same port and make sure they are each using unique ports.

Try the following command (replace 9443 accordingly if using a non-standard port):

```bash
curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/test/server-platform/origin
```
Returns
```text
Egeria OMAG Server Platform (version 5.2)
```

This calls the OMAG server platform using a REST API call.  The response `Egeria OMAG Server Platform (release X.x)` means the curl command communicated with a running OMAG Server Platform instance.

