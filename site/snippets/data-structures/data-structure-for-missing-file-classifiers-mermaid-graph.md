```mermaid
---
title: DataStructure - Data Structure for Missing File Classifiers [8b92bc90-70a3-4a62-95d9-51ba87024f9e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for Missing File Classifiers**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for Missing File Classifiers**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Asset Type Name**"}
1==>|"[9] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Data Encoding**"}
1==>|"[8] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Deployed Implementation Type (Technology Type)**"}
1==>|"[7] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Sync Time**"}
1==>|"[1] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Element Create Time**"}
1==>|"[10] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**File Extension**"}
1==>|"[5] 0..0 [Member Data Field]"|8
9@{ shape: stadium, label: "*Member Data Field*
**... plus 5 Items**"}
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
> Data Structure for Missing File Classifiers: The data structure lists the fields in the Missing File Classifiers product. (Extracted from 6.0-SNAPSHOT)
