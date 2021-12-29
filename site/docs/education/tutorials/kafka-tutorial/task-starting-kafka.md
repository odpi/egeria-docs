<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Starting Apache Kafka

=== "Command Line"

    !!! cli "From within the `bin` folder of Apache Kafka"
        ```shell
        ./zookeeper-server-start.sh ../config/zookeeper.properties &
        rm -rf /tmp/kafka-logs/*
        ./kafka-server-start.sh ../config/server.properties
        ```

=== "HomeBrew"

    !!! cli "When installed via [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew services start zookeeper
        brew services start kafka
        ```

--8<-- "snippets/abbr.md"
