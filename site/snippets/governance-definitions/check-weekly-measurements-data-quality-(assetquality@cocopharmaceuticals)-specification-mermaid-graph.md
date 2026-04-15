```mermaid
---
title: Specification for - check-weekly-measurements-data-quality (AssetQuality@CocoPharmaceuticals) [7494e350-1478-491a-90c1-e22856a47372]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: tag-rect, label: "*Governance Action Type*
**check-weekly-measurements-data-quality (AssetQuality@CocoPharmaceuticals)**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Angle Validation**"}
2==>3
subgraph 4 [Angle Validation details]
5@{ shape: text, label: "*description:*
**Validate that the angle measured for each leg is within the allowed -90 to +90 degree range.**"}
6@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
7@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
8@{ shape: text, label: "*explanation*
**The measurements are taken on a flat surface so the angle cannot be outside the range shown above.  A negative value means that the hip rotates inwards.  A positive value means that the hip rotates outwards**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*Right  Foot  Angle  In  Range:*
**Is the measured angle between -90 degrees and +90 degrees?  Zero means it is in range.  A negative value indicates the number of rows where it is out of range.**"}
11@{ shape: text, label: "*Left  Foot Angle  In  Range:*
**Is the measured angle between -90 degrees and +90 degrees?  Zero means it is in range.  A negative value indicates the number of rows where it is out of range.**"}
12@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
end
3==>4
13@{ shape: hex, label: "*Specification Property Value*
**Failed To Pass Quality Gate**"}
2==>13
subgraph 14 [Failed To Pass Quality Gate details]
15@{ shape: text, label: "*description:*
**Determine whether the quality checks passed.**"}
16@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
17@{ shape: text, label: "*type Name:*
**RequestForAction**"}
18@{ shape: text, label: "*explanation*
**If all the quality checks passed, then the supplied certification is added to the asset.  If not, this request for action is created and is linked to the failing annotations and asset.**"}
19@{ shape: text, label: "*expression:*
"}
20@{ shape: text, label: "*type Name:*
**RequestForAction**"}
end
13==>14
21@{ shape: hex, label: "*Specification Property Value*
**Date Validation**"}
2==>21
subgraph 22 [Date Validation details]
23@{ shape: text, label: "*description:*
**Validate that the date of the measurement is within the allowed date range.**"}
24@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
25@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
26@{ shape: text, label: "*explanation*
**The clinical trial runs for a specific period.  Therefore the measurements should be dated within this period.**"}
27@{ shape: text, label: "*expression:*
"}
28@{ shape: text, label: "*Date  In  Range:*
**Is the date of the measurement in date for the clinical trial?  Zero means it is in range.  A negative value indicates the number of rows where it is out of range.**"}
29@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
end
21==>22
30@{ shape: hex, label: "*Specification Property Value*
**Schema Validation**"}
2==>30
subgraph 31 [Schema Validation details]
32@{ shape: text, label: "*description:*
**Validate that the structure of the data in the resource matches the schema attached to the asset.**"}
33@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
34@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
35@{ shape: text, label: "*explanation*
**The assumption is that the schema defines the specification for the data.  Any deviation from the schema is an error.**"}
36@{ shape: text, label: "*expression:*
"}
37@{ shape: text, label: "*Matching  Column  Names:*
**Do the column names in the schema match those in the resource.  The order is important. Zero means a perfect match.  A negative value means there are mismatched columns.**"}
38@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
39@{ shape: text, label: "*Matching  Column  Count:*
**Do the number of columns described in the schema match the number of columns in the resource?  Zero means a perfect match.  A negative value means the resource has less columns and a positive value means that the resource has more columns.**"}
end
30==>31
40@{ shape: hex, label: "*Specification Property Value*
**Patient Identifier Validation**"}
2==>40
subgraph 41 [Patient Identifier Validation details]
42@{ shape: text, label: "*description:*
**Validate that the patient identifier is between 1 and 32.**"}
43@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
44@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
45@{ shape: text, label: "*explanation*
**The clinical trial has recruited 32 patients, each is given an identifier number to hide their identity. .**"}
46@{ shape: text, label: "*expression:*
"}
47@{ shape: text, label: "*Patient  Identifier  In  Range:*
**Is the patient identifier valid?  Zero means it is in range.  A negative value indicates the number of rows where it is out of range.**"}
48@{ shape: text, label: "*type Name:*
**QualityAnnotation**"}
end
40==>41
49@{ shape: hex, label: "*Specification Property Assignment*
**producedGuard**"}
1==>49
50@{ shape: hex, label: "*Specification Property Value*
**survey-failed**"}
49==>50
subgraph 51 [survey-failed details]
52@{ shape: text, label: "*description:*
**An unexpected error occurred during the survey process.  The survey report is incomplete.**"}
53@{ shape: text, label: "*completion Status:*
**Failed (The governance action service failed to execute the requested action.)**"}
54@{ shape: text, label: "*completion Status Description:*
**The governance action service failed to execute the requested action.**"}
end
50==>51
55@{ shape: hex, label: "*Specification Property Value*
**missing-schema-type**"}
49==>55
subgraph 56 [missing-schema-type details]
57@{ shape: text, label: "*description:*
**The surveyed asset does not have a schema type attached.  This means the survey is not able to certify that the data is stored in the correct structure.**"}
58@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
59@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
55==>56
60@{ shape: hex, label: "*Specification Property Value*
**data-certified**"}
49==>60
subgraph 61 [data-certified details]
62@{ shape: text, label: "*description:*
**All of the quality checks on the data succeeded.  The data has been certified.**"}
63@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
64@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
60==>61
65@{ shape: hex, label: "*Specification Property Value*
**missing-certification-type**"}
49==>65
subgraph 66 [missing-certification-type details]
67@{ shape: text, label: "*description:*
**The certification type is not supplied in the action targets.  This means the survey is not able to certify the data if it is correct.**"}
68@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
69@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
65==>66
70@{ shape: hex, label: "*Specification Property Value*
**data-not-certified**"}
49==>70
subgraph 71 [data-not-certified details]
72@{ shape: text, label: "*description:*
**One or more of the quality checks on the data failed.  The data has not been certified and a request for action has been raised.**"}
73@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
74@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
70==>71
75@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>75
76@{ shape: hex, label: "*Specification Property Value*
**Schema Validation**"}
75==>76
subgraph 31 [Schema Validation details]
77@{ shape: text, label: "*description:*
**The survey action service is validating that the schema attached to the asset matches the structure of the data stored in the asset.**"}
end
76==>31
78@{ shape: hex, label: "*Specification Property Value*
**Data Validation**"}
75==>78
subgraph 79 [Data Validation details]
80@{ shape: text, label: "*description:*
**The survey action service is validating that the data stored in the resource matches the specification.**"}
end
78==>79
81@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
75==>81
subgraph 82 [Check Asset details]
83@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
81==>82
84@{ shape: hex, label: "*Specification Property Value*
**Produce Exceptions**"}
75==>84
subgraph 85 [Produce Exceptions details]
86@{ shape: text, label: "*description:*
**The survey action service is writing out information about issues that is discovered during its analysis.**"}
end
84==>85
87@{ shape: hex, label: "*Specification Property Value*
**Check Action Targets**"}
75==>87
subgraph 88 [Check Action Targets details]
89@{ shape: text, label: "*description:*
**The survey action service is checking that additional information passed by the action targets is available.**"}
end
87==>88
90@{ shape: hex, label: "*Specification Property Assignment*
**producedActionTarget**"}
1==>90
91@{ shape: hex, label: "*Specification Property Value*
**surveyReport**"}
90==>91
subgraph 92 [surveyReport details]
93@{ shape: text, label: "*description:*
**The survey report created by a survey action service.**"}
94@{ shape: text, label: "*type Name:*
**SurveyReport**"}
95@{ shape: text, label: "*deployed Implementation Type:*
"}
96@{ shape: text, label: "*required:*
**false**"}
end
91==>92
97@{ shape: hex, label: "*Specification Property Value*
**steward**"}
90==>97
subgraph 98 [steward details]
99@{ shape: text, label: "*description:*
**The person, or team who is responsible for setting up the governance metadata associated with .**"}
100@{ shape: text, label: "*type Name:*
**Actor**"}
101@{ shape: text, label: "*deployed Implementation Type:*
"}
102@{ shape: text, label: "*required:*
**false**"}
end
97==>98
103@{ shape: hex, label: "*Specification Property Value*
**stewardAction**"}
90==>103
subgraph 104 [stewardAction details]
105@{ shape: text, label: "*description:*
**To Do element created for the steward.**"}
106@{ shape: text, label: "*type Name:*
**ToDo**"}
107@{ shape: text, label: "*deployed Implementation Type:*
"}
108@{ shape: text, label: "*required:*
**false**"}
end
103==>104
109@{ shape: hex, label: "*Specification Property Assignment*
**supportedActionTarget**"}
1==>109
110@{ shape: hex, label: "*Specification Property Value*
**dataQualityCertificationType**"}
109==>110
subgraph 111 [dataQualityCertificationType details]
112@{ shape: text, label: "*description:*
**The certification type that should be used to certify that data from the hospital conforms to specification.**"}
113@{ shape: text, label: "*type Name:*
**CertificationType**"}
114@{ shape: text, label: "*deployed Implementation Type:*
"}
115@{ shape: text, label: "*required:*
**false**"}
end
110==>111
116@{ shape: hex, label: "*Specification Property Value*
**hospital**"}
109==>116
subgraph 117 [hospital details]
118@{ shape: text, label: "*description:*
**Hospital that will be supplying data for the clinical trial.**"}
119@{ shape: text, label: "*type Name:*
**Organization**"}
120@{ shape: text, label: "*deployed Implementation Type:*
"}
121@{ shape: text, label: "*required:*
**false**"}
end
116==>117
style 88 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 115 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 116 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 90 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 117 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 91 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 118 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 92 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 119 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 93 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 94 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 95 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 96 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 97 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 99 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 14 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 120 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 121 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#40E0D0, stroke:#000000
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 28 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 31 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 32 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 33 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 34 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 35 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 36 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 40 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 41 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 58 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 59 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 61 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 62 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 63 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 66 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 71 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 72 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 73 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 74 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 75 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 76 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 77 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 78 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 79 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 100 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 101 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 102 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 103 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 106 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 80 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 109 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 85 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 86 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
