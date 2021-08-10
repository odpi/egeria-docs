<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Set up the default event bus

An [OMAG server](/egeria-docs/concepts/omag-server) uses an event bus such as [Apache Kafka :material-dock-window:](https://kafka.apache.org){ target=kafka }
to exchange events with other servers and tools.

Egeria manages the specific topic names and the event payloads;
however, it needs to know where the event bus is deployed and
any properties needed to configure it.

Since the event bus is used in multiple places,
the configuration document allows you to set up the details of the event bus
which are then incorporated into all the places where the event bus is needed.

!!! attention "Important sequencing information"
    You need to set up this information before configuring any of the following:

    - Using an event topic as the destination for the [audit log](/egeria-docs/concepts/audit-log).
    - Configuring the [access services](/egeria-docs/services/omas) in a
      [metadata server](/egeria-docs/concepts/metadata-server) or
      a [metadata access point](/egeria-docs/concepts/metadata-access-point).
    - Configuring registration to a [cohort](/egeria-docs/services/omrs/cohort) in a
      [metadata server](/egeria-docs/concepts/metadata-server),
      a [metadata access point](/egeria-docs/concepts/metadata-access-point),
      a [repository proxy](/egeria-docs/concepts/repository-proxy) or
      a [conformance test server](/egeria-docs/concepts/conformance-test-server).

The following command creates information about the event bus.
This information is used on the subsequent configuration of the OMAG server subsystems.
It does not affect any subsystems that have already been configured in the configuration document
and if the event bus is not needed, its values are ignored.

It is possible to add arbitrary name/value pairs as JSON in the
request body.  The correct properties to use are defined in the connector type for the event bus.

!!! post "POST - configure event bus"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/event-bus
    ```

???+ example "Example: Apache Kafka"
    For example, when using Apache Kafka as your event bus you may want to configure properties that
    control the behavior of the consumer that receives events and the producer that sends events.
    This is a typical set of producer and consumer properties:

    ```json linenums="1"
    {
    	"producer": {
    		"bootstrap.servers":"localhost:9092",
    		"acks":"all",
    		"retries":"0",
    		"batch.size":"16384",
    		"linger.ms":"1",
    		"buffer.memory":"33554432",
    		"max.request.size":"10485760",
    		"key.serializer":"org.apache.kafka.common.serialization.StringSerializer",
    		"value.serializer":"org.apache.kafka.common.serialization.StringSerializer",
    		"kafka.omrs.topic.id":"cocoCohort"
    	},
    	"consumer": {
       		"bootstrap.servers":"localhost:9092",
       		"zookeeper.session.timeout.ms":"400",
       		"zookeeper.sync.time.ms":"200",
       		"fetch.message.max.bytes":"10485760",
       		"max.partition.fetch.bytes":"10485760",
       		"key.deserializer":"org.apache.kafka.common.serialization.StringDeserializer",
       		"value.deserializer":"org.apache.kafka.common.serialization.StringDeserializer",
       		"kafka.omrs.topic.id":"cocoCohort"
    	}
    }
    ```

    A different type of event bus would use different properties.
