<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# 0705 Data Sharing

Data sharing describes the process of sharing data between different organizations or teams. It involves the exchange of data assets, such as datasets, files, or information, to enable collaboration, integration, and knowledge sharing. Data sharing can be facilitated through various mechanisms, including data exchange platforms, APIs, data sharing agreements, and data governance frameworks.

![UML](0705-Data-Sharing.svg)

## DataHub entity

The *DataHub* entity describes a collection of data assets that are available for sharing, as long as the requester satisfies the requirements laid down by the data owner.

## DataSharingRequest entity

The *DataSharingRequest* entity describes a request for data sharing.  It is used to track the status of the request and gather the details of the request (such as the requested data specification) and the data sharing agreement and related resources.

--8<-- "snippets/abbr.md"