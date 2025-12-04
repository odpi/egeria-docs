<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0535 Event Schemas

[Events](/concepts/basic-concepts/#event) capture the details of a specific situation or activity.  They are sent between services, often using an intermediary, such as an [Event Broker](/concepts/basic-concepts/#event-broker).  Event schemas provide the means to share the structure of the information flowing in the events.  They are typically attached to [*Topics*](/types/2/0223-Events-and-Logs).

![UML](0535-Event-Schemas.svg)

## EventType

An event schema begins with an *EventType* entity at its root.  It is linked to the asset using the [*Schema*](/types/5/0503-Asset-Schema) relationship.

The data fields in the event are represented using *EventSchemaAttribute* entities that are linked to the event type using the [*AttributeForSchema*](/types/5/0505-Schema-Attributes) relationship.

## EventSchemaAttribute

*EventSchemaAttribute* describes a data field or structure in an event schema.  The data type of the data field is stored in an attached [*TypeEmbeddedAttribute*](/types/5/0505-Schema-Attributes) classification.  If the data field is a structure, the *typeName* property in *TypeEmbeddedAttribute* is set to `StructSchemaType` and the nested data fields, represented by their own *EventSchemaAttribute* entities, are linked via the [*NestedSchemaAttribute*](/types/5/0505-Schema-Attributes) relationship.

In the example below, *EventTypeList* is linked to the asset (*KafkaTopic* in this case) via the *Schema* relationship and the event types represent each event option.  The *EventType* entities are linked to the *EventTypeList* using the *SchemaTypeOption* relationship.

![Schema for the Asset Manager OMAS Event](json-event-example.svg)

## EventTypeList

*EventTypeList* provides an entity that holds a list of event types.  It is used for an asset that produces events of different types.

![Event Type List](event-type-list.svg)

## EventSet

*EventSet* provides a specialized [*Collection*](/types/0/0021-Collections) to gather a collection of event schema definitions that are related.  The event schemas are represented by the *EventType* entity and linked to the *EventSet* using the *CollectionMembership* relationship.

![Event Sets](event-set.svg)
> An example of an event set showing the event types used in the Open Metadata Access Services (OMAS) Out Topics.




--8<-- "snippets/abbr.md"