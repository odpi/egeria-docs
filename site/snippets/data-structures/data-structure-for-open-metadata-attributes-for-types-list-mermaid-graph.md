```mermaid
---
title: DataStructure - Data Structure for Open Metadata Attributes For Types List [f3a34df6-aed4-4d54-8e07-63b75526fc40]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Open Metadata Attributes For Types List**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Open Metadata Attributes For Types List**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Open Metadata Attribute Name**"}
1==>|"[2] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Data Type**"}
1==>|"[4] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Is Nullable?**"}
1==>|"[3] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Open Metadata Attribute Status**"}
1==>|"[6] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[8] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Element Create Time**"}
1==>|"[7] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 2 Items**"}
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
> Data Structure for Open Metadata Attributes For Types List: The data structure lists the fields in the Open Metadata Attributes For Types List product. (Extracted from 6.0-SNAPSHOT)
