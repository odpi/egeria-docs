<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Style Guide

The style guidelines exist to keep the documentation clear and understandable.

## Choose the right title

Use a short, keyword-rich title that captures the intent of the document and draws the reader in. Ensure that the title clearly and concisely conveys the content or subject matter and is meaningful to a global audience.

The text for the title of the document must use title case. Capitalize the first letter of every word except conjunctions and prepositions.

| Do | Don't |
|---|---|
| `# Security Architecture` | `# Security architecture` |
| `# Code of Conduct` | `# Code Of Conduct` |

## Use sentence case for headings

Use sentence case for the headings in your document. Only capitalize the first word of the heading, except for proper nouns or acronyms.

| Do | Don't |
|---|---|
| Configuring rate limits | Configuring Rate Limits |
| Using Envoy for ingress | Using envoy for ingress |
| Using HTTPS | Using https |

## Use present tense

| Do | Don't |
|---|---|
| This command starts a proxy. | This command will start a proxy. |

!!! attention "Exception"
    Use future or past tense if it is required to convey the correct meaning. This exception is extremely rare and should be avoided.

## Use active voice

| Do | Don't |
|---|---|
| You can explore the API using a browser. | The API can be explored using a browser. |
| The YAML file specifies the replica count. | The replica count is specified in the YAML file. |

## Use simple and direct language

Use simple and direct language. Avoid using unnecessary phrases, such as saying "please."

| Do | Don't |
|---|---|
| To create a `ReplicaSet`, ... | In order to create a `ReplicaSet`, ... |
| See the configuration file. | Please see the configuration file. |
| View the Pods. | With this next command, we'll view the Pods. |

## Prefer shorter words over longer alternatives

| Do | Don't |
|---|---|
| This tool helps scaling up pods. | This tool facilitates scaling up pods. |
| Pilot uses the `purpose` field to ... | Pilot utilizes the `purpose` field to ... |

## Address the reader as "you"

| Do | Don't |
|---|---|
| You can create a `Deployment` by ... | We'll create a `Deployment` by ... |
| In the preceding output, you can see... | In the preceding output, we can see ... |

## Avoid using "we"

Using "we" in a sentence can be confusing, because the reader might not know whether they're part of the "we" you're describing.

| Do | Don't |
|---|---|
| Version 1.4 includes ... | In version 1.4, we have added ... |
| Egeria provides a new feature for ... | We provide a new feature ... |
| This page teaches you how to use pods. | In this page, we are going to learn about pods. |

## Avoid jargon and idioms

Some readers speak English as a second language. Avoid jargon and idioms to help make their understanding easier.

| Do | Don't |
|---|---|
| Internally, ... | Under the hood, ... |
| Create a new cluster. | Turn up a new cluster. |
| Initially, ... | Out of the box, ... |

## Avoid statements that will soon be out of date

Avoid using wording that becomes outdated quickly like "currently" and "new". A feature that is new today is not new for long.

| Do | Don't |
|---|---|
| In version 1.4, ... | In the current version, ... |
| The Federation feature provides ... | The new Federation feature provides ... |

## Create useful links

Don't use *here*, *click here* or URLs as the text for a hyperlink.

| Do | Don't |
|---|---|
| ... in a [metadata server](https://example.com) you can ... | ... in a metadata server, which you can read more about [here](https://example.com). |
| The [metadata access point](https://example.com) ... | [Read more](https://example.com) about metadata access points ... |
| The [`FooBar` :material-github:](https://example.com) class ... | The `FooBar` class ([https://example.com/somewhere/something/FooBar.java](https://example.com)) ... |

There are numerous [articles explaining what makes a good hyperlink :material-dock-window:](https://medium.com/@heyoka/dont-use-click-here-f32f445d1021){ target=medium }, but fundamentally the *"Don't"* examples above:

1. Decrease the overall usability of links.
2. Decrease the overall accessibility of the links.
3. Decrease search engine performance and content find-ability.

--8<-- "snippets/abbr.md"
