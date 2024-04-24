---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Valid Metadata OMVS

The Valid Metadata Open Metadata View Services (OMVS) is a REST API designed to back user interfaces (UIs) that support lists of valid values for open metadata attributes.  It offers two types of services:

* Maintain and query lists of valid values for open metadata attributes.
* Retrieve details of the defined open metadata types.

## Working with valid metadata values

[Valid Metadata Values](/guides/planning/valid-values/overview) uses [Valid Value Sets](/types/5/0545-Reference-Data) to maintain lists of valid values for open metadata attributes.  It aims to offer UI developers the ability to populate drop-downs with valid values for an attribute, or validate a value provided by an end user, or offer services that maintain these valid value lists.

There are twelve operations for maintaining the valid value lists:

* Three for creating a valid value.
* Three for deleting a valid value.
* Three for querying if a valid value is valid.
* Three for retrieving the properties of a specific valid value.

The reason for three operations for each method is that Egeria needs to distinguish between:

1. A valid value for a primitive attribute (string, integer, etc) or a primitive value in an array attribute.
2. A valid key in a map attribute (called a mapName).
3. A valid value associated with a key in a map attribute.

In addition, there is an operation for retrieving the entire list of valid values for an attribute, plus two methods for managing *Consistent Values* relationships.

## Retrieving open metadata types

The standard open metadata types are describe [on this website](/types).  It is also possible to [define your own](/guides/developer/open-metadata-archives/defining-new-types) open metadata types. The Valid Metadata OMVS provides services to query the types and understand how the lint together.



---8<-- "snippets/abbr.md"






