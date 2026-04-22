<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Lineage

Lineage shows how data and control flows from its origins to its various destinations. This includes details of the processing along the way.  It is used to understand:
 
* whether the data used in reports and analytics models has come from the correct sources and has passed through the correct processing (known as *traceability of data*).
  
* what would be the impact on downstream processing and consumers if something was changed (known as *impact analysis*).

* whether the operational processes that implement the data flows are executing correctly (known as *governance by expectation*).

[Lineage Management](/features/lineage-management/overview) describes how lineage is collected, managed and used in Egeria.

???+ info "Further information"

    The open metadata types for lineage relationships are found in the following models:

    * [Model 0210](/types/2/0210-Data-Stores) for the DataSetContent relationship.
    * [Model 0737](/types/7/0737-Solution-Implementation) for the ImplementedBy relationship
    * [Model 0750](/types/7/0750-Data-Passing) for the DataFlow, ProcessCall and ControlFlow relationships.
    * [Model 0755](/types/7/0755-Ultimate-Source-Destination) for the UltimateSource and UltimateDestination relationships.
    * [Model 0760](/types/7/0760-Business-Lineage) for the BusinessLineage classification.
    * [Model 0770](/types/7/0770-Lineage-Mapping) for the LineageMapping and DataMapping relaitonships.

    Also see how to set up an [information supply chain](/concepts/information-supply-chain).

--8<-- "snippets/abbr.md"