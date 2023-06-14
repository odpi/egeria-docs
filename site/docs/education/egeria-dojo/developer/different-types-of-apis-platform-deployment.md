<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


In `egeria-dev-projects`, there is a module called `egeria-platform-report`.  This contains a utility that reports on the status of a running OMAG Server Platform.  Navigate down the contents of `egeria-platform-report` until you come across a java class called `EgeriaPlatformReport`.

![egeria-platform-report](/education/egeria-dojo/developer/egeria-platform-report-module.png)

??? beginner "Run `EgeriaPlatformReport`"
    Select `EgeriaPlatformReport` and then `Run 'EgeriaPlatformReport...main()'` from the right-mouse menu.

    A new *Run* tab appears next to `EgeriaPlatform`.  `EgeriaPlatformReport` runs but fails:

    ```bash
    /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java ... org.odpi.openmetadata.devprojects.reports.platform.EgeriaPlatformReport
    ===============================
    OMAG Server Platform Report:    Sun Feb 13 22:13:33 GMT 2022
    ===============================
    Running against platform: https://localhost:9443
    Using userId: garygeeke
    
    Platform report for: https://localhost:9443
       Platform deployment
    There was an org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException exception when calling the platform.  Error message is: OMAG-COMMON-503-001 A client-side exception was received from API call getPlatformOrigin to OMAG Server EgeriaPlatform at https://localhost:9443.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.ResourceAccessException was received by method getPlatformOrigin from API call https://localhost:9443/open-metadata/platform-services/users/{1}/server-platform/origin to server EgeriaPlatform on platform https://localhost:9443.  The error message was I/O error on GET request for "https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform/origin": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested exception is javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
    
    Process finished with exit code 255
    
    ```
    This is because it does not have a valid security certification.  You will notice that IntelliJ has added a new configuration for `EgeriaPlatformReport'

??? beginner "Set up VM Options"
    
    ![egeria-platform-report configuration](/education/egeria-dojo/developer/egeria-platform-report-configuration.png)

    Click on the white down arrow of the configurations box and select `Edit Configurations...`.  Select the configuration for `EgeriaPlatformReport` to show its configuration form.
    
    Add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration.  This turns off the need for a certificate. 
    
    ??? tip "Don't see VM Options in the configuration form?"
        You may need to use the `Modify Options` dropdown to `Add VM Options` to your configuration form.
        ![Add VM Options](/education/egeria-dojo/developer/intellij-vm-options.png)
    
    ![egeria-platform-report configuration fixed](/education/egeria-dojo/developer/egeria-platform-report-configuration-fixed.png)

??? beginner "Rerun `EgeriaPlatformReport`"

    Re-run `EgeriaPlatformReport` by clicking on the green arrow on the *Run* tab.  There is more output this time even though it still seems to fail in the end. It begins with the report header that records the platform it is running against.
    
    ```bash
    ===============================
    OMAG Server Platform Report:    Mon Feb 14 07:57:05 GMT 2022
    ===============================
    Running against platform: https://localhost:9443
    Using userId: garygeeke
    
    Platform report for: https://localhost:9443
    ```
    
    Then `EgeriaPlatfromReport` starts to call the Egeria APIs that are used for configuring and managing the OMAG Server Platform.
    
    ```bash
       Platform deployment
          Egeria version: Egeria OMAG Server Platform (version 3.12)
          Configuration document store connector: <null>
          Platform security connector: <null>
    ```
    
    The `Egeria version` is retrieved using the `getPlatformOrigin` method of the [Platform Services](/services/platform-services/overview/).
    
    ```java linenums="1"
    PlatformServicesClient platformServicesClient = new PlatformServicesClient("MyPlatform", platformURLRoot);
         
    String platformOrigin = platformServicesClient.getPlatformOrigin(clientUserId);
    ```
    The connectors configured for the platform are retrieved using the [Administration Service's `OMAGServerPlatformConfigurationClient`](/services/admin-services/overview/#configuring-the-omag-server-platform){ target=dojo-support }
    
    ```java linenums="1"
    
    OMAGServerPlatformConfigurationClient platformConfigurationClient = new OMAGServerPlatformConfigurationClient(clientUserId, platformURLRoot);
    
    Connection configurationStoreConnection = platformConfigurationClient.getConfigurationStoreConnection();
    Connection platformSecurityConnection   = platformConfigurationClient.getPlatformSecurityConnection();
    ```
    
    Next is the list of *Registered services*.  These are optional services that can be plugged into the `OMAG Server Platform` and provide the services to retrieve and maintain/govern open metadata. The list that you see is the default set of services installed with the platform.  

    ??? beginner "List of registered services from `EgeriaPlatformReport`"
        
        ```bash      
           Registered services
              Data Manager OMAS: Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.
              Subject Area OMAS: Document knowledge about a subject area
              Design Model OMAS: Exchange design model content with tools and standard packages
              Glossary View OMAS: Support glossary terms visualization
              Asset Manager OMAS: Manage metadata from a third party asset manager
              Security Officer OMAS: Set up rules and security tags to protect data
              IT Infrastructure OMAS: Manage information about the deployed IT infrastructure
              Data Science OMAS: Create and manage data science definitions and models
              Community Profile OMAS: Define personal profile and collaborate
              Discovery Engine OMAS: Support for automated metadata discovery engines
              Data Engine OMAS: Exchange process models and lineage with a data engine
              Digital Architecture OMAS: Design of the digital services for an organization
              Asset Owner OMAS: Manage an asset
              Stewardship Action OMAS: Manage exceptions and actions from open governance
              Governance Program OMAS: Manage the governance program
              Digital Service OMAS: Manage a digital service through its lifecycle
              Asset Lineage OMAS: Store asset lineage
              Analytics Modeling OMAS: Provides metadata information for Analytics Modeling.
              Asset Consumer OMAS: Access assets through connectors
              Asset Catalog OMAS: Search and understand your assets
              DevOps OMAS: Manage a DevOps pipeline
              Software Developer OMAS: Interact with software development tools
              Project Management OMAS: Manage governance related projects
              Governance Engine OMAS: Set up an operational governance engine
              Data Privacy OMAS: Manage governance of privacy
              Security Manager OMAS: Manages exchange of metadata with a security service
              Repository Governance OMES: Maintains open metadata archives based on the activity in the connected cohorts.
              Governance Action OMES: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
              Asset Analysis OMES: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
              Files Integrator OMIS: Extract metadata about files stored in a file system or file manager.
              Topic Integrator OMIS: Exchange metadata with third party event-based brokers.
              API Integrator OMIS: Exchange metadata with third party API Gateways.
              Security Integrator OMIS: Distribute security properties to security enforcement points.
              Search Integrator OMIS: Store metadata with a third party technology that is focused on search efficiency.
              Database Integrator OMIS: Extract metadata such as schema, tables and columns from database managers.
              Lineage Integrator OMIS: Manage capture of lineage from a third party tool.
              Catalog Integrator OMIS: Exchange metadata with third party data catalogs.
              Analytics Integrator OMIS: Exchange metadata with third party analytics tools.
              Display Integrator OMIS: Exchange metadata with applications that display data to users.
              Organization Integrator OMIS: Load information about the teams and people in an organization and return collaboration activity.
              Glossary Author OMVS: View Service for glossary authoring.
              Dynamic Infrastructure and Operations OMVS: Explore and operate an open metadata ecosystem.
              Repository Explorer OMVS: Explore open metadata instances.
              Type Explorer OMVS: Explore the open metadata types in a repository or cohort.
              Server Author OMVS: Author servers.
        ```
    The registered are also retrieved through the [Platform Services](/services/platform-services/overview){ target=dojo-support } using the `getXXXServices` method as follows:
    
    ```java linenums="1"
    List<RegisteredOMAGService> registeredOMASs = platformServicesClient.getAccessServices(clientUserId);
    List<RegisteredOMAGService> registeredOMESs = platformServicesClient.getEngineServices(clientUserId);
    List<RegisteredOMAGService> registeredOMISs = platformServicesClient.getIntegrationServices(clientUserId);
    List<RegisteredOMAGService> registeredOMVSs = platformServicesClient.getViewServices(clientUserId);
    ```
??? beginner "Observe exception from `EgeriaPlatformReport`"
    
    Finally, `EgeriaPlatformReport` calls the [Administration Services](/services/admin-services/overview){ target=dojo-support } to request the list of configured servers.  At this stage, there are none.  In fact, the directory where they are kept has not even been created which is why an exception occurs.  It is printed out to show which directory (`data/servers`), relative to the working directory set up in the `EgeriaPlatform` configuration (`~/egeria-install/egeria-omag*`).
    ```bash      
       Platform servers
    There was an org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException exception when calling the platform.  Error message is: OMAG-ADMIN-500-002 Method retrieveAllServerConfigs returned an unexpected exception of org.odpi.openmetadata.frameworks.connectors.ffdc.OCFRuntimeException with message ENCRYPTED-DOC-STORE-400-014  Unable to retrieve the encrypted configuration files; exception was java.nio.file.NoSuchFileException with message data/servers, while attempting access file data/servers/null/config/null.config
    
    Process finished with exit code 255
    ```
    The next step will create a server configuration document that will also create the configuration directory and resolve this issue.  

    `EgeriaPlatformReport` also creates a [markdown](/guides/contributor/markdown) document called `egeria-platform-report.md` that contains its output.  This [version of egeria-platform-report.md](/education/egeria-dojo/developer/egeria-platform-report-no-servers) is included for your reference.        