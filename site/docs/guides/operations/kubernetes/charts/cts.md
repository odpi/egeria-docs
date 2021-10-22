<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Conformance Test Suite Chart (egeria-cts)

This is a deployment of Egeria that will automatically run the [Conformance Test Suite's repository workbench](/egeria-docs/guides/cts/overview/#repository-workbench) against a deployed [metadata repository](/egeria-docs/concepts/metadata-repository).

??? success "Prerequisites"
    In order to use the chart, you'll first need to have the following installed:

    - [x] A Kubernetes cluster at 1.15 or above
    - [x] the `kubectl` tool in your path
    - [x] [Helm 3.0 :material-dock-window:](https://github.com/helm/helm/releases){ target=helm } or above

No configuration of the chart is required to use defaults, but information is provided below.

## Installation

!!! cli "Install (deploy) the CTS chart"
    ```shell
    helm dep update egeria-cts
    helm install [-f overrides.yaml] <name> egeria-cts
    ```

    The `-f overrides.yaml` is optional, and only necessary if you are overriding any of the configuration (see options below), while the `<name>` is the name you want to give your deployment.

!!! attention "The installation may take a minute or so"
    This is because it is not only creating the required objects in Kubernetes to run the platforms, but also is configuring Egeria itself - which involves waiting for everything to startup before configuring Egeria via REST API calls.

## Configuration

In a helm chart the configuration that has been externalized by the chart writer is specified in the `values.yaml` file which you can find in this directory. However, rather than edit this file directly, it's recommended you create an additional file with the required overrides (for example, called `overrides.yaml`).

The primary values you will likely want to override in this chart are as follows:

### Technology under test

The *technology under test* ("tut") defines the repository that you want to run the CTS against. By default, the chart will run the CTS against the built-in graph repository. To configure it to test some other repository, you will need to override one or more of the following:

| Parameter | Description |
|---|---|
| `tut.serverType` | Defines the type of the repository to be tested: `native` for a built-in repository of Egeria core (like the in-memory repository), `plugin` for a pluggable native repository (like XTDB), or `proxy` for a third party repository technology (like Apache Atlas). |
| `tut.connectorProvider` | Should be the canonical class name of the connector provider class for the repository connector to use. |
| `tut.connectorConfig` | An optional structure defining any additional configuration for the connector. This should be provided as YAML, and will be automatically translated into JSON to pass through to the `configurationProperties` parameter of the connector when configuring it. |
| `tut.serverEndpoint.host` | When using a third party technology that relies on integrating to a system outside Egeria (i.e. when using a `proxy`), this is the hostname of the third party technology. |
| `tut.serverEndpoint.port` | When using a third party technology that relies on integrating to a system outside Egeria (i.e. when using a `proxy`), this is the port number of the third party technology. |
| `tut.serverEndpoint.protocol` | When using a third party technology that relies on integrating to a system outside Egeria (i.e. when using a `proxy`), this is the protocol to use when accessing the third party technology (e.g. `https`). |
| `tut.serverEndpoint.username` | When using a third party technology that relies on integrating to a system outside Egeria (i.e. when using a `proxy`), this is the username of the system user to use when accessing the third party technology. |
| `tut.serverEndpoint.password` | When using a third party technology that relies on integrating to a system outside Egeria (i.e. when using a `proxy`), this is the password for the system user to use when accessing the third party technology. |

??? example "Example `tut` override for XTDB"
    ```yaml
    tut:
      serverType: "plugin"
      connectorProvider: "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
      connectorConfig:
        xtdbConfig:
          xtdb/index-store:
            kv-store:
              xtdb/module: xtdb.lmdb/->kv-store
              db-dir: data/servers/xtdb/lmdb-index
          xtdb/document-store:
            kv-store:
              xtdb/module: xtdb.rocksdb/->kv-store
              db-dir: data/servers/xtdb/rdb-docs
          xtdb/tx-log:
            kv-store:
              xtdb/module: xtdb.rocksdb/->kv-store
              db-dir: data/servers/xtdb/rdb-tx
          xtdb.lucene/lucene-store:
            db-dir: data/servers/xtdb/lucene
    ```

### Connector downloads

In addition to the general technology under test configuration outlined above, when configuring the chart to test a non-core Egeria connector you also need to specify any dependencies that need to be downloaded to run that connector (i.e. at a minimum to make that connector's connector provider and connector itself available to the pod running the technology under test).

You do this by overriding the `downloads` value with a list of `filename` and `url` pairs.

??? example "Example `downloads` override for XTDB"
    ```yaml
    downloads:
      - filename: egeria-connector-xtdb-LATEST_RELEASE-jar-with-dependencies.jar
        url: "http://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=org.odpi.egeria&a=egeria-connector-xtdb&v=RELEASE&c=jar-with-dependencies"
    ```

??? question "Why both filename and URL?"
    As illustrated in the example above, some URLs may dynamically redirect and resolve to a given filename, for example to always download the latest release of a given file. Because we have minimal utilities installed in the pod to actually dynamically do these downloads, there are cases (like the example above) where the utilities are not able to automatically determine the filename to produce from such dynamic URLs.

    Therefore, by specifying both the URL and the filename we can ensure that the file is downloaded and stored as an expected output (like a `.jar` file) to ensure it can be automatically resolved by e.g. Java's class loader.

## Monitoring progress

You can monitor the progress of the CTS execution by looking at the log output of the `init-and-report` log:

!!! cli "Get the `init-and-report` pod name"
    ```shell
    kubectl get pods -l app.kubernetes.io/component=init-and-report
    ```

??? success "Example output for retrieving the `init-and-report` pod name"
    ```text
    NAME                                       READY   STATUS    RESTARTS   AGE
    p320-10-init-and-report-5845c9bb79-5ddwh   1/1     Running   0          45h
    t12-init-and-report-585b47f74-85r8m        1/1     Running   0          39m
    ```

    If you had multiple CTS deployments running in parallel in your cluster, this may return more than one result (as in the example above). The one that starts with the name you used as the name of your deployment is the one that represents your particular deployment.

Once you have the pod name, you can then view the log:

!!! cli "Review the `init-and-report` pod logs"
    ```shell
    kubectl logs -f <podname>
    ```

    Where the `<podname>` is the name of the pod discovered in the command above (e.g. `t12-init-and-report-585b47f74-85r8m`).

??? success "Example output from the `init-and-report` log"
    This opening section simply displays environment variables that have been configured, primarily useful for debugging or other diagnostics purposes:
    
    ```text
    -- Environment variables --
    ...
    CONNECTOR_PROVIDER=org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider
    ...
    -- End of Environment variables --
    ```
    
    The configuration then occurs. Of primary importance here is that all the results are `200` to indicate each operation was successful:

    ```text
    -- Configuring platform with required servers...
    
    > Configuring conformance test suite driver:
    
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/server-url-root?url=https://t12-platform:9443)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/server-type?typeName=Conformance)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/event-bus?topicURLRoot=egeria)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/cohorts/cts)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/conformance-suite-workbenches/repository-workbench/repositories)
    
    > Configuring technology under test:
    
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/server-url-root?url=https://t12-platform:9443)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/server-type?typeName=TUT)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/organization-name?name=Egeria)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/event-bus?topicURLRoot=egeria)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/local-repository/mode/plugin-repository/connection)
    {"class":"VoidResponse","relatedHTTPCode":200}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/cohorts/cts)
    
    -- End of configuration
    ```
    
    The CTS itself is then started up, followed by the technology under test:

    ```text
    -- Running the conformance test suite...
    
    > Starting conformance test suite:
    
    {"class":"SuccessMessageResponse","relatedHTTPCode":200,"successMessage":"Fri Oct 22 14:43:54 GMT 2021 cts is running the following services: [Open Metadata Repository Services (OMRS), Connected Asset Services, Conformance Suite Services]"}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/cts/instance)
    
    > Starting the technology under test:
    
    {"class":"SuccessMessageResponse","relatedHTTPCode":200,"successMessage":"Fri Oct 22 14:44:12 GMT 2021 tut is running the following services: [Open Metadata Repository Services (OMRS)]"}
    (200 - https://t12-platform:9443/open-metadata/admin-services/users/admin/servers/tut/instance)
    
    -- End of conformance test suite startup
    ```

    Once the CTS is running, a busy loop is then run to wait until the CTS has completed. The status of the CTS execution will be re-checked every 30 seconds and an update printed out to the log accordingly:

    ```text
    -- Collecting results of the conformance test suite...
    
    > Collecting basic configuration information...
    > Waiting for the conformance test suite to complete...
      ... still waiting (0d:00h:01m:00s)
      ... still waiting (0d:00h:01m:30s)
    ...
    ```

    Once completed, the pod will retrieve the detailed results from the CTS itself:

    ```text
    ...
       ... still waiting (0d:02h:13m:30s)

     > Retrieving detailed profile results...

       ... retrieving profile details for: Metadata sharing
       ... retrieving profile details for: Reference copies
       ... retrieving profile details for: Metadata maintenance
       ... retrieving profile details for: Dynamic types
       ... retrieving profile details for: Graph queries
       ... retrieving profile details for: Historical search
       ... retrieving profile details for: Entity proxies
       ... retrieving profile details for: Soft-delete and restore
       ... retrieving profile details for: Undo an update
       ... retrieving profile details for: Reidentify instance
       ... retrieving profile details for: Retype instance
       ... retrieving profile details for: Rehome instance
       ... retrieving profile details for: Entity search
       ... retrieving profile details for: Relationship search
       ... retrieving profile details for: Entity advanced search
       ... retrieving profile details for: Relationship advanced search
       
       > Retrieving detailed test case results...
       
       ... retrieving test case details for: repository-attribute-typedef-ActivityType
    ...
    ```

    Once all the results are collected, the pod will then bundle these all up into an archive and then print out the location of that archive within the pod:

    ```text
    ...
       ... retrieving test case details for: repository-typedef-ZoneHierarchy-null

     > Bundling all results into an archive...

    -- End of conformance test suite results collection, download from: /tmp/t12.tar.gz
    ```

!!! attention "The pod will continue running after the CTS has completed"
    Note that the pod itself will continue running after the CTS has completed: this is to provide adequate time to copy the bundled archive file of the results out of the pod. (If the pod were allowed to stop its execution any files within it would be lost.)

## Retrieving results

Once the CTS has completed running and the bundled archive file is available, it can be copied from the pod:

!!! cli "Copy results archive from the pod"
    ```shell
    kubectl cp <podname>:/tmp/<name>.tar.gz <filename>
    ```

    Where the `<podname>` is the name of the pod as discovered above (e.g. `t12-init-and-report-585b47f74-85r8m`) and the `<name>` is the name of the Helm deployment. (Alternatively, you could just copy the location from the log output as shown above in the monitoring section.)

    `<filename>` is the location on your local filesystem to which you want to copy the archive.

## Uninstallation

Once you have retrieved the results, or if you want to otherwise cancel or stop the running of the CTS:

!!! cli "Delete the deployment"
    ```shell
    helm delete <name>
    ```

    Where `<name>` is the name of your deployment. (If you are unsure what name you used, `helm list` lists all the deployments.)

---8<-- "snippets/abbr.md"
