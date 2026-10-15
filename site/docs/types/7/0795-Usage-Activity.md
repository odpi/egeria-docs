

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# 0795 - Usage Activity

The classifications below are used to gather statistics about usage activity around an element.

![UML](0795-Usage-Activity.svg)

## UsageActivity classification

The *UsageActivity* classification is used to describe the usage activity around an anchor element.  It is typically associated with an [Asset](/types/0/0010-Base-Model), [DigitalProduct](/types/7/0710-Digital-Products) or [GlossaryTerm](/types/3/0330-Terms).  It captures the following data related to the activity around itself and its anchored elements:

* *explicitGetCount* - the number of times the element, or one of its anchored elements, has been explicitly retrieved from the repository by an identifier or name.  This indicates that it is an element of specific interest to the calling user.
* *findCount* - the number of times the element, or one of its anchored elements, has been retrieved from the repository as part of a search request.  This indicates the element's findability.
* *updatePropertyCount* - the number of times the properties for an element have been updated in the repository.
* *updateAttachmentCount* - the number of times non-feedback anchored elements have been created, attached, detached, or updated in the repository.
* *updateFeedbackCount* - the number of times feedback for this element have been created or updated in the repository.
* *deleteAttachmentCount* - the number of times non-feedback anchored elements have been deleted from the repository.
* *deleteFeedbackCount* - the number of times feedback for this element has been deleted from the repository.

## MemberPopularityProfile classification

The *MemberPopularityProfile* classification is used to describe the usage activity around a grouping of elements.  It is typically attached to a [Collection](/types/0/0021-Collections) and summarizes the usage activity around the members of the collection.  It captures the following data related to the activity around its members:

* *explicitGetCountTotal* - the number of times any of the element's members have been explicitly retrieved from the repository by an identifier or name.
* *explicitGetCountProfile* - a map of member GUID to the number of times that member has been explicitly retrieved from the repository by an identifier or name.
* *findCountTotal* - the number of times any of the element's members have been retrieved from the repository as part of a search request.
* *findCountProfile* - a map of member GUID to the number of times that member has been retrieved from the repository as part of a search request.
* *updatePropertyCountTotal* - the number of times any of the element's members have had their properties updated in the repository.
* *updatePropertyCountProfile* - a map of member GUID to the number of times that a member's properties have been updated in the repository.
* *updateAttachmentCountTotal* - the number of times non-feedback anchored elements for any of the element's members have been created, attached, detached, or updated in the repository.
* *updateAttachmentCountProfile* - a map of member GUID to the number of times that a member's non-feedback attachments have been updated in the repository.
* *updateFeedbackCountTotal* - the number of times feedback for any of the element's members have been created or updated in the repository.
* *updateFeedbackCountProfile* - a map of member GUID to the number of times that a member's feedback attachments have been updated in the repository.
* *deleteAttachmentCountTotal* - the number of times non-feedback anchored elements for any of the element's members have been deleted from the repository.
* *deleteAttachmentCountProfile* - a map of member GUID to the number of times that a member's non-feedback attachments have been deleted from the repository.
* *deleteFeedbackCountTotal* - the number of times feedback for any of the element's members have been deleted from the repository.
* *deleteFeedbackCountProfile* - a map of member GUID to the number of times that a member's feedback attachments have been deleted from the repository.



--8<-- "snippets/abbr.md"