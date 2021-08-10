<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

[![License](https://img.shields.io/badge/license-CC--BY--4.0-green)](LICENSE)

# README

This repository exists to host the documentation for the Egeria project across its various code repositories.
The documentation itself should be accessed through GitHub pages at: []().

## Contributing

This project welcomes contributors from any organization or background, provided they are
willing to follow the simple processes outlined below, as well as adhere to the
[Code of Conduct](https://github.com/odpi/specs/wiki/ODPi-Code-of-Conduct).

Review the [community guide](https://egeria.ai/guides/community) to find out more.

## Documentation development

The documentation is written entirely in Markdown, but uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
project to generate the static content of the website itself from this Markdown input.

You can easily use this to test documentation changes out on your own machine locally
before committing them in a PR:

1. On a Mac, just do a `brew install mkdocs` (requires [HomeBrew](https://brew.sh)).
2. Then do a `pip3 install mkdocs-material [--upgrade]` (the last bit you might want to add and re-run periodically to keep things up-to-date).
3. From the `site` directory of your local clone of this repository, you can then just run:

    ```shell
    $ mkdocs serve
    ```

... and you'll shortly have a local documentation site running on your local machine, complete
with any changes you make (each change you make will auto-refresh the content and your browser).

----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the Egeria project.
