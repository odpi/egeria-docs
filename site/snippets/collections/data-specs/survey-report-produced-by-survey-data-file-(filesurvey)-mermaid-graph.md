```mermaid
---
title: ReportType - Survey report produced by survey-data-file (FileSurvey) [4dc563af-8917-473f-9801-d1d0c265e317]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Report Type*
**Survey report produced by survey-data-file (FileSurvey)**"}
2@{ shape: hex, label: "*Valid Metadata Value*
**Extract File Properties**"}
1==>|"Collection Membership"|2
3@{ shape: rect, label: "*Solution Component*
**Survey Data File**"}
3==>|"creates report [Solution Linking Wire]"|1
4@{ shape: tag-rect, label: "*Governance Action Type*
**survey-data-file (FileSurvey)**"}
1==>|"Implemented By"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#40E0D0, stroke:#000000
click 3 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Survey report produced by survey-data-file (FileSurvey): Connector supports the extractions of basic file properties. (Extracted from 6.0-SNAPSHOT)
