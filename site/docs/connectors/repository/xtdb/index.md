<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# XTDB OMRS Repository Connector

??? success "Fully conformant with all Egeria profiles"
    Last tested on [release 3.1 of Egeria, release 3.1 of connector using release 1.18.1 of XTDB](performance.md).

    Profile | Result
    ---|---
    [Metadata sharing](/egeria-docs/guides/cts/profiles/metadata-sharing) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Reference copies](/egeria-docs/guides/cts/profiles/reference-copies) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Metadata maintenance](/egeria-docs/guides/cts/profiles/metadata-maintenance) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Dynamic types](/egeria-docs/guides/cts/profiles/dynamic-types) | :material-help: UNKNOWN_STATUS
    [Graph queries](/egeria-docs/guides/cts/profiles/graph-queries) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Historical search](/egeria-docs/guides/cts/profiles/historical-search) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Entity proxies](/egeria-docs/guides/cts/profiles/entity-proxies) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Soft-delete and restore](/egeria-docs/guides/cts/profiles/soft-delete-and-restore) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Undo an update](/egeria-docs/guides/cts/profiles/undo-an-update) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Reidentify instance](/egeria-docs/guides/cts/profiles/reidentify-instance) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Retype instance](/egeria-docs/guides/cts/profiles/retype-instance) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Rehome instance](/egeria-docs/guides/cts/profiles/rehome-instance) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Entity search](/egeria-docs/guides/cts/profiles/entity-search) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Relationship search](/egeria-docs/guides/cts/profiles/relationship-search) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Entity advanced search](/egeria-docs/guides/cts/profiles/entity-advanced-search) | :material-check-all: CONFORMANT_FULL_SUPPORT
    [Relationship advanced search](/egeria-docs/guides/cts/profiles/relationship-advanced-search) | :material-check-all: CONFORMANT_FULL_SUPPORT

    ??? info "Additional notes"
        - The entity search tests could fail a particular long-running query pattern unless Lucene is configured: typically where a query by value or attribute is done without providing any restriction on the type of instances against which the query should run. Configure the connector with Lucene to avoid these timeouts.
        - The [Dynamic types](/egeria-docs/guides/cts/profiles/dynamic-types) profile currently does not have any tests defined, so will be `UNKNOWN_STATUS` for all repositories and connectors.

