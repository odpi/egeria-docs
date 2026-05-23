<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Action Author API

The Action Author API provides a REST API to support user interfaces (UIs)
relating to the set up and maintenance of the definition of the governance actions needed by your organization.

Governance actions can be a single operation, such as automatically classifying newly catalogued data.
These single operations are called **governance action types**.

Alternatively, a governance action may be a choreographed sequence of actions, where the result of one
action determines which action(s) run next. The choreographed sequence of actions is called a
**governance action process**.


## Further information

* [Governance Action Concept](/concepts/governance-action)
* [Governance Action Type Concept](/concepts/governance-action-type)
* [Governance Action Process Concept](/concepts/governance-action-process)

Sample requests for the REST API can be found in [Egeria-api-action-author.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/action-author/Egeria-api-action-author.http).


--8<-- "snippets/abbr.md"
