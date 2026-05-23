<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Creating a fork and a clone

The git repositories for Egeria are read only to everyone except the
[Egeria Maintainers](https://github.com/odpi/egeria/blob/main/MAINTAINERS.md).  This is to protect the content from
accidental or malicious damage.

However, anyone wanting to make a contribution needs
editing access to the repositories to make the change and test it.
This is achieved with the `git fork` and `git clone`.

#### Forking

Forking creates your own version of the egeria git repository that is linked back to the
original.

Figure 2 illustrates the forking process.

![Figure 2](/education/tutorials/git-and-git-hub-tutorial/git-hub-fork.svg)
> **Figure 2:** Forking an Egeria git repository

To create your fork, from your browser, navigate to the appropriate url for your repository:

* [Egeria GitHub URL](https://github.com/odpi/egeria),
* [Egeria Workspaces GitHub URL](https://github.com/odpi/egeria-workspaces),
* [Egeria DocumentationGitHub URL](https://github.com/odpi/egeria-docs),
* [Egeria Python GitHub URL](https://github.com/odpi/egeria-python),

* Log into the github UI with 
[your GitHub id](/education/tutorials/git-and-git-hub-tutorial/task-getting-git-hub-id).
You will then see a 'Fork' button at the top right, and should click this to 
create your own fork to work with Egeria. 

![Fork Button](/education/tutorials/git-and-git-hub-tutorial/git-hub-fork-button.png)

This only needs to be done once.

#### Cloning

Once you have your fork, you need to create a copy of the repository on your local machine.
This copy is called a **clone**.  You create a clone each time you are starting a significant piece of work.

Figure 3 illustrates the cloning process.

![Figure 3](/education/tutorials/git-and-git-hub-tutorial/git-clone.svg)
> **Figure 3:** Cloning an Egeria git repository

To create a clone on your machine enter the following in a new directory from a terminal/command window.
Replace `USER` with your GitHub userId.
____

=== "egeria.git"

    ```bash
    $ git clone https://github.com/USER/egeria.git
    $ cd egeria
    ```

=== "egeria-workspaces.git"

    ```bash
    $ git clone https://github.com/USER/egeria-workspaces.git
    $ cd egeria-workspaces
    ```

=== "egeria-docs.git"

    ```bash
    $ git clone https://github.com/USER/egeria-docs.git
    $ cd egeria-docs
    ```

=== "egeria-python.git"

    ```bash
    $ git clone https://github.com/USER/egeria-python.git
    $ cd egeria-python
    ```
____


The git clone command creates a new directory called `egeria` containing the Egeria content.

You should also set the upstream repository to connect your clone to the main Egeria repository:

____

=== "egeria.git"

    ```bash
    $ git remote add upstream https://github.com/odpi/egeria.git
    ```
=== "egeria-workspaces.git"

    ```bash
    $ git remote add upstream https://github.com/odpi/egeria-workspaces.git
    ```

=== "egeria-docs.git"   

    ```bash
    $ git remote add upstream https://github.com/odpi/egeria-docs.git
    ```

=== "egeria-python.git"

    ```bash
    $ git remote add upstream https://github.com/odpi/egeria-python.git
    ```

____

Now you are ready to [create a branch for your changes](/education/tutorials/git-and-git-hub-tutorial/task-creating-git-branches).

??? education "Further information"

    * Further details of [GitHub's fork and pull model](https://help.github.com/articles/about-collaborative-development-models/),
    * Further details on the [fork](https://guides.github.com/activities/forking/) command.



