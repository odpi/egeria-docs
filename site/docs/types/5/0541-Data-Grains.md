---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0541 Data Grains

[Data Grains](/concepts/data-grain) define the granularity of data.

Data Grains were invented by [the Kimball Group](https://www.kimballgroup.com/2008/11/fact-tables/) to describe the granularity of data in a data warehouse fact table.  The concept fits well into a metadata landscape too.  For example, you may have multiple data sources that capture sales data for your organization.  One data source may contain daily figures, another contains  weekly figures, and another contains monthly figures.  They are all the same type of data if you consider there [subject area](/concepts/subject-area).  They may even have the same [schema](/concepts/schema) so they will be technically easy to combine.  However, their different granularity means they can not be combined without transformation, and only at the most course-grained level, if distortion is to be avoided.

Data Grains are also useful when defining the data requirements for a project.  They can be associated with a [data field](/concepts/data-field) definition or associated with a [data lens](/concepts/data-lens).

![UML](0541-Data-Grains.svg)

## DataGrain entity

The *DataGrain* entity describes a description of a specific granularity.

## DataGrainHierarchy relationship

The *DataGrainHierarchy* relationship is used to associate related data grains - for example data grains for a single dimension showing which are more granular than another.

![Example of a hierarchy if data grains](/concepts/data-grain-hierarchy.svg)

## DataGrainDefinition relationship


## DataGrainAssignment relationship

The *DataGrainAssignment* relationship links a data grain to a element that describes an aspect of a digital resource and the data grain describes the granularity of the associate data.

--8<-- "snippets/abbr.md"