<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# XTDB Connector Performance

Following are details on XTDB's performance at the latest release of the connector (v3.3, using XTDB v1.19.0). All raw metrics and elements used to produce the results are described further under [reproducibility](#reproducibility) below, but the historical details themselves are no longer included below in the interest of being concise.

??? info "Details on the performance metrics"
    The *median* of all results for that method across all executions for a given set of volume parameters is given (all times in milliseconds) to give an idea of the "typical" result, while limiting potential skew from significant outliers.

    A more detailed set of statistics is best reviewed through the Jupyter Notebook provided in each results directory, where you can review:

    - the full distributions of execution times (including the outliers)
    - detailed individual outlier results (e.g. the top-10 slowest response times per method)
    - volumes in place during the tests (how many entities, how many relationships, etc)
    
    The volume parameters that were used for each test are specified using the convention `i-s`, where `i` is the value for the `instancesPerType` parameter to the PTS and `s` is the value for `maxSearchResults`. For example, `0005-02` means 5 instances will be created for every open metadata type and 2 will be the maximum number of results per page for methods that include paging.

    - All tests are run from `0005-02` through `0020-10` to give a sense of the performance impact of doubling the number of instances and search results.
    - Above this, the graph queries are no longer included: they become exponentially more complex as the volumes grow, and while they will still return results, the depth of their testing in the PTS means that they can contribute many hours (or even days) to the overall suite execution -- they are therefore left out to be able to more quickly produce results for the other methods at progressively higher volumes.
    - The page size is left at a maximum of `10` for subsequent tests so that it is only the volume of instances in total that are doubling each time, rather than also the number of detailed results.
    - Instance counts range from a few thousand (at `0005-02`) up to nearly one hundred thousand (at `0080-10`).
    - If time allows prior to the next release cycle, the XTDB connector will continue to be tested up to higher volumes (ideally up to `1280-10`, which is approximately 1.25 million metadata instances).

    In the graphical comparisons, a point plot is used to show the typical execution time of each method at the different volumes / by repository. Each point on the plot represents the _median_ execution time for that method, at a given volume of metadata. (For the repository comparison plots, `p` = XTDB and `g` = JanusGraph.) The horizontal lines that appear around each point are confidence intervals calculated by a bootstrapping process: in simple terms, the larger the horizontal line, the more variability there is for that particular method's execution time (a singular median value is insufficient to represent such variability on its own).

## XTDB at varying volumes

!!! summary
    The retrieval and write operations remain very consistent, with almost no variability, throughout the growth in volume. The search operations, however, begin to clearly degrade at the highest volumes tested. Further investigation into other optimized settings for the search operations for these larger volumes is likely warranted as the next step to continue to improve performance.

![Graphical comparison](volume_comparison.svg)

