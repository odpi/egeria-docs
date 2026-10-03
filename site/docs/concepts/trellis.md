<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Trellis

*Trellis* is the home of Egeria's AI applications.  Its [egeria-trellis :material-github:](https://github.com/odpi/egeria-trellis){ target=gh } git repository holds the applications that use large language models (LLMs) and retrieval-augmented generation (RAG) alongside the open metadata ecosystem, together with the libraries they share.

Egeria is central to each Trellis application.  It is the catalog of record for what the applications discover and create, and it is also the identity provider - you sign in to a Trellis application with your Egeria user identity, and the application calls Egeria as you.  The elements it publishes record you as their owner.  The applications call Egeria through [pyegeria](/concepts/pyegeria).

## The applications

There are currently two applications:

* **Resource Explorer** discovers, surveys and catalogs information resources - git repositories, PostgreSQL databases and file systems - using Egeria as the catalog.  It supports *scouting* (a fast, broad inventory across many resources), *assessment* (a deep analysis of a single resource's structure, security and quality), *discovery* (finding resources by what the surveys revealed) and *enrichment* (where people add context and answer the open questions that the surveys raised).  Investigations are recorded in Egeria as [projects](/concepts/project) with [working sets](/types/0/0021-Collections) of the resources being explored, and its survey results are stored as [survey reports](/concepts/survey-report) and annotations.  It can also recover the architecture of the resources it has explored and, once a reviewer has accepted the findings, record it as solution blueprints.
* **Egeria Advisor** is a conversational assistant for people working with Egeria and pyegeria.  It answers questions about Egeria's concepts and code, finds examples and definitions, and can carry out actions on your behalf through [Dr.Egeria](/user-interfaces/dr-egeria/overview) commands and reports.  Its answers are tailored to the [perspective](/concepts/perspective) you select, such as developer, data engineer, data steward or governance officer.

Each application is deployed and run independently of the other.

## How Trellis is organized

The git repository is a single Python workspace (managed with `uv`) containing the two applications and six libraries that they share.  The libraries cover authentication against Egeria (including the single sign-on hand-off from the [Egeria Workspaces](/egeria-workspaces) portal), a PostgreSQL/pgvector vector store, bounded context assembly for the LLM, the structure of ingested artifacts, step execution and query caching.  Keeping the applications in one workspace means that this common code is shared without version skew, while each application remains a separately deployable service.

By default the applications use a local [Ollama](https://ollama.com) server for their language models, and a PostgreSQL database with the pgvector extension for their vector collections.

## Running Trellis

There are two ways to run the applications:

* As an optional runtime alongside [Egeria Workspaces](/egeria-workspaces).  The *trellis* optional runtime starts Resource Explorer and Egeria Advisor against the Quickstart environment, and the Egeria Workspaces portal has tiles that open each application with single sign-on.  Variants of the runtime use Ollama running on the host, in a container, or on an NVIDIA or AMD (ROCm) GPU.
* From a clone of the git repository, following its `QUICKSTART.md`.  An Egeria platform is still needed, since it is the identity provider.

!!! attention "Technical preview"
    The Trellis applications are technical previews.  They are under active development, their behaviour and the metadata they create may change from release to release, and the answers produced by the language models are not always accurate.  We are looking for feedback: please tell us what works for you and what does not, by raising an issue in the [egeria-trellis repository :material-github:](https://github.com/odpi/egeria-trellis/issues){ target=gh } or by joining us on [Slack :fontawesome-brands-slack:](https://slack.lfaidata.foundation){ target=slack }.

!!! info "Further information"
    * [egeria-trellis git repository :material-github:](https://github.com/odpi/egeria-trellis){ target=gh }
    * [Egeria Workspaces](/egeria-workspaces)
    * [pyegeria](/concepts/pyegeria)

--8<-- "snippets/abbr.md"
