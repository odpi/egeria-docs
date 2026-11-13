```mermaid
---
title: Technology Report for - OMAG Server Platform [e76e450d-9533-4e98-b83d-c3ea7f8b0a08]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**OMAG Server Platform**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Software Server Platform*
**OMAG Server Platform template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**organizationName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**resourceName**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**platformUserId**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**platformURLRoot**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**identifier**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*placeholder Property*
**platformName**"}
4==>|"SpecificationPropertyAssignment"|12
13@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|13
14@{ shape: hex, label: "*placeholder Property*
**platformDescription**"}
4==>|"SpecificationPropertyAssignment"|14
15@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>15
16@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
15==>|"resource [Uncatalog Resource]"|16
17@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
16==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
17==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*Property Type*
**producedGuard**"}
16==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*produced Guard*
**service-failed**"}
19==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
19==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*produced Guard*
**missing-template**"}
19==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
19==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
16==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
24==>|"SpecificationPropertyAssignment"|25
26@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
15==>|"resource [Catalog Resource]"|26
27@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
15==>|"resource [Catalog Resource]"|27
28@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
27==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
28==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*Property Type*
**producedGuard**"}
27==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
30==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
30==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*produced Guard*
**service-failed**"}
30==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*produced Guard*
**missing-template**"}
30==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
27==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
35==>|"SpecificationPropertyAssignment"|36
37@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
15==>|"resource [Catalog Resource]"|37
38@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
37==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
38==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*Property Type*
**producedGuard**"}
37==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*produced Guard*
**service-failed**"}
40==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
40==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
40==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
40==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
37==>|"SpecificationPropertyAssignment"|45
46@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
45==>|"SpecificationPropertyAssignment"|46
47@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
37==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
47==>|"SpecificationPropertyAssignment"|48
49@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
15==>|"resource [Catalog Resource]"|49
50@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
49==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Configuration Property*
**friendshipGUID**"}
50==>|"SpecificationPropertyAssignment"|51
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 46 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 47 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#000000, fill:#BDB76B, stroke:#004563
style 50 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 14 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 15 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 16 color:#000000, fill:#40E0D0, stroke:#000000
style 17 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 1 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 2 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 3 color:#004563, fill:#b0e0e6, stroke:#004563
style 4 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 5 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 6 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 7 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 20 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 24 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#000000, fill:#BDB76B, stroke:#004563
style 27 color:#000000, fill:#40E0D0, stroke:#000000
style 28 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#000000, fill:#40E0D0, stroke:#000000
style 38 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
