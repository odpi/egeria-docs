<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Subject Areas

!!! example "Back at the bus company ..."
    The new focus on ensuring bus timetable information is accurate and available has created an increase in passengers for the bus company.  The assistant who is responsible for managing and disseminating the bus timetable information is not happy, however.  What should be a simple task is tedious and complicated because each form of the timetable (at the bus stop, internet download, printed timetables) are each using a different format.  For example, the master timetable and the timetables for the bus stop are in 24-hour clock, whereas the internet downloadable timetable and the printed timetable use am/pm.  This means the assistant has to translate the bus times from one format to another in order to publish a new set of timetables.  Similarly, the names of the bus stops are not consistent across the different formats.  The assistant realizes that some form of standardization is needed so that the different formats can be created automatically from the master timetables.  Otherwise, they are going to look for a new job! 

Using standard formats, names and meanings for resources, such as data, is critical to ensure they can be shared and reused for multiple purposes.  Open metadata provides the means to describe these standards and used them to create consistency across all copies, formats and uses.
The effort required to author and maintain a these standards, plus the governance processes required to ensure they are used wherever appropriate, is offset by the savings in managing and using the resources associated with the subject area.

**Recap:** 

* [Subject Areas](/concepts/subject-area) define the standards for your resources and their use. They cover resources that are widely shared across the organization and there is business value in maintaining consistency.
* Each subject area has an owner who is responsible for coordinating the development and maintenance of the subject area's materials.
* [Digital Resources](/concepts/digital-resource) that are managed using the subject area's materials are said to be part of the subject area's "domain".  This is called the *Subject Area Domain* and is synonymous with *Data Domain* - although since a subject area domain may manage resources that are not just data assets (such as systems and infrastructure), open metadata uses a more generic name.

--8<-- "docs/practices/common-data-definitions/semantic-to-implementation.md"


??? education "Defining subject areas in Egeria"

    - The [Subject Area](/services/omvs/subject-area/overview) API provides support for the definition of subject areas and the ability to retrieve details of the materials that are part of the subject area.
    - The [Defining Subject Areas scenario](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview/) for Coco Pharmaceuticals walks through the process of setting up.  


??? education "Coco Pharmaceuticals Scenarios"
    There are descriptions of creating glossaries and other materials for subject areas in the [Coco Pharmaceuticals Scenarios](/practices/coco-pharmaceuticals/scenarios/overview).

