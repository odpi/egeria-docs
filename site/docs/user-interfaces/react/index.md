<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# Egeria React UI Overview

The Egeria React UI is a React multi tenant User Interface for Open Metadata and Governance. It is part of the [Egeria](https://github.com/odpi/egeria/blob/master/README.md) project; as such it is bound by the same code of conduct, governance etc and it part of the Egeria community (and community calls).
The code for the lives in the Egeria React UI Git repository [https://github.com/odpi/egeria-react-ui](https://github.com/odpi/egeria-react-ui).
The Egeria React User Interface (UI), which provides a multi tenanted, persona based interface for users to work with Egeria solutions and Egeria ecosystem tools
is.

This repository is separate from the main Egeria repository, because the technology and build infrastructure is sufficiently different for the User interface.
Egeria React User Interface developers work with nodejs, develop in javascript, use the React framework and use npm; whereas the main Egeria repository attracts developers with Java skills.

The **Presentation Server** is a multi-tenant persona based server that serves a user interface - it issues rest calls downstream primarily to [view servers](https://egeria.odpi.org/open-metadata-implementation/admin-services/docs/concepts/view-server.html)
The React UI requires the presentation server to run, which in turn requires a view server which
in turn requires target services. Please refer to the [Egeria Key concepts](../../introduction/key-concepts/) if ypu want to learn more.

Follow this [setup checklist](./react-ui-setup-checklist) to plan your Egeria React UI.

### UI capability types

There are 2 types of UI capabilities in the Presentation Server.

* [Ecosystem Tool](../ecosystem/ecosystem.md) These are low level user exploration oriented user interfaces around resources, types and the operational landscape.
* [Solution](../solutions/solutions.md) There are solution orientated user interfaces for particular personas.

### UI capabilities

| UI Capability | UI Capability type |View Service | View service target | description |
| ----------- | ----------- | ------ | --- | --- |
| Type Explorer (Tex) | Ecosystem Tool | tex | OMRS | Exploration of the Egeria Type system loaded on server(s)
| Resource Explorer (Rex) | Ecosystem Tool | rex |  OMRS | Exploration of OMRS entities and relationships present on server(s)
| Dino | Ecosystem Tool |dino | OMRS | Exploration of the operation landscape |
| Glossary Author | Solution | Glossary Author | Subject Area OMAS | Glossary author tasks, including Glossary Terms, Categories and their relationships |
| Server Author | Solution | Server Author | Admin server and platform services | Server author tasks including authoring new server configurations |

### Architectural picture.

