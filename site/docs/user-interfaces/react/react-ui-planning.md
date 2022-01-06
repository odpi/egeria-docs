<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# Egeria React UI Planning

## UI capability types


There are 2 types of UI capabilities in the Presentation Server.

* ==Ecosystem Tool== These are low level user exploration oriented user interfaces around resources, types and the operational landscape.
* ==Solution== These are solution orientated user interfaces for particular personas.

Maybe this Ui is for demonstrations, in which case you may want to configure all its capabilities. 
You may want to have a solutions orientated Ui or an ecosystem tools oriented UI- as the users of each can be different in an organisation. 

## UI capabilities

Here is a table showing for a UI capability, which view service it calls and whacht target service the view service calls.
This information is important, so you can ensure that the appropriate view services and target services are configured to allow the UI
capability to work.

| UI Capability | UI Capability type |View Service | View service target | description |
| ----------- | ----------- | ------ | --- | --- |
| Type Explorer (Tex) | Ecosystem Tool | tex | OMRS | Exploration of the Egeria Type system loaded on server(s)
| Resource Explorer (Rex) | Ecosystem Tool | rex |  OMRS | Exploration of OMRS entities and relationships present on server(s)
| Dynamic Infrastructure and Operations (Dino) | Ecosystem Tool |dino | OMRS | Exploration of the operation landscape |
| Glossary Author | Solution | Glossary Author | Subject Area OMAS | Glossary author tasks, including Glossary Terms, Categories and their relationships |
| Server Author | Solution | Server Author | Admin server and platform services | Server author tasks including authoring new server configurations |

Planning your user interface means that you are choosing which UI capabilities to expose in the UI, which indicates which view services need to be 
configured and which target services. 

## Architectural picture.

Below is a picture of how the browser communicates with the presentation server (which is a node application). The presentation server handlers the login
using [passportjs](https://www.passportjs.org/) technology and the resources (html and images etc) as well as forwarding on the rest calls from the browser to the
view service.

![Figure 1 - Ui components](ui-components.drawio.svg)

The presentation server configuration is very simple; it uses environment variables to know where to issue its rest calls to.
More detailed information is configured in the view servers, using the standard OMAG server configuration.






