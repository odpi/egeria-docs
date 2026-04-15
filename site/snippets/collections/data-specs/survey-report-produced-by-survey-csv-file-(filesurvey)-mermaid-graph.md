```mermaid
---
title: ReportType - Survey report produced by survey-csv-file (FileSurvey) [02973657-b01d-4412-9d94-1c53eb4065a8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Report Type*
**Survey report produced by survey-csv-file (FileSurvey)**"}
2@{ shape: hex, label: "*Valid Metadata Value*
**Derive Schema From Data**"}
1==>|"Collection Membership"|2
3@{ shape: hex, label: "*Valid Metadata Value*
**Extract File Properties**"}
1==>|"Collection Membership"|3
4@{ shape: rect, label: "*Solution Component*
**Survey CSV File**"}
4==>|"creates report [Solution Linking Wire]"|1
5@{ shape: tag-rect, label: "*Governance Action Type*
**survey-csv-file (FileSurvey)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 3 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#40E0D0, stroke:#000000
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Survey report produced by survey-csv-file (FileSurvey): Connector supports the schema extraction and profiling of data in a CSV file. (Extracted from 6.0-SNAPSHOT)
