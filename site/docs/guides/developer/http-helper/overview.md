<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Using HTTP Helper to turn off certificate checking

The *HTTPHelper* is a Java class that is used to control HTTP settings.  Its most common use is in development environments to turn off certificate checking in a utility.

For example: if you see this error, then you need to use the HTTPHelper:

```
There was a org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException exception when calling the OMAG Server Platform.  Error message is: OMAG-COMMON-503-001 A client-side exception was received from API call registerListener to OMAG Server mds1 at https://localhost:7443.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.ResourceAccessException was received by method registerListener from API call https://localhost:7443/servers/{0}/open-metadata/access-services/asset-consumer/users/{1}/topics/out-topic-connection/{2} to server mds1 on platform https://localhost:7443.  The error message was I/O error on GET request for "https://localhost:7443/servers/mds1/open-metadata/access-services/asset-consumer/users/erinoverview/topics/out-topic-connection/egeria.dojo.assetlisten.AssetListen": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested exception is javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
```

The key part of the message is `PKIX path building failed ... unable to find valid certification path to requested target`.  It means the client does not trust the certificate presented by the OMAG Server Platform.  The example above was captured from an older release of Egeria; the services named in the URL will be different today, but the cause and the fix are the same.

!!! danger "Development use only"
    Turning off certificate checking means the client trusts any server, whatever certificate it presents.  In production, add the platform's certificate (or the certificate authority that signed it) to the trust store of the Java runtime running the utility instead.

The *HttpHelper* class (`org.odpi.openmetadata.http.HttpHelper`) is in the `http-helper` module.  Add it as a dependency of your utility.  Using Maven, add this to your `pom.xml` file:

```xml
<dependency>
    <groupId>org.odpi.egeria</groupId>
    <artifactId>http-helper</artifactId>
    <version>${open-metadata.version}</version>
</dependency>
```

Or using Gradle:

```groovy
implementation "org.odpi.egeria:http-helper:${egeriaVersion}"
```

Then add one of these lines to your main program before any Java client is created.  Egeria's default REST client connector checks the setting when it is constructed, so a client created before the call keeps checking certificates.

```java linenums="1"

HttpHelper.noStrictSSLIfConfigured();

```

`noStrictSSLIfConfigured()` only turns off certificate checking if the Java system property `strict.ssl` is set to `false`, so start your utility with this option on the `java` command (or in the VM options of your IntelliJ run configuration):

```bash
java -Dstrict.ssl=false -jar my-utility.jar
```

Alternatively, `HttpHelper.noStrictSSL()` turns off certificate checking unconditionally, and `HttpHelper.isStrictSSL()` reports whether checking is still in force.  The OMAG Server Platform uses the same class: it calls `noStrictSSL()` when its `strict.ssl` property (set in `application.properties`) is `false`.

--8<-- "snippets/abbr.md"
