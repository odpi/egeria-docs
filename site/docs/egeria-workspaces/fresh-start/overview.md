<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Freshstart Environment

The **freshstart** environment is a pre-configured environment that is designed for your work.  It is a good starting point for those who want to
start using Egeria for their own projects without having to configure everything from scratch.

## Up and running with Freshstart

---8<-- "snippets/tasks/task-getting-workspaces.md"


??? tip "4. "Set up your organization name"
    Edit the file `runtime-volumes/freshstart-platform-data/freshstart.application.properties` and scroll down to the `platform.organization.name` property to your organization name.  By default, it is set to `Egeria Freshstart`.  Make your name match the name of the group that your users belong to, or the owners of metadata managed by this deployment of freshstart.  So, for example, use your team name if it is a team deployment, or the organization name if it is for the whole organzation.

    For example, when [Robbie Records](/practices/coco-pharmaceuticals/persona/robbie-records) sets up his environment, he uses the name `Patient Records Data Sharing Hub`.

    ```yaml
    ###############################################
    ### Set up the name of who is running this platform.
    ##### If this is for personal use, add your own name.
    ##### If this is for your team, add your team name ...
    ################################################
    platform.organization.name=Patient Records Data Sharing Hub
    ```

??? tip "5. "Run the start-up command"
    Now, from the `egeria-workspaces` directory,
    run the startup command.
    
    === "Single Machine Operation"
    
        if everything is to run on a single computer use the following command to start the environment:
    
        ```bash
        ./fresh-start-local
        ```
    
    === "Multi-Machine Operation"
        
        If you want to run Egeria as a server, that people can connect to from their own machines use the following command to start the environment:
    
        ```bash
        ./fresh-start-multi-host` 
        ```
    ____
 
    The workspaces start up script will download all the software needed by Egeria and start it up. When it has completed the set up, it will display the URL of the *Egeria Portal*.  Click on the link, or copy the link and paste it into your browser.

??? tip "6. Start up the Egeria Portal"

    The Egeria Portal is a web application that allows you to explore the metadata that is stored in Egeria.

??? tip "7. Set up your users"

--8<-- "snippets/work-in-progress.md"

## Inside the Freshstart environment

![Freshstart Environment](egeria-workspaces-freshstart.svg)

--8<-- "snippets/abbr.md"
