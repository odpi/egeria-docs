<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Egeria Ecosystem UI Overview

The Ecosystem UI (Egeria React UI) is a React User Interface for Open Metadata and Governance.
The code lives in the [Egeria React UI Git repository](https://github.com/odpi/egeria-react-ui).

The Egeria Ecosystem User Interface (UI) provides a multi tenanted, persona based interface for users to work with Egeria solutions and Egeria ecosystem tools.
Egeria Ecosystem User interface using the following technologies:

* [React](https://reactjs.org/) - A JavaScript library for building user interfaces, that is declarative, has components and is 'learn once, write anywhere'. 
* [Nodejs](https://nodejs.org/) - Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
* [Passport](https://www.passportjs.org/) - Simple, unobtrusive authentication for Node.js.
* [Carbon Design system](https://www.carbondesignsystem.com/) - Carbon is IBM’s open source design system for products and digital experiences.

This repository is separate from the main [Egeria](https://github.com/odpi/egeria) repository, because the technology and build infrastructure is sufficiently different for the User interface.
Egeria Ecosystem User Interface developers work with nodejs, develop in javascript, use the React framework and use npm; whereas the main Egeria repository attracts developers with Java skills.

The **Presentation Server** is a multi-tenant persona based server that serves a user interface - it issues rest calls downstream primarily to [view servers](../../concepts/view-server.md)
The Ecosystem UI requires the presentation server to run, which in turn requires a view server which
in turn requires target services. Please refer to the [Egeria Key concepts](../../introduction/key-concepts/) if you want to learn more.

Follow this [UI Planning checklist](./ecosystem-ui-planning-checklist) to plan your Egeria Ecosystem UI.





