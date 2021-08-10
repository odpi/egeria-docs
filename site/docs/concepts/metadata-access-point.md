<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Metadata access point

A **metadata access point** is an [OMAG server](/egeria/concepts/omag-server) that can be a
[member of an open metadata repository cohort](/egeria/services/omrs/cohort/#cohort-members)
and supports the [access services](/egeria/services/omas).

![Metadata access point in OMAG server ecosystem](metadata-access-point.png)

This means it provides specialist metadata
APIs to user interfaces and governance servers that embrace metadata from
all connected open metadata repository cohorts.

The basic metadata access point has no metadata repository and metadata
is retrieved and stored from remote repositories via the [cohort](/egeria/services/omrs/cohort).
It can be upgraded to a [metadata server](/egeria/concepts/metadata-server)
by adding a metadata repository which will enable it to
store metadata locally.