Profile | Method | 0005-02 (4,900) | 0010-05 (9,800) | 0020-10 (19,600) | 0040-10 (39,200) | 0080-10 (78,400) | 0160-10 (156,800) | 0320-10 (313,600) | 0640-10 (627,200) | 1280-10 (1,254,400)
---|---|---|---|---|---|---|---|---|---|---
Entity creation | addEntity | 54.0 | 57.0 | 53.0 | 56.0 | 66.0 | 61.0
... | saveEntityReferenceCopy | 50.0 | 52.0 | 49.0 | 53.0 | 62.0 | 56.0
Entity search | findEntities | 29.0 | 39.0 | 42.0 | 67.0 | 95.0 | 218.0
... | findEntitiesByProperty | 30.0 | 32.0 | 35.0 | 51.0 | 77.0 | 220.0
... | findEntitiesByPropertyValue | 38.0 | 54.0 | 60.0 | 94.0 | 139.0 | 304.5
Relationship creation | addRelationship | 52.0 | 56.0 | 52.0 | 55.0 | 65.0 | 55.0
... | saveRelationshipReferenceCopy | 57.0 | 61.0 | 57.0 | 64.0 | 73.0 | 62.0
Relationship search | findRelationships | 24.0 | 31.0 | 33.0 | 39.0 | 32.0 | 40.0
... | findRelationshipsByProperty | 31.0 | 33.0 | 39.0 | 64.0 | 110.0 | 312.5
... | findRelationshipsByPropertyValue | 39.0 | 52.0 | 62.5 | 109.0 | 154.0 | 346.5
Entity classification | classifyEntity | 85.0 | 93.5 | 89.0 | 95.5 | 105.0 | 95.0
... | saveClassificationReferenceCopy | 81.0 | 90.0 | 82.0 | 89.0 | 100.0 | 89.0
Classification search | findEntitiesByClassification | 34.0 | 42.0 | 56.0 | 81.0 | 94.0 | 134.0
Entity update | nullPropertiesForEntities | 58.0 | 50.0 | 50.0 | 57.0 | 61.0 | 55.0
... | updateEntityProperties | 57.0 | 58.0 | 56.0 | 61.0 | 68.0 | 57.0
Relationship update | updateRelationshipProperties | 64.0 | 63.0 | 61.0 | 67.0 | 72.0 | 63.0
Classification update | updateEntityClassification | 110.5 | 101.0 | 127.0 | 124.0 | 136.0 | 141.0
Entity undo | undoEntityUpdate | 51.0 | 53.0 | 52.0 | 54.0 | 66.0 | 58.0
Relationship undo | undoRelationshipUpdate | 56.0 | 59.0 | 60.0 | 59.0 | 68.0 | 62.0
Entity retrieval | getEntityDetail | 16.0 | 16.0 | 15.0 | 16.0 | 14.0 | 16.0
... | getEntitySummary | 16.0 | 16.0 | 15.0 | 15.0 | 14.0 | 15.0
... | isEntityKnown | 16.0 | 16.0 | 15.0 | 16.0 | 14.0 | 16.0
Entity history retrieval | getEntityDetail | 19.0 | 20.0 | 18.0 | 19.0 | 18.0 | 19.0
... | getEntityDetailHistory | 21.0 | 21.0 | 20.0 | 21.0 | 19.0 | 21.0
Relationship retrieval | getRelationship | 17.0 | 17.0 | 16.0 | 17.0 | 15.0 | 16.0
... | isRelationshipKnown | 17.0 | 17.0 | 17.0 | 17.0 | 16.0 | 16.0
Relationship history retrieval | getRelationship | 21.0 | 21.0 | 20.0 | 21.0 | 19.0 | 20.0
... | getRelationshipHistory | 22.0 | 22.0 | 21.0 | 22.0 | 20.0 | 21.0
Entity history search | findEntities | 32.0 | 42.0 | 52.0 | 80.0 | 129.0 | 284.0
... | findEntitiesByProperty | 27.0 | 32.0 | 34.0 | 38.0 | 46.0 | 75.0
... | findEntitiesByPropertyValue | 38.0 | 51.0 | 71.0 | 106.0 | 171.0 | 360.0
Relationship history search | findRelationships | 27.0 | 34.0 | 43.0 | 42.0 | 39.0 | 53.0
... | findRelationshipsByProperty | 31.0 | 44.0 | 54.0 | 55.5 | 53.0 | 71.0
... | findRelationshipsByPropertyValue | 48.5 | 77.5 | 124.0 | 135.5 | 208.5 | 467.5
Graph queries | getEntityNeighborhood | 28.0 | 25.0 | 25.0 | -- | -- | 26.0
... | getLinkingEntities | 22.0 | 25.0 | 27.0 | -- | -- | --
... | getRelatedEntities | 356.0 | 701.5 | 1313.0 | -- | -- | --
... | getRelationshipsForEntity | 26.0 | 26.0 | 27.0 | 28.0 | 27.0 | 28.0
Graph history queries | getEntityNeighborhood | 27.0 | 24.0 | 24.0 | -- | -- | 25.0
... | getLinkingEntities | 22.0 | 25.0 | 27.0 | -- | -- | --
... | getRelatedEntities | 360.0 | 702.0 | 1318.0 | -- | -- | --
... | getRelationshipsForEntity | 24.0 | 24.0 | 25.0 | 27.0 | 25.0 | 26.0
Entity re-home | reHomeEntity | 68.5 | 55.0 | 50.0 | 62.0 | 73.0 | 56.0
Relationship re-home | reHomeRelationship | 59.0 | 50.0 | 47.0 | 55.0 | 49.0 | 47.0
Entity declassify | declassifyEntity | 75.0 | 66.5 | 65.0 | 67.0 | 71.0 | 68.5
... | purgeClassificationReferenceCopy | 67.0 | 65.0 | 58.0 | 62.0 | 68.0 | 68.0
Entity re-identify | reIdentifyEntity | 71.0 | 59.0 | 59.0 | 68.0 | 68.0 | 67.0
Relationship re-identify | reIdentifyRelationship | 58.0 | 50.0 | 48.0 | 55.0 | 57.0 | 49.0
Relationship delete | deleteRelationship | 54.0 | 48.0 | 45.0 | 50.0 | 50.0 | 47.0
Entity delete | deleteEntity | 67.0 | 54.0 | 53.0 | 57.0 | 60.0 | 58.0
Entity restore | restoreEntity | 60.0 | 50.0 | 45.0 | 47.0 | 51.0 | 49.0
Relationship restore | restoreRelationship | 48.0 | 44.0 | 40.0 | 44.0 | 45.0 | 44.0
Relationship purge | purgeRelationship | 34.0 | 32.0 | 31.0 | 32.0 | 32.0 | 34.0
... | purgeRelationshipReferenceCopy | 28.0 | 26.0 | 25.0 | 25.0 | 25.0 | 27.0
Entity purge | purgeEntity | 43.0 | 38.0 | 38.0 | 41.0 | 42.0 | 132.0
... | purgeEntityReferenceCopy | 32.0 | 28.0 | 28.0 | 29.0 | 30.0 | 92.0

