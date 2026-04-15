```mermaid
---
title: ReferenceCodeTable - Data set for domainIdentifier Valid Values [98c663e2-a0b8-436d-abf1-49d71e78293e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Reference Code Table*
**Data set for domainIdentifier Valid Values**"}
2@{ shape: delay, label: "*Search Keyword*
**65760442-89b0-48b4-ba89-06a5e213a072**"}
1==>|"Search Keyword Link"|2
3@{ shape: subproc, label: "*Notification*
**Thu Feb 26 16:16:09 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0003 The monitored ReferenceCodeTable resource Data set for domainIdentifier Valid Values (98c663e2-a0b8-436d-abf1-49d71e78293e) has changed for subscription type: Notification type for Ongoing update subscription for product Valid Metadata Value Set: domainIdentifier (f0ac4f4c-1ec3-48e4-a203-64db336fe09c)**"}
3==>|"changedElement [Action Target]"|1
4@{ shape: subproc, label: "*Notification*
**Thu Feb 26 16:16:09 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0003 The monitored ReferenceCodeTable resource Data set for domainIdentifier Valid Values (98c663e2-a0b8-436d-abf1-49d71e78293e) has changed for subscription type: Notification type for Ongoing update subscription for product Valid Metadata Value Set: domainIdentifier (f0ac4f4c-1ec3-48e4-a203-64db336fe09c)**"}
4==>|"changedElement [Action Target]"|1
5@{ shape: rect, label: "*Digital Product*
**domainIdentifier Valid Values**"}
5==>|"product data set [Collection Membership]"|1
6@{ shape: rounded, label: "*Virtual Connection*
**Asset Connection for domainIdentifier Valid Values**"}
1==>|"Asset Connection"|6
7@{ shape: rounded, label: "*Connection*
**JacquardHarvesterIntegrationConnector secrets store connection**"}
6==>|"restAPIBearerToken [Embedded Connection]"|7
8@{ shape: rounded, label: "*Connector Type*
**YAML File Secrets Store Connector**"}
7==>|"Connection Connector Type"|8
9@{ shape: rounded, label: "*Endpoint*
**JacquardHarvesterIntegrationConnector secret store endpoint**"}
7==>|"Connect To Endpoint"|9
10@{ shape: rounded, label: "*Connector Type*
**Valid Metadata Values Tabular Data Set Connector**"}
6==>|"Connection Connector Type"|10
11@{ shape: rounded, label: "*Endpoint*
**Reference data set for domainIdentifier Valid Values**"}
6==>|"Connect To Endpoint"|11
12@{ shape: doc, label: "*Notification Type*
**Notification type for Ongoing update subscription for product Valid Metadata Value Set: domainIdentifier**"}
12==>|"product asset [Monitored Resource]"|1
13@{ shape: processes, label: "*Governance Action Process*
**Create Daily refresh subscription for Valid Metadata Value Set: domainIdentifier**"}
13==>|"sourceDataSet [Target For Governance Action]"|1
14@{ shape: processes, label: "*Governance Action Process*
**Create Weekly refresh subscription for Valid Metadata Value Set: domainIdentifier**"}
14==>|"sourceDataSet [Target For Governance Action]"|1
15@{ shape: processes, label: "*Governance Action Process*
**Create Ongoing update subscription for Valid Metadata Value Set: domainIdentifier**"}
15==>|"sourceDataSet [Target For Governance Action]"|1
16@{ shape: processes, label: "*Governance Action Process*
**Create Evaluation subscription for Valid Metadata Value Set: domainIdentifier**"}
16==>|"sourceDataSet [Target For Governance Action]"|1
style 11 color:#000000, fill:#39add1, stroke:#004563
style 12 color:#FFFFFF, fill:#006400, stroke:#000000
style 13 color:#000000, fill:#40E0D0, stroke:#000000
style 14 color:#000000, fill:#40E0D0, stroke:#000000
style 15 color:#000000, fill:#40E0D0, stroke:#000000
style 16 color:#000000, fill:#40E0D0, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#9ACD32, fill:#8B008B, stroke:#004563
style 3 color:#000000, fill:#BDB76B, stroke:#004563
style 4 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#000000, fill:#838cc7, stroke:#3079ab
style 6 color:#000000, fill:#39add1, stroke:#004563
style 7 color:#000000, fill:#39add1, stroke:#004563
style 8 color:#000000, fill:#39add1, stroke:#004563
style 9 color:#000000, fill:#39add1, stroke:#004563
style 10 color:#000000, fill:#39add1, stroke:#004563
```
> Data set for domainIdentifier Valid Values: This asset represents the source of data for the digital product. (Extracted from 6.0-SNAPSHOT)
