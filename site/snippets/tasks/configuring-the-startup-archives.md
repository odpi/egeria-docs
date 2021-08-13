<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Load metadata

[Open metadata archives](/egeria-docs/concepts/open-metadata-archive) contain pre-canned metadata types and instances for [cohort members](/egeria-docs/services/omrs/cohort/#cohort-members).

Archives can be [added to the configuration document](#configure-metadata-to-load-on-startup) of a server to ensure their content is loaded each time the server is started. This is intended for repositories that do not store the archive content but keep it in memory.

Archives can also be [loaded to a running server](#add-to-a-running-server).

!!! attention "Loading the same archive multiple times"
    If an archive is loaded multiple times, its content is only added to the local repository
    if the repository does not have the content already.

### Add to a running server

Typically, an open metadata archive is stored as JSON format in a file. To load such a file use the following command:

!!! post "POST - load file"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/instance/open-metadata-archives/file
    ```

    The body of the request should be the fully-qualified path name or path relative to the startup directory of the OMAG Server Platform -- and the file name should not have any quotes around it.

Alternatively it is possible to set up the list of open metadata archives as a list of [connections](/egeria-docs/concepts/connection). These connections refer to [open metadata archive connectors](/egeria-docs/connectors/open-metadata-archive-store-connector) that can read and retrieve the open metadata archive content.

!!! post "POST - load from connection(s)"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/instance/open-metadata-archives/connection
    ```

    The body of the request should be the list of connections from which to load archives.

This option can be used when the open metadata archives are not stored in a file, or a different file format from the default one for the OMAG Server Platform is required.

### Configure metadata to load on startup

Typically, an open metadata archive is stored as JSON format in a file. To configure the load of such a file use the following command:

!!! post "POST - specify file to load"
    ```
    POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/open-metadata-archives/file
    ```

    The body of the request should be the fully-qualified path name or path relative to the startup directory of the OMAG Server Platform -- and the file name should not have any quotes around it.

Alternatively it is possible to set up the list of open metadata archives as a list of [connections](/egeria-docs/concepts/connection). These connections refer to connectors that can read and retrieve the open metadata archive content.

!!! post "POST - specify connection(s) to load"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/open-metadata-archives
    ```

    The body of the request should be the list of connections from which to load archives.

This option can be used when the open metadata archives are not stored in a file, or a different file connector from the default one for the OMAG Server Platform is required.

### Remove metadata load on startup

Finally, this is how to remove the archives from the configuration document.

!!! delete "DELETE - remove archives from configuration document"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/open-metadata-archives
    ```

    The body of the request should be the path to the metadata archive file.
