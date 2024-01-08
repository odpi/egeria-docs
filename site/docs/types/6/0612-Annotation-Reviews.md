<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0612 Annotation Reviews

The annotations associated with an asset can be seen by
people and tools querying the associated asset, their elements or
the controlling engine action.
However, the analysis within a survey analysis service may
only be able to make recommendations based on the information within the resource.
Where annotations refer to information that is used for governance,
they need to be approved and converted into classifications,
or related metadata.


![UML](0612-Annotation-Reviews.svg)

## AnnotationReview entity

The *AnnotationReview* entity records how the discovered annotations
have been actioned in the metadata server and the steward that
approved it.

## AnnotationReviewLink relationship

The *AnnotationReviewLink* relationship links an annotation to its review.

## AnnotationStatus enumeration

The *AnnotationStatus* enumeration describes the status of an annotation review.

--8<-- "snippets/abbr.md"