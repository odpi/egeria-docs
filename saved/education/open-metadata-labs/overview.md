<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Labs

The open metadata labs contain an interactive environment that allow you to experiment with different capabilities of the Egeria project.  As such we often refer to them as **Hands-on Labs**.

The open metadata labs are implemented using [Jupyter Notebooks](/education/tutorials/jupyter-tutorial/overview){target=new}.  Each lab notebook describes a scenario from the [Coco Pharmaceuticals](https://github.com/odpi/data-governance/tree/main/docs/coco-pharmaceuticals){target=new} case study, focusing on a challenge that one or more of the characters face and how they approached the solution.

The calls to the Egeria APIs necessary to complete the challenge are encoded in the [notebook](/education/tutorials/jupyter-tutorial/overview){target=new}, so you can experiment with the APIs.

These labs can be used for individual study, as part of a class and / or as the basis of a workbook for using Egeria within a specific organization.

## Running the Labs

There are two main ways to set up the software to run these labs.  These are listed below. They each create exactly the same environment that supports the labs. 

* [Using Kubernetes](/guides/operations/kubernetes){target=new} to run them in a flexible, self-contained environment - locally or in the cloud.  In this case, all software components required to run are deployed using single helm chart called **odpi-egeria-lab**. The process is described [here](/guides/operations/kubernetes/charts/lab/).
* [Using your own local environment directly](#running-egeria-natively).

Once the software is in place, and the four platforms are running, you then go to the `JupyterLab` browser window (typically at `http://localhost:8888/lab`) and begin with the [read-me-first.ipynb](https://github.com/odpi/egeria-jupyter-notebooks/blob/main/read-me-first.ipynb){target=new} lab notebook to familiarize yourself with the tutorial tools.  This notebook will guide you to the rest of the labs.

![Read me first Jupyter Notebook](/education/tutorials/jupyter-tutorial/jupyter-notebook-browser-window.png)

You can start running a notebook by simply double-clicking the filename in the left pane of the Jupyter interface.

## Running Egeria natively

The technologies described on this page are required to operation Egeria. They are included when using the self-contained environments, but they can also be installed and run natively (directly) on your system.

Just be aware that running them natively on your system will require the additional effort of downloading, installing, configuring and operating each one -- which the self-contained environments largely take care of for you. To make use of the latest Egeria software, you will likely also need to be familiar with how to [build Egeria](/education/tutorials/building-egeria-tutorial/overview) in order to use it natively.

??? education "Installing and configuring prerequisite software"
    --8<-- "snippets/tasks/task-installing-java.md"
    --8<-- "snippets/tasks/task-installing-git.md"
    --8<-- "snippets/tasks/task-installing-kafka.md"
    --8<-- "snippets/tasks/task-starting-kafka.md"
    --8<-- "snippets/tasks/task-downloading-egeria-source.md"
    --8<-- "snippets/tasks/task-building-egeria-source.md"
    --8<-- "snippets/tasks/task-installing-egeria.md"
    --8<-- "snippets/tasks/task-installing-jupyter.md"

??? education "Starting up your environment"
    Follow the [OMAG Server Platform tutorial](/education/tutorials/omag-server-tutorial/overview)
    for instructions on how to set up and run a platform yourself.
    You need to start four OMAG Server Platforms at the following URLs - remembering to use the `-Dserver.port=nnnn` option:
    
        - `https://localhost:9443`
        - `https://localhost:9444`
        - `https://localhost:9445`
        - `https://localhost:9446`
    

??? tip "Help"
  For additional help refer to our Slack channels at http://slack.lfaidata.foundation

--8<-- "snippets/abbr.md"
