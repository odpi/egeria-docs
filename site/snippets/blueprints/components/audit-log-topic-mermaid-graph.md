```mermaid
---
title: SolutionComponent - Audit Log Topic [9caf4cb6-c43d-49d5-aa50-02b06fc66225]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Audit Log Topic**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
3==>|"audit log notifications [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
4==>|"audit log notifications [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**Integration Daemon**"}
5==>|"audit log notifications [Solution Linking Wire]"|1
6@{ shape: cyl, label: "*Topic*
**egeria.omag.egeria.omag.server.quickstart.ffdc.audit-logs**"}
1==>|"running instance [Implemented By]"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/audit-log-destination-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-daemon/" "Click for more documentation" _blank
```
> Audit Log Topic: Provides notifications when audit log events of severity Error, Exception, Activity, Action, Decision, Security or Cohort are written to the audit log by registered OMAG Servers. (Extracted from 6.0-SNAPSHOT)
