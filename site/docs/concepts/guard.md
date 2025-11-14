---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Guards

Guards are labels that are produced by [governance services](/concepts/governance-service) when they complete and are used by the [Open Governance Services](/services/open-governance-services) to determine which [step](governance-action-process-step.md) to run next in a [governance action process](governance-action-process.md).

For example, in the process below, the governance service called *Get Day Of Week* produces a guard that represents the current day of the week.  This means that in its [specification](specification.md) it lists 7 *Produced Guard* properties (monday, tuesday, wednesday, thursday, friday, saturday and sunday).  Each of these possible guards are mapped to a step to run if that guard is produced.  When the process runs, the first step runs and produces at least one guard.  The steps linked to these guards are run.

![Controlling governance action process flow](guard-controls-process-flow.svg)

It is possible that multiple guards can be mapped to the same step. In the example below there are two follow-on steps to *Get Day Of Week*. The *Weekday Work* is run if *Get Day Of Week* produces a guard of monday, tuesday, wednesday, thursday or friday.  *Weekend Work* is run if the guard is saturday or sunday.

You may be wondering what would happen if *Get Day Of Week* produced multiple guards?  By default, the open governance services will run an instance of the follow-on steps for each of the guards produced by *Get Day of Week*.  So if *Get Day Of Week* returned the guards monday, monday, tuesday and saturday then *Weekday Work* would run 3 times and *Weekend Work* would run once.

It is possible to configure a step so it is only allowed to run once in the process instance. (See the *ignoreMultipleTriggers* property in the [GovernanceActionProcessStep](/types/4/0462-Governance-Action-Processes) metadata element).

![Multiple guards mapped to the same step](guards-can-map-to-same-step.svg)

It is also possible that some guards are not mapped on a governance action process. This is not a problem.  If an unmapped guard is produced during the execution of a governance action process, no follow-on step is run.  So, in the example below, nothing happens if the saturday or sunday guard is produced.  When there are no follow-on steps to run for a process, it terminates.

![Unmapped guards](guard-may-not-be-mapped.svg)

Finally, some guards may be flagged as *mandatory guards* (see *NextGovernanceActionProcessStep* relationship in [model 0462](/types/4/0462-Governance-Action-Processes)). A step can not run until all linked mandatory guards have been produced.  This allows the joining of parallel flows in the process.

![Mandatory guards](guards-halt-process-flow-if-mandatory.svg)

## Running the Daily Governance Action Process

Egeria includes a definition of the first governance action process shown on this page.  It is part of the [Core Content Pack](/content-packs/core-content-pack/overview) and so is loaded automatically in the default and quickstart environment.

--8<-- "snippets/abbr.md"