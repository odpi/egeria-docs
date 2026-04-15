```mermaid
---
title: DigitalProductFamily - Reference Data Sets [c6cbf377-928e-4216-b1f6-16a45794d589]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Reference Data Sets**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Digital Product*
**facilityType Valid Values**"}
1==>|"includes product [Collection Membership]"|3
4@{ shape: cyl, label: "*Reference Code Table*
**Data set for facilityType Valid Values**"}
3==>|"product data set [Collection Membership]"|4
5@{ shape: rect, label: "*Digital Product*
**Reference Data Set List**"}
1==>|"includes product [Collection Membership]"|5
6@{ shape: cyl, label: "*Reference Code Table*
**Data set for Reference Data Set List**"}
5==>|"product data set [Collection Membership]"|6
7@{ shape: rounded, label: "*Community*
**Open Metadata Reference Data special interest group**"}
7==>|"Scoped By"|1
8@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Reference Data Sets**"}
8==>|"Owner [Assignment Scope]"|1
9@{ shape: doc, label: "*License Type*
**Data for Internal Use**"}
1==>|"subscriber''s license [Governed By]"|9
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#838cc7, stroke:#3079ab
style 4 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#000000, fill:#838cc7, stroke:#3079ab
style 6 color:#000000, fill:#BDB76B, stroke:#004563
style 7 color:#000000, fill:#39add1, stroke:#004563
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#FFFFFF, fill:#006400, stroke:#000000
```
> Reference Data Sets: Each product in this folder is an extract of the reference data values managed by open metadata.  The reference data values are organized into a tabular data set, where each row is a specific valid value.  These products can be used as standard reference values when building other digital products to help consumers join data from multiple products together. (Extracted from 6.0-SNAPSHOT)
