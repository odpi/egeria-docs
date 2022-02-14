<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Paste this code between the curly braces of the `AssetCreate` class.

```java linenum=1
    private static final String fileName1  = "sample-data/oak-dene-drop-foot-weekly-measurements/week1.csv";
    private static final String fileName2  = "sample-data/oak-dene-drop-foot-weekly-measurements/week2.csv";
    private static final String fileName3  = "sample-data/oak-dene-drop-foot-weekly-measurements/week3.csv";
    private static final String fileName4  = "sample-data/oak-dene-drop-foot-weekly-measurements/week4.csv";
    private static final String fileName5  = "sample-data/oak-dene-drop-foot-weekly-measurements/week5.csv";
    private static final String fileName6  = "sample-data/old-market-drop-foot-weekly-measurements/week1.csv";
    private static final String fileName7  = "sample-data/old-market-drop-foot-weekly-measurements/week2.csv";
    private static final String fileName8  = "sample-data/old-market-drop-foot-weekly-measurements/week3.csv";
    private static final String fileName9  = "sample-data/old-market-drop-foot-weekly-measurements/week4.csv";
    private static final String fileName10 = "sample-data/old-market-drop-foot-weekly-measurements/week5.csv";

    private String serverName;
    private String serverURLRoot;
    private String clientUserId;

    private List<String> fileNames = new ArrayList<>();

    /**
     * Set up the parameters for the utility.
     *
     * @param serverName server to call
     * @param serverURLRoot location of server
     * @param clientUserId userId to access the server
     */
    private AssetCreate(String serverName,
                        String serverURLRoot,
                        String clientUserId)
    {
        this.serverName = serverName;
        this.serverURLRoot = serverURLRoot;
        this.clientUserId = clientUserId;

        /*
         * These are the names of files that need to be catalogued.
         */
        this.fileNames.add(fileName1);
        this.fileNames.add(fileName2);
        this.fileNames.add(fileName3);
        this.fileNames.add(fileName4);
        this.fileNames.add(fileName5);
        this.fileNames.add(fileName6);
        this.fileNames.add(fileName7);
        this.fileNames.add(fileName8);
        this.fileNames.add(fileName9);
        this.fileNames.add(fileName10);
    }
    
    
    /**
     * This runs the utility
     */
    private void run()
    {
        try
        {
            for (String fileName : fileNames)
            {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                System.out.println("Press enter to create asset for next file: " + fileName);
                
                br.readLine();

                // The code to create the asset goes here.
            }
        }
        catch (Exception error)
        {
            System.out.println("There was a " + error.getClass().getName() + " exception when calling the OMAG Server Platform.  Error message is: " + error.getMessage());
        }
    }


    /**
     * Main program that initiates the operation of the AssetCreate utility.  The parameters are optional.  They are passed space separated.
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
        System.out.println("Asset Create Utility:          ");
        System.out.println("===============================");
        System.out.println("Running against platform: " + platformURLRoot);
        System.out.println("Focused on server: " + serverName);
        System.out.println("Using userId: " + clientUserId);
        System.out.println();

        try
        {
            AssetCreate assetCreate = new AssetCreate(serverName, platformURLRoot, clientUserId);

            assetCreate.run();
        }
        catch (Exception  error)
        {
            System.out.println("Exception: " + error.getClass().getName() + " with message " + error.getMessage());
            System.exit(-1);
        }
    }
```

On the right-hand side of the editor you will see a square of yellow and 4 little yellow lines.  

![Warnings](/education/egeria-dojo/developer/asset-create-skeleton-warnings.png)

The yellow lines are warnings that the code is incomplete.  You can hover the mouse pointer over these lines and the reason for the warning is displayed.   As you add content to the file during this exercise, these lines should disappear.  If you make a syntax error, you will see a red line in this column showing which line is in error.  The yellow box at the top is a summary of the findings of the static analysis.  Hovering the mouse pointer over this area will show the report.  It will change colour to indicate the most serious finding.  You are aiming for a green tick, which means no errors have been found.