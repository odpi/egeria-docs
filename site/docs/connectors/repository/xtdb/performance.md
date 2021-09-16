<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# XTDB Connector Performance

Following are details on XTDB's performance at the latest release of the connector (v3.1, using XTDB v1.18.1). All raw metrics and elements used to produce the results are described further under [reproducibility](#reproducibility) below, but the historical details themselves are no longer included below in the interest of being concise.

??? info "Details on the performance metrics"
    The *median* of all results for that method across all executions for a given set of volume parameters is given (all times in milliseconds) to give an idea of the "typical" result, while limiting potential skew from significant outliers.

    A more detailed set of statistics is best reviewed through the Jupyter Notebook provided in each results directory, where you can review:

    - the full distributions of execution times (including the outliers)
    - detailed individual outlier results (e.g. the top-10 slowest response times per method)
    - volumes in place during the tests (how many entities, how many relationships, etc)
    
    The volume parameters that were used for each test are specified using the convention `i-s`, where `i` is the value for the `instancesPerType` parameter to the PTS and `s` is the value for `maxSearchResults`. For example, `5-2` means 5 instances will be created for every open metadata type and 2 will be the maximum number of results per page for methods that include paging.

    - All tests are run from `5-2` through `20-10` to give a sense of the performance impact of doubling the number of instances and search results.
    - Above this, the graph queries are no longer included: they become exponentially more complex as the volumes grow, and while they will still return results, the depth of their testing in the PTS means that they can contribute many hours (or even days) to the overall suite execution -- they are therefore left out to be able to more quickly produce results for the other methods at progressively higher volumes.
    - The page size is left at a maximum of `10` for subsequent tests so that it is only the volume of instances in total that are doubling each time, rather than also the number of detailed results.
    - Instance counts range from a few thousand (at `5-2`) up to nearly one hundred thousand (at `80-10`).
    
    In the graphical comparisons, a point plot is used to show the typical execution time of each method at the different volumes / by repository. Each point on the plot represents the _median_ execution time for that method, at a given volume of metadata. (For the repository comparison plots, `pts` = XTDB and `janus` = JanusGraph.) The horizontal lines that appear around each point are confidence intervals calculated by a bootstrapping process: in simple terms, the larger the horizontal line, the more variability there is for that particular method's execution time (a singular median value is insufficient to represent such variability on its own).

## XTDB at varying volumes

!!! summary
    The retrieval and write operations remain very consistent, with almost no variability, throughout the growth in volume. The search operations, however, begin to clearly degrade at the highest volumes tested. Further investigation into other optimized settings for the search operations for these larger volumes is likely warranted as the next step to continue to improve performance.

![Graphical comparison](volume_comparison.svg)

