---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0210 Data Stores

The *DataStore* entity describes a physical [digital resource](/concepts/resource) that supplies data.

## DataContentForDataSet

The *DataContentForDataSet* relationship defines how data is supplied to a [DataSet](/types/0/0010-Base-Model) from a particular [digital resources](/concepts/resource).  The DataSet entity includes a property called *formula*.  This describes the logic that is used to populate the data set.  The formula can include placeholders.  These placeholders are defined by the *queryId* properties in the linked DataContentForDataSet relationships.  The associated *query* property describes how the data from the linked dataContent resource is selected.

![UML](0210-Data-Stores.svg)

--8<-- "snippets/abbr.md"