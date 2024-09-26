<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The first time the platform report is run, you see an exception to say that the directory where the configuration is stored does not exist.  This directory is created when the first server is configured.

```bash
/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false "-javaagent:/Applications/IntelliJ IDEA.app/Contents/lib/idea_rt.jar=50666:/Applications/IntelliJ IDEA.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-dev-projects/egeria-dev-projects/egeria-platform-report/target/classes:/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-dev-projects/egeria-dev-projects/egeria-report-utilities/target/classes:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/ffdc-services/3.8-SNAPSHOT/ffdc-services-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/spring-rest-client-connector/3.8-SNAPSHOT/spring-rest-client-connector-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/springframework/spring-web/5.3.15/spring-web-5.3.15.jar:/Users/mandy-chessell/.m2/repository/org/springframework/spring-beans/5.3.15/spring-beans-5.3.15.jar:/Users/mandy-chessell/.m2/repository/org/codehaus/plexus/plexus-utils/3.4.1/plexus-utils-3.4.1.jar:/Users/mandy-chessell/.m2/repository/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar:/Users/mandy-chessell/.m2/repository/org/springframework/spring-core/5.3.15/spring-core-5.3.15.jar:/Users/mandy-chessell/.m2/repository/org/springframework/spring-jcl/5.3.15/spring-jcl-5.3.15.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/open-connector-framework/3.8-SNAPSHOT/open-connector-framework-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/slf4j/slf4j-api/1.7.35/slf4j-api-1.7.35.jar:/Users/mandy-chessell/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.13.1/jackson-databind-2.13.1.jar:/Users/mandy-chessell/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.13.1/jackson-core-2.13.1.jar:/Users/mandy-chessell/.m2/repository/com/fasterxml/jackson/core/jackson-annotations/2.13.1/jackson-annotations-2.13.1.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/audit-log-framework/3.8-SNAPSHOT/audit-log-framework-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/repository-services-apis/3.8-SNAPSHOT/repository-services-apis-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/repository-services-client/3.8-SNAPSHOT/repository-services-client-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/rest-client-factory/3.8-SNAPSHOT/rest-client-factory-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/rest-client-connectors-api/3.8-SNAPSHOT/rest-client-connectors-api-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/admin-services-api/3.8-SNAPSHOT/admin-services-api-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/admin-services-client/3.8-SNAPSHOT/admin-services-client-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/platform-services-api/3.8-SNAPSHOT/platform-services-api-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/platform-services-client/3.8-SNAPSHOT/platform-services-client-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/org/odpi/egeria/http-helper/3.8-SNAPSHOT/http-helper-3.8-SNAPSHOT.jar:/Users/mandy-chessell/.m2/repository/ch/qos/logback/logback-classic/1.2.10/logback-classic-1.2.10.jar:/Users/mandy-chessell/.m2/repository/ch/qos/logback/logback-core/1.2.10/logback-core-1.2.10.jar org.odpi.openmetadata.devprojects.reports.platform.EgeriaPlatformReport
===============================
OMAG Server Platform Report:    Wed Feb 09 11:36:27 GMT 2022
===============================
Running against platform: https://localhost:9443
Using userId: garygeeke

Platform report for: https://localhost:9443
   Platform deployment
      Egeria version: Egeria OMAG Server Platform (version 3.8-SNAPSHOT)
      Configuration document store connector: <null>
      Platform security connector: <null>
   Registered services
      Data Manager OMAS: Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.
      Design Model OMAS: Exchange design model content with tools and standard packages
      Asset Manager OMAS: Manage metadata from a third party asset manager
      IT Infrastructure OMAS: Manage information about the deployed IT infrastructure
      Data Science OMAS: Create and manage data science definitions and models
      Community Profile OMAS: Define personal profile and collaborate
      Digital Architecture OMAS: Design of the digital services for an organization
      Asset Owner OMAS: Manage an asset
      Stewardship Action OMAS: Manage exceptions and actions from open governance
      Governance Program OMAS: Manage the governance program
      Digital Service OMAS: Manage a digital service's lifecycle
      Asset Lineage OMAS: Store asset lineage
      Asset Consumer OMAS: Access assets through connectors
      DevOps OMAS: Manage a DevOps pipeline
      Software Developer OMAS: Interact with software development tools
      Project Management OMAS: Manage governance related projects
      Governance Server OMAS: Set up an operational governance engine
      Data Privacy OMAS: Manage governance of privacy
      Security Manager OMAS: Manages exchange of metadata with a security service
      Repository Governance OMES: Maintains open metadata archives based on the activity in the connected cohorts.
      Governance Action OMES: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
      Survey Action OMES: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
      Files Integrator OMIS: Extract metadata about files stored in a file system or file manager.
      Topic Integrator OMIS: Exchange metadata with third party event-based brokers.
      API Integrator OMIS: Exchange metadata with third party API Gateways.
      Security Integrator OMIS: Distribute security properties to security enforcement points.
      Database Integrator OMIS: Extract metadata such as schema, tables and columns from database managers.
      Lineage Integrator OMIS: Manage capture of lineage from a third party tool.
      Catalog Integrator OMIS: Exchange metadata with third party data catalogs.
      Analytics Integrator OMIS: Exchange metadata with third party analytics tools.
      Display Integrator OMIS: Exchange metadata with applications that display data to users.
      Organization Integrator OMIS: Load information about the teams and people in an organization and return collaboration activity.
      Glossary Manager OMVS: View Service for glossary authoring.
   Platform servers
There was an org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException exception when calling the platform.  Error message is: OMAG-ADMIN-500-002 Method retrieveAllServerConfigs returned an unexpected exception of org.odpi.openmetadata.frameworks.connectors.ffdc.OCFRuntimeException with message ENCRYPTED-DOC-STORE-400-014  Unable to retrieve the encrypted configuration files; exception was java.nio.file.NoSuchFileException with message data/servers, while attempting access file data/servers/null/config/null.config

Process finished with exit code 0

```