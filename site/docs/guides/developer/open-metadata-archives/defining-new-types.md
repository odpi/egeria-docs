<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Defining new types

Egeria supports a [wide variety of open metadata types](/types) that cover a broad range of metadata.  These types can be extended through the normal contribution process of the Egeria project.   It is also possible to create your own type definitions that can be exchanged across the [open metadata repository cohort](/concepts/cohort-member) and may also be maintained through Egeria's APIs using [extended properties](/parameters/overview/#typename-and-extendedproperties).

Type definitions need to be governed because they must be consistent across a cohort - during the whole time that one or more instances of the type are stored in the repositories.

## Dynamic definitions of types not recommended

Egeria does have APIs for dynamically defining types (for example, the `addTypeDef` operation of the [Metadata Expert](/services/omvs/metadata-expert/overview) view service), but it is recommended that you only use them when experimenting with types and instances.  Instead, you should manage your types in an [open metadata archive](/concepts/open-metadata-archive) that is loaded in the [metadata access servers](/concepts/metadata-access-server) during [each server start up](/guides/admin/servers/by-section/repository-services-section).

## Creating your own type archive

A type archive is created using a Java program that uses the [repository services archive utilities :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-archive-utilities){ target=gh } to add your new type definitions to an open metadata archive file.  This is the same approach that Egeria uses for its own [open metadata types](/types) (see [how the open metadata types archive is structured](#how-the-open-metadata-types-archive-is-structured) below).

Begin by setting up your build file - this is an example using Gradle, modelled on the build file of the [coco-metadata-archives :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/sample-metadata/coco-metadata-archives){ target=gh } module.  Egeria's libraries are published to Maven Central with the group `org.odpi.egeria`, so the same dependencies can be used from Maven.  The Java class where the `main()` method is located is `org.odpi.openmetadata.samples.archiveutilities.types.CocoTypesArchiveWriter` in this example.

??? example "Build file"
    ```groovy
    /*
     * SPDX-License-Identifier: Apache-2.0
     */

    plugins {
        id 'java'
        id 'application'
        id 'com.gradleup.shadow' version '9.6.1'
    }

    description = 'Builds the open metadata type archive for my extended types.'

    def egeriaVersion = '6.2'   // the Egeria release you are building against

    repositories {
        mavenCentral()
    }

    dependencies {
        implementation "org.odpi.egeria:repository-services-apis:${egeriaVersion}"
        implementation "org.odpi.egeria:repository-services-archive-utilities:${egeriaVersion}"
        implementation "org.odpi.egeria:open-metadata-types:${egeriaVersion}"
        implementation "org.odpi.egeria:content-pack-helpers:${egeriaVersion}"   // for ArchiveVersionStabilizer
    }

    application {
        mainClass = 'org.odpi.openmetadata.samples.archiveutilities.types.CocoTypesArchiveWriter'
    }

    shadowJar {
        archiveClassifier = 'jar-with-dependencies'
    }
    ```

The next example shows the code to build four new types:

* *BiopsyScope* - An EnumDef that holds an enumeration.
* *BiopsyReport* - An EntityDef describing a new type of entity.
* *BiopsySupportingEvidence* - A RelationshipDef describing a type of relationship that links the biopsy report to a Referenceable element that describes the subject of the report.
* *ReviewedByClinicalTrials* - A ClassificationDef that describes a new classification that indicates an element has been reviewed by the clinical trials team.  It captures details about the reviewer and their findings.

There are three main components.  A builder (`OMRSArchiveBuilder`) that constructs the archive in memory; a helper (`OMRSArchiveHelper`) that constructs each element for the archive; and a writer (a subclass of `OMRSArchiveWriter`) that first calls the builder to extract the content and then writes it to a file in JSON.

The open metadata types archive is passed to the builder as a dependent archive.  This is what allows `archiveBuilder.getEntityDef("Document")` to find the supertype of the new `BiopsyReport` entity type, and the `Referenceable` and `Asset` types used by the new relationship and classification.

??? example "Java program to build new types"
    ```java
    /* SPDX-License-Identifier: Apache-2.0 */
    /* Copyright Contributors to the ODPi Egeria project. */
    package org.odpi.openmetadata.samples.archiveutilities.types;
    
    import org.odpi.openmetadata.opentypes.OpenMetadataTypesArchive;
    import org.odpi.openmetadata.repositoryservices.archiveutilities.OMRSArchiveWriter;
    import org.odpi.openmetadata.repositoryservices.archiveutilities.OMRSArchiveBuilder;
    import org.odpi.openmetadata.repositoryservices.archiveutilities.OMRSArchiveHelper;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore.properties.OpenMetadataArchive;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore.properties.OpenMetadataArchiveType;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.ClassificationDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.ClassificationPropagationRule;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.EntityDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.EnumDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.EnumElementDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.RelationshipDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.RelationshipEndCardinality;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.RelationshipEndDef;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.TypeDefAttribute;
    import org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.properties.typedefs.TypeDefLink;
    import org.odpi.openmetadata.samples.archiveutilities.ArchiveVersionStabilizer;
    
    import java.io.File;
    import java.util.ArrayList;
    import java.util.Date;
    import java.util.List;
    
    
    /**
     * CocoTypesArchiveWriter creates a physical open metadata archive file containing
     * the additional specialized types needed by Coco Pharmaceuticals.
     */
    public class CocoTypesArchiveWriter extends OMRSArchiveWriter
    {
        private static final String cocoTypesArchiveFileName = "CocoTypesArchive.omarchive";
    
        /*
         * This is the header information for the archive.
         */
        private static final String                  archiveGUID        = "50874908-01f1-47e2-83ea-e571109a946e";
        private static final String                  archiveName        = "CocoTypes";
        private static final String                  archiveLicense     = "Apache 2.0";
        private static final String                  archiveDescription = "Specialized types for Coco Pharmaceuticals.";
        private static final OpenMetadataArchiveType archiveType        = OpenMetadataArchiveType.CONTENT_PACK;
        private static final String                  originatorName     = "Egeria Project";
        private static final Date                    creationDate       = new Date(1639984840038L);
    
        /*
         * Specific values for initializing TypeDefs
         */
        private static final long   versionNumber = new Date().getTime();
        private static final String versionName   = "1.0";
    
    
        private final OMRSArchiveBuilder archiveBuilder;
        private final OMRSArchiveHelper  archiveHelper;
    
        /**
         * Default constructor initializes the archive.
         */
        public CocoTypesArchiveWriter()
        {
            List<OpenMetadataArchive> dependentOpenMetadataArchives = new ArrayList<>();
    
            /*
             * This value allows the Coco Types to be based on the existing open metadata types
             */
            dependentOpenMetadataArchives.add(new OpenMetadataTypesArchive().getOpenMetadataArchive());
    
            this.archiveBuilder = new OMRSArchiveBuilder(archiveGUID,
                                                         archiveName,
                                                         archiveDescription,
                                                         archiveType,
                                                         originatorName,
                                                         archiveLicense,
                                                         creationDate,
                                                         dependentOpenMetadataArchives);
    
            this.archiveHelper = new OMRSArchiveHelper(archiveBuilder,
                                                       archiveGUID,
                                                       originatorName,
                                                       creationDate,
                                                       versionNumber,
                                                       versionName);
        }
    
    
        /**
         * Create an enum type that can be used as a type of attribute in an entity, relationship or classification.
         * It defines a set of values that the attribute can be set up with along with a default value.
         *
         * @return enum attribute type definition (EnumDef)
         */
        private EnumDef getBiopsyScopeEnum()
        {
            final String guid            = "fdb05618-d0fe-4725-946f-138ba74f6f43";
            final String name            = "BiopsyScope";
            final String description     = "Defines scope of the tissue removal for a biopsy.";
            final String descriptionGUID = null;
    
            EnumDef enumDef = archiveHelper.getEmptyEnumDef(guid, name, description, descriptionGUID);
    
            ArrayList<EnumElementDef> elementDefs = new ArrayList<>();
            EnumElementDef            elementDef;
    
            final int    element1Ordinal         = 0;
            final String element1Value           = "Unclassified";
            final String element1Description     = "There is no information on the scope of the biopsy.";
            final String element1DescriptionGUID = null;
    
            elementDef = archiveHelper.getEnumElementDef(element1Ordinal,
                                                         element1Value,
                                                         element1Description,
                                                         element1DescriptionGUID);
            elementDefs.add(elementDef);
            enumDef.setDefaultValue(elementDef);
    
            final int    element2Ordinal         = 1;
            final String element2Value           = "Excisional";
            final String element2Description     = "The biopsy removed all of the suspicious tissue.";
            final String element2DescriptionGUID = null;
    
            elementDef = archiveHelper.getEnumElementDef(element2Ordinal,
                                                         element2Value,
                                                         element2Description,
                                                         element2DescriptionGUID);
            elementDefs.add(elementDef);
    
            final int    element3Ordinal         = 2;
            final String element3Value           = "Incisional";
            final String element3Description     = "The biopsy took a sample of the tissue under examination.";
            final String element3DescriptionGUID = null;
    
            elementDef = archiveHelper.getEnumElementDef(element3Ordinal,
                                                         element3Value,
                                                         element3Description,
                                                         element3DescriptionGUID);
            elementDefs.add(elementDef);
    
            final int    element99Ordinal         = 99;
            final String element99Value           = "Other";
            final String element99Description     = "Another biopsy scope.";
            final String element99DescriptionGUID = null;
    
            elementDef = archiveHelper.getEnumElementDef(element99Ordinal,
                                                         element99Value,
                                                         element99Description,
                                                         element99DescriptionGUID);
            elementDefs.add(elementDef);
    
            enumDef.setElementDefs(elementDefs);
    
            return enumDef;
        }
    
    
        /**
         * Create the type definition for BiopsyReport.
         *
         * @return entity type definition (EntityDef)
         */
        private EntityDef getBiopsyReportEntity()
        {
            final String guid = "78479770-79ae-4bd8-b0ec-bf5e60c01e66";
    
            final String name            = "BiopsyReport";
            final String description     = "Results from a patient biopsy.";
            final String descriptionGUID = null;
    
            final String superTypeName = "Document";
    
            EntityDef entityDef = archiveHelper.getDefaultEntityDef(guid,
                                                                    name,
                                                                    this.archiveBuilder.getEntityDef(superTypeName),
                                                                    description,
                                                                    descriptionGUID);
    
            /*
             * Build the attributes
             */
            List<TypeDefAttribute> properties = new ArrayList<>();
            TypeDefAttribute       property;
    
            final String attribute1Name            = "biopsyScope";
            final String attribute1Description     = "Is this biopsy excisional (targeted removal) or incisional (sample taken).";
            final String attribute1DescriptionGUID = null;
            final String attribute2Name            = "biopsyTechniqueType";
            final String attribute2Description     = "How was the biopsy taken?";
            final String attribute2DescriptionGUID = null;
    
            property = archiveHelper.getEnumTypeDefAttribute("BiopsyScope",
                                                             attribute1Name,
                                                             attribute1Description,
                                                             attribute1DescriptionGUID);
            properties.add(property);
            property = archiveHelper.getStringTypeDefAttribute(attribute2Name,
                                                               attribute2Description,
                                                               attribute2DescriptionGUID);
            properties.add(property);
    
            entityDef.setPropertiesDefinition(properties);
    
            return entityDef;
        }
    
    
        /**
         * Crete a new type of relationship to link a biopsy report to other elements - assets, glossary terms, other definitions etc, that support the
         * conclusions of the biopsy report.
         *
         * @return relationship type definition (RelationshipDef)
         */
        private RelationshipDef getBiopsySupportingEvidenceRelationship()
        {
            final String guid            = "54300f97-0140-4adb-b9a9-308514694f8d";
            final String name            = "BiopsySupportingEvidence";
            final String description     = "Link between a biopsy report and other data sources.";
            final String descriptionGUID = null;
    
            final ClassificationPropagationRule classificationPropagationRule = ClassificationPropagationRule.NONE;
    
            RelationshipDef relationshipDef = archiveHelper.getBasicRelationshipDef(guid,
                                                                                    name,
                                                                                    null,
                                                                                    description,
                                                                                    descriptionGUID,
                                                                                    classificationPropagationRule);
    
            RelationshipEndDef relationshipEndDef;
    
            /*
             * Set up end 1.
             */
            final String                     end1EntityType               = "BiopsyReport";
            final String                     end1AttributeName            = "report";
            final String                     end1AttributeDescription     = "Report that the evidence is being linked to.";
            final String                     end1AttributeDescriptionGUID = null;
            final RelationshipEndCardinality end1Cardinality              = RelationshipEndCardinality.ANY_NUMBER;
    
            relationshipEndDef = archiveHelper.getRelationshipEndDef(this.archiveBuilder.getEntityDef(end1EntityType),
                                                                     end1AttributeName,
                                                                     end1AttributeDescription,
                                                                     end1AttributeDescriptionGUID,
                                                                     end1Cardinality);
            relationshipDef.setEndDef1(relationshipEndDef);
    
    
            /*
             * Set up end 2.
             */
            final String                     end2EntityType               = "Referenceable";
            final String                     end2AttributeName            = "evidence";
            final String                     end2AttributeDescription     = "Further information to support the report.";
            final String                     end2AttributeDescriptionGUID = null;
            final RelationshipEndCardinality end2Cardinality              = RelationshipEndCardinality.ANY_NUMBER;
    
            relationshipEndDef = archiveHelper.getRelationshipEndDef(this.archiveBuilder.getEntityDef(end2EntityType),
                                                                     end2AttributeName,
                                                                     end2AttributeDescription,
                                                                     end2AttributeDescriptionGUID,
                                                                     end2Cardinality);
            relationshipDef.setEndDef2(relationshipEndDef);
    
            /*
             * Build the attributes
             */
            List<TypeDefAttribute> properties = new ArrayList<>();
            TypeDefAttribute       property;
    
            final String attribute1Name            = "notes";
            final String attribute1Description     = "Information for the clinical trials team relating to the evidence.";
            final String attribute1DescriptionGUID = null;
    
            property = archiveHelper.getMapStringStringTypeDefAttribute(attribute1Name,
                                                                        attribute1Description,
                                                                        attribute1DescriptionGUID);
            properties.add(property);
    
    
            relationshipDef.setPropertiesDefinition(properties);
    
            return relationshipDef;
        }
    
    
        /**
         * Build a classification that can be attached to an asset to indicate that a member of the clinical trials has reviewed the contents
         * and made notes of their observations and conclusions.
         *
         * @return classification type definition (ClassificationDef)
         */
        private ClassificationDef getReviewedByClinicalTrialsClassification()
        {
            final String guid = "c2fa7555-f366-4869-88f3-897d6f2ec5a4";
    
            final String name            = "ReviewedByClinicalTrials";
            final String description     = "Declares that a report or data set has been assessed by the clinical trials team.";
            final String descriptionGUID = null;
    
            final List<TypeDefLink> linkedToEntities = new ArrayList<>();
    
            linkedToEntities.add(this.archiveBuilder.getEntityDef("Asset"));
    
            ClassificationDef classificationDef = archiveHelper.getClassificationDef(guid,
                                                                                     name,
                                                                                     null,
                                                                                     description,
                                                                                     descriptionGUID,
                                                                                     linkedToEntities,
                                                                                     false);
    
            /*
             * Build the attributes
             */
            List<TypeDefAttribute> properties = new ArrayList<>();
            TypeDefAttribute       property;
    
            final String attribute1Name            = "reviewer";
            final String attribute1Description     = "Person responsible for maintaining this relationship.";
            final String attribute1DescriptionGUID = null;
            final String attribute2Name            = "reviewerTypeName";
            final String attribute2Description     = "Type of element used to identify the reviewer.";
            final String attribute2DescriptionGUID = null;
            final String attribute3Name            = "reviewerPropertyName";
            final String attribute3Description     = "Name of property used to identify the reviewer.";
            final String attribute3DescriptionGUID = null;
            final String attribute4Name            = "notes";
            final String attribute4Description     = "Information for the clinical trials team relating to the review.";
            final String attribute4DescriptionGUID = null;
    
            property = archiveHelper.getStringTypeDefAttribute(attribute1Name,
                                                               attribute1Description,
                                                               attribute1DescriptionGUID);
            properties.add(property);
            property = archiveHelper.getStringTypeDefAttribute(attribute2Name,
                                                               attribute2Description,
                                                               attribute2DescriptionGUID);
            properties.add(property);
            property = archiveHelper.getStringTypeDefAttribute(attribute3Name,
                                                               attribute3Description,
                                                               attribute3DescriptionGUID);
            properties.add(property);
            property = archiveHelper.getMapStringStringTypeDefAttribute(attribute4Name,
                                                                        attribute4Description,
                                                                        attribute4DescriptionGUID);
            properties.add(property);
    
            classificationDef.setPropertiesDefinition(properties);
    
            return classificationDef;
        }
    
    
        /**
         * Returns the open metadata type archive containing all the new type definitions.
         *
         * @return populated open metadata archive object
         */
        protected OpenMetadataArchive getOpenMetadataArchive()
        {
            /*
             * Add attribute type definitions.
             */
            this.archiveBuilder.addEnumDef(getBiopsyScopeEnum());
    
            /*
             * Add the specialized types
             */
            this.archiveBuilder.addEntityDef(getBiopsyReportEntity());
            this.archiveBuilder.addRelationshipDef(getBiopsySupportingEvidenceRelationship());
            this.archiveBuilder.addClassificationDef(getReviewedByClinicalTrialsClassification());
    
    
            /*
             * The completed archive is ready to be packaged up and returned
             */
            return this.archiveBuilder.getOpenMetadataArchive();
        }
    
    
        /**
         * Generates and writes out an open metadata archive containing the new types.
         */
        public void writeOpenMetadataArchive()
        {
            try
            {
                System.out.println("Writing to file: " + cocoTypesArchiveFileName);
    
                super.writeOpenMetadataArchive(cocoTypesArchiveFileName, this.getStabilizedArchive(cocoTypesArchiveFileName));
            }
            catch (Exception error)
            {
                System.out.println("error is " + error);
            }
        }
    
    
        /**
         * Generates and writes out the open metadata archive created in the builder.
         *
         * @param folderName name of the folder to add the archive into
         */
        public void writeOpenMetadataArchive(String folderName)
        {
            try
            {
                String pathName = cocoTypesArchiveFileName;
    
                if (folderName != null)
                {
                    pathName = folderName + "/" + cocoTypesArchiveFileName;
                }
    
                System.out.println("Writing to file: " + pathName);
                super.writeOpenMetadataArchive(pathName, this.getStabilizedArchive(pathName));
            }
            catch (Exception error)
            {
                System.out.println("error is " + error);
            }
        }
    
    
        /**
         * Return the archive to write, with the types that are unchanged since the edition already at the path keeping
         * their previous versions.  The version number above is the build time, and a type's version is what tells the
         * servers of a cohort that it has been updated, so stamping unchanged types with it on every build announced
         * changes that had not happened.
         *
         * @param pathName path the archive is about to be written to
         * @return archive
         */
        private OpenMetadataArchive getStabilizedArchive(String pathName)
        {
            OpenMetadataArchive openMetadataArchive = this.getOpenMetadataArchive();
    
            if (new File(pathName).exists())
            {
                new ArchiveVersionStabilizer().stabilizeVersions(openMetadataArchive, super.readOpenMetadataArchive(pathName));
            }
    
            return openMetadataArchive;
        }
    
    
        /**
         * Main program to write the archive into the current directory.  (In egeria.git this class has no main
         * method - it is run by CocoArchivesWriter, which calls writeOpenMetadataArchive("content-packs").)
         *
         * @param args ignored
         */
        public static void main(String[] args)
        {
            new CocoTypesArchiveWriter().writeOpenMetadataArchive(null);
        }
    }
    ```

This example is located in the `egeria.git` repository in the [coco-metadata-archives :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/sample-metadata/coco-metadata-archives){ target=gh } module, and its output is `content-packs/CocoTypesArchive.omarchive`.  The `main()` method has been added for this page.

Notice how the version number of the types is handled.  The `versionNumber` passed to `OMRSArchiveHelper` is the time of the build, and a type's version is what tells the servers of a cohort that the type has been updated.  So before writing the archive, `getStabilizedArchive()` reads back the previous edition of the archive (with `readOpenMetadataArchive()` from `OMRSArchiveWriter`) and uses `ArchiveVersionStabilizer` (from the [content-pack-helpers :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/content-pack-helpers){ target=gh } module) to give each type that has not changed the version it had before.

!!! attention "Changing your types"
    Once instances of a type have been stored, the type should only change through a `TypeDefPatch`, rather than by editing the original definition.  `OMRSArchiveBuilder` has `getPatchForType()` to start a patch for an existing type and `addTypeDefPatch()` to add it to the archive.  This is how the open metadata types themselves are updated from one release to the next.

## How the open metadata types archive is structured

Egeria's own types are built in the same way, by the [open-metadata-types :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-metadata-types){ target=gh } module:

* `OpenMetadataTypesArchive` holds the archive header (its archive GUID is `bce3b0a0-662a-4f87-b8dc-844078a11a6e`, the value that appears in the `dependsOnArchives` property of archives that build on the open metadata types) and the new and changed types for the release currently in development.
* There is a class for each earlier release, from `OpenMetadataTypesArchive1_2` (types added before release 1.3) through to `OpenMetadataTypesArchive6_2`.  The types in these classes are approved and can only change through patches in a later class.
* Each class is constructed with the shared `OMRSArchiveBuilder`.  Its `getOriginalTypes()` method first creates the class for the previous release and calls its `getOriginalTypes()`, and then adds its own new types (`addEntityDef()`, `addRelationshipDef()`, `addClassificationDef()`, `addEnumDef()`) and patches (`addTypeDefPatch()`).  So calling `new OpenMetadataTypesArchive().getOpenMetadataArchive()` builds the complete set of types, release by release.
* `OpenMetadataTypesArchiveAccessor` provides methods to look up the type definitions in the resulting archive by name.  `OpenMetadataTypesArchiveWriter` writes the archive out as `content-packs/OpenMetadataTypes.omarchive`; it is run by `OpenMetadataTypesArchiveUtility` in the [open-metadata-types-utility :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-metadata-types-utility){ target=gh } module.  The file is for servers that do not use the Egeria libraries, which load the open metadata types automatically.

Within each class, the code is organized by [type model area](/types) - for example `add0482StatementsOfApplicability()` or `update0239Reports()` - and the type and property names come from the `OpenMetadataType` and `OpenMetadataProperty` enums in the Open Metadata Framework.

--8<-- "snippets/abbr.md"
