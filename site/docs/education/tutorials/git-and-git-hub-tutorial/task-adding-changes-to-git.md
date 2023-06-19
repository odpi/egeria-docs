<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

### Adding your changes to your git clone

Once you have completed your contribution, you are ready to add it to your git clone.

Most development work is done on your local clone with occasional calls to GitHub to
synchronize with its versions of the repository.

![Figure 4](/education/tutorials/git-and-git-hub-tutorial/git-development.svg)
> **Figure 4:** Local development process using git

Issue the `git status` command in a Terminal/Command window to verify all of your changes are
included.  This will list any new files and files that have been changed, but not yet included
in the git clone.  Use `git add` to add all of the files you want included.

For example:

```bash
$ git status

On branch example-branch
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	new-file.java

$ git add new-file.java
$ git status

On branch example-branch
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   new-file.java
```

Now you are ready to commit your contribution to your clone.


