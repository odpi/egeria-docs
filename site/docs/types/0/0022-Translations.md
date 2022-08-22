<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0022 - Translations

Translations provide a means to create alternative text in different languages to support a multilingual deployment of open metadata.

The *TranslationDetails* holds the translation for a single language. It includes the *language* and *locale*.  There are explicit properties of *displayName* and *description* for holding the translation for the *name*/*displayName* and *description* properties respectively.  Any other string properties that need a translation are added to *additionalTranslations*.

The TranslationDetails are linked to the original entity using the *TranslationLink* relationship.

![UML](0022-Translations.svg)


??? education "Further information"
    Translations can be maintained and retrieved through the [*Metadata Store Services*](/services/gaf-metadata-management) that are supported by all [Open Metadata Access Services (OMASs)](/services/omas).

--8<-- "snippets/abbr.md"
