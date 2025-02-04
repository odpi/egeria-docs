<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0210 Data Stores

[*DataSets*](#dataset-entity), [DataFeeds](#datafeed-entity) and [*DataStores*](#datastore-entity) are types of [*DataAsset*](/types/0/0010-Base-Model#dataset) that represent a collection of data.  The *DataStore* is a physical store, whereas the *DataFeed* is a continual supply of data and *DataSet* is dynamically constructed on request.  This model introduces the *DataContentForDataSet* relationship that shows how *DataSets* are constructed from other [Assets](/types/0/0010-Base-Model).

![UML](0210-Data-Stores.svg)

### DataSet entity

*DataSet* represents a collection of related data. This data does not need to be stored together. The *formula* property describes the logic used to populate the DataSet, *formulaType* describes the notation language used to describe the formula, and *deployedImplementationType* describes the class of technology that this data set belongs to.

## DataStore entity

The *DataStore* entity describes a physical [digital resource](/concepts/digital-resource) that supplies data.  The *deployedImplementationType* attribute describes the class of technology that is used in its implementation.  Values for the *deployedImplementationType* attribute can be managed for consistency in a [*deployed implementation type*](/concepts/deployed-implementation-type) valid value set.

## DataFeed entity

*DataFeed* identifies an asset that provides a continuous feed of data. The *deployedImplementationType* attribute describes the class of technology that is used in its implementation. Values for the *deployedImplementationType* attribute can be managed for consistency in a [*deployed implementation type*](/concepts/deployed-implementation-type) valid value set.

## DataContentForDataSet relationship

The *DataContentForDataSet* relationship defines how data is supplied to a [DataSet](/types/0/0010-Base-Model) from a particular [digital resources](/concepts/digital-resource).  The DataSet entity includes a property called *formula*.  This describes the logic that is used to populate the data set.  The formula can include placeholders.  These placeholders are defined by the *queryId* properties in the linked DataContentForDataSet relationships.  The associated *query* property describes how the data from the linked dataContent resource is selected and *queryType* identifies the language that the query is written in.

## DataAssetEncoding classification

The *DataAssetEncoding* classification provides the ability to store details of the data asset's format.

## DataScope classification

The *DataScope* classification identifies the scope of the data stored in the [digital-resource(s)](/concepts/digital-resource) represented by the entity it is attached to.  This classification can be attached to any [*Referenceable*](/types/0/0010-Base-Model), but it is typically associated with assets such as *DataStores* and *DataSets*.  The attributes of this classification identify the scope of the data in space and time.

* *minLongitude* - if the data is bound by an area, this is the longitude for bottom-left corner of the bounding box (BBOX) for the area covered by the data.
* *minLatitude* - if the data is bound by an area, this is the latitude for the bottom-left corner of the bounding box (BBOX) for the area covered by the data.
* *maxLongitude* - if the data is bound by an area, this is the longitude for top-right corner of the bounding box (BBOX) for the area covered by the data.
* *maxLatitude* - if the data is bound by an area, this is the latitude for top-right corner of the bounding box (BBOX) for the area covered by the data.
* *minHeight* - if the height above ground is relevant, this is the lowest height that the data covers.
* *maxHeight* - if the height above ground is relevant, this is the highest height that the data covers.
* *dataCollectionStartTime* - if the data is bound by time, this is the start time.
* *dataCollectionEndTime* - if the data is bound by time, this is the end time.
* *additionalProperties* - to support other properties that identify the scope of the data represented by this element.

??? deprecated "Deprecated types"
    * The *DataStoreEncoding* classification is deprecated in favour of *DataAssetEncoding* to allow encoding information to be attached to data sets and data feeds.

--8<-- "snippets/abbr.md"