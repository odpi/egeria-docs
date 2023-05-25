<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Artifacts

| Location | Usage |
|---|---|
| Maven Central | [egeria-connector-resource-jdbc :material-dock-window:](https://central.sonatype.com/artifact/org.odpi.egeria/egeria-connector-resource-jdbc){target=new} |
| Maven Central | [egeria-connector-integration-jdbc :material-dock-window:](https://central.sonatype.com/artifact/org.odpi.egeria/egeria-connector-integration-jdbc){target=new} |
| [Quay.io](https://quay.io/repository/odpi/egeria-connector-jdbc?tab=tags){ target=new } | `docker pull quay.io/odpi/egeria-connector-jdbc:TAGNAME` |
| [DockerHub](https://hub.docker.com/repository/docker/odpi/egeria-connector-jdbc/tags?page=1&ordering=last_updated){ target=blank } | `docker pull odpi/egeria-connector-jdbc:TAGNAME` |
| [Github connector release :material-github:](https://github.com/odpi/egeria-connector-jdbc/releases){ target=gh } | source code in `zip` and `tar.gz` formats or via `git checkout vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |

### Release process

??? success "1. Await core Egeria release"
    Connector release are done shortly after a corresponding Egeria core release. Any other changes to the connector are simply consolidated for the tandem release alongside Egeria core -- we do not do interim releases of the connector.

??? success "2. Track remaining issues and PRs"
    Aim to branch when most issues / PRs are complete to minimize back-porting from main, but not at the expense of impacting ongoing main development

??? success "3. Create release branch"
    - Checkout main `git checkout main`
    - Ensure local update `git fetch upstream`, `git merge upstream/main` (or `git reset --hard upstream/main`), `git pull --no-rebase`
    - Create branch `git branch release-x.y`
    - Push to upstream `git push upstream release-x.y`
    - Pull upstream `git pull upstream release-x.y`

??? success "4. Update `release-x.y` from `x.y-SNAPSHOT` to `x.y`"
    - `git checkout release-x.y`
    - Edit the `build.gradle` files (command line or IDE) to replace `x.y-SNAPSHOT` with the same non-snapshot version `x.y`, e.g. change `4.0-SNAPSHOT` to `4.0`.
    - If using an IDE like IntelliJ, make sure you have all hits by searching again as [by default only a limited number of hits are shown :material-dock-window:](https://youtrack.jetbrains.com/issue/IDEA-157855){ target=intellij }.
    - Make sure you are using **stable compatible Egeria implementation version** as a dependency
    - Check if you are using latest versions for third party dependencies
    - Add the changes and commit `git commit -s`
    - Create a PR, have reviewed / approved and merged as usual - aim to do this as quickly as reasonable so that there is no potential for version clash

??? success "5. Test, merge any remaining required changes into branch"
    - Run appropriate tests for the release. For example, in addition to automated build tests:
        - Run functional and regression test
        - If applicable, run the CTS and check that all profiles are compliant 
        - If infrastructure exists, run the PTS and check that there are no unexpected performance regressions.
    - Raise issues for any changes required as usual.
        - If there are any issues, delete the `release-x.y` branch, fix in `main` branch, and repeat steps (3-4) until no remaining issues.

??? success "6. Release artifacts publishing"
    - Build and publish release version by selecting the release branch and executing [github action](https://github.com/odpi/egeria-connector-jdbc/actions/workflows/release.yml){ target=gh }.
    - Review and release artifacts as explained in the [Maven Publishing Guide](/guides/contributor/release-process/maven-publish/#reviewing-releasing-artifacts){ target=new }.
    - Check if all maven artifacts are avaiable in maven central repository (it will take some time to sync)
    - Check if new docker containers are created under the different docker repositories respectively.

??? success "7. Update `main`s release version from `x.y-SNAPSHOT` to `x.z-SNAPSHOT`"
    - `git checkout main`
    - Ensure local update `git fetch upstream`, `git merge upstream/main`, `git pull --no-rebase`
    - Edit `build.gradle` (command line or IDE) to replace `x.y-SNAPSHOT` with `x.z-SNAPSHOT`.
    - Commit, and do not make any other changes.
    - Create a PR, have reviewed / approved and merged as usual

??? success "8. Create a release in GitHub and notify the community"
    - [Create the GitHub release :material-github:](https://github.com/odpi/egeria-connector-jdbc/releases){ target=gh }. Use `vx.y` as the tag, and ensure the correct branch is set for the target, i.e. `release-x.y`
    - Fill in the release notes using a short title summarizing the primary changes in the release and in the description outline the changes across new features, bug fixes, security fixes, any repository migration required, and minimum version of Egeria against which the connector should be used
    - Source archives will be added to the release on GitHub.
    - Notify the community on Slack or email channels.
    - Optionally add entry to the monthly newsletter.

--8<-- "snippets/abbr.md"
