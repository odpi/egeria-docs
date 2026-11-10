<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Python Client for Egeria (pyegeria)

The python functions from [pyegeria](/concepts/pyegeria) call the [Open Metadata View Services (OMVS)](/services/omvs) running in a [view server](/concepts/view-server).  There is a python class for each view service - for example `RuntimeManager`, `AssetCatalog`, `ClassificationExplorer` and `GlossaryManager` - and these are combined into the following clients:

* Egeria - covers all the functional pyegeria classes.
* EgeriaTech - for technical users that are setting up Egeria services, governance actions and metadata.  It covers most of the view services, plus server operations.
* EgeriaCat - for day-to-day use of Egeria as a catalog.  It combines `ProjectManager`, `GlossaryManager`, `AssetCatalog` and `MyProfile`.
* EgeriaConfig - for configuring new Egeria OMAG Servers.

EgeriaCat inherits the methods of its four classes.  Egeria, EgeriaTech and EgeriaConfig are *facades*: they create the individual view service clients on first use and pass each method call on to the client that provides it.  It is also possible to import and use the individual view service classes directly.

To make use of one of these clients, first import the client you need.  The command below imports EgeriaTech.

----

```python

from pyegeria import EgeriaTech

```

----

The `pyegeria` functions require information about the calling user and the network location of Egeria's runtime.  These are passed to the client when it is created.  The CLI also needs this information and to save the caller having to supply it on every request, it supports environment variables.  These same environment variables can be used with the `pyegeria` functions.

The code below extracts the values from these environment variables for use in the call to the constructor of the client.  The defaults shown are the ones pyegeria uses for the Egeria quickstart environment.

----

```python

import os

view_server = os.environ.get("EGERIA_VIEW_SERVER","qs-view-server")
url = os.environ.get("EGERIA_PLATFORM_URL","https://localhost:9443")
user_id = os.environ.get("EGERIA_USER", "peterprofile")
user_pwd = os.environ.get("EGERIA_USER_PASSWORD")

```

----

!!! tip "Default values"
    If a constructor parameter is omitted, pyegeria fills it in from its configuration: the `EGERIA_VIEW_SERVER`, `EGERIA_PLATFORM_URL`, `EGERIA_USER` and `EGERIA_USER_PASSWORD` environment variables, then the pyegeria configuration file (`config.json`, located using `PYEGERIA_ROOT_PATH` and `PYEGERIA_CONFIG_FILE`), then the built-in defaults.

### EgeriaTech help

This is the call to create the client.

----

```python
egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
```

-----

The next call logs the user into the Egeria platform, a token is returned.  It is retained by the client and automatically passed on each request to Egeria.  The token will eventually time out, at which time just reissue the `create_egeria_bearer_token()` function.  Call `close_session()` when you have finished with the client.

-----

```python
egeria_tech_token = egeria_tech.create_egeria_bearer_token()
```

----

Now you are ready to use the functions that call Egeria.  It is possible to use the standard python methods to retrieve information about the available functions.  Since EgeriaTech passes calls on to the individual view service clients, `dir(egeria_tech)` only lists the facade's own functions.  Use `dir` on one of the view service classes to list the functions it supports.

----

```python
from pyegeria import RuntimeManager
dir(RuntimeManager)
```

----

A question mark (?) after the name of the client (in Jupyter or IPython) shows how to create an instance of the client.

----

```python
EgeriaTech?
```
```
Init signature:
EgeriaTech(
    view_server: str = None,
    platform_url: str = None,
    user_id: str = None,
    user_pwd: str = None,
    token: str = None,
    timeout: int = None,
)
Docstring:
Client for technical Egeria users using lazy-loading composition.

Attributes:
    view_server: str
        Name of the view server to use.
    platform_url : str
        URL of the server platform to connect to
    user_id : str
        The identity of the user calling the method.
    user_pwd: str
        The password associated with the user_id. Defaults to None
    token: str, optional
        Bearer token

Methods:
    Methods are provided by composed sub-clients via delegation.
Type:           type
```

----

It is then possible to list the parameters of a specific function using the `help` function on the client instance.

----

```python
help(egeria_tech.get_related_elements)
```
```
Help on method get_related_elements in module pyegeria.omvs.classification_explorer:

get_related_elements(element_guid: str, relationship_type: Optional[str] = None, start_at_end: int = 1, start_from: int = 0, page_size: int = 0, output_format: str = 'JSON', report_spec: dict | str = None, body: Optional[dict | ResultsRequestBody] = None, **kwargs: Unpack[ListFilters]) -> list | str
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
    start_at_end: int, default = 1
        - The end of the relationship to start from - typically End1
    start_from: int, default = 0
        - index of the list to start from (0 for start).
    page_size: int, default = 0
        - maximum number of elements to return.
    output_format: str, default = "JSON"
        - Type of output to return.
    report_spec: dict | str, default = None
        - Output format set to use. If None, the default output format set is used.
    body: dict | ResultsRequestBody, optional
        - full request specification - if provided, overrides other parameters.

    Accepts the standard list filters as keyword arguments (see ``ListFilters``
    in ``pyegeria.core.request_filters``).

    Returns
    -------
    [dict] | str
        Returns a string if no elements found and a list of dict of elements with the results.

    Raises
    ------
    PyegeriaException
```

----

If you execute a function without capturing the response in a python variable, the JSON returned from Egeria is displayed.  With the default `output_format="JSON"`, the result is the list of elements returned by the view service.  In this example, `graph_query_depth=0` asks for the server element without its relationships to other elements.  (The `usageActivity` classification has been removed from the output to shorten it.)

