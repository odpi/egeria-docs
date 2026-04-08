---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Dr Egeria MD

MD is short for Markdown.  It is a lightweight markup language that can be used to create documents.  Markdown is widely used in software development, documentation, and blogging.  It is also supported in a great many tools.  Markdown documents can be shared through email and chat interfaces.  They are also parsable by AI document processors.  In summary, markdown is an excellent format for gathering information from subject-matter experts and documenting projects, ideas, requirements, specifications, and other proposals. 

Dr.Egeria MD is a markdown document processor that can be used to create and update open metadata as well as build reports.

![Dr Egeria](dr-egeria.svg)
> **Figure 1:** Dr Egeria in operation

A single markdown document can include explanatory text and diagrams interspersed with commands to the Dr.Egeria command processor.  

![Form Structures](form-structure.svg)
> **Figure 2:** Dr Egeria Form Structures

When the document is processed, Dr.Egeria reads the document, extracts the commands and turns them into calls to Egeria's rest API.  The commands may be to maintain open metadata elements or create a report.  

Reports may extract information as text, tables or mermaid diagrams. They are created in a new document from the form requesting that the report is generated.

With Dr.Egeria it is possible to create, maintain and report on:

* Glossaries and glossary terms
* Projects
* Collections
* Digital Products
* Data dictionaries and data specifications
* Solution components, roles and blueprints
* Feedback (comments, tags, likes and ratings) to existing metadata elements
* Governance Definitions such as License Types and Certification Types
* External References, such as Data Source Descriptions


## Using Obsidian

[Obsidian](https://obsidian.md/) is a popular markdown editor that supports [Mermaid Diagrams](/user-interfaces/mermaid/overview) and plug-in markdown processors such as Dr.Egeria.  Obsidian is free to use and available on many platforms.  

Dr.Egeria includes two types of plug-ins for Obsidian.  The first is a collection of command templates that can be browsed and pasted into a markdown document.  Once the command is filled out, the **Call Dr.Egeria** function can be selected to process the markdown document.

![Obsidian](obsidian.svg)
> **Figure 3:** The Obsidian Desktop

Obsidian therefore makes a very flexible and easy to use desktop environment for editing, organizing and processing Dr.Egeria forms and reports.

???+ note "Further Information"
    * [Mermaid Diagrams](/user-interfaces/mermaid/overview)
    * [Dr.Egeria Introduction - Part 1](https://github.com/odpi/egeria-python/blob/main/sample-data/egeria-inbox/dr-egeria-inbox/dr_egeria_intro_part1.md)
    * [Dr.Egeria Introduction - Part 2](https://github.com/odpi/egeria-python/blob/main/sample-data/egeria-inbox/dr-egeria-inbox/dr_egeria_intro_part2.md)
    * [Dr.Egeria Introduction - Part 3](https://github.com/odpi/egeria-python/blob/main/sample-data/egeria-inbox/dr-egeria-inbox/dr_egeria_intro_part3.md)

--8<-- "snippets/abbr.md"