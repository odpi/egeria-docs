
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Smart Collections

Egeria's [Classification Explorer](/services/omvs/classification-explorer/overview) and [Metadata Expert](/services/omvs/metadata-expert/overview) APIs offer sophisticated query expressions for exploring the open metadata ecosystem - searching by classification level (impact, confidence, criticality, confidentiality, retention), by property value, or by nested search conditions with operators like `LIKE` combined with `ANY`/`ALL` match criteria.  These let a caller ask very precise questions - for example, "find every `GlossaryTerm` currently classified with a Confidence Level of 3" - and get back exactly the elements that matter.

A team or project often needs to ask the same precise question repeatedly, rather than just once - a glossary team tracking which terms still need review, a data product owner watching for datasets that have drifted out of certification, a security team keeping an eye on newly-classified confidential assets.  Re-running the query by hand every time is tedious, and there is no single place to see the current answer without doing so.

A **smart collection** solves this by having a background connector - the **SmartCollectionsMembershipManager** integration connector - continuously maintain a [collection](/concepts/collection) of elements that match a saved query, so the query's current results are always available as an ordinary collection that can be browsed, linked to and retrieved like any other.


## How a smart collection works

A smart collection is built from three pieces of open metadata, described in [0725 Smart Collections](/types/7/0725-Smart-Collections):

* A **[ResultsSet](/types/7/0725-Smart-Collections)** - a specialized [Collection](/types/0/0021-Collections) whose membership is maintained by a connector rather than set up by hand.  It carries `createdTime`, `startTime`, `completionTime` and `completionMessage` properties that record when its membership was first established and the outcome of its most recent refresh.
* A **[SavedQuery](/types/7/0725-Smart-Collections)** - a `DataSet` [asset](/concepts/asset) that defines the REST call to run: a `queryURL` (any REST API operation on Egeria that returns a list of open metadata elements - typically one of the Classification Explorer or Metadata Expert operations) and an optional `queryRequestBody` holding the JSON request body for that call.
* A **SmartQuery** relationship connecting the two - it tells the connector which saved query determines a given results set's membership.

On every refresh, the **SmartCollectionsMembershipManager** connector:

1. Looks up the ResultsSet's SmartQuery relationship to find its SavedQuery.
2. Issues the SavedQuery's `queryURL`/`queryRequestBody` as a REST call.
3. Compares the GUIDs returned against the ResultsSet's current membership, adding any new matches and removing any elements that no longer match.
4. Updates the ResultsSet's `startTime`, `completionTime` and `completionMessage` to record the outcome - `completionMessage` is cleared on a successful refresh and set to an explanatory message if the query failed, so a broken saved query is visible rather than silently emptying the collection.

The connector is delivered as standard content in Egeria's core content pack, refreshing every 30 minutes by default, though it can also be asked to refresh immediately (see [step 6](#step-6-optional-ask-for-an-immediate-refresh) below).  It only works with `ResultsSet` collections attached to it as [catalog targets](/concepts/catalog-target) - each catalog target is one results set to maintain.


## Setting up a smart collection

The REST calls below assume a running view server (`view-server`) and a bearer token already obtained - see [Setting up your governance program](/guides/planning/governance-program/overview) or the [Metadata Expert API](/services/omvs/metadata-expert/overview) page for background on authentication.  The worked example tracks `GlossaryTerm` elements sitting at Confidence Level 3, for a glossary governance team that wants a standing list of terms needing review - the kind of query the [Classification Explorer API](/services/omvs/classification-explorer/overview) is designed for.

```python
from pyegeria import CollectionManager, AssetMaker

view_server = "view-server"
url         = "https://localhost:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

collection_manager = CollectionManager(view_server, url, user_id, user_pwd)
collection_manager.create_egeria_bearer_token()

asset_maker = AssetMaker(view_server, url, user_id, user_pwd)
asset_maker.create_egeria_bearer_token()
```

### Step 1: Create the Results Set collection

The Results Set is the collection whose membership will be maintained automatically.  It is usually its own anchor.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NewElementRequestBody",
      "isOwnAnchor" : true,
      "properties": {
        "class" : "ResultsSetProperties",
        "qualifiedName": "ResultsSet::GlossaryTermsNeedingReview",
        "displayName" : "Glossary Terms Needing Review",
        "description" : "Membership is maintained by the Smart Collections Integration Connector from the attached saved query."
      }
    }
    ```

=== "pyegeria"

    ```python
    results_set_body = {
        "class" : "NewElementRequestBody",
        "isOwnAnchor" : True,
        "properties": {
            "class" : "ResultsSetProperties",
            "qualifiedName": "ResultsSet::GlossaryTermsNeedingReview",
            "displayName" : "Glossary Terms Needing Review",
            "description" : "Membership is maintained by the Smart Collections Integration Connector from the attached saved query.",
        }
    }

    results_set_guid = collection_manager.create_collection(body=results_set_body)
    ```

### Step 2: Create the Saved Query asset

The Saved Query records the REST call that determines the results set's membership - here, the Classification Explorer's `by-confidence` search for `GlossaryTerm` elements at Confidence Level 3.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-maker/assets
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NewElementRequestBody",
      "isOwnAnchor" : true,
      "properties": {
        "class" : "SavedQueryProperties",
        "qualifiedName": "SavedQuery::GlossaryTermsAtConfidenceLevel3",
        "displayName" : "Glossary Terms at Confidence Level 3",
        "description" : "Searches the open metadata ecosystem for GlossaryTerm elements classified at Confidence Level 3.",
        "queryURL" : "https://localhost:9443/servers/view-server/api/open-metadata/classification-explorer/elements/by-confidence",
        "queryRequestBody" : "{\"class\":\"LevelIdentifierQueryProperties\",\"metadataElementTypeName\":\"GlossaryTerm\",\"returnSpecificLevel\":true,\"levelIdentifier\":3}"
      }
    }
    ```

