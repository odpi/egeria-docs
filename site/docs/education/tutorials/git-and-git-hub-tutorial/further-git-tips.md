<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

## Additional git tips

If you are working locally, and realise you have accidentally been making changes on master instead of another branch:

```bash
$ git stash
$ git checkout -b correct-branch
$ git stash pop
```

Messed up your master branch?

```bash
$ git checkout master
$ git fetch upstream
$ git reset --hard HEAD
$ git push
```

Correct your last commit

```bash
$ git commit --amend -s -m "New commit message"
```

View recent changes

```bash
$ git log
```

View recent changes in a prettier way:

```bash
$ git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
```

Take a fix you have pushed to a different branch (perhaps a top-level pom change, or something else you need) and apply it to your current branch:

```bash
$ git cherry-pick <commit-id>
```
---8<-- "snippets/abbr.md"
