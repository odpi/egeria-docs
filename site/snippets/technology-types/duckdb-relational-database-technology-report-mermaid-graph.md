```mermaid
---
title: Technology Report for - DuckDB Relational Database [07e91e40-adce-4c66-b34d-9d00cba1c783]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**DuckDB Relational Database**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Relational Database*
**DuckDB Relational Database template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**databaseName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**secretsStorePathName**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**databaseDescription**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**secretsCollectionName**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**databasePath**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>11
12@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
11==>|"governance action process [Survey Resource]"|12
13@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
12==>|"SpecificationPropertyAssignment"|13
14@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Sizes**"}
13==>|"SpecificationPropertyAssignment"|14
15@{ shape: hex, label: "*produced Annotation Type*
**Capture Frequent Values for Column**"}
13==>|"SpecificationPropertyAssignment"|15
16@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
13==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*produced Annotation Type*
**Capture Table Sizes for a Database Schema**"}
13==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Schema Measurements**"}
13==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*produced Annotation Type*
**Capture External File Data Source**"}
13==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*produced Annotation Type*
**Capture Attached Data Source**"}
13==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Column Measurements**"}
13==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
13==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Measurements**"}
13==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
13==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
13==>|"SpecificationPropertyAssignment"|25
26@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
12==>|"SpecificationPropertyAssignment"|26
27@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
26==>|"SpecificationPropertyAssignment"|27
28@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
26==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
26==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*supported Request Parameter*
**databasePath**"}
26==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**databaseDescription**"}
26==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
26==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
26==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
12==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
34==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
34==>|"SpecificationPropertyAssignment"|36
37@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
34==>|"SpecificationPropertyAssignment"|37
38@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
11==>|"governance action process [Catalog Resource]"|38
39@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
38==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Request Parameter*
**secretsStorePathName**"}
39==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*supported Request Parameter*
**databaseDescription**"}
39==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Request Parameter*
**databaseName**"}
39==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Request Parameter*
**databasePath**"}
39==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
39==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*supported Request Parameter*
**secretsCollectionName**"}
39==>|"SpecificationPropertyAssignment"|45
46@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
11==>|"governance action process [Catalog Resource]"|46
47@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>47
48@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
47==>|"resource [Catalog Resource]"|48
49@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
48==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*supported Configuration Property*
**canonicalMountPoint**"}
49==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Configuration Property*
**fileSystemName**"}
49==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*supported Configuration Property*
**databaseUserId**"}
49==>|"SpecificationPropertyAssignment"|52
53@{ shape: hex, label: "*supported Configuration Property*
**DuckDBFriendshipGUID**"}
49==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*supported Configuration Property*
**databaseName**"}
49==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*supported Configuration Property*
**databasePath**"}
49==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*supported Configuration Property*
**localMountPoint**"}
49==>|"SpecificationPropertyAssignment"|56
57@{ shape: hex, label: "*supported Configuration Property*
**databasePassword**"}
49==>|"SpecificationPropertyAssignment"|57
58@{ shape: hex, label: "*supported Configuration Property*
**attachStatements**"}
49==>|"SpecificationPropertyAssignment"|58
59@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
47==>|"resource [Catalog Resource]"|59
60@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
59==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
60==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*Property Type*
**producedGuard**"}
59==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*produced Guard*
**service-failed**"}
62==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*produced Guard*
**missing-template**"}
62==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
62==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
62==>|"SpecificationPropertyAssignment"|66
67@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
59==>|"SpecificationPropertyAssignment"|67
68@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
67==>|"SpecificationPropertyAssignment"|68
69@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
47==>|"resource [Survey Resource]"|69
70@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
69==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Measurements**"}
70==>|"SpecificationPropertyAssignment"|71
72@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
70==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
70==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*produced Annotation Type*
**Capture Frequent Values for Column**"}
70==>|"SpecificationPropertyAssignment"|74
75@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Measurements**"}
70==>|"SpecificationPropertyAssignment"|75
76@{ shape: hex, label: "*produced Annotation Type*
**Capture Attached Data Source**"}
70==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Column Measurements**"}
70==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Table Sizes**"}
70==>|"SpecificationPropertyAssignment"|78
79@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
70==>|"SpecificationPropertyAssignment"|79
80@{ shape: hex, label: "*produced Annotation Type*
**Capture External File Data Source**"}
70==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*produced Annotation Type*
**Capture Table Sizes for a Database Schema**"}
70==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*produced Annotation Type*
**Capture Database Schema Measurements**"}
70==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
69==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
83==>|"SpecificationPropertyAssignment"|84
85@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
83==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
83==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*Property Type*
**producedGuard**"}
69==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
87==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
87==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
87==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
69==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
91==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
91==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
91==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
69==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*supported Action Target*
**duckdbDatabase**"}
95==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
69==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
97==>|"SpecificationPropertyAssignment"|98
99@{ shape: hex, label: "*produced Action Target*
**steward**"}
97==>|"SpecificationPropertyAssignment"|99
100@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
97==>|"SpecificationPropertyAssignment"|100
101@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
47==>|"resource [Uncatalog Resource]"|101
102@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
101==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
102==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*Property Type*
**producedGuard**"}
101==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
104==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*produced Guard*
**missing-template**"}
104==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
104==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*produced Guard*
**service-failed**"}
104==>|"SpecificationPropertyAssignment"|108
109@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
101==>|"SpecificationPropertyAssignment"|109
110@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
109==>|"SpecificationPropertyAssignment"|110
111@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
47==>|"resource [Catalog Resource]"|111
112@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
111==>|"SpecificationPropertyAssignment"|112
113@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
112==>|"SpecificationPropertyAssignment"|113
114@{ shape: hex, label: "*Property Type*
**producedGuard**"}
111==>|"SpecificationPropertyAssignment"|114
115@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
114==>|"SpecificationPropertyAssignment"|115
116@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
114==>|"SpecificationPropertyAssignment"|116
117@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
114==>|"SpecificationPropertyAssignment"|117
118@{ shape: hex, label: "*produced Guard*
**service-failed**"}
114==>|"SpecificationPropertyAssignment"|118
119@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
111==>|"SpecificationPropertyAssignment"|119
120@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
119==>|"SpecificationPropertyAssignment"|120
121@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
111==>|"SpecificationPropertyAssignment"|121
122@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
121==>|"SpecificationPropertyAssignment"|122
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 111 color:#000000, fill:#40E0D0, stroke:#000000
style 112 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 113 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 114 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 115 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 116 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 118 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#000000, fill:#40E0D0, stroke:#000000
style 13 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 14 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 15 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 17 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 1 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 122 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 34 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 38 color:#000000, fill:#40E0D0, stroke:#000000
style 39 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#000000, fill:#40E0D0, stroke:#000000
style 47 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 48 color:#000000, fill:#BDB76B, stroke:#004563
style 49 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 54 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 59 color:#000000, fill:#40E0D0, stroke:#000000
style 60 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 61 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 62 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 67 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 68 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 69 color:#000000, fill:#40E0D0, stroke:#000000
style 70 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 73 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 101 color:#000000, fill:#40E0D0, stroke:#000000
style 102 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 107 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 109 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 83 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
```
