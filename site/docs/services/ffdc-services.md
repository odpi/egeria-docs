<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# First failure data capture (FFDC) services

The FFDC services supports common functions that many other services use in their REST API support:

* Logging the start and return to debug logging for each REST call made
* Capture exceptions before they are returned and set up appropriate information in response objects.

--8<-- "snippets/abbr.md"