=== "pyegeria"

    ```python
    saved_query_body = {
        "class" : "NewElementRequestBody",
        "isOwnAnchor" : True,
        "properties": {
            "class" : "SavedQueryProperties",
            "qualifiedName": "SavedQuery::GlossaryTermsAtConfidenceLevel3",
            "displayName" : "Glossary Terms at Confidence Level 3",
            "description" : "Searches the open metadata ecosystem for GlossaryTerm elements classified at Confidence Level 3.",
            "queryURL" : f"{url}/servers/{view_server}/api/open-metadata/classification-explorer/elements/by-confidence",
            "queryRequestBody" : (
                '{"class":"LevelIdentifierQueryProperties",'
                '"metadataElementTypeName":"GlossaryTerm",'
                '"returnSpecificLevel":true,"levelIdentifier":3}'
            ),
        }
    }

    saved_query_guid = asset_maker.create_asset(body=saved_query_body)
    ```

The `queryRequestBody` is stored as a plain string (typically JSON) so that it can hold the request body of *any* REST operation - it isn't limited to the Classification Explorer; a Metadata Expert `findMetadataElements` request with nested search conditions works exactly the same way.

### Step 3: Link the results set to the saved query

The **SmartQuery** relationship (type 0725) tells the connector which saved query to run.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/results-sets/{{resultsSetGUID}}/smart-query/{{savedQueryGUID}}/attach
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NewRelationshipRequestBody",
      "properties": {
        "class": "SmartQueryProperties",
        "label": "Membership query",
        "description": "Determines the membership of the results set."
      }
    }
    ```

=== "pyegeria"

    ```python
    smart_query_body = {
        "class" : "NewRelationshipRequestBody",
        "properties": {
            "class": "SmartQueryProperties",
            "label": "Membership query",
            "description": "Determines the membership of the results set.",
        }
    }

    url_marker = (f"{collection_manager.collection_command_root}/results-sets/"
                  f"{results_set_guid}/smart-query/{saved_query_guid}/attach")

    collection_manager.make_request("POST", url_marker, smart_query_body)
    ```

    `attach_smart_query()` is not yet wrapped as a purpose-built pyegeria method, so this uses the client's generic `make_request()` to call the same REST operation directly.

### Step 4: Attach the results set to the SmartCollectionsMembershipManager as a catalog target

This is what tells the connector to start maintaining this particular results set.  The connector's GUID is stable, since it is registered as reference data in Egeria's core content pack; the catalog target name must be `resultsSetToMaintain`, the name the connector recognizes.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-maker/integration-connectors/217bd925-b50d-4596-9ade-1d7a940e8874/catalog-targets/{{resultsSetGUID}}
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NewRelationshipRequestBody",
      "properties": {
        "class": "CatalogTargetProperties",
        "catalogTargetName" : "resultsSetToMaintain"
      }
    }
    ```

=== "pyegeria"

    ```python
    smart_collections_membership_manager_guid = "217bd925-b50d-4596-9ade-1d7a940e8874"

    catalog_target_body = {
        "class" : "NewRelationshipRequestBody",
        "properties": {
            "class": "CatalogTargetProperties",
            "catalogTargetName" : "resultsSetToMaintain",
        }
    }

    asset_maker.add_catalog_target(
        smart_collections_membership_manager_guid,
        results_set_guid,
        body=catalog_target_body,
    )
    ```

### Step 5: Link the smart collection to a convenient parent

A results set is rarely interesting on its own - it is usually set up by a [project](/concepts/project) or [team](/concepts/team) so its members can find it again.  Linking it to that parent element with a [`ResourceList`](/types/0/0019-More-Information) relationship makes it show up alongside the parent's other resources.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/metadata-elements/{{parentGUID}}/collections/{{resultsSetGUID}}/attach
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NewRelationshipRequestBody",
      "properties": {
        "class": "ResourceListProperties",
        "resourceUse": "Related Information",
        "resourceUseDescription": "Terms this team is currently reviewing for confidence."
      }
    }
    ```

=== "pyegeria"

    ```python
    resource_list_body = {
        "class" : "NewRelationshipRequestBody",
        "properties": {
            "class": "ResourceListProperties",
            "resourceUse": "Related Information",
            "resourceUseDescription": "Terms this team is currently reviewing for confidence.",
        }
    }

    collection_manager.attach_collection(parent_guid, results_set_guid, body=resource_list_body)
    ```

`parentGUID` here is the GUID of the team or project element - substitute whichever element represents the people who set up the smart collection.

### Step 6 (optional): Ask for an immediate refresh

The connector refreshes every 30 minutes by default.  To see results sooner, ask the integration daemon hosting it to refresh it now:

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{integrationDaemon}}/open-metadata/integration-daemon/integration-connectors/refresh
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "NameRequestBody",
      "name" : "SmartCollectionsMembershipManager"
    }
    ```

