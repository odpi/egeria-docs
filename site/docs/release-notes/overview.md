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

The project aims to produce a new release of Core Egeria about once a month. Each release includes new features and fixes to existing function.

!!! attention "Backwards compatibility"
    The team aims to provide complete backward compatibility for all components that are officially released[^1].

    If backwards compatible changes are not possible, it will be called out explicitly in the release notes with an explanation on how to upgrade.

Each release will also upgrade the level of its dependencies to ensure Egeria is running with all the latest security patches. We therefore recommend that you keep moving forward with us to get the best Egeria experience possible.

Our *main* branch is currently taking code for all future releases. Many of the features are large and the teams integrate code for partial function as soon as it is stable and has no impact on released function. So you will see support for much more function than is officially released. This way you can monitor and feedback on future items as they are developed.

[^1]: To understand more about what it means to have "released function" see [Egeria content status](content-status).

--8<-- "snippets/abbr.md"
