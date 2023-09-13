<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# JanusGraph Repository

!!! info "Connector summary"

    - Connector Category: [Native Repository Connector](/concepts/repository-connector)
    - Hosting Service: [Open Metadata Repository Services (OMRS)](/services/omrs)
    - Hosting Server: [Metadata Access Store](/concepts/metdata-access-store)
    - Source Module: [graph-repository-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/graph-repository-connector){ target=gh }
    - Jar File Name: `graph-repository-connector.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector/GraphOMRSRepositoryConnectorProvider.java`

Egeria's Local Graph Repository provides a local repository for a [Metadata Access Store](/concepts/metadata-access-store) that uses [JanusGraph](https://janusgraph.org/).

JanusGraph provides a graph library.  It uses two pluggable persistence stores: one for the graph and one for a search index that is used to find instances in the graph with specific values.

When the JanusGraph connector is started, it builds an index for each primitive property in the type system as well as the standard header properties - such as guid, createTime , ... JanusGraph then maps this call down onto whatever search index technology is configured.  At the same time, it is building up the graph representation as entities and relationships are stored.

## Egeria Jar files

Egeria's build produces 2 jar files for this connector:

* `graph-repository-connector-4.2-SNAPSHOT.jar` containing just the classes for the repository connector.  To use this version of the connector, you will need to include the JanusGraph libraries as well as the libraries for the chosen persistence stores in the class path of the [OMAG Server Platform](/concepts/omag-server-platform)(s) where the connector's server(s) are running.
* `graph-repository-connector-jar-with-dependencies-4.2-SNAPSHOT.jar` containing the classes for the repository connector and the version of JanusGraph that Egeria is using.  This version number is defined in the `janusVersion` of the `bom/build.gradle` file.  To use this version of the connector, you will need to include the libraries for the chosen persistence stores in the class path of the [OMAG Server Platform](/concepts/omag-server-platform)(s) where the connector's server(s) are running.

## Configuration

To configure a Metadata Access Store to use the Graph Repository, set the repository-mode to 'local-graph-repository'. For example:

```
POST {platformURLRoot}/open-metadata/admin-services/users/{userName}/servers/{serverName}/local-repository/mode/local-graph-repository
```

Replace the *{serverURLRoot}*, *{userName}* and *{serverName}* with the values appropriate for the server you are configuring.

The request body is optional and set to a map of property names to property values that specify the storage properties that JanusGraph is to use.  If the storage properties are null, the following properties are used:

| Property name          | Property value                                           |
|------------------------|----------------------------------------------------------|
| storage.backend        | berkeleyje                                               |
| storage.directory      | ./data/servers/{serverName}/repository/graph/berkeley    |
| index.search.backend   | lucene                                                   |
| index.search.directory | ./data/servers/{serverName}/repository/graph/searchindex |

This stores the graph store in the OMAG Server Platform's working directory in file called `./data/servers/{serverName}/repository/graph/berkeley` where the server name is inserted into *{serverName}*.  The search index is stored in [Apache Lucene](https://lucene.apache.org/).