## XTDB vs JanusGraph

!!! summary
    In almost all cases, the XTDB repository is *significantly* faster than JanusGraph: at most volumes completing all methods in less than 100ms and with very little variability. For JanusGraph, on the other hand, there is significant variability (in particular for methods like `findEntitiesByClassification`), and there are numerous examples of the median execution time taking more than multiple seconds.

    Even at 8 times the volume of metadata the XTDB connector still outperforms the JanusGraph connector in almost every method (the only exceptions being a few of the find methods, where the performance is approximately even at 2-4 times the volume).

!!! attention "Graph queries were disabled for JanusGraph"
    The graph queries were disabled for JanusGraph in order to have results in a timely manner: it would take more than a month to produce results for these queries for the JanusGraph connector. In addition, the 0040-10 and beyond scales were stopped when a single test scenario ran for more than 5 consecutive days (120 hours) without completing.

![Graphical comparison](repo_comparison.svg)

The XTDB results can be difficult to see in detail due to the skew from the Janus results, so it may be easier to look at this more granular comparison that drops the higher scales of Janus for readability of the XTDB results:

![Graphical comparison without large Janus volumes](repo_comparison_granular.svg)

Profile | Method | 0005-02 (XTDB) | 0005-02 (Janus) | 0010-05 (XTDB) | 0010-05 (Janus) | 0020-10 (XTDB) | 0020-10 (Janus) | 0040-10 (XTDB) | 0040-10 (Janus) | 0080-10 (XTDB) | 0080-10 (Janus) | 0160-10 (XTDB)
---|---|---|---|---|---|---|---|---|---|---|---|---
Entity creation | addEntity | 54.0 | 547.0 | 57.0 | 483.0 | 53.0 | 492.0 | 56.0 | DNF | 66.0 | DNF | 61.0
... | saveEntityReferenceCopy | 50.0 | 542.0 | 52.0 | 483.0 | 49.0 | 490.0 | 53.0 | DNF | 62.0 | DNF | 56.0
Entity search | findEntities | 29.0 | 356.0 | 39.0 | 487.0 | 42.0 | 852.0 | 67.0 | DNF | 95.0 | DNF | 218.0
... | findEntitiesByProperty | 30.0 | 42.0 | 32.0 | 54.0 | 35.0 | 71.0 | 51.0 | DNF | 77.0 | DNF | 220.0
... | findEntitiesByPropertyValue | 38.0 | 101.0 | 54.0 | 114.0 | 60.0 | 121.0 | 94.0 | DNF | 139.0 | DNF | 304.5
Relationship creation | addRelationship | 52.0 | 239.0 | 56.0 | 172.0 | 52.0 | 174.0 | 55.0 | DNF | 65.0 | DNF | 55.0
... | saveRelationshipReferenceCopy | 57.0 | 757.0 | 61.0 | 468.0 | 57.0 | 498.0 | 64.0 | DNF | 73.0 | DNF | 62.0
Relationship search | findRelationships | 24.0 | 51.0 | 31.0 | 65.0 | 33.0 | 97.0 | 39.0 | DNF | 32.0 | DNF | 40.0
... | findRelationshipsByProperty | 31.0 | 50.0 | 33.0 | 66.5 | 39.0 | 103.0 | 64.0 | DNF | 110.0 | DNF | 312.5
... | findRelationshipsByPropertyValue | 39.0 | 87.0 | 52.0 | 98.0 | 62.5 | 125.5 | 109.0 | DNF | 154.0 | DNF | 346.6
Entity classification | classifyEntity | 85.0 | 1369.0 | 93.5 | 1019.5 | 89.0 | 1052.0 | 95.5 | DNF | 105.0 | DNF | 95.0
... | saveClassificationReferenceCopy | 81.0 | 1139.0 | 90.0 | 948.5 | 82.0 | 982.0 | 89.0 | DNF | 100.0 | DNF | 89.0
Classification search | findEntitiesByClassification | 34.0 | 1697.0 | 42.0 | 2709.0 | 56.0 | 4354.5 | 81.0 | DNF | 94.0 | DNF | 134.0
Entity update | nullPropertiesForEntities | 58.0 | 578.0 | 50.0 | 380.0 | 50.0 | 407.0 | 57.0 | DNF | 61.0 | DNF | 55.0
... | updateEntityProperties | 57.0 | 894.0 | 58.0 | 744.0 | 56.0 | 752.0 | 61.0 | DNF | 68.0 | DNF | 57.0
Relationship update | updateRelationshipProperties | 64.0 | 678.0 | 63.0 | 490.5 | 61.0 | 493.0 | 67.0 | DNF | 72.0 | DNF | 63.0
Classification update | updateEntityClassification | 110.5 | 2082.0 | 101.0 | 1543.0 | 127.0 | 1757.0 | 124.0 | DNF | 136.0 | DNF | 141.0 
Entity undo | undoEntityUpdate | 51.0 | -- | 53.0 | -- | 52.0 | -- | 54.0 | -- | 66.0 | -- | 58.0
Relationship undo | undoRelationshipUpdate | 56.0 | -- | 59.0 | -- | 60.0 | -- | 59.0 | -- | 68.0 | -- | 62.0
Entity retrieval | getEntityDetail | 16.0 | 17.0 | 16.0 | 19.0 | 15.0 | 15.0 | 16.0 | DNF | 14.0 | DNF | 16.0
... | getEntitySummary | 16.0 | 16.0 | 16.0 | 18.0 | 15.0 | 14.0 | 15.0 | DNF | 14.0 | DNF | 15.0
... | isEntityKnown | 16.0 | 18.0 | 16.0 | 19.0 | 15.0 | 16.0 | 16.0 | DNF | 14.0 | DNF | 16.0
Entity history retrieval | getEntityDetail | 19.0 | -- | 20.0 | -- | 18.0 | -- | 19.0 | -- | 18.0 | -- | 19.0
... | getEntityDetailHistory | 21.0 | -- | 21.0 | -- | 20.0 | -- | 21.0 | -- | 19.0 | -- | 21.0
Relationship retrieval | getRelationship | 17.0 | 20.0 | 17.0 | 23.0 | 16.0 | 17.0 | 17.0 | DNF | 15.0 | DNF | 16.0
... | isRelationshipKnown | 17.0 | 21.0 | 17.0 | 23.0 | 17.0 | 17.0 | 17.0 | DNF | 16.0 | DNF | 16.0
Relationship history retrieval | getRelationship | 21.0 | -- | 21.0 | -- | 20.0 | -- | 21.0 | -- | 19.0 | -- | 20.0
... | getRelationshipHistory | 22.0 | -- | 22.0 | -- | 21.0 | -- | 22.0 | -- | 20.0 | -- | 21.0
Entity history search | findEntities | 32.0 | -- | 42.0 | -- | 52.0 | -- | 80.0 | -- | 129.0 | -- | 284.0
... | findEntitiesByProperty | 27.0 | -- | 32.0 | -- | 34.0 | -- | 38.0 | -- | 46.0 | -- | 75.0
... | findEntitiesByPropertyValue | 38.0 | -- | 51.0 | -- | 71.0 | -- | 106.0 | -- | 171.0 | -- | 360.0
Relationship history search | findRelationships | 27.0 | -- | 34.0 | -- | 43.0 | -- | 42.0 | -- | 39.0 | -- | 53.0
... | findRelationshipsByProperty | 31.0 | -- | 44.0 | -- | 54.0 | -- | 55.5 | -- | 53.0 | -- | 71.0
... | findRelationshipsByPropertyValue | 48.5 | -- | 77.5 | -- | 124.0 | -- | 135.5 | -- | 208.5 | -- | 467.5
Graph queries | getEntityNeighborhood | 28.0 | -- | 25.0 | -- | 25.0 | -- | -- | -- | -- | -- | 26.0
... | getLinkingEntities | 22.0 | -- | 25.0 | -- | 27.0 | -- | -- | -- | -- | -- | --
... | getRelatedEntities | 356.0 | -- | 701.5 | -- | 1313.0 | -- | -- | -- | -- | -- | --
... | getRelationshipsForEntity | 26.0 | 41.0 | 26.0 | 43.0 | 27.0 | 31.0 | 28.0 | DNF | 27.0 | DNF | 28.0
Graph history queries | getEntityNeighborhood | 27.0 | -- | 24.0 | -- | 24.0 | -- | -- | -- | -- | -- | 25.0
... | getLinkingEntities | 22.0 | -- | 25.0 | -- | 27.0 | -- | -- | -- | -- | -- | --
... | getRelatedEntities | 360.0 | -- | 702.0 | -- | 1318.0 | -- | -- | -- | -- | --| --
... | getRelationshipsForEntity | 24.0 | -- | 24.0 | -- | 25.0 | -- | 27.0 | -- | 25.0 | -- | 26.0
Entity re-home | reHomeEntity | 68.5 | 1033.0 | 55.0 | 785.0 | 50.0 | 807.0 | 62.0 | DNF | 73.0 | DNF | 56.0
Relationship re-home | reHomeRelationship | 59.0 | 675.0 | 50.0 | 409.0 | 47.0 | 419.0 | 55.0 | DNF | 49.0 | DNF | 47.0
Entity declassify | declassifyEntity | 75.0 | 2237.0 | 66.5 | 1700.0 | 65.0 | 1714.0 | 67.0 | DNF | 71.0 | DNF | 68.5
... | purgeClassificationReferenceCopy | 67.0 | -- | 65.0 | -- | 58.0 | -- | 62.0 | -- | 68.0 | -- | 68.0
Entity re-identify | reIdentifyEntity | 71.0 | 2456.0 | 59.0 | 1793.5 | 59.0 | 1862.0 | 68.0 | DNF | 68.0 | DNF | 67.0
Relationship re-identify | reIdentifyRelationship | 58.0 | 1223.0 | 50.0 | 869.0 | 48.0 | 871.0 | 55.0 | DNF | 57.0 | DNF | 49.0
Relationship delete | deleteRelationship | 54.0 | 622.0 | 48.0 | 437.0 | 45.0 | 453.0 | 50.0 | DNF | 50.0 | DNF | 47.0
Entity delete | deleteEntity | 67.0 | 1162.0 | 54.0 | 891.0 | 53.0 | 941.0 | 57.0 | DNF | 60.0 | DNF | 58.0
Entity restore | restoreEntity | 60.0 | 1099.0 | 50.0 | 880.0 | 45.0 | 897.0 | 47.0 | DNF | 51.0 | DNF | 49.0
Relationship restore | restoreRelationship | 48.0 | 549.0 | 44.0 | 418.5 | 40.0 | 437.0 | 44.0 | DNF | 45.0 | DNF | 44.0
Relationship purge | purgeRelationship | 34.0 | 214.0 | 32.0 | 211.0 | 31.0 | 204.0 | 32.0 | DNF | 32.0 | DNF | 34.0
... | purgeRelationshipReferenceCopy | 28.0 | 130.0 | 26.0 | 122.0 | 25.0 | 122.0 | 25.0 | DNF | 25.0 | DNF | 27.0
Entity purge | purgeEntity | 43.0 | 399.0 | 38.0 | 414.0 | 38.0 | 433.0 | 41.0 | DNF | 42.0 | DNF | 132.0
... | purgeEntityReferenceCopy | 32.0 | 299.0 | 28.0 | 284.0 | 28.0 | 276.5 | 29.0 | DNF | 30.0 | DNF | 92.0

