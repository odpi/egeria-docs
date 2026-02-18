```mermaid
---
title: SolutionBlueprint - Jacquard Digital Product Loom [bfa05ac2-02eb-48db-9066-de2d335ac562]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
4==>|"Develops [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
3==>|"query metadata [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
6==>|"retrieve data [Solution Linking Wire]"|3
7@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
7==>|"monitor product changes [Solution Linking Wire]"|3
8@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
8==>|"read subscription requirements [Solution Linking Wire]"|3
9@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
9==>|"remove subscription [Solution Linking Wire]"|3
10@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
10-.->3
11@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
1==>|"Collection Membership"|11
12@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
12==>|"Maintains [Solution Component Actor]"|11
13@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
11==>|"add products to catalog [Solution Linking Wire]"|13
11==>|"monitor for changes [Solution Linking Wire]"|5
11==>|"set up subscription managers [Solution Linking Wire]"|7
11==>|"maintain catalog entry [Solution Linking Wire]"|3
14@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
14-.->11
1==>|"Collection Membership"|7
7==>|"initiate when product changes [Solution Linking Wire]"|6
8==>|"configure subscription [Solution Linking Wire]"|7
15@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
7==>|"notify when product changes [Solution Linking Wire]"|15
16@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
16==>|"Collection Membership"|7
17@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
17-.->7
1==>|"Collection Membership"|13
18@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
18==>|"Shop for data [Solution Component Actor]"|13
13==>|"search for type of data [Solution Linking Wire]"|3
2==>|"Collection Membership"|13
19@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
19==>|"Collection Membership"|13
20@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
20-.->13
1==>|"Collection Membership"|5
19==>|"Collection Membership"|5
2==>|"Collection Membership"|5
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#f5fffa, stroke:#000000
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 18 color:#000000, fill:#FFE599, stroke:#000000
style 19 color:#000000, fill:#f5fffa, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
> Jacquard Digital Product Loom: Description of the processing used to create and manage the digital products derived from open metadata in the Open Metadata Digital Product Catalog. (Extracted from 6.0-SNAPSHOT)
