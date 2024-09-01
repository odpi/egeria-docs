<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### Starting the OMAG Server Platform

The OMAG Server Platform's `assembly/platform` directory contains a Java Archive (Jar) file for the [OMAG Server Platform](/concepts/omag-server-platform) itself along with a directory of libraries.

The name of the Java Archive (Jar) file will depend on the release of Egeria that you have installed.  In this example, the release is **5.0**.

```bash
$ ls platform
lib              omag-server-platform-5.0.jar
```

The OMAG Server Platform is started with the `java` command.

??? tip "Checking your Java installation"
    Ensure you have a Java runtime at Version 17 or above installed on your machine. Check the version of Java you have with the command **java -version** and [install the appropriate version](/education/tutorials/building-egeria-tutorial/task-installing-java) if needed. You only need the JRE but select the JDK if you expect to also write some Java code.

??? danger "MacOS users - XTDB hang, or platform exit due to mismatch crypto library"
    On the latest level of the MacOs operating system we have experienced hangs during server startup, or the OMAG Server Platform exiting with a message complaining about the unsafe load of a cryptographic library.  A question has been raised with the XTDB community to find out more about this library. In the meantime, there is a workaround if you see this issue: set the following environment variables before starting your OMAG Server Platform.  This switches XTDB to using its own cryptography libraries.

   ```properties
   XTDB_DISABLE_LIBCRYPTO=True;XTDB_ENABLE_BYTEUTILS_SHA1=True
   ```

Start the OMAG server platform with the following command:

```bash
java -Dloader.path=platform/lib,platform/extras -jar platform/omag-server-platform*.jar
```

This starts the platform listening on port `9443`.  Add the `-Dserver.port` parameter before the `-jar` parameter if you wish the platform to listen on a different port. For example, the following command starts the platform listening on port `9444`.  Multiple instances of the same OMAG Server Platform may run in a single machine (or in the same container).  However, they each need to listen on a different port.

```bash
java -Dloader.path=platform/lib -Dserver.port=9444 -jar platform/omag-server-platform*.jar
```

When the OMAG Server Platform starts up, it displays the `OMAG Server Platform` banner and then details of its configuration.

```text
 Project Egeria - Open Metadata and Governance
    ____   __  ___ ___    ______   _____                                 ____   _         _     ___
   / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
  / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
 / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
 \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/

 :: Powered by Spring Boot (v3.0.6) ::

2023-06-11T13:13:57.959+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 17.0.6 with PID 85411 (/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz/platform/omag-server-platform-4.3-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz)
2023-06-11T13:13:57.962+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to 1 default profile: "default"
2023-06-11T13:14:01.186+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
2023-06-11T13:14:02.400+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Working directory is: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz
2023-06-11T13:14:02.400+01:00  WARN 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Java trust store 'javax.net.ssl.trustStore' is null - this is needed by Tomcat - using 'server.ssl.trust-store'
2023-06-11T13:14:04.687+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9443 (https) with context path ''
2023-06-11T13:14:04.704+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Started OMAGServerPlatform in 7.591 seconds (process running for 8.325)
Sun Jun 11 13:14:04 BST 2023 No OMAG servers listed in startup configuration
Sun Jun 11 13:14:04 BST 2023 OMAG server platform ready for more configuration
```

When you see the `OMAG server platform ready for more configuration` message, it means the OMAG Server Platform has completed its start-up, and it is ready to use.

If you get an error that the port is in use, check for any applications using the same port and make sure they are each using unique ports.

Try the following command (replace 9443 accordingly if using a non-standard port):

```bash
curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/test/server-platform/origin
```
Returns
```text
Egeria OMAG Server Platform (version 4.3)
```

This calls the OMAG server platform using a REST API call.  The response `Egeria OMAG Server Platform (release X.x)` means the curl command communicated with a running OMAG Server Platform instance.
