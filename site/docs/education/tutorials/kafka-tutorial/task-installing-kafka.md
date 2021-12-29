<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Installing Apache Kafka

Apache Kafka's own [QuickStart Guide :material-dock-window:](https://kafka.apache.org/quickstart){ target=kafka } covers installation and basic usage. You may alternatively wish to install Kafka using a package manager such as [HomeBrew :material-dock-window:](https://brew.sh){ target=homebrew } on MacOS.

#### Apache Zookeeper Dependency

[Apache ZooKeeper](https://zookeeper.apache.org) is used by Apache Kafka for maintaining certain configuration
information. It is therefore typically a pre-requisite to using Apache Kafka.

The [QuickStart Guide provided by Kafka itself](https://kafka.apache.org/quickstart) includes quick-and-dirty
instructions on running a minimal ZooKeeper server necessary for Kafka's use. For more detailed information,
you will want to read the [ZooKeeper Getting Started Guide](https://zookeeper.apache.org/doc/current/zookeeperStarted.html).

#### Configuration

For Egeria, the Kafka server needs to be running a `PLAINTEXT` listener. From the directory where Kafka is installed, check the `config/server.properties` file so that the `listeners` and `advertised.listeners` are setup as follows:

!!! example "Example: Kafka configuration"
    ```text
    listeners=PLAINTEXT://localhost:9092
    advertised.listeners=PLAINTEXT://localhost:5092
    ```

    The example above uses `localhost:9092` for simplicity, assuming you are running Kafka locally on the same machine where you are doing your development. If running elsewhere, replace this with a name that is fully network resolveable (i.e. by both the host running Kafka and the client machines that will connect to Kafka from other hosts).


--8<-- "snippets/abbr.md"
