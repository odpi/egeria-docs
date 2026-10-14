<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Translations

An organization that operates across several countries needs its open metadata to be understood by people who work in different languages.  Egeria supports this by keeping each metadata element in a single *primary language* and attaching translations of its descriptive properties for each additional language.  A user interface can then show the translation that matches its user's language, and fall back to the original where there is none.

Translations are cheap to store but expensive to write and keep up to date, so it is worth deciding at the planning stage:

* what the primary language of the open metadata ecosystem is,
* which metadata elements should be translated, and into which languages, and
* who is responsible for creating and maintaining each translation.

These decisions are much easier to make before metadata is loaded than to retrofit once the catalog is in use.

## Choosing the primary language

The primary language is the language in which the properties of the metadata elements themselves are written - their display names, descriptions and other descriptive text.  It is the authoritative version: translations are derived from it, and when they disagree, the original wins.

Consider the following when choosing it:

* **The language of the people who maintain the metadata.**  Most metadata is written by the data owners, stewards and engineers who catalog the resources.  The primary language should be one that they can all write in.
* **The language of the harvested metadata.**  Much of the catalog is captured automatically by [integration connectors](/concepts/integration-connector) from the systems they catalog, and arrives in whatever language those systems use - often English for technical names.  Choosing a different primary language means these elements need either translating or rewriting.
* **The language of the content packs.**  The [content packs](/content-packs) supplied with Egeria, such as the definitions of technology types and templates, are written in English.

Some properties are never translated.  The *qualifiedName* of an element is its unique name and is used to identify it in integration and automation, so it stays the same in every language.  Neither are the technical names that must match the real resource, such as the name of a database column or a file.

!!! tip "Agree a naming convention for languages"
    A translation is found again by its *language* property, which is matched exactly - `Spanish`, `spanish` and `Castellano` are three different languages to Egeria.  Agree on one form for the names of the languages (and, if used, the locales) before any translations are written, and record them as [valid values](/guides/planning/valid-values/overview) so that the tools that create translations use the same ones.  The *languageCode* property can hold a standard code, such as one from ISO-639, alongside it.

## Deciding where translations are needed

Translating everything is rarely worthwhile.  Focus on the metadata that is read by people who do not work in the primary language, and that changes slowly enough for the translations to stay current.  Good candidates are:

* **[Glossary](/types/3/0310-Glossary) terms** - the business vocabulary is the most widely read part of the catalog and is often the first thing that users in other countries look up.
* **[Digital products](/concepts/digital-product)** - their descriptions are how consumers decide whether a product meets their needs.
* **[Governance definitions](/concepts/governance-definition)** - policies, rules and obligations that people in every country are expected to follow.
* **[Valid values](/concepts/valid-value-definition) and reference data** that are shown in user interfaces or reports.
* **[Subject area](/concepts/subject-area) descriptions** that orient new users.

Technical metadata that is maintained by integration connectors is usually a poor candidate.  It changes whenever the system it describes changes, and nothing marks a translation as out of date when the element it translates is updated.

For each kind of element, also decide:

* **Which languages it needs.**  Not every element needs every language.  Policies may need to be in the languages of every country they apply to, while a glossary for a local team only needs the languages of that team.
* **Which properties are translated.**  A translation has explicit *displayName* and *description* properties.  Any other string properties, such as a glossary term's *summary*, *examples* or *usage*, go in its *additionalTranslations* map, keyed by the property name.  Agree which properties are included for each type, so translations are consistent.
* **Whether locales are needed.**  One translation per language is usually enough.  Regional variants, such as Spanish for Spain and for Mexico, are only worth maintaining where the terminology or the regulations really differ.

An alternative for a community that works entirely in another language is a separate glossary written in that language: the [*Glossary*](/types/3/0310-Glossary/#glossary-entity) element has a *language* property to record which language it uses.  This suits vocabulary that is specific to one country, while translations suit vocabulary that is shared.

## Assigning responsibility

A translation is part of the metadata it translates, so it needs an owner in the same way.  Without clear responsibility, translations are written once and then drift as the original changes.

* **The owner of the original element is accountable** for its translations being correct.  For a glossary term this is typically the owner of its glossary or [subject area](/concepts/subject-area); for a policy it is the leader of its governance domain.
* **Translators are assigned per language**, and typically per subject area as well, since a good translation needs knowledge of both the language and the subject.  These can be set up as [governance roles](/types/4/0445-Governance-Roles) so that the responsibility is visible in the catalog - see [Governance Program](/guides/planning/governance-program/overview) for how roles are defined and assigned.
* **A change to the original needs to reach its translators.**  Agree how this happens: for example, the steward who approves a change to a glossary term raises a [to do](/concepts/to-do) for each translator of that term.

!!! summary "Planning checklist"
    * The primary language, and the naming convention for languages and locales.
    * The element types to translate, the languages each needs and the properties included.
    * The owner and translators for each group of elements, and how they learn of changes.

## Maintaining translations

Translations are maintained through the [Multi Language API](/services/omvs/multi-language/overview).  It attaches, updates, retrieves and removes the translations of any metadata element, and its page describes how a translation is matched to a language and locale.  Translations are stored as *TranslationDetail* elements, defined in [model 0022](/types/0/0022-Translations), and are [anchored](/concepts/anchor) to the element they translate, so they are removed with it.

--8<-- "snippets/abbr.md"
