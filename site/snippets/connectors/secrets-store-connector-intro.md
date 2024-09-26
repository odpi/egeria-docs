<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


The *secrets store connector* provides access to secrets such as passwords and certificates that are stored in a secure location.  Its purpose is to remove the need to store secrets in Egeria's [configuration document](/concepts/configuration-document) or [open metadata repository](/concepts/open-metadata-repository).  With the secrets store connector, it is possible to manage secrets relating to a resource or service connected to the open metadata ecosystem in secure vaults or services managed by the security team.

The secrets store connector is typically embedded in a connector that needs one or more secrets to perform its tasks.  Both connectors are initialised together by the [ConnectorBroker](/concepts/connector-broker).  The secrets store connector is called by the surrounding connector to extract the needed secrets.

![Secrets store connector](/connectors/secrets/secrets-store-connector.svg)

When the *ConnectorBroker* detects that there is a secrets connector embedded in another connector, it attempts to retrieve the standard secrets for the corresponding connection object (if they are null):

* userId
* clearPassword
* encryptedPassword

This means that even if the outer connector is written to expect these secrets in its connection object, they do not need to be stored in the connection object (ie in the configuration document or in the metadata store) but will be placed in the right fields by the [ConnectorBroker](/concepts/connector-broker).

If the name(s) of the secret(s) needed by the connector must be configured, they can be stored in the securedProperties.  The connector code knows the logical name and it looks up the real secret's name in secured properties.  Then the real secret's name is passed to the secrets store connector to do the look up for the secret value.

![Secrets store connector](/connectors/secrets/secured-properties.svg)

The picture below shows a practical example of using the secrets store connector.  It is embedded in an [integration connector](/concepts/integration-connector) which is deployed in a secured data centre to harvest metadata which is stored in an external cloud service.  The secrets store connector is initialized with the integration connector, both running in the secured data centre.  The secrets store connector uses a secrets store located in the secured data centre and managed by the data centre's team.  The data centre's team has complete control of the secrets that are being used by the integration connector and only the name of the secret is known outside of the secured data centre.

![Secured data centre](/connectors/secrets/secrets-store-connector-example.svg)

This pattern can also be used in the [Engine Host](/concepts/engine-host) with [governance services](/concepts/governance-service).

