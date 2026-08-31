<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Building the governance team

When [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) joined Coco Pharmaceuticals as the CDO, he soon realized that the execution of their business strategy to move to personalized medicine was being held back by their operational practices. Some of this was related to their use and management of data (his responsibility to fix of course), but there were broader issues relating to security, IT infrastructure management, software development and their corporate governance.  He realizes that he can not do this alone and calls his colleagues together to discuss how they proceed.

![Calling the governance leaders together](governance-leaders-meeting-in-progress.png)

They agree to divide the work amongst themselves, using the traditional governance domains to divide out the responsibilities, but maintaining the governance information using open metadata (Egeria) to be able to coordinate their work across the governance domains.

The result is as follows:

* [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) becomes the CDO and head of the DATA governance domain.
* [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) becomes the CISO and head of the SECURITY governance domain.
* [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) becomes the CPO and head of the PRIVACY governance domain.
* [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) as the CFO becomes head of the CORPORATE governance domain.
* [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) as the infrastructure lead becomes head of the IT INFRASTRUCTURE governance domain.
* [Polly Tasker](/practices/coco-pharmaceuticals/personas/polly-tasker) as the most senior software manager becomes had of the SOFTWARE DEVELOPMENT governance domain.

They also add more specialist governance leaders to the team.

* [Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview) is to lead the DATA SHARING governance domain.
* [Tessa Tube](/practices/coco-pharmaceuticals/personas/tessa-tube) is to lead the DRUG DEVELOPMENT governance domain.
* [Tom Tally](/practices/coco-pharmaceuticals/personas/tom-tally) is to lead the SUSTAINABILITY governance domain.

## Defining the governance drivers

Their first challenge is to document the **governance drivers**.  These are the business imperatives, regulations and threats that the governance team needs to focus on.

They begin with the business imperatives.  They try to capture the key concerns of their board and come up with:.

* **Personalized medicine** - the company wants to provide personalized medicine to its customers.  Initial projects in this space have provide promising.  This is a key focus of the board, and requires an extensive business transformation.  It is where the governance activity can add a lot of value.
* **Cyber Resilience** - the board recognizes that cyber-security is critical to avoid both loss of intellectual property and the ongoing operations of the business.
* **Sustainability** - sustainability is recognized by the board as a way to provide focus on the future viability of the business.

Next they think about the threats to the business, including:

* **Cyber-attacks**
* **Loss of competitiveness**
* **Insufficient talent**
* **Disruption in the supply chain**

They next list the regulations that govern the business.  These are divided into:

* **regulations that any business must adhere to**, such as financial reporting.
* **regulations that govern the drug development process**, such as the way clinical trials are conducted.
* **regulations that govern the manufacturing of pharmaceuticals**
* **regulations that govern the distribution of pharmaceuticals**

They create definitions for each of these drivers to capture the essential information needed to understand the governance requirements they represent and load them into Egeria using the [Dr Egeria](/user-interfaces/dr-egeria/overview) Markdown processor.

![The governance leadership team defining governance drivers](meeting-of-the-governance-leaders-2.png)
>The governance leadership team defining governance drivers

With the drivers in place, they agree to go back to their teams to define the responses to each of these governance drivers.

## The risk register

Before they disperse, the leaders meet a second time to build the **risk register**.  The idea comes from the [cybersecurity team](/practices/coco-pharmaceuticals/scenarios/assuring-it-systems-security/overview), where the practice is well established, but Jules asks for it to be built jointly - the threats they have just listed do not respect the domain boundaries they have just drawn, and a register owned by one team would only ever describe one team's view.

The distinction they settle on is between a threat and a risk.  A **threat** is a governance driver: a description of something that could go wrong.  A **risk** is the concrete, assessable consequence that a threat gives rise to in this company, rated for likelihood and impact - and therefore for importance - and linked back to the threat it realises.  "Cyber-attack" is a threat.  "Ransomware could encrypt manufacturing control systems and halt production of on-demand personalised treatments" is a risk, and it is the second of those that can be argued about, mitigated and measured.

Each leader brings the risks arising in their own domain, and the group rates them together.  Twelve risks come out of the session, in six categories:

