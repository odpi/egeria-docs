```mermaid
---
title: SolutionComponent - Content Packs Monitor [c67172bb-bd66-4d22-9ed7-ee6dc9c99b38]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Content Packs Monitor**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: stadium, label: "*Integration Connector*
**ContentPacksMonitorIntegrationConnector**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
```
> Content Packs Monitor: Catalogs open metadata archive files located in the ''content-packs'' directory.  This includes cataloguing the header information from the archive file.  This includes a description of its content.  The resulting open metadata elements are used to list the content packs that are available to load into the Open Metadata Ecosystem. (Extracted from 6.0-SNAPSHOT)
