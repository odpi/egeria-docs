<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### What are the REST APIs supported by the Platform?

The OMAG Server Platform has many REST APIs.  Enter **https://localhost:9443/swagger-ui/index.html** into your browser to see the list of available REST APIs.

Broadly speaking, the OMAG Server Platform supports:

* Services to operate the platform itself.
* Services to manage and govern the open metadata ecosystem.

The services operating the platform (primarily the [Administration Services](/services/admin-services/overview) and [Platform Services](/services/platform-services/overview)) are available all the time the OMAG Server Platform is running.  The other services require at least one OMAG Server running on the OMAG Server Platform to activate them.

OMAG Servers are started on the OMAG Server Platform through the Platform Services using a [configuration document](/concepts/configuration-document).  This configuration document is configured in the OMAG Server Platform using the Administration Services.

Understanding how to create a configuration document using the administration services is the next task in this tutorial.





