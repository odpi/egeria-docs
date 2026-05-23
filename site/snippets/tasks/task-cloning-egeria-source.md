<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Cloning the Egeria Source using git commands

The code for Egeria is downloaded from each git repository one at a time.  The commands shown in each tab below create a clone (copy) of the egeria git repositories for your own use.  

??? tip "When to use a fork and clone rather than a simple clone"
    If you want to make a contribution to Egeria, or wish a simple way to refresh your copy with the latest code, you need to [create a fork and clone your fork](/education/tutorials/git-and-git-hub-tutorial/#creating-a-fork-and-a-clone) rather than cloning the main repository itself. 

=== "egeria.git"

    Create a new directory for Egeria's main libraries. In the example below it is called `egeria-main-libraries`:

    ```bash
    mkdir egeria-main-libraries
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-main-libraries
    ```
    
    Egeria's source is extracted from GitHub using the following `git` command:
    
    ____

    === "Get a released version of the code"
        To retrieve the code for a specific release of Egeria enter
        ```bash
        git clone -b egeria-release-{release-number} --single-branch https://github.com/odpi/egeria.git
        ```
        For example, for release 3.14 use:
        ```bash
        git clone -b egeria-release-3.14 --single-branch https://github.com/odpi/egeria.git
        ```
    === "Get the latest version of the code"
        To retrieve the latest "SNAPSHOT" code from the `main` branch of Egeria enter:
        ```bash
        git clone https://github.com/odpi/egeria.git
        ```
    
    ____

    A new directory has been created with the core Egeria source code.  Change to the `egeria` directory and you are ready to build the source.
    
    ```bash
    cd egeria
    ```
  

=== "egeria-workspaces.git"

    Create a new directory for Egeria's workspaces.

    ```bash
    mkdir egeria-workspaces
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-workspaces
    ```
    
    Egeria's workspaces files are extracted from GitHub using the following `git` command:
    
    ```bash
    git clone https://github.com/odpi/egeria-workspaces.git
    ```
    
    A new directory has been created with the workspaces' source code.  Change to the `egeria-workspaces` directory and you are ready to build the source.
    
    ```bash
    cd egeria-workspaces
    ```
    
=== "egeria-docs.git"

    Create a new directory for Egeria's documentation.

    ```bash
    mkdir egeria-docs
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-docs
    ```
    
    Egeria's documentation is extracted from GitHub using the following `git` command:
    
    ```bash
    git clone https://github.com/odpi/egeria-docs.git
    ```
    
    A new directory has been created containing the documentation.  Change to the `egeria-docs` directory and you are ready to build the documentation.
    
    ```bash
    cd egeria-docs
    ```

=== "egeria-python.git"

    Create a new directory for Egeria's python function.

    ```bash
    mkdir egeria-python
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-python
    ```
    
    Egeria's python code is extracted from GitHub using the following `git` command:
    
    ```bash
    git clone https://github.com/odpi/egeria-python.git
    ```
    
    A new directory has been created containing the code.  Change to the `egeria-python` directory and you are ready to work with python.
    
    ```bash
    cd egeria-python
    ```
____

The `ls` command allows you to list the files from the repository:

```bash
ls
```

It should be the same as the contents of the git repository on GitHub.


