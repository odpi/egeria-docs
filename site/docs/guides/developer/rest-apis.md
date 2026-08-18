<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Calling Egeria's REST APIs

Egeria's REST APIs are also called Open Metadata View Services (OMVS) because they run in the [View Server](/concepts/view-server).  Their 

Egeria also uses REST APIs to issue synchronous calls between its servers and platforms.  These APIs are called via the [Java clients](/guides/developer/java-clients) and are considered internal to Egeria and there are no guarantees that they are backward compatible unless the individual module declares the REST API to be *supported*.

All the REST APIs are published through Swagger at this URL:

```

{{platformURLRoot}}/swagger-ui/index.html

```
The default rendering is poor and the Egeria community is looking for help to improve it.

It is also possible to get the raw Open API Specification from this URL:

```

{{platformURLRoot}}/v3/api-docs

```

Most modules also provide IntelliJ HTTP Client collections.  These can execute in an IntelliJ environment.  They are also easy to read and so are probably the best documentation of our REST API.


--8<-- "snippets/abbr.md"
