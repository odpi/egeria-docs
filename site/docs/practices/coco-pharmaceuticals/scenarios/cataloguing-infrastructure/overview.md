<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cataloguing Infrastructure

[Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) has maintained a list of all the servers used at Coco Pharmaceuticals that are his responsibility.  Individual departments may have bought their own equipment (servers/laptops etc) but he is not responsible for them.

![System Inventory Spreadsheet](gary-geeke-updating-systems-spreadsheet.png)

He has been pleased with this solution since it allows him to:

* List of all machines in his care at each location
* Plan capital for new purchases
* Keep track of software levels on all the machines
* Reorganize the workload when new projects start up

However:

* Maintaining the content - particularly for software levels - was tedious, and sometimes he got behind in cataloguing them.
* It was challenging to share the data with his team
* No automation was possible based off of this information.
* It was not possible to correlate with other teams – such as devOps, security and finance, ...

He decides to add the spreadsheet contents to Egeria to make it easy to manage.  He writes a simple script to load the contents through the [pyegeria](/concepts/pyegeria) API. After experimenting with a number of queries, he discovers that his data was not as consistent as he had thought and starts to clean up the data through the Egeria APIs.

He builds new scripts that populate different spreadsheet structures for his team's projects, and he is able to load any updates they make.

![Gary sees benefits in an online systems inventory](gary-geeke-viewing-lineage.png)

He gained the following benefits:

* Validation of system status was automated, simple check on reports and alerts
* Team freed up from maintaining the spreadsheets for infrastructure projects
* Formalisation of software levels into standard operating platforms reduced variation in system stacks and enabled a systematic upgrade process 

???+ info "Viewing system metadata"
    Gary is able to view the metadata for the systems in his inventory through [The Catalog](/user-interfaces/egeria-ui).
The definition of the governance domains can be seen in [egeria-explorer](/user-interfaces/egeria-explorer/overview) under the **Valid Values** tile, look for the **domainIdentifier** valid value set.  Setting up a new domain is through the [Valid Metadata API](/services/omvs/valid-metadata/overview).

    ![Valid Values for domainIdentifier](domain-identifier-valid-values.png)

Gary is ready to collaborate with [Lemmie Stage](/practices/coco-pharmaceuticals/personas/lemmie-stage) on automating metadata capture during the DevOps pipeline.

--8<-- "snippets/abbr.md"
