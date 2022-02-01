<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Testing Tools

## Postman

[Postman :material-dock-window:](https://www.postman.com/){ target=postman } is an interactive tool for calling REST APIs. The Egeria community uses Postman for demos and education as well as testing APIs during development.

![Postman client](/education/tutorials/postman-tutorial/postman-client.png)

!!! attention "Disable SSL certificate verification"
    Egeria by default uses secure HTTP requests (`https://`) with a self-signed certificate. By default, Postman does not allow self-signed certificates. Any Postman users will therefore need to go into **Preferences** -> **Settings** and on the **General** tab, turn off **SSL certificate verification** or requests will fail.

    ![Turn off self-signed certificate checking](/education/tutorials/postman-turn-off-certificate-checking.png)

!!! education "Further information"

    - [Egeria-specific Postman tutorial](/education/tutorials/postman-tutorial/overview).
    - [Adding Postman samples](/guides/contributor/guidelines/#postman-artifacts-for-apis)

## Command-line request tools

In addition to [Postman](#postman) there are command line tools for calling REST APIs.

### `curl`

The command that is most commonly available is `curl`.

!!! cli "Example `curl` command"
    ```shell
    curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/test/server-platform/origin
    ```

!!! attention "Disable SSL certificate verification"
    Note that Egeria is using `https://`, so if you have not replaced the provided self-signed certificate, ensure you include `--insecure` on any requests to skip certificate validation.

### `HTTPie`

As an alternative to `curl` you might like to try [HTTPie :material-dock-window:](https://httpie.org/){ target=httpie }, which has more advanced functions.

!!! attention "Disable SSL certificate verification"
    Note that Egeria is using `https://`, so if you have not replaced the provided self-signed certificate, ensure you include `--verify no` to any requests to skip certificate validation.

--8<-- "snippets/abbr.md"
