```mermaid
---
title: Specification for - DataDirectory:CreateAndSurvey [72feba61-2c2f-4c76-b519-1ec1859e3b66]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**DataDirectory:CreateAndSurvey**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedAnnotationType**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**Profile File Names to External Log**"}
2==>3
subgraph 4 [Profile File Names to External Log details]
5@{ shape: text, label: "*description:*
**Iterate through files under a directory (folder) and count the occurrences of each file name.**"}
6@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
7@{ shape: text, label: "*type Name:*
**ResourceProfileLogAnnotation**"}
8@{ shape: text, label: "*explanation*
**Some file names indicate a file of special type/use.  This profile information is likely to be large so it is logged to a CSV File.**"}
9@{ shape: text, label: "*expression:*
"}
10@{ shape: text, label: "*type Name:*
**ResourceProfileLogAnnotation**"}
end
3==>4
11@{ shape: hex, label: "*Specification Property Value*
**Profile File Extensions**"}
2==>11
subgraph 12 [Profile File Extensions details]
13@{ shape: text, label: "*description:*
**Iterate through files under a directory (folder) and count the occurrences of each file extension.**"}
14@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
15@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
16@{ shape: text, label: "*explanation*
**The file extension often provides a hint as to the type of file.**"}
17@{ shape: text, label: "*expression:*
"}
18@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
11==>12
19@{ shape: hex, label: "*Specification Property Value*
**Profile File Types**"}
2==>19
subgraph 20 [Profile File Types details]
21@{ shape: text, label: "*description:*
**Iterate through files under a directory (folder) and count the occurrences of each file type.**"}
22@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
23@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
24@{ shape: text, label: "*explanation*
**The file type is a category of file that describes its use.  The file types are defined as reference data in Egeria.**"}
25@{ shape: text, label: "*expression:*
"}
26@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
19==>20
27@{ shape: hex, label: "*Specification Property Value*
**Profile Asset Types**"}
2==>27
subgraph 28 [Profile Asset Types details]
29@{ shape: text, label: "*description:*
**Iterate through files under a directory (folder) and count each potential asset type if they were to be catalogued in open metadata.**"}
30@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
31@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
32@{ shape: text, label: "*explanation*
**The asset type is an open metadata type.  This annotation identifies the numbers of each type of asset that will be created if the files were catalogued in the open metadata ecosystem.**"}
33@{ shape: text, label: "*expression:*
"}
34@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
27==>28
35@{ shape: hex, label: "*Specification Property Value*
**Capture File Counts**"}
2==>35
subgraph 36 [Capture File Counts details]
37@{ shape: text, label: "*description:*
**Count up the number of files and directories under the surveyed directory that have specific characteristics.**"}
38@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
39@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
40@{ shape: text, label: "*explanation*
**Count the number of directories and files under the starting directory.**"}
41@{ shape: text, label: "*expression:*
"}
42@{ shape: text, label: "*Last file access time:*
**The last time that a file was accessed in the surveyed directory (or any subdirectory).**"}
43@{ shape: text, label: "*Number of files:*
**Number of files found under the surveyed directory (and all subdirectories).**"}
44@{ shape: text, label: "*Number of asset types:*
**Number of different file asset types detected when classifying the files under the surveyed directory.**"}
45@{ shape: text, label: "*Number of subdirectories (folders):*
**Number of subdirectories found under the surveyed directory.**"}
46@{ shape: text, label: "*Last file creation time:*
**The last time that a file was created in the surveyed directory (or any subdirectory).**"}
47@{ shape: text, label: "*Hidden  File  Count:*
**Number of files under the surveyed directory are hidden from standard users.**"}
48@{ shape: text, label: "*type Name:*
**ResourceMeasureAnnotation**"}
49@{ shape: text, label: "*Number of deployed implementation types:*
**Number of different file deployed implementation types detected when classifying the files under the surveyed directory.**"}
50@{ shape: text, label: "*Last file modification time:*
**The last time that a file was updated in the surveyed directory (or any subdirectory).**"}
51@{ shape: text, label: "*Number of inaccessible files:*
**Number of files under the surveyed folder that could not be accessed even to extract their basic properties.**"}
52@{ shape: text, label: "*Number of unique file extensions:*
**Number of different file extensions found under the surveyed directory.**"}
53@{ shape: text, label: "*Readable files/directories:*
**Number of files and directories found under the surveyed directory.**"}
54@{ shape: text, label: "*Number of unique filenames:*
**Number of different file names found under the surveyed directory.**"}
55@{ shape: text, label: "*Symbolic  Link  File  Count:*
**Number of files under the surveyed directory that are symbolic links to files in other locations.**"}
56@{ shape: text, label: "*Number of unclassified files:*
**Number of files under the surveyed directory that could not be classified using the existing reference data.**"}
57@{ shape: text, label: "*Executable files/directories:*
**Number of files and directories found under the surveyed that can be executed.**"}
58@{ shape: text, label: "*Total file size:*
**Total number of bytes from all files found under the surveyed directory (and all subdirectories).**"}
59@{ shape: text, label: "*Writable files/directories:*
**Number of files and directories found under the surveyed directory that can be written to.**"}
60@{ shape: text, label: "*Number of file types:*
**Number of different file types detected when classifying the files under the surveyed directory.**"}
end
35==>36
61@{ shape: hex, label: "*Specification Property Value*
**Profile Deployed Implementation Types**"}
2==>61
subgraph 62 [Profile Deployed Implementation Types details]
63@{ shape: text, label: "*description:*
**Iterate through files under a directory (folder) and count each potential deployed implementation type if they were to be catalogued in open metadata.**"}
64@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
65@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
66@{ shape: text, label: "*explanation*
**The deployed implementation type reflects the technology employed within this resource.  The deployed implementation type is defined as reference data in Egeria.**"}
67@{ shape: text, label: "*expression:*
"}
68@{ shape: text, label: "*type Name:*
**ResourceProfileAnnotation**"}
end
61==>62
69@{ shape: hex, label: "*Specification Property Value*
**Inaccessible files**"}
2==>69
subgraph 70 [Inaccessible files details]
71@{ shape: text, label: "*description:*
**List of files that the survey service was unable to retrieve the basic attributes for.**"}
72@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
73@{ shape: text, label: "*type Name:*
**RequestForAction**"}
74@{ shape: text, label: "*explanation*
**The survey service retrieves the basic attributes of a file as part of its profiling effort.  A file I/O error uses reference data to classify the purpose of files based on their file name.  This annotation captures all of the file names that could not be matched to the reference data. If any of these reveal files that are important to your organization then the reference data should be enhanced to include these files.**"}
75@{ shape: text, label: "*expression:*
"}
76@{ shape: text, label: "*type Name:*
**RequestForAction**"}
end
69==>70
77@{ shape: hex, label: "*Specification Property Value*
**Missing File Reference Data**"}
2==>77
subgraph 78 [Missing File Reference Data details]
79@{ shape: text, label: "*description:*
**List of files that could not be classified using the file reference data.**"}
80@{ shape: text, label: "*analysis Step:*
**Profiling Associated Resources**"}
81@{ shape: text, label: "*type Name:*
**RequestForAction**"}
82@{ shape: text, label: "*explanation*
**The survey service uses reference data to classify the purpose of files based on their file name.  This annotation captures all of the file names that could not be matched to the reference data. If any of these reveal files that are important to your organization then the reference data should be enhanced to include these files.**"}
83@{ shape: text, label: "*expression:*
"}
84@{ shape: text, label: "*type Name:*
**RequestForAction**"}
end
77==>78
85@{ shape: hex, label: "*Specification Property Assignment*
**supportedRequestParameter**"}
1==>85
86@{ shape: hex, label: "*Specification Property Value*
**description**"}
85==>86
subgraph 87 [description details]
88@{ shape: text, label: "*description:*
**The description of the element to help a consumer understand its content and purpose.**"}
89@{ shape: text, label: "*data Type:*
**string**"}
90@{ shape: text, label: "*example:*
**This file contains a week''s worth of patient data for the Teddy Bear Drop Foot clinical trial.**"}
91@{ shape: text, label: "*required:*
**false**"}
end
86==>87
92@{ shape: hex, label: "*Specification Property Value*
**directoryName**"}
85==>92
subgraph 93 [directoryName details]
94@{ shape: text, label: "*description:*
**The name of the leaf directory, without its enclosing directories.**"}
95@{ shape: text, label: "*data Type:*
**string**"}
96@{ shape: text, label: "*example:*
**myFiles**"}
97@{ shape: text, label: "*required:*
**false**"}
end
92==>93
98@{ shape: hex, label: "*Specification Property Value*
**versionIdentifier**"}
85==>98
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
**directoryPathName**"}
85==>104
subgraph 105 [directoryPathName details]
106@{ shape: text, label: "*description:*
**The full path name of the directory including the parent directory names and optional file system name, if applicable**"}
107@{ shape: text, label: "*data Type:*
**string**"}
108@{ shape: text, label: "*example:*
**/a/b/myFiles**"}
109@{ shape: text, label: "*required:*
**false**"}
end
104==>105
110@{ shape: hex, label: "*Specification Property Value*
**fileSystemName**"}
85==>110
subgraph 111 [fileSystemName details]
112@{ shape: text, label: "*description:*
**The unique name for the file system that this file/directory belongs.  It may be a machine name or a URL to a remote file store.**"}
113@{ shape: text, label: "*data Type:*
**string**"}
114@{ shape: text, label: "*example:*
"}
115@{ shape: text, label: "*required:*
**false**"}
end
110==>111
116@{ shape: hex, label: "*Specification Property Assignment*
**supportedAnalysisStep**"}
1==>116
117@{ shape: hex, label: "*Specification Property Value*
**Measure Resource**"}
116==>117
subgraph 118 [Measure Resource details]
119@{ shape: text, label: "*description:*
**The survey action service is taking measurements from the resource.**"}
end
117==>118
120@{ shape: hex, label: "*Specification Property Value*
**Produce Inventory**"}
116==>120
subgraph 121 [Produce Inventory details]
122@{ shape: text, label: "*description:*
**The survey action service is writing an inventory of the contents of the surveyed resource.**"}
end
120==>121
123@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
116==>123
subgraph 124 [Check Asset details]
125@{ shape: text, label: "*description:*
**The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.**"}
end
123==>124
126@{ shape: hex, label: "*Specification Property Value*
**Produce Exceptions**"}
116==>126
subgraph 127 [Produce Exceptions details]
128@{ shape: text, label: "*description:*
**The survey action service is writing out information about issues that is discovered during its analysis.**"}
end
126==>127
style 88 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 89 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 110 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 111 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 112 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 113 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 114 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 115 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 116 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
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
style 120 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 121 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 122 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
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
style 43 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 48 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 49 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 50 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 51 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 52 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 53 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 54 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 55 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 56 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 57 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 58 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 59 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 60 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 61 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 62 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 63 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 64 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 65 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 66 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 67 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 68 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 69 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 70 color:#260d1b, fill:#d98cb6, stroke:#260d1b
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
style 101 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 102 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 103 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 104 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 105 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 106 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 80 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 107 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 81 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 108 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 82 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 109 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 83 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 84 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 85 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 86 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 87 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
