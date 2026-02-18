```mermaid
---
title: Specification for - PostgreSQLDatabase:CreateAndSurvey [227b5cc0-5750-4d86-a7e4-b2843b7742c8]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**PostgreSQLDatabase:CreateAndSurvey**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Capture Database Schema Measurements**"}
2==>3
subgraph 4 [Capture Database Schema Measurements details]
5@{ shape: text, label: "*description:*
**Capture summary statistics about the database tables in a database schema.**"}
6@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
7@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
8@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about individual tables and columns, and aggregates them into a summary for the schema.**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*Rows  Inserted:*
**Number of rows inserted from any table in the database.**"}
11@{ shape: text, label: "*Rows  Updated:*
**Number of rows updated from any table in the database.**"}
12@{ shape: text, label: "*Rows  Fetched:*
**Number of rows retrieved from any table in the database.**"}
13@{ shape: text, label: "*Data size:*
**Number of stored bytes of data in the surveyed resource.**"}
14@{ shape: text, label: "*Last statistics reset:*
**Last time that the statistics were reset in the database.**"}
15@{ shape: text, label: "*Rows  Deleted:*
**Number of rows deleted from any table in the database.**"}
16@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
17@{ shape: text, label: "*Number of schemas:*
**Number of schemas found in the database.**"}
18@{ shape: text, label: "*Session  Time:*
**The length of time (milliseconds) that the database had at least one open session from an external client.**"}
19@{ shape: text, label: "*Number of columns:*
**Count of all columns in the tables/views.**"}
20@{ shape: text, label: "*Number of materialized views:*
**Count of materialized views in the database.**"}
21@{ shape: text, label: "*Database  Name:*
**Name of the database**"}
22@{ shape: text, label: "*Number of views:*
**Count of views in the database.**"}
23@{ shape: text, label: "*Number of tables:*
**Number of tables found in the database.**"}
24@{ shape: text, label: "*Active  Time:*
**The length of time (milliseconds) that the database was being actively queried.**"}
end
3==>4
25@{ shape: hex, label: "*Specification Property Value*
**Capture Frequent Values for Column**"}
2==>25
subgraph 26 [Capture Frequent Values for Column details]
27@{ shape: text, label: "*description:*
**Capture the most common values stored in the column and their frequencies.**"}
28@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
29@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
30@{ shape: text, label: "*explanation*
**This annotation extracts the statistics maintained by the database.**"}
31@{ shape: text, label: "*expression:*
"}
32@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
25==>26
33@{ shape: hex, label: "*Specification Property Value*
**Capture Database Measurements**"}
2==>33
subgraph 34 [Capture Database Measurements details]
35@{ shape: text, label: "*description:*
**Capture summary statistics about a database.**"}
36@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
37@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
38@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about a database and its usage.**"}
39@{ shape: text, label: "*expression:*
"}
40@{ shape: text, label: "*Rows  Inserted:*
**Number of rows inserted from any table in the database.**"}
41@{ shape: text, label: "*Rows  Updated:*
**Number of rows updated from any table in the database.**"}
42@{ shape: text, label: "*Rows  Fetched:*
**Number of rows retrieved from any table in the database.**"}
43@{ shape: text, label: "*Data size:*
**Number of stored bytes of data in the surveyed resource.**"}
44@{ shape: text, label: "*Last statistics reset:*
**Last time that the statistics were reset in the database.**"}
45@{ shape: text, label: "*Rows  Deleted:*
**Number of rows deleted from any table in the database.**"}
46@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
47@{ shape: text, label: "*Number of schemas:*
**Number of schemas found in the database.**"}
48@{ shape: text, label: "*Session  Time:*
**The length of time (milliseconds) that the database had at least one open session from an external client.**"}
49@{ shape: text, label: "*Number of columns:*
**Count of all columns in the tables/views.**"}
50@{ shape: text, label: "*Number of materialized views:*
**Count of materialized views in the database.**"}
51@{ shape: text, label: "*Database  Name:*
**Name of the database**"}
52@{ shape: text, label: "*Number of views:*
**Count of views in the database.**"}
53@{ shape: text, label: "*Number of tables:*
**Number of tables found in the database.**"}
54@{ shape: text, label: "*Active  Time:*
**The length of time (milliseconds) that the database was being actively queried.**"}
end
33==>34
55@{ shape: hex, label: "*Specification Property Value*
**Capture Database Column Measurements**"}
2==>55
subgraph 56 [Capture Database Column Measurements details]
57@{ shape: text, label: "*description:*
**Capture summary statistics about a database column.**"}
58@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
59@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
60@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about an individual column.**"}
61@{ shape: text, label: "*expression:*
"}
62@{ shape: text, label: "*Average  Column  Width:*
**Average width of the values in this column.**"}
63@{ shape: text, label: "*Most  Common  Values:*
**List of the most common values stored in this column.**"}
64@{ shape: text, label: "*Most  Common  Values  Frequency:*
**The frequency that each of the most common values occur.**"}
65@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
66@{ shape: text, label: "*Column name:*
**Name of the column within the table.**"}
67@{ shape: text, label: "*Column qualified name:*
**Qualified name of the column showing the database name, schema name and table name.**"}
68@{ shape: text, label: "*Column size:*
**Number of stored bytes in the column.**"}
69@{ shape: text, label: "*Not  Null:*
**Is a null value prohibited in this column?**"}
70@{ shape: text, label: "*Number  Of  Distinct  Values:*
**Number of distinct values stored in this column.**"}
71@{ shape: text, label: "*Column data type:*
**Data type of column.**"}
end
55==>56
72@{ shape: hex, label: "*Specification Property Value*
**Capture Database Table Measurements**"}
2==>72
subgraph 73 [Capture Database Table Measurements details]
74@{ shape: text, label: "*description:*
**Capture summary statistics about a database table.**"}
75@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
76@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
77@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about individual columns and aggregates them into a summary for the table.**"}
78@{ shape: text, label: "*expression:*
"}
79@{ shape: text, label: "*Table  Name:*
**Name of table.**"}
80@{ shape: text, label: "*Table  Qualified  Name:*
**Qualified name of table showing the database name and schema name.**"}
81@{ shape: text, label: "*Number  Of  Rows  Deleted:*
**Count of the number of rows deleted from this table since the last statistics reset.**"}
82@{ shape: text, label: "*Has  Rules:*
**Does this table have rules attached?**"}
83@{ shape: text, label: "*Number  Of  Rows  Updated:*
**Count of the number of rows updated in this table since the last statistics reset.**"}
84@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
85@{ shape: text, label: "*Number of columns:*
**Count of columns in the table/view.**"}
86@{ shape: text, label: "*Table  Size:*
**Number of stored bytes in the table.**"}
87@{ shape: text, label: "*Has  Indexes:*
**Is this table indexed?**"}
88@{ shape: text, label: "*Number  Of  Rows  Inserted:*
**Count of the number of rows inserted into this table since the last statistics reset.**"}
89@{ shape: text, label: "*Table  Type:*
**Is this a standard table, view or materialized view?**"}
90@{ shape: text, label: "*Resource  Owner:*
**Who owns this resource?**"}
91@{ shape: text, label: "*Has  Row  Security:*
**Is this table configured for row-based security?**"}
92@{ shape: text, label: "*Has  Triggers:*
**Does this table have triggers attached?**"}
93@{ shape: text, label: "*Query  Definition:*
**Which query, if any, is used to create this view or materialized view?**"}
94@{ shape: text, label: "*Is  Populated:*
**Is this table populated (typically true)?**"}
end
72==>73
95@{ shape: hex, label: "*Specification Property Value*
**Capture List of Tables**"}
2==>95
subgraph 96 [Capture List of Tables details]
97@{ shape: text, label: "*description:*
**Extract the list of visible tables in the surveyed Unity Catalog (UC) resource (server, catalog or schema).**"}
98@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
99@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
100@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
101@{ shape: text, label: "*expression:*
"}
102@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
95==>96
103@{ shape: hex, label: "*Specification Property Value*
**Capture Table Sizes for a Database Schema**"}
2==>103
subgraph 104 [Capture Table Sizes for a Database Schema details]
105@{ shape: text, label: "*description:*
**Extract the sizes of the visible tables in a database schema.**"}
106@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
107@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
108@{ shape: text, label: "*explanation*
**Tables listed include their database name and schema name.  If tables are missing, check the security permissions of the survey service''s database userId.**"}
109@{ shape: text, label: "*expression:*
"}
110@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
103==>104
111@{ shape: hex, label: "*Specification Property Value*
**Capture List of Schemas**"}
2==>111
subgraph 112 [Capture List of Schemas details]
113@{ shape: text, label: "*description:*
**Extract the list of visible schema in the surveyed resource.**"}
114@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
115@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
116@{ shape: text, label: "*explanation*
**Schemas listed include their catalog name and schema name.  If schemas are missing, check the security permissions of the survey service''s userId.**"}
117@{ shape: text, label: "*expression:*
"}
118@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
111==>112
119@{ shape: hex, label: "*Specification Property Value*
**Capture List of Table Columns**"}
2==>119
subgraph 120 [Capture List of Table Columns details]
121@{ shape: text, label: "*description:*
**Extract the list of visible columns within the tables in the surveyed resource.**"}
122@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
123@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
124@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
125@{ shape: text, label: "*expression:*
"}
126@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
119==>120
127@{ shape: hex, label: "*Specification Property Value*
**Capture Database Table Sizes**"}
2==>127
subgraph 128 [Capture Database Table Sizes details]
129@{ shape: text, label: "*description:*
**Extract the sizes of the visible tables in a database.**"}
130@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
131@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
132@{ shape: text, label: "*explanation*
**Tables listed include their database name and schema name.  If tables are missing, check the security permissions of the survey service''s database userId.**"}
133@{ shape: text, label: "*expression:*
"}
134@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
127==>128
135@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>135
136@{ shape: hex, label: "*Specification Property Value*
**databaseName**"}
135==>136
subgraph 137 [databaseName details]
138@{ shape: text, label: "*description:*
**The name of the database being catalogued.**"}
139@{ shape: text, label: "*data Type:*
**string**"}
140@{ shape: text, label: "*example:*
**myDatabase**"}
141@{ shape: text, label: "*required:*
**false**"}
end
136==>137
142@{ shape: hex, label: "*Specification Property Value*
**portNumber**"}
135==>142
subgraph 143 [portNumber details]
144@{ shape: text, label: "*description:*
**The number of the port to use to connect to a service.**"}
145@{ shape: text, label: "*data Type:*
**string**"}
146@{ shape: text, label: "*example:*
**1234**"}
147@{ shape: text, label: "*required:*
**false**"}
end
142==>143
148@{ shape: hex, label: "*Specification Property Value*
**hostIdentifier**"}
135==>148
subgraph 149 [hostIdentifier details]
150@{ shape: text, label: "*description:*
**The host IP address or domain name.**"}
151@{ shape: text, label: "*data Type:*
**string**"}
152@{ shape: text, label: "*example:*
**coconet.com**"}
153@{ shape: text, label: "*required:*
**false**"}
end
148==>149
154@{ shape: hex, label: "*Specification Property Value*
**secretsStorePathName**"}
135==>154
subgraph 155 [secretsStorePathName details]
156@{ shape: text, label: "*description:*
**The full path name to the secrets store file where the secrets collection for this server is located.**"}
157@{ shape: text, label: "*data Type:*
**string**"}
158@{ shape: text, label: "*example:*
**loading-bay/secrets/integration.omsecrets**"}
159@{ shape: text, label: "*required:*
**false**"}
end
154==>155
160@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
135==>160
subgraph 161 [versionIdentifier details]
162@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
163@{ shape: text, label: "*data Type:*
**string**"}
164@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
165@{ shape: text, label: "*required:*
**false**"}
end
160==>161
166@{ shape: hex, label: "*Specification Property Value*
**secretsCollectionName**"}
135==>166
subgraph 167 [secretsCollectionName details]
168@{ shape: text, label: "*description:*
**The name used to identify the collection of secrets that a particular connector is using.**"}
169@{ shape: text, label: "*data Type:*
**string**"}
170@{ shape: text, label: "*example:*
**local-postgres-db**"}
171@{ shape: text, label: "*required:*
**false**"}
end
166==>167
172@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
135==>172
subgraph 173 [serverName details]
174@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
175@{ shape: text, label: "*data Type:*
**string**"}
176@{ shape: text, label: "*example:*
**myServer**"}
177@{ shape: text, label: "*required:*
**false**"}
end
172==>173
178@{ shape: hex, label: "*Specification Property Value*
**databaseDescription**"}
135==>178
subgraph 179 [databaseDescription details]
180@{ shape: text, label: "*description:*
**The description of the database being catalogued.**"}
181@{ shape: text, label: "*data Type:*
**string**"}
182@{ shape: text, label: "*example:*
"}
183@{ shape: text, label: "*required:*
**false**"}
end
178==>179
184@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>184
185@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
184==>185
subgraph 186 [Check Asset details]
187@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
185==>186
188@{ shape: hex, label: "*Specification Property Value*
**Profiling Associated Resources**"}
184==>188
subgraph 189 [Profiling Associated Resources details]
190@{ shape: text, label: "*description:*
**The survey action service is profiling other resources associated with the surveyed resource.**"}
end
188==>189
style 88 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 190 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 115 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 116 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 90 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 117 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 91 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 118 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 92 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 119 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 93 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 94 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 95 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 96 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 97 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 98 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 99 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 122 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 123 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 124 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 125 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 126 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 127 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 128 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 129 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 26 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 27 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 28 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 130 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
style 39 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 140 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 141 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 142 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 143 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 144 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 145 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 146 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 147 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 148 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 149 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 150 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 151 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 152 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 153 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 154 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 155 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 156 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 157 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 158 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 159 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 50 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 51 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 52 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 58 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 59 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 160 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 161 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 162 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 163 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 164 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 165 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 166 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 167 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 168 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 169 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 170 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 171 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 172 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 173 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 174 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 175 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 176 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 177 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 178 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 179 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 71 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 73 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 74 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 75 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 76 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 77 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 78 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 79 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 180 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 181 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 182 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 183 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 184 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 185 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 186 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 187 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 100 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 188 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 101 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 189 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 102 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 106 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 80 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 109 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 85 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 86 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 87 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
