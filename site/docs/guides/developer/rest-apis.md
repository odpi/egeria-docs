<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Calling Egeria's REST APIs

Egeria uses REST APIs to issue synchronous calls between its servers and platforms.  These APIs are called via the [Java clients](/egeria-docs/guides/developer/java-clients) and are considered internal to Egeria and there are no guarantees that they are backward compatible unless the individual module declares the REST API to be *supported*.

Having said that, each REST API includes parameter validation and technically can be called by third party applications that do not support Java.  You can see examples of this in the [open metadata labs](/egeria-docs/education/open-metadata-labs) where the REST APIs are called from the python notebooks.

Developers and architects experimenting with Egeria also find it useful to call Egeria through the REST APIs using tools such as [postman](/egeria-docs/tools/testing/#postman).  As such the REST APIs are published through Swagger at this URL:

```

{{platformURLRoot}}/swagger-ui.html

```
The default rendering is poor and the Egeria community is looking for help to improve it.

It is also possible to get the raw Open API Specification from this URL:

```

{{platformURLRoot}}/v3/api-docs

```

Some modules also provide postman collections.


--8<-- "snippets/abbr.md"
