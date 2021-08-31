<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the basic properties

The basic properties of the OMAG Server are used in logging and events originating from the server. They help to document the purpose of the server (which helps with problem determination) and enable performance improvements by allowing the server to ignore activity or metadata that is not relevant to its operation.

The basic properties include two unique identifiers:

| Property | Description |
|---|---|
| `localServerId` | Unique identifier for this server. By default, this is initialized to a randomly generated Universal Unique identifier (UUID). |
| `localServerName` | Meaningful name for the server for use in messages and UIs. Ideally this value is unique to aid administrators in understanding the source of messages and events from the server. This value is set to the server name assigned when the configuration is created. |

The other basic properties have values that can be changed through the admin services API:

| Property | Description |
|---|---|
| `localServerType` | Descriptive type name for the server. Again this is useful information for the administrator to understand the role of the server. The default value is `Open Metadata and Governance Server`. |
| `organizationName` | Descriptive name for the organization that owns the local server/repository. This is useful when the open metadata repository cluster consists of metadata servers from different organizations, or different departments of an enterprise. The default value is `null`. |
| `localServerUserId` | UserId to use for server-initiated REST calls. The default is `OMAGServer`. |
| `localServerPassword` | Password to use for server-initiated REST calls. The default is `null`. This means that only the userId is sent in the HTTP header. |
| `maxPageSize` | The maximum page size that can be set on requests to the server. The default value is `1000`. A value of zero means unlimited page size. Although supported, the zero value is not recommended because it provides no protection from a large request denial of service attack. |

The sections that follow cover how to set up these values.

### Set server type name

The server type name should be set to something that describes the OMAG Server's role. It may be the name of a specific product that it is enabling, or a role in the metadata and governance landscape.

!!! post "POST - set server type"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-type?typeName="{{serverTypeName}}"
    ```

### Set organization name

The organization name may be the owning organization or department or team supported by the server.

!!! post "POST - set organization name"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/organization-name?name="{{organizationName}}"
    ```

### Set the server's user ID and optional password

The server's user ID is used when processing requests that do not have an end user, such as receiving an event from a topic. The default value is `OMAGServer`. Ideally each server should have its own user ID so it is possible to restrict the resources that each server has access to.

If the password is specified as well, the userId and password combination are used to provide authentication information on each REST call made by the server.

!!! post "POST - set server's userId"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-user-id?id="{{serverUserId}}"
    ```

!!! post "POST - set server's password"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-user-password?password="{{serverUserPassword}}"
    ```

### Set the maximum page size for REST API requests

The maximum page size value sets an upper limit on the number of results that a caller can request on any paging REST API to this server. Setting maximum page size helps to prevent a denial of service attack that uses very large requests to overwhelm the server. A value of `0` means no limit, and leaves the server open to such attacks.

!!! post "POST - set maximum page size"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/max-page-size?limit={{maxPageSize}}
    ```
