<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Egeria Core Release process

#### Obtaining releases / artifacts for Core Egeria
| Location | Usage |
|---|---|
| [Maven Central core Egeria release :material-dock-window:](https://mvnrepository.com/artifact/org.odpi.egeria){ target=maven } | typically used by other developers integrating with our code |
| [Github core Egeria Release :material-github:](https://github.com/odpi/egeria/releases){ target=gh } | source code in `zip` and `tar.gz` formats |
| `git` | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |

### Core Egeria Release process

Open up an issue in core egeria using the 'release' template. This contains check boxes for the activities that should be performed

??? success "1. Agree schedule"
    --8<-- "docs/guides/contributor/release-steps/agree-schedule.md"
??? success "2. Track remaining issues and PRs"
    --8<-- "docs/guides/contributor/release-steps/track-outstanding.md"
??? success "3. Create branch"
    - Checkout master `git checkout master`
    - Ensure local update `git pull upstream master`
    - Create branch `git branch egeria-release-x.y`
    - Push to upstream `git push upstream egeria-release-x.y`
    - after this check my master **REALLY IS** the same as upstream with `git reset --hard upstream/master` (noting that this could override any local changes)

??? success "4. Update master from `x.y-SNAPSHOT` to `x.z-SNAPSHOT`"
    - `git checkout master`
    - `git pull upstream master`
    - Edit all files (command line or IDE) to replace `x.y-SNAPSHOT` with the next version, e.g. change `1.3-SNAPSHOT` to `1.4-SNAPSHOT`. Most of the changes are in `pom.xml` or gradle files, however some code and documentation also has references to our versions and all need modifying.
    - If using an IDE like IntelliJ, make sure you have all hits by searching again as [by default only a limited number of hits are shown :material-dock-window:](https://youtrack.jetbrains.com/issue/IDEA-157855){ target=intellij }.
    - Commit
    - Create a PR, have reviewed / approved and merged as usual - aim to do this as quickly as reasonable so that there is no potential for version clash

??? success "5. Test, merge any remaining required changes into branch"
    - Run appropriate tests for the release. For example, in addition to automated tests: check notebooks, run the CTS and check for compliance, check the user interface.
    - Raise issues for any changes required as usual
    - Note that approval is required for changes going into a release branch
    - PR builds are run as usual; however, merge builds, Sonar, etc do not run
    - To backport changes from `master`, first wait until the PR is merged into `master`, then use `git cherrypick -s <commithash>` to apply to `egeria-release-x.y`, then push as usual.
    - In some cases a merge commit will need to be made using `git cherrypick -s -m 1 <commithash>`
    - If code has diverged significantly a manual recode may be easiest

??? success "6. Update branch's release version from `x.y-SNAPSHOT` to `x.y`"
    - Aim to make this change when the code appears to be ready to ship apart from final tests in order to avoid version confusion
    - `git checkout egeria-release-x.y`
    - `git pull upstream egeria-release-x.y`
    - Edit all files (command line or IDE) to replace `x.y-SNAPSHOT` with `x.y`, i.e. removing the `-SNAPSHOT` designation. Most of the changes are in `pom.xml` files; however, some code and documentation also has references to our versions and all need modifying.
    - Commit, and do not make any other changes.
    - Create a PR, have reviewed / approved and merged as usual

??? success "7. Create a release in GitHub"
    - [Create the GitHub release :material-github:](https://github.com/odpi/egeria/releases){ target=gh }. Use `Vx.y` as the tag, and ensure the correct branch is set for the target, i.e. `egeria-release-x.y`
    - Fill in the release notes using a title of `Release x.y` and [copy the notes from the appropriate release notes](/release-notes/overview)
    - Artifacts will be available on Maven Central within around half a day.
    - Source archives will be added to the release on GitHub.

--8<-- "snippets/abbr.md"
