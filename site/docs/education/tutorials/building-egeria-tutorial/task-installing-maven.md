<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Installing Maven

[Apache Maven :material-dock-window:](https://maven.apache.org/){ target=maven } is a build tool at is being phased out in the Egeria project, but is still required by some repositories. It is capable of code compilation, running unit tests, validating dependencies and Javadoc as well as build our distribution archive.

where it is used, Egeria requires Maven 3.5 or higher. 3.6.x or above is recommended.

!!! cli "Check if Maven is installed"
    ```shell
    mvn --version
    ```

Maven can be installed by downloading the software from the Apache maven website and unpacking it into a directory that is included in your `PATH`. Alternatively these methods are available:

=== "HomeBrew (MacOS)"

    !!! cli "Install Maven through [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew install maven
        ```

=== "RedHat"

    !!! cli "Install through `yum`"
        ```shell
        yum install maven
        ```

=== "Debian"

    !!! cli "Install through `apt-get`"
        ```shell
        apt-get install maven
        ```

=== "Windows"

    On Windows, you should use [Windows Subsystem for Linux :material-dock-window:](https://docs.microsoft.com/en-us/windows/wsl/){ target=ms } Version 2 or above, install an appropriate Linux distribution, and follow the instructions for that Linux distribution.


--8<-- "snippets/abbr.md"

