<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Metadata server

A **metadata server** is an [OMAG server](/egeria/concepts/omag-server) that hosts a
metadata repository with native support for open metadata types and
instances. It is able to be a 
[member of an open metadata repository cohort](/egeria/services/omrs/cohort/#cohort-members) and so
can exchange metadata with other members of the cohort.

![Metadata server in the open metadata ecosystem](metadata-server.png)

The metadata server typically has the [access services](/egeria/services/omas)
configured and so can act as a [metadata access point](/egeria/concepts/metadata-access-point).
It is important to have at least one metadata server in each cohort in order to
support all types of metadata.

--8<-- "snippets/abbr.md"
