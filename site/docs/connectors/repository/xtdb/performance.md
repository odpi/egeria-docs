<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# XTDB Connector Performance

Following are details on XTDB's performance at the latest release of the connector (v3.2, using XTDB v1.19.0). All raw metrics and elements used to produce the results are described further under [reproducibility](#reproducibility) below, but the historical details themselves are no longer included below in the interest of being concise.

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

Profile | Method | 05-02 (4,900) | 10-05 (9,800) | 20-10 (19,600) | 40-10 (39,200) | 80-10 (78,400)
---|---|---|---|---|---|---
Entity creation | addEntity | 54.0 | 53.0 | 53.0 | 50.0 | 51.0
... | saveEntityReferenceCopy | 49.0 | 48.0 | 49.0 | 47.0 | 48.0
Entity search | findEntities | 49.0 | 68.0 | 104.0 | 237.0 | 590.0
... | findEntitiesByProperty | 31.0 | 38.0 | 52.0 | 98.0 | 185.0
... | findEntitiesByPropertyValue | 47.0 | 61.0 | 88.5 | 129.0 | 258.0
Relationship creation | addRelationship | 52.0 | 50.0 | 51.0 | 50.0 | 51.0
... | saveRelationshipReferenceCopy | 54.0 | 53.0 | 53.0 | 53.0 | 53.0
Relationship search | findRelationships | 27.0 | 33.0 | 40.0 | 40.0 | 45.0
... | findRelationshipsByProperty | 30.0 | 37.0 | 54.0 | 114.0 | 207.0
... | findRelationshipsByPropertyValue | 45.5 | 52.0 | 77.5 | 128.0 | 256.0
Entity classification | classifyEntity | 83.0 | 80.0 | 80.0 | 80.0 | 83.0
... | saveClassificationReferenceCopy | 78.0 | 74.0 | 75.0 | 75.0 | 76.0
Classification search | findEntitiesByClassification | 36.0 | 46.0 | 63.0 | 91.0 | 125.0
Entity update | nullPropertiesForEntities | 52.0 | 49.0 | 47.0 | 53.0 | 50.0
... | updateEntityProperties | 54.0 | 54.0 | 57.0 | 54.0 | 54.0
Relationship update | updateRelationshipProperties | 62.0 | 59.0 | 65.0 | 60.0 | 58.0
Classification update | updateEntityClassification | 99.0 | 113.0 | 102.0 | 108.0 | 101.0
Entity undo | undoEntityUpdate | 49.0 | 51.0 | 50.0 | 49.0 | 47.0
Relationship undo | undoRelationshipUpdate | 55.0 | 56.0 | 56.0 | 55.0 | 58.0
Entity retrieval | getEntityDetail | 16.0 | 17.0 | 16.0 | 17.0 | 18.0
... | getEntitySummary | 16.0 | 16.0 | 16.0 | 17.0 | 18.0
... | isEntityKnown | 16.0 | 17.0 | 16.0 | 17.0 | 18.0
Entity history retrieval | getEntityDetail | 19.0 | 20.0 | 20.0 | 21.0 | 22.0
... | getEntityDetailHistory | 21.0 | 22.0 | 22.0 | 22.0 | 23.0
Relationship retrieval | getRelationship | 18.0 | 18.0 | 18.0 | 19.0 | 18.0
... | isRelationshipKnown | 18.0 | 18.0 | 18.0 | 19.0 | 18.0
Relationship history retrieval | getRelationship | 21.0 | 22.0 | 22.0 | 23.0 | 22.0
... | getRelationshipHistory | 22.0 | 23.0 | 23.0 | 24.0 | 23.0
Entity history search | findEntities | 57.0 | 94.5 | 162.0 | 627.0 | 1898.0
... | findEntitiesByProperty | 31.0 | 37.0 | 44.0 | 62.0 | 96.0
... | findEntitiesByPropertyValue | 44.0 | 60.0 | 90.0 | 184.0 | 428.0
Relationship history search | findRelationships | 28.0 | 38.0 | 45.0 | 52.0 | 56.0
... | findRelationshipsByProperty | 32.0 | 47.0 | 52.0 | 64.0 | 74.0
... | findRelationshipsByPropertyValue | 53.0 | 82.0 | 119.0 | 202.5 | 374.0
Graph queries | getEntityNeighborhood | 28.0 | 28.0 | 28.0 | -- | --
... | getLinkingEntities | 22.0 | 27.0 | 30.0 | -- | --
... | getRelatedEntities | 507.0 | 1182.0 | 2296.0 | -- | --
... | getRelationshipsForEntity | 26.5 | 29.0 | 29.0 | -- | --
Graph history queries | getEntityNeighborhood | 26.0 | 27.0 | 27.0 | -- | --
... | getLinkingEntities | 22.0 | 27.0 | 31.0 | -- | --
... | getRelatedEntities | 502.0 | 1183.5 | 2295.0 | -- | --
... | getRelationshipsForEntity | 25.0 | 26.0 | 27.0 | -- | --
Entity re-home | reHomeEntity | 50.0 | 49.0 | 49.0 | 53.0 | 50.0
Relationship re-home | reHomeRelationship | 46.0 | 46.0 | 45.0 | 49.0 | 47.0
Entity declassify | declassifyEntity | 62.0 | 58.5 | 57.0 | 62.0 | 65.0
... | purgeClassificationReferenceCopy | 59.0 | 56.0 | 53.0 | 57.0 | 58.0
Entity re-identify | reIdentifyEntity | 57.0 | 52.0 | 55.0 | 64.0 | 59.0
Relationship re-identify | reIdentifyRelationship | 48.0 | 45.0 | 48.0 | 53.0 | 49.0
Relationship delete | deleteRelationship | 46.0 | 44.0 | 46.0 | 52.0 | 47.0
Entity delete | deleteEntity | 51.0 | 49.0 | 50.0 | 55.0 | 53.0
Entity restore | restoreEntity | 46.0 | 42.0 | 42.0 | 45.0 | 44.0
Relationship restore | restoreRelationship | 43.0 | 39.0 | 41.0 | 41.0 | 41.0
Relationship purge | purgeRelationship | 34.0 | 33.0 | 35.0 | 40.0 | 37.0
... | purgeRelationshipReferenceCopy | 25.0 | 25.0 | 26.0 | 28.0 | 27.0
Entity purge | purgeEntity | 45.0 | 43.0 | 48.0 | 56.0 | 58.0
... | purgeEntityReferenceCopy | 29.0 | 28.0 | 30.0 | 32.0 | 33.0

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
Entity creation | addEntity | 54.0 | 516.0 | 53.0 | 475.0 | 53.0 | 480.0 | 50.0 | 513.0 | 51.0 | DNF
... | saveEntityReferenceCopy | 49.0 | 511.0 | 48.0 | 474.0 | 49.0 | 481.0 | 47.0 | 512.0 | 48.0 | DNF
Entity search | findEntities | 49.0 | 253.5 | 68.0 | 482.0 | 104.0 | 825.0 | 237.0 | 2214.0 | 590.0 | DNF
... | findEntitiesByProperty | 31.0 | 41.0 | 38.0 | 52.0 | 52.0 | 65.0 | 98.0 | 126.0 | 185.0 | DNF
... | findEntitiesByPropertyValue | 47.0 | 82.0 | 61.0 | 102.0 | 88.5 | 110.0 | 129.0 | 178.0 | 258.0 | DNF
Relationship creation | addRelationship | 52.0 | 170.0 | 50.0 | 164.0 | 51.0 | 159.0 | 50.0 | 168.0 | 51.0 | DNF
... | saveRelationshipReferenceCopy | 54.0 | 487.0 | 53.0 | 452.5 | 53.0 | 500.0 | 53.0 | 459.0 | 53.0 | DNF
Relationship search | findRelationships | 27.0 | 46.0 | 33.0 | 66.0 | 40.0 | 91.0 | 40.0 | 170.0 | 45.0 | DNF
... | findRelationshipsByProperty | 30.0 | 49.0 | 37.0 | 64.0 | 54.0 | 85.0 | 114.0 | 195.0 | 207.0 | DNF
... | findRelationshipsByPropertyValue | 45.5 | 77.0 | 52.0 | 98.5 | 77.5 | 113.5 | 128.0 | 203.0 | 256.0 | DNF
Entity classification | classifyEntity | 83.0 | 1039.5 | 80.0 | 1000.0 | 80.0 | 1065.0 | 80.0 | 1002.0 | 83.0 | DNF
... | saveClassificationReferenceCopy | 78.0 | 857.5 | 74.0 | 928.0 | 75.0 | 993.5 | 75.0 | 940.0 | 76.0 | DNF
Classification search | findEntitiesByClassification | 36.0 | 1277.0 | 46.0 | 2155.0 | 63.0 | 3483.5 | 91.0 | 8786.0 | 125.0 | DNF
Entity update | nullPropertiesForEntities | 52.0 | 424.0 | 49.0 | 379.0 | 47.0 | 405.0 | 53.0 | 413.0 | 50.0 | DNF
... | updateEntityProperties | 54.0 | 789.0 | 54.0 | 737.0 | 57.0 | 761.0 | 54.0 | 775.0 | 54.0 | DNF
Relationship update | updateRelationshipProperties | 62.0 | 518.0 | 59.0 | 469.0 | 65.0 | 527.0 | 60.0 | 527.0 | 58.0 | DNF
Classification update | updateEntityClassification | 99.0 | 1613.0 | 113.0 | 1540.0 | 102.0 | 1632.0 | 108.0 | 1598.0 | 101.0 | DNF
Entity undo | undoEntityUpdate | 49.0 | -- | 51.0 | -- | 50.0 | -- | 49.0 | -- | 47.0 | --
Relationship undo | undoRelationshipUpdate | 55.0 | -- | 56.0 | -- | 56.0 | -- | 55.0 | -- | 58.0 | --
Entity retrieval | getEntityDetail | 16.0 | 20.0 | 17.0 | 18.0 | 16.0 | 17.0 | 17.0 | 20.0 | 18.0 | DNF
... | getEntitySummary | 16.0 | 19.0 | 16.0 | 17.0 | 16.0 | 16.0 | 17.0 | 19.0 | 18.0 | DNF
... | isEntityKnown | 16.0 | 20.0 | 17.0 | 19.0 | 16.0 | 17.0 | 17.0 | 20.0 | 18.0 | DNF
Entity history retrieval | getEntityDetail | 19.0 | -- | 20.0 | -- | 20.0 | -- | 21.0 | -- | 22.0 | --
... | getEntityDetailHistory | 21.0 | -- | 22.0 | -- | 22.0 | -- | 22.0 | -- | 23.0 | --
Relationship retrieval | getRelationship | 18.0 | 23.0 | 18.0 | 21.0 | 18.0 | 19.0 | 19.0 | 22.0 | 18.0 | DNF
... | isRelationshipKnown | 18.0 | 23.0 | 18.0 | 21.0 | 18.0 | 19.0 | 19.0 | 22.0 | 18.0 | DNF
Relationship history retrieval | getRelationship | 21.0 | -- | 22.0 | -- | 22.0 | -- | 23.0 | -- | 22.0 | --
... | getRelationshipHistory | 22.0 | -- | 23.0 | -- | 23.0 | -- | 24.0 | -- | 23.0 | --
Entity history search | findEntities | 57.0 | -- | 94.5 | -- | 162.0 | -- | 627.0 | -- | 1898.0 | --
... | findEntitiesByProperty | 31.0 | -- | 37.0 | -- | 44.0 | -- | 62.0 | -- | 96.0 | --
... | findEntitiesByPropertyValue | 44.0 | -- | 60.0 | -- | 90.0 | -- | 184.0 | -- | 428.0 | --
Relationship history search | findRelationships | 28.0 | -- | 38.0 | -- | 45.0 | -- | 52.0 | -- | 56.0 | --
... | findRelationshipsByProperty | 32.0 | -- | 47.0 | -- | 52.0 | -- | 64.0 | -- | 74.0 | --
... | findRelationshipsByPropertyValue | 53.0 | -- | 82.0 | -- | 119.0 | -- | 202.5 | -- | 374.0 | --
Graph queries | getEntityNeighborhood | 28.0 | -- | 28.0 | -- | 28.0 | -- | -- | -- | -- | --
... | getLinkingEntities | 22.0 | -- | 27.0 | -- | 30.0 | -- | -- | -- | -- | --
... | getRelatedEntities | 507.0 | -- | 1182.0 | -- | 2296.0 | -- | -- | -- | -- | --
... | getRelationshipsForEntity | 26.5 | -- | 29.0 | -- | 29.0 | -- | -- | -- | -- | --
Graph history queries | getEntityNeighborhood | 26.0 | -- | 27.0 | -- | 27.0 | -- | -- | -- | --
... | getLinkingEntities | 22.0 | -- | 27.0 | -- | 31.0 | -- | -- | -- | -- | --
... | getRelatedEntities | 502.0 | -- | 1183.5 | -- | 2295.0 | -- | -- | -- | -- | --
... | getRelationshipsForEntity | 25.0 | -- | 26.0 | -- | 27.0 | -- | -- | -- | -- | --
Entity re-home | reHomeEntity | 50.0 | 865.0 | 49.0 | 761.0 | 49.0 | 823.0 | 53.0 | 813.0 | 50.0 | DNF
Relationship re-home | reHomeRelationship | 46.0 | 456.0 | 46.0 | 398.0 | 45.0 | 435.0 | 49.0 | 429.0 | 47.0 | DNF
Entity declassify | declassifyEntity | 62.0 | 1608.5 | 58.5 | 1636.0 | 57.0 | 1736.0 | 62.0 | 1713.0 | 65.0 | DNF
... | purgeClassificationReferenceCopy | 59.0 | -- | 56.0 | -- | 53.0 | -- | 57.0 | -- | 58.0 | --
Entity re-identify | reIdentifyEntity | 57.0 | 1970.0 | 52.0 | 1830.0 | 55.0 | 1972.0 | 64.0 | 2024.0 | 59.0 | DNF
Relationship re-identify | reIdentifyRelationship | 48.0 | 875.0 | 45.0 | 843.0 | 48.0 | 885.0 | 53.0 | 913.0 | 49.0 | DNF
Relationship delete | deleteRelationship | 46.0 | 443.5 | 44.0 | 436.0 | 46.0 | 459.0 | 52.0 | 471.0 | 47.0 | DNF
Entity delete | deleteEntity | 51.0 | 919.0 | 49.0 | 911.0 | 50.0 | 1003.0 | 55.0 | 904.0 | 53.0 | DNF
Entity restore | restoreEntity | 46.0 | 915.0 | 42.0 | 895.0 | 42.0 | 987.0 | 45.0 | 859.0 | 44.0 | DNF
Relationship restore | restoreRelationship | 43.0 | 404.0 | 39.0 | 424.0 | 41.0 | 441.5 | 41.0 | 435.0 | 41.0 | DNF
Relationship purge | purgeRelationship | 34.0 | 199.0 | 33.0 | 210.0 | 35.0 | 200.0 | 40.0 | 210.0 | 37.0 | DNF
... | purgeRelationshipReferenceCopy | 25.0 | 121.0 | 25.0 | 126.0 | 26.0 | 121.5 | 28.0 | 126.0 | 27.0 | DNF
Entity purge | purgeEntity | 45.0 | 381.0 | 43.0 | 428.0 | 48.0 | 431.5 | 56.0 | 431.0 | 58.0 | DNF
... | purgeEntityReferenceCopy | 29.0 | 289.0 | 28.0 | 286.0 | 30.0 | 276.0 | 32.0 | 285.0 | 33.0 | DNF

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
