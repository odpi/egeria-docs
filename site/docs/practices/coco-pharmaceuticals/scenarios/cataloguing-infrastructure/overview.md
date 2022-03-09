<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cataloguing Infrastructure

[Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) has maintained a list of all of the servers used at Coco Pharmaceuticals that are his responsibility.  Individual departments may have bought their own equipment (servers/laptops etc) but he is not responsible for them.

![System Inventory Spreadsheet](cataloguing-infrastructure-system-inventory-spreadsheet.svg)

He has been pleased with this solution since it allows him to:

* List of all machines in his care at each location
* Plan capital for new purchases
* Keep track of software levels on all of the machines
* Reorganize workload when new projects start up

However:

* Maintaining the content - particularly for software levels - was tedious and sometime he got behind in cataloguing them.
* It was difficult to share with team
* No automation possible based off of this information.
* It was difficult to correlate with other processes - dev ops, auditing, ...

He decides to add the spreadsheet contents to Egeria to make it easy to manage.  He writes a simple script to load the contents through the [IT Infrastructure OMAS](/services/omas/it-infrastructure/overview). After experimenting with a number of queries, he discovers that his data was not as consistent as he had thought and starts to clean up the data through the Egeria APIs.

He builds new scripts that populate different spreadsheet structures for his team's projects and are able to load any updates they make.

He saw the following benefits:

* Validation of system status was automated, simple check on reports and alerts
* Team freed up from maintaining the spreadsheets for infrastructure projects
* Formalisation of software levels into standard operating platforms reduced variation in system stacks and enabled a systematic upgrade process 

Gary is ready to collaborate with [Bob Nitter](/practices/coco-pharmaceuticals/personas/bob-nitter) and [Polly Tasker](/practices/coco-pharmaceuticals/personas/polly-tasker) on automating metadata capture during the DevOps pipeline.

--8<-- "snippets/abbr.md"
