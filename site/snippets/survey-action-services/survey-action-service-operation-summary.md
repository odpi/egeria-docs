<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Once installed in the engine host, the survey action service can be called either by:

* via an [engine action](/concepts/engine-action), or
* via a [governance action process](/concepts/governance-action-process).

Each time the survey action service starts, the Survey Action OMES creates a new [Survey Report](/concepts/survey-report) via a call to the Stewardship Action OMAS.  As the survey action service runs, it is retrieving metadata, and storing annotations, via its [survey context](/concepts/survey-context).  The Survey Action OMES routes these requests to the Stewardship Action OMAS which has access to the open metadata repositories.


