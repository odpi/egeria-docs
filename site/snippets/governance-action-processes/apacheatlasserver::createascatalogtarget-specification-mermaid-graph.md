```mermaid
---
title: Specification for - ApacheAtlasServer::CreateAsCatalogTarget [7a9e2bee-9b09-477d-8026-28a945cded16]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**ApacheAtlasServer::CreateAsCatalogTarget**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
2==>3
subgraph 4 [versionIdentifier details]
5@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
6@{ shape: text, label: "*data Type:*
**string**"}
7@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
8@{ shape: text, label: "*required:*
**false**"}
end
3==>4
9@{ shape: hex, label: "*Specification Property Value*
**secretsStorePathName**"}
2==>9
subgraph 10 [secretsStorePathName details]
11@{ shape: text, label: "*description:*
**The full path name to the secrets store file where the secrets collection for this server is located.**"}
12@{ shape: text, label: "*data Type:*
**string**"}
13@{ shape: text, label: "*example:*
**loading-bay/secrets/integration.omsecrets**"}
14@{ shape: text, label: "*required:*
**false**"}
end
9==>10
15@{ shape: hex, label: "*Specification Property Value*
**hostURL**"}
2==>15
subgraph 16 [hostURL details]
17@{ shape: text, label: "*description:*
**The host IP address or domain name of the server with the HTTP protocol prefix.**"}
18@{ shape: text, label: "*data Type:*
**string**"}
19@{ shape: text, label: "*example:*
**https:/ /coconet.com**"}
20@{ shape: text, label: "*required:*
**false**"}
end
15==>16
21@{ shape: hex, label: "*Specification Property Value*
**description**"}
2==>21
subgraph 22 [description details]
23@{ shape: text, label: "*description:*
**The description of the element to help a consumer understand its content and purpose.**"}
24@{ shape: text, label: "*data Type:*
**string**"}
25@{ shape: text, label: "*example:*
**This file contains a week''s worth of patient data for the Teddy Bear Drop Foot clinical trial.**"}
26@{ shape: text, label: "*required:*
**false**"}
end
21==>22
27@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
2==>27
subgraph 28 [serverName details]
29@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
30@{ shape: text, label: "*data Type:*
**string**"}
31@{ shape: text, label: "*example:*
**myServer**"}
32@{ shape: text, label: "*required:*
**false**"}
end
27==>28
33@{ shape: hex, label: "*Specification Property Value*
**portNumber**"}
2==>33
subgraph 34 [portNumber details]
35@{ shape: text, label: "*description:*
**The number of the port to use to connect to a service.**"}
36@{ shape: text, label: "*data Type:*
**string**"}
37@{ shape: text, label: "*example:*
**1234**"}
38@{ shape: text, label: "*required:*
**false**"}
end
33==>34
39@{ shape: hex, label: "*Specification Property Value*
**secretsCollectionName**"}
2==>39
subgraph 40 [secretsCollectionName details]
41@{ shape: text, label: "*description:*
**The name used to identify the collection of secrets that a particular connector is using.**"}
42@{ shape: text, label: "*data Type:*
**string**"}
43@{ shape: text, label: "*example:*
**local-postgres-db**"}
44@{ shape: text, label: "*required:*
**false**"}
end
39==>40
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 31 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 35 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 36 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
