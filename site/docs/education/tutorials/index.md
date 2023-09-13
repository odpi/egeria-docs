<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Tutorials

--8<-- "snippets/supported-platforms.md"

The tutorials provide step-by-step guides that help you work with Egeria and its associated technology.  They provide help to:

* **[Those that just want to run and use Egeria](#tutorials-for-running-egeria)**.  This includes how to download and build Egeria, install it in a convenient directory, customise it and use containers for cloud deployment.
* **[Those that want to develop code with Egeria](#tutorials-for-developing-with-egeria)** (such as building new connectors or calling Egeria's APIs).  This includes setting Egeria up in IntelliJ ready for your development work.
* **[Those that wish to contribute to Egeria's code base](#tutorials-for-contributing-to-egeria)**.  This includes fixing bugs and adding new features to Egeria.

## Tutorials for running Egeria

Egeria is an open source project that can be:

* Run to support the open metadata labs.  These labs show Egeria in an operational mode serving different users in the Coco Pharmaceuticals business.  Egeria is integrated with a variety of technologies in this environment, and it is set up to specifically support the scenarios within the labs.  The implementation of the labs uses Kubernetes.  Follow [this link if you want to run the labs](/education/open-metadata-labs/overview).

* Used directly from a prebuilt docker image from either [DockerHub](https://hub.docker.com/r/odpi/egeria) or [Quay.io](https://quay.io/repository/odpi/egeria).  This docker image includes all the Egeria runtimes and can be used to experiment with different features of Egeria.  If this option is for you, [go to the docker tutorial](/education/tutorials/docker-tutorial/overview).

* Downloaded and built to create your own customized version of Egeria.  Egeria is highly customizable, use this method if you wish to deploy a customized Egeria for your organization.  Go to [Starting with the code](#starting-with-the-code) if this is for you.

Customizing Egeria typically begins with downloading and building Egeria's source code.  This requires Java.

??? tip "Installing Java"
    --8<-- "snippets/tasks/task-installing-java.md"

Once you have Java installed, you are ready to begin:

??? education "Downloading Egeria's source code"
    --8<-- "snippets/tasks/task-downloading-egeria-source.md"

??? education "Building Egeria"
    --8<-- "snippets/tasks/task-building-egeria-source.md"

??? education "Installing Egeria"
    --8<-- "snippets/tasks/task-installing-egeria.md"

Once Egeria is installed, it is ready to be used.

## Tutorials for using Egeria

The [open metadata labs](/education/open-metadata-labs/overview) show how Egeria can be used in multiple scenarios.  The labs are organized by user role, allowing you to focus on the aspects of Egeria that interests you. 

The installed assembly gives you the option to run the platform directly from this assembly and/or customize the assembly and build it into a Docker image that can be used as part of a cloud-deployment.

??? education "Working with the OMAG Server Platform"
    The [OMAG Server Platform tutorial](/education/tutorials/omag-server-tutorial) takes you through the process of starting and stopping the platform; configuring, starting and stopping servers and querying the status of the platform and its servers.

??? education "Building a customized docker image"
    --8<-- "snippets/tasks/task-building-customized-docker-image.md"

## Tutorials for developing with Egeria

The Egeria community typically uses IntelliJ for its development.  Information on how to set up your copy of IntelliJ with Egeria and build new components that work with Egeria are found in the [Using IntelliJ tutorial](/education/tutorials/intellij-tutorial/overview).

## Tutorials for contributing to Egeria

Egeria uses [GitHub's fork and pull model :material-dock-window:](https://help.github.com/articles/about-collaborative-development-models/){ target=gh } to create a contribution. This process is described in detail in the [Git and GitHub tutorial](/education/tutorials/git-and-git-hub-tutorial/overview#using-git-and-github-when-making-a-contribution).

Each change should have a [GitHub issue](https://github.com/odpi/egeria/issues) explaining why the change is being made. The new or updated content should follow the Egeria [developer guidelines](/guides/contributor/guidelines).

Every contribution is signed to say that the contributor has the rights to make the contribution and agrees with the [Developer Certificate of Origin (DCO) :material-github:](https://github.com/odpi/egeria/blob/main/developer-resources/why-the-dco.md){ target=gh }



    
