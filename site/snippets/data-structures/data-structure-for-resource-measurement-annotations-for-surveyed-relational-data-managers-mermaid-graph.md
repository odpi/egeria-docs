```mermaid
---
title: DataStructure - Data Structure for Resource measurement annotations for surveyed Relational Data Managers [94be5d7c-a96d-43d2-8a74-4046f0e7d7ea]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Resource measurement annotations for surveyed Relational Data Managers**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Resource measurement annotations for surveyed Relational Data Managers**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Session Time**"}
1==>|"[16] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Column Count**"}
1==>|"[11] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Survey Annotation Unique Identifier (GUID)**"}
1==>|"[2] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[19] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Survey Subject Type Name**"}
1==>|"[6] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Rows Deleted**"}
1==>|"[15] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 13 Items**"}
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
> Data Structure for Resource measurement annotations for surveyed Relational Data Managers: The data structure lists the fields in the Relational Data Manager Measurements product. (Extracted from 6.0-SNAPSHOT)
