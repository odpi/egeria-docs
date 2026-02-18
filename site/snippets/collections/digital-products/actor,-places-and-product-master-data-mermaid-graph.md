```mermaid
---
title: DigitalProductFamily - Actor, Places and Product Master Data [0f50ceb1-b2f9-4998-957e-b5aa25922f27]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Actor, Places and Product Master Data**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Digital Product*
**List of Locations**"}
1==>|"includes product [Collection Membership]"|3
4@{ shape: cyl, label: "*Reference Code Table*
**Data set for List of Locations**"}
3==>|"product data set [Collection Membership]"|4
5@{ shape: rect, label: "*Digital Product*
**Digital Product List**"}
1==>|"includes product [Collection Membership]"|5
6@{ shape: cyl, label: "*Reference Code Table*
**Data set for Digital Product List**"}
5==>|"product data set [Collection Membership]"|6
7@{ shape: rect, label: "*Digital Product*
**Organization List**"}
1==>|"includes product [Collection Membership]"|7
8@{ shape: cyl, label: "*Reference Code Table*
**Data set for Organization List**"}
7==>|"product data set [Collection Membership]"|8
9@{ shape: rect, label: "*Digital Product*
**People List**"}
1==>|"includes product [Collection Membership]"|9
10@{ shape: cyl, label: "*Reference Code Table*
**Data set for People List**"}
9==>|"product data set [Collection Membership]"|10
11@{ shape: rounded, label: "*Community*
**Open Metadata Master Data special interest group**"}
11==>|"Scoped By"|1
12@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Actor, Places and Products**"}
12==>|"Owner [Assignment Scope]"|1
style 11 color:#000000, fill:#39add1, stroke:#004563
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 12 color:#000000, fill:#FFE599, stroke:#000000
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
> Actor, Places and Product Master Data: Each product in this folder lists information held in the open metadata about people, organizations, users, teams, locations and digital products.  This type of data is called master data because it describes the key entities that the organization operates around.  As such, some form of this data appears in most data sets.  Each product in this folder is organized into a tabular data set, where each row is a specific (master data) entity.   These are designed to be used as standard values that can be used for validation or to ensure that data in digital products is consistent making it easier to join data from multiple products. (Extracted from 6.0-SNAPSHOT)
