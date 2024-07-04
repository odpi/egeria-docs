<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

```bash
/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin/java -Dstrict.ssl=false -Dfile.encoding=UTF-8 -jar /egeria-install/egeria-platform-5.0-distribution.tar.gz/assembly/etc/utilities/egeria-config-utility-5.0.jar
==================================
OMAG Server Configuration Utility:    Wed Sep 13 12:48:44 BST 2023
==================================
Running against platform: https://localhost:9443 - Egeria OMAG Server Platform (version 5.0)
Using userId: garygeeke

Enter a command along with the server name and any optional parameters. Press enter to execute request.
  - create-metadata-store     <serverName>  
  - create-integration-daemon <serverName>  
  - add-api-connector         <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - add-infra-connector       <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - add-topic-connector       <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - log-event-contents        <serverName> <optionalConnectorProviderClassName> 
  - add-cohort-member         <serverName> <optionalCohortName> 
  - add-startup-archive       <serverName> <archiveFileName> 
  - update-server-user-id     <serverName> <newUserId> 
  - delete-server             <serverName>  
  - exit  
```
```bash
create-metadata-store test-metadata-store
```
```bash
Configuring metadata store: test-metadata-store

Enter a command along with the server name and any optional parameters. Press enter to execute request.
  - create-metadata-store     <serverName>  
  - create-integration-daemon <serverName>  
  - add-api-connector         <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - add-infra-connector       <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - add-topic-connector       <serverName> <metadataStoreServerName> <optionalConnectorProviderClassName> <optionalNetworkAddress>
  - log-event-contents        <serverName> <optionalConnectorProviderClassName> 
  - add-cohort-member         <serverName> <optionalCohortName> 
  - add-startup-archive       <serverName> <archiveFileName> 
  - update-server-user-id     <serverName> <newUserId> 
  - delete-server             <serverName>  
  - exit  
```


