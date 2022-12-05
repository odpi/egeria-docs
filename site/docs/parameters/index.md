<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Parameters and data properties used by Egeria

Egeria's APIs and event payloads use consistent names for many of its parameters/data fields.

- [effectiveTime](#effectivetime)
- [externalSourceGUID](#externalsourceguid-and-externalsourcename)
- [externalSourceName](#externalsourceguid-and-externalsourcename)
- [extendedProperties](#typename-and-extendedproperties)

- [forDuplicateProcessing](#forduplicateprocessing)
- [forLineage](#forlineage)

- [isMergeUpdate](#ismergeupdate)

- [mappingProperties](#mappingproperties)

- [name](#name)

- [pageSize](#startfrom-and-pagesize)

- [searchString](#searchstring)

- [startFrom](#startfrom-and-pagesize)

- [templateGUID](#templateguid-and-templateproperties)
- [templateProperties](#templateguid-and-templateproperties)
- [typeName](#typename-and-extendedproperties)

### effectiveFrom and effectiveTo



### effectiveTime

The `effectiveTime` date parameter is used when retrieving elements.  It specifies the time that elements must be [effective](/features/effectivity-dates/overview) in order to be returned on the request.  A null value means that the effectivity dates of the element are ignored.  

### externalSourceGUID and externalSourceName


### forDuplicateProcessing

The `forDuplicateProcessing` boolean parameter indicates whether the caller is part of the deduplication governance function or not.  Most callers set `forDuplicateProcessing` to `false`.  When it is true, all the automated merging of identified duplicate elements is skipped and the elements are returned as stored.  This allows the deduplication function to set up the relationships and classifications that control the deduplication process.

### forLineage

The `forLineage` flag is set by callers that are working with lineage.  Most callers will set this value to `false`.  It is used when retrieving elements to determine whether to return elements with the [*Memento*](/concepts/memento) classification.  The Memento classification indicates that the corresponding [digital resource](/concepts/resource) has been removed, and the metadata element has only been retained to support the linkage in a lineage graph.  

When `forLineage=false` elements with the Memento classification are not returned; when `forLineage=true` they are returned.

### templateGUID and templateProperties


### startFrom and pageSize
### name
### searchString
### isMergeUpdate

### typeName and extendedProperties


### externalId

### additionalProperties

### vendorProperties


--8<-- "snippets/abbr.md"