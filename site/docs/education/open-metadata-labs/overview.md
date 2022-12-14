<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Labs

The open metadata labs contain an interactive environment that allow you to experiment with different capabilities of the Egeria project.  As such we often refer to them as **Hands-on Labs**.

The open metadata labs are implemented using [Jupyter Notebooks](/education/tutorials/jupyter-tutorial/overview).  Each lab notebook describes a scenario from the [Coco Pharmaceuticals](https://github.com/odpi/data-governance/tree/main/docs/coco-pharmaceuticals) case study, focusing on a challenge that one or more of the characters face and how they approached the solution.

The calls to the Egeria APIs necessary to complete the challenge are encoded in the [notebook](/education/tutorials/jupyter-tutorial/overview), so you can experiment with the APIs.

These labs can be used for individual study, as part of a class and / or as the basis of a workbook for using Egeria within a specific organization.

## Running the Labs

There are two main ways to set up the software to run these labs.  These are listed below. They each create exactly the same environment that supports the labs. 

* [Using Kubernetes](/guides/operations/kubernetes) to run them in a flexible, self-contained environment - locally or in the cloud.
* [Using your own local environment directly](/education/open-metadata-labs/running-natively).

Once the software is in place, and the four platforms are running, you then go to the `JupyterLab` browser window (typically at `http://localhost:8888/lab`) and begin with the [read-me-first.ipynb](https://github.com/odpi/egeria/blob/main/open-metadata-resources/open-metadata-labs/read-me-first.ipynb) lab notebook to familiarize yourself with the tutorial tools.  This notebook will guide you to the rest of the labs.


![Read me first Jupyter Notebook](/education/tutorials/jupyter-tutorial/jupyter-notebook-browser-window.png)


You can start running a notebook by simply double-clicking the filename in the left pane of the Jupyter interface.

--8<-- "snippets/abbr.md"
