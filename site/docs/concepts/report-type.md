<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Report Type

A *report type* is the template for generating a [report](/concepts/report).  It is the definition; the report is the instance produced from it on a particular occasion.

Separating the two matters because most reports are produced repeatedly.  The report type describes what the report will always contain, and each report produced from it records what was actually found for a specific period.  Consumers of the report can therefore understand the shape of the content before any report has been run, and reports produced at different times can be compared with confidence because they were generated from the same definition.

## What a report type describes

A report type is a specialized [data specification](/concepts/data-specification).  This means its content is described in the same way as the data requirements for any other digital service: using [data structures](/concepts/data-structure) and [data fields](/concepts/data-field), linked to [glossary terms](/concepts/glossary-term) for their meaning and to [data value specifications](/concepts/data-value-specification) for the values they may take.

It also records:

* *createdTime* - when the report type was defined.
* *lastModifiedTime* and *lastModifier* - when the definition was last changed, and by whom.

Because a report type is a [collection](/concepts/collection), the supporting material for the report - its documentation, related [external references](/concepts/external-reference) and the governance definitions that apply to it - can be gathered inside it.

???+ info "Additional information"
    * The *ReportType* type is described in [Model 0239 Reports](/types/2/0239-Reports).
    * The [Data Designer API](/services/omvs/data-designer/overview) provides the operations for building the data structures and fields that make up the report type's specification.

--8<-- "snippets/abbr.md"
