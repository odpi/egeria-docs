```mermaid
---
title: Specification for - Create Daily refresh subscription for Valid Metadata Value Set: sortOrder [cd5e6df8-0ceb-457f-8f05-65383e3206ae]
---
flowchart LR
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: processes, label: "*Governance Action Process*
**Create Daily refresh subscription for Valid Metadata Value Set: sortOrder**"}
2@{ shape: hex, label: "*Specification Property Assignment*
**producedGuard**"}
1==>2
3@{ shape: hex, label: "*Specification Property Value*
**missing-action-target**"}
2==>3
subgraph 4 [missing-action-target details]
5@{ shape: text, label: "*description:*
**The named action target has not been supplied.**"}
6@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
7@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
3==>4
8@{ shape: hex, label: "*Specification Property Value*
**service-failed**"}
2==>8
subgraph 9 [service-failed details]
10@{ shape: text, label: "*description:*
**An unexpected error occurred while the governance service was running.  Messages are logged to the audit log explaining the source of the error.**"}
11@{ shape: text, label: "*completion Status:*
**Failed (The governance action service failed to execute the requested action.)**"}
12@{ shape: text, label: "*completion Status Description:*
**The governance action service failed to execute the requested action.**"}
end
8==>9
13@{ shape: hex, label: "*Specification Property Value*
**missing-request-parameter**"}
2==>13
subgraph 14 [missing-request-parameter details]
15@{ shape: text, label: "*description:*
**The named request parameter has not been supplied.**"}
16@{ shape: text, label: "*completion Status:*
**Invalid (The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).)**"}
17@{ shape: text, label: "*completion Status Description:*
**The governance action service has not performed the requested action because it is not appropriate (for example, a false positive).**"}
end
13==>14
18@{ shape: hex, label: "*Specification Property Value*
**delete-complete**"}
2==>18
subgraph 19 [delete-complete details]
20@{ shape: text, label: "*description:*
**The digital subscription has been deleted.**"}
21@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
22@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
18==>19
23@{ shape: hex, label: "*Specification Property Value*
**set-up-complete**"}
2==>23
subgraph 24 [set-up-complete details]
25@{ shape: text, label: "*description:*
**The new digital subscription has been created.  Its unique identifier (guid) is published in the ''newDigitalSubscription'' action target**"}
26@{ shape: text, label: "*completion Status:*
**Actioned (The governance action service for the governance action has successfully completed processing.)**"}
27@{ shape: text, label: "*completion Status Description:*
**The governance action service for the governance action has successfully completed processing.**"}
end
23==>24
28@{ shape: hex, label: "*Specification Property Assignment*
**supportedActionTarget**"}
1==>28
29@{ shape: hex, label: "*Specification Property Value*
**digitalSubscriptionRequester**"}
28==>29
subgraph 30 [digitalSubscriptionRequester details]
31@{ shape: text, label: "*description:*
**An actor requesting the digital subscription.**"}
32@{ shape: text, label: "*type Name:*
**Actor**"}
33@{ shape: text, label: "*deployed Implementation Type:*
"}
34@{ shape: text, label: "*required:*
**false**"}
end
29==>30
35@{ shape: hex, label: "*Specification Property Value*
**destinationDataSet**"}
28==>35
subgraph 36 [destinationDataSet details]
37@{ shape: text, label: "*description:*
**The Asset that is the target of the subscription.**"}
38@{ shape: text, label: "*type Name:*
**DataAsset**"}
39@{ shape: text, label: "*deployed Implementation Type:*
**Data Asset**"}
40@{ shape: text, label: "*required:*
**false**"}
end
35==>36
41@{ shape: hex, label: "*Specification Property Assignment*
**producedActionTarget**"}
1==>41
42@{ shape: hex, label: "*Specification Property Value*
**newDigitalSubscription**"}
41==>42
subgraph 43 [newDigitalSubscription details]
44@{ shape: text, label: "*description:*
**A newly created digital subscription (or a subtype of).**"}
45@{ shape: text, label: "*type Name:*
**DigitalSubscription**"}
46@{ shape: text, label: "*deployed Implementation Type:*
"}
47@{ shape: text, label: "*required:*
**false**"}
end
42==>43
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 44 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 23 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 45 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 46 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 47 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 26 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 27 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 28 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 29 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 30 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 31 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 32 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 33 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 34 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 35 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 14 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 36 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 15 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 37 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 38 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 39 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 19 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 1 color:#000000, fill:#53bbb4, stroke:#000000
style 2 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 3 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 5 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 6 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 7 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 8 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 40 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 41 color:#f2d9e7, fill:#260d1b, stroke:#f2d9e7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 42 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 43 color:#260d1b, fill:#d98cb6, stroke:#260d1b
```
