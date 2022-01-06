<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Server Author User Interface User Guide

The **Server Author** is a UI capability of the Egeria React UI that allows you to author OMAG Servers. OMAG serves are defined using configuration. This 
User Interface allows servers of different types to be authored.  

# Concepts

# Working with the Glossary Author user interface.

Note the screenshots might be slightly out of date with the code base, but hopefully help orientate the reader. 

## Getting to the Server Author start screen
- After logging into the Egeria react UI, you will see tasks at the left hand side of the user interface including the glossary author task.
<img src="leftnav.png" alt="Left hand side of the user interface" width="200px" width="200px" height="200px" />
- If you see a screen with a connect button like this <img src="connect.png" alt="connect button"  width="70px" height="40px" /> then the glossary author is not able to issue a successfully glossary call; this is caused by either
   - the Subject Area OMAS is not active, so the glossary author cannot call it
   - the glossary author view is not configured on the view server.
   - the presentation server is not configured to point to the glossary server view service.   
   If everything is correctly configured but the view server or its downstream server is not started then, start them and press the connect button.  
- Assuming you have successfully connected, then you are now in a position to author glossary content and should see
<img src="emptystartscreen.png" alt="Empty start screen" width="350px" height="100px" />  
- You will notice that you can choose the node to work with using the node tabs
<img src="nodetabs.png" alt="Node Tabs" width="350px" height="20px" /> 

## List of Servers

## Create a server