=== "Latest release"
    [![Release](https://img.shields.io/maven-central/v/org.odpi.egeria/egeria-connector-crux?label=release)](http://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=org.odpi.egeria&a=egeria-connector-crux&v=RELEASE&c=jar-with-dependencies)

=== "Latest snapshot"
    [![Development](https://img.shields.io/nexus/s/org.odpi.egeria/egeria-connector-xtdb?label=development&server=https%3A%2F%2Foss.sonatype.org)](https://oss.sonatype.org/content/repositories/snapshots/org/odpi/egeria/egeria-connector-xtdb/){ target=dl }

    Navigate to the latest snapshot directory, and within that find the latest connector archive with the name: `egeria-connector-xtdb-{version}-jar-with-dependencies.jar`

=== "Source"
    The connector is hosted in its own repository at [odpi/egeria-connector-xtdb :material-github:](https://github.com/odpi/egeria-connector-xtdb){ target=gh }, where the source code can be cloned and the connector built from source.

The *XTDB OMRS repository connector* enables the use of [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb } (formerly known as "Crux") and its own pluggable architecture to support a variety of underlying storage back-ends including S3, RocksDB, Apache Kafka, LMDB, JDBC and more.

XTDB supports temporal graph queries to provide native support for storing historical information and answering temporal queries. The connector is also capable of running as a highly-available service. In addition, currently this is the highest-performance open source persistent repository for Egeria across all operations: read, write, update, search and purge.

## How it works

The XTDB OMRS Repository Connector is a [repository connector](/egeria-docs/connectors/repository), hosted by the [plugin repository proxy](/egeria-docs/services/omrs/todo), running on a [metadata access store](/egeria-docs/concepts/metadata-access-store).

![Operation of the XTDB OMRS repository connector](xtdb-connector-overview.svg)

XTDB itself is started as an embedded process within the connector. It can be configured to use any of the various pluggable persistence layers supported by XTDB itself, and communication between the Java code of the connector and XTDB itself (which is implemented in Clojure) occurs directly via the XTDB Java API (not via REST).

The repository connector (and metadata collection) methods of the repository connector interface simply communicate with XTDB via XTDB's Java API to read and write information to the underlying XTDB node.

XTDB itself handles write transactions and persistence guarantees via its APIs, ensuring that all data is at least recorded into the transaction log and document store prior to any write method returning.

!!! tip "Synchronous by default, but configurable for asynchronous operation"
    By default, the repository connector further awaits confirmation that any write has been indexed (and is therefore available for read operations) prior to returning. However, it is also possible to [configure the connector in an "ingest-optimized" mode](#connector-options) that allows the indexing to occur asynchronously, and can therefore improve the speed of write operations significantly.

## Configuration

The following options are used to configure this connector, as part of the [*configure the local repository* step when configuring a metadata server](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-point/#configure-the-local-repository).

### Pluggable persistence

There are many options for configuring XTDB itself.

A list of overall persistence modules and deeper configuration options for each can be found through [XTDB's own documentation :material-dock-window:](https://xtdb.com/reference/configuration.html){ target=xtdb }.

To enable persistence, there are two options:

- send in the JSON document configuration outlined in [XTDB's own documentation :material-dock-window:](https://xtdb.com/reference/configuration.html){ target=xtdb } directly to the `xtdbConfig` key of the `configurationProperties` property of Egeria's connector configuration
- send in a string to the `xtdbConfigEDN` key of the `configurationProperties` of Egeria's connector configuration, which gives the EDN form of configuration outlined in [XTDB's own documentation :material-dock-window:](https://xtdb.com/reference/configuration.html){ target=xtdb }

Both approaches are valid and should be equally functional, but occasionally a bug may crop up that makes one or the other more or less feasible for a particular configuration.

??? example "Example persistence using JSON configuration"
    ```json linenums="1" hl_lines="8-30"
    {
      "class": "Connection",
      "connectorType": {
        "class": "ConnectorType",
        "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
      },
      "configurationProperties": {
        "xtdbConfig": {
          "xtdb.lucene/lucene-store": {
            "db-dir": "data/servers/xtdb/lucene"
          },
          "xtdb/index-store": {
            "kv-store": {
              "xtdb/module": "xtdb.rocksdb/->kv-store",
              "db-dir": "data/servers/xtdb/rdb-index"
            }
          },
          "xtdb/document-store": {
            "kv-store": {
              "xtdb/module": "xtdb.rocksdb/->kv-store",
              "db-dir": "data/servers/xtdb/rdb-docs"
            }
          },
          "xtdb/tx-log": {
            "kv-store": {
              "xtdb/module": "xtdb.rocksdb/->kv-store",
              "db-dir": "data/servers/xtdb/rdb-tx"
            }
          }
        }
      }
    }
    ```

    !!! attention "Some of the Lucene configuration will be automatically injected"
        When using the JSON-based configuration, some additional entries will be automatically injected to the Lucene configuration by Egeria: specifically the `indexer` and `analyzer` entries used to configure the Lucene index optimally for the OMRS-level search interfaces that Egeria defines. If you have defined your own `analyzer` or `indexer` in the configuration, these will be overridden by the connector's injection process -- in other words, any custom configuration you attempt for `analyzer` or `indexer` will be ignored.

    It is highly recommended to include the Lucene entry like that above as it offers significant performance improvements for any text-based queries.

    The remainder of the configuration in this example defines RocksDB to act as the persistence layer for XTDB's index and document stores, as well as its transaction log.

??? example "Example persistence using EDN configuration"
    ```json linenums="1" hl_lines="8"
    {
      "class": "Connection",
      "connectorType": {
        "class": "ConnectorType",
        "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
      },
      "configurationProperties": {
        "xtdbConfigEDN": "{:xtdb/index-store {:kv-store {:xtdb/module xtdb.rocksdb/->kv-store :db-dir \"data/servers/xtdb/rdb-index\"}} :xtdb/tx-log {:kv-store {:xtdb/module xtdb.rocksdb/->kv-store :db-dir \"data/servers/xtdb/rdb-tx\"}} :xtdb.lucene/lucene-store {:db-dir \"data/servers/xtdb/lucene\" :indexer {:xtdb/module xtdb.lucene.egeria/->egeria-indexer} :analyzer {:xtdb/module xtdb.lucene.egeria/->ci-analyzer}} :xtdb/document-store {:xtdb/module xtdb.jdbc/->document-store :connection-pool {:dialect {:xtdb/module xtdb.jdbc.psql/->dialect} :db-spec {:jdbcUrl \"jdbc:postgresql://myserver.com:5432/mydb?user=myuser&password=mypassword\"}}}}"
      }
    }
    ```

    !!! attention "The Lucene configuration will NOT be automatically injected"
        Unlike the JSON-based configuration, when using the EDN-based configuration the necessary Egeria components of the Lucene configuration will not be automatically injected. Therefore, make sure that your EDN configuration string includes in the Lucene configuration the following keys and settings in addition to the `:db-dir`:

        ```clojure hl_lines="3-4"
        {:xtdb.lucene/lucene-store {
            :db-dir "data/servers/xtdb/lucene"
            :indexer {:xtdb/module xtdb.lucene.egeria/->egeria-indexer}
            :analyzer {:xtdb/module xtdb.lucene.egeria/->ci-analyzer}}
        ```

        These configure the Lucene index optimally for the OMRS-level search interfaces that Egeria defines.

    !!! attention "Ordering of the EDN configuration is important"
        When configuring one of the components to use JDBC connectivity (such as the document store in the example above), the ordering of the configured services in the EDN configuration is important. Any service using a JDBC configuration should be placed at the very end of the EDN configuration. See [issue #246 :material-github:](https://github.com/odpi/egeria-connector-xtdb/issues/246){ target=gh } for details.

!!! tip "You may need to download additional dependencies"
    In general the dependent libraries for most persistence (other than JDBC) is included in the connector `.jar` file itself. For JDBC, you will need to download the appropriate driver for your specific data store and make this `.jar` file available in the same directory as the connector.

    For example, when using PostgreSQL you will need [org.postgresql:postgresql :material-dock-window:](https://search.maven.org/artifact/org.postgresql/postgresql){ target=dl }.

    You can generally determine the additional dependencies you will need by looking at the `project.clj` file of the relevant XTDB module -- specifically its `:dependencies` section. For example, sticking with JDBC, here is the [project.clj :material-github:](https://github.com/xtdb/xtdb/blob/master/modules/jdbc/project.clj){ target=xtdb }:

    ```clojure linenums="14" hl_lines="10"
      :dependencies [[org.clojure/clojure "1.10.3"]
                     [org.clojure/tools.logging "1.1.0"]
                     [com.xtdb/xtdb-core]
                     [pro.juxt.clojars-mirrors.com.github.seancorfield/next.jdbc "1.2.674"]
                     [org.clojure/java.data "1.0.86"]
                     [com.zaxxer/HikariCP "3.4.5"]
                     [pro.juxt.clojars-mirrors.com.taoensso/nippy "3.1.1"]

                     ;; Sample driver dependencies
                     [org.postgresql/postgresql "42.2.18" :scope "provided"]
                     [com.oracle.ojdbc/ojdbc8 "19.3.0.0" :scope "provided"]
                     [com.h2database/h2 "1.4.200" :scope "provided"]
                     [org.xerial/sqlite-jdbc "3.28.0" :scope "provided"]
                     [mysql/mysql-connector-java "8.0.23" :scope "provided"]
                     [com.microsoft.sqlserver/mssql-jdbc "8.2.2.jre8" :scope "provided"]]
    ```

### Connector options

There are currently two configuration options for the connector itself:

| Option | Description |
|---|---|
| `luceneRegexes` | Controls whether the connector will interpret unquoted regexes as Lucene-compatible (true) or not (false): in the latter case ensuring that we fallback to full Java regex checking (which will be significantly slower). |
| `syncIndex` | Controls whether the connector will wait for the XTDB indexes to be updated before returning from write operations (true) or only that they are only guaranteed to be persisted (false). |

!!! example "Example configuration showing the default settings"
    ```json
    {
      "class": "Connection",
      "connectorType": {
        "class": "ConnectorType",
        "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
      },
      "configurationProperties": {
        "xtdbConfig": { },
        "luceneRegexes": true,
        "syncIndex": true
      }
    }
    ```

!!! attention "When `syncIndex` is set to false, all write operations will return null"
    The `syncIndex` parameter is intended for mass ingestion use only. As of v3.2 the connector now makes use of XTDB's transaction function capability to ensure that all write operations are ACID compliant, even when done asynchronously. This guarantees that:

    - the write operation will be persisted and durable when the write operation returns
    - the write operation will be applied sequentially relative to any other (concurrent) write operations

    However, asynchronous mode explicitly means that the write operation will *not* be immediately indexed (for reading). When running this way, the resulting state of a given write operation will not be known until some point in the future. This means that we cannot return a reliable result from the write operation to the caller when the repository is running in asynchronous mode. Rather than returning something that is potentially incorrect, we have therefore opted to ensure that these write operations always return `null` when operating in asynchronous mode.

    You should therefore be careful that when using asynchronous mode you are not relying on any functionality that makes direct use of the results of write operations, as those results will always be `null` in this mode. (And of course, since the write is asynchronous, there will be some period of time during which doing a read operation for that same object will also return either no results or an older / stale version of the result until the write operation has been indexed.)

## High availability

A [sample Helm chart is provided for configuring the XTDB connector for high availability :material-github:](https://github.com/odpi/egeria-connector-xtdb/tree/main/cts/charts/ec-ha-xtdb){ target=gh }. This chart starts up a number of different elements and configures them in a specific sequence.

!!! attention "Sample requires a pre-existing JDBC database"
    The sample chart relies on a pre-existing JDBC database somewhere to use as the document store, and the moment assumes this will be of a PostgreSQL variety (that's the only driver it downloads). A quick setup would be to use [Enterprise DB's k8s operator :material-dock-window:](https://www.enterprisedb.com/docs/kubernetes/cloud_native_postgresql/installation_upgrade/#directly-using-the-operator-manifest){ target=edb } to quickly start up a PostgreSQL cluster in your kubernetes cluster, which is what the following diagrams illustrate[^1].

### Startup

![Kubernetes startup](xtdb-ha-2.svg)

When it is first deployed, the Helm chart starts a number of pods and services: for Egeria (purple), Kafka (red), execution of the Performance Test Suite and a pod used for configuration. (As mentioned above, it assumes a pre-existing JDBC database: a vanilla PostgreSQL cluster (grey) deployed and managed independently by EnterpriseDB's k8s operator.)

Each XTDB pod runs its own separate [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform), in its own JVM, and a script in the `init-and-report` pod will wait until all three pods' OMAG Server Platforms are running before proceeding to any of the following steps. (The `headless` service allows each pod to be directly addressed, without load-balancing, to do such a check.)

### Configure

![Configure Egeria](xtdb-ha-3.svg)

The next script creates a singular configuration document via the `pts` pod, and deploys this common configuration to each of the pods (again using the `headless` service to directly address each one individually): each will have a separate `xtdb` server configured with the same XTDB connector (same [metadata collection id](/egeria-docs/concepts/metadata-collection-id)).

When the `/instance` is called against each pod to start the connector, each will create a local index and instance of the `IXtdb` interface: all pointing to the same golden stores (in this example, Kafka and EDB) where all persistence for XTDB is handled. All servers will refer to the singular `xtdb` load-balancing service as their root URL.

![Configure XTDB](xtdb-ha-4.svg)

### Run

![Run PTS](xtdb-ha-5.svg)

Now when we start the Performance Test Suite, all traffic to the technology under test is routed via this `xtdb` load-balancing service: which will round-robin each request it receives to the underlying pods running the XTDB plugin repository connector.

Kafka has a similar service, which handles load-balancing across its own pods for all write operations.

The underlying JDBC cluster may have a similar load-balancing service again (e.g. if the data store uses sharding), but also may not. In this example the `edb-rw` service layer is instead an abstraction of the primary data store (`edb-1`): all writes will go to this primary data store, while the others act as secondary / standby servers to which EnterpriseDB is automatically handling data replication from the primary. If the primary pod fails, EnterpriseDB can re-point the `edb-rw` service layer to one of these existing secondary stores (which is automatically promoted to primary by EnterpriseDB).

### Outages

![Outages](xtdb-ha-6.svg)

Should there be any outage (in the example above, an Egeria pod, a Kafka pod, and an EnterpriseDB pod all going down) the Kubernetes services will simply stop routing traffic to those pods and the overall service will continue uninterrupted.

Depending on how the underlying services are managed, they may also be able to self-heal:

- Kafka is deployed as a `StatefulSet` in kubernetes, so if any pod fails kubernetes will automatically attempt to start another in its place to keep the total number of replicas defined by the `StatefulSet` running at all times.
- EnterpriseDB in our example was deployed through an operator: this operator self-heals any individual pod failure to e.g. start another standby server pointing at the same `PersistentVolumeClaim` as the failed pod (to pick up the data that was already replicated), switch the primary server to one of the standby servers if the primary server fails, and so on.

### Limitations

There are a number of limitations to be aware of with the high availability configuration:

!!! attention "Must use a non-embedded XTDB back-end"
    Write operations will only be consistent when using a non-embedded XTDB back-end: e.g. Kafka, S3, or JDBC.

!!! attention "Read operations are eventually consistent"
    Since the indexes are local to each pod, read operations will be eventually consistent: the specific pod to which a query is routed may not yet have updated its embedded index with the results of the very latest write operations from some other pod.

    (Note in particular that this has a knock-on impact to our test suites, which currently assume immediate consistency: expect various scenarios to fail if you decide to run them against an eventually-consistent HA configuration.)

!!! danger "Cannot yet be dynamically scaled"
    Currently configuration of Egeria requires making a number of REST API calls, which limits how dynamic we can be in adding or removing pods to an already-running cluster (in particular: [we cannot rely on a readiness probe to indicate pod readiness to process actual work, but only its readiness to be configured](https://github.com/odpi/egeria-connector-xtdb/issues/127#issuecomment-841678140){ target=issue }). We hope to address this soon by allowing configuration and startup to be done without relying on REST calls, at which point we should be able to also support dynamically adding and removing pods from the cluster.

[^1]: For other databases, modify the `JDBC_DRIVER_URL` value in the `configmap.yaml` of the chart to point to the location of the appropriate driver, and replace the use of the `bin/bootstrapConfig.sh` script in the `init-and-report.yaml` template with an inline script in that template (to specify [the appropriate XTDB configuration and JDBC dialect to use for the document store :material-dock-window:](https://xtdb.com/reference/jdbc.html#_example_configuration){ target=xtdb }).

--8<-- "snippets/abbr.md"
