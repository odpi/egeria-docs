<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Quickstart Environment

The **quickstart** environment is a pre-configured environment based around the [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) scenarios, designed for
learning and experimentation.  It is a good starting point for those who are new to Egeria and want to
get a feel for the platform without having to configure everything from scratch.

The instructions below will guide you through the process of setting up the environment on you own computer.  There is also a public version of the environment that you can use to explore Egeria, called the [Egeria Quickstart Demo Sandbox](/egeria-workspaces/demo-environment/overview).

## Up and running with Quickstart

---8<-- "snippets/tasks/task-getting-workspaces.md"

??? tip "4. "Run the start-up command"

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

??? tip "5. Select a persona"

    Selecting a persona logs you into the quickstart environment with the credentials for that persona.  This effects the view of the metadata, and access priviliges you have when exploring the system.  No-one can see everything.  So pick a persona closest to your interest.  For example, if you are interested in metadata about systems, pick **Gary Geeke**, if you like to explore their data governance program, pick **Jules Keeper** and so on. 

    The persona supported by the Quickstart environment are:

    * [Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview) - Erin is an information architect involved in the data governance program and the data aspects of their [business transformation](/practices/coco-pharmaceuticals).
    * [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) - Gary is their infrastructure lead.  He is building the inventory of their systems and a governance program on top.
    * [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) - Jules is the CDO, responsible for the data governance program.
    * [Peter Profile](/practices/coco-pharmaceuticals/personas/peter-profile) - Peter is a Data Engineer working on digital products and the supply chains used for clinical trials.
    * [Callie Quartile](/practices/coco-pharmaceuticals/personas/callie-quartile) - Callie is a data scientist working on clinical trials.
    * [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) - Ivor is the head of security and is setting up their security governance.
    * [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) - Faith is the head of HR and CPO and so is interested in the protection of personal data.
    * [Polly Tasker](/practices/coco-pharmaceuticals/personas/polly-tasker) - Polly is a senior IT Project Manager and is responsible for the IT governance program.
    * [Tom Tally](/practices/coco-pharmaceuticals/personas/tom-tally) - Tom leads the sustainability program.
    * [Lemmie Stage](/practices/coco-pharmaceuticals/personas/lemmie-stage) - Lemmie is a DevOps specialist looking to automae the capture of the IT landscape.
    * [Stew Faster](/practices/coco-pharmaceuticals/personas/stew-faster) - Stew is head of manufacturing. He is leading the digitization of the manufacturing plants.
 

??? tip "6. Start exploring the open metadata ecosystem"

    You are ready to go.  There are no set paths to follow, however, each of the [scenarios](/practices/coco-pharmaceuticals/scenarios) includes suggestions on how to explore Egeria in the context of that scenario.   

## Inside the Quickstart environment


![Quickstart Environment](egeria-workspaces-quickstart.svg)


--8<-- "snippets/abbr.md"
