<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Placeholders

A placeholder is a replaceable value.  It is distinguished by a double set of curly braces - `{{placeholder}}`.  Placeholders allow concrete values to be substituted when an element is either created of used.  They are found in many technologies.  For example, both Postman and IntelliJ's HTTP client use placeholders in their REST API definitions to denote network addresses or identifiers.  These values are supplied when the REST request is made through an environment file.

Egeria has support for placeholders both in its [configuration documents](/concepts/configuration-document) and its [template](/features/templated-cataloguing/overview) support that is used when creating metadata.

## Placeholder variables

The placeholders in the configuration document are called *placeholder variables*.  It is possible to use them when configuring a server:

```
###
# Set up the common properties needed to call your event bus.  The value of {{kafkaEndpoint}} is resolved in the
# application.properties file using the `platform.placeholder.variables` property.

POST {{baseURL}}/open-metadata/admin-services/users/{{adminUserId}}/servers/active-metadata-store/event-bus
Content-Type: application/json

{
"producer":
{
"bootstrap.servers":"{{kafkaEndpoint}}"
},
"consumer":
{
"bootstrap.servers":"{{kafkaEndpoint}}"
}
}

```
The value to substitute for `{{kafkaEndpoint}}` is provided in the OMAG Server Platform's `application.properties` file, like this:
```
platform.placeholder.variables=\
  {\
    "kafkaEndpoint" : "localhost:9092"\
  }
```
It is read and used on each server start up.

??? education "Further information on placeholder variables"

    * [Configuring the OMAG Server Platform](/guides/admin/configuring-the-omag-server-platform) for setting up the `additional.properties` file
    * [Configuring OMAG Servers](/guides/admin/servers) for details of using the placeholder properties.

## Placeholder properties

Placeholder properties may be added to attributes of the elements that are part of a template.  The values to substitute are provided to Egeria when the template is used to create a new open metadata element. 

Placeholder properties are particularly useful for elements that need to be unique in the resulting element, such as the *qualifiedName* attribute, or on attributes that provide a value specific to the new element, such as the *address* in *Endpoint*.

For example, the call below is from [Automated Curation OMVS](/services/omvs/automated-curation/overview).  It creates a new metadata element based on the template with the unique identifier passed in the `templateGUID` property  of the body.
```
###
# @name createElementFromTemplate
# Create a new element from a template.
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/catalog-templates/new-element
Authorization: Bearer {{token}}
Content-Type: application/json

{
   "templateGUID" : "add guid here",
   "isOwnAnchor" : true,
   "placeholderPropertyValues" : {
       "placeholderPropertyName1" : "placeholderPropertyValue1",
       "placeholderPropertyName2" : "placeholderPropertyValue2"
   }
}
```
Below is an outline of the default template for cataloguing a PostgreSQL Database Server.  This is represented as a [SoftwareServer](/types/0/0040-Software-Servers) asset, in includes a linked [SoftwareCapability](/types/0/0042-Software-Capabilities) for the [database manager (DBMS)](/types/0/0050-Applications-and-Processes).  There is also a [connection](/concepts/connection) linked from the asset to define how to create a connector to the PostgreSQL Database Server.  Notice that throughout the template, there are placeholder properties:

![PostgreSQL Database Server Template](/catalog-templates/postgres-server-catalog-template.svg)

Below is an example of a call to create an asset using the template:

```
###
# @name createElementFromTemplate (PostgreSQL Server)
# Create a new element from a template.
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/catalog-templates/new-element
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "templateGUID" : "542134e6-b9ce-4dce-8aef-22e8daf34fdb",
  "isOwnAnchor" : true,
  "placeholderPropertyValues" : {
    "hostIdentifier" : "coconet.com",
    "portNumber" : "5432",
    "serverName" : "DemoPostgreSQL1",
    "databaseUserId" : "psAdmin",
    "databasePassword" : "secret"
  }
}
```
The picture below shows the resulting asset elements, linked back to the elements from the template using the [SourcedFrom](/types/0/0011-Managing-Referenceables).
Notice how the `{{serverName}}` placeholder property is used in each element to create a unique qualifiedName.

![PostgreSQL Database Server Template in use](/catalog-templates/postgres-server-template-in-use.svg)

The placeholder properties can be used to make the templates easy to use, removing much of the repetitive creation of property values.  The result is a consistent set of elements for the asset.


??? education "Further information on placeholder properties"

    * [Automated Curation API](/services/omvs/automated-curation/overview)
    * [Templated Cataloguing](/features/templated-cataloguing/overview)

