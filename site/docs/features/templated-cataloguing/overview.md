
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Templated cataloging

--8<-- "snippets/features/templated-cataloguing/templated-cataloguing-intro.md"

## An example

--8<-- "snippets/features/templated-cataloguing/templated-cataloguing-example.md"

## The scope of a template

The scope of a template is controlled by the [Anchors classification](/features/anchor-management/overview).  In the picture below, the elements in blue represent the scope of the template.  The elements in white show the new elements created from the template.  The relationships to the elements in green are duplicated during the templating process, but the green elements themselves are not duplicated. 

![The scope of the template](template-scope.svg)

Ths means it is possible to navigate from, say the license, to each of the assets bound by the terms of the license.



## Support for templated cataloguing

The [Template Manager OMVS](/services/omvs/template-manager/overview) provides the ability to set up templates and the [Automated Curation OMVS](/services/omvs/automated-curation/overview)  provides the ability to locate and use templates to catalog new assets.

## Adding automation

It is also possible to use templates in the integration connectors running during [Integrated cataloguing](/feaatures/integrated-cataloguing).  The connector is typically passed the qualified names of the templates that it should use in the [CatalogTarget](/types/4/0464-Dynamic-Integration-Groups) relationship.

--8<-- "snippets/abbr.md"