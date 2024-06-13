<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


A *Verification governance action service* tests the properties of specific open metadata elements to ensure they are set up correctly and do not indicate a situation where governance activity is required.
For example, it may check that a new asset has an owner assigned, is set up with [governance zones](/concepts/governance-zone) and includes a connection and a schema.

The verification governance action services publishes [guards](/concepts/guard) to report on any errors it finds.  It may also create [incident reports](/concepts/incident-report) to coordinate actions to correct any errors.
The guards returned from the verification governance action service can be used to trigger other governance services as part of a [governance action process](/concepts/governance-action-process).

![Function of the verification governance action service](/frameworks/gaf/verification-governance-action-service.svg)