Details of other supported storage backends and how to specify them are found in the [JanusGraph documentation](https://docs.janusgraph.org/storage-backend/). 

# Deployment Notes


Here are some usage notes based on experience configuring and testing JanusGraph using different underlying technologies.

## Configurations

As discussed above, there are two steps to establishing a working JanusGraph based Egeria repository. We need to send a JSON snippet to JanusGraph detailing how to communicate with the underlying technologies and we need to ensure the right Jar files are on the Java path.

In the examples below we show the use of a separate search index - which although not strictly necessary for JanusGraph, does offer improved performance and support for many queries.


### Berkeley DB and Lucene

As mentioned above, the default configuration for JanusGraph is to use BerkeleyDB and Lucene. This will persist the graph and search index files. Note that this simple configuration provides little resilience beyond what your file system provides.

If you want to change the file locations rather than use the defaults, then you need to pass in a JSON configuration in the body of the REST call. Here is an example:

```json
{
	"storage.backend" 				: "berkeleyje",
	"storage.directory"				: "your data directory",

	"index.search.backend"		: "lucene",
	"index.search.directory" 	: "your search directory" 

}
```

No additional jar files are required for this default configuration.

### HBase and ElasticSearch

Using HBase offers massive scalability and an opportunity to provide storage resilience - but is, however, more effort to configure - particularly if you are unfamiliar with Hadoop technology. If you already have a mature hadoop deployment then this can be a cost-effective option. A couple of additional considerations for HBase:

- JanusGraph writes its configuration into the first row of the HBase table. So if you want to change configurations by, for example, changing a search engine parameter, then you must delete the row (or the table) in order for your change to be effective. This also means it can be expensive to change configurations once the system is in productive use.
- Some deployments of HBase can be finicky in the hostnames they accept - sometimes numerical IP addresses, sometimes symbolic IP addressed work - and you might need mappings between them in a local /etc/hosts file.
- If "storage.hbase.skip-schema-check" is true then JanusGraph assumes the HBase table already exists; if false, it will create the table automatically if it doesn't exist.
- Additional configuration options can be found at: [JanusGraph - HBase](https://docs.janusgraph.org/storage-backend/hbase/)


We also show the use of ElasticSearch which provides a resilient search cluster. ElasticSearch has an extensive set of options that can be configured - especially around security and authentication. Shown below are some basic settings, more robust and sophisticated approaches are available. Here are a couple additional considerations:

- Many ElasticSearch deployments automatically set up  self-signed certificates for SSL. You may need to include this certificate to successfully connect to ElasticSearch. Each node in the ElasticSearch cluster may have its own certificate. There are a couple of different ways the certificates can be injected - one approach is to add it to the Trust Store defined by the Egeria Platform  [Application Properties File](https://egeria-project.org/guides/admin/configuring-the-omag-server-platform/#certificates-for-the-omag-server-platform) using utilities like *openssl* and *keytool*.
- Most modern ElasticSearch deployments use the REST interface.
- Additional configuration options can be found at: [JanusGraph - ElasticSearch](https://docs.janusgraph.org/index-backend/elasticsearch/)


HBase and ElasticSearch are both commonly deployed as shared services that may be used by many applications - so we must be careful to specify unique table/index names.


In the snippet below we also show the use of a local cache to improve performance as we are using remote persistence:

```json
{ 

	"storage.backend": "hbase",  
	"storage.hostname": "set of hbase zookeeper endpoints",  
	"storage.port": "2181",  
	"storage.hbase.skip-schema-check" : "false",
	"storage.hbase.table": "table name for my server",
	"index.search.backend" : "elasticsearch",  
	"index.search.hostname" : "set of ElasticSearch endpoints",  
	"index.search.elasticsearch.connect-timeout": "2000", 
	"index.search.elasticsearch.ssl.allow-self-signed-certificates": "true",  
	"index.search.elasticsearch.ssl.enabled": "true",  
	"index.search.elasticsearch.http.auth.type" : "basic",  
	"index.search.elasticsearch.http.auth.basic.username" : "myUser",  
	"index.search.elasticsearch.http.auth.basic.password" : "your password",  
	"index.search.elasticsearch.interface": "REST_CLIENT",  
	"index.search.index-name" : "index name for my server",  

	"cache.db-cache": "true",  
	"cache.db-cache-clean-wait": "20",  
	"cache.db-cache-time": "180000",  
	"cache.db-cache-size": "0.5"  
} 
``` 

#### Adding needed Jar files

The second part of configuring the JanusGraph repository connector is making sure that the necessary Jar files are on the java class path.

* First we need to decide how we want to make the needed Jar files available on the class path. This will depend on our Egeria deployment approach.
* Second, we need to identify which files are needed - and this can sometimes be a matter of trial and error.
* Finally, we will often want to automate the acquisition and placement of the right Jar files into the right places before starting the Egeria platform so that they will be available to the connector at runtime.

##### Adding Jar files to the class path

Injecting needed Jar files onto the class path depends on how you are deploying Egeria.

* Running as a standard Java application then you can easily download the Jar files and add them to the platform/lib directory under the Egeria OMAG Server working directory.
* If you are deploying with Helm charts in a Kubernetes environment then you may want to create a custom yaml file to download the Jar files during the installation process.
* If your are deploying via a Docker container then you would likely download the files when you build the container.

To download the files (once they have been identified), you can create a script of curl commands. For example, a command to download the hadoop-hdfs-client-3.3.0 jar file from the *maven* repository would look like:

```bash
curl -o ./hadoop-hdfs-client-3.3.0.jar https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-hdfs-client/3.3.0/hadoop-hdfs-client-3.3.0.jar
```

The curl command also specifies where you want to download the file to - so be careful where you run the command and how you formulate the download location. The curl command can also be issued within the docker build file. For kubernetes deployments with Helm charts, a yaml file can contain a similar set of commands of the form:

```text
   - url: https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-hdfs-client/3.3.0/hadoop-hdfs-client-3.3.0.jar
     filename: hadoop-hdfs-client-3.3.0.jar`
```

If you create a yaml file called myAddedJars.yaml containing these directives, then it can be executed as part of install command. Here is a simplified example that adds this directive to the command that installs the Egeria Lab helm chart:

```bash
helm install -f ./myAddedJars.yaml lab egeria/odpi-egeria-lab`
```

A more complete discussion can be found at [Egeria Helm Lab Chart](https://egeria-project.org/guides/operations/kubernetes/charts/lab/?h=helm+lab#adding-additional-connectors)

##### Locate the Jar files

Discovering the right set of Jar files to support a particular connector can require a bit of trial and error. You add the Jar files you think you need, start up Egeria, configure the connector and then start it - and see if it works by observing the audit log (often the console log).  You may see exceptions due to missing classes - which means you then need to find what Jar files contain the missing classes, download the Jar files,  and add them to the class path.

For example, to configure a JanusGraph repository with HBase and ElasticSearch, the following jar files were added to the class path:


``` text
woodstox-core-6.2.0.jar
x-pack-transport-7.15.0.jar
zookeeper-3.5.7.jar
zookeeper-jute-3.5.7.jar
stax2-api-4.2.2.jar
tinkergraph-gremlin-3.4.6.jar
transport-nio-client-7.15.0.jar
lucene-suggest-8.6.2.jar
solr-solrj-7.7.2.jar
lucene-analyzers-common-8.6.2.jar
lucene-core-8.6.2.jar
htrace-hbase-4.2.0-incubating.jar
hadoop-shaded-protobuf_3_7-1.1.0.jar
hbase-client-2.3.3.jar
hbase-hadoop2-compat-2.3.3.jar
hbase-hadoop-compat-2.3.3.jar
hadoop-common-3.3.0.jar
gremlin-shaded-3.4.6.jar
hadoop-annotations-3.3.0.jar
hadoop-auth-3.3.0.jar
hadoop-aws-3.3.0.jar
gremlin-core-3.4.6.jar
gremlin-driver-3.4.6.jar
```

This list doesn't include JanusGraph ElasticSearch and HBase libraries because these have already been added into the Jar file named **graph-repository-connector-jar-with-dependencies-4.2-SNAPSHOT.jar **  during the Egeria build process - we do need to make sure this key file is on the class path (by default it should be automatically installed during the build process into the *platform/lib* directory).  Also note that this list may include more Jar files than strictly needed - it is easier to add more and prune later if desired.

Finding the Jar files needed can be tedious - often consulting sites like [sonatype](https://oss.sonatype.org/#welcome) is useful.




### Other Configurations

JanusGraph supports many other storage and search index technologies including:
- Apache Cassandra
- Google Cloud Bigtable
- ScyllaDB
- Apache Solr

Please see the JanusGraph documentation for more details.


## Troubleshooting

When you are setting up the JanusGraph repository connector, there are two challenges:

* Getting the storage properties passed in the configuration call's request body to contain the correct properties to connect to the storage backends with the correct behaviour.
* Ensuring the JanusGraph and persistence store libraries included in the OMAG Server Platform's classpath are sufficient and are of compatible versions.

If there are missing JanusGraph libraries, you may see this type of error since the connector provider `org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider` is unable to load the connector.

```
Fri Jun 02 18:16:31 BST 2023 cocoMDS1 Startup OMRS-AUDIT-0044 The connector for the local repository is being started in mode Open Metadata Native using connector provider org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider and configuration properties null
2023-06-02T18:16:31.900+01:00  INFO 31359 --- [nio-9444-exec-2] o.o.o.f.a.cocoMDS1.OperationalServices   : cocoMDS18ee5673f-7b82-4a50-a19a-e8616270a6e7 OMRS-AUDIT-0044 The connector for the local repository is being started in mode Open Metadata Native using connector provider org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider and configuration properties null
2023-06-02T18:16:31.900+01:00  INFO 31359 --- [nio-9444-exec-2] o.o.o.f.a.cocoMDS1.OperationalServices   : cocoMDS18ee5673f-7b82-4a50-a19a-e8616270a6e7 OMRS-AUDIT-0044 The connector for the local repository is being started in mode Open Metadata Native using connector provider org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider and configuration properties null
Fri Jun 02 18:59:51 BST 2023 cocoMDS1 Exception OMRS-AUDIT-0034 The connector to the local repository failed with a org.odpi.openmetadata.frameworks.connectors.ffdc.ConnectionCheckedException exception and the following error message: OCF-CONNECTION-400-005 Unknown Connector Provider class org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider passed in connection <Unknown>
Fri Jun 02 18:59:51 BST 2023 cocoMDS1 Exception OMRS-AUDIT-0034 Supplementary information: log record id f7359934-859b-4695-9c5e-5da74d1c8331 org.odpi.openmetadata.frameworks.connectors.ffdc.ConnectionCheckedException returned message of OCF-CONNECTION-400-005 Unknown Connector Provider class org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider passed in connection <Unknown> and stacktrace of
OCFCheckedExceptionBase{reportedHTTPCode=400, reportingClassName='org.odpi.openmetadata.frameworks.connectors.ConnectorBroker', reportingActionDescription='validateConnection', reportedErrorMessage='OCF-CONNECTION-400-005 Unknown Connector Provider class org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider passed in connection <Unknown>', reportedErrorMessageId='OCF-CONNECTION-400-005', reportedErrorMessageParameters=[org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider, <Unknown>], reportedSystemAction='The system is unable to create the requested connector instance because the Connector Provider's class is not known to the JVM.  This may be because the Connector Provider's jar is not installed in the local JVM or the wrong Java class name has been configured in the connection.', reportedUserAction='Verify that the Connector Provider and Connector jar files are properly configured in the process.  Update the connection configuration to include a valid Java class name for the connector provider in the connectorProviderClassName property of the connection's connectorType. Then retry the request.', reportedCaughtException=java.lang.ClassNotFoundException: org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider, reportedCaughtExceptionClassName='java.lang.ClassNotFoundException', relatedProperties=null}
at org.odpi.openmetadata.frameworks.connectors.ConnectorBroker.getConnectorProvider(ConnectorBroker.java:172)
at org.odpi.openmetadata.frameworks.connectors.ConnectorBroker.validateConnection(ConnectorBroker.java:289)
at org.odpi.openmetadata.frameworks.connectors.ConnectorBroker.getConnector(ConnectorBroker.java:336)
at org.odpi.openmetadata.repositoryservices.localrepository.repositoryconnector.LocalOMRSConnectorProvider.getConnector(LocalOMRSConnectorProvider.java:205)
at org.odpi.openmetadata.repositoryservices.localrepository.repositoryconnector.LocalOMRSConnectorProvider.getConnector(LocalOMRSConnectorProvider.java:136)
at org.odpi.openmetadata.repositoryservices.admin.OMRSOperationalServices.getLocalOMRSConnector(OMRSOperationalServices.java:1235)
at org.odpi.openmetadata.repositoryservices.admin.OMRSOperationalServices.initializeLocalRepository(OMRSOperationalServices.java:812)
at org.odpi.openmetadata.repositoryservices.admin.OMRSOperationalServices.initializeCohortMember(OMRSOperationalServices.java:421)
at org.odpi.openmetadata.adminservices.server.OMAGServerOperationalServices.activateWithSuppliedConfig(OMAGServerOperationalServices.java:324)
at org.odpi.openmetadata.adminservices.server.OMAGServerOperationalServices.activateWithStoredConfig(OMAGServerOperationalServices.java:154)
at org.odpi.openmetadata.adminservices.spring.OperationalServicesResource.activateWithStoredConfig(OperationalServicesResource.java:60)
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.base/java.lang.reflect.Method.invoke(Method.java:568)
at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:207)
at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:152)
at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)
at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:884)
at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:797)
at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1081)
at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:974)
at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1011)
at org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:914)
at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:590)
at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:885)
at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:658)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:205)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:51)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.odpi.openmetadata.http.HttpRequestHeadersFilter.doFilter(HttpRequestHeadersFilter.java:62)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:100)
at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.springframework.web.filter.FormContentFilter.doFilterInternal(FormContentFilter.java:93)
at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.springframework.web.filter.ServerHttpObservationFilter.doFilterInternal(ServerHttpObservationFilter.java:109)
at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:201)
at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:174)
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:149)
at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:166)
at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:90)
at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:482)
at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:115)
at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:93)
at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:74)
at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:341)
at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:390)
at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:63)
at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:894)
at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1741)
at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:52)
at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
at java.base/java.lang.Thread.run(Thread.java:833)
Caused by: java.lang.ClassNotFoundException: org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector.GraphOMRSRepositoryConnectorProvider
at java.base/java.net.URLClassLoader.findClass(URLClassLoader.java:445)
at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:587)
at org.springframework.boot.loader.LaunchedURLClassLoader.loadClass(LaunchedURLClassLoader.java:151)
at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:520)
at java.base/java.lang.Class.forName0(Native Method)
at java.base/java.lang.Class.forName(Class.java:375)
at org.odpi.openmetadata.frameworks.connectors.ConnectorBroker.getConnectorProvider(ConnectorBroker.java:160)
... 67 more
```

If you see tis type of error, or subsequent connection or security errors when JanusGraph is connecting to its persistence stores, [turn on debug logging](/)

--8<-- "snippets/abbr.md"