Profile | Method | 05-02 (4,850) | 10-05 (9,700) | 20-10 (19,400) | 40-10 (38,800) | 80-10 (77,600)
---|---|---|---|---|---|---
Entity creation | addEntity | 55.0 | 48.0 | 46.0 | 48.0 | 44.0
... | saveEntityReferenceCopy | 52.0 | 45.0 | 43.0 | 46.0 | 42.0
Entity search | findEntities | 54.0 | 65.0 | 88.0 | 215.0 | 413.0
... | findEntitiesByProperty | 31.0 | 36.0 | 44.0 | 100.0 | 151.0
... | findEntitiesByPropertyValue | 58.0 | 71.0 | 102.0 | 170.0 | 331.0
Relationship creation | addRelationship | 48.0 | 47.0 | 45.0 | 47.0 | 44.0
... | saveRelationshipReferenceCopy | 52.0 | 49.0 | 47.0 | 49.0 | 46.0
Relationship search | findRelationships | 28.0 | 30.0 | 33.0 | 39.0 | 39.0
... | findRelationshipsByProperty | 29.0 | 35.0 | 43.0 | 105.0 | 166.0
... | findRelationshipsByPropertyValue | 47.0 | 59.0 | 78.0 | 159.0 | 362.0
Entity classification | classifyEntity | 78.0 | 73.5 | 72.0 | 75.0 | 73.0
... | saveClassificationReferenceCopy | 70.0 | 59.0 | 63.0 | 64.0 | 62.0
Classification search | findEntitiesByClassification | 37.0 | 44.0 | 60.0 | 97.0 | 113.0
Entity update | reTypeEntity | 44.0 | 41.0 | 40.0 | 46.0 | 41.0
... | updateEntityProperties | 58.0 | 53.0 | 53.0 | 49.0 | 49.0
Relationship update | updateRelationshipProperties | 63.0 | 56.0 | 56.0 | 56.0 | 54.0
Classification update | updateEntityClassification | 96.0 | 92.5 | 87.0 | 90.0 | 88.0
Entity undo | undoEntityUpdate | 49.0 | 53.0 | 50.0 | 48.0 | 44.0
Relationship undo | undoRelationshipUpdate | 56.0 | 55.0 | 54.0 | 53.0 | 52.0
Entity retrieval | getEntityDetail | 17.0 | 16.0 | 16.0 | 16.0 | 16.0
... | getEntitySummary | 17.0 | 16.0 | 16.0 | 16.0 | 16.0
... | isEntityKnown | 17.0 | 16.0 | 16.0 | 16.0 | 16.0
Entity history retrieval | getEntityDetail | 20.0 | 19.0 | 19.0 | 19.0 | 19.0
... | getEntityDetailHistory | 22.0 | 21.0 | 21.0 | 21.0 | 21.0
Relationship retrieval | getRelationship | 18.0 | 17.0 | 17.0 | 18.0 | 17.0
... | isRelationshipKnown | 18.0 | 17.0 | 17.0 | 18.0 | 17.0
Relationship history retrieval | getRelationship | 21.0 | 21.0 | 21.0 | 21.0 | 21.0
... | getRelationshipHistory | 23.0 | 22.0 | 22.0 | 22.0 | 22.0
Entity history search | findEntities | 60.5 | 89.0 | 140.0 | 549.5 | 1574.0
... | findEntitiesByProperty | 31.0 | 34.0 | 40.0 | 55.0 | 73.0
... | findEntitiesByPropertyValue | 54.0 | 75.0 | 129.5 | 295.5 | 676.0
Relationship history search | findRelationships | 28.0 | 34.0 | 43.0 | 49.0 | 49.0
... | findRelationshipsByProperty | 33.0 | 41.0 | 55.0 | 63.0 | 65.0
... | findRelationshipsByPropertyValue | 55.0 | 84.0 | 143.0 | 228.0 | 516.0
Graph queries | getEntityNeighborhood | 27.0 | 26.0 | 24.0 | -- | --
... | getLinkingEntities | 21.0 | 25.0 | 26.0 | -- | --
... | getRelatedEntities | 563.0 | 1057.0 | 1873.0 | -- | --
... | getRelationshipsForEntity | 26.0 | 27.0 | 25.0 | -- | --
Graph history queries | getEntityNeighborhood | 26.0 | 25.0 | 24.0 | -- | --
... | getLinkingEntities | 21.0 | 25.0 | 26.0 | -- | --
... | getRelatedEntities | 559.5 | 1057.5 | 1873.0 | -- | --
... | getRelationshipsForEntity | 25.0 | 25.0 | 24.0 | -- | --
Entity re-home | reHomeEntity | 46.0 | 45.0 | 44.0 | 51.0 | 45.0
Relationship re-home | reHomeRelationship | 43.0 | 45.0 | 41.0 | 46.0 | 44.0
Entity declassify | declassifyEntity | 66.0 | 63.0 | 63.0 | 68.5 | 64.0
... | purgeClassificationReferenceCopy | 58.0 | 55.5 | 55.5 | 62.0 | 56.0
Entity re-identify | reIdentifyEntity | 55.0 | 51.0 | 49.0 | 64.0 | 56.0
Relationship re-identify | reIdentifyRelationship | 44.0 | 47.0 | 40.0 | 49.0 | 44.0
Relationship delete | deleteRelationship | 40.0 | 40.0 | 39.0 | 47.0 | 41.0
Entity delete | deleteEntity | 45.0 | 45.0 | 43.0 | 55.0 | 48.0
Entity restore | restoreEntity | 39.0 | 39.0 | 37.0 | 45.0 | 40.0
Relationship restore | restoreRelationship | 37.0 | 39.0 | 36.0 | 43.0 | 36.0
Relationship purge | purgeRelationship | 32.0 | 32.0 | 30.0 | 39.0 | 33.0
... | purgeRelationshipReferenceCopy | 23.0 | 24.0 | 22.0 | 27.0 | 24.0
Entity purge | purgeEntity | 40.0 | 40.0 | 40.0 | 52.0 | 45.0
... | purgeEntityReferenceCopy | 24.0 | 24.0 | 24.0 | 29.0 | 26.0

