<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Running Egeria natively

The technologies described on this page are required to operation Egeria. They are included when using the self-contained environments, but they can also be installed and run natively (directly) on your system.

Just be aware that running them natively on your system will require the additional effort of downloading, installing,
configuring and operating each one -- which the self-contained environments largely take care of for you. To make use
of the latest Egeria software, you will likely also need to be familiar with how to [build Egeria](/education/tutorials/building-egeria-tutorial/overview) in
order to use it natively.

## Installing and configuring prerequisite software

--8<-- "snippets/tasks/task-installing-java.md"
--8<-- "snippets/tasks/task-installing-git.md"
--8<-- "snippets/tasks/task-installing-kafka.md"
--8<-- "snippets/tasks/task-starting-kafka.md"
--8<-- "snippets/tasks/task-downloading-egeria-source.md"
--8<-- "snippets/tasks/task-building-egeria-source.md"
--8<-- "snippets/tasks/task-installing-egeria.md"
--8<-- "snippets/tasks/task-installing-jupyter.md"

## Starting up your environment

Follow the [OMAG Server Platform tutorial](/education/tutorials/omag-server-tutorial/overview)
for instructions on how to set up and run a platform yourself.
You need to start four OMAG Server Platforms at the following URLs - remembering to use the `-Dserver.port=nnnn` option:

- `https://localhost:9443`
- `https://localhost:9444`
- `https://localhost:9445`
- `https://localhost:9446`


## Help

For additional help refer to our Slack channels at http://slack.lfaidata.foundation

--8<-- "snippets/abbr.md"
