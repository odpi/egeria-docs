<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Dojo day 1

## Egeria introduction

In this session, you will learn about the function and value of Egeria
along with the key concepts and use cases it supports.

!!! beginner "Egeria introduction [:material-microsoft-powerpoint:](https://github.com/odpi/data-governance/raw/master/workshops/may-2020/egeria-dojo-day-1-1-introduction.pptx){ target=slides }"
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/s249ofNoETY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

### Test yourself

??? question "Which of the following are part of the Open Metadata Manifesto?"
    1. Metadata needs to be centralized so it can be managed.
    1. Maintenance of metadata must be automated.
    1. The availability of metadata management must become ubiquitous.
    1. Metadata access must become open and remotely accessible.

??? question "Name 3 tools that could connect to Egeria."

??? question "Name a metadata standard."

## Egeria project introduction

In this session, you will learn about the contents of the Egeria project.
It will also describe the software to download in preparation for
the next session.

!!! beginner "Egeria project introduction"
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/CN81aeSlWlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

### GitHub repositories

[GitHub](https://github.com) is a public service for managing files - particularly files associated
with a software project. Many open source projects use GitHub and Egeria is no exception.

All of the content for the Egeria project is stored in git repositories.
For example, these web pages you are reading as part of the dojo are
managed in [Egeria's main git repository](https://github.com/odpi/egeria/tree/master/open-metadata-publication/website/docs/getting-started/dojo){ target=code }.

Each directory in the repository has a README.md file written in [the Markdown standard](../../../developer-resources/tools/Markdown.md).
You can either click through on GitHub or link to the [Content Organization](../../../Content-Organization.md)
that lists the directories with descriptions.

### Other resources

The Egeria community love to collaborate on the work they do. Git and GitHub is
an excellent way to exchange and manage files. In addition, the community
runs public calls that anyone can join, as well as a number of Slack channels.

Details of the different ways the community operates is described in our
[Community Guide](../../../guides/community/).

### Test yourself

??? question "Name three of the git repositories owned by the Egeria project, and describe what they do."

??? question "Describe why the Egeria project is called _Egeria_"

??? question "Login to Slack and post a message to the `#egeria-dojo-live` channel"
    A simple "I'm working my way through the dojo!" will do :heart:

## Running Egeria

In this session, you will learn about the Open Metadata and Governance (OMAG) Server Platform that
hosts many of the services provided by Egeria.

!!! intermediate "Running Egeria"
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/jnxY2epKgzY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

### Prerequisites

Before we get started there are some steps to prepare your machine.

!!! tip "Ensure Docker Desktop and Postman are installed and running"
    For this session you will need both of these tools installed and running on your machine:
    
    - [Docker Desktop](todo.md)
    - [Postman](todo.md)

Follow the links below to find out a little bit about these technologies and ensure the software
is installed.

- [Docker Desktop](../../../developer-resources/tools/Docker.md)
- [Postman](../../../developer-resources/tools/Postman.md)

Once these technologies are installed, work through the tutorials - starting with Docker to get the
OMAG Server Platform running and then Postman to get
ready to work with the platform and the servers running on top if it.

- [Docker Tutorial](../docker-tutorial)
- [Postman Tutorial](../postman-tutorial)

At this point you should have Postman installed with the collections loaded, and Egeria's OMAG Server Platform running
as a docker container.

### Test yourself

??? question "What is the message from the OMAG Server Platform that says it is ready to process requests?"

??? question "How do you find out the version of Egeria running in an OMAG Server Platform?"

??? question "What is the url to view the Swagger UI page for the OMAG Server Platform?"

## Configuring the OMAG Server Platform

In this session, you will learn how to set up the OMAG Server Platform.

!!! intermediate "Configuring the OMAG Server Platform"
    <div class="video-wrapper">
        <iframe src="https://www.youtube.com/embed/-YScFx0fQk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

### Server origin

In the previous session you downloaded an application called Postman and loaded collections of
pre-defined requests. This tool makes it easy to issue REST API requests to the OMAG Server Platform.

Check that it is working by locating the `Get Server Origin` request in the
`Egeria-platform-services` collection.
When you click on that request in the left-hand list, a new tab opens and you can click on send to
issue the request.  You should see the same response as when you issues the platform origin request from
[Swagger](../docker-tutorial) earlier.  Below is this response in Postman.

![Postman server origin](../../../developer-resources/tools/postman-platform-origin.png#pagewidth)

If this does not work, then there is something wrong either in Postman or your platform.
Check the URL string that was used in the request (shown in orange in the middle of the screen.)

The screen shot below shows the error message when the egeria environment is not set.
This can be fixed by setting it in the top right-hand dropdown.  If the Egeria environment is not
listed then you need to load the environment ([Postman tutorial](../postman-tutorial)).

![Postman server origin - no environment](../../../developer-resources/tools/postman-platform-origin-no-environment.png#pagewidth)

If the baseURL variable is set to a different value to the server platform then Postman can not connect.
In the screen capture below, you can see the baseURL is set to the default of `https://localhost:9443` when it should be
`https://localhost:9443` because the platform is running in docker.

![Postman server origin - wrong base url](../../../developer-resources/tools/postman-platform-origin-wrong-base-url.png#pagewidth)

Finally, if the OMAG Server Platform is not running the even though everything is set up correctly in
Postman, it has nothing to connect to.  Restart the platform ([Docker tutorial](../docker-tutorial)).

![Postman server origin - platform down](../../../developer-resources/tools/postman-platform-origin-no-platform.png#pagewidth)

In last part of this session you will learn how to set up the OMAG Server Platform so that it is secure and
determine the services and servers that are associated with the platform.

### Configuration document store

### Platform security

### Registered services

### Known / active servers


Review the description of the OMAG Server Platform configuration:

* [Configuring the OMAG Server Platform](../../../open-metadata-implementation/admin-services/docs/user/configuring-the-omag-server-platform.md)

The link below takes you to a task description in the Egeria Administration User Guide.
The user guide describes the REST API call(s) needed to complete the task.
You can choose to type the request into postman, or use the requests already defined in the
`Egeria-admin-services-platform-configuration` Postman collection.

* [Add the Coco Pharmaceuticals platform security connector to the platform](../../../open-metadata-implementation/admin-services/docs/user/configuring-the-platform-security-connector.md)
  Try running the platform origin command again - it should fail with a security error.  Change the `user` variable
  in the Egeria environment from `me` to `garygeeke` and rerun the request.  It will work again because
  `garygeeke` is the user id of the Coco Pharmaceuticals IT infrastructure lead and has permission to run the platform
  commands.

Finally, use the `Egeria-admin-services-platform-configuration` Postman collection to experiment with the
different registered services and and known and active server requests.
These are useful to know as we move to configure servers on the platform.

This is the end of the session on the OMAG Server Platform.
