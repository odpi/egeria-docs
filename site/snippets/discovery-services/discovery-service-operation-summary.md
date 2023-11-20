<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Once installed in the engine host, the open discovery service can be called either by:

* issuing a REST API call to the engine host, or
* via an [engine action](/concepts/engine-action, or
* via a [governance action process](/concepts/governance-action-process).

Each time the open discovery service starts, the Asset Analysis OMES creates a new [Discovery Analysis Report](/concepts/discovery-analysis-report) via a call to the Discovery Engine OMAS.  As the open discovery service runs, it is retrieving metadata, and storing annotations and data fields, via its [discovery context](/concepts/discovery-context).  The Asset Analysis OMES routes these requests to the Discovery Engine OMAS which has access to the open metadata repositories.


