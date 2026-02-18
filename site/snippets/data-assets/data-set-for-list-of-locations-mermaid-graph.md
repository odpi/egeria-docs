```mermaid
---
title: ReferenceCodeTable - Data set for List of Locations [529beeb7-5996-4cbe-9bb2-dac646237e20]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Reference Code Table*
**Data set for List of Locations**"}
2@{ shape: delay, label: "*Search Keyword*
**130be5ea-7968-438e-99d5-e788bbdb4925**"}
1==>|"Search Keyword Link"|2
3@{ shape: rect, label: "*Digital Product*
**List of Locations**"}
3==>|"product data set [Collection Membership]"|1
4@{ shape: doc, label: "*Notification Type*
**Notification type for Ongoing update subscription for product Location List**"}
4==>|"product asset [Monitored Resource]"|1
5@{ shape: processes, label: "*Governance Action Process*
**Create Daily refresh subscription for Location List**"}
5==>|"sourceDataSet [Target For Governance Action]"|1
6@{ shape: processes, label: "*Governance Action Process*
**Create Ongoing update subscription for Location List**"}
6==>|"sourceDataSet [Target For Governance Action]"|1
7@{ shape: processes, label: "*Governance Action Process*
**Create Weekly refresh subscription for Location List**"}
7==>|"sourceDataSet [Target For Governance Action]"|1
8@{ shape: processes, label: "*Governance Action Process*
**Create Evaluation subscription for Location List**"}
8==>|"sourceDataSet [Target For Governance Action]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#9acd32, fill:#8b008b, stroke:#004563
style 3 color:#000000, fill:#838cc7, stroke:#3079ab
style 4 color:#FFFFFF, fill:#006400, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
style 7 color:#000000, fill:#53bbb4, stroke:#000000
style 8 color:#000000, fill:#53bbb4, stroke:#000000
```
> Data set for List of Locations: This asset represents the source of data for the digital product. (Extracted from 6.0-SNAPSHOT)
