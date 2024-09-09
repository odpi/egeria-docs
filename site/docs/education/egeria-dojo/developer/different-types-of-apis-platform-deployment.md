<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


In the `omag-server-platform` assembly, there is a jar file called `egeria-platform-report.jar` under the `etc/reports` directory.  This contains a utility that reports on the status of a running OMAG Server Platform.

??? beginner "Run `EgeriaPlatformReport`"
    Select `EgeriaPlatformReport` and then `Run 'EgeriaPlatformReport...main()'` from the right-mouse menu.

    A new *Run* tab appears next to `EgeriaPlatform`.  `EgeriaPlatformReport` runs but fails:

    ```bash
    /Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin/java -Dfile.encoding=UTF-8 -jar /Users/mandy-chessell/egeria-install/egeria-platform-5.0-distribution.tar.gz/assembly/etc/reports/egeria-platform-report.jar
    ===============================
    OMAG Server Platform Report:    Mon Sep 04 18:00:51 BST 2023
    ===============================
    Running against platform: https://localhost:9443
    Using userId: garygeeke
    
    Platform report for: https://localhost:9443
    Platform deployment
    There was an org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException exception when calling the platform.  Error message is: OMAG-COMMON-503-001 A client-side exception was received from API call getPlatformOrigin to OMAG Server EgeriaPlatform at https://localhost:9443.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.ResourceAccessException was received by method getPlatformOrigin from API call https://localhost:9443/open-metadata/platform-services/users/{1}/server-platform/origin to server EgeriaPlatform on platform https://localhost:9443.  The error message was I/O error on GET request for "https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform/origin": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
    
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
    /Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin/java -Dstrict.ssl=false -Dfile.encoding=UTF-8 -jar /Users/mandy-chessell/egeria-install/egeria-platform-5.0-distribution.tar.gz/assembly/etc/reports/egeria-platform-report.jar
    ===============================
    OMAG Server Platform Report:    Mon Sep 04 19:38:03 BST 2023
    ===============================
    Running against platform: https://localhost:9443
    Using userId: garygeeke
    
    Platform report for: https://localhost:9443
    ```
    
    Then `EgeriaPlatfromReport` starts to call the Egeria APIs that are used for configuring and managing the OMAG Server Platform.
    
    ```bash
    Platform deployment
      Egeria version: Egeria OMAG Server Platform (version 5.0)
      Configuration document store connector: <null>
      Platform security connector: <null>
    ```
    
    The `Egeria version` is retrieved using the `getPlatformOrigin` method of the [Platform Services](/services/platform-services/overview/).
    
    ```java linenums="1"
    PlatformServicesClient platformServicesClient = new PlatformServicesClient("MyPlatform", platformURLRoot);
         
    String platformOrigin = platformServicesClient.getPlatformOrigin(clientUserId);
    ```
    The connectors configured for the platform are retrieved using the platform services client and [Administration Service's `OMAGServerPlatformConfigurationClient`](/services/admin-services/overview/#configuring-the-omag-server-platform){ target=dojo-support }
    
    ```java linenums="1"
    OMAGServerPlatformConfigurationClient platformConfigurationClient   = new OMAGServerPlatformConfigurationClient(clientUserId, platformURLRoot);
    
    Connection configurationStoreConnection = platformConfigurationClient.getConfigurationStoreConnection();
    Connection platformSecurityConnection   = platformServicesClient.getPlatformSecurityConnection();
    ```
    
    Next is the list of *Registered services*.  These are optional services that can be plugged into the `OMAG Server Platform` and provide the services to retrieve and maintain/govern open metadata. The list that you see is the default set of services installed with the platform.  

    ??? beginner "List of registered services from `EgeriaPlatformReport`"
        
        ```bash      
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
              Digital Service OMAS: Manage a digital service through its lifecycle
              Asset Lineage OMAS: Store asset lineage
              Asset Consumer OMAS: Access assets through connectors
              DevOps OMAS: Manage a DevOps pipeline
              Software Developer OMAS: Interact with software development tools
              Project Management OMAS: Manage governance related projects
              Governance Server OMAS: Set up an operational governance engine
              Data Privacy OMAS: Manage governance of privacy
              Security Manager OMAS: Manages exchange of metadata with a security service
              Governance Action OMES: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
              Repository Governance OMES: Dynamically governance open metadata repositories in the connected cohorts.
              Survey Action OMES: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
              Infrastructure Integrator OMIS: Exchange information relating to IT infrastructure such as hosts, platforms, servers, server capabilities and services.
              Files Integrator OMIS: Extract metadata about files stored in a file system or file manager.
              Topic Integrator OMIS: Exchange metadata with third party event-based brokers.
              Security Integrator OMIS: Distribute security properties to security enforcement points.
              API Integrator OMIS: Exchange metadata with third party API Gateways.
              Lineage Integrator OMIS: Manage capture of lineage from a third party tool.
              Database Integrator OMIS: Extract metadata such as schema, tables and columns from database managers.
              Catalog Integrator OMIS: Exchange metadata with third party data catalogs.
              Display Integrator OMIS: Exchange metadata with applications that display data to users.
              Analytics Integrator OMIS: Exchange metadata with third party analytics tools.
              Organization Integrator OMIS: Load information about the teams and people in an organization and return collaboration activity.
              Glossary Manager OMVS: Create glossary terms and organize them into categories as part of a controlled workflow process. It supports the editing glossary and multiple states.
              My Profile OMVS: Manage information about the logged on user as well as their preferences.
              Glossary Browser OMVS: View glossary terms and categories within a glossary.
        ```
    The registered are also retrieved through the [Platform Services](/services/platform-services/overview){ target=dojo-support } using the `getXXXServices` method as follows:
    
    ```java linenums="1"
    List<RegisteredOMAGService> registeredOMASs = platformServicesClient.getAccessServices(clientUserId);
    List<RegisteredOMAGService> registeredOMESs = platformServicesClient.getEngineServices(clientUserId);
    List<RegisteredOMAGService> registeredOMISs = platformServicesClient.getIntegrationServices(clientUserId);
    List<RegisteredOMAGService> registeredOMVSs = platformServicesClient.getViewServices(clientUserId);
    ```
??? beginner "Observe no servers from `EgeriaPlatformReport`"
    
    Finally, `EgeriaPlatformReport` calls the [Administration Services](/services/admin-services/overview){ target=dojo-support } to request the list of configured servers.  At this stage, there are none.
    ```bash      
       Platform servers
          None
    
    Process finished with exit code 0
    ```
    The next step will create a server configuration document that will also create the configuration directory and the report will start to show servers.  

    `EgeriaPlatformReport` also creates a [markdown](/guides/contributor/markdown) document called `egeria-platform-report.md` that contains its output.  This [version of egeria-platform-report.md](/education/egeria-dojo/developer/egeria-platform-report-no-servers) is included for your reference.        