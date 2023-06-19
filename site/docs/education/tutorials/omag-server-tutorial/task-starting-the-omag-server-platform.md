<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Starting the OMAG Server Platform

The [OMAG Server Platform's installation directory](/education/tutorials/building-egeria-tutorial/task-installing-egeria) contains a Java Archive (Jar) file for the [OMAG Server Platform](/concepts/omag-server-platform) itself along with a directory of libraries.

The name of the Java Archive (Jar) file will depend on the release of Egeria that you have installed.  In this example, the release is **4.2**.

```bash
$ ls platform
lib              omag-server-platform-4.2.jar
```

The OMAG Server Platform is started with the `java` command.  

??? tip "Checking your Java installation"
    Ensure you have a Java runtime at Version 17 or above installed on your machine. Check the version of Java you have with the command **java -version** and [install the appropriate version](/education/tutorials/building-egeria-tutorial/task-installing-java) if needed. You only need the JRE but select the JDK if you expect to also write some Java code.)

Start the OMAG server platform with the following command:

```bash
java -Dloader.path=platform/lib -jar platform/omag-server-platform*.jar
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

2023-06-11T13:13:57.959+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 17.0.6 with PID 85411 (/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz/platform/omag-server-platform-4.2-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz)
2023-06-11T13:13:57.962+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to 1 default profile: "default"
2023-06-11T13:14:01.186+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
2023-06-11T13:14:02.400+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Working directory is: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz
2023-06-11T13:14:02.400+01:00  WARN 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Java trust store 'javax.net.ssl.trustStore' is null - this is needed by Tomcat - using 'server.ssl.trust-store'
2023-06-11T13:14:04.687+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9443 (https) with context path ''
2023-06-11T13:14:04.704+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Started OMAGServerPlatform in 7.591 seconds (process running for 8.325)
Sun Jun 11 13:14:04 BST 2023 No OMAG servers listed in startup configuration
Sun Jun 11 13:14:04 BST 2023 OMAG server platform ready for more configuration
```

When you see the `OMAG server platform ready for more configuration` message, it means the OMAG Server Platform has completed its start up and it ready to use.

If you get an error that the port is in use, check for any applications using the same port and make sure they are each using unique ports.

Try the following command (replace 9443 accordingly if using a non standard port):

```bash
curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/test/server-platform/origin
```
```text
Egeria OMAG Server Platform (version 4.2)
```

This calls the OMAG server platform using a REST API call.  The response `Egeria OMAG Server Platform (release X.x)` means the curl command communicated with a running OMAG Server Platform instance.

The OMAG Server Platform has many REST APIs.  Enter **https://localhost:9443/swagger-ui/index.html** into your browser to see the list of available REST APIs.

Broadly speaking, the OMAG Server Platform supports:

* Services to operate the platform.
* Open metadata and governance services to manage the open metadata ecosystem.

The services operating the platform (primarily the [Administration Services](/services/admin-services/overview) and [Platform Services](/services/platform-services/overview)) are available all the time the OMAG Server Platform is running.  The open metadata and governance services include a server name in the URL and they are routed to the named OMAG Server running on the OMAG Server Platform.

OMAG Servers are started on the OMAG Server Platform through the Platform Services using a [configuration document](/concepts/configuration-document).  This configuration document is configured in the OMAG Server Platform using the Administration Services.

Understanding how to create a configuration document using the administration services [is the next task in this tutorial](/education/tutorials/omag-server-tutorial/task-creating-configuration-documents).

--8<-- "snippets/abbr.md"