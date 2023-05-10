<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Example Audit & Logging Configuration (json)

In this example:
 - Egeria platforms, hosting servers, are running within Kubernetes
 - Output from pods will be monitored by logging tools that work best with JSON format logs

We therefore want to 
 - configure the Egeria Audit Log to output JSON format to the console
 - ensure logging output from other non-egeria components is also sent to the console in JSON format

See [OMAG Server Platform Logging](omag-server-platform-logging.md) for more information on configuration.

## Approach

By default, 
 - The Egeria Audit Logs for each server will be written to the console in plain text
 - Any other logging within the server chassis will use slf4j-api, or will have an adapter within the executable that maps from other logging frameworks to slf4j-api
 - In the server chassis we use Logback classic as the standard slf4j-api implementation

Therefore the simplest approach we will take is to
 - configure the Egeria audit log to use slf4j-api
 - create a logback configuration file which outputs in json.

An alternative would be to use a different slf4j-api implementation, such as log4j2 (making sure to exclude logback), and configure that to output in json.

## Detailed steps
### Define a logback configuration file

Create the following file and place it in a well known directory:
``` xml
<!-- Example logging configuration for logback. Requires additional libraries -->
<configuration>
<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <layout class="ch.qos.logback.contrib.json.classic.JsonLayout">
        <jsonFormatter class="ch.qos.logback.contrib.jackson.JacksonJsonFormatter">
            <prettyPrint>false</prettyPrint>
        </jsonFormatter>
        <timestampFormat>yyyy-MM-dd' 'HH:mm:ss.SSS</timestampFormat>
        <appendLineSeparator>true</appendLineSeparator>
        <includeContextName>false</includeContextName>
    </layout>
</appender>

<logger name="jsonLogger" level="TRACE">
    <appender-ref ref="json" />
</logger>

</configuration>
```
### Downloading the additional libraries

The above logback configuration requires some additional libraries for the json output. 

- ch.qos.logback.contrib:logback-jackson
- ch.qos.logback.contrib:logback-json-classic

These can be downloaded from maven central, or built from the [logback contrib project](https://github.com/qos-ch/logback-contrib). Here we'll download directly from maven central.

Download these into a new directory, such as ~/libs/logging
``` bash
wget https://repo1.maven.org/maven2/ch/qos/logback/contrib/logback-jackson/0.1.5/logback-jackson-0.1.5.jar
wget https://repo1.maven.org/maven2/ch/qos/logback/contrib/logback-json-classic/0.1.5/logback-json-classic-0.1.5.jar
```


### Launch the egeria platform

In this example we pass properties as invocation parameters, though these can also be configured in a properties file, or set via environment variables. 

In this case we are running egeria from an unpacked distribution, and so additional libraries are in ./server/lib, whilst the executable jar is in ./server. We also add the location of the additional libraries we downloaded to the loader path (comma separated).

Replace the location of the configuration file as appropriate.

``` bash
java -Dlogging.config=/Users/jonesn/work/json-audit-log/logback-json.xml -Dloader.path=./server/lib,/Users/jonesn/libs/logging -jar server/server-chassis-spring-4.1-SNAPSHOT.jar
```
### Configure a server

Here we configure a simple metadata server as an example. The default audit log is deleted, and a new one created which uses slf4j-api. 

``` bash
#!/bin/sh

# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Egeria project.

# Script will be run by k8s as part of our initialization job.
# Assumed here - platform up & responding to REST api, plus Kafka is available

# Note - expect to port this to python, aligned with our notebook configuration
# - this will facilitate error handling (vs very verbose scripting). Groovy an alternative
# Initial a version a script to get the basics working

EGERIA_ENDPOINT=https://localhost:9443
EGERIA_USER=garygeeke
EGERIA_SERVER=mds1
KAFKA_ENDPOINT=localhost:9092

echo '-- Environment variables --'
env
echo '-- End of Environment variables --'

echo -e '\n-- Configuring platform with requires servers'
# Set the URL root
echo -e '\n\n > Setting server URL root:\n'
curl -f -k --verbose --basic admin:admin -X POST \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/server-url-root?url=${EGERIA_ENDPOINT}"

# Setup the event bus
echo -e '\n\n > Setting up event bus:\n'

curl -f -k --verbose --basic admin:admin \
  --header "Content-Type: application/json" \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/event-bus" \
  --data '{"producer": {"bootstrap.servers": "'"${KAFKA_ENDPOINT}"'"}, "consumer": {"bootstrap.servers": "'"${KAFKA_ENDPOINT}"'"} }'

# Enable all the access services (we will adjust this later)
echo -e '\n\n > Enabling all access servces:\n'

curl -f -k --verbose --basic admin:admin -X POST \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/access-services?serviceMode=ENABLED"

# Use a local graph repo
echo -e '\n\n > Use local graph repo:\n'

curl -f -k --verbose --basic admin:admin -X POST \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/local-repository/mode/local-graph-repository"

# Configure the cohort membership
echo -e '\n\n > configuring cohort membership:\n'

curl -f -k --verbose --basic admin:admin -X POST \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/cohorts/${EGERIA_COHORT}"

# -- Audit log settings

# Remove existing audit log
curl -f -k --verbose --basic admin:admin -X DELETE \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/audit-log-destinations"

# Add slf audit log
# requires library to be downloaded and added to path Identifier
#
# mvn dependency:get -Dartifact=ch.qos.logback.contrib:logback-json-classic:LATEST -Ddest=logback-json-classic.jar

curl -f -k --verbose --basic admin:admin -X POST \
  "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/audit-log-destinations/SLF4J"

# Start up the server
echo -e '\n\n > Starting the server:\n'

curl -f -k --verbose --basic admin:admin -X POST --max-time 900 \
                "${EGERIA_ENDPOINT}/open-metadata/admin-services/users/${EGERIA_USER}/servers/${EGERIA_SERVER}/instance"
```
