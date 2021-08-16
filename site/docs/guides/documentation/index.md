<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Documentation guide

We strive to provide complete, concise and maintainable documentation for the project. To achieve these goals, all contributed documentation should adhere to the guidance provided in this *documentation guide*, split into the following sub-guides:

- [Formatting standards](formatting) to keep the content of the documentation consistent.
- [Style guide](style) to keep the documentation clear and understandable.

## Technical context

The repository hosting the documentation for Egeria is separate from the individual code repositories, and is maintained at [odpi/egeria-docs :material-github:](https://github.com/odpi/egeria-docs){ target=gh }.

The documentation itself is all managed as Markdown files for ease of maintenance and readability. We use the [MkDocs :material-dock-window:](https://www.mkdocs.org){ target=mkdocs } generator along with the [Material for MkDocs :material-dock-window:](https://squidfunk.github.io/mkdocs-material/){ target=material } theme to generate a static website from these Markdown files. This static website is deployed to the `gh-pages` branch of the documentation repository, from which GitHub pages then hosts the documentation website itself.

## Adding to the documentation

When contributing to the documentation, you can easily use this to test documentation changes out on your own machine locally before committing them in a PR:

1. On a Mac, just do a `brew install mkdocs` (requires [HomeBrew](https://brew.sh)).
2. Then do a `pip3 install mkdocs-material [--upgrade]` (the last bit you might want to add and re-run periodically to keep things up-to-date).
3. From the `site` directory of your local clone of this repository, you can then just run:

    ```shell
    $ mkdocs serve
    ```

... and you'll shortly have a local documentation site running on your local machine, complete with any changes you make (each change you make will auto-refresh the content and your browser).

!!! tip "Look for warnings"
    As part of running its generator, MkDocs will automatically warn you if it finds any broken links within your documentation. Pay close attention to these, as the PR merge mechanism for documentation will strictly enforce that no broken links are found in order to merge any changes into the main documentation.

--8<-- "snippets/abbr.md"
