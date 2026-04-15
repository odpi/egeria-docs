```mermaid
---
title: NotificationType - Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus [48096b3c-79c0-4973-86a2-5b47904bb79d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Notification Type*
**Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus**"}
2@{ shape: subproc, label: "*Notification*
**Thu Feb 26 15:34:03 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0005 A regular notification for subscription type Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus (48096b3c-79c0-4973-86a2-5b47904bb79d) has been triggered.  It will trigger again in 1440 milliseconds**"}
1==>|"Actions"|2
3@{ shape: subproc, label: "*Notification*
**Thu Feb 26 16:06:43 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0001 Welcome to your subscription for product subscription type: Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus (48096b3c-79c0-4973-86a2-5b47904bb79d)**"}
1==>|"Actions"|3
4@{ shape: subproc, label: "*Notification*
**Thu Feb 26 15:34:03 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0005 A regular notification for subscription type Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus (48096b3c-79c0-4973-86a2-5b47904bb79d) has been triggered.  It will trigger again in 1440 milliseconds**"}
1==>|"Actions"|4
5@{ shape: subproc, label: "*Notification*
**Thu Feb 26 16:06:43 GMT 2026 BAUDOT-SUBSCRIPTION-MANAGEMENT-0001 Welcome to your subscription for product subscription type: Notification type for Daily refresh subscription for product Valid Metadata Value Set: assignmentStatus (48096b3c-79c0-4973-86a2-5b47904bb79d)**"}
1==>|"Actions"|5
6@{ shape: trap-t, label: "*Engine Action*
**baudot-subscription-manager (EgeriaWatchdog)**"}
6==>|"notificationType [Action Target]"|1
7@{ shape: rounded, label: "*Note Log*
**Notifications for Open Metadata Reference Data special interest group**"}
1==>|"community notifications [Notification Subscriber]"|7
8@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Valid Metadata Value Set: assignmentStatus**"}
1==>|"product manager notifications [Notification Subscriber]"|8
9@{ shape: processes, label: "*Governance Action Process*
**Create Daily refresh subscription for Valid Metadata Value Set: assignmentStatus**"}
9==>|"subscriptionManagerNotificationType [Target For Governance Action]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#BDB76B, stroke:#004563
style 3 color:#000000, fill:#BDB76B, stroke:#004563
style 4 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#000000, fill:#BDB76B, stroke:#004563
style 6 color:#000000, fill:#7fffd4, stroke:#000000
style 7 color:#000000, fill:#39add1, stroke:#004563
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#40E0D0, stroke:#000000
```
