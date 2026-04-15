```mermaid
---
title: DataStructure - Data Structure for Organization List [0e8daf48-0898-4d3d-bf81-80a8a31d7014]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Organization List**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Organization List**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Display Name**"}
1==>|"[4] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Globally Unique Identifier (GUID)**"}
1==>|"[1] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[8] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Description**"}
1==>|"[6] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Open Metadata Type Name**"}
1==>|"[2] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Identifier**"}
1==>|"[3] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 2 Items**"}
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
> Data Structure for Organization List: The data structure lists the fields in the Organization List product. (Extracted from 6.0-SNAPSHOT)
