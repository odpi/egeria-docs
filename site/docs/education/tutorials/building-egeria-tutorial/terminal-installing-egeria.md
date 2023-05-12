<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


The [egeria build process](/education/tutorials/building-egeria-tutorial/overview) creates the distribution files for Egeria in the `open-metadata-distribution/open-metadata-assemblies` project.   To see its contents, after a full gradle build completes, use the following `cd` command to change to its `build/distributions` directory:

```bash
cd open-metadata-distribution/open-metadata-assemblies/build/distributions
```
List the files:
```bash
ls
```
The distribution tar file is `{{release}}-distribution.tar.gz` or `egeria-4.1-distribution.tar.gz` in this example.

```bash
egeria-4.1-distribution.tar.gz
```

Create a directory for the install and copy the tar file into it. The two commands shown below create an install directory in your home directory and then copies the egeria distribution file into it.

```bash
mkdir ~/egeria-install
```
```bash
cp egeria*-distribution.tar.gz ~/egeria-install
```

These next commands change to the new directory and lists its contents.

```bash
cd ~/egeria-install
```

It is now possible to unpack the tar file with the following steps.

```bash
gunzip egeria*-distribution.tar.gz
```
```bash
tar -xf egeria*-distribution.tar
```
A new directory is created called `{{release}}-distribution.tar.gz` or `egeria-4.1-distribution.tar.gz` in this example.  Change to this new directory and list its contents as shown below.

```bash
cd egeria*gz
```
```bash
ls
```
```bash
LICENSE			content-packs		samples			user-interface
NOTICE			keystore.p12		server			utilities
conformance-suite	sample-data		truststore.p12
```

As before, you may notice different files as Egeria evolves.

Under `server` is a directory for the [OMAG Server Platform](/concepts/omag-server-platform) that is used to run open metadata and governance services.  This is the `server-chassis-spring-4.1.jar`.  

```bash
ls server
```
```bash
lib				server-chassis-spring-4.1.jar
```
The `lib` directory is where the jar files for connectors, samples and new registered services are installed.  The initial list includes the connectors that are located in the `egeria.git` repository.
```bash
ls server/lib
```
```bash
audit-log-console-connector-4.1.jar
audit-log-event-topic-connector-4.1.jar
audit-log-file-connector-4.1.jar
audit-log-slf4j-connector-4.1.jar
avro-file-connector-4.1.jar
basic-file-connector-4.1.jar
cohort-registry-file-store-connector-4.1.jar
configuration-encrypted-file-store-connector-4.1.jar
configuration-file-store-connector-4.1.jar
csv-file-connector-4.1.jar
data-folder-connector-4.1.jar
discovery-service-connectors-4.1.jar
dynamic-archiver-connectors-4.1.jar
elasticsearch-integration-connector-4.1.jar
files-integration-connectors-4.1.jar
governance-action-connectors-4.1.jar
governance-services-sample-4.1.jar
graph-repository-connector-jar-with-dependencies-4.1.jar
inmemory-open-metadata-topic-connector-4.1.jar
inmemory-repository-connector-4.1.jar
kafka-integration-connector-4.1.jar
kafka-open-metadata-topic-connector-4.1.jar
omrs-rest-repository-connector-4.1.jar
open-lineage-janus-connector-4.1.jar
open-metadata-archive-directory-connector-4.1.jar
open-metadata-archive-file-connector-4.1.jar
open-metadata-security-samples-4.1.jar
openapi-integration-connector-4.1.jar
openlineage-integration-connectors-4.1.jar
spring-rest-client-connector-4.1.jar
```

Copy the jar files for any additional connectors you want to use into the `lib` directory.  The connectors available for Egeria are listed in the [Connector Catalog](/connectors).

The `content-packs` directory contains [Open Metadata Archives](/concepts/open-metadata-archive) that provide sample open metadata content.  The `README.md` describes their content.
```bash
ls content-packs
```
```bash
CloudInformationModel.json			DataStoreConnectorTypes.json
CocoBusinessSystemsArchive.json			OpenConnectorsArchive.json
CocoClinicalTrialsTemplatesArchive.json		OpenMetadataTypes.json
CocoComboArchive.json				README.md
CocoGovernanceEngineDefinitionsArchive.json	SimpleAPICatalog.json
CocoGovernanceProgramArchive.json		SimpleDataCatalog.json
CocoOrganizationArchive.json			SimpleEventCatalog.json
CocoSustainabilityArchive.json			SimpleGovernanceCatalog.json
CocoTypesArchive.json
```
The `sample-data` directory contains sample data that is used in various labs and samples.
```bash
ls sample-data/*
```
```bash
sample-data/oak-dene-drop-foot-weekly-measurements:
week1.csv	week3.csv	week5.csv	week7.csv	week9.csv
week2.csv	week4.csv	week6.csv	week8.csv

sample-data/old-market-drop-foot-weekly-measurements:
week1.csv	week3.csv	week5.csv	week7.csv	week9.csv
week2.csv	week4.csv	week6.csv	week8.csv
```
--8<-- "snippets/abbr.md"
