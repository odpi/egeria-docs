<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Promise

A *Promise* is a classification that indicates that the element it is attached to describes a [real-world digital resource](/concepts/digital-resource) that has not yet been delivered.  The element is a commitment (a promise) that the resource will exist, rather than a description of something that is available today.

Promise elements are created when the lineage graph is being designed ahead of the resources it describes.  For example, an information supply chain may show a new data set being produced by a process that is still under development.  Cataloguing the data set with the *Promise* classification allows the lineage relationships to be created and reviewed before the resource is built, and lets consumers see what is coming.

The element is not returned to callers unless the caller specifies the *forLineage* parameter.  If it is set to `true`, the *Promise* classification is ignored and the element is returned.  This prevents a promised resource appearing in catalog searches as if it were ready to use.

The properties of the classification record the delivery plan:

* *deploymentStatus* and *userDefinedDeploymentStatus* - how far the delivery has progressed.
* *startTime* - when work on the resource started.
* *dueTime* - when the resource is expected to be delivered.
* *lastReviewTime* - when the delivery progress was last reviewed.
* *completionTime* - when the resource was delivered.

Once the resource is delivered, the *Promise* classification is removed and the element becomes visible to all callers.  The classification can be attached to any [OpenMetadataRoot](/types/0/0010-Base-Model/#openmetadataroot-entity) entity.

## Managing promises

The [Classification Explorer API](/services/omvs/classification-explorer/overview) provides the operations to add and remove the classification:

* `setElementAsPromise` adds the *Promise* classification, with its delivery plan properties, to an existing element.  From that point the element is only returned to lineage requests.
* `clearElementAsPromise` removes the classification once the resource has been delivered.  The request must set `forLineage=true`, because the promised element is invisible to the request otherwise.

A promised element still reserves its *qualifiedName*.  A request to create another element with the same unique name fails while the promise is in place, which stops a second catalog entry being created for the resource when it is finally delivered.  This is different from a *Memento* element, whose unique name is released for reuse.

Elements with the *Promise* classification are shown with their own visual style in Egeria's [mermaid](/user-interfaces/mermaid/overview) graphs, so that planned resources are easy to distinguish from those that are available.

## Promise and Memento

*Promise* and [*Memento*](/concepts/memento) mark the two ends of an element's life in a lineage graph:

* A *Promise* element describes a resource that does not exist yet.
* A *Memento* element describes a resource that no longer exists.

Both are hidden from normal catalog queries and both are returned when `forLineage=true`, so that the lineage graph remains complete from the planned origins of the data through to resources that have since been retired.

!!! info "Open Metadata Types"
    The definition for the *Promise* classification is found in the [0010 Base Model](/types/0/0010-Base-Model/#promise-classification)


--8<-- "snippets/abbr.md"