----

```python

egeria_tech.get_servers_by_name("qs-metadata-store", graph_query_depth=0)

```
```json
[
  {
    "class": "OpenMetadataRootElement",
    "elementHeader": {
      "class": "ElementHeader",
      "headerVersion": 0,
      "status": "ACTIVE",
      "type": {
        "typeId": "aa7c7884-32ce-4991-9c41-9778f1fec6aa",
        "typeName": "SoftwareServer",
        "superTypeNames": [
          "ITInfrastructure",
          "Infrastructure",
          "Asset",
          "Referenceable",
          "OpenMetadataRoot"
        ],
        "typeVersion": 1,
        "typeDescription": "Software services to support a runtime environment for applications and data stores.",
        "typeCategory": "ENTITY_DEF"
      },
      "origin": {
        "sourceServer": "qs-metadata-store",
        "originCategory": "LOCAL_COHORT",
        "homeMetadataCollectionId": "9905c3cb-94c5-4494-9229-0d6f69c0b842",
        "homeMetadataCollectionName": "qs-metadata-store"
      },
      "versions": {
        "createdBy": "omagspcatnpa",
        "updatedBy": "omagspcatnpa",
        "maintainedBy": [
          "omagspcatnpa"
        ],
        "createTime": "2026-10-25T10:25:42.604+00:00",
        "updateTime": "2026-11-09T20:14:29.953+00:00",
        "version": 9,
        "lastRequestId": "c912e3a2-ee3a-440d-b862-8dc35f86f807"
      },
      "guid": "81aee2d5-151f-4f61-b8ad-b22785cd6ffd",
      "anchor": {
        "class": "ElementClassification",
        "headerVersion": 0,
        "status": "ACTIVE",
        "type": {
          "typeId": "aa44f302-2e43-4669-a1e7-edaae414fc6e",
          "typeName": "Anchors",
          "typeVersion": 1,
          "typeDescription": "Identifies the anchor entity for an element that is part of a large composite object such as an asset.",
          "typeCategory": "CLASSIFICATION_DEF"
        },
        "origin": {
          "sourceServer": "qs-metadata-store",
          "originCategory": "LOCAL_COHORT",
          "homeMetadataCollectionId": "9905c3cb-94c5-4494-9229-0d6f69c0b842",
          "homeMetadataCollectionName": "qs-metadata-store"
        },
        "versions": {
          "createdBy": "omagspcatnpa",
          "updatedBy": "omagspcatnpa",
          "maintainedBy": [
            "omagspcatnpa"
          ],
          "createTime": "2026-10-25T10:25:42.566+00:00",
          "updateTime": "2026-10-25T10:25:42.566+00:00",
          "version": 1,
          "lastRequestId": "6b012148-a3e8-4c86-b25d-7ddbdc3d00e1"
        },
        "classificationOrigin": "ASSIGNED",
        "classificationName": "Anchors",
        "classificationProperties": {
          "class": "AnchorsProperties",
          "typeName": "Anchors",
          "anchorTypeName": "SoftwareServer",
          "anchorDomainName": "Asset"
        }
      }
    },
    "properties": {
      "class": "SoftwareServerProperties",
      "typeName": "SoftwareServer",
      "qualifiedName": "Metadata Access Store::https://localhost:9443::qs-metadata-store",
      "identifier": "qs-metadata-store",
      "displayName": "qs-metadata-store from Coco Pharmaceuticals on https://localhost:9443",
      "description": "A metadata store that supports Open Metadata Access Services (OMASs) with event notifications.  It provides metadata to qs-view-server, qs-engine-host and qs-integration-daemon.",
      "versionIdentifier": "6.3-SNAPSHOT",
      "category": "Egeria Deployment",
      "url": "https://egeria-project.org/concepts/metadata-access-store/",
      "additionalProperties": {
        "organizationName": "Coco Pharmaceuticals",
        "platformURLRoot": "https://localhost:9443",
        "serverName": "qs-metadata-store",
        "serverId": "00d42a19-1d53-4155-8ba4-3b14ac6c87d6"
      },
      "resourceName": "Coco Pharmaceuticals.qs-metadata-store",
      "namespacePath": "Coco Pharmaceuticals",
      "deployedImplementationType": "Metadata Access Store",
      "deploymentStatus": "ACTIVE"
    }
  }
]
```

----

Assigning the results to a python variable means you can extract specific values.  If nothing matches, the function returns the string `"No elements found"` rather than a list.

----

```python

def get_server_guid(server_name):
    server_details = egeria_tech.get_servers_by_name(server_name, graph_query_depth=0)
    if isinstance(server_details, list) and server_details:
        element_header = server_details[0].get('elementHeader')
        if element_header:
            return element_header.get('guid')
    return "???"


server_guid = get_server_guid("qs-metadata-store")

print("Unique identifier (guid) for 'qs-metadata-store' is " + server_guid)

```
```

Unique identifier (guid) for 'qs-metadata-store' is 81aee2d5-151f-4f61-b8ad-b22785cd6ffd

```

!!! education "Further information"
    * [Scripting commands](/guides/developer/scripting-commands/overview) describes the command line tools that are installed with pyegeria.
    * The source code and further documentation for pyegeria is in the [egeria-python](https://github.com/odpi/egeria-python) GitHub repository.


--8<-- "snippets/abbr.md"
