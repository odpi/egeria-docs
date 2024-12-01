<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Python Client for Egeria (pyegeria)

The python functions from [pyegeria](/concepts/pyegeria) are organized into 5 separate clients:

* EgeriaMy - for querying an individual's profiles, to-dos and adding feedback to metadata stored in Egeria.
* EgeriaCat - for day-to-day use of Egeria
* EgeriaTech - for setting up Egeria services and governance actions.
* EgeriaGov (coming) - for creating and maintaining governance domains.
* EgeriaConfig - for configuring new Egeria OMAG Servers

EgeriaCat, EgeriaTech and EgeriaGov all extend EgeriaMy. EgeriaConfig is standalone.

To make use of one of these clients, first import the client you need. The command below imports EgeriaTech.

----

```python

from pyegeria import EgeriaTech

```
----

The `pyegeria` functions require information about the calling user and the network location of Egeria's runtime.  These are passed to the client when it is created.  The CLI also needs this information and to save the caller having to supply it on every request, it supports environment variables.  These same environment variables can be used with the `pyegeria` functions.

The code below extracts the values from these environment variables for use in the call to the constructor of the client.

----

```python

import os

view_server = os.environ.get("VIEW_SERVER","view-server")
url = os.environ.get("EGERIA_VIEW_SERVER_URL","https://host.docker.internal:9443")
user_id = os.environ.get("EGERIA_USER", "peterprofile")
user_pwd = os.environ.get("EGERIA_USER_PASSWORD")

```

----

### EgeriaTech help

This is the call to create the client.

----

```python
egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
```

-----

The next call logs the user into the Egeria platform, a token is returned.  It is retained by the client and automatically passed on each request to Egeria.  The token will eventually time out, at which time just reissue the `create_egeria_bearer_token()` function.

-----

```python
egeria_tech_token = egeria_tech.create_egeria_bearer_token()
```

----

Now you are ready to use the functions that call Egeria.  It is possible to use the standard python methods to retrieve information about the available functions. For example `dir` lists the functions supported by the client.

----

```python
dir(egeria_tech)
```

----

A question mark (?) after the name of the client shows how to create an instance of the client.

----

```python
EgeriaTech?
```
```
Init signature:
EgeriaTech(
    view_server: str,
    platform_url: str,
    user_id: str,
    user_pwd: str = None,
    token: str = None,
)
Docstring:     
Client for technical Egeria users.

Attributes:

    view_server: str
            Name of the server to use.
    platform_url : str
        URL of the server platform to connect to
    user_id : str
        The identity of the user calling the method - this sets a default optionally used by the methods
        when the user doesn't pass the user_id on a method call.
    user_pwd: str
        The password associated with the user_id. Defaults to None
    token: str, optional
        Bearer token

Methods:
    Inherits methods from EgeriaCat, ActionAuthor, AutomatedCuration,
    ClassificationManager, RegisteredInfo, ValidMetadataManager
File:           /opt/conda/lib/python3.12/site-packages/pyegeria/egeria_tech_client.py
Type:           type
Subclasses:     


```

----

It is then possible to list the parameters of a specific function using the `help` function.

----

```python
help(EgeriaTech.get_related_elements)
```
```
Help on function get_related_elements in module pyegeria.classification_manager_omvs:

get_related_elements(self, element_guid: str, relationship_type: str = None, open_metadata_type_name: str = None, start_at_end: int = 1, effective_time: str = None, for_lineage: bool = None, for_duplicate_processing: bool = None, start_from: int = 0, page_size: int = 500, time_out: int = 30) -> list | str
    Retrieve elements linked by relationship type name. If the relationship type is None, then all related elements
    will be returned. It is also possible to limit the results by specifying a type name for the elements that
    should be returned. If no type name is specified then any type of element may be returned.

    https://egeria-project.org/types/

    Parameters
    ----------
    element_guid: str
        - the base element to get related elements for
    relationship_type: str
        - the type of relationship to navigate to related elements
    open_metadata_type_name : str, default = None
        - open metadata type to be used to restrict the search
    start_at_end: int, default = 1
        - The end of the relationship to start from - typically End1
    effective_time: str, default = None
        - Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
    for_lineage: bool, default is set by server
        - determines if elements classified as Memento should be returned - normally false
    for_duplicate_processing: bool, default is set by server
        - Normally false. Set true when the caller is part of a deduplication function
    start_from: int, default = 0
        - index of the list to start from (0 for start).
    page_size
        - maximum number of elements to return.


    time_out: int, default = default_time_out
        - http request timeout for this request

    Returns
    -------
    [dict] | str
        Returns a string if no elements found and a list of dict of elements with the results.

    Raises
    ------
    InvalidParameterException
        one of the parameters is null or invalid or
    PropertyServerException
        There is a problem adding the element properties to the metadata repository or
    UserNotAuthorizedException
        the requesting user is not authorized to issue this request.

```

----

If you execute a function without capturing the response in a python variable, the JSON returned from Egeria is displayed:

----

