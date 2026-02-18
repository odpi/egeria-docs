<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Glossary Author User Interface User Guide

The **Glossary Author** is a UI capability of the Egeria React UI that allows you to author glossary content, such as Glossaries, Terms, Categories
and the relationships between them.

# Concepts

Egeria has subject area open types that are described in [Area 3](https://egeria.odpi.org/open-metadata-publication/website/open-metadata-types/Area-3-models.html). This mature model of glossary content describes the relevant concepts around glossaries.

The Glossary Author exposes concepts (json objects) that map onto the open types. The Glossary Author concepts are intended to make it easier for a 
user interface to author glossaries. 

As metadata is often best thought of as a graph; the Glossary author user interface exposes the concept of a Graph containing only the concepts relevant  to a glossary author. The Graph is composed of Nodes (vertices) and Relationships (edges).  

Glossary, Category and Term are all types of Node. The Node object contains standard Egeria properties including:

* Name - name to be displayed.
* qualified name - readable unique name
* guid - global unique identifier.

Glossary Author Node inheritance model, including the nodes that inherit from Term, Category and Glossary. 
 <img src="./glossary-author-nodes .svg" alt="Glossary author node model" width="200px" />


# Working with the Glossary Author user interface.

## Getting to the Glossary Author start screen
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

## Adding a Glossary
- Add a Glossary using the + button, which will display a wizard to create it. 

## Working with a Nodes
- Navigating back after having created a glossary called 'glossary1' in an empty system will show you a cards of all the glossaries you have
  (one in this case).
- ==List view== You can toggle the card view to show the glossaries as a list
- ==paging== - notice the paging options, these allow you to change the page size (how many are displayed), page through the results if there is more than a page's worth to display.
- ==filter== Entering text into the filter box filters the displayed results. If you want an exact match, check the Exact match flag.   

## Buttons that appear when a node is selected 
- Note that there is a checkbox on the node card; when checked, buttons appear indicating actions you can perform against the selected node:
  - ==QuickTerms== is shown for glossary, to quickly create Terms under the selected glossary
  - ==children== shows the children of the selected node.
  - ==the pen icon== displays an edit screen for the selected node
  - ==the delete icon== deletes the selected node. Glossaries with content cannot be deleted.

## Quick terms
On the quick term screen 
- Press the + button to add extra rows
- Fill in the name and description in the rows
- Press Create Terms on Server button and the terms will be created. Terms without names will show as errors.

## Working with Categories and Terms
Working with Categories and terms, is similar to working with Glossaries, apart from
  - choosing the Term or Category node tab, Terms or Categories can be created, in this case a wizard is displayed which asks the user to choose the glossary in which the term or Category should be created. 
   
## Glossary children
- When the glossary children action is chosen, the categories and terms under that glossary are displayed. 

- By default only top categories are displayed, these are categories that do not have a parent category. If you want to see the all the categories under the glossary then toggle the Top Categories slider to 'All Categories'. 

## Breadcrumb
While navigating, a breadcrumb is created showing how deep the current node is that is being authored. 


## Future improvements
- a breadcrumb to be optimized to minimize the url length.
- add governance classification authoring
- add spine object views
- add collaboration authoring and viewing
- start with a context from the community profile.
 