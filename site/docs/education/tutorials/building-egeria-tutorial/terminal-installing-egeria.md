<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->



The [egeria build process](/education/tutorials/building-egeria-tutorial/overview) creates the distribution files for Egeria in the `open-metadata-distribution` module.   To see its contents, after a full gradle build completes, use the following `cd` command to change to its `build/distributions` directory:

```bash
cd open-metadata-distribution/open-metadata-assemblies/build/distributions
```
List the files:
```bash
ls
```
The distribution tar file is `{{release}}-distribution.tar.gz` or `egeria-3.14-distribution.tar.gz` in this example.

```bash
egeria-3.14-distribution.tar.gz
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
gunzip -xf egeria*-distribution.tar.gz
```
```bash
tar -xf egeria*-distribution.tar
```
A new directory is created called `{{release}}-distribution.tar.gz` or `egeria-3.14-distribution.tar.gz` in this example.  Change to this new directory and list its contents as shown below.

```bash
cd egeria-omag*
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

Under `server` is a directory for the [OMAG Server Platform](/concepts/omag-server-platform) that is used to run open metadata and governance services.  This is the `server-chassis-spring-3.14.jar`.  

```bash
ls server
```
```bash
lib				server-chassis-spring-3.14.jar
```
The `lib` directory is where the jar files for connectors, samples and new registered services are installed.  The initial list includes the connectors that are located in the `egeria.git` repository.
```bash
ls server/lib
```
```bash
audit-log-console-connector-3.14.jar
audit-log-event-topic-connector-3.14.jar
audit-log-file-connector-3.14.jar
audit-log-slf4j-connector-3.14.jar
avro-file-connector-3.14.jar
basic-file-connector-3.14.jar
cohort-registry-file-store-connector-3.14.jar
configuration-encrypted-file-store-connector-3.14.jar
configuration-file-store-connector-3.14.jar
csv-file-connector-3.14.jar
data-folder-connector-3.14.jar
discovery-service-connectors-3.14.jar
dynamic-archiver-connectors-3.14.jar
elasticsearch-integration-connector-3.14.jar
files-integration-connectors-3.14.jar
governance-action-connectors-3.14.jar
governance-services-sample-3.14.jar
graph-repository-connector-jar-with-dependencies-3.14.jar
inmemory-open-metadata-topic-connector-3.14.jar
inmemory-repository-connector-3.14.jar
kafka-integration-connector-3.14.jar
kafka-open-metadata-topic-connector-3.14.jar
omrs-rest-repository-connector-3.14.jar
open-lineage-janus-connector-3.14.jar
open-metadata-archive-directory-connector-3.14.jar
open-metadata-archive-file-connector-3.14.jar
open-metadata-security-samples-3.14.jar
openapi-integration-connector-3.14.jar
openlineage-integration-connectors-3.14.jar
spring-rest-client-connector-3.14.jar
```

Copy the jar files for any additional connectors you want to use into the `lib` directory.  The connectors available for Egeria are listed in the [Connector Catalog](/connectors).

--8<-- "snippets/abbr.md"
