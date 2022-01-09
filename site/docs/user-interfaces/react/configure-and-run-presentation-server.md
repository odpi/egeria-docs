<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Setup

If you are following the [checklist](react-ui-planning-checklist.md) you should have completed the following checked tasks before proceeding.

- [x] [Plan](../../planning/guide/) your Egeria topology- including how many platforms, how many servers, cohort and connectors
- [x] [Plan your UI](react-ui-planning-checklist.md) which UI capabilities you require.
- [x] Start Egeria platform(s)
- [x] [Configure metadata server platform](../../admin/configuring-the-omag-server-platform) if required (some of the Kubenetes images already configure a metadata server platform)
- [x] [Configure and start metadata access store server](../../admin/servers/configuring-a-metadata-access-store)  if required (some of the Kubenetes images already configure a metadata access store server)
- [x] [Configure and start view services](../../admin-services/view-server)  for each of the UI capabilities you require. The name of the UI capability is the same as the name of the view service.
- [ ] *Configure and run the presentation server by following the below instructions*
- [ ] Validate that the presentation server is running as expected.

This page describes the steps required to configure and run the presentation server.

## 1. Download the Egeria React user interface code

Start by downloading the Egeria React User Interface into a folder on your machine. <p>
Either

* Download the <a href="https://github.com/odpi/egeria-react-ui/releases/latest" target="_blank">Latest Release</a>.
The released user interface is supplied in an archive, containing the source code as a <code>zip</code> file and a <code>tar.gz</code> file, which you need to extract.
* <code>git clone</code> the repository using the instructions under the Code button at <a href="https://github.com/odpi/egeria-react-ui" target="_blank">Latest code </a>
  
You now should have a folder on your machine with the Egeria React User Interface code extracted.

## 2. Set the presentation server environment variable

The presentation server is the node application for the user interface. It serves the web pages, proxies the rest calls and handles the login.
For a particular tenant the presentation server needs to know which back end server to send requests to. This information is supplied in an
environment variable(s).

The environment variable is:

<code>EGERIA_PRESENTATIONSERVER_SERVER_\<localServerName\>={"remoteServerName":"\<remoteServerName\>","remoteURL":"\<remoteURL\>"}</code>

where

<code><localServerName\></code> should be replaced with the local server name. This segment is the start segment of the url that the browser sends.

<code><remoteServerName\></code> should be replaced with the remote server name. This is the name of the view service that has been configured in the view server.

<code><remoteURL\></code> should be replaced with the remote server URL. This is the URL of the view service.

Since this environment variable is typically handled by the shell and includes a json fragment, when setting it you need to be sure
to 'escape' quotation characters, so you would type:

```bash
EGERIA_PRESENTATIONSERVER_SERVER_aaa="{\"remoteServerName\":\"cocoView1\",\"remoteURL\":\"https://localhost:9443\"}"
```
We can see this is set as we expect
```
$ echo $EGERIA_PRESENTATIONSERVER_SERVER_aaa
{"remoteServerName":"cocoView1","remoteURL":"https://localhost:9443"}
```
To get an initial environment up-and-running just download the `truststore.p12`
file from: [https://github.com/odpi/egeria/raw/master/truststore.p12](https://github.com/odpi/egeria/raw/master/truststore.p12).

??? question "Transport-level security"
    The [truststore.p12](https://github.com/odpi/egeria/raw/master/truststore.p12)
    file provides a local truststore for Java. This allows the self-signed certificate embedded
    within the server chassis (by default) to be trusted.

    Without this trust, interactions with the server chassis (such as the REST calls that are made
    through Java to handle interaction between the chassis and the connector) will result in an
    `SSLHandshakeException`.

    While this `truststore.p12` file allows SSL-encrypted communication, the fact that
    it relies on a self-signed certificate means that there is no independent source of trust
    in the interactions (which would typically be achieved through an independent Certificate
    Authority).

    Additional details on TLS for Egeria can be found in [the Egeria documentation](../../concepts/omag-server.html).

## 3. Running the presentation server 
To run on a different machine, copy over the cra-client and cra-server/build folders, maintaining their relative locations to the target machine.

Once you have the code where you want to run it:
<ol>
  <li>Navigate to the <code>cra-client</code> folder and run <code>npm install</code></li>
  <li>Navigate to the <code>cra-server</code> folder and run <code>npm install</code></li>
</ol>


=== "In production mode"
    To run the presentation server in production mode, the javascript and resources need to be [minified](https://reactjs.org/docs/optimizing-performance.html).
    <ol> 
    <li>Navigate into <code>cra-client</code>, then run  <code>npm run build</code>. The cra-client folder now should contain a <code>build</code> folder containing the artifiacts to run in production.</li>  
    <li>Run <code>npm run prod</code> in the <code>cra-server folder</code>.</li>
    </ol>
=== "In development mode"
     <ol> 
     <li> Navigate into <code>cra-server</code> and run <code>npm start</code>. </li>
     <li>After a couple of minutes while it builds, for tenant aaa, you should be able to login. </li>
     </ol>


## 4. Demo login 

If you have used the sample environment variables and are using the  <a href="https://egeria.odpi.org/open-metadata-resources/open-metadata-tutorials/egeria-dojo/">Egeria Dojo setup</a>, then you can login as follows.  

In your web browser go to <code>https://localhost:9443/aaa/ </code>  Replace host/port accordingly

* In this example `aaa` is the tenant name we used above when defining the environment variable
* The trailing / is currently required to allow the login page to load

For ecosystem tools use user 'garygeeke' and password 'admin'.
For glossary author use user 'faithbroker' and password 'admin'.


## 5. SSL configuration
By default the Egeria React UI uses a truststore.p12 and keystore.p12 files for ssl. The p12 files are copies of files [https://github.com/odpi/egeria/blob/master/keystore.p12](https://github.com/odpi/egeria/blob/master/keystore.p12) and [https://github.com/odpi/egeria/blob/master/truststore.p12](https://github.com/odpi/egeria/blob/master/truststore.p12), which are the definitive sources of these files. The keystore and truststore files allow Egeria to run simply in a demo/development; this is not appropriate for production, which should be appropriately secured.     
