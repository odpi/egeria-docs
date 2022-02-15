<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### Using HTTP Helper to turn off certificate checking 

The *HTTPHelper* is a Java class that is used to control HTTP settings.  Its most common use is in development environments to turn off certificate checking in a utility.

For example: if you see this error, then you need to use the HTTPHelper:

```
There was a org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException exception when calling the OMAG Server Platform.  Error message is: OMAG-COMMON-503-001 A client-side exception was received from API call registerListener to OMAG Server mds1 at https://localhost:9443.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.ResourceAccessException was received by method registerListener from API call https://localhost:9443/servers/{0}/open-metadata/access-services/asset-consumer/users/{1}/topics/out-topic-connection/{2} to server mds1 on platform https://localhost:9443.  The error message was I/O error on GET request for "https://localhost:9443/servers/mds1/open-metadata/access-services/asset-consumer/users/erinoverview/topics/out-topic-connection/egeria.dojo.assetlisten.AssetListen": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested exception is javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
```

Add the HTTPHelper module as a dependency in your `pom.xml` file.

```xml
<dependency>
    <groupId>org.odpi.egeria</groupId>
    <artifactId>http-helper</artifactId>
    <version>${open-metadata.version}</version>
</dependency>
```

Then add this line to your main program before any call is made to a Java client.

```java linenums="1"

HttpHelper.noStrictSSLIfConfigured();

```

--8<-- "snippets/abbr.md"