```mermaid
---
title: DigitalProductFamily - Reference Data Sets [2ca66143-4acc-4838-815c-87e78b42878a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Reference Data Sets**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Digital Product*
**Reference Data Set List**"}
1==>|"includes product [Collection Membership]"|3
4@{ shape: cyl, label: "*Reference Code Table*
**Data set for Reference Data Set List**"}
3==>|"product data set [Collection Membership]"|4
5@{ shape: rounded, label: "*Community*
**Open Metadata Reference Data special interest group**"}
5==>|"Scoped By"|1
6@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Reference Data Sets**"}
6==>|"Owner [Assignment Scope]"|1
7@{ shape: doc, label: "*License Type*
**Data for Internal Use**"}
1==>|"subscriber''s license [Governed By]"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#838cc7, stroke:#3079ab
style 4 color:#000000, fill:#bdb76b, stroke:#004563
style 5 color:#000000, fill:#39add1, stroke:#004563
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#FFFFFF, fill:#006400, stroke:#000000
```
> Reference Data Sets: Each product in this folder is an extract of the reference data values managed by open metadata.  The reference data values are organized into a tabular data set, where each row is a specific valid value.  These products can be used as standard reference values when building other digital products to help consumers join data from multiple products together. (Extracted from 6.0-SNAPSHOT)
