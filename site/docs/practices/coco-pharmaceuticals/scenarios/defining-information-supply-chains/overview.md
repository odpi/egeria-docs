<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Identifying the key information supply chains

[Information Supply Chains](/concepts/information-supply-chain) represent the flow of key information from its sources to its destinations.  The detail from lineage data captured from the relevant IT operations is associated with the information supply chain so it can be used for analysis and metrics collection, monitoring and business decision-making.   An optional high level design of the flow associated with the information supply chain provides a business-friendly view of the data/control flow.

## Background

[Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) is keen that Coco Pharmaceuticals' [data strategy](/practices/coco-pharmaceuticals/scenarios/defining-the-data-strategy/overview) is focused on the key data processing changes that will drive Coco Pharmaceuticals' transformation to personalized medicine.  [Erin Overview's](/practices/coco-pharmaceuticals/personas/erin-overview) work identifying the [key subject areas](/practices/coco-pharmaceuticals/scenarios/defining-the-data-strategy/overview) highlighted the lack of data exchange between the research, sales, manufacturing and finance.  This will need to change if they are to reduce their cycle times and batch sizes down to single patient requests.  

At this point, they have a [high-level conceptual architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview) for the systems integration and an initial list of [existing authoritative sources](/practices/coco-pharmaceuticals/scenarios/identifying-authoritative-sources/overview).  The challenge now is to define the critical data flows that will be enabled through this new architecture and how they should be designed, rolled out and monitored to ensure they are working as expected.

## Identifying the key information supply chains

Jules calls a working session with [Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview), [Peter Profile](/practices/coco-pharmaceuticals/personas/peter-profile) and the governance leaders.  Coco Pharmaceuticals runs many hundreds of data flows and the point of the session is not to list them, but to agree which ones the company will govern, monitor and be measured on at this level.

The discussion stalls until Erin proposes four tests.  A flow qualifies as strategic if it meets **any one** of them:

| Test | The question it answers |
|---|---|
| **Business continuity** | If this flow stopped for a day, would the company stop making, selling or shipping something? |
| **Regulatory exposure** | Does a regulator have a statutory expectation of this data arriving somewhere, correct and on time? |
| **Patient safety** | Could a fault in this flow reach a patient? |
| **Irreversibility** | Once wrong data has travelled this flow, can the damage be undone? |

The fourth test is the one Jules argues hardest for.  Most data quality problems are recoverable - a report is reissued, a figure is restated.  A serial number issued twice, a pack decommissioned in error, or a patient-derived material that has lost its identity are not.  Flows with that property have to be watched *before* the fault propagates rather than reported on afterwards, and that is a different engineering problem.

With the tests agreed, each governance leader nominates the flows from their domain, argues them against the tests, and the group settles on sixteen.

| # | Information supply chain | Tests met |
|---|---|---|
| 1 | Personalised Treatment Ordering | continuity, regulatory, patient safety, irreversible |
| 2 | Clinical Trials | regulatory, patient safety, irreversible |
| 3 | Adverse Event and Safety Reporting | patient safety, regulatory, irreversible |
| 4 | Batch Manufacturing and Release | continuity, regulatory, patient safety, irreversible |
| 5 | Product Serialisation and Verification | continuity, regulatory, patient safety, irreversible |
| 6 | Cold Chain and Dangerous Goods Consignment | regulatory, patient safety, irreversible |
| 7 | Physical Inventory Tracking | continuity, regulatory |
| 8 | New Drug Product Details | continuity, regulatory |
| 9 | Financial Close and External Reporting | regulatory, continuity |
| 10 | Third Party Onboarding and Payment | regulatory, continuity, irreversible |
| 11 | Employee Expense Payment | regulatory |
| 12 | New Employee Onboarding | continuity, regulatory |
| 13 | Workforce Competency and Qualification | regulatory, patient safety |
| 14 | Occupational Health Surveillance | regulatory, irreversible |
| 15 | Data Subject Rights | regulatory |
| 16 | Sustainability Reporting | regulatory |

Seven of the sixteen already exist in Egeria - they are supplied by the metadata archive that is loaded when the metadata server starts, and are already wired to the components that produce their lineage.  The register **adopts** those rather than recreating them.  The other nine are flows the governance programs plainly depend on, but which nothing had yet named as a supply chain.

Several arguments from the meeting are worth recording, because they are the reason particular flows are on the list:

* **Adverse Event and Safety Reporting** did not exist as a flow anybody owned.  Safety signals arrive from trial sites, treating clinicians, patients, product complaints and published literature, and each door was managed by whoever owned that door.  The statutory clock starts on first receipt by any part of the company and does not care which door was used.  Naming the chain is what makes the clock measurable end to end.
* **Workforce Competency and Qualification** crosses a domain boundary in a direction nobody planned.  [Human resources](/practices/coco-pharmaceuticals/personas/faith-broker) maintains training records for employment reasons; manufacturing and drug development read them as compliance evidence at the moment a batch is certified or a trial is inspected.  The evidence has to be current at the moment of the act, not at the moment of the audit, which makes the *freshness* of the flow the thing being governed.
* **Third Party Onboarding and Payment** is on the list because of the supplier fraud [Sally Counter](/practices/coco-pharmaceuticals/personas/sally-counter) detected.  The fraud lived in the gap between the screening and the payment.  The company's defence had rested on one person's familiarity with a ledger rather than on a control - which is a supply chain observation: a flow nobody had described end to end was being monitored by somebody who happened to know what normal looked like.
* **Data Subject Rights** is the only entry whose difficulty is a direct consequence of the others.  A subject access request is hard exactly to the extent that the company cannot say where personal data travels, so the register itself is part of the answer.

The group also agrees the **handovers** between chains, because that is where accountability changes hands and where a fault in one chain becomes a failure in the next.  Batch Manufacturing and Release turns out to be the busiest junction in the company: a batch cannot be certified unless the product definition was correct, the raw material was verified and the operator was qualified - three facts arriving from three different chains with three different owners.

??? info "Loading the strategic information supply chains"
    The Markdown file containing the register is available in either the JupyterLab or Obsidian environment of [Quickstart](/egeria-workspaces/quick-start/overview).  It is located in 'coco-workbooks/0. data-governance-program/strategic-information-supply-chains.md'.  [Link to the Markdown document on GitHub](https://github.com/odpi/egeria-workspaces/blob/main/coco-workbooks/0.%20data-governance-program/strategic-information-supply-chains.md).  It creates the nine new chains, adopts the seven from the archive, links the handovers between them, and attaches each chain to the [governance definitions](/concepts/governance-definition) that govern it.

??? info "Viewing the information supply chains"
    The register can be viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview) either through the **Solution Architect** card or the **Collections** card, selecting **Strategic Solutions** and then **Strategic Information Supply Chains**.

Reading the governance links in the opposite direction turns out to be the more useful exercise.  An obligation with no supply chain attached is either operating on data that does not move, or is an obligation nobody has yet worked out how to observe.

## Laying out the solution components

The register is a list of names.  What makes it a monitor is the link from each chain to the [solution components](/concepts/solution-component) that execute it, because that is what allows activity, errors and volumetrics to roll up from the real systems into a view somebody can be held accountable for.

Erin and Peter work through the sixteen chains one at a time, identifying the components each one needs and reviewing the result with the governance leader who owns the flow - [Stew Faster](/practices/coco-pharmaceuticals/personas/stew-faster) for manufacturing, distribution and inventory, [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) for the financial chains, [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) for the workforce and privacy chains, and [Tessa Tube](/practices/coco-pharmaceuticals/personas/tessa-tube) for the trials and safety chains.  Two of the sixteen need no work: Clinical Trials and Sustainability Reporting arrive from the metadata archive already complete.

The result is seventy-one components organised into eleven business system groups, joined by a hundred and thirty [solution linking wires](/concepts/solution-blueprint).  Each wire records which supply chains it implements, so Egeria assembles each chain's implementation graph from the wires rather than from a hand-drawn picture.

They find the archive has laid foundations nobody had built on.  Five [solution blueprints](/concepts/solution-blueprint) exist as stubs, and every one of them sits exactly where a strategic supply chain needs components - so they fill the stubs in rather than inventing parallel blueprints beside them.

| Archive blueprint | Components before | Components added |
|---|---|---|
| Personalized Medicine Order Fulfillment | 1 | 6 |
| Automated Manufacturing Control | 0 | 14 |
| Inventory Management | 1 | 3 |
| Employee Management | 1 | 10 |
| Hazardous Material Management | 1 | 11 |

Drawing the wires produces findings the register could not have produced on its own:

* **Components belong to more chains than anyone expected.**  The qualification register is read by manufacturing, by clinical trials and by dangerous goods transport, and none of those consumers is a human resources use case.  The HazMat inventory serves occupational health, transport classification and inventory tracking from one substance identity.  Each of these is a component whose owner is answering questions they were not asked when it was bought.
* **The handovers are where the work is.**  Forty-four of the hundred and thirty wires implement more than one supply chain.  Those are the wires worth instrumenting first, and none of them belongs unambiguously to one team.
* **Some chains are gates, not flows.**  Batch release, material quarantine and identifier upload are not conveyances; they are refusals that occasionally let something through.  Modelling them as wires makes the gate visible as a dependency, which is what a downstream team needs in order to understand why their input sometimes does not arrive.

??? info "Loading the solution components"
    The Markdown file containing the component analysis is available in either the JupyterLab or Obsidian environment of [Quickstart](/egeria-workspaces/quick-start/overview).  It is located in 'coco-workbooks/1. coco-data-hub/strategic-supply-chain-analysis.md'.  [Link to the Markdown document on GitHub](https://github.com/odpi/egeria-workspaces/blob/main/coco-workbooks/1.%20coco-data-hub/strategic-supply-chain-analysis.md).  It loads after the register and before 'solution-design.md', because the eight business function components of the [data-driven systems architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview) are shared by every strategic chain and are created here.

??? info "Viewing a supply chain's implementation"
    Selecting an information supply chain in [Egeria Explorer](/user-interfaces/egeria-explorer/overview) under the **Solution Architect** card shows its member components and the wires between them, assembled from the wire definitions rather than drawn by hand.

## Mapping the components to real systems

A solution component is a design element.  Before the chains can be monitored, each component has to be linked to the system that actually runs it, so Erin and Peter take the seventy-one components to [Gary Geeke's](/practices/coco-pharmaceuticals/personas/gary-geeke) [systems inventory](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview) and try to match them up.

The exercise produces two conclusions, and both of them are more useful than the mapping itself.

### There are systems missing from the inventory

Gary's inventory is thorough about the infrastructure he is responsible for, and silent about everything else.  Departments that bought their own systems never appeared in his spreadsheet, because they were never his to maintain - and a good number of the components the chains depend on turn out to live in exactly those systems.  The gaps cluster in predictable places:

* Systems bought by a single department to solve a single department's problem, and then quietly relied on by somebody else - the qualification register being the clearest case, read at the moment of a batch signature by a process its owner had never been asked about.
* Systems operated by third parties, where the boundary matters more than the internals: the screening service, the carriers, the national verification repositories the pharmacies check.
* Systems whose absence was invisible because nothing failed.  Nobody had missed them from the inventory, because the inventory had never been asked a question that needed them.

The second conclusion follows from the first: the inventory was answering *what do we run?* when the supply chains were asking *what do we depend on?*  Those are different questions and they need the same catalogue.

### The integration gaps become visible

Where both ends of a wire do map to real systems, it becomes possible to ask how the data actually gets from one to the other - and for a significant number of wires the honest answer is a periodic extract, a spreadsheet, or a person.  The pattern repeats across the chains and is always the same shape: an approval and the act it authorises sit in different systems, and the value of the approval depends entirely on it still being attached when the act happens.

* Expense approval and expense payment.
* Supplier screening and supplier payment - the gap the fraud lived in.
* Operator qualification and batch signature.
* Certificate currency and the signing of a dangerous goods declaration.
* A joiner or leaver event and the access that should follow or end with it.

None of these is a new discovery to the team that owns it.  What is new is that they are now visible as the *same* defect, in one picture, ranked by the supply chains that run through them - which turns a list of local irritations into an integration backlog with a business case attached.

## Cataloguing the missing systems and scoping the Data Hub

The work splits in two.

Gary takes the list of missing systems and catalogues them, extending the inventory beyond the infrastructure he owns to the systems the business depends on.  He is already doing this for the recently acquired Austin and Bucharest sites, whose systems arrived as spreadsheets from teams that had catalogued their own estates, so the mechanism exists and it is the coverage that changes.  Along the way he discovers that each site had invented its own systematic naming convention, and captures both as naming standard rules - a small piece of housekeeping that makes the two estates comparable.

??? info "Extending the systems inventory"
    The notebook that loads the additional systems is available in the JupyterLab environment of [Quickstart](/egeria-workspaces/quick-start/overview), in 'coco-workbooks/4. keeping-safe/extending-the-systems-inventory'.  [Link to the notebook on GitHub](https://github.com/odpi/egeria-workspaces/blob/main/coco-workbooks/4.%20keeping-safe/extending-the-systems-inventory/extending-the-systems-inventory.ipynb).  The naming conventions the two sites had each invented are captured in [naming-conventions.md](https://github.com/odpi/egeria-workspaces/blob/main/coco-workbooks/4.%20keeping-safe/extending-the-systems-inventory/naming-conventions.md).

Erin and Peter take the integration gaps and use them to scope the Coco Data Hub.  They now have something the architecture discussion had been missing: an ordered list of the flows that matter, the components at each end of them, and evidence of which handovers are carried today by an extract or a person.  The chains that cross the most boundaries, and the wires that implement more than one chain, are where the hub earns its place - and the ones that do not need it can be left alone.

That scoping is the beginning of the [new systems architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview), where the Data Hub design and the implementation plan are built up flow by flow.

!!! info "Further information"

    * [Information supply chains](/concepts/information-supply-chain)
    * [Solution blueprints](/concepts/solution-blueprint) and [solution components](/concepts/solution-component)
    * [Cataloguing infrastructure](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview)
    * [Defining the new systems architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview)


--8<-- "snippets/abbr.md"