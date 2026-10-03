<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Testing Tools

## HTTP Client Collections

IntelliJ supports a simple format for describing calls to REST APIs.  These are called [HTTP Client Collections](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html).
The beauty of them is that in addition to being executable in an IntelliJ environment, they are very readable and so the Egeria community uses them to document the OMAG Server Platform REST API.  These files have a http file extension.

## Command-line request tools

In addition to IntelliJ there are command line tools for calling REST APIs.

### `curl`

The command that is most commonly available is `curl`.

!!! cli "Example `curl` command"
    ```shell
    curl --insecure -X GET https://localhost:7443/open-metadata/platform-services/users/test/server-platform/origin
    ```

!!! attention "Disable SSL certificate verification"
    Note that Egeria is using `https://`, so if you have not replaced the provided self-signed certificate, ensure you include `--insecure` on any requests to skip certificate validation.

### `HTTPie`

As an alternative to `curl` you might like to try [HTTPie :material-dock-window:](https://httpie.org/){ target=httpie }, which has more advanced functions.

!!! attention "Disable SSL certificate verification"
    Note that Egeria is using `https://`, so if you have not replaced the provided self-signed certificate, ensure you include `--verify no` to any requests to skip certificate validation.

## Functional verification test (FVT) suites

Functional verification tests exercise several components together, running them the way they are deployed rather than calling them directly.  The suites are in the [open-metadata-fvt](https://github.com/odpi/egeria/tree/main/open-metadata-test/open-metadata-fvt) module of the egeria repository, whose README describes each one in detail.

Every suite is **opt-in** - none of them run as part of an ordinary build.  Most need a PostgreSQL server, an Apache Kafka broker, or both.  Each is started by naming its property on the command line, for example:

!!! cli "Running the files-fvt suite"
    ```shell
    ./gradlew :open-metadata-test:open-metadata-fvt:files-fvt:test -PrunFilesFvt
    ```

| Suite                  | Property                                         | What it covers                                                                                                      |
|------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `auth-fvt`             | `-PrunAuthFvt`                                   | The platform's own authentication: logging on, bearer tokens, changing a password and managing user accounts.       |
| `bitol-fvt`            | `-PrunBitolFvt`, `-PrunBitolFvtInMemory`         | The Bitol data contract (ODCS) and data product (ODPS) support.                                                     |
| `client-fvt`           | `-PrunClientFvt`                                 | The connector context clients that the platform hands to a connector.                                               |
| `cts-fvt`              | `-PrunCtsFvtPostgres`, `-PrunCtsFvtInMemory`     | Runs the [Conformance Test Suite](/guides/cts) against Egeria's own repositories.                                   |
| `darwin-fvt`           | `-PrunDarwinFvt`                                 | The Darwin Product Dependency Manager.                                                                              |
| `duplicate-fvt`        | `-PrunDuplicateFvt`                              | [Duplicate management](/features/duplicate-management/overview), including the Mendel Automated Duplicate Manager.  |
| `files-fvt`            | `-PrunFilesFvt`, `-PrunFilesFvtNoKafka`          | The file connectors and the Files content pack.                                                                     |
| `openlineage-fvt`      | `-PrunOpenLineageFvt`                            | The OpenLineage integration connectors.                                                                             |
| `platform-catalog-fvt` | `-PrunPlatformCatalogFvt`                        | The OMAG Server Platform Cataloguer.                                                                                |
| `postgres-fvt`         | `-PrunPostgresFvt`, `-PrunPostgresFvtNoKafka`    | The PostgreSQL connectors and the PostgreSQL content pack.                                                          |
| `query-fvt`            | `-PrunQueryFvt`, `-PrunQueryFvtInMemory`         | The repository query surface: paging, sorting, filtering, historical queries and special characters.                |
| `security-fvt`         | `-PrunSecurityFvt`                               | The [metadata security](/features/metadata-security/overview) checks.                                               |
| `server-fvt`           | `-PrunServerFvt`                                 | The administration, platform and server operation services behind the Runtime Manager API.                          |
| `subscription-fvt`     | `-PrunSubscriptionFvt`                           | The Open Metadata Digital Product Catalog, from locating a product to receiving its data.                           |
| `tabular-data-fvt`     | `-PrunTabularDataFvt`                            | The tabular data set connectors.                                                                                    |
| `templates-fvt`        | `-PrunTemplatesFvt`                              | Every template shipped in the content packs.                                                                        |
| `type-fvt`             | `-PrunTypeFvt`                                   | The open metadata type system - that every type in the model is usable.                                             |

--8<-- "snippets/abbr.md"
