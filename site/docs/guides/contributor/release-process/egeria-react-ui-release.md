<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Egeria Ecosystem UI (React UI) Release process

#### Obtaining releases / artifacts for  Ecosystem User Interface (Egeria React UI)

| Location | Usage |
|---|---|
| [Maven Central Egeria React UI Release:material-dock-window:](https://mvnrepository.com/artifact/org.odpi.egeria-react-ui){ target=maven } | typically used by other developers integrating with our code |
| [Github Egeria React UI Release :material-github:](https://github.com/odpi/egeria-react-ui/releases){ target=gh } | source code in `zip` and `tar.gz` formats |
| `git` | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |
| `git` | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |


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
??? success "3. Check for vulnerabilities"
     - issue npm audit on cra-client and cra-server, and decide if you want to update any of the packages.
     - update the security docs in the docs folder if you change any packages
??? success "4. Create branch"
    - Checkout main `git checkout main`
    - Ensure local update `git pull upstream main`
    - Create branch `git branch release-x.y`
    - Push to upstream `git push upstream release-x.y`

??? success "5. Update main from `x.y-rc` to `x.z-rc`"
    - `git checkout main`
    - `git checkout -b localbranch` 
    - `git pull upstream main`
    - Edit cra-client/package.json `x.y-rc` with the next version `x.z-rc`, e.g. change `3.1-rc` to `3.2-rc`.
    - Edit cra-server/package.json `x.y-rc` with the next version `x.z-rc`, e.g. change `3.1-rc` to `3.2-rc`.
    - `git add .`
    - `git commit -s -m"git..."`
    - Create a PR, have reviewed / approved and merged as usual - aim to do this as quickly as reasonable so that there is no potential for version clash

??? success "6. Test, merge any remaining required changes into branch"
    - Run appropriate tests for the release. Run each of the parts of the UI to ensure they return results (TODO more details required).
    - Raise issues for any changes required as usual
    - Note that approval is required for changes going into a release branch
    - PR builds are run as usual; however, merge builds, Sonar, etc do not run
    - To backport changes from `main`, first wait until the PR is merged into `main`, then use `git cherrypick -s <commithash>` to apply to `release-x.y`, then push as usual.
    - In some cases a merge commit will need to be made using `git cherrypick -s -m 1 <commithash>`
    - If code has diverged significantly a manual recode may be easiest

??? success "7. Update branch's release version from `x.y-rc` to `x.y`"
    - 'git reset --hard upstream/release-x.z'   (the newly create remote branch)
    - Edit cra-client/package.json `x.y-rc` with the next version `x.y`, e.g. change `3.2-rc` to `3.2`.
    - Edit cra-server/package.json `x.y-rc` with the next version `x.y`, e.g. change `3.2-rc` to `3.2`.
    - 'git checkout -b localbranch'
    - 'git add .'
    - 'git commit -s -m"..."'
    - 'git remote remove upstream'
    - 'git remote add upstream https://github.com/odpi/egeria-react-ui -t release-x.z'
    - 'git push upstream'        
    - in the github ui, create a pr but change the target from 'main' to release-x.z'
    - check that the changes are as expected and merge.
    - 'git remote remove upstream'
    - 'git remote add upstream https://github.com/odpi/egeria-react-ui'
    - 'git fetch upstream'
    - 'git reset --hard upstream/main'

??? success "8. Create a release in GitHub"
    - [Create the GitHub release :material-github:](https://github.com/odpi/egeria-react-ui/releases){ target=gh }. Use `Vx.y` as the tag, and ensure the correct branch is set for the target, i.e. `egeria-release-x.y`
    - Fill in the release notes using a title of `Release x.y` and [copy the notes from the appropriate release notes](/release-notes/overview)
    - Artifacts will be available on Maven Central within around half a day.
    - Source archives will be added to the release on GitHub within an hour or so.


--8<-- "snippets/abbr.md"
