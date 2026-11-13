```mermaid
---
title: Technology Report for - Unity Catalog Server [755dc072-81c4-4b55-a51a-16f6f7f74e6f]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**Unity Catalog Server**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*Software Server*
**Unity Catalog Server template**"}
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
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**hostURL**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**resourceName**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**description**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>11
12@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
11==>|"governance action process [Catalog Resource]"|12
13@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
11==>|"governance action process [Survey Resource]"|13
14@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
13==>|"SpecificationPropertyAssignment"|14
15@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
14==>|"SpecificationPropertyAssignment"|15
16@{ shape: hex, label: "*produced Annotation Type*
**Capture Unity Catalog (UC) Server Metrics**"}
14==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Executable Functions**"}
14==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*produced Annotation Type*
**Log of Unity Catalog (UC) Resources**"}
14==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
14==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Unity Catalog (UC) Catalogs**"}
14==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
14==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*produced Annotation Type*
**Capture List of File Volumes**"}
14==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Analytical Models**"}
14==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
13==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
24==>|"SpecificationPropertyAssignment"|25
26@{ shape: hex, label: "*supported Request Parameter*
**hostURL**"}
24==>|"SpecificationPropertyAssignment"|26
27@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
24==>|"SpecificationPropertyAssignment"|27
28@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
24==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**description**"}
24==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
24==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
24==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
13==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
32==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
32==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
32==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
32==>|"SpecificationPropertyAssignment"|36
37@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
11==>|"governance action process [Catalog Resource]"|37
38@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
37==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Request Parameter*
**resourceName**"}
38==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Request Parameter*
**portNumber**"}
38==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
38==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Request Parameter*
**description**"}
38==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Request Parameter*
**serverName**"}
38==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Request Parameter*
**hostURL**"}
38==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>45
46@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|46
47@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
46==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
47==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*Property Type*
**producedGuard**"}
46==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
49==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
49==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*produced Guard*
**service-failed**"}
49==>|"SpecificationPropertyAssignment"|52
53@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
49==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
46==>|"SpecificationPropertyAssignment"|54
55@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
54==>|"SpecificationPropertyAssignment"|55
56@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
46==>|"SpecificationPropertyAssignment"|56
57@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
56==>|"SpecificationPropertyAssignment"|57
58@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
45==>|"resource [Uncatalog Resource]"|58
59@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
58==>|"SpecificationPropertyAssignment"|59
60@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
59==>|"SpecificationPropertyAssignment"|60
61@{ shape: hex, label: "*Property Type*
**producedGuard**"}
58==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
61==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
61==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*produced Guard*
**missing-template**"}
61==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*produced Guard*
**service-failed**"}
61==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
58==>|"SpecificationPropertyAssignment"|66
67@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
66==>|"SpecificationPropertyAssignment"|67
68@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|68
69@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
68==>|"SpecificationPropertyAssignment"|69
70@{ shape: hex, label: "*supported Configuration Property*
**excludeVolumeNames**"}
69==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*supported Configuration Property*
**excludeSchemaNames**"}
69==>|"SpecificationPropertyAssignment"|71
72@{ shape: hex, label: "*supported Configuration Property*
**excludeFunctionNames**"}
69==>|"SpecificationPropertyAssignment"|72
73@{ shape: hex, label: "*supported Configuration Property*
**excludeTableNames**"}
69==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*supported Configuration Property*
**includeTableNames**"}
69==>|"SpecificationPropertyAssignment"|74
75@{ shape: hex, label: "*supported Configuration Property*
**includeVolumeNames**"}
69==>|"SpecificationPropertyAssignment"|75
76@{ shape: hex, label: "*supported Configuration Property*
**includeFunctionNames**"}
69==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*supported Configuration Property*
**includeSchemaNames**"}
69==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*Property Type*
**supportedTemplate**"}
68==>|"SpecificationPropertyAssignment"|78
79@{ shape: hex, label: "*supported Template*
**Unity Catalog Function**"}
78==>|"SpecificationPropertyAssignment"|79
80@{ shape: hex, label: "*supported Template*
**Unity Catalog Catalog**"}
78==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*supported Template*
**Unity Catalog Schema**"}
78==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*supported Template*
**Unity Catalog Volume**"}
78==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*supported Template*
**Unity Catalog Table**"}
78==>|"SpecificationPropertyAssignment"|83
84@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|84
85@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
84==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*supported Configuration Property*
**excludeCatalogNames**"}
85==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*supported Configuration Property*
**UnityCatalogFriendshipGUID**"}
85==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*supported Configuration Property*
**includeCatalogNames**"}
85==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*Property Type*
**supportedTemplate**"}
84==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*supported Template*
**Unity Catalog Registered Model**"}
89==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*supported Template*
**Unity Catalog Server**"}
89==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*supported Template*
**Unity Catalog Registered Model Version**"}
89==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*supported Template*
**Unity Catalog Schema**"}
89==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*supported Template*
**Unity Catalog Function**"}
89==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*supported Template*
**Databricks Unity Catalog Server**"}
89==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*supported Template*
**Unity Catalog Table**"}
89==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*supported Template*
**Unity Catalog Volume**"}
89==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*supported Template*
**Unity Catalog Catalog**"}
89==>|"SpecificationPropertyAssignment"|98
99@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
45==>|"resource [Survey Resource]"|99
100@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
99==>|"SpecificationPropertyAssignment"|100
101@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Executable Functions**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Table Columns**"}
100==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Tables**"}
100==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Analytical Models**"}
100==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*produced Annotation Type*
**Capture List of File Volumes**"}
100==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Unity Catalog (UC) Catalogs**"}
100==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*produced Annotation Type*
**Log of Unity Catalog (UC) Resources**"}
100==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*produced Annotation Type*
**Capture Unity Catalog (UC) Server Metrics**"}
100==>|"SpecificationPropertyAssignment"|108
109@{ shape: hex, label: "*produced Annotation Type*
**Capture List of Schemas**"}
100==>|"SpecificationPropertyAssignment"|109
110@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
99==>|"SpecificationPropertyAssignment"|110
111@{ shape: hex, label: "*supported Request Parameter*
**excludeSchemaNames**"}
110==>|"SpecificationPropertyAssignment"|111
112@{ shape: hex, label: "*supported Request Parameter*
**includeSchemaNames**"}
110==>|"SpecificationPropertyAssignment"|112
113@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
110==>|"SpecificationPropertyAssignment"|113
114@{ shape: hex, label: "*Property Type*
**producedGuard**"}
99==>|"SpecificationPropertyAssignment"|114
115@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
114==>|"SpecificationPropertyAssignment"|115
116@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
114==>|"SpecificationPropertyAssignment"|116
117@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
114==>|"SpecificationPropertyAssignment"|117
118@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
99==>|"SpecificationPropertyAssignment"|118
119@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
118==>|"SpecificationPropertyAssignment"|119
120@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
118==>|"SpecificationPropertyAssignment"|120
121@{ shape: hex, label: "*supported Analysis Step*
**Measure Resource**"}
118==>|"SpecificationPropertyAssignment"|121
122@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
118==>|"SpecificationPropertyAssignment"|122
123@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
99==>|"SpecificationPropertyAssignment"|123
124@{ shape: hex, label: "*supported Action Target*
**unityCatalogServer**"}
123==>|"SpecificationPropertyAssignment"|124
125@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
99==>|"SpecificationPropertyAssignment"|125
126@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
125==>|"SpecificationPropertyAssignment"|126
127@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
125==>|"SpecificationPropertyAssignment"|127
128@{ shape: hex, label: "*produced Action Target*
**steward**"}
125==>|"SpecificationPropertyAssignment"|128
129@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
45==>|"resource [Catalog Resource]"|129
130@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
129==>|"SpecificationPropertyAssignment"|130
131@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
130==>|"SpecificationPropertyAssignment"|131
132@{ shape: hex, label: "*Property Type*
**producedGuard**"}
129==>|"SpecificationPropertyAssignment"|132
133@{ shape: hex, label: "*produced Guard*
**missing-template**"}
132==>|"SpecificationPropertyAssignment"|133
134@{ shape: hex, label: "*produced Guard*
**service-failed**"}
132==>|"SpecificationPropertyAssignment"|134
135@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
132==>|"SpecificationPropertyAssignment"|135
136@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
132==>|"SpecificationPropertyAssignment"|136
137@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
129==>|"SpecificationPropertyAssignment"|137
138@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
137==>|"SpecificationPropertyAssignment"|138
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 110 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 113 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 114 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 115 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 116 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 118 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 99 color:#000000, fill:#40E0D0, stroke:#000000
style 12 color:#000000, fill:#40E0D0, stroke:#000000
style 13 color:#000000, fill:#40E0D0, stroke:#000000
style 14 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 15 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 17 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 1 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 122 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 2 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 123 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#004563, fill:#b0e0e6, stroke:#004563
style 124 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 125 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 5 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 126 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 6 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 127 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 7 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 128 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 129 color:#000000, fill:#40E0D0, stroke:#000000
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 20 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 24 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 130 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 131 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 132 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 133 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 134 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 135 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 136 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 137 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 138 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#000000, fill:#40E0D0, stroke:#000000
style 38 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 53 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 54 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#000000, fill:#40E0D0, stroke:#000000
style 59 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 67 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 68 color:#000000, fill:#BDB76B, stroke:#004563
style 69 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 73 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 101 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 107 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 109 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 83 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 84 color:#000000, fill:#BDB76B, stroke:#004563
style 85 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
