```mermaid
---
title: DataStructure - Data Structure for List of Annotations from all Survey Reports [61adb0bd-a7f3-48f0-9a64-7fc2681e2ced]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for List of Annotations from all Survey Reports**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for List of Annotations from all Survey Reports**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**End Timestamp**"}
1==>|"[13] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Category**"}
1==>|"[7] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Element Create Time**"}
1==>|"[22] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Purpose**"}
1==>|"[11] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Engine Host User Identifier (userId)**"}
1==>|"[21] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Asset Type Name**"}
1==>|"[15] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 16 Items**"}
1-.->9
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#DEB887, stroke:#000000
style 3 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 4 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 5 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 6 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 7 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 8 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
> Data Structure for List of Annotations from all Survey Reports: The data structure lists the fields in the Annotations List product. (Extracted from 6.0-SNAPSHOT)
