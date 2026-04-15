```mermaid
---
title: DataStructure - Data Structure for Open Metadata Data Types List [24ca736a-455d-4d2e-b006-d48b76615ac3]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Open Metadata Data Types List**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Open Metadata Data Types List**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Globally Unique Identifier (GUID)**"}
1==>|"[2] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Description**"}
1==>|"[3] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Data Type**"}
1==>|"[1] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[6] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Category**"}
1==>|"[4] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Element Create Time**"}
1==>|"[5] 0..0 [Member Data Field]"|8
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#DEB887, stroke:#000000
style 3 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 4 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 5 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 6 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 7 color:#000000, fill:#ffe3cc, stroke:#FFA500
style 8 color:#000000, fill:#ffe3cc, stroke:#FFA500
```
> Data Structure for Open Metadata Data Types List: The data structure lists the fields in the Open Metadata Data Types List product. (Extracted from 6.0-SNAPSHOT)
