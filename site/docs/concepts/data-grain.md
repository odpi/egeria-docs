<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Data Grain

A *Data Grain* is part of a [data specification](/concepts/data-specification) that describes the level of detail in a single row/object in a data source.  Data warehouses aim to capture data at the most granular level that can be achieved whilst ensuring the granularity of every row in the table is the same.

In Egeria, the data grain is one on the dimensions of scope captured in a [data lens](/concepts/data-lens).  It is used to filter out data that is too course-grained to be used by a project.

![Purpose of a data grain](data-grain.svg)
> A data grain definition can be used to filter out data sources whose data is too course-grained.

Data grains are often linking in order of granularity to enable the matching of data sources to a data lens to consider more finely-grained data sources as potential candidates for the project because their detail can be rolled out to the desired granularity. 

![Data grain hierarchy](data-grain-hierarchy.svg)
> A hierarchy of temporal data grains

## The grain statement

The grain statement is a formal definition of the granularity of a data set.   It describes what a single row/object/element in the data set represents.  It often concatenates granularity definitions from multiple dimensions - such as:

> One row holds the number of *confirmed sales orders* per *month* across all of *Coco Pharmaceuticals*

## Discovering the data grain

It is possible to examine the data values within a data source to come up with a grain statement.  For example, you can evaluate the "resolution" of the data by looking for the **lowest common denominator** in these three core pillars:

|Dimension|How to Evaluate Grain| Examples of Grain Levels                                              |
|---|---|-----------------------------------------------------------------------|
|**Temporal**|Find the smallest increment of time that changes between rows.| Millisecond, Hourly, Daily Snapshot, Monthly Aggregate.               |
|**Geospatial**|Determine the smallest boundary represented. Check if coordinates are precise or "jittered."| GPS Coordinates, Street Address, Zip Code/Postcode, ISO Country Code. |
|**Organizational**|Identify the hierarchy level the data belongs to.| Individual Employee, Team/Dept, Legal Entity, Global Holding.         |


This is called the **observed** data grain.  It may be that there are missing values in the data source at the time of your analysis that would impact the data grain result if they were correctly added at a later date.  The true data grain is called the **intrinsic** data grain.

Another point to note is that data grain may be event driven - for example, a new row is created each time a new sales order is taken.  This is typical in operational systems.  Data that has been extracted from operational systems for reporting/analysis purposes is often aggregated and the grains then become periodic or some other form of aggregation.  This process often reduces the granularity of the data.

Finally, it is important to validate that master/detail (aka header/line) information is not incorporated into the same row leading to unnecessary duplication of data - and double-counting as further analysis takes place.  This is called the **mixed grain trap**.

???+ info "Additional information"
    * The open metadata types for a data grain are found in [Model 0541 Data Grains](/types/5/0541-Data-Grains/).
    * The open metadata types for data grain discovery are found in [Model 0626 Data Grain Discovery](/types/6/0626-Data-Grain-Discovery/).
    * [Data Designer OMVS](/services/omvs/data-designer/overview) provides the API for creating data grains.


--8<-- "snippets/abbr.md"
