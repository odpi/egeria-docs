<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Downloading the Egeria Source from GitHub

The code for Egeria is downloaded from each git repository one at a time.  The commands shown below create a clone (copy) of the egeria git repositories for your own use.  If you want to make a contribution to Egeria, you need to [clone your own fork](/education/tutorials/git-and-git-hub-tutorial/#creating-a-fork-and-a-clone) of a repository rather than the main repository itself. 

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
    
    === "Get the latest version of the code"
        To retrieve the latest "SNAPSHOT" code from the `main` branch of Egeria enter:
        ```bash
        git clone https://github.com/odpi/egeria.git
        ```
    === "Get a released version of the code"
        To retrieve the code for a specific release of Egeria enter
        ```bash
        git clone -b egeria-release-{release-number} --single-branch https://github.com/odpi/egeria.git
        ```
        For example, for release 3.14 use:
        ```bash
        git clone -b egeria-release-3.14 --single-branch https://github.com/odpi/egeria.git
        ```
        
    A new directory has been created with the core Egeria source code.  Change to the `egeria` directory and you are ready to build the source.
    
    ```bash
    cd egeria
    ```
  

=== "egeria-samples.git"

    Create a new directory for Egeria's main libraries. In the example below it is called `egeria-samples-source`:

    ```bash
    mkdir egeria-samples-source
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-samples-source
    ```
    
    Egeria's samples source is extracted from GitHub using the following `git` command:
    
    ```bash
    git clone https://github.com/odpi/egeria-samples.git
    ```
    
    A new directory has been created with the samples' source code.  Change to the `egeria-samples` directory and you are ready to build the source.
    
    ```bash
    cd egeria-samples
    ```
    
=== "egeria-dev-projects.git"

    Create a new directory for Egeria's developer projects. In the example below it is called `egeria-dev-projects-source`:

    ```bash
    mkdir egeria-dev-projects-source
    ```
    
    Change to your new directory.
    
    ```bash
    cd egeria-dev-projects-source
    ```
    
    Egeria's source is extracted from GitHub using the following `git` command:
    
    ```bash
    git clone https://github.com/odpi/egeria-dev-projects.git
    ```
    
    A new directory has been created with the developer projects source code.  Change to the `egeria-dev-projects` directory and you are ready to build the source.
    
    ```bash
    cd egeria-dev-projects
    ```

The `ls` command allows you to list the files from the repository:

```bash
ls
```

It should be the same as the contents of the git repository on GitHub.

---8<-- "snippets/abbr.md"
