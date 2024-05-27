<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


At the top of the distribution is a Docker script (called `DockerFile`) that converts the distribution into a Docker container for running in a cloud environment.  If Egeria is to run in a cloud environment then this script is run after you have customized the content of the distribution.  This customization may involve adding connector implementations and, if it is for production use, stripping out the examples, samples and libraries that you do not need.

The `assembly` directory contains the real content of the distribution.  This is where the content packs, connectors, sample configuration and runtime libraries are located.  It is organized into three parts:

* The `platform` directory includes all the files needed to run the platform.
* The `etc` directory has additional files and utilities that can be helpful when running the platform.
* The `opt` directory has samples and other useful content that can be helpful when experimenting with Egeria.

To run the platform, change to the `platform` directory and follow the instructions in the `README.md`.

### Content Packs

The content packs are located in the `opt/content-packs` directory.  They include:

* [Core Content Pack](/content-packs/core-content-pack/overview) that provides metadata to configure and call the connectors included in the distribution.
* [Cloud Information Model](/content-packs/cim-content-pack/overview) that provides a simple commerce [glossary](/practices/common-data-definitions/overview).
* [Coco Pharmaceuticals Sample Metadata](/content-packs/coco-content-pack/overview) that provides metadata that drives the [Coco Pharmaceuticals scenarios](/practices/coco-pharmaceuticals).
* [Simple Catalog Content Pack](/content-packs/simple-content-pack/overview) that provides a simple asset catalog showing how databases, APIs and Events can be catalogued and linked together with a glossary term.
* [Open Metadata Types Content Pack](/content-packs/types-content-pack/overview) that provides the definitions of the [Open Metadata Types](/types).
    
### Sample Configurations

The `opt/sample-configs` directory contains the configuration for five Egeria servers (called [OMAG Servers](/concepts/omag-server)) that all run on a single instances of Egeria's platform (called the [OMAG Server Platform](/concepts/omag-server-platform)).  Server configuration defines which of Egeria's services are active, which in turn defines the types of connectors that can run. The sample configurations are sufficient to run most Egeria use cases.  Adding additional servers is often needed just to scale the deployment.

The servers are:

* **simple-metadata-store** is a [Metadata Access Store](/concepts/metadata-access-store/) that provides REST APIs for retrieving and maintaining open metadata. This server is set up to use a repository that keeps its metadata in memory. It loads the [Simple Catalog Content Pack](https://egeria-project.org/content-packs/simple-content-pack/overview/). This means that each time the server is restarted, it starts with just the content of the [Simple Catalog Content Pack](/content-packs/simple-content-pack/overview) in its repository.

The `simple-metadata-store` server is not configured to use Apache Kafka and so it does not produce events when metadata is changed. The next set of servers make use of Apache Kafka to both send and receive events. The Apache Kafka broker should be listening at `localhost:9092`.

* **active-metadata-store** is a [Metadata Access Store](/concepts/metadata-access-store/) that supports both REST APIs for retrieving and maintaining open metadata along with event notifications each time there is change in the metadata.  It is storing its metadata in an XTDB key-value repository stored on the local file system under the `platform/data/servers/active-metadata-store` directory.  This means that any metadata that you create will still be in the repository when you restart this server. (The repository can be cleared by deleting the `platform/data/servers/active-metadata-store/repository` directory.) This server automatically loads the [Core ]

* **integration-daemon** is an [Integration Daemon](https://egeria-project.org/concepts/integration-daemon/) that catalogs files stored on the filesystem.  It is set up to catalog any file located in `sample-data/data-files` under the `platform` directory. It is also looking for additional configuration added to active-metadata-store under the **Egeria:IntegrationGroup:DefaultIntegrationGroup** [integration group](https://egeria-project.org/concepts/integration-group/).

* **engine-host** is an [Engine Host](https://egeria-project.org/concepts/engine-host/) that is running the **AssetSurvey** and **AssetGovernance** [governance engines](https://egeria-project.org/concepts/governance-engine/) used to create and manage metadata.  The configuration of these governance engines is found in the active-metadata-store.

The final server provides the services for Egeria's UIs.

* **view-server** is a [View Server](https://egeria-project.org/concepts/view-server/) that calls the active-metadata-store to send and retrieve metadata from its repository.  Its services are designed to support calls from non-Java environments such as python and javascript. Egeria's user interfaces make calls to the view server.

These service call one another as follows:

![Sample server interactions](/guides/planning/sample-configs.svg)