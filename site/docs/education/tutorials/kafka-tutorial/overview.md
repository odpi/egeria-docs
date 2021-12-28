<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Apache Kafka

[Apache Kafka :material-dock-window:](https://kafka.apache.org){ target=kafka } is an event bus that is used to pass events between different Egeria servers.

Kafka's own [QuickStart Guide :material-dock-window:](https://kafka.apache.org/quickstart){ target=kafka } covers installation and basic usage. You may alternatively wish to install Kafka using a package manager such as [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew } on MacOS.

For Egeria, the Kafka server needs to be running a `PLAINTEXT` listener. From the directory where Kafka is installed, check the `config/server.properties` file so that the `listeners` and `advertised.listeners` are setup as follows:

!!! example "Example: Kafka configuration"
    ```text
    listeners=PLAINTEXT://localhost:9092
    advertised.listeners=PLAINTEXT://localhost:5092
    ```

    The example above uses `localhost:9092` for simplicity, assuming you are running Kafka locally on the same machine where you are doing your development. If running elsewhere, replace this with a name that is fully network resolveable (i.e. by both the host running Kafka and the client machines that will connect to Kafka from other hosts).

## Starting Kafka

=== "MacOS"

    !!! cli "When installed via [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew services start zookeeper
        brew services start kafka
        ```

=== "Linux"

    !!! cli "From within the `bin` folder of Apache Kafka"
        ```shell
        ./zookeeper-server-start.sh ../config/zookeeper.properties &
        rm -rf /tmp/kafka-logs/*
        ./kafka-server-start.sh ../config/server.properties
        ```

## Shutting down Kafka

=== "MacOS"

    !!! cli "When installed via [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew }"
        ```shell
        brew services stop kafka
        brew services stop zookeeper
        ```

=== "Linux"

    !!! cli "From within the `bin` folder of Apache Kafka"
        ```shell
        ./kafka-server-stop.sh
        ./zookeeper-server-stop.sh
        ```

--8<-- "snippets/abbr.md"
