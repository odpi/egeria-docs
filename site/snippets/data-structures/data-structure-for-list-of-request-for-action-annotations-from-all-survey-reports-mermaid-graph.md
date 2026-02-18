```mermaid
---
title: DataStructure - Data Structure for List of Request For Action Annotations from all Survey Reports [adbd9819-8d97-4887-a398-3c9fa760f31d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Data Structure*
**Data Structure for List of Request For Action Annotations from all Survey Reports**"}
2@{ shape: rect, label: "*Data Spec*
**Data Specification for List of Request For Action Annotations from all Survey Reports**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Data Field*
**Survey Report Unique Identifier (GUID)**"}
1==>|"[1] 0..0 [Member Data Field]"|3
4@{ shape: rect, label: "*Data Field*
**Element Create Time**"}
1==>|"[5] 0..0 [Member Data Field]"|4
5@{ shape: rect, label: "*Data Field*
**Survey Annotation Unique Identifier (GUID)**"}
1==>|"[2] 0..0 [Member Data Field]"|5
6@{ shape: rect, label: "*Data Field*
**Element Last Update Time**"}
1==>|"[6] 0..0 [Member Data Field]"|6
7@{ shape: rect, label: "*Data Field*
**Action Request Name**"}
1==>|"[4] 0..0 [Member Data Field]"|7
8@{ shape: rect, label: "*Data Field*
**Survey Subject Unique Identifier (GUID)**"}
1==>|"[3] 0..0 [Member Data Field]"|8
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#deb887, stroke:#000000
style 3 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 4 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 5 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 6 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 7 color:#000000, fill:#ffe3cc, stroke:#f9845b
style 8 color:#000000, fill:#ffe3cc, stroke:#f9845b
```
> Data Structure for List of Request For Action Annotations from all Survey Reports: The data structure lists the fields in the Request For Action Annotations List product. (Extracted from 6.0-SNAPSHOT)
