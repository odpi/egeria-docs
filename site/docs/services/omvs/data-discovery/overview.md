
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Data Discovery API

The Data Discovery API provides a REST API to support user interfaces (UIs)
relating to the discovery and analysis of digital resources (assets) and their data.
It enables external survey and analysis engines (such as data quality analysers) to load their findings
into open metadata.

## Key concepts

The Data Discovery API supports the following key concepts:

* **Survey Reports**: Capture the analysis of IT resources and data from a specific run of a survey engine.
* **Annotations**: Individual findings within a survey report. These can be linked to the elements they describe,
  associated with previous runs for trend analysis, or used to trigger governance actions.

## Further information

* [Survey Reports and Annotation Concepts](https://egeria-project.org/concepts/survey-report/)

Sample requests for the REST API can be found in Egeria-api-data-discovery.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-discovery/Egeria-api-data-discovery.http).


---8<-- "snippets/abbr.md"






