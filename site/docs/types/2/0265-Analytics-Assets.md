<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0265 Analytics Assets

The term *Analytics* is use here to describe processing that is trained and operated using data.  [Analytical Development Assets](/types/2/0285-Analytical-Development-Assets) cover the training process.  The assets below describe the deployed and running components.

![UML](0265-Analytics-Assets.svg)

## DeployedAnalyticsModel entity

The *DeployedAnalyticsModel* entity describes an Analytics Model that is deployed into one or more IT infrastructure environments.  It is a type of [DeployedSoftwareComponent](/types/2/0215-Software-Components).

## AnalyticsModelRun entity

The *AnalyticsModelRun* entity describes an invocation of a deployed Analytics Model.  It is a type of [TransientEmbeddedProcess](/types/2/0215-Software-Components).

An *AnalyticsModelRun* entity is typically linked to its *DeployedAnalyticsModel* entity using the [ProcessHierarchy](/types/2/0215-Software-Components) relationship.

--8<-- "snippets/abbr.md"