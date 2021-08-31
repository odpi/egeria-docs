<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Formatting Standards

These formatting standards exist to keep the content of the documentation consistent.

## Links

### Link within docs using absolute links

When linking between pages in the documentation use the regular Markdown linking syntax, but with the absolute path to the Markdown document or area you wish to link to. For example:

```markdown
... is a type of [OMAG Server](/egeria-docs/concepts/omag-server) that ...
```

!!! tip "Note that we do not need to point at a specific Markdown file"
    Note from the example above that we do not need to point at a specific Markdown file.

    In the example above, the actual file is `omag-server.md`; however, MkDocs will automatically generate an `omag-server/index.html` output for this Markdown which our URL above refers to.

    This syntax is useful because it means that if we start with a simple single file for some content (like `omag-server.md`) but later decide it needs additional explanation across various other files, we can simply turn this area of documentation into a directory (`omag-server`) with many files within it. The link above _does not need to change_ and will simply point to the `omag-server/index.md` that should exist after moving from single-file to a directory-based documentation for that area.

This ensures certain contexts in the documentation hierarchy are retained, even if deeply-nested documentation itself happens to move around, and takes advantage of the way MkDocs works to give us additional flexibility in extending the documentation later on without needing to retroactively go back and fix links everywhere that refers to that content.

### Link to code with a GitHub icon

When linking to one of the code repositories, add both a `:material-github:` icon to the end of the link name, and a target to the link:

```markdown
[`Foo` :material-github:](https://github.com/.../Foo.java){ target=gh }
```

