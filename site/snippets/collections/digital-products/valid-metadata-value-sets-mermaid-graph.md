```mermaid
---
title: DigitalProductFamily - Valid Metadata Value Sets [9e006e82-358f-48e2-af8c-5b41571d979a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Valid Metadata Value Sets**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Digital Product*
**Valid Metadata Value Set List**"}
1==>|"includes product [Collection Membership]"|3
4@{ shape: cyl, label: "*Reference Code Table*
**Open Metadata Property List for Valid Metadata Value Set List**"}
3==>|"product data set [Collection Membership]"|4
5@{ shape: rect, label: "*Digital Product*
**sortOrder Valid Values**"}
1==>|"includes product [Collection Membership]"|5
6@{ shape: cyl, label: "*Reference Code Table*
**Data set for sortOrder Valid Values**"}
5==>|"product data set [Collection Membership]"|6
7@{ shape: rect, label: "*Digital Product*
**direction Valid Values**"}
1==>|"includes product [Collection Membership]"|7
8@{ shape: cyl, label: "*Reference Code Table*
**Data set for direction Valid Values**"}
7==>|"product data set [Collection Membership]"|8
9@{ shape: rect, label: "*Digital Product*
**contactMethodType Valid Values**"}
1==>|"includes product [Collection Membership]"|9
10@{ shape: cyl, label: "*Reference Code Table*
**Data set for contactMethodType Valid Values**"}
9==>|"product data set [Collection Membership]"|10
11@{ shape: rect, label: "*Digital Product*
**useType Valid Values**"}
1==>|"includes product [Collection Membership]"|11
12@{ shape: cyl, label: "*Reference Code Table*
**Data set for useType Valid Values**"}
11==>|"product data set [Collection Membership]"|12
13@{ shape: rect, label: "*Digital Product*
**stars Valid Values**"}
1==>|"includes product [Collection Membership]"|13
14@{ shape: cyl, label: "*Reference Code Table*
**Data set for stars Valid Values**"}
13==>|"product data set [Collection Membership]"|14
15@{ shape: stadium, label: "*Collection Membership*
**... plus 48 Items**"}
1-.->15
16@{ shape: rounded, label: "*Community*
**Open Metadata Reference Data special interest group**"}
16==>|"Scoped By"|1
17@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Valid Metadata Value Sets**"}
17==>|"Owner [Assignment Scope]"|1
18@{ shape: doc, label: "*License Type*
**Data for Internal Use**"}
1==>|"subscriber''s license [Governed By]"|18
style 11 color:#000000, fill:#838cc7, stroke:#3079ab
style 12 color:#000000, fill:#BDB76B, stroke:#004563
style 13 color:#000000, fill:#838cc7, stroke:#3079ab
style 14 color:#000000, fill:#BDB76B, stroke:#004563
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#39add1, stroke:#004563
style 17 color:#000000, fill:#FFE599, stroke:#000000
style 18 color:#FFFFFF, fill:#006400, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#838cc7, stroke:#3079ab
style 4 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#000000, fill:#838cc7, stroke:#3079ab
style 6 color:#000000, fill:#BDB76B, stroke:#004563
style 7 color:#000000, fill:#838cc7, stroke:#3079ab
style 8 color:#000000, fill:#BDB76B, stroke:#004563
style 9 color:#000000, fill:#838cc7, stroke:#3079ab
style 10 color:#000000, fill:#BDB76B, stroke:#004563
```
> Valid Metadata Value Sets: Each product in this folder is an extract of the valid metadata values.  The valid metadata values are organized into a tabular data set, where each row is a specific valid value.  These products can be used as standard reference values when building other digital products to help consumers join data from multiple products together. (Extracted from 6.0-SNAPSHOT)
