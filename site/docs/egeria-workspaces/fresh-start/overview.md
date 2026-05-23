<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Freshstart Environment

The **freshstart** environment is a pre-configured environment that is designed for your work.  It is a good starting point for those who want to
start using Egeria for their own projects without having to configure everything from scratch.

## Up and running with Freshstart

---8<-- "snippets/tasks/task-getting-workspaces.md"

Now, from the `egeria-workspaces` directory,
run the start up command.

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


The script will download all the software needed by Egeria and start it up.





--8<-- "snippets/work-in-progress.md"

## Inside the Freshstart environment

![Freshstart Environment](egeria-workspaces-freshstart.svg)

--8<-- "snippets/abbr.md"
