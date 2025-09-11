<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0450 Governance Rollout

An important aspect of the governance program is the ability to measure its effectiveness and identify the activities that are delivering the highest value, or operating with the greatest efficiency etc.

A value (or collection of values) that should be captured to demonstrate the effectiveness of an aspect of the governance program is documented using the [GovernanceMetric](/types/4/0430-Technical-Control) entity.  

The associated measurements for the metric an either be stored in a data source such as a database or file, particularly if it is a lot of data or captured in a classification attached to the element that the data values describe.


![UML](0450-Governance-Rollout.svg)

## GovernanceExpectations classification

The calculation of governance metrics is often a summary of many other measurements each associated with different resources (such as data sources and processes).
These resources are catalogued as [Assets](/types/0/0010-Base-Model).
The definition of their expected behaviour or content can be captured using the *GovernanceExpectations* classification attached to their Asset.

## GovernanceMeasurements classification

The measurements that support the assessment of a particular resource can be gathered and stored in a *GovernanceMeasurements* classification attached to its Asset.

## GovernanceResults relationship

Alternatively, if it is easier to gather the measurements in an external data source, the asset that describes this data source can be linked to the appropriate governance metrics using the *GovernanceResults* relationship.

The *queryType* and *query* attributes of this relationship capture the query used to retrieve the relevant data for the metric.


--8<-- "snippets/abbr.md"