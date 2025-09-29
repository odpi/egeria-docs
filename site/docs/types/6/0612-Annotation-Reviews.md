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

The *AnnotationReview* entity is a [Review](/types/1/0135-Actions-For-People) entity that records a review of the suitability/quality of the annotations linked as [ActionTargets](/types/0/0013-Actions).


## AnnotationStatus enumeration

The *AnnotationStatus* enumeration describes the status of an annotation review.

--8<-- "snippets/abbr.md"