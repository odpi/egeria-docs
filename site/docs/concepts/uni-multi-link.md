<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Relationship Linkage Rules (Relationship Category)

Relationships have a cardinality.  This determines, when starting from a particular element, how many relationships of a particular type are allowed.  If multiple (many) relationships are permitted. the relationship category further controls how many relationships of a specific type are permitted between two elements.

## Uni-link relationships

This is the default category, and most common setting. *Uni-link* means only one relationship of this type can be connected between two element instances in a specific direction. If a second relationship is connected between them in a specific direction, the properties of the original relationship are simply updated.

![Uni-link Relationship Diagram](uni-link-relationship-category.svg)

## Reversible relationships

*Reversible* means a relationship can be created in both directions between two elements.  However, only one relationship will be stored and later "creates" will simply update the properties of the original relationship.  A reversible relationship is defined by setting the attribute name of either end to be the same value.

![Reversible Relationship Diagram](reversible-relationship-category.svg)

## Multi-link relationships

*Multi-link* means multiple instances of the relationship may be present between two elements.  In this case, the relationship properties are key in identifying the significance of each relationship instance.  A multi-link relationship is defined using the milti-link boolean setting in the relationship definition.

![Multi-link Relationship Diagram](multi-link-relationship-category.svg)


--8<-- "snippets/abbr.md"