## XTDB vs JanusGraph

!!! summary
    In almost all cases, the XTDB repository is *significantly* faster than JanusGraph: at most volumes completing all methods in less than 100ms and with very little variability. For JanusGraph, on the other hand, there is significant variability (in particular for methods like `findEntitiesByClassification`), and there are numerous examples of the median execution time taking more than multiple seconds.

    Even at 8 times the volume of metadata the XTDB connector still outperforms the JanusGraph connector in almost every method (the only exceptions being a few of the find methods, where the performance is approximately even at 2-4 times the volume).

!!! attention "Graph queries were disabled for JanusGraph"
    The graph queries were disabled for JanusGraph in order to have results in a timely manner: it would take more than a month to produce results for these queries for the JanusGraph connector.

![Graphical comparison](repo_comparison.svg)

The XTDB results can be difficult to see in detail due to the skew from the Janus results, so it may be easier to look at this more granular comparison that drops the higher scales of Janus for readability of the XTDB results:

![Graphical comparison without large Janus volumes](repo_comparison_granular.svg)

Profile | Method | 05-02 (XTDB) | 05-02 (Janus) | 10-05 (XTDB) | 10-05 (Janus) | 20-10 (XTDB) | 20-10 (Janus) | 40-10 (XTDB) | 40-10 (Janus) | 80-10 (XTDB) | 80-10 (Janus)
---|---|---|---|---|---|---|---|---|---|---|---
Entity creation | addEntity | 55.0 | 440.0 | 48.0 | 450.0 | 46.0 | 483.0 | 48.0 | 481.0 | 44.0 | DNF
... | saveEntityReferenceCopy | 52.0 | 435.0 | 45.0 | 451.0 | 43.0 | 481.0 | 46.0 | 479.0 | 42.0 | DNF
Entity search | findEntities | 54.0 | 260.0 | 65.0 | 454.0 | 88.0 | 973.5 | 215.0 | 2104.0 | 413.0 | DNF
... | findEntitiesByProperty | 31.0 | 40.0 | 36.0 | 50.0 | 44.0 | 79.0 | 100.0 | 115.0 | 151.0 | DNF
... | findEntitiesByPropertyValue | 58.0 | 85.0 | 71.0 | 94.0 | 102.0 | 123.0 | 170.0 | 165.0 | 331.0 | DNF
Relationship creation | addRelationship | 48.0 | 160.0 | 47.0 | 162.0 | 45.0 | 162.5 | 47.0 | 156.0 | 44.0 | DNF
... | saveRelationshipReferenceCopy | 52.0 | 460.0 | 49.0 | 456.0 | 47.0 | 480.0 | 49.0 | 464.0 | 46.0 | DNF
Relationship search | findRelationships | 28.0 | 45.0 | 30.0 | 60.0 | 33.0 | 99.0 | 39.0 | 146.0 | 39.0 | DNF
... | findRelationshipsByProperty | 29.0 | 48.0 | 35.0 | 63.0 | 43.0 | 109.0 | 105.0 | 171.0 | 166.0 | DNF
... | findRelationshipsByPropertyValue | 47.0 | 71.0 | 59.0 | 86.0 | 78.0 | 120.0 | 159.0 | 181.0 | 362.0 | DNF
Entity classification | classifyEntity | 78.0 | 886.0 | 73.5 | 921.5 | 72.0 | 1031.0 | 75.0 | 961.0 | 73.0 | DNF
... | saveClassificationReferenceCopy | 70.0 | 738.0 | 59.0 | 845.5 | 63.0 | 969.5 | 64.0 | 895.5 | 62.0 | DNF
Classification search | findEntitiesByClassification | 37.0 | 606.0 | 44.0 | 1029.0 | 60.0 | 2195.5 | 97.0 | 3696.0 | 113.0 | DNF
Entity update | reTypeEntity | 44.0 | 390.0 | 41.0 | 374.5 | 40.0 | 453.0 | 46.0 | 381.0 | 41.0 | DNF
... | updateEntityProperties | 58.0 | 698.0 | 53.0 | 720.5 | 53.0 | 804.0 | 49.0 | 776.5 | 49.0 | DNF
Relationship update | updateRelationshipProperties | 63.0 | 456.5 | 56.0 | 467.0 | 56.0 | 499.0 | 56.0 | 456.0 | 54.0 | DNF
Classification update | updateEntityClassification | 96.0 | 1178.5 | 92.5 | 1259.5 | 87.0 | 1410.0 | 90.0 | 1262.0 | 88.0 | DNF
Entity undo | undoEntityUpdate | 49.0 | -- | 53.0 | -- | 50.0 | -- | 48.0 | -- | 44.0 | --
Relationship undo | undoRelationshipUpdate | 56.0 | -- | 55.0 | -- | 54.0 | -- | 53.0 | -- | 52.0 | --
Entity retrieval | getEntityDetail | 17.0 | 18.0 | 16.0 | 18.0 | 16.0 | 16.0 | 16.0 | 16.0 | 16.0 | DNF
... | getEntitySummary | 17.0 | 17.0 | 16.0 | 17.0 | 16.0 | 15.0 | 16.0 | 15.0 | 16.0 | DNF
... | isEntityKnown | 17.0 | 19.0 | 16.0 | 18.0 | 16.0 | 16.0 | 16.0 | 16.0 | 16.0 | DNF
Entity history retrieval | getEntityDetail | 20.0 | -- | 19.0 | -- | 19.0 | -- | 19.0 | -- | 19.0 | --
... | getEntityDetailHistory | 22.0 | -- | 21.0 | -- | 21.0 | -- | 21.0 | -- | 21.0 | --
Relationship retrieval | getRelationship | 18.0 | 23.0 | 17.0 | 20.0 | 17.0 | 19.0 | 18.0 | 18.0 | 17.0 | DNF
... | isRelationshipKnown | 18.0 | 23.0 | 17.0 | 20.0 | 17.0 | 19.0 | 18.0 | 18.0 | 17.0 | DNF
Relationship history retrieval | getRelationship | 21.0 | -- | 21.0 | -- | 21.0 | -- | 21.0 | -- | 21.0 | --
... | getRelationshipHistory | 23.0 | -- | 22.0 | -- | 22.0 | -- | 22.0 | -- | 22.0 | --
Entity history search | findEntities | 60.5 | -- | 89.0 | -- | 140.0 | -- | 549.5 | -- | 1574.0 | --
... | findEntitiesByProperty | 31.0 | -- | 34.0 | -- | 40.0 | -- | 55.0 | -- | 73.0 | --
... | findEntitiesByPropertyValue | 54.0 | -- | 75.0 | -- | 129.5 | -- | 295.5 | -- | 676.0 | --
Relationship history search | findRelationships | 28.0 | -- | 34.0 | -- | 43.0 | -- | 49.0 | -- | 49.0 | --
... | findRelationshipsByProperty | 33.0 | -- | 41.0 | -- | 55.0 | -- | 63.0 | -- | 65.0 | --
... | findRelationshipsByPropertyValue | 55.0 | -- | 84.0 | -- | 143.0 | -- | 228.0 | -- | 516.0 | --
Graph queries | getEntityNeighborhood | 27.0 | -- | 26.0 | -- | 24.0 | -- | -- | -- | -- | --
... | getLinkingEntities | 21.0 | -- | 25.0 | -- | 26.0 | -- | -- | -- | -- | --
... | getRelatedEntities | 563.0 | -- | 1057.0 | -- | 1873.0 | -- | -- | -- | -- | --
... | getRelationshipsForEntity | 26.0 | -- | 27.0 | -- | 25.0 | -- | -- | -- | -- | --
Graph history queries | getEntityNeighborhood | 26.0 | -- | 25.0 | -- | 24.0 | -- | -- | -- | -- | --
... | getLinkingEntities | 21.0 | -- | 25.0 | -- | 26.0 | -- | -- | -- | -- | --
... | getRelatedEntities | 559.5 | -- | 1057.5 | -- | 1873.0 | -- | -- | -- | -- | --
... | getRelationshipsForEntity | 25.0 | -- | 25.0 | -- | 24.0 | -- | -- | -- | -- | --
Entity re-home | reHomeEntity | 46.0 | 759.0 | 45.0 | 739.0 | 44.0 | 909.0 | 51.0 | 775.0 | 45.0 | DNF
Relationship re-home | reHomeRelationship | 43.0 | 405.5 | 45.0 | 394.0 | 41.0 | 453.0 | 46.0 | 394.0 | 44.0 | DNF
Entity declassify | declassifyEntity | 66.0 | 1302.0 | 63.0 | 1374.5 | 63.0 | 1629.0 | 68.5 | 1420.0 | 64.0 | DNF
... | purgeClassificationReferenceCopy | 58.0 | -- | 55.5 | -- | 55.5 | -- | 62.0 | -- | 56.0 | --
Entity re-identify | reIdentifyEntity | 55.0 | 1745.0 | 51.0 | 1735.0 | 49.0 | 2310.5 | 64.0 | 1864.0 | 56.0 | DNF
Relationship re-identify | reIdentifyRelationship | 44.0 | 855.0 | 47.0 | 823.5 | 40.0 | 950.5 | 49.0 | 885.0 | 44.0 | DNF
Relationship delete | deleteRelationship | 40.0 | 398.0 | 40.0 | 407.0 | 39.0 | 466.0 | 47.0 | 434.0 | 41.0 | DNF
Entity delete | deleteEntity | 45.0 | 785.0 | 45.0 | 824.0 | 43.0 | 1054.0 | 55.0 | 886.0 | 48.0 | DNF
Entity restore | restoreEntity | 39.0 | 809.5 | 39.0 | 871.0 | 37.0 | 1091.0 | 45.0 | 874.0 | 40.0 | DNF
Relationship restore | restoreRelationship | 37.0 | 395.0 | 39.0 | 401.0 | 36.0 | 517.0 | 43.0 | 443.0 | 36.0 | DNF
Relationship purge | purgeRelationship | 32.0 | 146.0 | 32.0 | 194.0 | 30.0 | 210.0 | 39.0 | 202.0 | 33.0 | DNF
... | purgeRelationshipReferenceCopy | 23.0 | 118.0 | 24.0 | 116.0 | 22.0 | 126.0 | 27.0 | 117.0 | 24.0 | DNF
Entity purge | purgeEntity | 40.0 | 271.0 | 40.0 | 381.0 | 40.0 | 433.5 | 52.0 | 416.0 | 45.0 | DNF
... | purgeEntityReferenceCopy | 24.0 | 271.0 | 24.0 | 259.0 | 24.0 | 277.0 | 29.0 | 253.0 | 26.0 | DNF

