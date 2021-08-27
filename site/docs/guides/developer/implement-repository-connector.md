
!!! attention "A common tripping point for conformance"
    The routing behavior described for homed metadata instances can only be enforced when the requests go through OMRS itself. For third party tools that provide their own services / user interface through which updates can be made, a common tripping point becomes the fact that these services / user interfaces need to adhere to the same protocol principles outlined above -- specifically, ensuring reference copies are also immutable through these product-native interfaces -- in order to conform to the Egeria protocol.

    For cases where the tool is unable to do so, we are actively investigating other mitigation measures like providing a [Smart Repository Proxy :material-github:](https://github.com/odpi/egeria/issues/5402){ target=gh } to ensure that any changes to metadata that violate the protocol remain isolated in that third party technology and are not inadvertently propagated elsewhere in the cohort.
