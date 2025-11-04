<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Defining valid values for your open metadata

The [open metadata types](/types) include attributes that are string values.  These string values give you freedom and flexibility to add the values you want.  However, arbitrary strings can make automation hard, and you may want to set up some more formal definitions of the values that should be used.

Consider the [*Project*](/types/1/0130-Projects) entity type shown below.  

<img src="/services/omvs/valid-metadata/project-type.svg" style="float:left">

In addition to attributes such as *qualifiedName*, *category* and *additionalProperties* inherited from [*Referenceable*](/types/0/0010-Base-Model), this type adds multiple attributes to the properties of a ProjectCharter instance such as:

* *mission*
* *purposes*
* *projectPhase*
* *projectStatus*
* *projectHealth*

The *mission* attribute is likely to be free-form text, laying out the reasons and aspirations behind the project.  However, the *category* and the *purposes* may be used by automated processes - or may trigger people to perform certain tasks.  

Having free-form text in such attributes may lead to errors and misunderstandings if the values are filled out incorrectly.  Therefore, Egeria supports the ability to set up lists of valid values for particular properties in open metadata.

Part of the planning process is to consider which metadata attributes should have restricted values and which can be free-form text. Setting these values up early avoids reworking the metadata values later.

### Predefined valid metadata values

Egeria already includes valid metadata values in it content packs.  They support common technologies in use by most organizations as well as Egeria's solutions.

For example, the `CoreContentPack.omarchive`, which is loaded automatically when the main metadata store is started, includes valid value definitions for the [*deployedImplementationType*](/concepts/deployed-implementation-type), [*fileType*](/concepts/file-type), [*fileName*](/types/2/0220-Files-and-Folders) and [*fileExtension*](/types/2/0220-Files-and-Folders) properties.  These values can be used to control the values stored in these properties.  They are also linked with each other and other metadata elements:

* The *deployedImplementationType* valid values are used to provide an index of connectors, templates and other resources that support specific types of technology.  The [Automated Curation OMVS](/services/omvs/automated-curation/overview) provides an API to query these valid values and the linked resources.

* The *fileType*, *fileName* and *fileExtension* valid values are used by the [file connectors](connectors/#files) that survey and catalog files in the file system.  They allow the known files to classified in various way to increase the insight into the files available to the organization.

These values can be updated and augmented to match the needs of your organization.


--8<-- "snippets/abbr.md"
