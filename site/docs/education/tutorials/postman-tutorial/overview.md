<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# Postman

Postman provides an interactive application for issuing [REST APIs :material-dock-window:](https://en.wikipedia.org/wiki/Representational_state_transfer){ target=wp } calls to a server and reviewing responses.

Basically a REST API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data.  The call is made using a URL - just like requesting a web page from your browser.  In fact, when you request a web page from your browser, the browser is issuing a GET HTTP request for the page.

REST APIs for services such as the open metadata and governance services of Egeria use the full range of HTTP requests as follows:

* **GET** - retrieving simple structures.
* **POST** - creating, updating, deleting complex structures and retrieving long lists of information with paging.
* **DELETE** - deleting simple structures.

With Postman it is possible issue these HTTP requests and experiment with what they do.
The Egeria dojos use Postman *collections* to illustrate the calls and save you typing in the full URLs (which can be quite long :).

Egeria by default uses https:// requests with a self-signed certificate. Any Postman users therefore will need to
go into settings->general and turn off 'SSL certificate verification' or requests will fail.

## Setting up Postman 

Postman is a [free download :material-dock-window:](https://www.getpostman.com/){ target=pm } with optional enterprise licenses for teams.  It includes a wide variety of [tutorials :material-dock-window:](https://learning.getpostman.com/concepts/){ target=pm } to help you go from novice to expert.  Familiarity with Postman will help you get the most value from the Egeria tutorials.

Install Postman from [the Postman downloads site :material-dock-window:](https://www.getpostman.com/downloads/){ target=pm }. At the time of writing 5.9.0 is  current and recommended.

Once Postman is installed, start up the application.  You should see an initial page something like this:

![Postman main window](postman-mainmenu.png)

## Setting up Postman with Egeria data

We will import two types of information from Egeria's code repository on GitHub:
* Environments - these define the values of replaceable variables in the API calls, such as host and server names.
* Collections - these define the REST API calls to issue.

Follow through these steps to configure your Postman environment:

## Create a new workspace

Creating a workspace for egeria helps keep everything we'll work with together. If you mess up your
postman files later, you can just create a new environment again to work with

Select the workspace menu at the top of the Postman interface, and create a new one
called 'Egeria dojo':

![Creating a new Environment 1](postman-workspace1.png)
![Creating a new Environment 2](postman-workspace2.png)
![Creating a new Environment 3](postman-workspace3.png)

## Importing Egeria Postman data

We now will
* Select 'Import' and select 'GitHub' as the source
* Authenticate as required
* Select the odpi/egeria repository on GitHub
* Import all the Postman data found

![Import Begin](postman-import-begin.png)
![Select import source](postman-import-coderepo.png)
![Auth with GitHub](postman-import-gotogh.png)
![Select egeria repo](postman-import-ghrepo.png)
![Select what to import](postman-import-select.png)
![After Import](postman-import-after.png)

## Updating Postman settings

Egeria uses secure connections. However the demo environment has self-signed certificates which 
Postman will not see as valid without further configuration. To simplify this process we will 
turn off certificate validation in postman:

* Go to settings
* Ensure 'SSL certificate verification' is switched off

![Select Settings](postman-settings-select.png)
![Disable certificate validation](postman-settings-change.png)

## Egeria Environment settings

The Import process will have imported some egeria environment settings.

In general you can leave the values as default except for hostnames which should be pointed at the relevant
Egeria platform. Tutorial content will walk you through this explicitly.

* Make the egeria environment the default in this workspace

![Select Egeria environment](postman-env-select.png)
![Edit Egeria environment](postman-env-editselect.png)
![View and edit environment values](postman-env-edit.png)

## Finished!

Postman is now ready to be used with egeria. Refer back to the tutorials for specific
examples, or experiment!

Instructions for contributing new Postman collections
are located in the [developer-resources :material-dock-window:](/egeria-docs/guides/contributor/guidelines/#postman-artifacts-for-apis){ target=docs} .

--8<-- "snippets/abbr.md"
