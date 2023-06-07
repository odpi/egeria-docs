<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Platform origin profile

The platform origin profile requires that an [Open Metadata and
Governance (OMAG) Server Platform](/concepts/omag-server-platform) is able to report its origin.

## Origin identifier

The open metadata standards defines a `getServerOrigin`
operation (`../open-metadata/admin-services/users/{{adminUserId}}/server-platform-origin`).
This operation returns an origin descriptor.
Typically, this identifies the vendor, product name and version of the server.
It is useful to administrators to be able to validate the platform that is running.

This is the test case that validates whether the operation is present.

### Platform origin test case

Validate the retrieval of the origin descriptor from the server platform that hosts one or more open metadata
repositories and/or servers.

This test uses the getServerPlatformOrigin operation (`../open-metadata/platform-services/users/{{adminUserId}}/server-platform-origin`)
operation to test that the platform knows its origin descriptor.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `platform-origin-01` | The origin descriptor has successfully been retrieved from the server platform. If this assertion fails, check that the server platform is started and the open metadata services are activated. |

???+ discovered "Discovered properties"
    | ID | Description |
    |---|---|
    | `Platform origin id` | Descriptive name for the server platform implementation. |

??? success "Example output for platform origin test case"
    ```json
    {
      "class" : "OpenMetadataTestCaseResult",
      "testCaseId" : "platform-origin",
      "testCaseName" : "Platform origin test case",
      "testCaseDescriptionURL" : "https://egeria.odpi.org/open-metadata-conformance-suite/docs/platform-workbench/platfrom-origin-test-case.md",
      "assertionMessage" : "Platform origin descriptor successfully retrieved",
      "successfulAssertions" : [ "Origin descriptor retrieved from platform." ],
      "unsuccessfulAssertions" : [ ],
      "discoveredProperties" : {
        "Repository origin id" : "Egeria OMAG Server Platform (version 3.1-SNAPSHOT)"
      }
    }
    ```

--8<-- "snippets/abbr.md"
