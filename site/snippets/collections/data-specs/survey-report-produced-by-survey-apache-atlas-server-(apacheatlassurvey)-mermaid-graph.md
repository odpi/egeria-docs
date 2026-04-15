```mermaid
---
title: ReportType - Survey report produced by survey-apache-atlas-server (ApacheAtlasSurvey) [05529034-8b64-4a11-adcd-4143f2ea534b]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Report Type*
**Survey report produced by survey-apache-atlas-server (ApacheAtlasSurvey)**"}
2@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas End 2 Attached Relationship Types**"}
1==>|"Collection Membership"|2
3@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas Attached End 1 Entity Types**"}
1==>|"Collection Membership"|3
4@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas Attached Entity Type Pairs**"}
1==>|"Collection Membership"|4
5@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas Attached Classification Types**"}
1==>|"Collection Membership"|5
6@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas Attached Entity Types By Business Metadata**"}
1==>|"Collection Membership"|6
7@{ shape: hex, label: "*Valid Metadata Value*
**Apache Atlas Attached Entity Types By Classification**"}
1==>|"Collection Membership"|7
8@{ shape: stadium, label: "*Collection Membership*
**... plus 6 Items**"}
1-.->8
9@{ shape: rect, label: "*Solution Component*
**Survey an Apache Atlas Server**"}
9==>|"creates report [Solution Linking Wire]"|1
10@{ shape: tag-rect, label: "*Governance Action Type*
**survey-apache-atlas-server (ApacheAtlasSurvey)**"}
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
> Survey report produced by survey-apache-atlas-server (ApacheAtlasSurvey): Discovers the types and number of instances within an Apache Atlas server. (Extracted from 6.0-SNAPSHOT)
