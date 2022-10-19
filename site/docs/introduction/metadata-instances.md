<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->



At the granular level of the repository services, we refer to specific metadata objects as *metadata instances*, which can only be one of the following:

- An *entity* is capable of describing a metadata object on its own: for example, a business vocabulary term, database, field in a schema, and so on. If you think about metadata as a graph, these are the nodes (vertices) in the graph. They typically describe concepts, people, places and things.
- A *relationship* describes a (typically) directional association between two entities: for example, the semantic meaning of a relational database column by relating a business vocabulary term with the relational database column. In a graph sense, these are the links (edges) that show how entities are related.
- While not strictly speaking a kind of metadata instance, a *classification* provides a means to extend an entity with additional facets of information: for example, describing the level of confidentiality with which a particular relational database column should be treated. Classifications describe additional attributes of an entity and can be used to identify entities that are similar in a specific aspect.


--8<-- "snippets/abbr.md"
