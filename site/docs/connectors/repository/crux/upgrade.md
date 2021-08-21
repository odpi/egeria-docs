<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Upgrading the Crux Connector

The connector embeds its own persistence layer (storage) for metadata in Crux. While we try to keep this underlying storage unchanged as much as possible to ease moving from one version of the connector to another, this is not always possible.

It may therefore be necessary to occasionally migrate any pre-existing metadata stored in the embedded Crux repository in order to make use of the latest features and performance benefits of a new version of the connector.

!!! attention "Persistence layer version must be compatible with connector version"
    To ensure the integrity of the metadata, the connector will validate that the version of the persistence matches the version the connector expects before even attempting to run -- if this validation fails, you will see an `OMRS-CRUX-REPOSITORY-500-003` error in the audit log to indicate that you must first migrate the metadata before running this version of the connector.

    In other words: if migration is needed, the newer version of the connector will not allow you to run against an older set of metadata without first running the migration.

    Your only options will be to continue to use an older version of the connector (with which your pre-existing metadata is compatible), or to run this offline migration of your repository and then run the newer version of the connector.

The migration itself runs outside the connector (while the connector is offline), in order to maximize the throughput of the in-place upgrade of the repository. The time it takes to run the migration naturally depends on a number of factors, such as the amount of pre-existing metadata that must be migrated and the specific changes needed by the upgrade.

As a very approximate metric, we would expect the in-place upgrade to be capable of migrating 60-100 metadata instances (entities or relationships) per second.  So 10 000 instances should take approximately 2 minutes.

## 1. Obtain migrator

Start by downloading the Crux repository migrator:

=== "Latest release"
    [![Release](https://img.shields.io/maven-central/v/org.odpi.egeria/egeria-connector-crux-migrator?label=release)](http://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=org.odpi.egeria&a=egeria-connector-crux-migrator&v=RELEASE&c=jar-with-dependencies)

=== "Latest snapshot"
    [![Development](https://img.shields.io/nexus/s/org.odpi.egeria/egeria-connector-crux-migrator?label=development&server=https%3A%2F%2Foss.sonatype.org)](https://oss.sonatype.org/content/repositories/snapshots/org/odpi/egeria/egeria-connector-crux-migrator/){ target=dl }

The migrator is `egeria-connector-crux-migrator-{version}-jar-with-dependencies.jar`

## 2. Configure repository

Before running the migrator, define the configuration of your repository. The configuration must be defined in a JSON file, following [Crux's JSON configuration format :material-dock-window:](https://opencrux.com/reference/configuration.html){ target=crux }.

??? tip "Take Crux configuration from Egeria connector configuration"
    The simplest way to ensure this matches the configuration used by your connector is to copy the `cruxConfig` property from the request you POST to Egeria to configure your connector. Simply be certain to replace any relative paths with absolute paths to data to ensure the migrator can find the metadata.

??? example "Example connector configuration in Egeria"
    ```json linenums="1" hl_lines="9-31"
    {
      "class": "Connection",
      "connectorType": {
        "class": "ConnectorType",
        "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.crux.repositoryconnector.CruxOMRSRepositoryConnectorProvider"
      },
      "configurationProperties": {
        "cruxConfig":
        {
          "crux/index-store": {
            "kv-store": {
              "crux/module": "crux.rocksdb/->kv-store",
              "db-dir": "data/servers/crux/rdb-index"
            }
          },
          "crux/document-store": {
            "kv-store": {
              "crux/module": "crux.rocksdb/->kv-store",
              "db-dir": "data/servers/crux/rdb-docs"
            }
          },
          "crux/tx-log": {
            "kv-store": {
              "crux/module": "crux.rocksdb/->kv-store",
              "db-dir": "data/servers/crux/rdb-tx"
            }
          },
          "crux.lucene/lucene-store": {
            "db-dir": "data/servers/crux/lucene"
          }
        }
      }
    }    
    ```

## 3. Make a backup

As the migration runs in-place, it is always a good practice to take a backup of your repository first.

Different configurations will require different approaches to backup. If your configuration makes use of pluggable components that have their own backup utilities (Kafka, JDBC, etc) then you should follow the best practices for backing up those components themselves: e.g. from Apache Kafka or the database vendor.

For pluggable components that persist their data directly to the filesystem (RocksDB, Lucene, LMDB, etc), you may be able to simply backup the files directly.

??? caution "Ensure connector is not running before taking backup"
    In all cases, you should ensure that your connector is shutdown (not running), and that any data is appropriately quiesced prior to running the backup.

??? cli "Example filesystem backup"
    For example, running this command when the persistence is using the example configuration above:

    ```shell
    tar cvf backup.tar .../data/servers/crux
    ```

    will backup all the files used by RocksDB and Lucene:

    ```text
    a .../data/servers/crux
    a .../data/servers/crux/rdb-index
    a .../data/servers/crux/lucene
    a .../data/servers/crux/config
    a .../data/servers/crux/cohorts
    a .../data/servers/crux/rdb-tx
    a .../data/servers/crux/rdb-docs
    ...
    ```

## 4. Run the in-place upgrade

Run the following command to execute the in-place upgrade:

!!! cli "Execute the in-place upgrade"
    ```shell
    java -jar egeria-connector-crux-migrator-*-jar-with-dependencies.jar config.json
    ```

    Where `config.json` is the file containing your repository's configuration.

If you run the migrator and no migration is actually needed, the output will indicate that your repository is already at the necessary version to work with this version of the connector, and no migration is needed. You can simply proceed with running the connector.

??? success "Example output when no migration is needed"
    ```text
    Starting a Crux node using configuration: config.json
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    ... checking if migration is needed (crux.api.java.JCruxNode@25c4bb06)
    This node is already at the latest version of the persistence layer -- no migration needed.
    ```

If a migration is necessary, it will immediately begin to run. The output will indicate the existing version of the persistence layer, and the version that is expected by this version of the connector. If you are making a jump across several migrations, you may see this last line appear multiple times with different existing versions listed each time: the in-place upgrade sequentially applies the necessary migrations step-by-step.

??? success "Example output when migration is required"
    ```text
    Starting a Crux node using configuration: config.json
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
    ... checking if migration is needed (crux.api.java.JCruxNode@25c4bb06)
    The node is at version -1, while latest is 2 -- migrating...
    ```

## 5. Start the connector

Once the previous (in-place upgrade) command completes, you should now be able to start your connector. See the [instructions on configuring the connector](/egeria-docs/connectors/repository/crux/#configuration) for more details.

## Change log

There should be no need to actually understand these details, as the connector (and migration) will handle them for you. However, for the interested reader, the following changes were made to the storage layer in the specified release:

### 2.9

- `InstanceAuditHeaderMapping` no longer separates the type GUID and supertype GUIDs, but places all such information into a single vector (for improved search performance)
- `RelationshipMapping` no longer has separate properties for each entity proxy, but stores them as a vector: this retains their ordering, but allows relationships to be more efficiently searched from either related entity

--8<-- "snippets/abbr.md"
