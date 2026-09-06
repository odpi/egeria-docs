<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0450 Governance Rollout

An important aspect of the governance program is the ability to measure its effectiveness and identify the activities that are delivering the highest value, or operating with the greatest efficiency etc.

A value (or collection of values) that should be captured to demonstrate the effectiveness of an aspect of the governance program is documented using the *GovernanceMetric* entity.  

The associated measurements for the metric an either be stored in a data source such as a database or file, particularly if it is a lot of data or captured in a classification attached to the element that the data values describe.

![UML](0450-Governance-Rollout.svg)

## GovernanceRule entity

The *GovernanceRule* entity defines an executable rule that can be deployed at particular points in the processing.
It is a type of [GovernanceControl](/types/4/0420-Governance-Controls).

## DataQualityRule entity

The *DataQualityRule* entity is a type of *GovernanceRule* that describes a check on the quality of data, for example that a data field has no null values or that a data set has an expected number of rows.  It captures the check in the terms used by data contract standards such as the [Open Data Contract Standard (ODCS)](https://bitol.io), so that a check declared in a contract can be catalogued, governed and regenerated.  The rule is typically linked to the [data structure or data field](/types/5/0580-Data-Dictionaries) it checks using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.

* *qualityDimension* - The dimension of quality being checked, for example accuracy, completeness, conformity, consistency, coverage, timeliness or uniqueness.
* *checkType* - The type of data quality check: text (described for humans), library (a standard metric), sql (a query) or custom (run by a named engine).
* *metric* - The name of the standard metric evaluated by a library check, for example nullValues, missingValues, invalidValues, duplicateValues or rowCount.
* *severity* - The severity of a failure of the rule, for example info, warning or error.
* *businessImpact* - The business impact of a failure of the rule, for example operational or regulatory.
* *method* - How the check is performed.
* *units* - The units of measure of the measured value, for example rows, percent or a currency.
* *schedule* - The schedule configuration for the scheduler, for example a cron expression.
* *scheduler* - The name of the scheduler that runs the check, for example cron.
* *expression* - The query or expression evaluated by a sql check.
* *qualityEngine* - The name of the engine that runs a custom check, for example soda or great-expectations.
* *comparisonOperator* - The operator used to compare the measured value with the threshold values, for example mustBe, mustNotBe, mustBeGreaterThan, mustBeGreaterOrEqualTo, mustBeLessThan, mustBeLessOrEqualTo, mustBeBetween or mustNotBeBetween.
* *thresholdValues* - The threshold values that the measured value is compared with.  Most operators take one value; the between operators take two.

## GovernanceMetric entity

An important aspect of the governance program is the ability to measure its effectiveness and identify the activities that are delivering the highest value, or operating with the greatest efficiency etc.

A value (or collection of values) that should be captured to demonstrate the effectiveness of an aspect of the governance program is documented using the *GovernanceMetric* entity.  This is a type of [GovernanceControl](/types/4/0420-Governance-Controls).

The associated measurements for the metric an either be stored in a data source such as a database or file, particularly if it is a lot of data or captured in a classification attached to the element that the data values describe.

* *measurement* - Format or description of the measurements captured for this metric.
* *target* - Definition of the measurement values that the governance definitions are trying to achieve.

## GovernanceExpectations classification

The calculation of governance metrics is often a summary of many other measurements each associated with different resources (such as data sources and processes).
These resources are catalogued as [Assets](/types/0/0010-Base-Model).
The definition of their expected behaviour or content can be captured using the *GovernanceExpectations* classification attached to their Asset.

* *counts* - A set of metric name to count value pairs.
* *values* - A set of metric name to string value pairs.
* *flags* - A set of metric name to boolean value pairs.
* *dates* - A set of metric name to date value pairs.

## GovernanceMeasurements classification

The measurements that support the assessment of a particular resource can be gathered and stored in a *GovernanceMeasurements* classification attached to its Asset.

* *dataCollectionStartTime* - If the data is bound by time, this is the start time.
* *counts* - A set of metric name to count value pairs.
* *values* - A set of metric name to string value pairs.
* *flags* - A set of metric name to boolean value pairs.
* *dates* - A set of metric name to date value pairs.
* *dataCollectionEndTime* - If the data is bound by time, this is the end time.

## GovernanceResults relationship

Alternatively, if it is easier to gather the measurements in an external data source, the asset that describes this data source can be linked to the appropriate governance metrics using the *GovernanceResults* relationship.

The *queryType* and *query* attributes of this relationship capture the query used to retrieve the relevant data for the metric.

* *query* - Query used to extract data, can include placeholders.
* *queryType* - Type of query used to extract data.

--8<-- "snippets/abbr.md"