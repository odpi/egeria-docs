```mermaid
---
title: Technology Report for - PostgreSQL Server [ff7c8d09-9813-453e-9895-7a2b0a6b0be3]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**PostgreSQL Server**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Software Server*
**PostgreSQL Server template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**serverName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**portNumber**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**description**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**resourceName**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*placeholder Property*
**hostIdentifier**"}
4==>|"SpecificationPropertyAssignment"|12
13@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>13
14@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
13==>|"governance action process [Catalog Resource]"|14
15@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
13==>|"governance action process [Catalog Resource]"|15
16@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
15==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
16==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
16==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
16==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
16==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
16==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*supported Request Parameter*
**description**"}
16==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
16==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
16==>|"SpecificationPropertyAssignment"|24
25@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
13==>|"governance action process [Survey Resource]"|25
26@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
25==>|"SpecificationPropertyAssignment"|26
27@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
26==>|"SpecificationPropertyAssignment"|27
28@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
25==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
28==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
28==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
28==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*supported Request Parameter*
**description**"}
28==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
28==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
28==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
28==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
28==>|"SpecificationPropertyAssignment"|36
37@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
28==>|"SpecificationPropertyAssignment"|37
38@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
25==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
38==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
38==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
38==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>42
43@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
42==>|"resource [Catalog Resource]"|43
44@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
43==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*supported Configuration Property*
**excludeDatabaseList**"}
44==>|"SpecificationPropertyAssignment"|45
46@{ shape: hex, label: "*supported Configuration Property*
**databasePassword**"}
44==>|"SpecificationPropertyAssignment"|46
47@{ shape: hex, label: "*supported Configuration Property*
**hostIdentifier**"}
44==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Configuration Property*
**serverName**"}
44==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*supported Configuration Property*
**databaseUserId**"}
44==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*supported Configuration Property*
**includeDatabaseList**"}
44==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Configuration Property*
**portNumber**"}
44==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*supported Configuration Property*
**PostgreSQLFriendshipGUID**"}
44==>|"SpecificationPropertyAssignment"|52
53@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
42==>|"resource [Catalog Resource]"|53
54@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
53==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
54==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*Property Type*
**producedGuard**"}
53==>|"SpecificationPropertyAssignment"|56
57@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
56==>|"SpecificationPropertyAssignment"|57
58@{ shape: hex, label: "*produced Guard*
**service-failed**"}
56==>|"SpecificationPropertyAssignment"|58
59@{ shape: hex, label: "*produced Guard*
**missing-template**"}
56==>|"SpecificationPropertyAssignment"|59
60@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
56==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
53==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
61==>|"SpecificationPropertyAssignment"|62
63@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
42==>|"resource [Catalog Resource]"|63
64@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
63==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
64==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*Property Type*
**producedGuard**"}
63==>|"SpecificationPropertyAssignment"|66
67@{ shape: hex, label: "*produced Guard*
**service-failed**"}
66==>|"SpecificationPropertyAssignment"|67
68@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
66==>|"SpecificationPropertyAssignment"|68
69@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
66==>|"SpecificationPropertyAssignment"|69
70@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
66==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
63==>|"SpecificationPropertyAssignment"|71
72@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
71==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
63==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
73==>|"SpecificationPropertyAssignment"|74
75@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
42==>|"resource [Uncatalog Resource]"|75
76@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
75==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
76==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*Property Type*
**producedGuard**"}
75==>|"SpecificationPropertyAssignment"|78
79@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
78==>|"SpecificationPropertyAssignment"|79
80@{ shape: hex, label: "*produced Guard*
**missing-template**"}
78==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
78==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*produced Guard*
**service-failed**"}
78==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
75==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
83==>|"SpecificationPropertyAssignment"|84
85@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
42==>|"resource [Survey Resource]"|85
86@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
85==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
86==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
85==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
88==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
88==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
88==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*Property Type*
**producedGuard**"}
85==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
92==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
92==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
92==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
85==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
96==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
96==>|"SpecificationPropertyAssignment"|98
99@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
96==>|"SpecificationPropertyAssignment"|99
100@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
85==>|"SpecificationPropertyAssignment"|100
101@{ shape: hex, label: "*produced Action Target*
**steward**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
100==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
100==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
85==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*supported Action Target*
**postgreSQLServer**"}
104==>|"SpecificationPropertyAssignment"|105
style 88 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 89 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 14 color:#000000, fill:#40E0D0, stroke:#000000
style 15 color:#000000, fill:#40E0D0, stroke:#000000
style 16 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 17 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 24 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 25 color:#000000, fill:#40E0D0, stroke:#000000
style 26 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 38 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 42 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 43 color:#000000, fill:#BDB76B, stroke:#004563
style 44 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 47 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#000000, fill:#40E0D0, stroke:#000000
style 54 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#000000, fill:#40E0D0, stroke:#000000
style 64 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 67 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 68 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 71 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 73 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#000000, fill:#40E0D0, stroke:#000000
style 76 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 101 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 83 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#000000, fill:#40E0D0, stroke:#000000
style 86 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
