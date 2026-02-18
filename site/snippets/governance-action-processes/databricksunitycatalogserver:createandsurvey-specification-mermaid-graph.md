```mermaid
---
title: Specification for - DatabricksUnityCatalogServer:CreateAndSurvey [f806f64c-56fe-4a9d-a19b-39dd4cc7995e]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**DatabricksUnityCatalogServer:CreateAndSurvey**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Log of Unity Catalog (UC) Resources**"}
2==>3
subgraph 4 [Log of Unity Catalog (UC) Resources details]
5@{ shape: text, label: "*description:*
**Log file of resource name, description and deployed implementation type.**"}
6@{ shape: text, label: "*analysis Step:*
**Produce Inventory**"}
7@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
8@{ shape: text, label: "*explanation*
**If resource are missing, check the security permissions of the survey service''s userId.**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
3==>4
11@{ shape: hex, label: "*Specification Property Value*
**Capture List of Analytical Models**"}
2==>11
subgraph 12 [Capture List of Analytical Models details]
13@{ shape: text, label: "*description:*
**Extract the list of visible analytical models in the surveyed resource (manager).**"}
14@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
15@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
16@{ shape: text, label: "*explanation*
**Models are listed by their full name, with respect to the resource manager.  If models are missing, check the security permissions of the survey service''s userId.**"}
17@{ shape: text, label: "*expression:*
"}
18@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
11==>12
19@{ shape: hex, label: "*Specification Property Value*
**Capture List of File Volumes**"}
2==>19
subgraph 20 [Capture List of File Volumes details]
21@{ shape: text, label: "*description:*
**Extract the list of visible file-based volumes in the surveyed resource (manager).**"}
22@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
23@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
24@{ shape: text, label: "*explanation*
**Volumes are listed by their full name, with respect to the resource manager.  If volumes are missing, check the security permissions of the survey service''s userId.**"}
25@{ shape: text, label: "*expression:*
"}
26@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
19==>20
27@{ shape: hex, label: "*Specification Property Value*
**Capture List of Schemas**"}
2==>27
subgraph 28 [Capture List of Schemas details]
29@{ shape: text, label: "*description:*
**Extract the list of visible schema in the surveyed resource.**"}
30@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
31@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
32@{ shape: text, label: "*explanation*
**Schemas listed include their catalog name and schema name.  If schemas are missing, check the security permissions of the survey service''s userId.**"}
33@{ shape: text, label: "*expression:*
"}
34@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
27==>28
35@{ shape: hex, label: "*Specification Property Value*
**Capture List of Table Columns**"}
2==>35
subgraph 36 [Capture List of Table Columns details]
37@{ shape: text, label: "*description:*
**Extract the list of visible columns within the tables in the surveyed resource.**"}
38@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
39@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
40@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
41@{ shape: text, label: "*expression:*
"}
42@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
35==>36
43@{ shape: hex, label: "*Specification Property Value*
**Capture List of Unity Catalog (UC) Catalogs**"}
2==>43
subgraph 44 [Capture List of Unity Catalog (UC) Catalogs details]
45@{ shape: text, label: "*description:*
**Extract the list of visible catalogs in a Unity Catalog (UC) server.**"}
46@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
47@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
48@{ shape: text, label: "*explanation*
**If catalogs are missing, check the security permissions of the survey service''s userId.**"}
49@{ shape: text, label: "*expression:*
"}
50@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
43==>44
51@{ shape: hex, label: "*Specification Property Value*
**Capture List of Tables**"}
2==>51
subgraph 52 [Capture List of Tables details]
53@{ shape: text, label: "*description:*
**Extract the list of visible tables in the surveyed Unity Catalog (UC) resource (server, catalog or schema).**"}
54@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
55@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
56@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
57@{ shape: text, label: "*expression:*
"}
58@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
51==>52
59@{ shape: hex, label: "*Specification Property Value*
**Capture List of Executable Functions**"}
2==>59
subgraph 60 [Capture List of Executable Functions details]
61@{ shape: text, label: "*description:*
**Extract the list of visible functions in the surveyed resource (manager).**"}
62@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
63@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
64@{ shape: text, label: "*explanation*
**Functions are listed by their full name, with respect to the resource manager.  If functions are missing, check the security permissions of the survey service''s userId.**"}
65@{ shape: text, label: "*expression:*
"}
66@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
59==>60
67@{ shape: hex, label: "*Specification Property Value*
**Capture Unity Catalog (UC) Server Metrics**"}
2==>67
subgraph 68 [Capture Unity Catalog (UC) Server Metrics details]
69@{ shape: text, label: "*description:*
**Capture summary statistics about a database.**"}
70@{ shape: text, label: "*analysis Step:*
**Measure Resource**"}
71@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
72@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about a Unity Catalog (UC) server and its contents.**"}
73@{ shape: text, label: "*expression:*
"}
74@{ shape: text, label: "*Number of  Functions:*
**Number of functions found in the surveyed resource.**"}
75@{ shape: text, label: "*Number of  Catalogs:*
**Number of catalogs defined in this server.**"}
76@{ shape: text, label: "*Number of  Models:*
**Number of models found in the surveyed resource.**"}
77@{ shape: text, label: "*Number of  Volumes:*
**Number of volumes found in the surveyed resource.**"}
78@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
end
67==>68
79@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>79
80@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
79==>80
subgraph 81 [serverName details]
82@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
83@{ shape: text, label: "*data Type:*
**string**"}
84@{ shape: text, label: "*example:*
**myServer**"}
85@{ shape: text, label: "*required:*
**false**"}
end
80==>81
86@{ shape: hex, label: "*Specification Property Value*
**portNumber**"}
79==>86
subgraph 87 [portNumber details]
88@{ shape: text, label: "*description:*
**The number of the port to use to connect to a service.**"}
89@{ shape: text, label: "*data Type:*
**string**"}
90@{ shape: text, label: "*example:*
**1234**"}
91@{ shape: text, label: "*required:*
**false**"}
end
86==>87
92@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
79==>92
subgraph 93 [versionIdentifier details]
94@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
95@{ shape: text, label: "*data Type:*
**string**"}
96@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
97@{ shape: text, label: "*required:*
**false**"}
end
92==>93
98@{ shape: hex, label: "*Specification Property Value*
**hostURL**"}
79==>98
subgraph 99 [hostURL details]
100@{ shape: text, label: "*description:*
**The host IP address or domain name of the server with the HTTP protocol prefix.**"}
101@{ shape: text, label: "*data Type:*
**string**"}
102@{ shape: text, label: "*example:*
**https:/ /coconet.com**"}
103@{ shape: text, label: "*required:*
**false**"}
end
98==>99
104@{ shape: hex, label: "*Specification Property Value*
**secretsCollectionName**"}
79==>104
subgraph 105 [secretsCollectionName details]
106@{ shape: text, label: "*description:*
**The name used to identify the collection of secrets that a particular connector is using.**"}
107@{ shape: text, label: "*data Type:*
**string**"}
108@{ shape: text, label: "*example:*
**local-postgres-db**"}
109@{ shape: text, label: "*required:*
**false**"}
end
104==>105
110@{ shape: hex, label: "*Specification Property Value*
**secretsStorePathName**"}
79==>110
subgraph 111 [secretsStorePathName details]
112@{ shape: text, label: "*description:*
**The full path name to the secrets store file where the secrets collection for this server is located.**"}
113@{ shape: text, label: "*data Type:*
**string**"}
114@{ shape: text, label: "*example:*
**loading-bay/secrets/integration.omsecrets**"}
115@{ shape: text, label: "*required:*
**false**"}
end
110==>111
116@{ shape: hex, label: "*Specification Property Value*
**description**"}
79==>116
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
122@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>122
123@{ shape: hex, label: "*Specification Property Value*
**Profiling Associated Resources**"}
122==>123
subgraph 124 [Profiling Associated Resources details]
125@{ shape: text, label: "*description:*
**The survey action service is profiling other resources associated with the surveyed resource.**"}
end
123==>124
126@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
122==>126
subgraph 127 [Check Asset details]
128@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
126==>127
129@{ shape: hex, label: "*Specification Property Value*
**Produce Inventory**"}
122==>129
subgraph 130 [Produce Inventory details]
131@{ shape: text, label: "*description:*
**The survey action service is writing an inventory of the contents of the surveyed resource.**"}
end
129==>130
132@{ shape: hex, label: "*Specification Property Value*
**Measure Resource**"}
122==>132
subgraph 133 [Measure Resource details]
134@{ shape: text, label: "*description:*
**The survey action service is taking measurements from the resource.**"}
end
132==>133
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
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 95 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 96 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 97 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 122 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 123 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 124 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 125 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 126 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 127 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 128 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
style 130 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 131 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 132 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 133 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 134 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 68 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 69 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 70 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 71 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 72 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 73 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 74 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 75 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 76 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 77 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 78 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 79 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 100 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 101 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 102 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 103 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 80 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 109 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 85 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
