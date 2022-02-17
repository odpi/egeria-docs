<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


The structure of an *open metadata archive writer* that builds an open metadata archive as a json file, uses

* One or more *Archive Helper* classes to construct the elements for the archive.
* An *archive builder* class that holds the archive content in memory as it is assembled.

Your archive writer class then extracts the content from the builder to write out the archive file.

![in memory approach](/guides/developer/open-metadata-archives/in-memory-archive-construction.svg)

Egeria provides the following utility modules in `egeria.git` to help you create an archive writer.

* Module `repository-services-archive-utilities` - located in `open-metadata-implementation/repository-services` - provides the functions for archive building using [Open Metadata Repository Service (OMRS)](/services/omrs) type definitions and instances.  These are the objects that are stored in the archive and all of this modules classes begin `OMRS`. 
* Module `content-pack-helpers` - located in `open-metadata-reources/open-metadata-archives` - has archive helper classes for building instances of well known types such as assets, connections and schema.
        
Using these utilities, your archive writer inherits from `OMRSArchiveWriter` which does all of the work of formatting the archive and writing it to disk.

Your archive writer creates an instance of `OMRSArchiveBuilder` to accumulate the content of the archive.  

* When it is building types, it uses the `OMRSArchiveHelper` to create each type definition and then adds it to the archive builder.  

* When it is creating instances, your archive writer typically uses the appropriate helper classes in `content-pack-helpers`.  However, this only for ease of coding because they manage the mapping from, say an *asset* to an entity instance of type `Asset` .  

The `content-pack-helpers` all use `OMRSArchiveHelper` in their implementation to create the actually archive object.  To illustrate, here is the code inside `SimpleCatalogArchiveHelper` for creating an entity instance of type `Asset`.  The `archiveHelper` it is using is of type `OMRSArchiveHelper`.  It is passed your archive writer's `archiveBuilder` in its constructor and so you also see the call to add the entity to the archive builder at the end of the method. 

```java linenums="1"

    /**
     * Create an asset entity.
     *
     * @param typeName name of asset subtype to use - default is Asset
     * @param qualifiedName unique name for the asset
     * @param displayName display name for the asset
     * @param description description about the asset
     * @param additionalProperties any other properties
     * @param extendedProperties additional properties defined in the sub type
     * @param classifications list of classifications (if any)
     *
     * @return id for the asset
     */
    public String addAsset(String               typeName,
                           String               qualifiedName,
                           String               displayName,
                           String               description,
                           Map<String, String>  additionalProperties,
                           Map<String, Object>  extendedProperties,
                           List<Classification> classifications)
    {
        final String methodName = "addAsset";

        String assetTypeName = ASSET_TYPE_NAME;

        if (typeName != null)
        {
            assetTypeName = typeName;
        }

        InstanceProperties properties = archiveHelper.addStringPropertyToInstance(archiveRootName, null, QUALIFIED_NAME_PROPERTY, qualifiedName, methodName);
        properties = archiveHelper.addStringPropertyToInstance(archiveRootName, properties, NAME_PROPERTY, displayName, methodName);
        properties = archiveHelper.addStringPropertyToInstance(archiveRootName, properties, DESCRIPTION_PROPERTY, description, methodName);
        properties = archiveHelper.addStringMapPropertyToInstance(archiveRootName, properties, ADDITIONAL_PROPERTIES_PROPERTY, additionalProperties, methodName);
        properties = archiveHelper.addPropertyMapToInstance(archiveRootName, properties, extendedProperties, methodName);

        EntityDetail assetEntity = archiveHelper.getEntityDetail(assetTypeName,
                                                                 idToGUIDMap.getGUID(qualifiedName),
                                                                 properties,
                                                                 InstanceStatus.ACTIVE,
                                                                 classifications);

        archiveBuilder.addEntity(assetEntity);

        return assetEntity.getGUID();
    }
```

Once all of the type definitions and instances have been created, your archive writer extracts the content of the archive from the archive builder.  It is returned as an `OpenMetadataArchive` object which it passes to its super class (`OMRSArchiveWriter`) along with the file name of and the new open metadata archive is written to disk.

```java linenums="1"

    /**
     * Returns the open metadata archive containing new metadata entities.
     *
     * @return populated open metadata archive object
     */
    protected OpenMetadataArchive getOpenMetadataArchive()
    {

        // add content of archive here

        
        /*
         * Save the GUIDs use in the archive so they can be consistent in the next version.
         */
        archiveHelper.saveGUIDs();

        /*
         * The completed archive is ready to be packaged up and returned
         */
        return this.archiveBuilder.getOpenMetadataArchive();
    }


    /**
     * Generates and writes out the open metadata archive created in the builder.
     */
    private void writeOpenMetadataArchive()
    {
        try
        {
            System.out.println("Writing to file: " + archiveFileName);

            super.writeOpenMetadataArchive(archiveFileName, this.getOpenMetadataArchive());
        }
        catch (Exception error)
        {
            System.out.println("error is " + error.toString());
        }
    }


```