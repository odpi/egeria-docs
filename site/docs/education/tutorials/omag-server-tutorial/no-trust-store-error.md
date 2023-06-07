<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


You will see this type of error if the trust store is not in the platform's home directory (or its location is not explicitly specified on the command line).
```bash
org.springframework.context.ApplicationContextException: Failed to start bean 'webServerStartStop'; nested exception is org.springframework.boot.web.server.WebServerException: Unable to start embedded Tomcat server
        at org.springframework.context.support.DefaultLifecycleProcessor.doStart(DefaultLifecycleProcessor.java:181) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.context.support.DefaultLifecycleProcessor.access$200(DefaultLifecycleProcessor.java:54) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.context.support.DefaultLifecycleProcessor$LifecycleGroup.start(DefaultLifecycleProcessor.java:356) ~[spring-context-5.3.15.jar!/:5.3.15]
        at java.base/java.lang.Iterable.forEach(Iterable.java:75) ~[na:na]
        at org.springframework.context.support.DefaultLifecycleProcessor.startBeans(DefaultLifecycleProcessor.java:155) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.context.support.DefaultLifecycleProcessor.onRefresh(DefaultLifecycleProcessor.java:123) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.context.support.AbstractApplicationContext.finishRefresh(AbstractApplicationContext.java:935) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:586) ~[spring-context-5.3.15.jar!/:5.3.15]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:145) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:732) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:414) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:302) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1303) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1292) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.odpi.openmetadata.serverchassis.springboot.OMAGServerPlatform.main(OMAGServerPlatform.java:95) ~[classes!/:na]
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[na:na]
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[na:na]
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[na:na]
        at java.base/java.lang.reflect.Method.invoke(Method.java:566) ~[na:na]
        at org.springframework.boot.loader.MainMethodRunner.run(MainMethodRunner.java:49) ~[server-chassis-spring-3.12-SNAPSHOT.jar:na]
        at org.springframework.boot.loader.Launcher.launch(Launcher.java:108) ~[server-chassis-spring-3.12-SNAPSHOT.jar:na]
        at org.springframework.boot.loader.Launcher.launch(Launcher.java:58) ~[server-chassis-spring-3.12-SNAPSHOT.jar:na]
        at org.springframework.boot.loader.PropertiesLauncher.main(PropertiesLauncher.java:467) ~[server-chassis-spring-3.12-SNAPSHOT.jar:na]
Caused by: org.springframework.boot.web.server.WebServerException: Unable to start embedded Tomcat server
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.start(TomcatWebServer.java:229) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.web.servlet.context.WebServerStartStopLifecycle.start(WebServerStartStopLifecycle.java:43) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.context.support.DefaultLifecycleProcessor.doStart(DefaultLifecycleProcessor.java:178) ~[spring-context-5.3.15.jar!/:5.3.15]
        ... 22 common frames omitted
Caused by: java.lang.IllegalArgumentException: standardService.connector.startFailed
        at org.apache.catalina.core.StandardService.addConnector(StandardService.java:238) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.addPreviouslyRemovedConnectors(TomcatWebServer.java:282) ~[spring-boot-2.6.3.jar!/:2.6.3]
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.start(TomcatWebServer.java:213) ~[spring-boot-2.6.3.jar!/:2.6.3]
        ... 24 common frames omitted
Caused by: org.apache.catalina.LifecycleException: Protocol handler start failed
        at org.apache.catalina.connector.Connector.startInternal(Connector.java:1075) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.catalina.core.StandardService.addConnector(StandardService.java:234) ~[tomcat-embed-core-9.0.58.jar!/:na]
        ... 26 common frames omitted
Caused by: java.lang.IllegalArgumentException: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-dev-projects/egeria-dev-projects/truststore.p12 (No such file or directory)
        at org.apache.tomcat.util.net.AbstractJsseEndpoint.createSSLContext(AbstractJsseEndpoint.java:99) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.AbstractJsseEndpoint.initialiseSsl(AbstractJsseEndpoint.java:71) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.NioEndpoint.bind(NioEndpoint.java:233) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.AbstractEndpoint.bindWithCleanup(AbstractEndpoint.java:1213) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.AbstractEndpoint.start(AbstractEndpoint.java:1299) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.coyote.AbstractProtocol.start(AbstractProtocol.java:614) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.catalina.connector.Connector.startInternal(Connector.java:1072) ~[tomcat-embed-core-9.0.58.jar!/:na]
        ... 28 common frames omitted
Caused by: java.io.FileNotFoundException: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-dev-projects/egeria-dev-projects/truststore.p12 (No such file or directory)
        at java.base/java.io.FileInputStream.open0(Native Method) ~[na:na]
        at java.base/java.io.FileInputStream.open(FileInputStream.java:219) ~[na:na]
        at java.base/java.io.FileInputStream.<init>(FileInputStream.java:157) ~[na:na]
        at java.base/java.io.FileInputStream.<init>(FileInputStream.java:112) ~[na:na]
        at java.base/sun.net.www.protocol.file.FileURLConnection.connect(FileURLConnection.java:86) ~[na:na]
        at java.base/sun.net.www.protocol.file.FileURLConnection.getInputStream(FileURLConnection.java:184) ~[na:na]
        at org.apache.catalina.startup.CatalinaBaseConfigurationSource.getResource(CatalinaBaseConfigurationSource.java:118) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.SSLUtilBase.getStore(SSLUtilBase.java:197) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.SSLHostConfig.getTruststore(SSLHostConfig.java:730) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.SSLUtilBase.getTrustManagers(SSLUtilBase.java:422) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.SSLUtilBase.createSSLContext(SSLUtilBase.java:245) ~[tomcat-embed-core-9.0.58.jar!/:na]
        at org.apache.tomcat.util.net.AbstractJsseEndpoint.createSSLContext(AbstractJsseEndpoint.java:97) ~[tomcat-embed-core-9.0.58.jar!/:na]
        ... 34 common frames omitted




```

