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

![Postman main window](postman-main-menu.png)

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

![Creating a new Environment 1](postman-create-workspace1.png)
![Creating a new Environment 2](postman-create-workspace2.png)
![Creating a new Environment 3](postman-workspace-created.png)

## Importing Egeria Postman data

We now will

* Individually import the Egeria Postman collections required for this dojo
* Select 'Import' and select 'Link' as the source
* Paste the URL found below for the `Egeria-admin-services-operational` collection

    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-implementation/admin-services/Egeria-admin-services-operational.postman_collection.json
    ```

* Confirm the correct collection will be imported
* Confirm the collection was imported successfully

![Import Begin](postman-collection-import-begin.png)
![Select import source](postman-collection-url.png)
![Confirm Collection to import](postman-collection-importconf.png)
![Confirm imported successfully](postman-collection-importcomplete.png)

* Repeat the same procedure for the following Egeria collections:

    `Egeria-admin-services-platform-configuration`
    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-implementation/admin-services/Egeria-admin-services-platform-configuration.postman_collection.json
    ```
    `Egeria-admin-services-server-configuration`
    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-implementation/admin-services/Egeria-admin-services-server-configuration.postman_collection.json
    ```
    `Egeria-asset-owner-omas`
    ```
    https://raw.githubusercontent.com/odpi/egeria/c31a2b19c3b42da1c2622dbe4ebed958f6a62cb5/open-metadata-implementation/access-services/asset-owner/Egeria-asset-owner-omas.postman_collection.json
    ```
    `Egeria-platform-services`
    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-implementation/platform-services/Egeria-platform-services.postman_collection.json
    ```
    `Egeria-repository-services-local-repository`
    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-implementation/repository-services/Egeria-repository-services-local-repository.postman_collection.json
    ```
    `Egeria-repository-services-metadata-highway`
    ```
    https://raw.githubusercontent.com/odpi/egeria/e256aa1ca99240ac276b584f652cf02382220bf7/open-metadata-implementation/repository-services/Egeria-repository-services-metadata-highway.postman_collection.json
    ```

* Once all collections are imported, your workspace should appear as:

![Show all imported collections](postman-show-imported-collections.png)

We must now import the environment required for this dojo

* Again, select 'Import' and select 'Link' as the source
* Paste the sample environment URL found below

    ```
    https://raw.githubusercontent.com/odpi/egeria/40ec581a8dbf82eeb7e96e2412099358193e8fc1/open-metadata-resources/open-metadata-samples/postman-rest-samples/Egeria.postman_environment.json
    ```

* Confirm the environment to be imported
* Confirm the environment was imported successfully

![No existing environments](postman-environments-empty.png)
![Select environment import source](postman-environment-import-link.png)
![Confirm environment import](postman-environment-confirmation.png)
![Environment imported successfully](postman-environment-import-complete.png)

## Updating Postman settings

Egeria uses secure connections. However the demo environment has self-signed certificates which 
Postman will not see as valid without further configuration. To simplify this process we will 
turn off certificate validation in postman:

* Go to settings
* Ensure 'SSL certificate verification' is switched off

![Select Settings](postman-locate-settings.png)
![Disable certificate validation](postman-settings-options.png)

## Egeria Environment settings

The Import process will have imported some egeria environment settings.

In general you can leave the values as default except for hostnames which should be pointed at the relevant
Egeria platform. Tutorial content will walk you through this explicitly.

* Make the egeria environment the default in this workspace

![Select Egeria environment](postman-env-switch.png)
![Edit Egeria environment](postman-env-find-quicklook.png)
![View and edit environment values](postman-env-quicklook-view.png)

## Finished!

Postman is now ready to be used with egeria. Refer back to the tutorials for specific
examples, or experiment!

Instructions for contributing new Postman collections
are located in the [developer-resources :material-dock-window:](/guides/contributor/guidelines/#postman-artifacts-for-apis){ target=docs} .

--8<-- "snippets/abbr.md"
