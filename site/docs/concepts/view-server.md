<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# View Server

A **view server** is an [OMAG server](/egeria/concepts/view-server)
that hosts the REST API services to support a UI.  
These REST API services are called 
[Open Metadata View Services (OMVS)](/egeria/services/view) 
and they are designed to support specific display paradigms needed
by different types of UIs.

The view services are typically
called by the [presentation server](/egeria/concepts/presentation-server), but may also be used by third parties.
The presentation server hosts the JavaScript that controls the browser display.

![A view server in the open metadata ecosystem](view-server.png)

--8<-- "snippets/abbr.md"
