<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Scripting commands

The *pyegeria* command line services allow interaction with the open metadata and governance services of Egeria from a scripting language. The naming convention for the widgets helps to understand their behaviour. When the widget starts with:

* get - it will return details about a single item
* list - lists elements through a paging interface like "more" - use q to quit.
* view - provides a live view - typically of a status - use control-c to quit

## Installation
The **pyegeria** Egeria Python client can be installed from **pypi** . Python version 3.10 and above is a pre-requisite.
One common way to install Python packages is with the **pip** command. So to install **pyegeria** you can execute:

```shell
pip install pyegeria
```

This will install **pyegeria** and all of its required packages.

## Using

Once **pyegeria** is installed. The widgets may be invoked from a terminal window or shell either as a command or as a python script.
To start a widget as a command, just type its full name at the command prompt. For instance, typing:

```shell
view_platform_status.py
```

Will display a table showing the status of all running Egeria OMAG Server platforms.

![view_platform_status.png](view_platform_status.png)


Commands can also be invoked directly if you are in the same folder as the widget (or the widgets are on the python search path).

```shell
python3 view_platform_status.py
```

All of the widgets have optional command line arguments. You can see them by setting the `--h` help flag.

![command help](widget-help.png)

Most of the commands allow you to specify an Egeria OMAG Platform, Server (usually a view server), and user identity.  If not specified, default values will use the Egeria default configuration with:

* platform = "https://localhost:9443"
* server = "view-server"
* user id = a user, such as **erinoverview** from the fictitious [Coco Pharmaceuticals](https://egeria-project.org/practices/coco-pharmaceuticals/) environment.

!!! info "Full Guide to Egeria's Python Commands"
    The full guide to Egeria's Python Commands is available at [Command Line Interfaces](https://github.com/odpi/egeria-python/blob/main/pyegeria/commands/doc/command-overview.md)

--8<-- "snippets/abbr.md"