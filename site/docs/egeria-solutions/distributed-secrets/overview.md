<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Distributed Secrets

An open metadata ecosystem connects to a great many systems.  Each integration connector that catalogs a database, each governance service that checks a security group, and each user that logs on needs a secret - a password, an API key, a certificate or a token.  If those secrets are copied into configuration files, connection definitions or the metadata repository, every copy is another place they can leak from, and changing a password becomes a hunt through the estate.

The *Distributed Secrets* solution keeps secrets where they need to be, and nowhere else.  Secrets are held in secure *secrets stores*, close to the components that use them and under the control of the people responsible for them.  Only the *name* of a secret travels through Egeria's configuration and open metadata.

## How secrets are kept out of open metadata

A [secrets store connector](/concepts/secrets-store-connector) provides access to a secrets store at runtime.  It is embedded in the connector that needs the secrets, and the two are initialized together by the [connector broker](/concepts/connector-broker).

* The [connection](/concepts/connection) for the outer connector holds only the *names* of the secrets it needs, in its secured properties.
* At runtime, the secrets store connector retrieves the real values from the secrets store.  If the outer connector expects the standard *userId*, *clearPassword* or *encryptedPassword* values in its connection, the connector broker fills them in automatically, so existing connectors do not need to change.
* Secrets are grouped into named *secrets collections*, each holding everything needed for one kind of connection - the secret values, a description of any token-issuing API to call, and a refresh interval so that rotated secrets are picked up without a restart.

Since the secrets store is separate from the configuration document and the [open metadata repository](/concepts/open-metadata-repository), copying, exporting or backing up the metadata does not copy the secrets.

## Putting the secrets where they are used

Each component can use its own secrets store, located in the environment where it runs.  This is what makes the solution *distributed*.  For example, an [integration connector](/concepts/integration-connector) can run in a secured data centre, harvesting metadata into a metadata repository running in an external cloud service.  Its secrets store sits in the same data centre and is managed by the data centre's own team.  They keep complete control of the credentials, and only the name of the secret is known outside the data centre.  The same pattern applies to [governance services](/concepts/governance-service) running in an [engine host](/concepts/engine-host).

When someone sets up a new integration connector, the [Automated Curation API](/services/omvs/automated-curation/overview) can save the [client-side secret](/concepts/client-side-secret) it needs directly into a nominated secrets store.  The credentials are supplied at the point of configuration, without ever being written into the connector's configuration.

## Protecting access to Egeria itself

The same mechanism protects the open metadata ecosystem.  The OMAG Server Platform's user directory - the user accounts, their passwords, their security roles and groups, and the security access controls for each [governance zone](/features/governance-zoning/overview) - is held in a secrets store and accessed through a secrets store connector by the [open metadata security connectors](/features/metadata-security/overview).

When a user logs on, they exchange their user identifier and password for a bearer token, which is then used to authenticate each API call.  The password is not passed on to the services that the user calls, and the token expires after an hour.

The user directory is maintained through the [Security Officer API](/services/omvs/security-officer/overview) and reviewed with the [Auditing Users](/egeria-solutions/auditing-users/overview) solution, which flags any user account that still has a clear text password.

## Available secrets stores

Egeria provides a secrets store connector for YAML files placed in the secure execution environment of the [OMAG Server Platform](/concepts/omag-server-platform).  The default user directory, `coco-user-directory.omsecrets`, uses this format, and its structure is described in [0227 Keystores](/types/2/0227-Keystores).

Secrets store connectors are pluggable, so organizations that use an enterprise secrets manager or vault can write a connector for it, allowing Egeria to use the same secrets management as the rest of the estate.

!!! summary "Usage"
    Distributed secrets reduce the number of places that a secret is stored to one, put that place under the control of the people responsible for it, and allow secrets to be rotated without reconfiguring Egeria.  This keeps the open metadata ecosystem from becoming a weak point in the organization's security.

!!! education "Further information"
    * [Open Metadata Security](/features/metadata-security/overview) describes the security connectors and secrets stores.
    * [Configuring the OMAG Server Platform](/guides/admin/configuring-the-omag-server-platform) shows how to set the location of the platform's user directory.

--8<-- "snippets/abbr.md"
