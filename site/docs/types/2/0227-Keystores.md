<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0227 Keystores

The keystores store secrets.  They are needed to validate the identity of the people and processes using IT systems.

![UML](0227-Keystores.svg)

## KeyStoreFile entity

The *KeyStoreFile* entity represents a file that stores secrets.  For example, Egeria uses YAML encoded [secrets store files](/concepts/secrets-store-connector) to store its secrets.

## SecretsCollection entity

A *SecretsStoreCollection* entity represents a collection of related secrets. A key store file may hold multiple secrets collections.  In open metadata, they are connected by the [DataSetContent](0210-Data-Stores.md) relationship.

The secrets store collection may contain many types of secrets, from credentials to user accounts, security groups security roles and security access controls.

The diagram below shows the structure of the `coco-user-directory.omsecrets` file that holds the default user directory for the [OMAG Server Platform](/concepts/omag-server-platform).  The types used to model the secrets inside a secrets collection are defined in [model 0423](/types/4/0423-Security-Controls).

![Key Store Example](keystore-example.svg)

--8<-- "snippets/abbr.md"

