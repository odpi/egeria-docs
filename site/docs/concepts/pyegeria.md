<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Pyegeria

The [pyegeria python library](https://github.com/odpi/egeria-python) provides a wide-ranging set of python functions for interacting with the Egeria runtime. In addition there is a command level interface (CLI) for issuing commands to Egeria and widgets to display information held by Egeria.  It includes:

* [Python client](/guides/developer/python-client/overview) - A collection of python functions for calling the Open Metadata and Governance services provided by egeria from a python program - or programming environment, such as Jupyter notebooks.


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

--8<-- "snippets/abbr.md"
