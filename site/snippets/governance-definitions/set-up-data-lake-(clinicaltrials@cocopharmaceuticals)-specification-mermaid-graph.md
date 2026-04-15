```mermaid
---
title: Specification for - set-up-data-lake (ClinicalTrials@CocoPharmaceuticals) [4c33571b-043b-4fba-9b4f-ada7cd8910d3]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: tag-rect, label: "*Governance Action Type*
**set-up-data-lake (ClinicalTrials@CocoPharmaceuticals)**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**secretsCollectionName**"}
2==>3
subgraph 4 [secretsCollectionName details]
5@{ shape: text, label: "*description:*
**The name used to identify the collection of secrets that a particular connector is using.**"}
6@{ shape: text, label: "*data Type:*
**string**"}
7@{ shape: text, label: "*example:*
**local-postgres-db**"}
8@{ shape: text, label: "*required:*
**false**"}
end
3==>4
9@{ shape: hex, label: "*Specification Property Value*
**dataLakeVolumeTemplateGUID**"}
2==>9
subgraph 10 [dataLakeVolumeTemplateGUID details]
11@{ shape: text, label: "*description:*
**Unique identifier of the template to use when cataloguing the directory where the weekly measurements results are to be stored.  Also add the placeholders used by this template as request parameters.**"}
12@{ shape: text, label: "*data Type:*
**string**"}
13@{ shape: text, label: "*example:*
**92d2d2dc-0798-41f0-9512-b10548d312b7**"}
14@{ shape: text, label: "*required:*
**false**"}
end
9==>10
15@{ shape: hex, label: "*Specification Property Value*
**validatedWeeklyFilesDataSetName**"}
2==>15
subgraph 16 [validatedWeeklyFilesDataSetName details]
17@{ shape: text, label: "*description:*
**Name of the data set that will list the files that have been certified.**"}
18@{ shape: text, label: "*data Type:*
**string**"}
19@{ shape: text, label: "*example:*
**Validated Incoming Weekly Measurements For Teddy Bear Drop Foot Clinical Trial**"}
20@{ shape: text, label: "*required:*
**false**"}
end
15==>16
21@{ shape: hex, label: "*Specification Property Value*
**landingAreaFileTemplateGUID**"}
2==>21
subgraph 22 [landingAreaFileTemplateGUID details]
23@{ shape: text, label: "*description:*
**Unique identifier of the template to use in the landing area when onboarding a file from a hospital.  A new, partially filled out template will be created for the hospital.  This template is of type CSVFile.**"}
24@{ shape: text, label: "*data Type:*
**string**"}
25@{ shape: text, label: "*example:*
**5e5ffc97-237d-46c6-95c3-49405035dedc**"}
26@{ shape: text, label: "*required:*
**false**"}
end
21==>22
27@{ shape: hex, label: "*Specification Property Value*
**schemaDescription**"}
2==>27
subgraph 28 [schemaDescription details]
29@{ shape: text, label: "*description:*
**The description of the database schema being catalogued.**"}
30@{ shape: text, label: "*data Type:*
**string**"}
31@{ shape: text, label: "*example:*
"}
32@{ shape: text, label: "*required:*
**false**"}
end
27==>28
33@{ shape: hex, label: "*Specification Property Value*
**validatedWeeklyFilesTemplateGUID**"}
2==>33
subgraph 34 [validatedWeeklyFilesTemplateGUID details]
35@{ shape: text, label: "*description:*
**Unique identifier of the DataFileCollection template used to create the asset that holds the list of validated weekly measurement files.**"}
36@{ shape: text, label: "*data Type:*
**string**"}
37@{ shape: text, label: "*example:*
**409f1f89-00c6-4297-8436-6a25f2b2e2f2**"}
38@{ shape: text, label: "*required:*
**false**"}
end
33==>34
39@{ shape: hex, label: "*Specification Property Value*
**dataLakeSchemaDescription**"}
2==>39
subgraph 40 [dataLakeSchemaDescription details]
41@{ shape: text, label: "*description:*
**Description of the schema to use in the data lake for the clinical trial.**"}
42@{ shape: text, label: "*data Type:*
**string**"}
43@{ shape: text, label: "*example:*
**Example clinical trial used for education and testing of governance procedures.**"}
44@{ shape: text, label: "*required:*
**false**"}
end
39==>40
45@{ shape: hex, label: "*Specification Property Value*
**databaseName**"}
2==>45
subgraph 46 [databaseName details]
47@{ shape: text, label: "*description:*
**The name of the database being catalogued.**"}
48@{ shape: text, label: "*data Type:*
**string**"}
49@{ shape: text, label: "*example:*
**myDatabase**"}
50@{ shape: text, label: "*required:*
**false**"}
end
45==>46
51@{ shape: hex, label: "*Specification Property Value*
**dataLakeSchemaTemplateGUID**"}
2==>51
subgraph 52 [dataLakeSchemaTemplateGUID details]
53@{ shape: text, label: "*description:*
**Unique identifier of the template to use when cataloguing the unity catalog schema where the clinical trial results are to be stored.  Also add the placeholders used by this template as request parameters.**"}
54@{ shape: text, label: "*data Type:*
**string**"}
55@{ shape: text, label: "*example:*
**5bf92b0f-3970-41ea-b0a3-aacfbf6fd92e**"}
56@{ shape: text, label: "*required:*
**false**"}
end
51==>52
57@{ shape: hex, label: "*Specification Property Value*
**dataLakeFileTemplateGUID**"}
2==>57
subgraph 58 [dataLakeFileTemplateGUID details]
59@{ shape: text, label: "*description:*
**Unique identifier of the template to use in the data lake when onboarding a file from a hospital.  A new, partially filled out template will be created for the hospital.  This template is of type CSVFile.**"}
60@{ shape: text, label: "*data Type:*
**string**"}
61@{ shape: text, label: "*example:*
**b2ec7c9d-3462-488a-897d-8e873658dded**"}
62@{ shape: text, label: "*required:*
**false**"}
end
57==>58
63@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
2==>63
subgraph 64 [serverName details]
65@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
66@{ shape: text, label: "*data Type:*
**string**"}
67@{ shape: text, label: "*example:*
**myServer**"}
68@{ shape: text, label: "*required:*
**false**"}
end
63==>64
69@{ shape: hex, label: "*Specification Property Value*
**dataLakeSchemaName**"}
2==>69
subgraph 70 [dataLakeSchemaName details]
71@{ shape: text, label: "*description:*
**Name of the schema to use in the data lake for the clinical trial.**"}
72@{ shape: text, label: "*data Type:*
**string**"}
73@{ shape: text, label: "*example:*
**teddy_bear_drop_foot**"}
74@{ shape: text, label: "*required:*
**false**"}
end
69==>70
75@{ shape: hex, label: "*Specification Property Value*
**portNumber**"}
2==>75
subgraph 76 [portNumber details]
77@{ shape: text, label: "*description:*
**The number of the port to use to connect to a service.**"}
78@{ shape: text, label: "*data Type:*
**string**"}
79@{ shape: text, label: "*example:*
**1234**"}
80@{ shape: text, label: "*required:*
**false**"}
end
75==>76
81@{ shape: hex, label: "*Specification Property Value*
**dataLakeVolumeName**"}
2==>81
subgraph 82 [dataLakeVolumeName details]
83@{ shape: text, label: "*description:*
**Name of the volume in Unity Catalog (UC).**"}
84@{ shape: text, label: "*data Type:*
**string**"}
85@{ shape: text, label: "*example:*
**weekly-measurements**"}
86@{ shape: text, label: "*required:*
**false**"}
end
81==>82
87@{ shape: hex, label: "*Specification Property Value*
**landingAreaDirectoryTemplateGUID**"}
2==>87
subgraph 88 [landingAreaDirectoryTemplateGUID details]
89@{ shape: text, label: "*description:*
**Unique identifier of the template to use when creating the FileFolder for hospital''s landing area files.**"}
90@{ shape: text, label: "*data Type:*
**string**"}
91@{ shape: text, label: "*example:*
**fbdd8efd-1b69-474c-bb6d-0a304b394146**"}
92@{ shape: text, label: "*required:*
**false**"}
end
87==>88
93@{ shape: hex, label: "*Specification Property Value*
**hostIdentifier**"}
2==>93
subgraph 94 [hostIdentifier details]
95@{ shape: text, label: "*description:*
**The host IP address or domain name.**"}
96@{ shape: text, label: "*data Type:*
**string**"}
97@{ shape: text, label: "*example:*
**coconet.com**"}
98@{ shape: text, label: "*required:*
**false**"}
end
93==>94
99@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
2==>99
subgraph 100 [versionIdentifier details]
101@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
102@{ shape: text, label: "*data Type:*
**string**"}
103@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
104@{ shape: text, label: "*required:*
**false**"}
end
99==>100
105@{ shape: hex, label: "*Specification Property Value*
**schemaName**"}
2==>105
subgraph 106 [schemaName details]
107@{ shape: text, label: "*description:*
**The name of the database schema being catalogued.**"}
108@{ shape: text, label: "*data Type:*
**string**"}
109@{ shape: text, label: "*example:*
**MyServer.schema**"}
110@{ shape: text, label: "*required:*
**false**"}
end
105==>106
111@{ shape: hex, label: "*Specification Property Value*
**dataLakeVolumeDirectoryPathName**"}
2==>111
subgraph 112 [dataLakeVolumeDirectoryPathName details]
113@{ shape: text, label: "*description:*
**Path name to store the files for the volume.**"}
114@{ shape: text, label: "*data Type:*
**string**"}
115@{ shape: text, label: "*example:*
**/deployments/data/coco-data-lake/research/clinical-trials/drop-foot/weekly-measurements**"}
116@{ shape: text, label: "*required:*
**false**"}
end
111==>112
117@{ shape: hex, label: "*Specification Property Value*
**secretsStorePathName**"}
2==>117
subgraph 118 [secretsStorePathName details]
119@{ shape: text, label: "*description:*
**The full path name to the secrets store file where the secrets collection for this server is located.**"}
120@{ shape: text, label: "*data Type:*
**string**"}
121@{ shape: text, label: "*example:*
**loading-bay/secrets/integration.omsecrets**"}
122@{ shape: text, label: "*required:*
**false**"}
end
117==>118
123@{ shape: hex, label: "*Specification Property Value*
**dataLakeVolumeDescription**"}
2==>123
subgraph 124 [dataLakeVolumeDescription details]
125@{ shape: text, label: "*description:*
**Short description of the volume in Unity Catalog (UC).**"}
126@{ shape: text, label: "*data Type:*
**string**"}
127@{ shape: text, label: "*example:*
**Weekly measurements for Teddy Bear Drop Foot clinical trial**"}
128@{ shape: text, label: "*required:*
**false**"}
end
123==>124
129@{ shape: hex, label: "*Specification Property Value*
**airflowDAGName**"}
2==>129
subgraph 130 [airflowDAGName details]
131@{ shape: text, label: "*description:*
**Name of the Apache Airflow DAG that copies the data from validated data files into the treatment validation sandbox.**"}
132@{ shape: text, label: "*data Type:*
**string**"}
133@{ shape: text, label: "*example:*
**populateSandbox**"}
134@{ shape: text, label: "*required:*
**false**"}
end
129==>130
135@{ shape: hex, label: "*Specification Property Assignment*
**producedGuard**"}
1==>135
136@{ shape: hex, label: "*Specification Property Value*
**missing-information**"}
135==>136
subgraph 137 [missing-information details]
138@{ shape: text, label: "*description:*
**One or more of the required request parameters is either not supplied, or an invalid value.**"}
139@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
140@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
136==>137
141@{ shape: hex, label: "*Specification Property Value*
**set-up-complete**"}
135==>141
subgraph 142 [set-up-complete details]
143@{ shape: text, label: "*description:*
**The set up tasks have completed successfully.**"}
144@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
145@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
141==>142
146@{ shape: hex, label: "*Specification Property Value*
**set-up-failed**"}
135==>146
subgraph 147 [set-up-failed details]
148@{ shape: text, label: "*description:*
**An unexpected exception occurred while performing the set up tasks.**"}
149@{ shape: text, label: "*completion Status:*
**Failed (The governance action service failed to execute the requested action.)**"}
150@{ shape: text, label: "*completion Status Description:*
**The governance action service failed to execute the requested action.**"}
end
146==>147
151@{ shape: hex, label: "*Specification Property Assignment*
**supportedActionTarget**"}
1==>151
152@{ shape: hex, label: "*Specification Property Value*
**onboardingPipeline**"}
151==>152
subgraph 153 [onboardingPipeline details]
154@{ shape: text, label: "*description:*
**The standard onboarding pipeline that brings data from the landing area to the data lake that is not customized for a project or hospital.**"}
155@{ shape: text, label: "*type Name:*
**GovernanceActionProcess**"}
156@{ shape: text, label: "*deployed Implementation Type:*
"}
157@{ shape: text, label: "*required:*
**false**"}
end
152==>153
158@{ shape: hex, label: "*Specification Property Value*
**onboardHospitalProcess**"}
151==>158
subgraph 159 [onboardHospitalProcess details]
160@{ shape: text, label: "*description:*
**The Governance Action Process that sets up the onboarding pipeline.  SetUpDataLake needs to pass the destination directory onto this process.**"}
161@{ shape: text, label: "*type Name:*
**GovernanceActionProcess**"}
162@{ shape: text, label: "*deployed Implementation Type:*
"}
163@{ shape: text, label: "*required:*
**false**"}
end
158==>159
164@{ shape: hex, label: "*Specification Property Value*
**dataLakeCatalog**"}
151==>164
subgraph 165 [dataLakeCatalog details]
166@{ shape: text, label: "*description:*
**Schema where the weekly measurements volume is to reside.**"}
167@{ shape: text, label: "*type Name:*
**Database**"}
168@{ shape: text, label: "*deployed Implementation Type:*
**Unity Catalog Catalog**"}
169@{ shape: text, label: "*required:*
**false**"}
end
164==>165
170@{ shape: hex, label: "*Specification Property Value*
**dataEngineer**"}
151==>170
subgraph 171 [dataEngineer details]
172@{ shape: text, label: "*description:*
**Person responsible for the design of the data stores and templates, plus management of the data pipelines.**"}
173@{ shape: text, label: "*type Name:*
**Actor**"}
174@{ shape: text, label: "*deployed Implementation Type:*
"}
175@{ shape: text, label: "*required:*
**false**"}
end
170==>171
176@{ shape: hex, label: "*Specification Property Value*
**lastUpdateConnector**"}
151==>176
subgraph 177 [lastUpdateConnector details]
178@{ shape: text, label: "*description:*
**Integration connector that maintains the last update date for the volume.**"}
179@{ shape: text, label: "*type Name:*
**IntegrationConnector**"}
180@{ shape: text, label: "*deployed Implementation Type:*
**Integration Connector**"}
181@{ shape: text, label: "*required:*
**false**"}
end
176==>177
182@{ shape: hex, label: "*Specification Property Value*
**clinicalTrialProject**"}
151==>182
subgraph 183 [clinicalTrialProject details]
184@{ shape: text, label: "*description:*
**Project used to control the clinical trial.**"}
185@{ shape: text, label: "*type Name:*
**Project**"}
186@{ shape: text, label: "*deployed Implementation Type:*
"}
187@{ shape: text, label: "*required:*
**false**"}
end
182==>183
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 115 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 116 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 90 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 118 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 119 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 96 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 97 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 120 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 121 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#40E0D0, stroke:#000000
style 122 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 123 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 124 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 125 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 126 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 127 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 128 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 129 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 130 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 131 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 132 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 133 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 134 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 135 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 136 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 137 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 138 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 139 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 31 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 32 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 36 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 140 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 141 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 142 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 143 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 144 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 145 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 146 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 147 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 148 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 149 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 150 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 151 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 152 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 153 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 154 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 155 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 156 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 157 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 158 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 159 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 50 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 56 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 59 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 160 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 161 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 162 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 163 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 164 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 165 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 166 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 167 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 168 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 169 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 170 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 171 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 172 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 173 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 174 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 175 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 176 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 177 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 178 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 179 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 71 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 72 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 73 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 74 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 78 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 79 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 180 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 181 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 182 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 183 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 184 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 185 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 186 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 187 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 100 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 101 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 102 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 103 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 104 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 80 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 109 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 85 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 86 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
