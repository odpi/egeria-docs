<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Paste this code between the curly braces of the `AssetListen` class.

```java linenums="1"
    private String serverName;
    private String platformURLRoot;
    private String clientUserId;

    private AssetConsumer client;

    /**
     * Set up the parameters for the utility.
     *
     * @param serverName server to call
     * @param platformURLRoot location of server
     * @param clientUserId userId to access the server
     */
    private AssetListen(String serverName,
                        String platformURLRoot,
                        String clientUserId)
    {
        this.serverName = serverName;
        this.platformURLRoot = platformURLRoot;
        this.clientUserId = clientUserId;

        try
        {
            client = new AssetConsumer(serverName, platformURLRoot);
        }
        catch (Exception error)
        {
            System.out.println("There was an exception when creating the Asset Consumer OMAS client.  Error message is: " + error.getMessage());
        }
    }


    /**
     * Process an event that was published by the Asset Consumer OMAS.
     *
     * @param event event object - call getEventType to find out what type of event.
     */
    public void processEvent(AssetConsumerEvent event)
    {
        if (event.getEventType() == AssetConsumerEventType.NEW_ASSET_EVENT)
        {
            NewAssetEvent assetEvent = (NewAssetEvent)event;

            System.out.println("------------------------------------------------------------------------");
            System.out.println("EVENT: " + assetEvent.getEventType().getEventTypeName() + " - for asset " + assetEvent.getAsset().getGUID());

            this.printAsset(assetEvent.getAsset());
        }
        else if (event.getEventType() == AssetConsumerEventType.UPDATED_ASSET_EVENT)
        {
            UpdatedAssetEvent assetEvent = (UpdatedAssetEvent)event;

            System.out.println("------------------------------------------------------------------------");
            System.out.println("EVENT: " + assetEvent.getEventType().getEventTypeName() + " - for asset " + assetEvent.getAsset().getGUID() + " - at " + assetEvent.getUpdateTime());

            this.printAsset(assetEvent.getAsset());
        }
    }


    /**
     * This method displays some of the data from the CSV File.
     *
     * @param connector connector to the CSV file
     */
    private void displayFile(CSVFileStoreConnector connector)
    {
        try
        {
            System.out.println("    ===============================");

            System.out.println("    Accessing file: " + connector.getFileName());

            long         numberOfRecords  = connector.getRecordCount();
            long         displayedRecords = 10;

            System.out.println("Number of records: " + numberOfRecords);
            
            if (numberOfRecords < displayedRecords)
            {
                displayedRecords = numberOfRecords;
                System.out.println("All records ...");
            }
            else
            {
                System.out.println("First 10 records ...");
            }

            if (displayedRecords > 0)
            {
                List<String> columnNames = connector.getColumnNames();
                int          startingFrom = 0;
                
                if (columnNames == null)
                {
                    /*
                     * Column names are first line of the file - not in the metadata
                     */
                    columnNames = connector.readRecord(0);
                    startingFrom = 1;
                }

                System.out.println("    File content:");

                System.out.println("    ------------------------------------------------------------------------");
                System.out.println("      " + columnNames);
                System.out.println("    ------------------------------------------------------------------------");

                for (int i = startingFrom; i < displayedRecords; i++)
                {
                    List<String> columns = connector.readRecord(i);

                    System.out.println("      " + columns);
                }

                System.out.println("    ------------------------------------------------------------------------");
            }

        }
        catch (FileReadException error)
        {
            System.out.println("The connector is unable to retrieve the requested record because the file is too short.");
        }
        catch (Exception exception)
        {
            System.out.println("Exception " + exception.getMessage());
        }
    }


    /**
     * Print out details of an asset.
     * 
     * @param asset retrieved asset
     */
    private void printAsset(Asset asset)
    {
        System.out.println("------------------------------------------------------------------------");

        System.out.println("  Asset Details:");
        System.out.println("    guid: " + asset.getGUID());
        System.out.println("    qualifiedName: " + asset.getQualifiedName());
        System.out.println("    displayName: " + asset.getDisplayName());
        System.out.println("    description: " + asset.getDescription());
        System.out.println("    member of zones: " + asset.getZoneMembership());
        
        try
        {
            /*
             * Is there a connector associated with the asset?
             */
            Connector connector = client.getConnectorForAsset(clientUserId, asset.getGUID());

            if (connector instanceof CSVFileStoreConnector)
            {
                displayFile((CSVFileStoreConnector)connector);
            }
        }
        catch (Exception error)
        {
            System.out.println("Unable to use connector for asset: " + asset.getGUID());
        }
    }


    /**
     * This runs the utility
     */
    private void run()
    {
        try
        {
            AssetConsumerEventClient eventClient = new AssetConsumerEventClient(serverName,
                                                                                platformURLRoot,
                                                                                null,
                                                                                null,
                                                                                10,
                                                                                null,
                                                                                this.getClass().getName());

            eventClient.registerListener(clientUserId,this);
        }
        catch (Exception error)
        {
            System.out.println("There was a " + error.getClass().getName() + " exception when calling the OMAG Server Platform.  Error message is: " + error.getMessage());
        }
    }


    /**
     * Main program that initiates the operation of the AssetListen utility.  The parameters are optional.  They are passed space separated.
     * They are used to override the utility's default values.
     *
     * @param args 1. service platform URL root, 2. client userId, 3. server name,
     */
    public static void main(String[] args)
    {
        String  platformURLRoot = "https://localhost:9443";
        String  clientUserId = "erinoverview";
        String  serverName = "mds1";

        if (args.length > 0)
        {
            platformURLRoot = args[0];
        }

        if (args.length > 1)
        {
            clientUserId = args[1];
        }

        if (args.length > 2)
        {
            serverName = args[2];
        }

        System.out.println("===============================");
        System.out.println("Asset Listen Utility:          ");
        System.out.println("===============================");
        System.out.println("Running against platform: " + platformURLRoot);
        System.out.println("Focused on server: " + serverName);
        System.out.println("Using userId: " + clientUserId);
        System.out.println();

        HttpHelper.noStrictSSLIfConfigured();

        try
        {
            AssetListen assetListen = new AssetListen(serverName, platformURLRoot, clientUserId);

            assetListen.run();
        }
        catch (Exception  error)
        {
            System.out.println("Exception: " + error.getClass().getName() + " with message " + error.getMessage());
            System.exit(-1);
        }
    }
```
