<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

![Blue - Intermediate sessions](egeria-dojo-session-coding-blue-intermediate-session.png)

# Making a contribution to Egeria - Step-by-Step

In this session, you will be guided on how to make a simple change to the Egeria project.
This change is to add a new file to the
[egeria-dojo-postcards directory](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-tutorials/egeria-dojo-postcards)
and link to it in the `README.md` file of the same directory.

![Making a contribution to Egeria](egeria-dojo-day-2-3-contribution-to-egeria.png)

There are two videos for this session:

* How to make a contribution: [https://youtu.be/vdHRtuIYwoE](https://youtu.be/vdHRtuIYwoE)
* Pull Requests and testing: [https://youtu.be/pMODYyPJ1b4](https://youtu.be/pMODYyPJ1b4)

## The Steps

To create your own contribution, click on each step and complete the tasks described:

* [Review the contributor guidelines](/guides/contributor/guidelines) to understand the requirements for an Egeria contribution.

* [Log on to GitHub](/education/tutorials/git-and-git-hub-tutorial/task-getting-git-hub-id).

* [Create a Git Issue](/education/tutorials/git-and-git-hub-tutorial/task-creating-an-issue-on-git-hub). 
  Every contribution begins with a `git issue`. This describes the changes that you plan to make.
  The more detail that you provide, the better the maintainers will understand your contribution and
  be able to process it faster.
  
* [Create a fork and clone of the git repository](/education/tutorials/git-and-git-hub-tutorial/task-creating-a-fork-and-clone) to bring the Egeria code onto your machine.

* [Create a new git branch](/education/tutorials/git-and-git-hub-tutorial/task-adding-changes-to-git) to contain your change.

* [Load Egeria into your IDE](/education/tutorials/intellij-tutorial/task-loading-egeria-into-intellij) so that you can see the project contents.

* [Build Egeria](/education/tutorials/intellij-tutorial/task-building-egeria-in-intellij) so it is ready to run.
  The link assumes you are using IntelliJ.  If you prefer working with the command line try [this link](/education/tutorials/building-egeria-tutorial/task-building-egeria-source)

* [Create your contribution](/education/tutorials/intellij-tutorial/task-creating-content-with-intellij) - typically using the IDE.
  You need to create a new markdown file, add your message to the file and then add a link to the README.md file.
  Both of these files should use [Markdown](/guides/contributor/markdown) and
  include license and copyright statements top and bottom of the file just like this file: 
  [License File Example](https://raw.githubusercontent.com/odpi/egeria/main/developer-resources/License-Example-Files/License_for_Markdown_Files.md).
  
  (There is more information on licences in the [Contributor Guidelines](/guides/contributor/guidelines).)

* [Test your changes](/education/tutorials/testing-egeria-tutorial) to make sure your new function works and nothing else has broken.
  Since this is a document change, there should be no impact on the code - so running these tests is to check that
  nothing has changed by accident.

* [Add and commit changes to Git](/education/tutorials/git-and-git-hub-tutorial/task-adding-changes-to-git).
  As you commit your changes, make sure they are signed (see [Why the DCO?](https://github.com/odpi/egeria/tree/main/developer-resources/why-the-dco.md)).

* Initiate the [request to include your changes](/education/tutorials/git-and-git-hub-tutorial/task-git-pull-push-pr) into the main branch of Egeria.
  
Once the PR is in place, GitHub will check the DCOs for you commits, and then run a full build on Java 17.  The Egeria maintainers will review your contribution and may ask you to make changes to it.  When it is acceptable, they will merge it into main and your contribution is complete.


----
* Progress to [Types of Contribution](egeria-dojo-day-2-4-types-of-contribution.md)


* Return to [Tools for Contributors](egeria-dojo-day-2-2-tools-for-contributors.md)

---8<-- "snippets/abbr.md"
