<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


The [egeria build process](/education/tutorials/building-egeria-tutorial/overview) creates the distribution files for Egeria in the `open-metadata-distribution` module.   To see its contents, use the following `cd` command to change to the `target` directory:

```bash
cd open-metadata-distribution/open-metadata-assemblies/target
```
List the files:
```bash
ls -l
```
The name of the files is determined by the release level of the code that you [downloaded from GitHub](/education/tutorials/git-and-git-hub-tutorial/overview/#downloading-the-egeria-source-from-github).  In this example, the release is **egeria-3.3-SNAPSHOT**.  The files in this list will also change as Egeria develops. 
```bash
antrun                                                  egeria-3.6-SNAPSHOT-distribution
archive-tmp                                             egeria-3.6-SNAPSHOT-distribution.tar.gz
egeria-3.6-SNAPSHOT-deploy                              open-metadata-assemblies-3.6-SNAPSHOT-javadoc.jar
egeria-3.6-SNAPSHOT-deploy.tar.gz                       open-metadata-assemblies-3.6-SNAPSHOT-sources.jar
```
The install image tar file is `{{release}}-distribution.tar.gz` or `egeria-3.6-SNAPSHOT-distribution.tar.gz` in this example.

Create a directory for the install and copy the tar file into it.
The two commands shown below create an install directory at the same level in the
file system as the **egeria** build library and then copies the egeria distribution file into it.

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
```bash
ls
```
```bash
egeria-3.6-SNAPSHOT-distribution.tar.gz
```

It is now possible to unpack the tar file.

```bash
tar -xf egeria*-distribution.tar.gz
```
A new directory is created called `egeria-omag-3.6-SNAPSHOT`.  Change to this new directory and list its contents as shown below.

```bash
cd egeria-omag*
```
```bash
ls
```
```bash
LICENSE                 content-packs           samples                 user-interface
NOTICE                  keystore.p12            server                  utilities
conformance-suite       sample-data             truststore.p12

```

As before, you may notice different files as Egeria evolves.

Under `server` is a directory for the [OMAG Server Platform](/concepts/omag-server-platform) that is used to run open metadata and governance services.  This is the `server-chassis-spring-3.6-SNAPSHOT.jar`.  

```bash
ls server
```
```bash
lib				server-chassis-spring-3.6-SNAPSHOT.jar
```
The `lib` directory is where the jar files for connectors, samples and new registered services are installed.  The initial list includes the connectors that are located in the `egeria.git` repository.
```bash
ls server/lib
```
```bash
audit-log-console-connector-3.6-SNAPSHOT.jar
audit-log-event-topic-connector-3.6-SNAPSHOT.jar
audit-log-file-connector-3.6-SNAPSHOT.jar
audit-log-slf4j-connector-3.6-SNAPSHOT.jar
avro-file-connector-3.6-SNAPSHOT.jar
basic-file-connector-3.6-SNAPSHOT.jar
cohort-registry-file-store-connector-3.6-SNAPSHOT.jar
configuration-encrypted-file-store-connector-3.6-SNAPSHOT.jar
configuration-file-store-connector-3.6-SNAPSHOT.jar
csv-file-connector-3.6-SNAPSHOT.jar
data-folder-connector-3.6-SNAPSHOT.jar
discovery-service-connectors-3.6-SNAPSHOT.jar
dynamic-archiver-connectors-3.6-SNAPSHOT.jar
elasticsearch-integration-connector-3.6-SNAPSHOT.jar
files-integration-connectors-3.6-SNAPSHOT.jar
governance-action-connectors-3.6-SNAPSHOT.jar
governance-services-sample-3.6-SNAPSHOT.jar
graph-repository-connector-3.6-SNAPSHOT-jar-with-dependencies.jar
inmemory-open-metadata-topic-connector-3.6-SNAPSHOT.jar
inmemory-repository-connector-3.6-SNAPSHOT.jar
kafka-integration-connector-3.6-SNAPSHOT.jar
kafka-open-metadata-topic-connector-3.6-SNAPSHOT.jar
omrs-rest-repository-connector-3.6-SNAPSHOT.jar
open-lineage-janus-connector-3.6-SNAPSHOT.jar
open-metadata-archive-directory-connector-3.6-SNAPSHOT.jar
open-metadata-archive-file-connector-3.6-SNAPSHOT.jar
open-metadata-security-samples-3.6-SNAPSHOT.jar
openapi-integration-connector-3.6-SNAPSHOT.jar
openlineage-integration-connectors-3.6-SNAPSHOT.jar
spring-rest-client-connector-3.6-SNAPSHOT.jar
```

--8<-- "snippets/abbr.md"
