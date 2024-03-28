<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0223 Events and Logs

Processing is often triggered when a specific event or situation occurs.  There are also sources of data that provide a continuous feed of data - for example a sensor monitoring the temperature.  This model introduces the different types of [*Assets*](/types/0/0010-Base-Model/#asset) associated with events and continuous data feeds.

![UML](0223-Events-and-Logs.svg)

## DataFeed entity

*DataFeed* identifies an asset that provides a continuous feed of data. The *deployedImplementationType* attribute describes the class of technology that is used in its implementation. Values for the *deployedImplementationType* attribute can be managed for consistency in a [*deployed implementation type*](/concepts/deployed-implementation-type) valid value set.

## Topic entity

A *Topic* is a type of [*DataSet*](/types/0/0010-Base-Model/#dataset) that is accessed using a publish-subscribe event interface.  There are processes that add events to the topic, and other processes that subscribe to the topic and receive a copy of each event that is added.  It is shown as a data set because some topics are in memory and some make use of an underlying [*DataStore*](/types/2/0210-Data-Stores) to provide a persistent/reliable delivery service.

The additional attributes for *Topic* are:

* *topicName* holds the fully qualified name of the topic.  This frees up the *name* property to hold a shorter, more human-readable name.
* *topicType* identifies the type of topic.  This may refer to its reliability or other features supported by the event broker.

## KafkaTopic entity

[Apache Kafka](https://kafka.apache.org/) is a popular open source technology that provides support for *Topics*.  There is a specific type for an Apache Kafka topic because there is a [resource connector](/contectors/resource/kafka-open-metadata-topic-connector) for Apache Kafka and this type identifies when it is appropriate to use this connector to access the topic contents.

## SubscriberList entity and TopicSubscribers relationship

Some services manage a specific subscriber list.  This is represented by the *SubscriberList* entity type.  The links to the topics that the subscription refers to is represented by the *TopicSubscribers* relationship type.

## LogFile entity

A *LogFile* entity is a subtype of [*DataFile*](/types/2/0220-Files-and-Folders) that contains events that have been captured and stored. The *purpose* attribute describes the use of log file - for example, it is a debug log, audit log, ....

## AssociatedLog relationship

The *AssociatedLog* relationship shows the [Asset](/types/0/0010-Base-Model) (typically a *LogFile*) where logging information for the linked [Referenceable](/types/0/0010-Base-Model) is located.


--8<-- "snippets/abbr.md"