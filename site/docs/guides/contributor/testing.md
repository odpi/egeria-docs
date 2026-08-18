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

--8<-- "snippets/abbr.md"