| Category | Owner | Risks identified | Rating |
|---|---|---|---|
| Cyber Security | [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) | Ransomware disruption to manufacturing operations; theft of personalised treatment intellectual property | Critical |
| Privacy and Data Protection | [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) | Accidental disclosure of patient data through misconfigured access; insider misuse of sensitive patient data | High |
| Supply Chain | [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) | Onboarding of a fraudulent or compromised supplier; counterfeit or substandard materials entering manufacturing | High to Critical |
| Drug Development and Manufacturing | [Tessa Tube](/practices/coco-pharmaceuticals/personas/tessa-tube) | Loss of clinical trial data integrity; manufacturing batch records failing GMP traceability requirements | High to Critical |
| Knowledge Management | [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) | Loss of undocumented governance knowledge when staff leave; inconsistent data definitions undermining cross-department reporting | Medium-High to High |
| Event Security | [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) | A terrorism-related incident at the annual conference; failure to discharge [Martyn's Law](/practices/coco-pharmaceuticals/scenarios/preparing-for-martyns-law/overview) responsible person duties | Medium-High |

Each risk records its likelihood, its impact and the implications that follow - what would have to be true for the company to be able to say it had responded.  The ransomware risk, for example, carries the requirement that manufacturing systems be segmented from the corporate network, that offline and tested backups exist for everything critical to production, and that the incident response plan cover manufacturing downtime specifically.  Those implications are what the domain programs are later written against.

The exercise of linking every risk back to a threat exposes a gap that nobody had noticed.  Three of the twelve arise from regulatory obligations - FDA clinical trial regulations, Good Manufacturing Practice, and Martyn's Law - that the leaders had captured as **regulations** but never as **threats**.  The risks were real, and each had an owner, but there was no driver in the model for them to answer to.  The team defines the missing threats so that every risk links to one.

This turns out to be the first practical demonstration of the point Jules had been making about keeping the definitions in open metadata rather than in separate documents.  Nobody discovered the gap by reading the register; it appeared because the links would not resolve.

## Building out the governance domains

Then each leader takes their domain back to their own team.  The domains develop in parallel, and what comes back is more than anyone had expected.

| Domain | Led by | What their program covers |
|---|---|---|
| `Privacy` | [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) | EU and UK GDPR compliance, and - because the company is a US-listed parent with UK and EU subsidiaries - controllership between group entities, international transfers to the US parent, and the supervisory authority relationships that follow from the group structure. |
| `Security` | [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) | The definitions supporting ISO 27001 certification, from his team's work on the [data security strategy](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview). |
| `Drug Development` | [Tessa Tube](/practices/coco-pharmaceuticals/personas/tessa-tube) with [Tanya Tidie](/practices/coco-pharmaceuticals/personas/tanya-tidie) | Good Clinical Practice, the EU Clinical Trials Regulation, source data attribution and verification, trial master file completeness, blinding integrity, adverse event reporting, and a twenty-five year retention obligation that outlives every system holding the records. |
| `Corporate` | [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) with [Tom Tally](/practices/coco-pharmaceuticals/personas/tom-tally) and [Sally Counter](/practices/coco-pharmaceuticals/personas/sally-counter) | The obligations the company carries as a company rather than as a manufacturer or a trial sponsor: that its reported figures are true, that the third parties it pays are who they claim to be, and that its dealings with prescribing clinicians are transparent.  Sarbanes-Oxley, the Foreign Corrupt Practices Act and the UK Bribery Act all apply at once across the group. |
| `Manufacturing` | [Stew Faster](/practices/coco-pharmaceuticals/personas/stew-faster) with [Florence Paynter](/practices/coco-pharmaceuticals/personas/florence-paynter) and [George Pie](/practices/coco-pharmaceuticals/personas/george-pie) | Good Manufacturing Practice made operational: batch record integrity, ALCOA+ data integrity, equipment qualification, deviations and CAPA, supplier qualification, cold chain monitoring, and the controls that arise when a batch is made for one identified patient. |
| `Manufacturing` (serialisation) | the same manufacturing team | The unique identifiers carried by every saleable pack, and the national systems a pharmacy checks before dispensing.  Kept separate because it has its own regulations, its own external interfaces, and a data volume larger than the whole of the rest of manufacturing combined. |
| `Human Resource Management` | [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) | Employment law that differs across the US parent and the UK and EU subsidiaries, and pay transparency obligations that are among the most data-intensive reporting duties the company carries. |
| `Health and Safety` | [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) | Occupational exposure and health surveillance, the hazardous substance register and its safety data sheets, waste classification and disposal, and emergency arrangements derived from what is actually held at each location.  A second file covers biological agents and the contained use of genetically modified organisms. |
| `Distribution` | the manufacturing team | Dangerous goods transport: solvents between research sites, cytotoxic product to hospital pharmacies, clinical samples, patient-derived material travelling in both directions on a clock, and the lithium batteries in the temperature monitoring devices accompanying almost all of it. |
| `Diversity, Equity and Inclusion` | Head of DEI *(appointment pending)* | Whether the medicines the company develops actually work for the populations that will take them - across clinical evidence, patient-affecting models, and organisational representation. |
| `Data` | [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) with [Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview) and [Peter Profile](/practices/coco-pharmaceuticals/personas/peter-profile) | Written last, to dovetail into everything the other teams produced. |

Four of these domains did not exist when the leaders divided the work.  `Human Resource Management`, `Health and Safety`, `Distribution` and `Diversity, Equity and Inclusion` each had to be registered as a [governance domain](/concepts/governance-domain) before any definition could claim it - and the fact that they were missing from the original list is itself a finding.  The traditional domains describe how a company governs its *information*; they do not describe how a pharmaceutical company governs the things that can hurt somebody.

## What the domain programs revealed

Read together, the programs give the leadership team its first comprehensive view of what Coco Pharmaceuticals is actually obliged to do.  Several things become clear that no single domain could have seen.

**The domains are layered, and the layer decides who should own a definition.**

| Layer | Domains | Role |
|---|---|---|
| Business outcome and regulatory | `Manufacturing`, `Privacy`, `Corporate`, `Drug Development`, `Human Resource Management`, `Diversity, Equity and Inclusion`, `Health and Safety`, `Distribution` | Carry responsibility for business results and regulatory compliance, and own the drivers |
| Systemic | `Data`, `Security` | Address systemic issues across the business, in service of the outcome domains |
| Serving | `IT Infrastructure`, `Software Development` | Provide the digital services the business runs on |

**Some domains face two ways at once.**  Human resource management answers outward to employment law, and inward supplies data other domains depend on absolutely: manufacturing cannot certify a batch without evidence the operator was qualified, drug development cannot show good clinical practice compliance without site training records, and security cannot revoke access to someone it has not been told has left.  Until the programs were written side by side, those were three assumptions rather than three obligations.

**Obligations from different domains can genuinely conflict.**  The health and safety program makes the sharpest case.  Every other control in the plant protects the product from the people; these protect the people from the product.  Coco Pharmaceuticals handles compounds that are pharmacologically active at very small doses, and the containment needed to protect an operator can work directly against the conditions needed to protect a sterile product - airflow that pulls contamination away from an operator pushes it toward the product.  Such conflicts are resolved by engineering judgement, but they have to be *recognised* first, and a change assessed only for its manufacturing consequences will pass while creating an exposure risk nobody evaluated.

**The group structure reaches into everything.**  A trial site sits in the UK or the EU, the sponsor entity determines who the data controller is, and the data consolidates into a US-held clinical database - so a clinical trial engages obligations owned by the privacy domain.  A pack destined for Belfast and one destined for Dublin leave the same production line and are governed by different serialisation regimes.  The same corporate shape appears in the financial, privacy, employment and serialisation programs, described four times by four teams who had never compared notes.

**Definitions in one domain depend on definitions in another.**  Transport classification is drawn from the substance register that health and safety maintains and the agent classification in the biological agents file.  The corporate program links to the raw material obligation in manufacturing.  The personalised medicine programme turns out to be contained use of genetically modified organisms in the legal sense - manufacturing governs the patient identity attached to that material, and nothing had governed the fact that it is a GMO at all.

The dependencies are numerous enough that the loading order of the definitions has to follow the story: a definition can only link to one that already exists.

## Why data governance matters to all of it

The shape of Jules' own program is the clearest evidence of what the exercise proved.  The `Data` domain owns only three governance drivers - the small number of problems that originate in how the organisation manages data itself, that no single domain can fix from inside its own boundary, and that surface as damage in several domains at once.  Everything else in the data governance program responds to drivers owned elsewhere.

That makes it short on drivers and long on links, and deliberately so: most of what the data domain does exists to let another domain meet an obligation that is theirs.  A data policy that answers no driver and serves no domain is governance without a customer.

It also explains why the leaders' insistence on maintaining their definitions in open metadata rather than in separate documents turns out to matter more than it seemed at the time.  Each team wrote its own program, but the value is in the links between them - and links can only be followed if the definitions live in the same place.  The set of obligations they have now described is the material that the [key information supply chains](/practices/coco-pharmaceuticals/scenarios/defining-information-supply-chains/overview) are later drawn against, and reading those links backwards becomes a governance check in itself: an obligation with no data flow attached is either operating on data that does not move, or is an obligation nobody has yet worked out how to observe.

??? info "Loading the governance programs"
    The Dr.Egeria Markdown files for all of the domain programs are available in either the JupyterLab or Obsidian environment of [Quickstart](/egeria-workspaces/quick-start/overview), in 'coco-workbooks/0. data-governance-program'.  [Link to the directory on GitHub](https://github.com/odpi/egeria-workspaces/tree/main/coco-workbooks/0.%20data-governance-program).  Its `README.md` gives the load order and explains the dependencies between the domains - each file is loaded as the governance leader who owns it, so that the definitions are attributed to the right person.

??? info "Viewing the governance programs"
    The definitions can be viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview) through the **Governance Definitions** card, or through the **Collections** card by selecting **Folios** and then **Governance Folios**, where each governance leader's folio collects the definitions they are responsible for.

See:

* [Creating the Data Governance Program](/practices/coco-pharmaceuticals/scenarios/creating-data-governance-program/overview)
* [Creating the Security Governance Program](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview)
* [Creating the Sustainability Governance Program](/practices/coco-pharmaceuticals/scenarios/sustainability-initiative/overview)

!!! info "Further information"

    * [Planning for a governance program](/guides/planning/governance-program/overview)
    * [Governance Definitions](/concepts/governance-definition)

    The governance definitions created by the governance leaders can be loaded into Egeria and then viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview) in the [Quickstart](/egeria-workspaces/quick-start/overview) environment.

--8<-- "snippets/abbr.md"
