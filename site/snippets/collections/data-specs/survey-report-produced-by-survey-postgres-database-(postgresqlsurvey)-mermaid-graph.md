```mermaid
---
title: ReportType - Survey report produced by survey-postgres-database (PostgreSQLSurvey) [f6d04704-77c9-4e19-a56a-8d6bc6399fc8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Report Type*
**Survey report produced by survey-postgres-database (PostgreSQLSurvey)**"}
2@{ shape: hex, label: "*Valid Metadata Value*
**Capture List of Schemas**"}
1==>|"Collection Membership"|2
3@{ shape: hex, label: "*Valid Metadata Value*
**Capture Database Schema Measurements**"}
1==>|"Collection Membership"|3
4@{ shape: hex, label: "*Valid Metadata Value*
**Capture Database Column Measurements**"}
1==>|"Collection Membership"|4
5@{ shape: hex, label: "*Valid Metadata Value*
**Capture Database Table Sizes**"}
1==>|"Collection Membership"|5
6@{ shape: hex, label: "*Valid Metadata Value*
**Capture Table Sizes for a Database Schema**"}
1==>|"Collection Membership"|6
7@{ shape: hex, label: "*Valid Metadata Value*
**Capture Frequent Values for Column**"}
1==>|"Collection Membership"|7
8@{ shape: stadium, label: "*Collection Membership*
**... plus 4 Items**"}
1-.->8
9@{ shape: rect, label: "*Solution Component*
**Survey PostgreSQL Database**"}
9==>|"creates report [Solution Linking Wire]"|1
10@{ shape: tag-rect, label: "*Governance Action Type*
**survey-postgres-database (PostgreSQLSurvey)**"}
1==>|"Implemented By"|10
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 3 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 4 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 5 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 6 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 7 color:#FFFFFF, fill:#bf4086, stroke:#732650
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#40E0D0, stroke:#000000
click 9 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Survey report produced by survey-postgres-database (PostgreSQLSurvey): Surveys the tables and columns found in a PostgreSQL database server (Extracted from 6.0-SNAPSHOT)
