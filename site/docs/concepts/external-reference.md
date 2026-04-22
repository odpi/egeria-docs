<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# External references

Most elements in open metadata include a [URL attribute](/types/0/0010-Base-Model).  This allows a link to an additional source of information to be included in the metadata element.  For example, a metadata element describing a software component such as a connector may include a URL that points to its implementation or design document on a site like GitHub.

Some external sources are significant in their own right.  Open metadata supports elements called external references that describe the information in these external sources.  They can then be listed in [collections](/concepts/collection) or referenced directly by other metadata elements.

There are six types of external references:

* [External Reference (generic)](#external-reference)
* [External Data Source](#external-data-source)
* [External Model Source](#external-model-source)
* [External Source Code](#external-source-code)
* [Cited Document](#cited-document)
* [Related Media](#related-media)


A list of external references can be attached to any [referenceable](/concepts/referenceable) such as
a [personal profile](/concepts/personal-profile),
a [community](/concepts/community),
a [team](/concepts/organizations/#team),
a [governance definition](/concepts/governance-definition),
or an [asset](/concepts/asset).

The [External Links API](/services/omvs/external-links/overview) supports the create and maintenance of all external reference types.  External references can also be organized into [collections](/concepts/collection) for easier management and discovery.  Collections are maintained by the [Collection Manager API](/services/omvs/collection-manager/overview).

## External Reference

*ExternalReference* is the generic type for all external references.  It is typically used directly to describe web pages.

The *ExternalReferenceLink* relationship is used to connect the external reference to a related metadata element.  This relationship is a [multi-link](/concepts/uni-multi-link) so the related element can link to the external reference multiple times with different labels and descriptions.

## External Data Source

An *ExternalDataSource* element is a type of external reference that describes a data source such as a digital product or data set in an external data catalog or marketplace.  The URL in the link to the catalog entry page for the data source.  External data sources are also linked to their related elements using *ExternalReferenceLink* relationships.  This may be, for example, the equivalent [digital product description](/concepts/digital-product) in the open metadata ecosystem, or a [project](/concepts/project) that is using the external data source.

If an [asset](/concepts/asset) describes a [digital resource](/concepts/digital-resource) that is derived from the external data source, the asset should be linked to the external data source using a [lineage relationship](/concepts/lineage) such as [*DataFlow*]() or *DataSetContent*.

## External Model Source

An *ExternalModelSource* element is a type of external reference that describes a model source in a marketplace or library. The URL in the link to the catalog entry page for the model source.  External model sources are also linked to their related elements using *ExternalReferenceLink* relationships.  This may be, for example, the equivalent [digital product description](/concepts/digital-product) in the open metadata ecosystem, or a [asset](/concepts/asset) that is using the external model source.

Most external models are downloaded and deployed locally to allow for training and to keep the data it is using secure.  If, however, the external model is being called by one of your processes, represented by the [Process](/concepts/process) element, then the external model source should be linked to the process using a lineage relationship such as [DataFlow](/concepts/lineage#DataFlow) .

## External Source Code

An *ExternalSourceCode* element is a type of external reference that describes the source code for a software component. External source code elements are also linked to their related elements using *ExternalReferenceLink* relationships.

## Cited Document

A *CitedDocument* element is a type of external reference that describes a multi-section document.  The related elements are linked to the cited document using *CitedDocumentLink* relationship which allows the relevant section to be identified.

## Related Media

The *RelatedMedia* is a special type of external reference that describes a media file such as an image or video file.  The related elements are linked to the cited document using *CitedDocumentLink* relationship which allows the intended use of the media to be identified.

???+ info "Further information"

    * [Model 0014](/types/0/0014-External-References) describes the open metadata types for external references, external data sources, external model sources, and external source code.
    * [Model 0015](/types/0/0015-Linked-Media-Types) describes the open metadata types for related media such as images and videos.
    * [Model 0016](/types/0/0016-Cited-Documents) describes the open metadata types for cited documents.
    * [Assessing a new Regulation](/egeria-solutions/assessing-new-regulation/overview) describes the use of external references to gather information and references for a regulation in preparation to understand its requirements and then develop policies and controls to comply with it.


--8<-- "snippets/abbr.md"
