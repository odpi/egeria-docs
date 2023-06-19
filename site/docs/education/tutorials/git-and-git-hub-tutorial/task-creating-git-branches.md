<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Creating a branch for your work

Once you have a [clone of the git repository](/education/tutorials/git-and-git-hub-tutorial/overview/#cloning)
there is one more step before you can begin developing. 

Most development work is done on your local clone with occasional calls to GitHub to
synchronize with its versions of the repository.

![Figure 4](/education/tutorials/git-and-git-hub-tutorial/git-development.svg)
> **Figure 4:** Local development process using git

The top level branch (copy) of a git repository is called `main`.
It is recommended not to make any changes directly to main
but just to use it for reference and as a basis for branching.

It is also recommended to create a new branch for each distinct set of changes. This keeps the commit history pushed
to Egeria clean, and makes reviews of the code much easier for the maintainers.
Since GitHub manages the introduction of new content on a branch basis it is also a way to be able to easily rework, by updating a
change later before it has been incorporated back into the main Egeria code.

First update your copy of main in your clone and push to your GitHub fork.

```bash
$ git checkout main
$ git pull upstream main
$ git push
```

Once you have the latest code on your machine, create a branch for your changes. The
commands below set up a branch called "example-branch" based off of main, and also push
it back to your personal fork:

```bash
$ git checkout -b example-branch main
$ git push origin example-branch

```

When you create your own branch, use a name that describes that the branch is for as you will
use it for all changes you are collecting together to push as one group to Egeria.
This name will be publicly visible too once you start pushing your changes
to Egeria so keep it clean :).

You can also see that 'origin' will point to your GitHub fork, whilst 'upstream' points to the Egeria main branch:

```bash
$ git remote -v

origin https://github.com/USER/egeria (fetch)
origin https://github.com/USER/egeria (push)
upstream https://github.com/odpi/egeria.git (fetch)
upstream https://github.com/odpi/egeria.git (push)

```

Now you can make your changes to the content.  


