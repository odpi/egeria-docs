```mermaid
---
title: SolutionBlueprint - Open Metadata Digital Product Catalog Components [60f86dc1-f4c1-4f70-a22f-6cfcf3dea5ed]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Digital Product Delivery Location**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
4==>|"Consume data [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
5==>|"maintain data [Solution Linking Wire]"|3
6@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
6==>|"(maybe) remove copy [Solution Linking Wire]"|3
2==>|"Collection Membership"|3
7@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
7==>|"Collection Membership"|3
8@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
8-.->3
1==>|"Collection Membership"|6
9@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
9==>|"Cancel product subscription [Solution Component Actor]"|6
10@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
6==>|"remove subscription [Solution Linking Wire]"|10
2==>|"Collection Membership"|6
11@{ shape: rect, label: "*Solution Blueprint*
**Cancelling a Subscription to a Digital Product**"}
11==>|"Collection Membership"|6
1==>|"Collection Membership"|5
5==>|"retrieve data [Solution Linking Wire]"|10
12@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
12==>|"initiate when product changes [Solution Linking Wire]"|5
2==>|"Collection Membership"|5
13@{ shape: rect, label: "*Solution Blueprint*
**Creating a new Subscription to a Digital Product**"}
13==>|"Collection Membership"|5
14@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
14-.->5
15@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
1==>|"Collection Membership"|15
9==>|"Subscribe to product [Solution Component Actor]"|15
15==>|"configure subscription [Solution Linking Wire]"|12
15==>|"read subscription requirements [Solution Linking Wire]"|10
2==>|"Collection Membership"|15
13==>|"Collection Membership"|15
1==>|"Collection Membership"|12
16@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
12==>|"notify when product changes [Solution Linking Wire]"|16
12==>|"monitor product changes [Solution Linking Wire]"|10
17@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
17==>|"set up subscription managers [Solution Linking Wire]"|12
2==>|"Collection Membership"|12
18@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
18-.->12
1==>|"Collection Membership"|17
19@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
19==>|"Maintains [Solution Component Actor]"|17
17==>|"maintain catalog entry [Solution Linking Wire]"|10
20@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
17==>|"add products to catalog [Solution Linking Wire]"|20
21@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
17==>|"monitor for changes [Solution Linking Wire]"|21
22@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
22==>|"Collection Membership"|17
23@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
23-.->17
24@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
1-.->24
style 11 color:#000000, fill:#f5fffa, stroke:#000000
style 22 color:#000000, fill:#f5fffa, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#000000, fill:#f5fffa, stroke:#000000
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#FFE599, stroke:#000000
style 20 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
style 21 color:#000000, fill:#DDA0DD, stroke:#000000
```
> Open Metadata Digital Product Catalog Components: Description of the processing used to create and manage the digital products derived from open metadata. (Extracted from 6.0-SNAPSHOT)
