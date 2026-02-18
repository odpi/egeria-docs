```mermaid
---
title: DataStructure - Data Structure for List of Annotations from all Survey Reports [80d9c232-608c-4c9f-9ef9-de64a9a3473b]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for List of Annotations from all Survey Reports**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for List of Annotations from all Survey Reports**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Open Metadata Type Name**"}
1==>|"[4] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Qualified Name**"}
1==>|"[5] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Engine Action Unique Identifier (GUID)**"}
1==>|"[17] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Survey Subject Unique Identifier (GUID)**"}
1==>|"[3] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Identifier**"}
1==>|"[8] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[23] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 16 Items**"}
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
> Data Structure for List of Annotations from all Survey Reports: The data structure lists the fields in the Annotations List product. (Extracted from 6.0-SNAPSHOT)
