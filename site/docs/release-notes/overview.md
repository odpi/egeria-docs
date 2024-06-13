<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Release Notes Overview

Egeria is a large and active project with teams advancing its function on multiple fronts.  Our work is split across [multiple git repositories](https://egeria-project.org/education/tutorials/git-and-git-hub-tutorial/egeria-git-repositories/) that supply components on different release schedules. Therefore, we aim to provide an update on our activities and releases in our monthly newsletter.

The [roadmap for Egeria](/release-notes/roadmap) describes the end vision for Egeria and our current status.  

!!! tip "Feedback"
    One way you can help us is to feedback on your experiences, both good and bad. We would love to hear from you!

    If you discover an issue in the release you are using, we recommend first upgrading to the latest available release. If this does not resolve the problem, please raise a new [GitHub issue :material-dock-window:](https://github.com/odpi/egeria/issues){ target=gh }.

    You can also follow our discussions by joining us on [Slack :fontawesome-brands-slack:](https://slack.lfaidata.foundation){ target=slack }.

## Core Egeria Function

The *Core Egeria* technology is located in the [egeria.git](https://github.com/odpi/egeria) repository.  It provides the [OMAG Server Platform](/concepts/omag-server-platform), java clients for the [OMAG Servers](/concepts/omag-server) that run on the OMAG Server Platform along with the [Conformance Test Suite (CTS)](/guides/cts/overview).

The project aims to produce a new release of Core Egeria about once every 6 weeks. Each release includes new features and fixes to existing function.  This is also an opportunity to update the levels of our dependencies to reduce vulnerabilities.

The table below shows the planned dates for future releases.  The branch date is the date that a copy of the main branch is taken.  This copy is the candidate code for the release.  We then run tests on this copy and release to maven central once any issues have been resolved.  Any fixes that are necessary are made to the main branch and then back-ported to the release branch.  It typically takes a week to go from making the release branch to the new release going to maven central.

| Release | Branch date        | Release Date        | Core theme           |
|---------|--------------------|---------------------|----------------------|
| 4.2     | 17th July 2023     | 20th July 2023      | Runtime optimization |
| 4.3     | 4th September 2023 | 13th September 2023 | New assemblies       |
| 5.0     | 10th June 2024     |                     | Survey Framework     |
| 5.1     | 2nd September 2024 |                     |                      |


!!! attention "Backwards compatibility"
    The team aims to provide complete backward compatibility for all components that are marked *stable*[^1].

    If backwards compatible changes are not possible, it will be called out explicitly in the release notes with an explanation on how to upgrade.

Each release will also upgrade the level of its dependencies to ensure Egeria is running with all the latest security patches. We therefore recommend that you keep moving forward with us to get the best Egeria experience possible.

Our *main* branch is currently taking code for all future releases. Many of the features are large and the teams integrate code for partial function as soon as it is stable and has no impact on released function. So you will see support for much more function than is officially released. This way you can monitor and feedback on future items as they are developed.

[^1]: To understand more about what it means to have "stable function" see [Egeria content status](content-status).

--8<-- "snippets/abbr.md"
