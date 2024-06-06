<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring the presentation server

The [presentation server](/concepts/presentation-server) can be implemented with any webserver technology that is able to act as a reverse proxy and host the Javascript static content needed gor Egeria's [General User UI](/user-interfaces/general/overview).  In these instructions we are using [NGINX](https://nginx.org/en/).

??? tip "Installing nginx"
    On macOS, nginx can be installed using [Homebrew](https://brew.sh/) with the following command: `brew install nginx`


## Managing the Javascript static content

### Downloading

Egeria's UI static content is located in [https://github.com/odpi/egeria-ui](https://github.com/odpi/egeria-ui).

```shell
git clone https://github.com/odpi/egeria-ui.git
```
This creates a new directory called `egeria-ui`
```shell
cd egeria-ui
```
### Building

The content is built using the Node Package Manager (NPM) version 16.13.0.

??? tip "Installing NPM"
    On macOS, npm can be installed using [Homebrew](https://brew.sh/) with the following command: `brew install npm`.
    You also need to install the Node Version Manager (NVM) to move NPM back to version 16.13.0. (Use `brew install nvm` and follow the instructions to complete the install).

First, ensure all of your packages are up to date on your local machine:

```shell
 npm install npm@8.1.0

```
Then run the following command and the static content is built in `build`
```shell
npm run build
```
You can then copy the contents of `build` to where you want nginx to retrieve it from


--8<-- "snippets/abbr.md"