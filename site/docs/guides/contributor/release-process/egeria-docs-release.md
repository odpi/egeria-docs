<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->
### Update the Release guide

[Release notes](/release-notes/overview) are available as part of the online documentation. In order to update these release notes,
you should

??? success "1. Agree schedule"
    - Agree on appropriate dates for branching given expected duration for testing, vacation / public holidays
        - Typically, allow 2-4 days between branching and availability
        - Communicate with team on regular calls, and via #egeria-github on Slack
        - In the last week before branching discuss holding off on any big changes in master that could destabilize the codebase
??? success "2. Track remaining issues and PRs"
    - Ensure any required issues / PRs for the release have the correct milestone set
        - Move any issues / PRs not expected to make / not required for the release to a future milestone
        - Aim to branch when most issues / PRs are complete to minimize back-porting from master, but not at the expense of impacting ongoing master development
        - Agree final branch date / criteria
??? success "3. change the release guide content"
    * make a new link for the new release and point to a new page for example [https://egeria-project.org/release-notes/3-5/](https://egeria-project.org/release-notes/3-5/)
    * Copy the latest content to the new release page
    * Ensure that the [Latest Release Notes](https://egeria-project.org/release-notes/latest/) are updated
    * Ensure the [Next Release Notes](/release-notes/overview/next) is updated
!!! success "4. test locally"
!!! success "5. merge changes"

### Tell the community the release has been made

Post a slack update on the egeria-announce channel to tell the community. For example :

`Egeria 3.5 has been released
Available via :
Source: git  https://github.com/odpi/egeria/releases/tag/V3.5
Maven artifacts: Maven Central (via maven/gradle) (may take a few hours to mirror)
Container images - https://quay.io/repository/odpi/egeria?tab=tags (no pull request limits) & https://hub.docker.com/r/odpi/egeria (includes arm64)
k8s Helm Chart repository https://github.com/odpi/egeria-charts (now supports arm64)
Release notes at https://odpi.github.io/egeria-docs/release-notes/3-5/
A full list of changes can be found at https://github.com/odpi/egeria/compare/V3.4...V3.5 (edited)

Open metadata and governance for enterprises - automatically capturing, managing and exchanging metadata between tools and platforms, no matter the vendor
`
--8<-- "snippets/abbr.md"
