<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Quickstart Environment

The **quickstart** environment is a pre-configured environment around [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) that is designed to be used for
learning and experimentation.  It is a good starting point for those who are new to Egeria and want to
get a feel for the platform without having to configure everything from scratch.

## Up and running with Quickstart

---8<-- "snippets/tasks/task-getting-workspaces.md"

Now, from the `egeria-workspaces` directory,
run the start up command.

=== "Single Machine Operation"

    if everything is to run on a single computer use the following command to start the environment:

    ```bash
    ./quick-start-local
    ```

=== "Multi-Machine Operation"

    If you want to run Egeria as a server, that people can connect to from their own machines use the following command to start the environment:

    ```bash
    ./quick-start-multi-host` 
    ```
____


The script will download all the software needed by Egeria and start it up.  Once it has completed, you are ready to go ...

## Begin with the Explorer





--8<-- "snippets/work-in-progress.md"

## Inside the Quickstart environment


![Quickstart Environment](egeria-workspaces-quickstart.svg)


--8<-- "snippets/abbr.md"
