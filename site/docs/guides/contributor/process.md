<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Way of Working

## Issues

Egeria uses [GitHub issues :material-dock-window:](https://help.github.com/en/github/managing-your-work-on-github/managing-your-work-with-issues){ target=gh }.

### Opening issues

Issues can be opened by any GitHub user, and are used for a variety of purposes:

- Problems getting Egeria working
- Proposed new features
- Identification of a bug
- Suggested process change
- Or really anything that affects Egeria

All PRs should have an associated issue to facilitate discussion. You should include a helpful abstract and as many notes as possible about what you see, what you've tried, your environment, any logs, what you expected to happen, etc.

### Triaging new issues

New issues are triaged by [maintainers](/guides/project-operations/#maintainers), who will:

- Assign the issue to someone who can take care of what is reported - even if not the final owner
- Assign a milestone if it is immediately obvious that the issue relates to capability set out in a release plan, or is needed very soon, otherwise leave blank
- Assign relevant tags to the issue

### Working on issues

The issue owner (assignee) will then:

- Update the issue as soon as possible with an initial response
- When raising a PR, refer to the issue number (e.g. `#1234`) so that the discussion is clearly linked with the proposed code change. Use `Fixes #1234` if this PR will completely address the issue, so that GitHub will automatically close the issue when the PR is merged.
- Keep the milestone realistic, if set
- Regularly review outstanding issues and update, reassign, close as needed

### Closing issues

- Issues with PRs marked as `fixes #1234` will close automatically when the PR is merged
- Other issues fixed in other ways should be closed manually
- Any issues open after 60 days with no activity (including assignments) will have a comment added saying they will be closed
- 20 days later the issue will be closed
- If an issue is closed accidentally or prematurely, reopen and add appropriate comments

## Release process
Follow [these steps]("docs/guides/contributor/release-process/index.md") to create a new Egeria release for each Egeria repository.


## Security hardening

As part of developing Egeria, we will inevitably come across areas identified by various code analysis tools as potential security vulnerabilities. The following guidelines define the way we will work with these (identifying, reporting, tracking, etc) as well as some common techniques we can apply to address them.

The maintainers have a weekly call to triage identified vulnerabilities from various sources:

- [Sonar scans :material-dock-window:](https://sonarcloud.io/organizations/odpi/projects){ target=security }
- [Nexus IQ scans :material-dock-window:](https://nexus-iq.wl.linuxfoundation.org){ target=security }
- Any third party inputs (i.e. from consumers) -- which can be sent to us at [egeria-security@lists.lfaidata.foundation](mailto:egeria-security@lists.lfaidata.foundation)

Work can then begin on resolving them, with two potential options (depending on complexity):

- Quick to resolve: create an issue when we believe we have a fix, and link the PR with the fix to the issue
- For any we cannot quickly resolve, we will use [GitHub's security advisories :material-github:](https://github.com/odpi/egeria/security/advisories){ target=gh } to capture the details and notify publicly about the potential vulnerability

In general, any vulnerabilities will typically be addressed through one of the following techniques:

### Code changes

When the code identified as having a potential vulnerability is our own, we should naturally investigate how to change our code in order to reduce or remove the impact or likelihood of that exposure. This could be through applying input or output validation of data we receive, or ensuring that we use features built-in to any external components to do such processing.

### Dependency exclusions

External modules on which we depend often have their own set of embedded dependencies. Some of these transitive dependencies may have vulnerabilities, and we may not actually use any of the functionality they provide.

In these cases, we can (and should) safely exclude these transitive dependencies as part of the POM dependency
management.

!!! example "Example: excluding a transitive dependency from a dependent library"
    For example, `testng` has a dependency on the `snakeyaml` library, but this is only used when configuring `testng` with YAML documents (which we do not do). We can therefore safely exclude the transitive `snakeyaml` dependency of `testng` using the following in the root-level `pom.xml`:

    ```xml linenums="1"
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <scope>test</scope>
        <version>7.1.0</version>
        <exclusions>
        <!-- Exclude snakeyaml, which has open CVEs and is unused -->
            <exclusion>
                <groupId>org.yaml</groupId>
                <artifactId>snakeyaml</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
    ```

### Forced dependency version updates

In other cases we actually do rely on the functionality provided by these transitive dependencies, so we cannot simply exclude them. However, it may be possible to force the version of these dependencies to be updated so that a vulnerable older version of the dependency (the minimal version on which the library depends) is not used by default.

!!! example "Example: forcing an updated version of a transitive dependency"
    Take for example `janusgraph` -- it has a transitive dependency on the `sleepycat` library, and by default quite an old version which has some known problems. By adding an explicit dependency for a newer version of the `sleepycat` module we can force this newer version to be used by `janusgraph` as well.

    ```xml
    <dependency>
        <groupId>com.sleepycat</groupId>
        <artifactId>je</artifactId>
        <version>18.3.12</version>
    </dependency>
    ```

Of course making this change requires testing, to ensure that the newer version of the transitive library is still compatible with the base dependency.

## Feature branches

The standard development approach for Egeria is to:

- make code changes on a branch on one's own fork
- create a PR to push from this branch to master

Most of the time these are coded by a single developer, with additional review / testing from peers as part of the PR process. On occasion a few developers may directly collaborate on the code changes and can pull / push to / from each other's branches, or share updates in other ways.

`master` therefore always represents the "best so far" code, ideally in a "ready to release" state, through build automation, testing and peer pressure. Everyone benefits from the latest code changes and any divergence between a developer's environment and `master` is minimized.

Sometimes, however, there is a need to coordinate a larger piece of work in a team of developers who need the ability to:

- Reduce the impact of changes on master - i.e. for everyone else
- Reduce the impact of constant updates from master, in order to have a stable environment for feature-oriented testing

In these cases a *feature branch* may be proposed. A GitHub issue should be created, and the proposal discussed in one of the regular Egeria calls to build consensus around the need for such a branch.

!!! attention "Feature branches add overhead"
    They can lead to code divergence and complexity, and they will only be created in compelling circumstances for long-running feature work.

Once agreed, one of the maintainers / admins will make the required setup. See the last section of this document for some more information on this.

### Working in a feature branch

Any work specifically and solely for the feature should be done on the agreed branch, but it's important that normal defect fixes and enhancements to unrelated features should continue to be worked on via `master`: i.e. working on a dev's own fork for a short period (hours/days) and merged back to `master`.

This helps other developers working on the project, and reduces the complexity of subsequent merges from the feature branch.

The team working on the feature will need to arrange / agree their own builds for testing / deployment.

### Merging to master and releasing

We do not release from a feature branch. All release branches are made from `master`.

It is the feature team's responsibility to:

- Merge the latest code from `master`
- Merge feature branch back to `master`

There's no set schedule for this. Longer intervals offers the feature more stability, but can rapidly build up a much more complex merge scenario which the feature team will need to resolve.

It is the feature team's responsibility to respond to any issues in `master`, and to validate that the feature is "good".

### Administrative tasks

These tasks should only be performed by someone familiar with the process and with appropriate authority after establishing team agreement. As such, exact commands are not given below:

??? success "Creating a branch"
    - Create a feature branch named `feature-XXX` where `XXX` is a descriptive name for the feature. (With issues, using the issue number can be helpful, but since we expect a small number of feature branches, this seems clearer.)
    - Ensure branch protections are set to the same as `master`, to ensure all changes follow the same process as for master: for example, must go via PRs.

??? success "Builds"
    It's expected that all Feature branches should have PR verification to ensure submitted code changes in a PR do not break the main build. This is purely a compilation test to check against breakage. Build artifacts are not distributed or saved.

    Features could benefit from a 'merge' build which ensures the latest code in the branch works well together. This build also typically generates:
    - Maven artifacts (to a snapshot repository)
    - Docker images (to Docker Hub)

    In the future, it's expected these will get used for automatic tests, and used by other deployment approaches such as Docker Compose and Kubernetes.

    However, currently our repository and naming / versioning setup is not able to do this since branch names are not taken into account.

In Egeria we also may perform:

- Scans for code quality
- Scans for licensing
- Security-related scans
- Builds for Docker images other than core Egeria

These will also not be done for a feature branch.

### Closing a feature branch

When the feature branch is no longer required, it can be deleted by an admin.

Similarly to requesting a feature branch, an issue should be raised, and team agreement sought beforehand.

--8<-- "snippets/abbr.md"