## Reproducibility

### Re-running the tests

Two Helm charts are provided, that were used to automate the execution of these suites against the XTDB repository connector:

- [The Helm chart used to execute the CTS suite](/egeria-docs/guides/operations/kubernetes/charts/cts)
- [The Helm chart used to execute the PTS suite](/egeria-docs/guides/operations/kubernetes/charts/pts)

These use a default configuration for the XTDB repository where Lucene is used as a text index and RocksDB is used for all persistence: index store, document store and transaction log. No additional tuning of any parameters (XTDB or RocksDB) is applied: they use all of their default settings.

### Data points

The [`cts/results` :material-github:](https://github.com/odpi/egeria-connector-xtdb/tree/main/cts/results){ target=gh } directory in the code repository for the connector contains results of running the suites against the XTDB connector. For each test suite execution, you will find the following details:

- `openmetadata_pts_summary.json` - a summary of the results of each profile
- Description of the k8s environment
    - `deployment` - details of the deployed components used for the test
    - `configmap.yaml` - details of the variables used within the components of the test
- The OMAG Server configurations:
    - `omag.server.[tut|xtdb|crux].config` - the configuration of the XTDB connector (proxy)
    - `omag.server.pts.config` - the configuration of the test workbench
- The cohort registrations:
    - `cohort.[pts|coco].[tut|xtdb|crux].local` - the local XTDB connector (proxy) cohort registration information
    - `cohort.[pts|coco].[tut|xtdb|crux].remote` - the cohort members considered remote from the XTDB connector (proxy)'s perspective
    - `cohort.[pts|coco].pts.local` - the local test Workbench cohort registration
    - `cohort.[pts|coco].pts.remote` - the cohort members considered remote from the test Workbench's perspective
- Detailed results:
    - `pd.tar.gz` - an archive containing the full detailed results of every profile tested
    - `tcd.tar.gz` - an archive containing the full detailed results of every test case executed
- Jupyter Notebooks used to analyze the results:
    - `analyze-performance-results.ipynb` - details about the environment, instance counts, and distribution of elapsed times per method, also illustrating how the results can be analyzed more deeply
    - `calculate-medians.ipynb` - used to calculate the medians displayed in the table further below
    - (to run either of these notebooks, you will need to first extract the `pd.tar.gz` file to have the JSON results files for analysis)

--8<-- "snippets/abbr.md"
