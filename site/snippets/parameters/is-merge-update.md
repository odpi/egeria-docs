<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The `isMergeUpdate` boolean parameter appears on update methods.  It describes what should be done about properties that are currently stored in an element but not passed on the update request.

If `isMergeUpdate` is set to `true`, then the supplied properties are merged with the stored properties.  The supplied properties replaces individual matching properties.  

![isMergeUpdate=true](/parameters/is-merge-update-true.svg)

If `isMergeUpdate` is set to `false`, then the supplied properties replace the stored properties.

![isMergeUpdate=false](/parameters/is-merge-update-false.svg)


