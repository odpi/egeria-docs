<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Documentation Tools

## draw.io

We use the free [draw.io :material-dock-window:](https://app.diagrams.net){ target=draw } tool to produce all the diagrams for our website and presentations. Following the process outlined below, the draw.io files are stored as XML, which means it is easy to manage them in git.

The tool can be run from the browser, or as a desktop tool. We recommend the desktop tool if you are doing editing of the diagrams because it supports auto-save.

!!! tip "Opening multiple diagrams"
    Whenever you start draw.io, it offers the choice to either open a new diagram or an existing file. On the desktop, **New...** means new window, and you can use it to have multiple files open at once.

### New diagrams

!!! attention "Export new diagrams as an SVG, including a copy of the diagram"
    The following instructions must be followed to maximize diagram maintainability.

To save a new diagram, choose **File** -> **Export as** -> **SVG...**

Ensure the **Include a copy of my diagram** box is ticked, and tick the **Transparent Background** box as well:

![Export properties](draw.io-export-properties.png)

This will ensure that:

- the output renders nicely at all sizes in any modern web browser (no image artifacts, especially on text)
- the diagram is entirely self-contained, and can continue to be edited and evolved in draw.io
- each diagram is version-controlled in git as its own independent XML file
- subsequent changes to the diagram can just directly edit this SVG file (no further **Export as** needed)

### Existing diagrams

As indicated above, to edit existing SVG diagrams, you should be able to simply:

- open them directly in draw.io
- make any changes directly to the diagram
- save the file (no **Export as** needed)

## Swagger

Swagger automatically generates a website that documents the REST APIs supported by the [OMAG Server Platform](/concepts/omag-server-platform). It is based on the [Open API Specification (V3) :material-dock-window:](http://spec.openapis.org/oas/v3.0.3){ target=api }.

The website is found at `<serverURLroot>/swagger-ui.html`, where `<serverURLroot>` is the location of the OMAG Server Platform (for example, `https://localhost:9443/swagger-ui.html`).

The top of the page gives a general description of the OMAG Server Platform plus a link to more documentation.

![Swagger heading](../../education/tutorials/swagger-tutorial/swagger-ui-top.png)

The content for this header is located in the [OMAGServerPlatform.java :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/server-chassis/server-chassis-spring/src/main/java/org/odpi/openmetadata/serverchassis/springboot/OMAGServerPlatform.java){ target=gh } file that provides the `main()` method for the OMAG Server Platform.

!!! example "Swagger annotations in [`OMAGServerPlatform.java` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/server-chassis/server-chassis-spring/src/main/java/org/odpi/openmetadata/serverchassis/springboot/OMAGServerPlatform.java){ target=gh }"
    ```java linenums="1"
    @OpenAPIDefinition(
            info = @Info(
                    title = "Egeria's Open Metadata and Governance (OMAG) Server Platform",
                    version = "3.1-SNAPSHOT",
                    description = "The OMAG Server Platform provides a runtime process and platform for Open Metadata and Governance (OMAG) Services.\n" +
                            "\n" +
                            "The OMAG services are configured and activated in OMAG Servers using the Administration Services.\n" +
                            "The configuration operations of the admin services create configuration documents, one for each OMAG Server.  " +
                            "Inside a configuration document is the definition of which OMAG services to activate in the server. " +
                            "These include the repository services (any type of server), the access services (for metadata access points " +
                            "and metadata servers), governance services (for governance servers) and view services (for view servers).  " +
                            "Once a configuration document is defined, the OMAG Server can be started and stopped multiple times by " +
                            "the admin services server instance operations.  \n" +
                            "\n" +
                            "The OMAG Server Platform also supports platform services to query details of the servers running on the platform.\n" +
                            "\n" +
                            "The OMAG Server Platform can host multiple OMAG servers at any one time. " +
                            "Each OMAG server is isolated within the server platform and so the OMAG server platform can be used to support multi-tenant " +
                            "operation for a cloud service, " +
                            "or host a variety of different OMAG Servers needed at a particular location.\n" +
                            "\n" +
                            "Click on the documentation link to find out more ...",
                    license = @License(name = "Apache 2.0", url = "https://www.apache.org/licenses/LICENSE-2.0"),
                    contact = @Contact(url = "https://egeria.odpi.org", name = "Egeria Project", email = "egeria-technical-discuss@lists.lfaidata.foundation")
            ),
    
            externalDocs = @ExternalDocumentation(description = "OMAG Server Platform documentation",
                    url="https://egeria.odpi.org/open-metadata-implementation/admin-services/docs/user")
            )    
    ```

Beneath the header is a list of the platform's REST APIs.  This is the definition for the
*operational services* that are part of the *administration services*:

![Swagger service](../../education/tutorials/swagger-tutorial/swagger-ui-service.png)

The REST API operations are grouped into services by the following `@Tag` annotation that appears in each [Spring](/guides/contributor/runtime/#spring) resource bean that is part of the service. If the name of the `@Tag` matches then the operations in the resource beans are all part of the same service.

!!! example "Swagger annotations in [OperationalServicesResource.java :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/admin-services/admin-services-spring/src/main/java/org/odpi/openmetadata/adminservices/spring/OperationalServicesResource.java){ target=gh }"
    ```java linenums="1"
    @Tag(name="Administration Services - Operational",
         description="The operational administration services support the management " +
                     "of OMAG Server instances.  This includes starting and stopping the servers as well as querying and changing their operational state.",
         externalDocs=@ExternalDocumentation(description="Further information",
                                             url="https://odpi.github.io/guides/operations/guide.html"))
    ```

Further information can be provided for each operation. This is one of the *operational services* operations:

![Swagger operation](../../education/tutorials/swagger-tutorial/swagger-ui-operation.png)

This is added to the spring resource bean using the `@Operation` annotation:

!!! example "Swagger annotations"
    ```java linenums="1"
    @Operation(summary="Activate server with stored configuration document",
               description="Activate the named OMAG server using the appropriate configuration document found in the configuration store.",
               externalDocs=@ExternalDocumentation(description="Configuration Documents",
               url="https://egeria.odpi.org/open-metadata-implementation/admin-services/docs/concepts/configuration-document.html"))
    ```

--8<-- "snippets/abbr.md"
