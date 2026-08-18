<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Client-side secret

A *client-side secret* is a secret - a password, an API key, a certificate, a token - that is needed by an Egeria component acting as the *client* in a call to a third party system.  The most common case is an [integration connector](/concepts/integration-connector) that has to authenticate with the technology it is cataloguing, but any connector making an outbound call has the same need.

The secret is never held in the [connection](/concepts/connection) object, the [configuration document](/concepts/configuration-document) or the [open metadata repository](/concepts/open-metadata-repository).  Instead it is stored in a secure secrets store and retrieved at runtime through a [secrets store connector](/concepts/secrets-store-connector).  Only the *name* of the secret travels through open metadata; the value stays where the security team put it.

## Secrets collections

Secrets are grouped into named *secrets collections*.  A collection holds everything needed to make one kind of connection or to support one security service:

* *secrets* - the named secret values themselves.
* *tokenAPI* - a description of the token-issuing API to call, when the connection uses a token rather than a static credential.
* *refreshTimeInterval* - how often the connector should re-read the collection, so that rotated secrets are picked up without a restart.
* *users*, *namedLists* and *securityAccessControls* - the user accounts, lists and access control settings used when the collection is supporting an authentication or authorization service.

The secrets store itself is catalogued as an [asset](/concepts/asset), which is how it is identified when a client-side secret is being maintained.

## Maintaining client-side secrets

The [Automated Curation API](/services/omvs/automated-curation/overview) provides operations to save (create or replace) and to delete a client-side secret in a nominated secrets store.  This allows the person setting up an integration connector to supply the credentials it needs at the point of configuring it, without those credentials ever being written into the connector's configuration.

Once the secret is in place, the [connector broker](/concepts/connector-broker) initializes the secrets store connector alongside the connector that needs it, and the surrounding connector requests the secret by name when it starts up.

???+ info "Additional information"
    * [Secrets store connector](/concepts/secrets-store-connector) describes how secrets are retrieved at runtime, including how the standard *userId*, *clearPassword* and *encryptedPassword* values are filled in automatically.
    * The *securedProperties* of a [connection](/concepts/connection) hold the names of the secrets that a connector needs - see [Model 0201 Connectors and Connections](/types/2/0201-Connectors-and-Connections).

--8<-- "snippets/abbr.md"
