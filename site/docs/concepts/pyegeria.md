<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Pyegeria

The [pyegeria python library](https://github.com/odpi/egeria-python) provides a wide-ranging set of python functions for retrieving the status of Egeria's platform, servers and connectors, and interacting with the open metadata ecosystem. 

![pyegeria](pyegeria.svg)

It is available in through a variety of interfaces.

* A [Python client](/guides/developer/python-client/overview) supporting a collection of python functions for calling Egeria's [Open Metadata and Governance (OMAG) services](/services/omvs) from a python program - or programming environment, such as Jupyter notebooks.
* A [command level interface (CLI)](/user-interfaces/hey-egeria/overview) for issuing commands to Egeria and widgets to display information held by Egeria.
* A [text-based menu of commands](/user-interfaces/hey-egeria/overview) allowing you to enter the options in a form and execute the command.
* A [markdown processor](/user-interfaces/dr-egeria/overview) for creating open metadata definitions such as solution blueprints, digital products, data specifications and glossaries of terms. It can also be used to create markdown reports and forms for updating metadata.


## Installing pyegeria (and keeping up to date)

*pyegeria* is installed from PyPI using the `pip install pyegeria` command.  It is advancing rapidly, so it is worthwhile checking that you have the latest level.  Firstly, to upgrade the base python functions, run the following command in your python environment (Jupyter Notebook, PyCharm, venv, etc):

```shell
pip install pyegeria --upgrade
```
If the libraries are upgraded, you will need to restart the python kernel. For example, from the JupyterLab menu bar select Kernel->Restart Kernel... and then confirm that you want the kernel to restart.

To check that the widgets and CLI are up-to-date, enter the following command on a command line (terminal/command window).

```shell
pipx upgrade pyegeria
```

!!! info "Further Information"
    * [Python Clients](/guides/developer/python-clients/overview)
    * [Scripting commands](/guides/developer/scripting-commands/overview)
    * [Hey Egeria](/user-interfaces/hey-egeria/overview)

--8<-- "snippets/abbr.md"
