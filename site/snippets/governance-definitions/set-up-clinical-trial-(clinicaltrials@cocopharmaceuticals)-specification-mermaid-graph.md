```mermaid
---
title: Specification for - set-up-clinical-trial (ClinicalTrials@CocoPharmaceuticals) [23ceab08-f644-49c7-b7f3-95f39fe41c84]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: tag-rect, label: "*Governance Action Type*
**set-up-clinical-trial (ClinicalTrials@CocoPharmaceuticals)**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**dataLakeSchemaTemplateGUID**"}
2==>3
subgraph 4 [dataLakeSchemaTemplateGUID details]
5@{ shape: text, label: "*description:*
**Unique identifier of the template to use when cataloguing the unity catalog schema where the clinical trial results are to be stored.  Also add the placeholders used by this template as request parameters.**"}
6@{ shape: text, label: "*data Type:*
**string**"}
7@{ shape: text, label: "*example:*
**5bf92b0f-3970-41ea-b0a3-aacfbf6fd92e**"}
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
15@{ shape: hex, label: "*Specification Property Assignment*
**producedGuard**"}
1==>15
16@{ shape: hex, label: "*Specification Property Value*
**missing-information**"}
15==>16
subgraph 17 [missing-information details]
18@{ shape: text, label: "*description:*
**One or more of the required request parameters is either not supplied, or an invalid value.**"}
19@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
20@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
16==>17
21@{ shape: hex, label: "*Specification Property Value*
**set-up-complete**"}
15==>21
subgraph 22 [set-up-complete details]
23@{ shape: text, label: "*description:*
**The set up tasks have completed successfully.**"}
24@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
25@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
21==>22
26@{ shape: hex, label: "*Specification Property Value*
**set-up-failed**"}
15==>26
subgraph 27 [set-up-failed details]
28@{ shape: text, label: "*description:*
**An unexpected exception occurred while performing the set up tasks.**"}
29@{ shape: text, label: "*completion Status:*
**Failed (The governance action service failed to execute the requested action.)**"}
30@{ shape: text, label: "*completion Status Description:*
**The governance action service failed to execute the requested action.**"}
end
26==>27
31@{ shape: hex, label: "*Specification Property Assignment*
**supportedActionTarget**"}
1==>31
32@{ shape: hex, label: "*Specification Property Value*
**hospitalCertificationGovernanceActionType**"}
31==>32
subgraph 33 [hospitalCertificationGovernanceActionType details]
34@{ shape: text, label: "*description:*
**The Governance Action Type that implements the hospital certification process.**"}
35@{ shape: text, label: "*type Name:*
**GovernanceActionType**"}
36@{ shape: text, label: "*deployed Implementation Type:*
"}
37@{ shape: text, label: "*required:*
**false**"}
end
32==>33
38@{ shape: hex, label: "*Specification Property Value*
**itProjectManager**"}
31==>38
subgraph 39 [itProjectManager details]
40@{ shape: text, label: "*description:*
**Person responsible for the delivery of the new templates and components for the clinical trial.**"}
41@{ shape: text, label: "*type Name:*
**Actor**"}
42@{ shape: text, label: "*deployed Implementation Type:*
"}
43@{ shape: text, label: "*required:*
**false**"}
end
38==>39
44@{ shape: hex, label: "*Specification Property Value*
**hospitalOnboardingGovernanceActionType**"}
31==>44
subgraph 45 [hospitalOnboardingGovernanceActionType details]
46@{ shape: text, label: "*description:*
**The Governance Action Type that implements the hospital certification process.**"}
47@{ shape: text, label: "*type Name:*
**GovernanceActionType**"}
48@{ shape: text, label: "*deployed Implementation Type:*
"}
49@{ shape: text, label: "*required:*
**false**"}
end
44==>45
50@{ shape: hex, label: "*Specification Property Value*
**hospitalCertificationTypeTemplate**"}
31==>50
subgraph 51 [hospitalCertificationTypeTemplate details]
52@{ shape: text, label: "*description:*
**The template to create the certification type that should be used to certify the hospital.**"}
53@{ shape: text, label: "*type Name:*
**CertificationType**"}
54@{ shape: text, label: "*deployed Implementation Type:*
"}
55@{ shape: text, label: "*required:*
**false**"}
end
50==>51
56@{ shape: hex, label: "*Specification Property Value*
**dataScientist**"}
31==>56
subgraph 57 [dataScientist details]
58@{ shape: text, label: "*description:*
**Person responsible for the analysis of the clinical trial data.**"}
59@{ shape: text, label: "*type Name:*
**Actor**"}
60@{ shape: text, label: "*deployed Implementation Type:*
"}
61@{ shape: text, label: "*required:*
**false**"}
end
56==>57
62@{ shape: hex, label: "*Specification Property Value*
**dataEngineer**"}
31==>62
subgraph 63 [dataEngineer details]
64@{ shape: text, label: "*description:*
**Person responsible for the design of the data stores and templates, plus management of the data pipelines.**"}
65@{ shape: text, label: "*type Name:*
**Actor**"}
66@{ shape: text, label: "*deployed Implementation Type:*
"}
67@{ shape: text, label: "*required:*
**false**"}
end
62==>63
68@{ shape: hex, label: "*Specification Property Value*
**clinicalTrialParentProject**"}
31==>68
subgraph 69 [clinicalTrialParentProject details]
70@{ shape: text, label: "*description:*
**Campaign used to control all clinical trials.**"}
71@{ shape: text, label: "*type Name:*
**Project**"}
72@{ shape: text, label: "*deployed Implementation Type:*
"}
73@{ shape: text, label: "*required:*
**false**"}
end
68==>69
74@{ shape: hex, label: "*Specification Property Value*
**clinicalTrialManager**"}
31==>74
subgraph 75 [clinicalTrialManager details]
76@{ shape: text, label: "*description:*
**The person who manages the relationships and agreements with the hospitals and patients.**"}
77@{ shape: text, label: "*type Name:*
**Actor**"}
78@{ shape: text, label: "*deployed Implementation Type:*
"}
79@{ shape: text, label: "*required:*
**false**"}
end
74==>75
80@{ shape: hex, label: "*Specification Property Value*
**integrationDeveloper**"}
31==>80
subgraph 81 [integrationDeveloper details]
82@{ shape: text, label: "*description:*
**Person building the data quality evaluation components.**"}
83@{ shape: text, label: "*type Name:*
**Actor**"}
84@{ shape: text, label: "*deployed Implementation Type:*
"}
85@{ shape: text, label: "*required:*
**false**"}
end
80==>81
86@{ shape: hex, label: "*Specification Property Value*
**informationSupplyChainTemplate**"}
31==>86
subgraph 87 [informationSupplyChainTemplate details]
88@{ shape: text, label: "*description:*
**The template to create the information supply chain for this clinical trial.**"}
89@{ shape: text, label: "*type Name:*
**InformationSupplyChain**"}
90@{ shape: text, label: "*deployed Implementation Type:*
"}
91@{ shape: text, label: "*required:*
**false**"}
end
86==>87
92@{ shape: hex, label: "*Specification Property Value*
**dataQualityCertificationTypeTemplate**"}
31==>92
subgraph 93 [dataQualityCertificationTypeTemplate details]
94@{ shape: text, label: "*description:*
**The template to create the certification type that should be used to certify that data from the hospital conforms to specification.**"}
95@{ shape: text, label: "*type Name:*
**CertificationType**"}
96@{ shape: text, label: "*deployed Implementation Type:*
"}
97@{ shape: text, label: "*required:*
**false**"}
end
92==>93
98@{ shape: hex, label: "*Specification Property Value*
**setUpDataLakeGovernanceActionType**"}
31==>98
subgraph 99 [setUpDataLakeGovernanceActionType details]
100@{ shape: text, label: "*description:*
**The Governance Action Type that sets up the volume in the data lake catalog.**"}
101@{ shape: text, label: "*type Name:*
**GovernanceActionType**"}
102@{ shape: text, label: "*deployed Implementation Type:*
"}
103@{ shape: text, label: "*required:*
**false**"}
end
98==>99
104@{ shape: hex, label: "*Specification Property Value*
**clinicalTrialOwner**"}
31==>104
subgraph 105 [clinicalTrialOwner details]
106@{ shape: text, label: "*description:*
**The person who is accountable for the correct management of the clinical trial.**"}
107@{ shape: text, label: "*type Name:*
**Actor**"}
108@{ shape: text, label: "*deployed Implementation Type:*
"}
109@{ shape: text, label: "*required:*
**false**"}
end
104==>105
110@{ shape: hex, label: "*Specification Property Value*
**hospitalNominationGovernanceActionType**"}
31==>110
subgraph 111 [hospitalNominationGovernanceActionType details]
112@{ shape: text, label: "*description:*
**The Governance Action Type that tentatively adds a hospital to a clinical trial.**"}
113@{ shape: text, label: "*type Name:*
**GovernanceActionType**"}
114@{ shape: text, label: "*deployed Implementation Type:*
"}
115@{ shape: text, label: "*required:*
**false**"}
end
110==>111
116@{ shape: hex, label: "*Specification Property Value*
**lastUpdateConnector**"}
31==>116
subgraph 117 [lastUpdateConnector details]
118@{ shape: text, label: "*description:*
**Integration connector that maintains the last update date for the volume.**"}
119@{ shape: text, label: "*type Name:*
**IntegrationConnector**"}
120@{ shape: text, label: "*deployed Implementation Type:*
**Integration Connector**"}
121@{ shape: text, label: "*required:*
**false**"}
end
116==>117
122@{ shape: hex, label: "*Specification Property Value*
**landingAreaConnector**"}
31==>122
subgraph 123 [landingAreaConnector details]
124@{ shape: text, label: "*description:*
**Integration connector that maintains the last update date for the volume.**"}
125@{ shape: text, label: "*type Name:*
**IntegrationConnector**"}
126@{ shape: text, label: "*deployed Implementation Type:*
**Integration Connector**"}
127@{ shape: text, label: "*required:*
**false**"}
end
122==>123
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
style 10 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 98 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 99 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 16 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 17 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 120 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 121 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#40E0D0, stroke:#000000
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
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 21 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 22 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 27 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 28 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 29 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 30 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 31 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 32 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 33 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 34 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 35 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 36 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 39 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 41 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 50 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 51 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 52 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 56 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 57 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 58 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 59 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 61 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 71 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 72 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 73 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 74 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 75 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 76 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 77 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 78 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 79 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