## Reproducibility

### Re-running the tests

Two Helm charts are provided, that were used to automate the execution of these suites against the XTDB repository connector:

- [The Helm chart used to execute the CTS suite :material-github:](https://github.com/odpi/egeria-connector-xtdb/tree/main/cts/charts/ec-cts-xtdb){ target=gh }
- [The Helm chart used to execute the PTS suite :material-github:](https://github.com/odpi/egeria-connector-xtdb/tree/main/cts/charts/ec-pts-xtdb){ target=gh }

These use a default configuration for the XTDB repository where Lucene is used as a text index and RocksDB is used for all persistence: index store, document store and transaction log. No additional tuning of any parameters (XTDB or RocksDB) is applied: they use all of their default settings.

### Data points

The [`cts/results` :material-github:](https://github.com/odpi/egeria-connector-xtdb/tree/main/cts/results){ target=gh } directory in the code repository for the connector contains results of running the suites against the XTDB connector. For each test suite execution, you will find the following details:

- `openmetadata_cts_summary.json` - a summary of the results of each profile
- Description of the k8s environment
    - `deployment` - details of the deployed components used for the test
    - `configmap.yaml` - details of the variables used within the components of the test
- The OMAG Server configurations:
    - `omag.server.[crux|xtdb].config` - the configuration of the XTDB connector (proxy)
    - `omag.server.cts.config` - the configuration of the test workbench
- The cohort registrations:
    - `cohort.coco.[crux|xtdb].local` - the local XTDB connector (proxy) cohort registration information
    - `cohort.coco.[crux|xtdb].remote` - the cohort members considered remote from the XTDB connector (proxy)'s perspective
    - `cohort.coco.cts.local` - the local test Workbench cohort registration
    - `cohort.coco.cts.remote` - the cohort members considered remote from the test Workbench's perspective
- Detailed results:
    - `pd.tar.gz` - an archive containing the full detailed results of every profile tested
    - `tcd.tar.gz` - an archive containing the full detailed results of every test case executed
- Jupyter Notebooks used to analyze the results:
    - `analyze-performance-results.ipynb` - details about the environment, instance counts, and distribution of elapsed times per method, also illustrating how the results can be analyzed more deeply
    - `calculate-medians.ipynb` - used to calculate the medians displayed in the table further below
    - (to run either of these notebooks, you will need to first extract the `pd.tar.gz` file to have the JSON results files for analysis)

--8<-- "snippets/abbr.md"
