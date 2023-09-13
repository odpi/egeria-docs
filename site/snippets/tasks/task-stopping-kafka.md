<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Shutting down Apache Kafka

=== "Command Line"

    !!! cli "From within the `bin` folder of Apache Kafka"
        ```shell
        ./kafka-server-stop.sh
        ./zookeeper-server-stop.sh
        ```

=== "HomeBrew"

    !!! cli "When installed via [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew services stop kafka
        brew services stop zookeeper
        ```


