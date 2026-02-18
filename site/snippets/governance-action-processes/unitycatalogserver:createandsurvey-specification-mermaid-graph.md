```mermaid
---
title: Specification for - UnityCatalogServer:CreateAndSurvey [39dbedae-7753-4d05-9a7a-4a6c80cb02f5]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**UnityCatalogServer:CreateAndSurvey**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Capture Unity Catalog (UC) Server Metrics**"}
2==>3
subgraph 4 [Capture Unity Catalog (UC) Server Metrics details]
5@{ shape: text, label: "*description:*
**Capture summary statistics about a database.**"}
6@{ shape: text, label: "*analysis Step:*
**Measure Resource**"}
7@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
8@{ shape: text, label: "*explanation*
**This annotation retrieves statistics about a Unity Catalog (UC) server and its contents.**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*Number of  Functions:*
**Number of functions found in the surveyed resource.**"}
11@{ shape: text, label: "*Number of  Catalogs:*
**Number of catalogs defined in this server.**"}
12@{ shape: text, label: "*Number of  Models:*
**Number of models found in the surveyed resource.**"}
13@{ shape: text, label: "*Number of  Volumes:*
**Number of volumes found in the surveyed resource.**"}
14@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
end
3==>4
15@{ shape: hex, label: "*Specification Property Value*
**Capture List of Tables**"}
2==>15
subgraph 16 [Capture List of Tables details]
17@{ shape: text, label: "*description:*
**Extract the list of visible tables in the surveyed Unity Catalog (UC) resource (server, catalog or schema).**"}
18@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
19@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
20@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
21@{ shape: text, label: "*expression:*
"}
22@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
15==>16
23@{ shape: hex, label: "*Specification Property Value*
**Log of Unity Catalog (UC) Resources**"}
2==>23
subgraph 24 [Log of Unity Catalog (UC) Resources details]
25@{ shape: text, label: "*description:*
**Log file of resource name, description and deployed implementation type.**"}
26@{ shape: text, label: "*analysis Step:*
**Produce Inventory**"}
27@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
28@{ shape: text, label: "*explanation*
**If resource are missing, check the security permissions of the survey service''s userId.**"}
29@{ shape: text, label: "*expression:*
"}
30@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
23==>24
31@{ shape: hex, label: "*Specification Property Value*
**Capture List of Table Columns**"}
2==>31
subgraph 32 [Capture List of Table Columns details]
33@{ shape: text, label: "*description:*
**Extract the list of visible columns within the tables in the surveyed resource.**"}
34@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
35@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
36@{ shape: text, label: "*explanation*
**Tables listed include their catalog name, schema name and table name.  If tables are missing, check the security permissions of the survey service''s userId.**"}
37@{ shape: text, label: "*expression:*
"}
38@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
31==>32
39@{ shape: hex, label: "*Specification Property Value*
**Capture List of Executable Functions**"}
2==>39
subgraph 40 [Capture List of Executable Functions details]
41@{ shape: text, label: "*description:*
**Extract the list of visible functions in the surveyed resource (manager).**"}
42@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
43@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
44@{ shape: text, label: "*explanation*
**Functions are listed by their full name, with respect to the resource manager.  If functions are missing, check the security permissions of the survey service''s userId.**"}
45@{ shape: text, label: "*expression:*
"}
46@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
39==>40
47@{ shape: hex, label: "*Specification Property Value*
**Capture List of Analytical Models**"}
2==>47
subgraph 48 [Capture List of Analytical Models details]
49@{ shape: text, label: "*description:*
**Extract the list of visible analytical models in the surveyed resource (manager).**"}
50@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
51@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
52@{ shape: text, label: "*explanation*
**Models are listed by their full name, with respect to the resource manager.  If models are missing, check the security permissions of the survey service''s userId.**"}
53@{ shape: text, label: "*expression:*
"}
54@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
47==>48
55@{ shape: hex, label: "*Specification Property Value*
**Capture List of File Volumes**"}
2==>55
subgraph 56 [Capture List of File Volumes details]
57@{ shape: text, label: "*description:*
**Extract the list of visible file-based volumes in the surveyed resource (manager).**"}
58@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
59@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
60@{ shape: text, label: "*explanation*
**Volumes are listed by their full name, with respect to the resource manager.  If volumes are missing, check the security permissions of the survey service''s userId.**"}
61@{ shape: text, label: "*expression:*
"}
62@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
55==>56
63@{ shape: hex, label: "*Specification Property Value*
**Capture List of Schemas**"}
2==>63
subgraph 64 [Capture List of Schemas details]
65@{ shape: text, label: "*description:*
**Extract the list of visible schema in the surveyed resource.**"}
66@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
67@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
68@{ shape: text, label: "*explanation*
**Schemas listed include their catalog name and schema name.  If schemas are missing, check the security permissions of the survey service''s userId.**"}
69@{ shape: text, label: "*expression:*
"}
70@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
63==>64
71@{ shape: hex, label: "*Specification Property Value*
**Capture List of Unity Catalog (UC) Catalogs**"}
2==>71
subgraph 72 [Capture List of Unity Catalog (UC) Catalogs details]
73@{ shape: text, label: "*description:*
**Extract the list of visible catalogs in a Unity Catalog (UC) server.**"}
74@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
75@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
76@{ shape: text, label: "*explanation*
**If catalogs are missing, check the security permissions of the survey service''s userId.**"}
77@{ shape: text, label: "*expression:*
"}
78@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
71==>72
79@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>79
80@{ shape: hex, label: "*Specification Property Value*
**description**"}
79==>80
subgraph 81 [description details]
82@{ shape: text, label: "*description:*
**The description of the element to help a consumer understand its content and purpose.**"}
83@{ shape: text, label: "*data Type:*
**string**"}
84@{ shape: text, label: "*example:*
**This file contains a week''s worth of patient data for the Teddy Bear Drop Foot clinical trial.**"}
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
**hostURL**"}
79==>92
subgraph 93 [hostURL details]
94@{ shape: text, label: "*description:*
**The host IP address or domain name of the server with the HTTP protocol prefix.**"}
95@{ shape: text, label: "*data Type:*
**string**"}
96@{ shape: text, label: "*example:*
**https:/ /coconet.com**"}
97@{ shape: text, label: "*required:*
**false**"}
end
92==>93
98@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
79==>98
subgraph 99 [versionIdentifier details]
100@{ shape: text, label: "*description:*
**The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.**"}
101@{ shape: text, label: "*data Type:*
**string**"}
102@{ shape: text, label: "*example:*
**6.0-SNAPSHOT**"}
103@{ shape: text, label: "*required:*
**false**"}
end
98==>99
104@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
79==>104
subgraph 105 [serverName details]
106@{ shape: text, label: "*description:*
**The name of the server being catalogued.**"}
107@{ shape: text, label: "*data Type:*
**string**"}
108@{ shape: text, label: "*example:*
**myServer**"}
109@{ shape: text, label: "*required:*
**false**"}
end
104==>105
110@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>110
111@{ shape: hex, label: "*Specification Property Value*
**Measure Resource**"}
110==>111
subgraph 112 [Measure Resource details]
113@{ shape: text, label: "*description:*
**The survey action service is taking measurements from the resource.**"}
end
111==>112
114@{ shape: hex, label: "*Specification Property Value*
**Produce Inventory**"}
110==>114
subgraph 115 [Produce Inventory details]
116@{ shape: text, label: "*description:*
**The survey action service is writing an inventory of the contents of the surveyed resource.**"}
end
114==>115
117@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
110==>117
subgraph 118 [Check Asset details]
119@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
117==>118
120@{ shape: hex, label: "*Specification Property Value*
**Profiling Associated Resources**"}
110==>120
subgraph 121 [Profiling Associated Resources details]
122@{ shape: text, label: "*description:*
**The survey action service is profiling other resources associated with the surveyed resource.**"}
end
120==>121
style 88 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 115 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 116 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 90 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 118 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 93 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 94 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 95 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 96 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 97 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 122 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 23 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 24 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 28 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 34 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 35 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 36 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 48 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
style 60 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 70 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