=== "pyegeria"

    ```python
    from pyegeria import EgeriaTech

    egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
    egeria_tech.create_egeria_bearer_token()

    egeria_tech.refresh_integration_connectors(
        connector_name="SmartCollectionsMembershipManager",
        server="integration-daemon",
    )
    ```

    Replace `"integration-daemon"` with the name of the [integration daemon](/concepts/integration-daemon) that has the SmartCollectionsMembershipManager connector configured.


## Retrieving the membership of a smart collection

Once the connector has run at least once, the results set can be read like any other collection - the fact that its membership is maintained automatically is invisible to the caller retrieving it.

=== "REST"

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{resultsSetGUID}}/members
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "ResultsRequestBody",
      "startFrom" : 0,
      "pageSize": 0
    }
    ```

    To check the results set's own status properties (`createdTime`, `startTime`, `completionTime`, `completionMessage`) rather than its members, retrieve the collection itself:

    ```http
    POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{resultsSetGUID}}/retrieve
    Authorization: Bearer {{token}}
    Content-Type: application/json

    {
      "class" : "GetRequestBody"
    }
    ```

=== "pyegeria"

    ```python
    members = collection_manager.get_collection_members(collection_guid=results_set_guid)

    for member in members:
        properties = member.get("properties", {})
        print("* " + properties.get("qualifiedName", "") + " - " + properties.get("displayName", ""))

    # Check the status of the most recent refresh
    results_set = collection_manager.get_collection_by_guid(results_set_guid)
    results_set_properties = results_set.get("properties", {})
    print("Last refreshed:", results_set_properties.get("completionTime"))
    print("Outcome:", results_set_properties.get("completionMessage") or "succeeded")
    ```

<!-- SCREENSHOT PLACEHOLDER: smart-collection-members.png - a results set and its current membership, as shown in the Egeria UI. -->
*(Screenshot to follow: a results set and its current membership, as displayed in the Egeria UI.)*


## Security: membership is filtered per caller

The SmartCollectionsMembershipManager connector runs as its own configured userId (`smartcnpa`), authenticating its REST calls with a bearer token drawn from a [secrets store](/concepts/secrets-store-connector).  This userId is typically given broad read access across the metadata ecosystem, because the connector needs to be able to run the saved query effectively and build a genuinely complete picture of what matches - if its own permissions were as narrow as an individual team member's, the results set could quietly miss elements that the team actually needed to see.

This means the membership the connector stores in the results set can be a **fairly complete set of results compared to what any individual caller might see directly** - it reflects what the query matches from the connector's own, broad vantage point, not from the vantage point of whoever eventually looks at the collection.

That gap is closed at read time, not at write time.  When [Open Metadata Security](/features/metadata-security/overview) is configured, every retrieval of a results set's membership - whether over REST or through pyegeria - is subject to the same per-caller checks as any other metadata read: `OpenMetadataRepositorySecurity.validateUserForEntityRead` and `validateUserForRelationshipRead` are applied for the *calling user's own identity*, and `OpenMetadataAssetSecurity.validateUserForAssetRead` (including [governance zone](/features/governance-zoning/overview) visibility) applies too if the members are assets. Each of these checks can redact or remove content the caller is not entitled to see.

The practical consequence: two people retrieving the membership of the same smart collection, at the same moment, can legitimately see different results - each sees the subset of what the connector found that they, personally, are authorized to read.  The count and content the connector recorded on the results set (and anything you observe by querying as an administrator or as the connector's own userId) should be treated as the connector's broad view, not as a promise of what every viewer will actually receive.


## Related information

* [0725 Smart Collections](/types/7/0725-Smart-Collections) - the open metadata types (`ResultsSet`, `SavedQuery`, `SmartQuery`) that a smart collection is built from.
* [Collections](/concepts/collection) - background on collections generally, including other uses of results set collections.
* [Classification Explorer API](/services/omvs/classification-explorer/overview) and [Metadata Expert API](/services/omvs/metadata-expert/overview) - the APIs whose operations are typically used as a saved query's `queryURL`.
* [Collection Manager API](/services/omvs/collection-manager/overview) - creates and retrieves collections, and links a results set to its saved query.
* [Asset Maker API](/services/omvs/asset-maker/overview) - creates the saved query asset and attaches catalog targets to integration connectors.
* [Open Metadata Security](/features/metadata-security/overview) - the per-caller filtering applied whenever a results set's membership is read.
* [Integration Connector](/concepts/integration-connector) and [Catalog Target](/concepts/catalog-target) - background on how the SmartCollectionsMembershipManager is configured to work on a specific results set.

--8<-- "snippets/abbr.md"
