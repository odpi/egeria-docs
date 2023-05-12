<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Coding Guidelines

Egeria provides technology for an open standard that seeks to improve the processing and protection of data across organizations. For its developers, this carries the benefit that their work receives high recognition, but also additional responsibilities to ensure its wide applicability and longevity.

For example, Egeria seeks a broad audience - from developers to adopting vendors to consuming users. Building this audience and allowing the community to scale requires clarity in the way the software is written, documented, packaged and used. Many of the guidelines seek to make it easier for someone new to pick up the software, at the expense of maybe a little more work, or a little less freedom of action for the original developer.

As such, these guidelines exist to remind us of these broader responsibilities.

## Build environment

The core of Egeria is written primarily in [Java](/guides/developer/languages/#java), and the minimum level required to build and run it is 17.

Most developers use MacOS, while our official builds use Linux (Ubuntu/Centos/RHEL should all be fine).

!!! attention "Windows is unsupported"
    The traditional Windows environment is not directly supported. It is recommended to use [WSL2 :material-dock-window:](https://docs.microsoft.com/en-us/windows/wsl/){ target=ms } which offers a full Linux environment.

[Gradle](https://gradle.org/) is used to control the builds, and is automatically downloaded when needed. (see [gradle wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html))

IDEs can make navigating the Egeria code easier. Each IDE can vary a lot. Many of the Egeria community use [JetBrains IntelliJ](/education/tutorials/intellij-tutorial/overview) for the core Egeria project, which is very large. Smaller projects, and non-java projects also will work well with [Microsoft Visual Code](https://code.visualstudio.com/).

In the case of problems the first problem determination step is to check you can build Egeria normally at the command line i.e. `./gradlew build` from the source root. That will prove at least Java and Gradle are correct.

!!! tip "Set `JAVA_HOME`"
    We have also noticed that you need to ensure `JAVA_HOME` is set or the build will fail running Javadoc.

## Eliminate any build warnings

Build output should be checked for any warnings, i.e. `[WARNING]`, and these should be eliminated.

The Java compiler is set to use `-Xlint:all` and may report warnings about deprecated function, unsafe casts, unchecked conversions, and so on -- all of which should be addressed.

Other tools used in the build may also result in warnings which should also be addressed, whilst test cases should ensure output is captured to avoid such warnings appear in the build logs.

## Include license in every file

All files for Egeria should have a license included. We use the [SPDX :material-dock-window:](https://spdx.org/ids){ target=spdx } encoding to keep the headers simple.

!!! example "License header for documentation (`.md`)"
    ```xml linenums="1"
    <!-- SPDX-License-Identifier: CC-BY-4.0 -->
    <!-- Copyright Contributors to the Egeria project. -->
    ```

    Note that we no longer need to include an explicit footer in documentation files, as this is already included in the overall documentation site as the footer of every page.

!!! example "License header for XML files (`.xml`)"
    ```xml linenums="1"
    <?xml version="1.0" encoding="UTF-8"?>
    <!-- SPDX-License-Identifier: Apache-2.0 -->
    <!-- Copyright Contributors to the Egeria project.  -->
    ```

!!! example "License header for Java code (`.java`)"
    ```java linenums="1"
    /* SPDX-License-Identifier: Apache-2.0 */
    /* Copyright Contributors to the Egeria project. */
    ```

## Document

Although all code for Egeria should be clear and easy to read, the code itself can only describe *what* it is doing: it can rarely describe *why* it is doing it. Also, the Egeria codebase is quite large and hard to digest in one go. Having summaries of its behavior and philosophy helps people to understand its capability faster.

### `README.md`

Each directory (apart from Java packages) should have a `README.md` file that describes the content of the directory. These files are displayed automatically by GitHub when the directory is accessed and this helps someone to understand the structure while navigating through the directories.

The exception is that directories representing Java packages do not need README files because they are covered by Javadoc.

### Javadoc

[Javadoc :material-dock-window:](https://docs.oracle.com/en/java/javase/17/javadoc/javadoc.html){ target=java } is used to build a code reference for [our public site](https://odpi.github.io/egeria/index.html). It is generated as part of the build.  There are three places where Javadoc should be provided by the developer of Java code:

- Every Java source file should begin with a header Javadoc tag just before the start of the class/interface/enum, which explains the purpose and responsibilities of the code.
- All public methods should have a clear Javadoc header describing the purpose, parameters and results (including exceptions). This includes test cases.
- Each Java package should include a `package-info.java` file describing the purpose of the package and its content.

Java code files may have additional comments, particularly where the processing is complex. The most useful comments are those that describe the purpose, or intent of the code, rather than a description of what each line of code is doing.

The output from a build should be checked to ensure there are no Javadoc warnings: for example about undocumented parameters or exceptions.

Javadoc is published as part of each published artifact, which allows IDEs to show the documentation automatically. It is also published to an [Egeria javadoc website](https://odpi.github.io/egeria/index.html) as part of the build process.

## Log through ALF

Egeria will typically be embedded in complex deployment environments. This means that we cannot rely on standard developer logging provided by components such as SLF4J. Instead, we use [First Failure Data Capture (FFDC)](/services/common/ffdc-services) through the [Audit Log Framework (ALF)](/frameworks/alf/overview).

## Be consistent with style and layout

There are many coding and layout styles that provide clear and readable code. Developers can choose the layout they prefer but with the following restrictions / suggestions:

- Try to use full words rather than abbreviations or shortened versions of a word for names such as class names, method names and variable names. Cryptic names create more effort for the reader to follow the code.
- Use the same style throughout a file.
- If changing an existing file, use the same style and layout as the original developer. Do **not** impose your own style in the middle of the code since the inconsistency that you introduce makes the whole file harder to read. It should not be possible to see where you have made the changes once the code is committed into git.
- For Java unit tests use `/src/test/java` folder of the module (standard Maven location), and postfix Java file names for tests with the word `Test`.

### Dates and times

In Egeria, date / time instants are always represented as Unix Epoch time with millisecond precision (milliseconds elapsed since January 1, 1970).

- The Egeria [OMRS](/services/omrs) layer handles date / time as either `java.lang.Long` or as `java.util.Date` objects. It does not store localised versions of the date / time.
- In other Egeria APIs that might be developed, it is **strongly recommended** to store dates and times as a Long or Date.
- In addition, it is possible to expose localised date representations if required.

## Write tests

Egeria is an integration technology which means that it uses a comprehensive multi-level approach to testing.

Modules include unit tests. These unit tests should focus on simple validation of Java beans, utilities and code that can easily be tested in isolation. The unit tests run as part of the build and a pull request
cannot be incorporated into main if any unit tests are failing. They should not significantly extend the time of the build since this impacts all the contributors' productivity. Our preferred Java frameworks for unit testing are [JUnit5 :material-dock-window:](http://junit.org){ target=test }, [TestNG :material-dock-window:](http://testng.org){ target=test } and [Mockito :material-dock-window:](http://mockito.org){ target=test }.

External APIs (typically they include both a client and a server component) are tested using functional verification tests (FVTs). These are located in the [open-metadata-test/open-metadata-fvt :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-test/open-metadata-fvt) module. The aim of these tests is to check that the APIs validate all of their parameters and function correctly in a single server environment. These tests also operate as part of the build but are not run as part of the PR process. Modules should ensure they include some FVTs as they move [from development to technical preview](/release-notes/content-status). By the time the module is moving to released function, the FVTs should be able to validate that this function is stable and correct.

Some connectors are tested via the [Conformance Test Suite](/guides/cts/overview). If you deliver a connector that is covered by this test suite, you should run the tests before merging changes into main. The conformance test suite is also run as part of the release process.

Egeria's [hands on labs](/education/open-metadata-labs) provide a complex multi-server environment and are typically used by contributors to verify that their changes have not regressed any of the
basic function.

We are also interested in building out a comprehensive integration test to allow automated complex multi-server scenarios that can be running continuously.

## Sign-off commits to accept DCO

We have tried to make it as easy as possible to make contributions. This applies to how we handle the legal aspects of contribution.

We simply ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message. This is the same approach that the [Linux® Kernel community :material-dock-window:](http://elinux.org/Developer_Certificate_Of_Origin){ target=dco } uses to manage code contributions.

Here is an example `Signed-off-by` line, which indicates that the submitter accepts the DCO:

```
Signed-off-by: John Doe <john.doe@hisdomain.com>
```

You can include this automatically when you commit a change to your local git repository using:

!!! cli "Include DCO automatically when committing changes"
    ```bash
    $ git commit -s
    ```

By signing your work, you are confirming that the origin of the content makes it suitable to add to this project. See [Developer Certificate of Origin (DCO) :material-dock-window:](https://developercertificate.org/){ target=dco }.

## Review code changes

If you are asked to review a code change it will be located in a pull request (PR) on one of [Egeria's git repositories :material-github:](https://github.com/odpi?q=egeria&type=&language=&sort=){ target=gh }.

Within the pull requests are a number of commits that describe the changes to particular files that will be made when the pull request is merged into the repository.

As a reviewer, you need to look at the code changes and satisfy yourself that:

- The code change is neat and readable and follows the code style of the rest of the module.
- The logic is clear and there are comments if the logic is complex.
- The code does not have any obvious defects - such as likely to cause a `NullPointerException`.
- There are no uses of `log.error()` for logging errors that are not accompanied by an equivalent message to the audit log.
- If new dependencies have been added, these are documented in the developer resources.
- If changes to the types have been made, these changes are:
    - only made to the current release's types (that is, in `OpenMetadataTypesArchive.java`). It is permissible to correct typos in the other files but not change the shape of the types in the types created in previous releases (in files called `OpenMetadataTypesArchiveX_X.java`).
    - documented in [UML diagrams in the drawio files](/types) and the diagram has been exported as an image.

If you are also the code owner of the changed code then you also need to be sure that the changes are consistent with the current and intended future design of the module.

## Create samples

### Postman artifacts for APIs

We tend to use [Postman :material-dock-window:](https://www.getpostman.com){ target=postman } to test the various API endpoints we develop in Egeria. As such, there are a number of samples we make available for anyone to use for testing or otherwise becoming familiar with the Egeria APIs.

!!! tip "Disable SSL verification in Postman"
    Egeria by default uses `https://` requests with a self-signed certificate. Any Postman users therefore will need to go into **Settings** -> **General** and turn off **SSL certificate verification** or requests will fail.

When developing a new API in Egeria, you may want to make similar samples available to both provide examples of using the API and for basic testing purposes. These should be developed as follows:

1. Wherever possible, re-use the environment variables that are already defined in [Egeria.postman_environment.json :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-resources/open-metadata-samples/postman-rest-samples/Egeria.postman_environment.json){ target=gh }. If you need another variable that is not already defined, add it to this environment definition.

    This way we have a single environment definition that covers all possible sample configurations.

1. Create a [Postman Collection :material-dock-window:](https://learning.getpostman.com/docs/postman/collections/intro-to-collections/){ target=postman } that includes REST samples for your API. Name it using the convention `Egeria-<area>-<operations>` where `<area>` represents the unique area of your API (for example the name of an OMAS) and `<operations>` can optionally be used to distinguish between multiple collections that may be useful for different purposes (e.g. read vs. write operations). Consider adding [test scripts :material-dock-window:](https://learning.getpostman.com/docs/postman/scripts/test-scripts/){ target=postman } to your collection to check expected values, if you intend to use them for testing purposes.

    Once ready for sharing, export the collection into a file and commit your collection into GitHub wherever is most appropriate for the anticipated users of the samples.

1. Create a descriptive entry in [postman-rest-samples/README.md :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-resources/open-metadata-samples/postman-rest-samples/README.md){ target=gh } under a sub-section of the **Sample Collections** heading, linking to your new collection within GitHub. Use the existing samples defined there for guidance: provide a limited introductory description to any pre-requisites for your collection, if it needs to be run after some other collection define these in a sequence, etc.

    If your description for use requires more than 1-2 simple sentences, consider linking to more detailed instructions rather than putting these all into the general `README`. (See samples where we link out to more information on loading Coco Pharmaceuticals samples rather than embedding all of this detail directly in the one `README`.)

1. Within your descriptive entry, link to your collection. Following the other examples, provide a link to the raw file so that the link itself can be copy / pasted into Postman (without needing to download the file and then import it).

In this way, anyone wanting access to the REST samples of Egeria has a single place from which to find
them, while those working in a particular area of Egeria can still find the appropriate samples for that area
directly within the area of interest.

## Manage dependencies

New dependencies **must** only be introduced with the agreement of the broader community. These include frameworks, utility classes, annotations and external packages. This may seem annoying but there are good reasons for this:

- The Egeria code needs to be embeddable in different vendor products. This is made easier by keeping the code libraries we are dependent on to the minimum in order to avoid conflicts with libraries a consuming vendor may have already chosen, or where it needs to be embedded in an environment where certain dependencies may not be available.
- As developers, we have legal obligations to ensure we only use appropriately licensed software in our work and part of the discussion related a new dependency is to understand its license.
- Some projects may provide useful functionality but are only supported by one person who may get bored with it, or no longer have the time to support it. We should aim to build on dependent libraries that are backed by a strong community or vendor.
- Each library function, or set of annotations, adds to the learning curve of new people joining the team. By only bringing in the really beneficial libraries we ensure that the complexity they see relates only to the complexity of the problem space, rather than the additional complexity we have introduced in pursuit of playing with new functions.
- Each additional library extends the code footprint on which Egeria is based, and this inevitably extends the potential security exposure footprint. Limiting the libraries we use allows us to more quickly focus on resolving any potential security concerns (CVEs) any particular library may introduce.

If a developer wishes to introduce a new dependency to the Egeria project, they should prepare a short guide (in a markdown file) that explains the value of the new library, how it is to be used and links to more information. They should then present their recommendation to the community and if agreed by the community, store the guide in the developer resources.

Once in place, the dependency should be maintained across the smallest appropriate number of modules, and should be consistent throughout: particularly when it may impact consuming technologies.

### General rules

- Calls to third party technology that Egeria is integrating must be isolated into connectors so that they are optional. 
- Code should be in a seperate repo if lifecycle, community or technology significantly differ from Egeria core.
- Try to use standard Java and Egeria's existing dependencies where possible - consider carefully if a new dependency is needed.
- Use dependency constraints defined in the egeria bom (bom/build.gradle) to ensure consistent use of versions
- Always use the dependency at the lowest-level `build.gradle` where it's needed.
- Use a current non-beta version of a dependency.
- Check build output carefully for any dependency warnings and errors.
- Do not add any exceptions to the existing rules without discussion with other maintainers.

### `slf4j` and bindings

- Any utility, sample, tool or other *applications* (like the server chassis) that have an entry point (typically `main()`) should [include a binding for `slf4j` :material-dock-window:](http://www.slf4j.org/faq.html){ target=slf4j }.
    - Use `logback` when possible (for example, `ch.qos.logback:logback-classic`).
    - Do **not** provide a configuration file: default formatting will be used and can be overriden by logback configuration at deployment time.
- Test code automatically includes `slf4j-simple` - a simple logging implementation
- Other code that forms libraries (most of our code) **must not** include a `slf4j` logging implementation. Otherwise, the application loses control of the logging implementation, hidden config files can change behavior, and a `multiple_bindings` issue will be raised by `slf4j`.
- If non-egeria dependencies use other logging frameworks, add in appropriate adapters to map them to slf4j-api as this will avoid conflicts and confusion.

### Understanding dependencies

Running `./gradlew printAllDependencies` is a useful way to understand what dependencies (direct and transitive) a module has.

### Adding a new dependency

- Check if the dependency is already listed in the BOM at `bom/build.gradle`. If not:
  - add an extra property under ext-> for clarity ie:
  ```groovy
     kafkaVersion = '3.4.0'
  ```
  - add a section such as the following within the `dependencies->constraints` section. This will include a version`:
    ```groovy
       api("org.apache.kafka:kafka-clients:${kafkaVersion}")
    ```
    This declaration only means that *if* a dependency is used, this version is used.

- Add the dependency to the `dependencies` section of your project's `build.gradle`:
  ```groovy
  api("org.apache.kafka:kafka-clients:${kafkaVersion}")
  ```

  Note that the version is not included - it will be picked up from the constraints`.

Now build to include some checks for correct usage of dependencies (see below):

!!! cli "Build Egeria"
    ```shell
    ./gradlew build
    ```

!!! info "More on scopes"
    Most dependencies will be of scope `Implementation` (used for build and runtime & test), or `testImplementation` (for test tools). There are [other scopes available :material-dock-window:](https://docs.gradle.org/current/userguide/declaring_dependencies.html){ target=gradle }.

### Build time checks

The top-level `build.gradle` defines checks that are run in reference to dependencies:

- correct scope applied to dependencies (ie are they used at runtime only, or for build, or perhaps just for test)
- any dependencies that are not used
- missing dependencies
- conflicts in logging implementations
- conflicts on other standard libraries (such as javax.* vs jakarta.*)

See the top level build.gradle for more details

If any of these checks fail an appropriate message will be displayed and the build will fail.

!!! attention "Incompatible versions"
    In some cases where incompatible versions are reported, it may be due to transitive dependencies: for example a component the Egeria code does not depend on directly, but only indirectly. The path to resolve the version could result in different versions being used, or at least attempted, then failing. To resolve this a reference can be added in our constraints to specify the version to use.

## Maintain security

Egeria's dependencies are scanned for potential CVEs automatically in two main ways:

- GitHub [scans dependencies :material-dock-window:](https://help.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies){ target=gh } for known CVEs.
- Regular [Sonatype scans :material-dock-window:](https://lift.sonatype.com/results/github.com/odpi){ target=sonatype } is run.

The maintainers will review these regularly and action any required changes through issues and pull requests.

Egeria code itself is also scanned for vulnerabilities by various scanners which vary by repository. Sonatype Lift and Github CodeQL are commonly used, and will add notes into PRs for developers to review.


For more information on how potential security issues are handled, see [security hardening](/guides/developer/process/#security-hardening).

## Keeping dependencies up to date

[Dependabot](https://github.com/dependabot) is enabled on all egeria repositories to keep our dependencies up to date. This includes not just java code, but other languages too. Docker container images, and github actions are also covered.

Dependabot will notice when a new dependency update is available, and create a PR in the repository. For egeria this is typically monthly, on the 1st of the month. (but repositories vary)

These PRs should be reviewed promptly, and merged if possible. Where there is a reason to delay and close the PR, and issue should be opened to track any blockers to performing the merge

This is a responsibility of the github repository owner.

For an example refer to the core egeria [dependabot.yml](https://github.com/odpi/egeria/blob/main/.github/dependabot.yml)

### Handling large numbers of updates

Some repositories, such as core Egeria, may have many dependencies to update, resulting in many PRs at the beginning of each month. rather than merging PRs one by one, a 

To merge each individually could take a long time, especially as the other PRs then need rebasing, and will again have FVTs re-run.

An alternative is to:

* Ensure your origin/main is updated with upstream/main (`git checkout main && git pull upstream main`)
* Create a development branch (ie 'dependabot_20230512') (`git checkout -b dependabot_20230512`)
* Open up each PR in turn, and for each commit listed, cherry-pick into the dev branch (`git cherry-pick -s <commit-id>`)
* Build/test locally, and fix as required (`./gradlew build`)
* create a PR
* merge PR
* At this point, over the next day or so, the dependabot PRs will automatically close
* After 1 day manually review any still left open - sometimes they fail to rebase.

For the actual cherry-picking, if the  is installed a script can be used.

For example, the following will:

 * cherry pick a commit
 * Display if any conflicts occur
 * If needed, user should then fix up the conflict manually, and to a `git add . && git cherry-pick --continue`, or skip with `git cherry-pick --abort`
 * wait for user to hit enter. 
 * this will continue until all open PRs from dependabot are handled (max 49)

The following tools must be installed:

 * [jq](https://github.com/stedolan/jq)
 * [GitHub CLI 'gh'](https://cli.github.com)
```
#!/bin/sh
git fetch --all
for c in `gh pr list -L49 --app 'dependabot' --json id,commits | jq '.[] | .commits[].oid' `
do
  c2=`echo $c | tr -d '"'`
  git cherry-pick -s  $c2
read y
done
```
### Grouped Updates

In May 2023 Github started a private beta to enable [grouping of updates](https://gist.github.com/brrygrdn/0dac4e16c68898fda33d8fa81d575e1a) in response to feedback. The core 'egeria' repository is enabled for this capability.

The objective is to select sets of dependencies that are best managed as one unit. This should improve consistency, and mean that we run the updates together in the verification pipeline - including
running our FVT tests. Independently the updates might fail since there could be dependencies between spring and springboot.

An example is spring where we also include tomcat:
```yaml
  # Grouping of dependencies - useful to retain consistency & prevent build breaks
  groups:
    spring:
      patterns:
        - "*spring*"
        - "*tomcat*"
```


--8<-- "snippets/abbr.md"
