```mermaid
---
title: DataStructure - Data Structure for Resource measurement annotations for surveyed Relational Tables [4135fd6f-877d-42a6-aabc-dd9acd556a99]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Resource measurement annotations for surveyed Relational Tables**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Resource measurement annotations for surveyed Relational Tables**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Survey Subject Unique Identifier (GUID)**"}
1==>|"[4] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Survey Report Unique Identifier (GUID)**"}
1==>|"[1] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[14] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**View Count**"}
1==>|"[9] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Survey Subject Type Name**"}
1==>|"[6] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Display Name**"}
1==>|"[7] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 8 Items**"}
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
> Data Structure for Resource measurement annotations for surveyed Relational Tables: The data structure lists the fields in the Relational Table Measurements product. (Extracted from 6.0-SNAPSHOT)