This ensures that a reader clicking the link ([`Foo` :material-github:](https://example.com){ target=gh }) will know that they will be directed to code, and that it will open in a new tab / window.

### Link to other sites with a window icon

When linking to some other non-Egeria site, add both a `:material-dock-window:` icon to the end of the link name, and a target to the link:

```markdown
[some example :material-dock-window:](https://example.com){ target=example }
```

This ensures that a reader clicking [the link :material-dock-window:](https://example.com){ target=example } will know that they will be going to some non-Egeria site, and it will open in a new tab / window.

## Prefer SVG format for diagrams

Use regular Markdown syntax for images. For example:

```markdown
![Description of what the image depicts](image-filename.svg)
```

To make localization easier and enhance accessibility, the preferred image format is SVG. We recommend to use [draw.io](/egeria-docs/guides/developer/tools/documentation/#drawio){ target=draw } for creating images and diagrams. Use **Export as** to save your image in SVG format. Keep the **Include a copy of my diagram** option checked to allow later loading the SVG in draw.io and be sure to check **Embed images** if your diagram includes any.

If your diagram depicts a process, try to avoid adding the descriptions of the steps to the diagram. Instead, only add the numbers of the steps to the diagram and add the descriptions of the steps as a numbered list in the document. Ensure that the numbers on the list match the numbers on your diagram.

The SVG format allows the diagram to be dynamically scaled in the browser without introducing various image artifacts that create noise or otherwise impair visibility of the image: making the diagrams easier to understand.

Providing a description of the image is required for accessibility purposes, as it will act as the alternative text for e.g. screen-readers for anyone who is unable to see the image itself.

Avoiding text descriptions and explanations embedded in the diagrams means that the content is also more accessible (again for screen-readers), but also more broadly in that it is then indexed by the documentation site and can be searched. (Text embedded inside a diagram or image is not searchable.)

## Do **not** wrap lines

Avoid wrapping lines after a fixed number of characters or in a middle of a sentence. Instead, configure your editor to soft-wrap when editing documentation.

| Do | Don't |
|---|---|
| This is a long line. | This is a<br>long line. |

This enhances the maintainability of the documentation by a broader audience:

- different people will inevitably have different preferences for screen sizes and widths (we do not need to worry about constantly reformatting or scrolling what one or another contributor has decided is their own optimal line-break size)
- reviewing a diff of changes will be easier to identify actual content vs spacing / newline positioning changes
- changes in indentation that may be needed for e.g. bullet lists, inclusion within an admonition, etc will only require indenting the single wrapped line
- including content into a table in Markdown (which does not allow newlines within it) will be easier

## Use angle brackets for placeholders

Use angle brackets for placeholders in commands or code samples. Tell the reader what the placeholder represents. For example:

1. Display information about a pod:
    ```shell
    $ kubectl describe pod <pod-name>
    ```

    Where `<pod-name>` is the name of one of your pods.

!!! attention "We may revise this approach in the future"
    We may revise this approach if / when we start to make use of the theme's [extensive code annotation capabilities :material-dock-window:](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-annotations){ target=material } that allow such descriptions of the placeholders to be embedded more directly within the code block itself.

## Use **bold** to emphasize user interface elements

Use Markdown's double-asterisk to indicate **bold**:

```markdown
Click **Fork**.
```

| Do | Don't |
|---|---|
| Click **Fork**. | Click "Fork". |
| Select **Other**. | Select 'Other'. |

This enhances the readability of the key actions that a user is expected to take through a user interface.

!!! question "Why use double-asterisk (`**`) and not double-underscore (`__`)?"
    Markdown applications in general do not agree on how to handle underscores in the middle of words. While we would expect this need to be rare, the double-asterisk form allows bold to be used even within the middle of a word.

## Use **bold** to emphasize important text

Use **bold** to emphasize text that is particularly important. Avoid overusing bold as it reduces its impact and readability.

| Do | Don't |
|---|---|
| Examples of **bad** configurations: | Examples of **bad configurations**: |
| The maximum length of the name field is **256 characters**. | **The maximum length of the name field is 256 characters.** |

## Do **not** use capitalization for emphasis

Only use the original capitalization found in the code or configuration files when referencing those values directly. Use back-ticks `` ` ` `` around the referenced value to make the connection explicit. For example, use `InstanceHeader`, not `Instance Header` or `instance header`.

If you are not referencing values or code directly, use normal sentence capitalization, for example, "The instance header captures key information about the metadata instance like its GUID."

For code, the `back-tick` form is intended to represent **exactly** what you're referring to, so you should specify it exactly as it is defined: with precisely the same spacing, capitalization, etc.

For non-code values, [mixing capitalization makes the text harder to scan and comprehend, as well as more difficult and therefore stressful to read :material-dock-window:](https://readabilityguidelines.co.uk/grammar-points/capital-letters/){ target=readability }. Therefore, using normal sentence capitalization greatly enhances the readability of the content.

The **only** exceptions to this should be as follows:

- Proper nouns (i.e. Egeria)
- Any phrase that is prefixed or suffixed with Open Metadata (or an OMxx abbreviation)
- Any phrase that we commonly abbreviate using an acronym (i.e. frameworks like Open Discovery Framework): check the `snippets/abbr.md` for a list of such common abbreviations.

| Do | Don't |
|---|---|
| Egeria | egeria |
| Open Metadata Repository Services (OMRS) | open metadata repository services |
| repository services | Repository Services |
| Asset Consumer OMAS | asset consumer OMAS |
| OMAG Server Platform | OMAG server platform |
| OMAG Server | OMAG server |
| metadata access point | Metadata Access Point |
| Metadata Access Point OMAG Server | metadata access point OMAG Server |
| Open Discovery Framework (ODF) | open discovery framework |
| Audit Log Framework (ALF) | audit log framework |

## Use *italics* to emphasize new terms

Use Markdown's single-asterisk to indicate *italics*:

| Do | Don't |
|---|---|
| A *cluster* is a set of nodes ... | A "cluster" is a set of nodes ... |
| These components form the *control plane*. | These components form the **control plane**. |

!!! question "Why use single-asterisk (`*`) and not single-underscore (`_`)?"
    Markdown applications in general do not agree on how to handle underscores in the middle of words.
    While we would expect this need to be rare, the single-asterisk form allows italics to be used even
    within the middle of a word.

## Use `back-ticks` around file names, directories, and paths

| Do | Don't |
|---|---|
| Open the `foo.yaml` file. | Open the foo.yaml file. |
| Go to the `/content/docs/architecture` directory. | Go to the _/content/docs/architecture_ directory. |
| Open the `/data/args.yaml` file. | Open the **/data/args.yaml** file. |
| Go to the `/docs` directory. | Go to the "/docs" directory. |

## Use `back-ticks` around inline code, commands, objects and field names

| Do | Don't |
|---|---|
| The `foo run` command creates a `Deployment`. | The "foo run" command creates a `Deployment`. |
| For declarative management, use `foo apply`. | For declarative management, use **foo apply**. |
| Set the value of the `ports` field in the configuration file. | Set the value of the "ports" field in the configuration file. |
| The value of the `rule` field is a `Rule` object. | The value of the **rule** field is a `Rule` object. |

Only use inline code and commands to mention specific labels, flags, values, functions, objects, variables, modules, or commands.

## Code blocks

Use the provided custom admonitions for code and configuration blocks, within which the standard Markdown triple `back-tick` approach can be used to give the code block itself.

Using the triple `back-tick` approach ensures that we can include syntax highlighting for the specific language being shown within the code block, and provides a simple single-click link mechanism for the reader to copy the entire content of that code block for further revision or pasting elsewhere.

Each admonition wraps these to give a distinct visual cue as to its content: allowing us to avoid other cues that we might otherwise need to embed within the code block itself (for example, the `$` or `#` command-line prompts). Avoiding the inclusion of this visual cue information in the text means that readers who copy the text do not need to manually remove this from what's been copied before making use of it.

Finally, by using admonitions we not only have the visual cue but can easily make use of the distinct capabilities of the `!!!`, `???` and `???+` syntax to always display the content, start with the content collapsed but allow it to be expanded, or start with it expanded but allow it to be collapsed (respectively).

### Use `cli` admonition for commands

Use the `cli` admonition to wrap the code block in a visual cue that indicates a command:

`````markdown
???+ cli "Brief description of command"
    ```shell
    kubectl get pods
    ```
`````

Leave out any command-line prompt (`$`, `#`, etc).

???+ cli "Brief description of command"
    ```shell
    kubectl get pods
    ```

### Use `post`, `get`, `put`, `delete` admonitions for APIs

For APIs, use the distinct admonition that represents the type of operation: `post`, `get`, `put`, `delete`.

`````markdown
???+ get "GET - brief description of API call"
    ```
    {{platformURLRoot}}/open-metadata/...
    ```
`````

While the colors have been chosen to align with the Swagger documentation colors for each operation, for accessibility purposes always start the description of the API call with the operation type.

For parameters in the URL, always do the following:

- Specify the platform URL variable at the beginning, always named `{{platformURLRoot}}`
- Specify the administrative user variable as `{{adminUserId}}`
- Specify the server's name variable as `{{serverName}}`
- Specify any other parameters or variables in the URL using the double-curly-brace formatting `{{...}}`.

This ensures that the endpoint can be quickly copied into tools like Postman, and by using the same variable names consistently someone can setup their own environment definition once and make use of all the API calls they decide to copy into the tool without needing to manually make each parameter consistent.

???+ get "GET - brief description of API call"
    ```
    {{platformURLRoot}}/open-metadata/...
    ```

???+ post "POST - brief description of API call"
    ```
    {{platformURLRoot}}/open-metadata/...
    ```

???+ put "PUT - brief description of API call"
    ```
    {{platformURLRoot}}/open-metadata/...
    ```

???+ delete "DELETE - brief description of API call"
    ```
    {{platformURLRoot}}/open-metadata/...
    ```

### Use `example` admonition for file content

Use the `example` admonition to wrap a code block that represents a file's contents, and include both the type of content (`json`, etc) and the `linenums="1"` directives next to the opening triple `back-tick`. Use two spaces for indentation of lines.

`````markdown
???+ example "Name or brief description of file's purpose"
    ```json linenums="1"
    {
      "foo": "bar",
      "baz": {
      }
    }
    ```
`````

This ensures that the syntax of the file is appropriately highlighted, that line numbers are printed for ease of reference, and that the indentation is not overly-intrusive (causing horizontal scrolling within the code block to become necessary).

???+ example "Name or brief description of file's purpose"
    ```json linenums="1"
    {
      "foo": "bar",
      "baz": {
      }
    }
    ```

## Use hyphen (`-`) for unordered lists

Use a single hyphen (`-`) for unordered lists rather than a single asterisk (`*`).

This should avoid the potential for misinterpretation by the generator that a bulleted list is text that we intended (or not) to be either bolded or italicized.

## Include license header

Every Markdown document should include a license header with the CC-BY-4.0 attribute license:

!!! example "License header for documentation files"
    ```xml linenums="1"
    <!-- SPDX-License-Identifier: CC-BY-4.0 -->
    <!-- Copyright Contributors to the Egeria project. -->
    ```

## Remove license footer

The MkDocs generator automatically includes a footer at the bottom of every page on the site, which includes displaying overall copyright information and the CC-BY-4.0 license (and link). Therefore, these footers should be removed from the Markdown files themselves.

## Include abbreviations snippet

A list of abbreviations is being maintained under `snippets/abbr.md`. This snippet should therefore be included in every Markdown document to automatically highlight and provide a hover-over expansion for acronyms. Add this line, on its own, to the end of every (non-snippet) Markdown document: `--8<-- "snippets/abbr.md"`

--8<-- "snippets/abbr.md"
