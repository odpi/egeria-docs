<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


These are the steps to get up and running with your chosen egeria-workspaces environment:
              
??? tip "1. Download and install a **Docker hosting environment**"
    The Egeria community typically uses [Docker Desktop](https://www.docker.com/products/docker-desktop) which is free for individuals, and offers a selection of plans for businesses that wish to create a supported environment.  Alternatively you could use something like [Podman](https://podman.io/docs) or [Vagrant](https://www.vagrantup.com/) to run the environment.

??? tip "2. Download and install `git` (optional, but simplifies the process of keeping Egeria up to date)"
    Git is a source code management system that provides access to Egeria's code. Type the command `git -v` to see if it is installed.  If the git command is not recognized, the [Install Git](https://github.com/git-guides/install-git) guide provides instructions for various operating systems.

??? tip "3. Download Egeria's workspaces' Git repository"
    Egeria's workspaces' git repository is on [GitHub](https://github.com/odpi/egeria-workspaces).  There are three approaches, a simple download, a git clone or using a git fork and clone.  The latter two are recommended because they make it easy to refresh your environment with the latest workspaces function.  However, they do require 'git' to be installed on your local machine (see step above).  

    The fork and clone method is only needed if you think you may wish to contribute some of your work to the Egeria project.  You need a GitHub account to create a fork. (How to [create a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) if you do not already have one.).

    === "Simple download"
        Download the latest version of Egeria's workspaces from GitHub by clicking on the green **Code** button and selecting **Download ZIP**.

        ![Download Egeria Workspaces ZIP file](/egeria-workspaces/download-egeria-workspaces.png)
        
        Unzip the file and change to the `egeria-workspaces` directory.
        
    === "Simple git clone"
    
        From a command window, create a new directory (folder) for Egeria's workspaces on your local machine.
    
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
     
    === "Fork and clone for project contributors"
    
        From a command window, create a new directory (folder) for Egeria's workspaces on your local machine.
    
        ```bash
        mkdir egeria-workspaces
        ```
        
        Change to your new directory.
        
        ```bash
        cd egeria-workspaces
        ```
        
        Egeria's workspaces files are extracted from GitHub using the following `git` command.  Replace `USER` with your GitHub user name:
        
        ```bash
        $ git clone https://github.com/USER/egeria-workspaces.git
        ```
        
        A new directory has been created with the workspaces' source code.  Change to the `egeria-workspaces` directory and you are ready to build the source.
        
        ```bash
        cd egeria-workspaces
        ```
       
        Next set-up the upstream repository to connect your clone to the main Egeria repository:
    
        ```bash
        $ git remote add upstream https://github.com/odpi/egeria-workspaces.git
        ```
    
        Finally check that all is set up correctly:
    
        ```bash
        $ git remote -v
        origin  https://github.com/USER/egeria-workspaces.git (fetch)
        origin  https://github.com/USER/egeria-workspaces.git (push)
        upstream        https://github.com/odpi/egeria-workspaces.git (fetch)
        upstream        https://github.com/odpi/egeria-workspaces.git (push)
        $
        ```
    _____
    
    The `ls` command allows you to list the files from the repository:
    
    ```bash
    ls
    ```
    
    It should be the same as the contents of the git repository on GitHub.
    