<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0210 Data Stores

Both [*DataSets*](/types/0/0010-Base-Model#dataset) and [*DataStores*](#datastore) are types of [*Asset*](/types/0/0010-Base-Model#dataset) that represent a collection of data.  The *DataStore* is a physical store, whereas the *DataSet* is dynamically constructed on request.  This model introduces the *DataStore* and the relationship that shows how *DataSets* are constructed from them.

![UML](0210-Data-Stores.svg)

## DataStore entity

The *DataStore* entity describes a physical [digital resource](/concepts/resource) that supplies data.  The *deployedImplementationType* attribute describes the technology that is used in its implementation.

## DataContentForDataSet relationship

The *DataContentForDataSet* relationship defines how data is supplied to a [DataSet](/types/0/0010-Base-Model) from a particular [digital resources](/concepts/resource).  The DataSet entity includes a property called *formula*.  This describes the logic that is used to populate the data set.  The formula can include placeholders.  These placeholders are defined by the *queryId* properties in the linked DataContentForDataSet relationships.  The associated *query* property describes how the data from the linked dataContent resource is selected.

## DataStoreEncoding classification

The *DataStoreEncoding* classification provides the ability to store details of the data stores physical characteristics.


--8<-- "snippets/abbr.md"