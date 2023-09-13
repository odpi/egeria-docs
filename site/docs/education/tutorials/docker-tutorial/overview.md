<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Docker tutorial

**Docker** is a [simple container runtime and standard](https://www.docker.com/why-docker).

Every time the egeria Pull Request (PR) build runs, it creates a **latest** docker image of egeria based on the latest content of the `main` branch of [egeria.git](https://github.com/odpi/egeria) and pushes it to the docker catalog on the [Docker website](https://hub.docker.com/r/odpi/egeria).  The site also contains docker images for each official release of egeria.  

Alternatively, you can build a customized docker image of egeria, that includes or excludes the connectors and services that you need.

This page takes you through the different options for building and running egeria using docker containers.

## Building your own docker image

--8<-- "snippets/tasks/task-building-customized-docker-image.md"


## Using the standard docker container on docker hub

This docker image provides a simple way to bring a runnable version of Egeria onto your machine.  It also provides the basis for a [Kubernetes](/guides/operations/kubernetes) deployment of Egeria.

The docker catalog page for egeria is at [https://hub.docker.com/r/odpi/egeria](https://hub.docker.com/r/odpi/egeria). The **Overview** tab describes the docker container.

![Egeria Docker Page Overview Tab](egeria-docker-page-overview.png)

The **Tags** tab shows the different releases that are available.

![Egeria Docker Page Tags Tab](egeria-docker-page-tags.png#pagewidth)

----

### Getting the docker runtime

The docker image needs a runtime to execute.  It can run in the cloud using **Docker Hub** or
on your machine using the **Docker Desktop**. 
The description below describes how to use the docker desktop.

Docker Desktop supports running a docker image as a standalone container, or as part of group of containers started with **docker-compose**.

Go to the [Docker website](https://www.docker.com/why-docker) and select the **Download Docker Desktop**.

![DockerHub home page](docker-homepage.png#pagewidth)

Follow the instructions for you operating system.  For macOS, the docker desktop
is installed like a standard application.

![macOS install of docker desktop](docker-desktop-install.png)

Once it is installed, it can be launched like any
application, such as through the launchpad/start menu.


This tutorial explains how to use the Egeria Docker Image published to the
docker catalog at [https://hub.docker.com/r/odpi/egeria](https://hub.docker.com/r/odpi/egeria).

Egeria's docker image includes the Egeria install image.  When the image is started
using docker, a new egeria docker container is created.  As it starts up, an instance of
the Egeria runtime - that is the
[OMAG Server Platform](/concepts/omag-server-platform) -
is started at port https 9443.

This container can be incorporated into larger container orchestration environments or used standalone.
This tutorial describes how to use it standalone.  The [Open Metadata Labs](/education/open-metadata-labs/overview)
use this container with `Kubernetes`
container services to create a complete open metadata solution.
Link to [Open Metadata Labs](/education/open-metadata-labs/overview) to learn more.

## Working with Egeria's docker image

Once the docker desktop is installed, start the docker desktop application.
It may take a little while to complete its start up so check it is running before continuing.

For example, on macOS, the docker desktop can be found on the **Launchpad**. Once it is running,
the docker whale icon appears on the top menu bar.  Clicking on the docker whale icon reveals a menu
and the status of the desk top is visible. 
This menu is used to shut down docker at the end of the dojo.

![macOS running Docker desktop](docker-desktop-running.png)

----

## Downloading the egeria docker image

The command to download Egeria's docker image is `docker pull odpi/egeria`.
This is issued from a command/terminal window in the directory where you want the
container to be copied to.

If you see the following response, then the docker runtime is not installed properly on your machine.

```bash
$ docker pull odpi/egeria
-bash: docker: command not found
```

If all is well, the image downloads.  Notice it is pulling the latest main build by default.

```bash
$ docker pull odpi/egeria
Using default tag: latest
latest: Pulling from odpi/egeria
e7c96db7181b: Pull complete 
f910a506b6cb: Pull complete 
b6abafe80f63: Pull complete 
a83b87485b54: Pull complete 
10d9ee7d5688: Pull complete 
9558171b7a95: Pull complete 
Digest: sha256:18451a4676a6688e03f284f887ba5be7026c17805ee0b919ed02cb131621d45b
Status: Downloaded newer image for odpi/egeria:latest
docker.io/odpi/egeria:latest
$
```
To check it will run, try the `docker run --publish 19443:9443 odpi/egeria`.
This will start the image as a new docker container.  As the container initializes it starts a single copy of the
[OMAG Server Platform](/concepts/omag-server-platform).
The OMAG Server Platform is the Egeria runtime platform where the Egeria REST services run.

The `--publish 19443:9443` parameter maps the 9443 port inside the docker that the OMAG Server Platform
has registered with to port 19443

![Docker container structure](docker-container-overview.png)

You should see the server logo come up and finally a message 
`OMAG server platform ready for more configuration`.  This message means it has successfully started.

Once you can see that it has started, use `Control-C` to stop it.

```bash
$ docker run --publish 19443:9443 odpi/egeria
Picked up JAVA_TOOL_OPTIONS: 
 ODPi Egeria
    ____   __  ___ ___    ______   _____                                 ____   _         _     ___
   / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
  / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
 / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
 \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/

 :: Powered by Spring Boot (v2.3.0.RELEASE) ::

10:12:28.047 [main] INFO  o.s.b.w.e.tomcat.TomcatWebServer - Tomcat initialized with port(s): 9443 (https)
10:12:41.688 [main] INFO  o.s.b.w.e.tomcat.TomcatWebServer - Tomcat started on port(s): 9443 (https) with context path ''

Thu Jun 04 10:12:32 BST 2020 No OMAG servers listed in startup configuration
Thu Jun 04 10:12:41 BST 2020 OMAG server platform ready for more configuration
^C
$
```

# Working with the Docker Desktop Dashboard

The docker desktop **dashboard** makes it easy to control your docker containers.
It is started from the docker desktop menu.  Select the `Dashboard` option.
You will see something like this:

![Docker Desktop initial view](docker-container-down.png)

Each time a new docker container is created, it is given a generated name.
In the example above the name is `gifted-lovelace` which is a great tribute to
[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace).

You can see that the container is not running (`EXITED`) because you stopped it earlier with `Control-C`.

Hover your mouse pointer over the container entry and some options appear.

![Docker Desktop initial view](docker-container-start-options.png)

The triangular "START" button is to start the container running again and the Bin/Trash can is to delete your container.
Press the "START" button to start your container again.

When the container is running, more options are available to you when you hover the mouse over the container entry.

![Docker Desktop initial view](docker-container-running.png)

The first symbol is the "OPEN IN BROWSER" option.  Click on it and your browser opens.  You should see an error displayed:


![White label error](docker-container-open-in-browser-error.png)

Update the URL as follows:

![Correct URL](../swagger-tutorial/swagger-ui-url.png)

and press enter.  After a few moments, Egeria's Swagger page should open.  This is an automatically
generated page that describes the REST APIs of Egeria's OMAG Server Platform.
There is more information on swagger in the [Swagger Tutorial](/education/tutorials/swagger-tutorial/overview).

![Top if Swagger Page](../swagger-tutorial/swagger-ui-top.png)

Page down until you see the "Platform Services".  The platform services provide support for
administrators running Egeria.

![Platform Services Entry on Swagger page](../swagger-tutorial/swagger-ui-platform-services.png)

Click on the angle bracket on the right hand end of the entry and the list of REST API operations
is displayed.

![Platform Services detail on Swagger page](../swagger-tutorial/swagger-ui-platform-services-detail.png)

Now click on the first blue entry for platform origin. Then press the `Try it Out` button.

![Try it out button on Swagger page](../swagger-tutorial/swagger-ui-try-it-out-button.png)

and enter `garygeeke` in the `userId` field and then the `Execute` button.

![Platform Origin execution on Swagger page](../swagger-tutorial/swagger-ui-platform-origin-execution.png)

You can see that through the Swagger UI it is possible to try out different REST requests and make sure the
platform is operating correctly.    The platform origin request is particularly useful for verifying
what version of the OMAG Server Platform is running.

The Swagger UI is useful for ad hoc testing.
However, later in the Dojo we will cover a tool called [Postman](/education/tutorials/postman-tutorial/overview)
that provides a more powerful testing experience.

So back to the Docker Desktop.  The second option on the docker desktop is "CLI".  

![Docker Desktop running view](docker-desktop-running-options.png)


This opens the Terminal/Command
window **inside the docker container**.  You are in the home directory of the OMAG Server Platform.
This contains the contents of the egeria install image.  It is also the home directory of
the OMAG Server Platform which is where it will write its files.  Type `ls` to list the files.

```bash
$ ls
LICENSE            clients            server             utilities
NOTICE             conformance-suite  user-interface
$
```
Only the files from the install image are present because we have not asked the OMAG Server Platform to do
anything yet.  However, as we configure servers and run them, you will see new files appearing.
You can check back here from time to time to see the files accumulating.
If you delete this container then all of the files that the OMAG Server Platform created are lost.

(If you want to know more about the egeria install image, see the
[Installing Egeria Tutorial](/education/tutorials/installing-egeria-tutorial).)

The third button on the docker desktop is the "STOP" button and the fourth button is "RESTART".
If you just need to test these buttons, remember to ensure that the docker container is running
when you have finished because it is needed for the rest of the session.

![Docker Desktop running view](docker-desktop-running-options.png)

The final button is "DELETE".  As described above, it deletes the container and uoi need to start again with
`docker run --publish 19443:9443 odpi/egeria`.

If you now click on the whitespace of the container's entry, a new section opens up with 3 tabs.

"Logs" shows the console logs. Each new run of the container appends new log information to the end of this console.

![Docker Container logs](docker-container-logs.png)

"Inspect" shows the settings for the container.

![Docker container settings](docker-container-inspect.png)

"Stats" shows the resource usage of the container.

![Docker container stats](docker-container-stats.png)

... and that is all you need to know about docker.

----


---8<-- "snippets/abbr.md"

