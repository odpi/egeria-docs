```mermaid
---
title: DigitalProductFamily - Survey Reports [eddea903-0eab-4003-a8e1-92ac8e3b49c1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Survey Reports**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Digital Product*
**Resource measurement annotations for surveyed directories (folders)**"}
1==>|"includes product [Collection Membership]"|3
4@{ shape: cyl, label: "*Reference Code Table*
**Data set for Resource measurement annotations for surveyed directories (folders)**"}
3==>|"product data set [Collection Membership]"|4
5@{ shape: rect, label: "*Digital Product*
**List of Request For Action Annotations from all Survey Reports**"}
1==>|"includes product [Collection Membership]"|5
6@{ shape: cyl, label: "*Reference Code Table*
**Data set for List of Request For Action Annotations from all Survey Reports**"}
5==>|"product data set [Collection Membership]"|6
7@{ shape: rect, label: "*Digital Product*
**Resource measurement annotations for surveyed Relational Data Managers**"}
1==>|"includes product [Collection Membership]"|7
8@{ shape: cyl, label: "*Reference Code Table*
**Data set for Resource measurement annotations for surveyed Relational Data Managers**"}
7==>|"product data set [Collection Membership]"|8
9@{ shape: rect, label: "*Digital Product*
**List of Annotations from all Survey Reports**"}
1==>|"includes product [Collection Membership]"|9
10@{ shape: cyl, label: "*Reference Code Table*
**Data set for List of Annotations from all Survey Reports**"}
9==>|"product data set [Collection Membership]"|10
11@{ shape: rect, label: "*Digital Product*
**Resource measurement annotations for surveyed Relational Tables**"}
1==>|"includes product [Collection Membership]"|11
12@{ shape: cyl, label: "*Reference Code Table*
**Data set for Resource measurement annotations for surveyed Relational Tables**"}
11==>|"product data set [Collection Membership]"|12
13@{ shape: rect, label: "*Digital Product*
**Resource measurement annotations for surveyed Files**"}
1==>|"includes product [Collection Membership]"|13
14@{ shape: cyl, label: "*Reference Code Table*
**Data set for Resource measurement annotations for surveyed Files**"}
13==>|"product data set [Collection Membership]"|14
15@{ shape: stadium, label: "*Collection Membership*
**... plus 7 Items**"}
1-.->15
16@{ shape: rounded, label: "*Community*
**Open Metadata Observability special interest group**"}
16==>|"Scoped By"|1
17@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Survey Reports**"}
17==>|"Owner [Assignment Scope]"|1
18@{ shape: doc, label: "*License Type*
**Data for Internal Use**"}
1==>|"subscriber''s license [Governed By]"|18
style 11 color:#000000, fill:#838cc7, stroke:#3079ab
style 12 color:#000000, fill:#bdb76b, stroke:#004563
style 13 color:#000000, fill:#838cc7, stroke:#3079ab
style 14 color:#000000, fill:#bdb76b, stroke:#004563
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#39add1, stroke:#004563
style 17 color:#000000, fill:#FFE599, stroke:#000000
style 18 color:#FFFFFF, fill:#006400, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#838cc7, stroke:#3079ab
style 4 color:#000000, fill:#bdb76b, stroke:#004563
style 5 color:#000000, fill:#838cc7, stroke:#3079ab
style 6 color:#000000, fill:#bdb76b, stroke:#004563
style 7 color:#000000, fill:#838cc7, stroke:#3079ab
style 8 color:#000000, fill:#bdb76b, stroke:#004563
style 9 color:#000000, fill:#838cc7, stroke:#3079ab
style 10 color:#000000, fill:#bdb76b, stroke:#004563
```
> Survey Reports: Each product in this folder publishes insights from the surveys published through the open survey framework.  These surveys may be run as engine actions in the Engine Host, or run in an external surveying process that published results through the Data Discovery API. (Extracted from 6.0-SNAPSHOT)
