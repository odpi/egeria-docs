<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

New releases can be created by Egeria maintainers that have the appropriate access on each GitHub repository.

Releases are published to

[Maven Central :material-dock-window:](https://oss.sonatype.org){ target=maven }
[Quay.io :material-dock-window:](https://quay.io/odpi){ target=maven }
[Docker.io :material-dock-window:](https://docker.io/odpi){ target=maven }


### Overall release policy

- Aim to release approximately every month
- Typically, target end of month for external availability
- Will only release an update between releases in exceptional circumstances
- Preserves backwards compatibility as much as possible
- Try and maintain a regular heartbeat: even if completion of some features continues in a subsequent release
- `main` / `main` kept open for new code features
- When the core Egeria is released, we have found it useful to create releases of other Egeria repositories (connector and user interface repositories) using the same version numbers as core Egeria. 
- Egeria charts are produced for each release of core Egeria; these charts include compatible user interface and connector content.    


### Releases for different repositories 

The Egeria project is split across different git repositories, so that each repository can be built independently and can have its own community.
Here are the release processes for Egeria repositories:


| Git repository | Description | Update process |
| ----------- | ----------- | -------------- |
| [https://github.com/odpi/egeria](https://github.com/odpi/egeria) | Egeria core | [Egeria core Release process](/guides/contributor/release-process/egeria-core-release)  |
| [https://github.com/odpi/egeria-react-ui](https://github.com/odpi/egeria-react-ui)  | Egeria React UI        | [Egeria React UI Release process](/guides/contributor/release-process/egeria-react-ui-release)| 
| [https://github.com/odpi/egeria-charts](https://github.com/odpi/egeria-charts)  | Egeria charts | [Egeria charts Release process](/guides/contributor/release-process/egeria-charts-release) |
| [https://github.com/odpi/egeria-docs](https://github.com/odpi/egeria-docs)  | Release guide | [Egeria Update Release Guide process](/guides/contributor/release-process/egeria-charts-release) |
| [https://github.com/odpi/egeria-connector-xtdb](https://github.com/odpi/egeria-connector-xtdb)  | XTDB connector | [XTDB connector release process](/guides/contributor/release-process/egeria-connector-xtdb-release) |
| TODO | Other Egeria Git repositories | TODO |




--8<-- "snippets/abbr.md"
