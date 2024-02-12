<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Placeholders

A placeholder is a replaceable value.  It is distinguished by a double set of curly braces - `{{placeholder}}`.  Placeholders allow concrete values to be substituted when an element is either created of used.  They are found in many technologies.  For example, both Postman and IntelliJ's HTTP client use placeholders in their REST API definitions to denote network addresses or identifiers.  These values are supplied when the REST request is made through an environment file.

Egeria has support for placeholders both in its [configuration documents](/concepts/configuration-document) and its [template](/features/templated-cataloguing/overview) support that is used when creating metadata.