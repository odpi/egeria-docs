```mermaid
---
title: Technology Report for - Db2 for Linux, UNIX and Windows Database Server [74ade7ad-a333-41ea-8af0-3da43a41c4ab]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**Db2 for Linux, UNIX and Windows Database Server**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Software Server*
**Db2 for Linux, UNIX and Windows Database Server template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**resourceName**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**hostIdentifier**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**databaseName**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**serverName**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**description**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*placeholder Property*
**portNumber**"}
4==>|"SpecificationPropertyAssignment"|12
13@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|13
14@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>14
15@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
14==>|"governance action process [Catalog Resource]"|15
16@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
14==>|"governance action process [Catalog Resource]"|16
17@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
16==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
17==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*supported Request Parameter*
**description**"}
17==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
17==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
17==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
17==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
17==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
17==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
17==>|"SpecificationPropertyAssignment"|25
26@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
17==>|"SpecificationPropertyAssignment"|26
27@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
14==>|"governance action process [Survey Resource]"|27
28@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
27==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
28==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
27==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
30==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
30==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
30==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
30==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
30==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
30==>|"SpecificationPropertyAssignment"|36
37@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
30==>|"SpecificationPropertyAssignment"|37
38@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
30==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
30==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Request Parameter*
**description**"}
30==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
27==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
41==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
41==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
41==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>45
46@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
45==>|"resource [Survey Resource]"|46
47@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
46==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
47==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
46==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
49==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
49==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
49==>|"SpecificationPropertyAssignment"|52
53@{ shape: hex, label: "*Property Type*
**producedGuard**"}
46==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
53==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
53==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
53==>|"SpecificationPropertyAssignment"|56
57@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
46==>|"SpecificationPropertyAssignment"|57
58@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
57==>|"SpecificationPropertyAssignment"|58
59@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
57==>|"SpecificationPropertyAssignment"|59
60@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
57==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
46==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
61==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
61==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*produced Action Target*
**steward**"}
61==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
46==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*supported Action Target*
**db2luwServer**"}
65==>|"SpecificationPropertyAssignment"|66
67@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|67
68@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
67==>|"SpecificationPropertyAssignment"|68
69@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
68==>|"SpecificationPropertyAssignment"|69
70@{ shape: hex, label: "*Property Type*
**producedGuard**"}
67==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
70==>|"SpecificationPropertyAssignment"|71
72@{ shape: hex, label: "*produced Guard*
**service-failed**"}
70==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
70==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
70==>|"SpecificationPropertyAssignment"|74
75@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
67==>|"SpecificationPropertyAssignment"|75
76@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
75==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
67==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
77==>|"SpecificationPropertyAssignment"|78
79@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|79
80@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
79==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
80==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*Property Type*
**producedGuard**"}
79==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*produced Guard*
**missing-template**"}
82==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*produced Guard*
**service-failed**"}
82==>|"SpecificationPropertyAssignment"|84
85@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
82==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
82==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
79==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
87==>|"SpecificationPropertyAssignment"|88
89@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|89
90@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
89==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*supported Configuration Property*
**hostIdentifier**"}
90==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*supported Configuration Property*
**serverName**"}
90==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*supported Configuration Property*
**excludeDatabaseList**"}
90==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*supported Configuration Property*
**databasePassword**"}
90==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*supported Configuration Property*
**portNumber**"}
90==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*supported Configuration Property*
**includeDatabaseList**"}
90==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*supported Configuration Property*
**DB2LUWFriendshipGUID**"}
90==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*supported Configuration Property*
**databaseUserId**"}
90==>|"SpecificationPropertyAssignment"|98
99@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
45==>|"resource [Uncatalog Resource]"|99
100@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
99==>|"SpecificationPropertyAssignment"|100
101@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*Property Type*
**producedGuard**"}
99==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
102==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*produced Guard*
**missing-template**"}
102==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
102==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*produced Guard*
**service-failed**"}
102==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
99==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
107==>|"SpecificationPropertyAssignment"|108
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#000000, fill:#BDB76B, stroke:#004563
style 90 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#000000, fill:#40E0D0, stroke:#000000
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 14 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 15 color:#000000, fill:#40E0D0, stroke:#000000
style 16 color:#000000, fill:#40E0D0, stroke:#000000
style 17 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
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
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 27 color:#000000, fill:#40E0D0, stroke:#000000
style 28 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 38 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 46 color:#000000, fill:#40E0D0, stroke:#000000
style 47 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 54 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 58 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 66 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 67 color:#000000, fill:#40E0D0, stroke:#000000
style 68 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 73 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 78 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 79 color:#000000, fill:#40E0D0, stroke:#000000
style 100 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 101 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 107 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 83 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
```
