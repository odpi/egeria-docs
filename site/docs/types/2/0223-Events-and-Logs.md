<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0223 Events and Logs

Processing is often triggered when a specific event or situation occurs.  There are also sources of data that provide a continuous feed of data - for example a sensor monitoring the temperature.  This model introduces the different types of [*Assets*](/types/0/0010-Base-Model/#asset) associated with events and continuous data feeds.

![UML](0223-Events-and-Logs.svg)

## DataFeed

*DataFeed* identifies an asset that provides a continuous feed of data.

## Topic

A *Topic* is a type of [*DataSet*](/types/0/0010-Base-Model/#dataset) that is accessed using a publish-subscribe event interface.  There are processes that add events to the topic, and other processes that subscribe to the topic and receive a copy of each event that is added.  It is shown as a data set because some topics are in memory and some make use of an underlying [*DataStore*](/types/2/0210-Data-Stores) to provide a persistent/reliable delivery service. 

## KafkaTopic

[Apache Kafka](https://kafka.apache.org/) is a popular open source technology that provides support for *Topics*.  There is a specific type for an Apache Kafka topic because there is a [resource connector](/contectors/resource/kafka-open-metadata-topic-connector) for Apache Kafka and this type identifies when it is appropriate to use this connector to access the topic contents.

## SubscriberList and TopicSubscribers

Some services manage a specific subscriber list.  This is represented by the *SubscriberList* entity type.  The links to the topics that the subscription refers to is represented by the *TopicSubscribers* relationship type.

## LogFile

A *LogFile* is a subtype of [*DataFile*]() that contains events.

## AssociatedLog



--8<-- "snippets/abbr.md"