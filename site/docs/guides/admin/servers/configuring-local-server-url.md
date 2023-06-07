<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Set the server URL root

Configure the `targetPlatformURLRoot` with the [platform URL Root](/concepts/omag-server/#platform-url-root) value of where the OMAG Server Platform will run.
This may not be the same as `platformURLRoot` if the configuration document will be deployed to a different OMAG Server Platform from the one used to maintain it.

!!! post "POST - set server URL root"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-url-root?url={{targetPlatformURLRoot}}
    ```

??? question "What is the difference between {{platformURLRoot}} and {{targetPlatformURLRoot}}?"
    The `{{targetPlatformURLRoot}}` gives the location of the OMAG Server Platform on which this configured service is intended to run, while the `{{platformURLRoot}}` gives the location of the OMAG Server Platform in which this configuration document is maintained.

    They could be, but do not need to be, the same location.
