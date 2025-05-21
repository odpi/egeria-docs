<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Egeria Core Release process

#### Obtaining releases / artifacts for Core Egeria
| Location                                                                                                                       | Usage                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Maven Central core Egeria release :material-dock-window:](https://mvnrepository.com/artifact/org.odpi.egeria){ target=maven } | typically used by other developers integrating with our code                                                                                                       |
| [Github core Egeria Release :material-github:](https://github.com/odpi/egeria/releases){ target=gh }                           | source code in `zip` and `tar.gz` formats                                                                                                                          |
| `git`                                                                                                                          | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped)                                                                  |
| [Container images :material-dock-window:](https://quay.io/odpi){ target=quay }                                                 | Ready to run container images for egeria platform & supporting tasks. Can use directly, and also used from our [Helm charts](/guides/operations/kubernetes/charts) |

### Core Egeria Release process

Open up an issue in core egeria using the 'release' template. This contains check boxes for the activities that should be performed.

Release names follow the V.R pattern typically ie 2.8, 3.10, 4.0.

If an urgent release is required with, for example, a critical security fix, then we may ship a V.R.M release it 2.8.1, 3.10.1, 3.10.2. The overall process is similar but refer to point 8 for more detail.

??? success "1. Agree schedule"
     - Agree on appropriate dates for branching given expected duration for testing, vacation / public holidays
         - Typically, allow 2-4 days between branching and availability
         - Communicate with team on regular calls, and via #egeria-github on Slack
         - In the last week before branching discuss holding off on any big changes in main that could destabilize the codebase
??? success "2. Track remaining issues and PRs"
    - Ensure any required issues / PRs for the release have the correct milestone set
        - Move any issues / PRs not expected to make / not required for the release to a future milestone
        - Aim to branch when most issues / PRs are complete to minimize back-porting from main, but not at the expense of impacting ongoing main development
        - Agree final branch date / criteria
??? success "3. Create branch"

    - Clone egeria into a new directory:

        - `mkdir egeria-release-x.y`
        - `git clone https://github.com/USER/egeria.git`
        - `cd egeria`
        - `git remote add upstream https://github.com/odpi/egeria.git`
       
    - Checkout main `git checkout main`
    - Ensure local update `git pull upstream main`
    - Create branch `git branch egeria-release-x.y`
    - Push to upstream `git push upstream egeria-release-x.y`
    - after this check my main **REALLY IS** the same as upstream with `git reset --hard upstream/main` (noting that this could override any local changes)

??? success "4. Update main from `x.y-SNAPSHOT` to `x.z-SNAPSHOT`"
    - `git checkout main`
    - `git pull upstream main`
    - Edit all files (command line or IDE) to replace `x.y-SNAPSHOT` with the next version, e.g. change `1.3-SNAPSHOT` to `1.4-SNAPSHOT`. Most of the changes are in gradle files, however some code and documentation also has references to our versions and all need modifying.
    - If using an IDE like IntelliJ, make sure you have all hits by searching again as [by default only a limited number of hits are shown :material-dock-window:](https://youtrack.jetbrains.com/issue/IDEA-157855){ target=intellij }.
    - Create new java class for new release and ensure all type changes in [OpenMetadataArchive](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-metadata-types) are moved to this new file.
    - Commit
    - Create a PR, have reviewed / approved and merged as usual - aim to do this as quickly as reasonable so that there is no potential for version clash

??? success "5. Test, merge any remaining required changes into branch"
    - Run appropriate tests for the release. For example, in addition to automated tests: check notebooks, run the CTS and check for compliance, check the user interface.
    - Raise issues for any changes required as usual
    - Note that approval is required for changes going into a release branch
    - PR builds are run as usual; however, merge builds, Sonar, etc do not run
    - To backport changes from `main`, first wait until the PR is merged into `main`, then use `git cherrypick -s <commithash>` to apply to `egeria-release-x.y`, then push as usual.
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
    - Fill in the release notes using a title of `Release x.y`. Select the option to include automated release notes. The content will need to be trimmed by deleting from the top to the point where the release being worked on appears ie for release 3.8, look for the update to 3.8-SNAPSHOT and cut up until that point.
    - Contact the release lead (Mandy Chessell) to release the updated maven artifacts (this copies them from the staging repository on oss.sonatype.org to the release repository, which is what is picked up via maven central search)
    - Artifacts will be available on Maven Central within minutes, but may take a few hours to appear in searches.
    - Source archives will be added to the release on GitHub.
    - this step will also create and publish container images to quay.io and docker.io .

??? amendments "8. Make amendments to the release"
    - The following instructions are the github amendments you need to make for point release x.y.z. 
    - Changes should occur on the x.y release branch. For example if it's intended to ship release 3.10.1 with an urgent security fix, we work with the egeria-release-3.10 branch.
    - update the project version ie 3.10.1-SNAPSHOT or similar. 
    - On main issue `git log` and note the commit id `<cid>` that you want to put into the branch
    - Set your local git to the release using `git reset --hard upstream/egeria-release-x.y` 
    - Create a local branch  `git checkout local1`
    - Apply the commit you need `git cherry-pick  -s <cid>` 
    - Commit the change `git commit -s -m"descriptive message"`
    - Push the change `git push`
    - In the github ui, create pr as usual but specify the release as the target.
    - [Create the GitHub release :material-github:](https://github.com/odpi/egeria/releases){ target=gh }. Use `Vx.y.z` as the tag, and ensure the correct branch is set for the target, i.e. `egeria-release-x.y`
    - Fill in the release notes using a title of `Release x.y.z`. Select the option to include automated release notes. 
    - Contact the release lead to move the artifacts from the maven staging repository to final release as in 7. above

??? success "9. Release notes in egeria-docs"
    - In addition to the automated release notes above, update the release
      notes published on the egeria-docs website.
    - Refer to the files at https://github.com/odpi/egeria-docs/tree/main/site/docs/release-notes
    - Create a new file for the release you are working on ie '3-9.md' where the '.' for the version is replaced by a hyphen '-'
    - Add the new release to mkdocs.yml (for the left navigation bar)
    - update 'latest.md' and 'next.md' to point to the current/next release accordingly
    - List known issues, breaking changes, major enhancements in this release (refer to previous release notes for examples)


--8<-- "snippets/abbr.md"
