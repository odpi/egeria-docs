<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Open Integration Framework (OIF)

The *Open Integration Framework (OIF)* provides the interfaces for running [integration connectors](/concepts/integration-connector).

## Integration connector interfaces

The OIF is built on the [Open Connector Framework (OCF)](/frameworks/ocf/overview).  As such, it offers interfaces for the integration connector and the associated connector provider that extend the *Connector* and *ConnectorProvider* OCF interfaces respectively.

Specifically it offers:

* *IntegrationConnector* is the interface that is specific to an integration connector.
* *IntegrationConnectorBase* is the base class for an integration connector.  It provides implementations of the *initialize()*, *start()* and *disconnect()* methods as well as useful functions needed by many integration connectors.
* *IntegrationConnectorProvider* is the base class for the integration connector's [connector provider](/concepts/connector-provider).

## Integration context

The *IntegrationContext* class provides the base class for the context object that provides open metadata services to the integration connector.  The integration context is passed to the integration connector between *initialize()* and *start()* method calls.

## Catalog target

A catalog target is an open metadata element that the integration connector should use as a root element for its work.

## Permitted synchronization

The *PermittedSynchronization* enumeration can be used to limit the activities of a particular integration connector.  It is set in the integration connector's configuration and enforced by the context.

## Integration context manager

The context manager is responsible for setting up the integration context for the integration connector.

## Framework implementation

Egeria provides a full implementation of the OIF. It provides an [integration daemon](/concepts/integration-daemon) server where the integration connectors run.  There are specialist [integration services](/services/omis) that provide specialist integration contexts along with their integration context manager.
There are also implementations of integration connectors in the [integration-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors){ target=gh } module.

--8<-- "snippets/abbr.md"