```python

egeria_tech.get_servers_by_name("active-metadata-store")

```
```json
[{'properties': {'class': 'SoftwareServerProperties',
   'typeName': 'SoftwareServer',
   'qualifiedName': 'Metadata Access Server:active-metadata-store',
   'displayName': 'active-metadata-store',
   'displayDescription': 'A metadata store that supports Open Metadata Access Services (OMASs) with event notifications.  It provides metadata to view-server, engine-host and integration-daemon.',
   'name': 'active-metadata-store',
   'resourceName': 'active-metadata-store',
   'versionIdentifier': 'Egeria OMAG Server Platform (version 5.2-SNAPSHOT)',
   'resourceDescription': 'A metadata store that supports Open Metadata Access Services (OMASs) with event notifications.  It provides metadata to view-server, engine-host and integration-daemon.',
   'deployedImplementationType': 'Metadata Access Server'},
  'elementHeader': {'class': 'ElementHeader',
   'headerVersion': 0,
   'status': 'ACTIVE',
   'type': {'typeId': 'aa7c7884-32ce-4991-9c41-9778f1fec6aa',
    'typeName': 'SoftwareServer',
    'superTypeNames': ['ITInfrastructure',
     'Infrastructure',
     'Asset',
     'Referenceable',
     'OpenMetadataRoot'],
    'typeVersion': 2,
    'typeDescription': 'Software services to support a runtime environment for applications and data stores.'},
   'origin': {'sourceServer': 'active-metadata-store',
    'originCategory': 'LOCAL_COHORT',
    'homeMetadataCollectionId': '61400a70-8c49-4635-b221-a8b11872ae16',
    'homeMetadataCollectionName': 'active-metadata-store'},
   'versions': {'createdBy': 'omagspcatnpa',
    'createTime': '2024-11-29T16:59:21.837+00:00',
    'version': 1},
   'guid': '492a3052-737c-4c28-bb42-090661b2ea39',
   'classifications': [{'class': 'ElementClassification',
     'headerVersion': 0,
     'status': 'ACTIVE',
     'type': {'typeId': 'aa44f302-2e43-4669-a1e7-edaae414fc6e',
      'typeName': 'Anchors',
      'typeVersion': 3,
      'typeDescription': 'Identifies the anchor entity for an element that is part of a large composite object such as an asset.'},
     'origin': {'sourceServer': 'active-metadata-store',
      'originCategory': 'LOCAL_COHORT',
      'homeMetadataCollectionId': '61400a70-8c49-4635-b221-a8b11872ae16',
      'homeMetadataCollectionName': 'active-metadata-store'},
     'versions': {'createdBy': 'omagspcatnpa',
      'createTime': '2024-11-29T16:59:21.835+00:00',
      'version': 1},
     'classificationOrigin': 'ASSIGNED',
     'classificationName': 'Anchors',
     'classificationProperties': {'anchorTypeName': 'SoftwareServer',
      'anchorDomainName': 'Asset'}},
    {'class': 'ElementClassification',
     'headerVersion': 0,
     'status': 'ACTIVE',
     'type': {'typeId': '74a256ad-4022-4518-a446-c65fe082d4d3',
      'typeName': 'MetadataServer',
      'superTypeNames': ['ServerPurpose'],
      'typeVersion': 3,
      'typeDescription': 'A server hosting a metadata collection.'},
     'origin': {'sourceServer': 'active-metadata-store',
      'originCategory': 'LOCAL_COHORT',
      'homeMetadataCollectionId': '61400a70-8c49-4635-b221-a8b11872ae16',
      'homeMetadataCollectionName': 'active-metadata-store'},
     'versions': {'createdBy': 'omagspcatnpa',
      'createTime': '2024-11-29T16:59:21.835+00:00',
      'version': 1},
     'classificationOrigin': 'ASSIGNED',
     'classificationName': 'MetadataServer'},
    {'class': 'ElementClassification',
     'headerVersion': 0,
     'status': 'ACTIVE',
     'type': {'typeId': 'adce83ac-10f1-4279-8a35-346976e94466',
      'typeName': 'LatestChange',
      'typeVersion': 1,
      'typeDescription': 'Defines the latest change to an anchor entity and its associated attachments.'},
     'origin': {'sourceServer': 'active-metadata-store',
      'originCategory': 'LOCAL_COHORT',
      'homeMetadataCollectionId': '61400a70-8c49-4635-b221-a8b11872ae16',
      'homeMetadataCollectionName': 'active-metadata-store'},
     'versions': {'createdBy': 'activenpa',
      'createTime': '2024-11-29T16:59:22.177+00:00',
      'version': 1},
     'classificationOrigin': 'ASSIGNED',
     'classificationName': 'LatestChange',
     'classificationProperties': {'relationshipType': 'DeployedOn',
      'attachmentType': 'Asset',
      'changeTarget': 'AttachmentRelationship',
      'actionDescription': 'Linking ITInfrastructure 492a3052-737c-4c28-bb42-090661b2ea39 to Asset 44bf319f-1e41-4da1-b771-2753b92b631a',
      'attachmentGUID': '44bf319f-1e41-4da1-b771-2753b92b631a',
      'user': 'omagspcatnpa',
      'changeAction': 'Created'}}]}}]
```

----

Assigning the results to a python variable means you can extract specific values:

----

```python

def get_server_guid(serverName):
    serverDetails = egeria_tech.get_servers_by_name(serverName)
    if serverDetails:
        elementHeader = serverDetails[0].get('elementHeader')
        if elementHeader:
            return elementHeader.get('guid')
    return "???"
            

serverGUID = get_server_guid("active-metadata-store")

print("Unique identifier (guid) for 'active-metadata-store' is " + serverGUID)

```
```

Unique identifier (guid) for 'active-metadata-store' is 492a3052-737c-4c28-bb42-090661b2ea39

```



--8<-- "snippets/abbr.md"
