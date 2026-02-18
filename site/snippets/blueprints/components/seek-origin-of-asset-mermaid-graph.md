```mermaid
---
title: SolutionComponent - Seek Origin of Data [0e982f14-b5f9-4c0d-9bdf-647a2a637efa]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Seek Origin of Data**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Core Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: tag-rect, label: "*Governance Action Type*
**seek-origin-of-asset (AssetOnboarding)**"}
1==>|"Implemented By"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Seek Origin of Data: Using the lineage relationships, trace back to the source of data for a requested asset.  If a single DigitalResourceOrigin classification is encountered then add it to the asset.  If null, or multiple DigitalResourceOrigin classifications are encountered, raise an error. (Extracted from 6.0-SNAPSHOT)
