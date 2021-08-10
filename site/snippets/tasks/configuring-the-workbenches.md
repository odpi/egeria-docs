<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the workbenches

The workbenches are configured using the OMAG Server Platform Administration Services. 
This defines which workbenches to run and how to connect to the technology to test.
This configuration defines an OMAG server that will run the requested conformance suite tests.

Configure the OMAG server that will run the requested conformance suite tests.
The requested workbenches will begin to execute their tests as soon as the OMAG server is started.

### Repository workbench

To run a metadata repository through the Repository Workbench, first configure a CTS server in the
[OMAG Server Platform](/egeria/concepts/omag-server-platform) by configuring its general properties
like server type, event bus, cohort, etc. Before starting the CTS server instance, configure the
repository workbench within it using the following command:

!!! post "POST - configure repository workbench"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/cts/conformance-suite-workbenches/repository-workbench/repositories
    ```

    Send the repository workbench configuration as the request body, similar to the following:

    ```json hl_lines="3"
    {
      "class": "RepositoryConformanceWorkbenchConfig",
      "tutRepositoryServerName": "myserver",
      "maxSearchResults": 5
    }    
    ```

    The required `tutRepositoryServerName` parameter defines the name of the repository server you wish to test,
    while the optional `maxSearchResults` parameter controls the sizing of the tests: both the number of
    instances the tests will attempt to create to carry out its tests and how extensive the search-based
    tests are.

!!! attention "Start the technology under test _after_ the CTS server"
    This repository server to test (`myserver` in the example above) should be [configured and started](/egeria/guides/admin/configuring-a-metadata-server)
    _after_ starting the CTS repository workbench instance. Once the CTS server instance is started it will wait for
    the technology under test (the server named by the `tutRepositoryServerName` parameter) to be up and running
    before then starting its suite of tests.

The OMAG server also supports a REST API for querying the results of running the conformance suite tests.
These commands include:

- Retrieve the results from a single named workbench.
- Retrieve the results from all workbenches and test cases (beware that the response can be 100's of MB in size, and
  may overflow your JVM heap).
- Retrieve the results from all failed test cases.
- Retrieve the IDs of all test cases.
- Retrieve the results from a specific test cases (for example, iterating through the above call's response).
- Retrieve the names of all profiles.
- Retrieve the details of a single profile's results (for example, iterating through the above call's response).

!!! attention "The resulting reports can be large"
    Ensure the jvm running the CTS server has at least 1GB heap to avoid any Java heap errors.

The Open Metadata Conformance Suite also has a client called `OpenMetadataConformanceTestReport` that will
retrieve the conformance report and all details. It will store a summarized report in `openmetadata_cts_summary.json`,
and the full details of each profile and test case in `profile-details` and `test-cases` sub-directories, respectively.
The client also outputs a summary of the test run.

??? success "Example output for a successful CTS run"
    This output is an example of a successful run:

    ```text
    $ OpenMetadataConformanceTestReport cSuiteServer https://localhost:9444
    =======================================
    Open Metadata Conformance Test Report
    =======================================
    Contacting conformance suite server: cts (https://localhost:9443)
    
    Saving full profile details into 'profile-details' directory...
    Summary of profile results:
    ... Metadata sharing: CONFORMANT_FULL_SUPPORT
    ... Reference copies: CONFORMANT_FULL_SUPPORT
    ... Metadata maintenance: CONFORMANT_FULL_SUPPORT
    ... Dynamic types: UNKNOWN_STATUS
    ... Graph queries: CONFORMANT_FULL_SUPPORT
    ... Historical search: CONFORMANT_FULL_SUPPORT
    ... Entity proxies: CONFORMANT_FULL_SUPPORT
    ... Soft-delete and restore: CONFORMANT_FULL_SUPPORT
    ... Undo an update: CONFORMANT_FULL_SUPPORT
    ... Reidentify instance: CONFORMANT_FULL_SUPPORT
    ... Retype instance: CONFORMANT_FULL_SUPPORT
    ... Rehome instance: CONFORMANT_FULL_SUPPORT
    ... Entity search: CONFORMANT_FULL_SUPPORT
    ... Relationship search: CONFORMANT_FULL_SUPPORT
    ... Entity advanced search: CONFORMANT_FULL_SUPPORT
    ... Relationship advanced search: CONFORMANT_FULL_SUPPORT
    Saving full test case details into 'test-case-details' directory (can take 1-2 minutes)...
    Summary:
    ... number of tests: 4965
    ... number of tests passed: 4965
    ... number of tests failed: 0
    ... number of tests skipped: 0
    
    Congratulations, technology under test is conformant
    
    Process finished with exit code 0
    ```

??? failure "Example output for an unsuccessful CTS run"
    The example below is for an unsuccessful run (where one of the Entity search tests has failed):

    ```text
    $ OpenMetadataConformanceTestReport cSuiteServer https://localhost:9444
    =======================================
    Open Metadata Conformance Test Report
    =======================================
    Contacting conformance suite server: cts (https://localhost:9443)
    
    Saving full profile details into 'profile-details' directory...
    Summary of profile results:
    ... Metadata sharing: CONFORMANT_FULL_SUPPORT
    ... Reference copies: CONFORMANT_FULL_SUPPORT
    ... Metadata maintenance: CONFORMANT_FULL_SUPPORT
    ... Dynamic types: UNKNOWN_STATUS
    ... Graph queries: CONFORMANT_FULL_SUPPORT
    ... Historical search: CONFORMANT_FULL_SUPPORT
    ... Entity proxies: CONFORMANT_FULL_SUPPORT
    ... Soft-delete and restore: CONFORMANT_FULL_SUPPORT
    ... Undo an update: CONFORMANT_FULL_SUPPORT
    ... Reidentify instance: CONFORMANT_FULL_SUPPORT
    ... Retype instance: CONFORMANT_FULL_SUPPORT
    ... Rehome instance: CONFORMANT_FULL_SUPPORT
    ... Entity search: NOT_CONFORMANT
    ... Relationship search: CONFORMANT_FULL_SUPPORT
    ... Entity advanced search: CONFORMANT_FULL_SUPPORT
    ... Relationship advanced search: CONFORMANT_FULL_SUPPORT
    Saving full test case details into 'test-case-details' directory (can take 1-2 minutes)...
    Summary:
    ... number of tests: 4965
    ... number of tests passed: 4964
    ... number of tests failed: 1
    ... number of tests skipped: 0
    
    Technology under test is not yet conformant
    
    Process finished with exit code 1
    ```
