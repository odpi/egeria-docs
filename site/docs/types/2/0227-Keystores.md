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

## UserAccountProfile classification

The *UserAccountProfile* classification is used to describe the type and status of user accounts that are defined in the attach secrets collection.

* *userAccountCount* - Count of the user accounts in the secrets store.
* *employeeAccountCount* - Count of the employee user accounts in the secrets store.
* *contractorAccountCount* - Count of the contractor user accounts in the secrets store.
* *externalAccountCount* - Count of the external user accounts in the secrets store.
* *digitalAccountCount* - Count of the digital user accounts in the secrets store.
* *activeAccountCount* - Count of the active user accounts in the secrets store.
* *expiredAccountCount* - Count of the user accounts with expired credentials in the secrets store.
* *lockedAccountCount* - Count of the locked user accounts in the secrets store."
* *disabledAccountCount* - Count of the disabled user accounts in the secrets store.
* *additionalProperties* - additional properties for the user account profile.

--8<-- "snippets/abbr.md"

