```mermaid
---
title: Technology Report for - PostgreSQL Relational Database [ff56fc56-c4a1-469e-8040-472e8fe54694]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**PostgreSQL Relational Database**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Relational Database*
**PostgreSQL Relational Database template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**databaseName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**portNumber**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**serverName**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**databaseDescription**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*placeholder Property*
**hostIdentifier**"}
4==>|"SpecificationPropertyAssignment"|12
13@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>13
14@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
13==>|"governance action process [Survey Resource]"|14
15@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
14==>|"SpecificationPropertyAssignment"|15
16@{ shape: hex, label: "*produced Annotation Type*
**Capture Frequent Values for Column**"}
15==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
15==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*produced Annotation Type*
**Capture Table Sizes for a Database Schema**"}
15==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Column Measurements**"}
15==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
15==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
15==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Sizes**"}
15==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Measurements**"}
15==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
15==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Schema Measurements**"}
15==>|"SpecificationPropertyAssignment"|25
26@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
14==>|"SpecificationPropertyAssignment"|26
27@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
26==>|"SpecificationPropertyAssignment"|27
28@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
26==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
26==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*supported Request Parameter*
**databaseDescription**"}
26==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
26==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
26==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
26==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
26==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
26==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
14==>|"SpecificationPropertyAssignment"|36
37@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
36==>|"SpecificationPropertyAssignment"|37
38@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
36==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
36==>|"SpecificationPropertyAssignment"|39
40@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
13==>|"governance action process [Catalog Resource]"|40
41@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
40==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
41==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
41==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
41==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*supported Request Parameter*
**hostIdentifier**"}
41==>|"SpecificationPropertyAssignment"|45
46@{ shape: hex, label: "*supported Request Parameter*
**databaseDescription**"}
41==>|"SpecificationPropertyAssignment"|46
47@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
41==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
41==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
41==>|"SpecificationPropertyAssignment"|49
50@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
13==>|"governance action process [Catalog Resource]"|50
51@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>51
52@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
51==>|"resource [Survey Resource]"|52
53@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
52==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
53==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Measurements**"}
53==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*produced Annotation Type*
**Capture Table Sizes for a Database Schema**"}
53==>|"SpecificationPropertyAssignment"|56
57@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Schema Measurements**"}
53==>|"SpecificationPropertyAssignment"|57
58@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
53==>|"SpecificationPropertyAssignment"|58
59@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Sizes**"}
53==>|"SpecificationPropertyAssignment"|59
60@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
53==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Column Measurements**"}
53==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
53==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*produced Annotation Type*
**Capture Frequent Values for Column**"}
53==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
52==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
64==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
64==>|"SpecificationPropertyAssignment"|66
67@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
64==>|"SpecificationPropertyAssignment"|67
68@{ shape: hex, label: "*Property Type*
**producedGuard**"}
52==>|"SpecificationPropertyAssignment"|68
69@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
68==>|"SpecificationPropertyAssignment"|69
70@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
68==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
68==>|"SpecificationPropertyAssignment"|71
72@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
52==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
72==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
72==>|"SpecificationPropertyAssignment"|74
75@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
72==>|"SpecificationPropertyAssignment"|75
76@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
52==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*supported Action Target*
**postgresDatabase**"}
76==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
52==>|"SpecificationPropertyAssignment"|78
79@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
78==>|"SpecificationPropertyAssignment"|79
80@{ shape: hex, label: "*produced Action Target*
**steward**"}
78==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
78==>|"SpecificationPropertyAssignment"|81
82@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
51==>|"resource [Catalog Resource]"|82
83@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
82==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
83==>|"SpecificationPropertyAssignment"|84
85@{ shape: hex, label: "*Property Type*
**producedGuard**"}
82==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*produced Guard*
**missing-template**"}
85==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
85==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*produced Guard*
**service-failed**"}
85==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
85==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
82==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
90==>|"SpecificationPropertyAssignment"|91
92@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
51==>|"resource [Catalog Resource]"|92
93@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
92==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
93==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*Property Type*
**producedGuard**"}
92==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
95==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*produced Guard*
**service-failed**"}
95==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
95==>|"SpecificationPropertyAssignment"|98
99@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
95==>|"SpecificationPropertyAssignment"|99
100@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
92==>|"SpecificationPropertyAssignment"|100
101@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
92==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
102==>|"SpecificationPropertyAssignment"|103
104@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
51==>|"resource [Uncatalog Resource]"|104
105@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
104==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
105==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*Property Type*
**producedGuard**"}
104==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*produced Guard*
**service-failed**"}
107==>|"SpecificationPropertyAssignment"|108
109@{ shape: hex, label: "*produced Guard*
**missing-template**"}
107==>|"SpecificationPropertyAssignment"|109
110@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
107==>|"SpecificationPropertyAssignment"|110
111@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
107==>|"SpecificationPropertyAssignment"|111
112@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
104==>|"SpecificationPropertyAssignment"|112
113@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
112==>|"SpecificationPropertyAssignment"|113
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 113 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#000000, fill:#40E0D0, stroke:#000000
style 93 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 14 color:#000000, fill:#40E0D0, stroke:#000000
style 15 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 26 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 37 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 38 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#000000, fill:#40E0D0, stroke:#000000
style 41 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 47 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 50 color:#000000, fill:#40E0D0, stroke:#000000
style 51 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 52 color:#000000, fill:#40E0D0, stroke:#000000
style 53 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 54 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 67 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 68 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 73 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 101 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#000000, fill:#40E0D0, stroke:#000000
style 105 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 107 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#000000, fill:#40E0D0, stroke:#000000
style 109 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 83 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
