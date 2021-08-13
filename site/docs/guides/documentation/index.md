<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Documentation guide

We strive to provide complete, concise and maintainable documentation for the project. To achieve these goals, all contributed documentation should adhere to the guidance provided in this **documentation guide**, split into the following sub-guides:

- [Formatting standards](formatting) to keep the content of the documentation consistent.
- [Style guide](style) to keep the documentation clear and understandable.

## Technical context

The repository hosting the documentation for Egeria is separate from the individual code repositories, and is maintained at [odpi/egeria-docs :material-github:](https://github.com/odpi/egeria-docs){ target=gh }.

The documentation itself is all managed as Markdown files for ease of maintenance and readability. We use the [MkDocs :material-dock-window:](https://www.mkdocs.org){ target=mkdocs } generator along with the [Material for MkDocs :material-dock-window:](https://squidfunk.github.io/mkdocs-material/){ target=material } theme to generate a static website from these Markdown files. This static website is deployed to the `gh-pages` branch of the documentation repository, from which GitHub pages then hosts the documentation website itself.

--8<-- "snippets/abbr.md"
