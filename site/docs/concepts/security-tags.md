<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Security Tags

*Security tags* are the labels and properties that a security engine uses to work out which access control rules apply to a resource.

The point of security tags is to keep the *classification* of the data separate from the *rules* about who may see it.  Egeria records what the data is - reference data, personal data, expiring at a particular date.  The security manager, such as Apache Ranger, holds the rules that say what to do about it.  Because the two are separate, a rule can be changed without re-tagging thousands of columns, and a column can be re-tagged without rewriting any rules.

## What a security tag holds

The *SecurityTags* classification carries two things:

* *securityLabels* - simple labels indicating that the data belongs to a particular category, for example `reference-data` or `product-description`.
* *securityProperties* - name-value pairs whose values the rules can act on, for example `expires-on` -> `31/12/2024`.

## Where security tags are attached

A *SecurityTags* classification can be attached to any [referenceable](/concepts/referenceable), and the level it is attached at determines its reach:

* On a schema attribute - a database column, for example - it applies to that data field alone.  This is the most common case.
* On a group of fields, such as a database table or schema, it applies to every field in the group.
* On the [asset](/concepts/asset) itself, it applies to all the data the asset contains.
* On a glossary or [glossary term](/concepts/glossary-term), where the tagging follows the meaning of the data rather than its location.

The tags are then distributed to the security manager along with the technical metadata, and the rules run against them at the point of access.

???+ info "Additional information"
    * The *SecurityTags* classification is described in [Model 0423 Security Definitions](/types/4/0423-Security-Definitions), alongside the security groups, lists, roles and access controls it works with.
    * [Synchronized Access Control](/features/synchronized-access-control/overview) describes the full lifecycle - cataloguing, augmenting, consolidating into security tags, distributing to the security managers, and auditing the result.

--8<-- "snippets/abbr.md"
