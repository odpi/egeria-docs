```mermaid
---
title: Technology Report for - File System Directory [d1986b2f-cc82-4a5a-9e9a-559ec9e98edc]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: hex, label: "*Technology Type*
**File System Directory**"}
2@{ shape: hex, label: "*Technology Type*
**Catalog Templates**"}
1==>2
3@{ shape: card, label: "*File Folder*
**File System Directory template**"}
2==>|"catalog templates"|3
4@{ shape: hex, label: "*Property Type*
**placeholderProperty**"}
3==>|"SpecificationPropertyAssignment"|4
5@{ shape: hex, label: "*placeholder Property*
**fileSystemName**"}
4==>|"SpecificationPropertyAssignment"|5
6@{ shape: hex, label: "*placeholder Property*
**directoryPathName**"}
4==>|"SpecificationPropertyAssignment"|6
7@{ shape: hex, label: "*placeholder Property*
**directoryName**"}
4==>|"SpecificationPropertyAssignment"|7
8@{ shape: hex, label: "*placeholder Property*
**deployedImplementationType**"}
4==>|"SpecificationPropertyAssignment"|8
9@{ shape: hex, label: "*placeholder Property*
**description**"}
4==>|"SpecificationPropertyAssignment"|9
10@{ shape: hex, label: "*placeholder Property*
**directoryAddress**"}
4==>|"SpecificationPropertyAssignment"|10
11@{ shape: hex, label: "*placeholder Property*
**versionIdentifier**"}
4==>|"SpecificationPropertyAssignment"|11
12@{ shape: hex, label: "*Technology Type*
**Governance Action Processes**"}
1==>12
13@{ shape: processes, label: "*Surveying Action Process*
**Survey Resource**"}
12==>|"governance action process [Survey Resource]"|13
14@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
13==>|"SpecificationPropertyAssignment"|14
15@{ shape: hex, label: "*produced Annotation Type*
**Profile Asset Types**"}
14==>|"SpecificationPropertyAssignment"|15
16@{ shape: hex, label: "*produced Annotation Type*
**Capture File Counts**"}
14==>|"SpecificationPropertyAssignment"|16
17@{ shape: hex, label: "*produced Annotation Type*
**Profile File Names to External Log**"}
14==>|"SpecificationPropertyAssignment"|17
18@{ shape: hex, label: "*produced Annotation Type*
**Profile Deployed Implementation Types**"}
14==>|"SpecificationPropertyAssignment"|18
19@{ shape: hex, label: "*produced Annotation Type*
**Missing File Reference Data**"}
14==>|"SpecificationPropertyAssignment"|19
20@{ shape: hex, label: "*produced Annotation Type*
**Inaccessible files**"}
14==>|"SpecificationPropertyAssignment"|20
21@{ shape: hex, label: "*produced Annotation Type*
**Profile File Types**"}
14==>|"SpecificationPropertyAssignment"|21
22@{ shape: hex, label: "*produced Annotation Type*
**Profile File Extensions**"}
14==>|"SpecificationPropertyAssignment"|22
23@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
13==>|"SpecificationPropertyAssignment"|23
24@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
23==>|"SpecificationPropertyAssignment"|24
25@{ shape: hex, label: "*supported Request Parameter*
**directoryPathName**"}
23==>|"SpecificationPropertyAssignment"|25
26@{ shape: hex, label: "*supported Request Parameter*
**directoryAddress**"}
23==>|"SpecificationPropertyAssignment"|26
27@{ shape: hex, label: "*supported Request Parameter*
**deployedImplementationType**"}
23==>|"SpecificationPropertyAssignment"|27
28@{ shape: hex, label: "*supported Request Parameter*
**directoryName**"}
23==>|"SpecificationPropertyAssignment"|28
29@{ shape: hex, label: "*supported Request Parameter*
**description**"}
23==>|"SpecificationPropertyAssignment"|29
30@{ shape: hex, label: "*supported Request Parameter*
**fileSystemName**"}
23==>|"SpecificationPropertyAssignment"|30
31@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
23==>|"SpecificationPropertyAssignment"|31
32@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
13==>|"SpecificationPropertyAssignment"|32
33@{ shape: hex, label: "*supported Analysis Step*
**Produce Actions**"}
32==>|"SpecificationPropertyAssignment"|33
34@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
32==>|"SpecificationPropertyAssignment"|34
35@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
32==>|"SpecificationPropertyAssignment"|35
36@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
32==>|"SpecificationPropertyAssignment"|36
37@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
12==>|"governance action process [Catalog Resource]"|37
38@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
37==>|"SpecificationPropertyAssignment"|38
39@{ shape: hex, label: "*supported Request Parameter*
**directoryName**"}
38==>|"SpecificationPropertyAssignment"|39
40@{ shape: hex, label: "*supported Request Parameter*
**fileSystemName**"}
38==>|"SpecificationPropertyAssignment"|40
41@{ shape: hex, label: "*supported Request Parameter*
**deployedImplementationType**"}
38==>|"SpecificationPropertyAssignment"|41
42@{ shape: hex, label: "*supported Request Parameter*
**directoryPathName**"}
38==>|"SpecificationPropertyAssignment"|42
43@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
38==>|"SpecificationPropertyAssignment"|43
44@{ shape: hex, label: "*supported Request Parameter*
**directoryAddress**"}
38==>|"SpecificationPropertyAssignment"|44
45@{ shape: hex, label: "*supported Request Parameter*
**description**"}
38==>|"SpecificationPropertyAssignment"|45
46@{ shape: processes, label: "*Cataloguing Action Process*
**Catalog Resource**"}
12==>|"governance action process [Catalog Resource]"|46
47@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
46==>|"SpecificationPropertyAssignment"|47
48@{ shape: hex, label: "*supported Request Parameter*
**directoryPathName**"}
47==>|"SpecificationPropertyAssignment"|48
49@{ shape: hex, label: "*supported Request Parameter*
**versionIdentifier**"}
47==>|"SpecificationPropertyAssignment"|49
50@{ shape: hex, label: "*supported Request Parameter*
**directoryAddress**"}
47==>|"SpecificationPropertyAssignment"|50
51@{ shape: hex, label: "*supported Request Parameter*
**fileSystemName**"}
47==>|"SpecificationPropertyAssignment"|51
52@{ shape: hex, label: "*supported Request Parameter*
**deployedImplementationType**"}
47==>|"SpecificationPropertyAssignment"|52
53@{ shape: hex, label: "*supported Request Parameter*
**directoryName**"}
47==>|"SpecificationPropertyAssignment"|53
54@{ shape: hex, label: "*supported Request Parameter*
**description**"}
47==>|"SpecificationPropertyAssignment"|54
55@{ shape: processes, label: "*Deleting Action Process*
**Catalog Resource**"}
12==>|"governance action process [Catalog Resource]"|55
56@{ shape: hex, label: "*Technology Type*
**Resource List**"}
1==>56
57@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|57
58@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
57==>|"SpecificationPropertyAssignment"|58
59@{ shape: hex, label: "*supported Configuration Property*
**newFileProcessName**"}
58==>|"SpecificationPropertyAssignment"|59
60@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|60
61@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
60==>|"SpecificationPropertyAssignment"|61
62@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
61==>|"SpecificationPropertyAssignment"|62
63@{ shape: hex, label: "*Property Type*
**producedGuard**"}
60==>|"SpecificationPropertyAssignment"|63
64@{ shape: hex, label: "*produced Guard*
**missing-connector**"}
63==>|"SpecificationPropertyAssignment"|64
65@{ shape: hex, label: "*produced Guard*
**service-failed**"}
63==>|"SpecificationPropertyAssignment"|65
66@{ shape: hex, label: "*produced Guard*
**missing-asset**"}
63==>|"SpecificationPropertyAssignment"|66
67@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
63==>|"SpecificationPropertyAssignment"|67
68@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
60==>|"SpecificationPropertyAssignment"|68
69@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
68==>|"SpecificationPropertyAssignment"|69
70@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
60==>|"SpecificationPropertyAssignment"|70
71@{ shape: hex, label: "*supported Action Target*
**integrationConnector**"}
70==>|"SpecificationPropertyAssignment"|71
72@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
56==>|"resource [Survey Resource]"|72
73@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
72==>|"SpecificationPropertyAssignment"|73
74@{ shape: hex, label: "*produced Annotation Type*
**Profile Asset Types**"}
73==>|"SpecificationPropertyAssignment"|74
75@{ shape: hex, label: "*produced Annotation Type*
**Capture File Counts**"}
73==>|"SpecificationPropertyAssignment"|75
76@{ shape: hex, label: "*produced Annotation Type*
**Profile File Extensions**"}
73==>|"SpecificationPropertyAssignment"|76
77@{ shape: hex, label: "*produced Annotation Type*
**Profile File Types**"}
73==>|"SpecificationPropertyAssignment"|77
78@{ shape: hex, label: "*produced Annotation Type*
**Inaccessible files**"}
73==>|"SpecificationPropertyAssignment"|78
79@{ shape: hex, label: "*produced Annotation Type*
**Profile File Names to External Log**"}
73==>|"SpecificationPropertyAssignment"|79
80@{ shape: hex, label: "*produced Annotation Type*
**Profile Deployed Implementation Types**"}
73==>|"SpecificationPropertyAssignment"|80
81@{ shape: hex, label: "*produced Annotation Type*
**Missing File Reference Data**"}
73==>|"SpecificationPropertyAssignment"|81
82@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
72==>|"SpecificationPropertyAssignment"|82
83@{ shape: hex, label: "*supported Request Parameter*
**analysisLevel**"}
82==>|"SpecificationPropertyAssignment"|83
84@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
82==>|"SpecificationPropertyAssignment"|84
85@{ shape: hex, label: "*Property Type*
**producedGuard**"}
72==>|"SpecificationPropertyAssignment"|85
86@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
85==>|"SpecificationPropertyAssignment"|86
87@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
85==>|"SpecificationPropertyAssignment"|87
88@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
85==>|"SpecificationPropertyAssignment"|88
89@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
72==>|"SpecificationPropertyAssignment"|89
90@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
89==>|"SpecificationPropertyAssignment"|90
91@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
89==>|"SpecificationPropertyAssignment"|91
92@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
89==>|"SpecificationPropertyAssignment"|92
93@{ shape: hex, label: "*supported Analysis Step*
**Produce Actions**"}
89==>|"SpecificationPropertyAssignment"|93
94@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
72==>|"SpecificationPropertyAssignment"|94
95@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
94==>|"SpecificationPropertyAssignment"|95
96@{ shape: hex, label: "*produced Action Target*
**steward**"}
94==>|"SpecificationPropertyAssignment"|96
97@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
94==>|"SpecificationPropertyAssignment"|97
98@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
72==>|"SpecificationPropertyAssignment"|98
99@{ shape: hex, label: "*supported Action Target*
**fileToSurvey**"}
98==>|"SpecificationPropertyAssignment"|99
100@{ shape: tag-rect, label: "*Governance Action Type*
**Watch Metadata Element**"}
56==>|"resource [Watch Metadata Element]"|100
101@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
100==>|"SpecificationPropertyAssignment"|101
102@{ shape: hex, label: "*supported Request Parameter*
**instanceToMonitor**"}
101==>|"SpecificationPropertyAssignment"|102
103@{ shape: hex, label: "*supported Request Parameter*
**declassifiedElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|103
104@{ shape: hex, label: "*supported Request Parameter*
**newElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|104
105@{ shape: hex, label: "*supported Request Parameter*
**updatedElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|105
106@{ shape: hex, label: "*supported Request Parameter*
**deletedElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|106
107@{ shape: hex, label: "*supported Request Parameter*
**actionTargetNameTwo**"}
101==>|"SpecificationPropertyAssignment"|107
108@{ shape: hex, label: "*supported Request Parameter*
**interestingTypeName**"}
101==>|"SpecificationPropertyAssignment"|108
109@{ shape: hex, label: "*supported Request Parameter*
**classifiedElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|109
110@{ shape: hex, label: "*supported Request Parameter*
**watchedFolderName**"}
101==>|"SpecificationPropertyAssignment"|110
111@{ shape: hex, label: "*supported Request Parameter*
**updatedRelationshipProcessName**"}
101==>|"SpecificationPropertyAssignment"|111
112@{ shape: hex, label: "*supported Request Parameter*
**ChangedProperties**"}
101==>|"SpecificationPropertyAssignment"|112
113@{ shape: hex, label: "*supported Request Parameter*
**newRelationshipProcessName**"}
101==>|"SpecificationPropertyAssignment"|113
114@{ shape: hex, label: "*supported Request Parameter*
**reclassifiedElementProcessName**"}
101==>|"SpecificationPropertyAssignment"|114
115@{ shape: hex, label: "*supported Request Parameter*
**deletedRelationshipProcessName**"}
101==>|"SpecificationPropertyAssignment"|115
116@{ shape: hex, label: "*supported Request Parameter*
**actionTargetName**"}
101==>|"SpecificationPropertyAssignment"|116
117@{ shape: hex, label: "*Property Type*
**producedGuard**"}
100==>|"SpecificationPropertyAssignment"|117
118@{ shape: hex, label: "*produced Guard*
**monitoring-failed**"}
117==>|"SpecificationPropertyAssignment"|118
119@{ shape: hex, label: "*produced Guard*
**monitoring-completed**"}
117==>|"SpecificationPropertyAssignment"|119
120@{ shape: hex, label: "*produced Guard*
**monitoring-invalid**"}
117==>|"SpecificationPropertyAssignment"|120
121@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
100==>|"SpecificationPropertyAssignment"|121
122@{ shape: hex, label: "*produced Action Target*
**instanceToMonitor**"}
121==>|"SpecificationPropertyAssignment"|122
123@{ shape: hex, label: "*produced Action Target*
**notificationType**"}
121==>|"SpecificationPropertyAssignment"|123
124@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
100==>|"SpecificationPropertyAssignment"|124
125@{ shape: hex, label: "*supported Action Target*
**watchedFolder**"}
124==>|"SpecificationPropertyAssignment"|125
126@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
56==>|"resource [Survey Resource]"|126
127@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
126==>|"SpecificationPropertyAssignment"|127
128@{ shape: hex, label: "*produced Annotation Type*
**Profile File Types**"}
127==>|"SpecificationPropertyAssignment"|128
129@{ shape: hex, label: "*produced Annotation Type*
**Profile Asset Types**"}
127==>|"SpecificationPropertyAssignment"|129
130@{ shape: hex, label: "*produced Annotation Type*
**Profile Deployed Implementation Types**"}
127==>|"SpecificationPropertyAssignment"|130
131@{ shape: hex, label: "*produced Annotation Type*
**Profile File Names to External Log**"}
127==>|"SpecificationPropertyAssignment"|131
132@{ shape: hex, label: "*produced Annotation Type*
**Capture File Counts**"}
127==>|"SpecificationPropertyAssignment"|132
133@{ shape: hex, label: "*produced Annotation Type*
**Profile File Extensions**"}
127==>|"SpecificationPropertyAssignment"|133
134@{ shape: hex, label: "*produced Annotation Type*
**Missing File Reference Data**"}
127==>|"SpecificationPropertyAssignment"|134
135@{ shape: hex, label: "*produced Annotation Type*
**Inaccessible files**"}
127==>|"SpecificationPropertyAssignment"|135
136@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
126==>|"SpecificationPropertyAssignment"|136
137@{ shape: hex, label: "*supported Request Parameter*
**analysisLevel**"}
136==>|"SpecificationPropertyAssignment"|137
138@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
136==>|"SpecificationPropertyAssignment"|138
139@{ shape: hex, label: "*Property Type*
**producedGuard**"}
126==>|"SpecificationPropertyAssignment"|139
140@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
139==>|"SpecificationPropertyAssignment"|140
141@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
139==>|"SpecificationPropertyAssignment"|141
142@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
139==>|"SpecificationPropertyAssignment"|142
143@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
126==>|"SpecificationPropertyAssignment"|143
144@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
143==>|"SpecificationPropertyAssignment"|144
145@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
143==>|"SpecificationPropertyAssignment"|145
146@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
143==>|"SpecificationPropertyAssignment"|146
147@{ shape: hex, label: "*supported Analysis Step*
**Produce Actions**"}
143==>|"SpecificationPropertyAssignment"|147
148@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
126==>|"SpecificationPropertyAssignment"|148
149@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
148==>|"SpecificationPropertyAssignment"|149
150@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
148==>|"SpecificationPropertyAssignment"|150
151@{ shape: hex, label: "*produced Action Target*
**steward**"}
148==>|"SpecificationPropertyAssignment"|151
152@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
126==>|"SpecificationPropertyAssignment"|152
153@{ shape: hex, label: "*supported Action Target*
**fileToSurvey**"}
152==>|"SpecificationPropertyAssignment"|153
154@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|154
155@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
154==>|"SpecificationPropertyAssignment"|155
156@{ shape: hex, label: "*supported Configuration Property*
**defaultPublisher**"}
155==>|"SpecificationPropertyAssignment"|156
158@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|158
159@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
158==>|"SpecificationPropertyAssignment"|159
160@{ shape: hex, label: "*supported Configuration Property*
**newFileProcessName**"}
159==>|"SpecificationPropertyAssignment"|160
161@{ shape: tag-rect, label: "*Governance Action Type*
**Uncatalog Resource**"}
56==>|"resource [Uncatalog Resource]"|161
162@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
161==>|"SpecificationPropertyAssignment"|162
163@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
162==>|"SpecificationPropertyAssignment"|163
164@{ shape: hex, label: "*Property Type*
**producedGuard**"}
161==>|"SpecificationPropertyAssignment"|164
165@{ shape: hex, label: "*produced Guard*
**service-failed**"}
164==>|"SpecificationPropertyAssignment"|165
166@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
164==>|"SpecificationPropertyAssignment"|166
167@{ shape: hex, label: "*produced Guard*
**missing-template**"}
164==>|"SpecificationPropertyAssignment"|167
168@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
164==>|"SpecificationPropertyAssignment"|168
169@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
161==>|"SpecificationPropertyAssignment"|169
170@{ shape: hex, label: "*produced Action Target*
**deletedAsset**"}
169==>|"SpecificationPropertyAssignment"|170
171@{ shape: rounded, label: "*Connector Type*
**Configure Connector**"}
56==>|"resource [Configure Connector]"|171
172@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|172
173@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|173
174@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
173==>|"SpecificationPropertyAssignment"|174
175@{ shape: hex, label: "*supported Configuration Property*
**newFileProcessName**"}
174==>|"SpecificationPropertyAssignment"|175
176@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
56==>|"resource [Survey Resource]"|176
177@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
176==>|"SpecificationPropertyAssignment"|177
178@{ shape: hex, label: "*produced Annotation Type*
**Profile Asset Types**"}
177==>|"SpecificationPropertyAssignment"|178
179@{ shape: hex, label: "*produced Annotation Type*
**Profile File Extensions**"}
177==>|"SpecificationPropertyAssignment"|179
180@{ shape: hex, label: "*produced Annotation Type*
**Profile Deployed Implementation Types**"}
177==>|"SpecificationPropertyAssignment"|180
181@{ shape: hex, label: "*produced Annotation Type*
**Profile File Types**"}
177==>|"SpecificationPropertyAssignment"|181
182@{ shape: hex, label: "*produced Annotation Type*
**Missing File Reference Data**"}
177==>|"SpecificationPropertyAssignment"|182
183@{ shape: hex, label: "*produced Annotation Type*
**Profile File Names to External Log**"}
177==>|"SpecificationPropertyAssignment"|183
184@{ shape: hex, label: "*produced Annotation Type*
**Capture File Counts**"}
177==>|"SpecificationPropertyAssignment"|184
185@{ shape: hex, label: "*produced Annotation Type*
**Inaccessible files**"}
177==>|"SpecificationPropertyAssignment"|185
186@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
176==>|"SpecificationPropertyAssignment"|186
187@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
186==>|"SpecificationPropertyAssignment"|187
188@{ shape: hex, label: "*supported Request Parameter*
**analysisLevel**"}
186==>|"SpecificationPropertyAssignment"|188
189@{ shape: hex, label: "*Property Type*
**producedGuard**"}
176==>|"SpecificationPropertyAssignment"|189
190@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
189==>|"SpecificationPropertyAssignment"|190
191@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
189==>|"SpecificationPropertyAssignment"|191
192@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
189==>|"SpecificationPropertyAssignment"|192
193@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
176==>|"SpecificationPropertyAssignment"|193
194@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
193==>|"SpecificationPropertyAssignment"|194
195@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
193==>|"SpecificationPropertyAssignment"|195
196@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
193==>|"SpecificationPropertyAssignment"|196
197@{ shape: hex, label: "*supported Analysis Step*
**Produce Actions**"}
193==>|"SpecificationPropertyAssignment"|197
198@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
176==>|"SpecificationPropertyAssignment"|198
199@{ shape: hex, label: "*supported Action Target*
**fileToSurvey**"}
198==>|"SpecificationPropertyAssignment"|199
200@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
176==>|"SpecificationPropertyAssignment"|200
201@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
200==>|"SpecificationPropertyAssignment"|201
202@{ shape: hex, label: "*produced Action Target*
**steward**"}
200==>|"SpecificationPropertyAssignment"|202
203@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
200==>|"SpecificationPropertyAssignment"|203
204@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|204
205@{ shape: tag-rect, label: "*Governance Action Type*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|205
206@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
205==>|"SpecificationPropertyAssignment"|206
207@{ shape: hex, label: "*supported Request Parameter*
**templateGUID**"}
206==>|"SpecificationPropertyAssignment"|207
208@{ shape: hex, label: "*Property Type*
**producedGuard**"}
205==>|"SpecificationPropertyAssignment"|208
209@{ shape: hex, label: "*produced Guard*
**service-failed**"}
208==>|"SpecificationPropertyAssignment"|209
210@{ shape: hex, label: "*produced Guard*
**set-up-complete**"}
208==>|"SpecificationPropertyAssignment"|210
211@{ shape: hex, label: "*produced Guard*
**delete-complete**"}
208==>|"SpecificationPropertyAssignment"|211
212@{ shape: hex, label: "*produced Guard*
**missing-template**"}
208==>|"SpecificationPropertyAssignment"|212
213@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
205==>|"SpecificationPropertyAssignment"|213
214@{ shape: hex, label: "*produced Action Target*
**newAsset**"}
213==>|"SpecificationPropertyAssignment"|214
215@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|215
216@{ shape: hex, label: "*Property Type*
**supportedConfigurationProperty**"}
215==>|"SpecificationPropertyAssignment"|216
217@{ shape: hex, label: "*supported Configuration Property*
**newFileProcessName**"}
216==>|"SpecificationPropertyAssignment"|217
218@{ shape: tag-rect, label: "*Governance Action Type*
**Survey Resource**"}
56==>|"resource [Survey Resource]"|218
219@{ shape: hex, label: "*Property Type*
**producedAnnotationType**"}
218==>|"SpecificationPropertyAssignment"|219
220@{ shape: hex, label: "*produced Annotation Type*
**Profile Asset Types**"}
219==>|"SpecificationPropertyAssignment"|220
221@{ shape: hex, label: "*produced Annotation Type*
**Capture File Counts**"}
219==>|"SpecificationPropertyAssignment"|221
222@{ shape: hex, label: "*produced Annotation Type*
**Profile File Extensions**"}
219==>|"SpecificationPropertyAssignment"|222
223@{ shape: hex, label: "*produced Annotation Type*
**Profile Deployed Implementation Types**"}
219==>|"SpecificationPropertyAssignment"|223
224@{ shape: hex, label: "*produced Annotation Type*
**Profile File Names to External Log**"}
219==>|"SpecificationPropertyAssignment"|224
225@{ shape: hex, label: "*produced Annotation Type*
**Inaccessible files**"}
219==>|"SpecificationPropertyAssignment"|225
226@{ shape: hex, label: "*produced Annotation Type*
**Profile File Types**"}
219==>|"SpecificationPropertyAssignment"|226
227@{ shape: hex, label: "*produced Annotation Type*
**Missing File Reference Data**"}
219==>|"SpecificationPropertyAssignment"|227
228@{ shape: hex, label: "*Property Type*
**supportedRequestParameter**"}
218==>|"SpecificationPropertyAssignment"|228
229@{ shape: hex, label: "*supported Request Parameter*
**finalAnalysisStep**"}
228==>|"SpecificationPropertyAssignment"|229
230@{ shape: hex, label: "*supported Request Parameter*
**analysisLevel**"}
228==>|"SpecificationPropertyAssignment"|230
231@{ shape: hex, label: "*Property Type*
**producedGuard**"}
218==>|"SpecificationPropertyAssignment"|231
232@{ shape: hex, label: "*produced Guard*
**survey-failed**"}
231==>|"SpecificationPropertyAssignment"|232
233@{ shape: hex, label: "*produced Guard*
**survey-invalid**"}
231==>|"SpecificationPropertyAssignment"|233
234@{ shape: hex, label: "*produced Guard*
**survey-completed**"}
231==>|"SpecificationPropertyAssignment"|234
235@{ shape: hex, label: "*Property Type*
**supportedAnalysisStep**"}
218==>|"SpecificationPropertyAssignment"|235
236@{ shape: hex, label: "*supported Analysis Step*
**Check Asset**"}
235==>|"SpecificationPropertyAssignment"|236
237@{ shape: hex, label: "*supported Analysis Step*
**Produce Inventory**"}
235==>|"SpecificationPropertyAssignment"|237
238@{ shape: hex, label: "*supported Analysis Step*
**Produce Actions**"}
235==>|"SpecificationPropertyAssignment"|238
239@{ shape: hex, label: "*supported Analysis Step*
**Profiling Associated Resources**"}
235==>|"SpecificationPropertyAssignment"|239
240@{ shape: hex, label: "*Property Type*
**producedActionTarget**"}
218==>|"SpecificationPropertyAssignment"|240
241@{ shape: hex, label: "*produced Action Target*
**surveyReport**"}
240==>|"SpecificationPropertyAssignment"|241
242@{ shape: hex, label: "*produced Action Target*
**steward**"}
240==>|"SpecificationPropertyAssignment"|242
243@{ shape: hex, label: "*produced Action Target*
**stewardAction**"}
240==>|"SpecificationPropertyAssignment"|243
244@{ shape: hex, label: "*Property Type*
**supportedActionTarget**"}
218==>|"SpecificationPropertyAssignment"|244
245@{ shape: hex, label: "*supported Action Target*
**fileToSurvey**"}
244==>|"SpecificationPropertyAssignment"|245
246@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|246
247@{ shape: stadium, label: "*Integration Connector*
**Catalog Resource**"}
56==>|"resource [Catalog Resource]"|247
style 230 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 231 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 232 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 233 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 113 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 234 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 114 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 235 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 115 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 236 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 116 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 237 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 117 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 238 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 118 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 239 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 13 color:#000000, fill:#40E0D0, stroke:#000000
style 14 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 15 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 17 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 240 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 241 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 242 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 1 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 122 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 243 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 2 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 123 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 244 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#004563, fill:#b0e0e6, stroke:#004563
style 124 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 245 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 125 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 246 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 126 color:#000000, fill:#40E0D0, stroke:#000000
style 247 color:#000000, fill:#BDB76B, stroke:#004563
style 6 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 127 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 7 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 128 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 129 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 20 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 24 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 130 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 131 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 132 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 133 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 134 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 135 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 136 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 137 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 138 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 139 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
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
style 140 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 141 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 142 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 143 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 144 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 145 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 146 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 147 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 148 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 149 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#000000, fill:#40E0D0, stroke:#000000
style 47 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 150 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 151 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 152 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 153 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 154 color:#000000, fill:#BDB76B, stroke:#004563
style 155 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 156 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 158 color:#000000, fill:#BDB76B, stroke:#004563
style 159 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 54 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 55 color:#000000, fill:#40E0D0, stroke:#000000
style 56 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 57 color:#000000, fill:#BDB76B, stroke:#004563
style 58 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 160 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 161 color:#000000, fill:#40E0D0, stroke:#000000
style 162 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 163 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 164 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 165 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 166 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 167 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 168 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 169 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 60 color:#000000, fill:#40E0D0, stroke:#000000
style 61 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 67 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 68 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 170 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 171 color:#000000, fill:#CCE5FF, stroke:#000000
style 172 color:#000000, fill:#BDB76B, stroke:#004563
style 173 color:#000000, fill:#BDB76B, stroke:#004563
style 174 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 175 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 176 color:#000000, fill:#40E0D0, stroke:#000000
style 177 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 178 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 179 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#000000, fill:#40E0D0, stroke:#000000
style 73 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 180 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 181 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 182 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 183 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 184 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 185 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 186 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 187 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 188 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 189 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 82 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 83 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 190 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 191 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 192 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 193 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 194 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 195 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 196 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 197 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 198 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 199 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 200 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 201 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 202 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 203 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 204 color:#000000, fill:#BDB76B, stroke:#004563
style 205 color:#000000, fill:#40E0D0, stroke:#000000
style 206 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 207 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 208 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 209 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 210 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 211 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 212 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 213 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 214 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 215 color:#000000, fill:#BDB76B, stroke:#004563
style 216 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 217 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 218 color:#000000, fill:#40E0D0, stroke:#000000
style 219 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 220 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#000000, fill:#40E0D0, stroke:#000000
style 221 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 101 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 222 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 223 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 224 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 225 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 226 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 227 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 107 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 228 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 108 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 229 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 109 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
