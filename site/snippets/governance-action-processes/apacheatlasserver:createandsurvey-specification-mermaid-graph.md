```mermaid
---
title: Specification for - ApacheAtlasServer:CreateAndSurvey [82fc3daa-acfc-42c5-88b7-6522b3948949]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**ApacheAtlasServer:CreateAndSurvey**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Entity Types By Business Metadata**"}
2==>3
subgraph 4 [Apache Atlas Attached Entity Types By Business Metadata details]
5@{ shape: text, label: "*description:*
**Count of entities where this type of business metadata properties are attached, organized by entity type.**"}
6@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
7@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
8@{ shape: text, label: "*explanation*
**Entities may optionally have business metadata properties attached to them.**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
3==>4
11@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Entity Type Pairs**"}
2==>11
subgraph 12 [Apache Atlas Attached Entity Type Pairs details]
13@{ shape: text, label: "*description:*
**Count of entity type pairs for this type of relationship.**"}
14@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
15@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
16@{ shape: text, label: "*explanation*
**Entities are linked together using relationships.  There are different types of relationships. These are the entity types is attached to both ends of this relationship type.**"}
17@{ shape: text, label: "*expression:*
"}
18@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
11==>12
19@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas End 1 Attached Relationship Types**"}
2==>19
subgraph 20 [Apache Atlas End 1 Attached Relationship Types details]
21@{ shape: text, label: "*description:*
**Count of different types of relationships attached to this type of entity at End 1.**"}
22@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
23@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
24@{ shape: text, label: "*explanation*
**Entities are linked together using relationships.  These are the relationships where this entity type is attached to end 1 of the relationship type.**"}
25@{ shape: text, label: "*expression:*
"}
26@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
19==>20
27@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas End 2 Attached Relationship Types**"}
2==>27
subgraph 28 [Apache Atlas End 2 Attached Relationship Types details]
29@{ shape: text, label: "*description:*
**Count of different types of relationships attached to this type of entity at End 2.**"}
30@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
31@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
32@{ shape: text, label: "*explanation*
**Entities are linked together using relationships.  These are the relationships where this entity type is attached to end 2 of the relationship type.**"}
33@{ shape: text, label: "*expression:*
"}
34@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
27==>28
35@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Business Metadata Types**"}
2==>35
subgraph 36 [Apache Atlas Attached Business Metadata Types details]
37@{ shape: text, label: "*description:*
**Count of the different types of business metadata properties attached to this type of entity.**"}
38@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
39@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
40@{ shape: text, label: "*explanation*
**Entities may optionally have business metadata properties attached to them.**"}
41@{ shape: text, label: "*expression:*
"}
42@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
35==>36
43@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached End 2 Entity Types**"}
2==>43
subgraph 44 [Apache Atlas Attached End 2 Entity Types details]
45@{ shape: text, label: "*description:*
**Count of entity types attached at end 2 of this type of relationship.**"}
46@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
47@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
48@{ shape: text, label: "*explanation*
**Entities are linked together using relationships.  There are different types of relationships. These are the entity types attached to end 1 of this relationship type.**"}
49@{ shape: text, label: "*expression:*
"}
50@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
43==>44
51@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Classification Types**"}
2==>51
subgraph 52 [Apache Atlas Attached Classification Types details]
53@{ shape: text, label: "*description:*
**Count of classification types attached to this type of entity.**"}
54@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
55@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
56@{ shape: text, label: "*explanation*
**Classifications are used to group entities with similar characteristics together.**"}
57@{ shape: text, label: "*expression:*
"}
58@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
51==>52
59@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Server Metrics**"}
2==>59
subgraph 60 [Apache Atlas Server Metrics details]
61@{ shape: text, label: "*description:*
**Metrics maintained by Apache Atlas.**"}
62@{ shape: text, label: "*analysis Step:*
**Measure Resource**"}
63@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
64@{ shape: text, label: "*explanation*
**These metrics are extracted through the Apache Atlas REST API.**"}
65@{ shape: text, label: "*expression:*
"}
66@{ shape: text, label: "*business Metadata Defs:*
**Number of business metadata type definitions (BusinessMetadataDefs) defined in the Apache Atlas server.**"}
67@{ shape: text, label: "*entity Defs:*
**Number of entity type definitions (EntityDefs) defined in the Apache Atlas server.**"}
68@{ shape: text, label: "*classification Count:*
**Number of tags (classifications) attached to entities stored in the Apache Atlas server.**"}
69@{ shape: text, label: "*classification Defs:*
**Number of classification type definitions (ClassificationDefs) defined in the Apache Atlas server.**"}
70@{ shape: text, label: "*entity Instance Count:*
**Number of entities stored in the Apache Atlas server.**"}
71@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
72@{ shape: text, label: "*relationship Defs:*
**Number of relationship type definitions (RelationshipDefs) defined in the Apache Atlas server.**"}
73@{ shape: text, label: "*entity With Subtypes Instance Count:*
**Number of active entity instances stored in the Apache Atlas server for each entity type (with its subtypes included in the count).**"}
74@{ shape: text, label: "*type Unused Count:*
**Number of types that are not used in the Apache Atlas server.**"}
75@{ shape: text, label: "*type Count:*
**Number of types defined in the Apache Atlas server.**"}
76@{ shape: text, label: "*classified Entity Count:*
**Number of entities with tags (classifications) attached in the Apache Atlas server.**"}
end
59==>60
77@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached End 1 Entity Types**"}
2==>77
subgraph 78 [Apache Atlas Attached End 1 Entity Types details]
79@{ shape: text, label: "*description:*
**Count of entity types attached at end 1 of this type of relationship.**"}
80@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
81@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
82@{ shape: text, label: "*explanation*
**Entities are linked together using relationships.  There are different types of relationships. These are the entity types attached to end 1 of this relationship type.**"}
83@{ shape: text, label: "*expression:*
"}
84@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
77==>78
85@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Entity Types By Classification**"}
2==>85
subgraph 86 [Apache Atlas Attached Entity Types By Classification details]
87@{ shape: text, label: "*description:*
**Count of entities by type where this classification is attached, organized by entity type.**"}
88@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
89@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
90@{ shape: text, label: "*explanation*
**Classifications are used to group entities with similar characteristics together.**"}
91@{ shape: text, label: "*expression:*
"}
92@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
85==>86
93@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Attached Labels**"}
2==>93
subgraph 94 [Apache Atlas Attached Labels details]
95@{ shape: text, label: "*description:*
**Count of different types of labels attached to this type of entity.**"}
96@{ shape: text, label: "*analysis Step:*
**Profile Data**"}
97@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
98@{ shape: text, label: "*explanation*
**Entities may optionally have informal labels attached to them.**"}
99@{ shape: text, label: "*expression:*
"}
100@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
93==>94
101@{ shape: hex, label: "*Specification Property Value*
**Apache Atlas Type Analysis**"}
2==>101
subgraph 102 [Apache Atlas Type Analysis details]
103@{ shape: text, label: "*description:*
**Extract the types defined by the Apache Atlas server.**"}
104@{ shape: text, label: "*analysis Step:*
**Schema Extraction**"}
105@{ shape: text, label: "*type Name:*
**SchemaAnalysisAnnotation**"}
106@{ shape: text, label: "*explanation*
**The Apache Atlas types are converted into a graph schema that is attached to the SoftwareServer asset that represents the Apache Atlas server.**"}
107@{ shape: text, label: "*expression:*
"}
108@{ shape: text, label: "*type Name:*
**SchemaAnalysisAnnotation**"}
end
101==>102
109@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>109
110@{ shape: hex, label: "*Specification Property Value*
**secretsCollectionName**"}
109==>110
subgraph 111 [secretsCollectionName details]
112@{ shape: text, label: "*description:*
**The name used to identify the collection of secrets that a particular connector is using.**"}
113@{ shape: text, label: "*data Type:*
**string**"}
114@{ shape: text, label: "*example:*
**local-postgres-db**"}
115@{ shape: text, label: "*required:*
**false**"}
end
110==>111
116@{ shape: hex, label: "*Specification Property Value*
**description**"}
109==>116
subgraph 117 [description details]
118@{ shape: text, label: "*description:*
**The description of the element to help a consumer understand its content and purpose.**"}
119@{ shape: text, label: "*data Type:*
**string**"}
120@{ shape: text, label: "*example:*
**This file contains a week''s worth of patient data for the Teddy Bear Drop Foot clinical trial.**"}
121@{ shape: text, label: "*required:*
**false**"}
end
116==>117
122@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
109==>122
subgraph 123 [versionIdentifier details]
124@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
125@{ shape: text, label: "*data Type:*
**string**"}
126@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
127@{ shape: text, label: "*required:*
**false**"}
end
122==>123
128@{ shape: hex, label: "*Specification Property Value*
**portNumber**"}
109==>128
subgraph 129 [portNumber details]
130@{ shape: text, label: "*description:*
**The number of the port to use to connect to a service.**"}
131@{ shape: text, label: "*data Type:*
**string**"}
132@{ shape: text, label: "*example:*
**1234**"}
133@{ shape: text, label: "*required:*
**false**"}
end
128==>129
134@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
109==>134
subgraph 135 [serverName details]
136@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
137@{ shape: text, label: "*data Type:*
**string**"}
138@{ shape: text, label: "*example:*
**myServer**"}
139@{ shape: text, label: "*required:*
**false**"}
end
134==>135
140@{ shape: hex, label: "*Specification Property Value*
**secretsStorePathName**"}
109==>140
subgraph 141 [secretsStorePathName details]
142@{ shape: text, label: "*description:*
**The full path name to the secrets store file where the secrets collection for this server is located.**"}
143@{ shape: text, label: "*data Type:*
**string**"}
144@{ shape: text, label: "*example:*
**loading-bay/secrets/integration.omsecrets**"}
145@{ shape: text, label: "*required:*
**false**"}
end
140==>141
146@{ shape: hex, label: "*Specification Property Value*
**hostURL**"}
109==>146
subgraph 147 [hostURL details]
148@{ shape: text, label: "*description:*
**The host IP address or domain name of the server with the HTTP protocol prefix.**"}
149@{ shape: text, label: "*data Type:*
**string**"}
150@{ shape: text, label: "*example:*
**https:/ /coconet.com**"}
151@{ shape: text, label: "*required:*
**false**"}
end
146==>147
152@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>152
153@{ shape: hex, label: "*Specification Property Value*
**Profile Data**"}
152==>153
subgraph 154 [Profile Data details]
155@{ shape: text, label: "*description:*
**The survey action service is profiling the data associated with the resource.**"}
end
153==>154
156@{ shape: hex, label: "*Specification Property Value*
**Schema Extraction**"}
152==>156
subgraph 157 [Schema Extraction details]
158@{ shape: text, label: "*description:*
**The survey action service is extracting the schema from the resource.**"}
end
156==>157
159@{ shape: hex, label: "*Specification Property Value*
**Measure Resource**"}
152==>159
subgraph 160 [Measure Resource details]
161@{ shape: text, label: "*description:*
**The survey action service is taking measurements from the resource.**"}
end
159==>160
162@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
152==>162
subgraph 163 [Check Asset details]
164@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
162==>163
style 88 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 115 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 116 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 118 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 92 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 119 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 95 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 96 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 97 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 98 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 120 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 121 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 122 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 123 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 124 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 125 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 126 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 127 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 128 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 129 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 130 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 131 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 132 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 133 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 134 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 135 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 136 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 137 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 138 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 139 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 31 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 32 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 33 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 34 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 140 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 141 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 142 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 143 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 144 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 145 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 146 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 147 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 148 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 149 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 40 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 150 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 151 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 152 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 153 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 154 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 155 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 156 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 157 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 158 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 159 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 50 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 56 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 57 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 58 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 59 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 160 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 161 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 162 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 163 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 164 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 70 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 71 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 72 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 73 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 74 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 75 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 76 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 77 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 78 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 79 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 100 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 101 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 103 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 104 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 105 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 106 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 80 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 109 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 85 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
