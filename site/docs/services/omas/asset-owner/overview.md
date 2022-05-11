<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Asset Owner OMAS

| Description              | Value                                                                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link to Implementation   | [open-metadata-implementation/access-services/asset-owner :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/access-services/asset-owner){ target=gh } |
| Audit Log Component Id   | 205                                                                                                                                                                                            |
| Audit Log Message Prefix | OMAS-ASSET-OWNER                                                                                                                                                                               |
| URL Marker               | asset-owner                                                                                                                                                                                    |


The Asset Owner OMAS provides APIs and notifications for tools and applications supporting the work of *Asset Owners* in protecting and enhancing their assets.

## What is an Asset Owner?

An asset may have the [`Ownership` classification](/types/4/0445-Governance-Roles) attached.  This identifies the owner of the asset.  This may be a [user identity](/concepts/user-identity), [person role](/concepts/person-role) or [profile](/concepts/personal-profile).

The owner is responsible for the correct classification of assets and the assignment of connection(s) to the asset.  The owner typically links the asset (or more likely the asset's schema elements) to glossary terms and declares the asset's associated licenses and certifications.

Asset owners can maintain a note log for each of their assets.  They can view the feedback and respond to it.  The Asset Owner OMAS generates notifications about new feedback linked to an asset.



--8<-- "snippets/abbr.md"
