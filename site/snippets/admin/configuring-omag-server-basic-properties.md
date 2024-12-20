<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the basic server properties

The basic server properties are used in logging and events originating from the server. They help to document the purpose of the server (which helps with problem determination) and enable performance improvements by allowing the server to ignore activity or metadata that is not relevant to its operation.

| Property                 | Description                                                                                                                                                                                                                                                                                                    |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *localServerDescription* | Description for the server. This is useful information for the administrator to understand the role of the server. The default value is `null`.                                                                                                                                                                |
| *organizationName*       | Descriptive name for the organization that owns the local server/repository. This is useful when the open metadata repository cluster consists of metadata servers from different organizations, or different departments of an enterprise. The default value is `null`.                                       |
| *localServerUserId*      | UserId to use for server-initiated REST calls. The default is `OMAGServer`.                                                                                                                                                                                                                                    |
| *localServerPassword*    | Password to use for server-initiated REST calls. The default is `null`. This means that only the userId is sent in the HTTP header.                                                                                                                                                                            |
| *localServerURL*         | The URL of the platform where the server is to be deployed.  It should be the value used by external services to call the server since its broadcast across an [open metadata repository cohort](/concepts/cohort-member) and used when deploying the server's configuration document to the correct platform. |
| *maxPageSize*            | The maximum page size that can be set on requests to the server. The default value is `1000`. A value of zero means unlimited page size. Although supported, the zero value is not recommended because it provides no protection from a large request denial of service attack.                                |

Typically, these values are set up in a single command.

--8<-- "snippets/admin/calls/set-basic-server-properties.md"

Alternatively, you can set these properties one at a time.

??? post "setServerDescription"
    The server description should be set to something that describes the OMAG Server's role. It may be the name of a specific product that it is enabling, or a role in the metadata and governance landscape.  Its purpose is to help administrators identify which server configuration they need to work with.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-description
    ```
    The description is passed in the request body as a text string.

??? post "setOrganizationName"
    The organization name may be the owning organization or you may use it to identify the department or team that is supported by this server.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/organization-name?name="{{organizationName}}"
    ```
??? post "setServerUserId"
    The server's userId is used when processing requests that do not have an end user, such as receiving an event from a topic. The default value is `OMAGServer`. Ideally each server should have its own userId, so it is possible to restrict the resources that each server has access to and identify the origin of updates to the metadata elements.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-user-id?id="{{serverUserId}}"
    ```

??? post "setServerPassword"
    If the password is specified, the userId and password combination are used to provide authentication information on each REST call made by the server.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-user-password?password="{{serverUserPassword}}"
    ```

??? post "setServerURLRoot"
    Configure the `targetPlatformURLRoot` with the [platform URL Root](/concepts/omag-server/#platform-url-root) value of where the OMAG Server Platform will run.
    This may not be the same as `platformURLRoot` if the configuration document will be deployed to a different OMAG Server Platform from the one used to maintain it.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-url-root?url={{targetPlatformURLRoot}}
    ```

    ??? question "What is the difference between {{platformURLRoot}} and {{targetPlatformURLRoot}}?"
        The `{{targetPlatformURLRoot}}` gives the location of the OMAG Server Platform on which this configured service is intended to run, while the `{{platformURLRoot}}` gives the location of the OMAG Server Platform in which this configuration document is maintained.

        They could be, but do not need to be, the same location.

??? post "setMaxPageSize"
    The maximum page size value sets an upper limit on the number of results that a caller can request on any paging REST API to this server. Setting maximum page size helps to prevent a denial of service attack that uses very large requests to overwhelm the server. A value of `0` means no limit, and leaves the server open to such attacks.
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/max-page-size?limit={{maxPageSize}}
    ```

### Retrieving a server's basic properties

It is possible to retrieve the basic server properties to verify the values they are set to.

--8<-- "snippets/admin/calls/get-basic-server-properties.md"


