<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

New releases can be created by Egeria maintainers that have the appropriate access on each GitHub repository.

Releases are published to

[Maven Central :material-dock-window:](https://oss.sonatype.org){ target=maven }
[Maven Central :material-dock-window:](https://quay.io/odpi){ target=maven }
[Maven Central :material-dock-window:](https://docker.io/odpi){ target=maven }


### Overall release policy

- Aim to release approximately every month
- Typically, target end of month for external availability
- Will only release an update between releases in exceptional circumstances
- Preserves backwards compatibility as much as possible
- Try and maintain a regular heartbeat: even if completion of some features continues in a subsequent release
- `master` / `main` kept open for new code features
- When the core Egeria is released, we have found it useful to create releases of other Egeria repositories (connector and user interface repositories) using the same version numbers as core Egeria. 
- Egeria charts are produced for each release of core Egeria; these charts include compatible user interface and connector content.    


[Release notes are available as part of the online documentation](/release-notes/overview).

### Releases for different repositories 

The Egeria project is split across different git repositories, so that each repository can be built independently and can have its own community.
Here are the release processes for Egeria repositories:

[Egeria core Release process](docs/guides/contributor/release-process/egeria-core-release.md)
[Egeria React UI Release process](docs/guides/contributor/release-process/egeria-react-ui-release.md)
[Egeria charts Release process](docs/guides/contributor/release-process/egeria-charts-release.md)

TODO - other Git repositories

--8<-- "snippets/abbr.md"
