```mermaid
---
title: Solution Component - Set up Data Lake [fb32bef2-e79f-4893-b500-2e547f24d482]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: subproc, label: "*Solution Component*
**Set up Data Lake**"}
subgraph 2 [Subcomponents]
3@{ shape: lin-cyl, label: "*Solution Component*
**Weekly Measurements Data Lake Folder**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
```
> Set up Data Lake: Set up the data stores for receiving data from the hospitals - this includes the file system directory and Unity Catalog Volume for incoming patient measurements, along with the data set collection for certified measurement files. (Extracted from V1.0)
