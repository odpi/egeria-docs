```mermaid
---
title: Technology Report for - Oracle Database Server [f98b41b9-9c37-4913-a17f-35935034505f]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**Oracle Database Server**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Software Server*
**Oracle Database Server template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**serverName**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**resourceName**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**databaseName**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**hostIdentifier**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*placeholder Property*
**description**"}
4==>|"SpecificationPropertyAssignment"|12
13@{ shape: hex, label: "*placeholder Property*
**portNumber**"}
4==>|"SpecificationPropertyAssignment"|13
14@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>14
15@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
14==>|"governance action process [Catalog Resource]"|15
16@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
15==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
16==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
16==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
16==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
16==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
16==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
16==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*supported Request Parameter*
**description**"}
16==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
16==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
16==>|"SpecificationPropertyAssignment"|25
26@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
14==>|"governance action process [Catalog Resource]"|26
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
**finalAnalysisStep**"}
30==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
30==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
30==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Request Parameter*
**description**"}
30==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
30==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
30==>|"SpecificationPropertyAssignment"|36
37@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
30==>|"SpecificationPropertyAssignment"|37
38@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
30==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
30==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
30==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
27==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
41==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
41==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
41==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>45
46@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|46
47@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
46==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Configuration Property*
**hostIdentifier**"}
47==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*supported Configuration Property*
**includeDatabaseList**"}
47==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*supported Configuration Property*
**databasePassword**"}
47==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Configuration Property*
**portNumber**"}
47==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*supported Configuration Property*
**OracleFriendshipGUID**"}
47==>|"SpecificationPropertyAssignment"|52
53@{ shape: hex, label: "*supported Configuration Property*
**databaseUserId**"}
47==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*supported Configuration Property*
**excludeDatabaseList**"}
47==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*supported Configuration Property*
**additionalConnectionProperties**"}
47==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*supported Configuration Property*
**serverName**"}
47==>|"SpecificationPropertyAssignment"|56
57@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
45==>|"resource [Uncatalog Resource]"|57
58@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
57==>|"SpecificationPropertyAssignment"|58
59@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
58==>|"SpecificationPropertyAssignment"|59
60@{ shape: hex, label: "*Property Type*
**producedGuard**"}
57==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*produced Guard*
**missing-template**"}
60==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
60==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
60==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*produced Guard*
**service-failed**"}
60==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
57==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
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
**set-up-complete**"}
70==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*produced Guard*
**service-failed**"}
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
**Survey Resource**"}
45==>|"resource [Survey Resource]"|79
80@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
79==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
80==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
79==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
82==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
82==>|"SpecificationPropertyAssignment"|84
85@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
82==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*Property Type*
**producedGuard**"}
79==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
86==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
86==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
86==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
79==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
90==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
90==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
90==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
79==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*produced Action Target*
**steward**"}
94==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
94==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
94==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
79==>|"SpecificationPropertyAssignment"|98
99@{ shape: hex, label: "*supported Action Target*
**oracleServer**"}
98==>|"SpecificationPropertyAssignment"|99
100@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|100
101@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
101==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*Property Type*
**producedGuard**"}
100==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*produced Guard*
**missing-template**"}
103==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
103==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*produced Guard*
**service-failed**"}
103==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
103==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
100==>|"SpecificationPropertyAssignment"|108
109@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
108==>|"SpecificationPropertyAssignment"|109
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 14 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
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
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#000000, fill:#40E0D0, stroke:#000000
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
style 46 color:#000000, fill:#BDB76B, stroke:#004563
style 47 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 54 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#000000, fill:#40E0D0, stroke:#000000
style 58 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 60 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 61 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 100 color:#000000, fill:#40E0D0, stroke:#000000
style 101 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 102 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 103 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 107 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 82 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 109 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 83 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 86 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
