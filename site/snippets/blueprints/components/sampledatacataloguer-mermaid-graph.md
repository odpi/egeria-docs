```mermaid
---
title: SolutionComponent - Sample Data Files Monitor [acebfa6f-f3a6-4fe3-a467-963a4e5bf0d6]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Sample Data Files Monitor**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"Catalog Resource [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|4
5@{ shape: stadium, label: "*Integration Connector*
**SampleDataFilesMonitorIntegrationConnector**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Sample Data Files Monitor: Catalogs any files added to the ''loading-bay/sample-data'' directory.  This is used to demonstrate how different types of files are catalog in open metadata.  Just drop the files that you want to experiment with into the directory anf they will be catalogued.  Use the Asset Maker API to query the results. (Extracted from 6.0-SNAPSHOT)
