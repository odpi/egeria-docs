```mermaid
---
title: DataStructure - Data Structure for category Valid Values [90b73a9b-601a-4536-ac05-241664f8da18]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for category Valid Values**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for category Valid Values**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Identifier**"}
1==>|"[5] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Is Case Sensitive?**"}
1==>|"[11] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Description**"}
1==>|"[7] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Category**"}
1==>|"[8] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Globally Unique Identifier (GUID)**"}
1==>|"[1] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Preferred Value**"}
1==>|"[10] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 8 Items**"}
1-.->9
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#deb887, stroke:#000000
style 3 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 4 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 5 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 6 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 7 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 8 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
> Data Structure for category Valid Values: The data structure lists the fields in the Valid Metadata Value Set: category product. (Extracted from 6.0-SNAPSHOT)
