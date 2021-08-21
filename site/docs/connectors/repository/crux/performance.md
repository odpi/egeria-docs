<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Crux Connector Performance

Following are details on Crux's performance at the latest release of the connector (v3.0, using Crux v1.18.1). All raw metrics and elements used to produce the results are described further under [reproducibility](#reproducibility) below, but the historical details themselves are no longer included below in the interest of being concise.

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
    
    In the graphical comparisons, a point plot is used to show the typical execution time of each method at the different volumes / by repository. Each point on the plot represents the _median_ execution time for that method, at a given volume of metadata. (For the repository comparison plots, `pts` = Crux and `janus` = JanusGraph.) The horizontal lines that appear around each point are confidence intervals calculated by a bootstrapping process: in simple terms, the larger the horizontal line, the more variability there is for that particular method's execution time (a singular median value is insufficient to represent such variability on its own).

## Crux at varying volumes

!!! summary
    The retrieval and write operations remain very consistent, with almost no variability, throughout the growth in volume. The search operations, however, begin to clearly degrade at the highest volumes tested. Further investigation into other optimized settings for the search operations for these larger volumes is likely warranted as the next step to continue to improve performance.

![Graphical comparison](volume_comparison.svg)

Profile | Method | 05-02 (4,630) | 10-05 (9,260) | 20-10 (18,520)
---|---|---|---|---
Entity creation | addEntity | 51.0 | 45.0 | 44.0
... | saveEntityReferenceCopy | 48.0 | 42.0 | 42.0
Entity search | findEntities | 48.0 | 50.5 | 92.0
... | findEntitiesByProperty | 34.0 | 31.0 | 44.0
... | findEntitiesByPropertyValue | 52.0 | 60.0 | 102.0
Relationship creation | addRelationship | 47.0 | 42.0 | 43.0
... | saveRelationshipReferenceCopy | 49.0 | 44.0 | 45.0
Relationship search | findRelationships | 26.0 | 26.0 | 32.0
... | findRelationshipsByProperty | 34.0 | 29.0 | 42.0
... | findRelationshipsByPropertyValue | 42.0 | 53.0 | 73.0
Entity classification | classifyEntity | 74.0 | 69.0 | 67.0
... | saveClassificationReferenceCopy | 65.0 | 56.0 | 55.0
Classification search | findEntitiesByClassification | 37.0 | 39.0 | 55.0
Entity update | reTypeEntity | 51.0 | 40.0 | 37.0
... | updateEntityProperties | 54.0 | 49.0 | 47.0
Relationship update | updateRelationshipProperties | 60.0 | 50.0 | 50.0
Classification update | updateEntityClassification | 92.0 | 83.0 | 86.0
Entity undo | undoEntityUpdate | 52.0 | 43.0 | 44.0
Relationship undo | undoRelationshipUpdate | 57.0 | 48.0 | 49.0
Entity retrieval | getEntityDetail | 16.0 | 14.0 | 15.0
... | getEntitySummary | 17.0 | 15.0 | 15.0
... | isEntityKnown | 17.0 | 15.0 | 15.0
Entity history retrieval | getEntityDetail | 20.0 | 17.0 | 18.0
... | getEntityDetailHistory | 22.0 | 19.0 | 19.0
Relationship retrieval | getRelationship | 18.0 | 15.0 | 16.0
... | isRelationshipKnown | 18.0 | 16.0 | 16.0
Relationship history retrieval | getRelationship | 21.0 | 19.0 | 19.0
... | getRelationshipHistory | 22.0 | 20.0 | 20.0
Entity history search | findEntities | 64.0 | 76.5 | 112.5
... | findEntitiesByProperty | 31.0 | 31.0 | 34.0
... | findEntitiesByPropertyValue | 54.0 | 69.0 | 109.5
Relationship history search | findRelationships | 28.0 | 30.0 | 40.0
... | findRelationshipsByProperty | 31.0 | 37.0 | 48.0
... | findRelationshipsByPropertyValue | 55.0 | 75.0 | 116.0
Graph queries | getEntityNeighborhood | 27.0 | 24.0 | 23.0
... | getLinkingEntities | 21.0 | 23.0 | 25.0
... | getRelatedEntities | 546.0 | 871.0 | 1415.0
... | getRelationshipsForEntity | 26.0 | 24.0 | 24.0
Graph history queries | getEntityNeighborhood | 27.0 | 23.0 | 23.0
... | getLinkingEntities | 21.0 | 23.0 | 25.0
... | getRelatedEntities | 548.5 | 875.0 | 1410.5
... | getRelationshipsForEntity | 24.0 | 22.0 | 22.0
Entity re-home | reHomeEntity | 58.5 | 43.0 | 40.0
Relationship re-home | reHomeRelationship | 56.0 | 39.0 | 37.0
Entity declassify | declassifyEntity | 80.0 | 56.0 | 56.0
... | purgeClassificationReferenceCopy | 65.0 | 50.0 | 48.0
Entity re-identify | reIdentifyEntity | 61.0 | 48.0 | 47.0
Relationship re-identify | reIdentifyRelationship | 50.0 | 40.0 | 38.0
Relationship delete | deleteRelationship | 48.0 | 37.0 | 38.0
Entity delete | deleteEntity | 56.0 | 42.0 | 42.0
Entity restore | restoreEntity | 44.0 | 37.0 | 36.0
Relationship restore | restoreRelationship | 43.0 | 33.0 | 36.0
Relationship purge | purgeRelationship | 38.0 | 28.0 | 29.0
... | purgeRelationshipReferenceCopy | 28.0 | 21.0 | 22.0
Entity purge | purgeEntity | 55.0 | 35.0 | 41.0
... | purgeEntityReferenceCopy | 32.0 | 21.0 | 24.0

## Crux vs JanusGraph

!!! summary
    In almost all cases, the Crux repository is *significantly* faster than JanusGraph: at most volumes completing all methods in less than 100ms and with very little variability. For JanusGraph, on the other hand, there is significant variability (in particular for methods like `findEntitiesByClassification`), and there are numerous examples of the median execution time taking more than multiple seconds.

    Even at 8 times the volume of metadata the Crux connector still outperforms the JanusGraph connector in almost every method (the only exceptions being a few of the find methods, where the performance is approximately even at 2-4 times the volume).

!!! attention "Graph queries were disabled for JanusGraph"
    The graph queries were disabled for JanusGraph in order to have results in a timely manner: it would take more than a month to produce results for these queries for the JanusGraph connector.

![Graphical comparison](repo_comparison.svg)

The Crux results can be difficult to see in detail due to the skew from the Janus results, so it may be easier to look at this more granular comparison that drops the higher scales of Janus for readability of the Crux results:

![Graphical comparison without large Janus volumes](repo_comparison_granular.svg)

Profile | Method | 05-02 (Crux) | 05-02 (Janus) | 10-05 (Crux) | 10-05 (Janus) | 20-10 (Crux) | 20-10 (Janus)
---|---|---|---|---|---|---|---
Entity creation | addEntity | 51.0 | 434.0 | 45.0 | 466.5 | 44.0 | 444.0
... | saveEntityReferenceCopy | 48.0 | 440.5 | 42.0 | 469.0 | 42.0 | 447.0
Entity search | findEntities | 48.0 | 224.0 | 50.5 | 402.0 | 92.0 | 934.0
... | findEntitiesByProperty | 34.0 | 36.0 | 31.0 | 48.0 | 44.0 | 73.0
... | findEntitiesByPropertyValue | 52.0 | 73.0 | 60.0 | 90.0 | 102.0 | 121.5
Relationship creation | addRelationship | 47.0 | 151.0 | 42.0 | 154.5 | 43.0 | 156.0
... | saveRelationshipReferenceCopy | 49.0 | 424.0 | 44.0 | 461.5 | 45.0 | 418.0
Relationship search | findRelationships | 26.0 | 40.0 | 26.0 | 60.0 | 32.0 | 107.0
... | findRelationshipsByProperty | 34.0 | 39.0 | 29.0 | 57.0 | 42.0 | 95.0
... | findRelationshipsByPropertyValue | 42.0 | 66.0 | 53.0 | 88.0 | 73.0 | 136.0
Entity classification | classifyEntity | 74.0 | 873.0 | 69.0 | 865.0 | 67.0 | 896.0
... | saveClassificationReferenceCopy | 65.0 | 731.0 | 56.0 | 801.5 | 55.0 | 839.0
Classification search | findEntitiesByClassification | 37.0 | 545.0 | 39.0 | 917.5 | 55.0 | 1902.5
Entity update | reTypeEntity | 51.0 | 382.0 | 40.0 | 369.0 | 37.0 | 361.0
... | updateEntityProperties | 54.0 | 759.0 | 49.0 | 723.0 | 47.0 | 740.0
Relationship update | updateRelationshipProperties | 60.0 | 422.0 | 50.0 | 418.0 | 50.0 | 435.0
Classification update | updateEntityClassification | 92.0 | 1191.0 | 83.0 | 1187.0 | 86.0 | 1241.5
Entity undo | undoEntityUpdate | 52.0 | -- | 43.0 | -- | 44.0 | --
Relationship undo | undoRelationshipUpdate | 57.0 | -- | 48.0 | -- | 49.0 | --
Entity retrieval | getEntityDetail | 16.0 | 18.0 | 14.0 | 17.0 | 15.0 | 18.0
... | getEntitySummary | 17.0 | 17.0 | 15.0 | 17.0 | 15.0 | 17.0
... | isEntityKnown | 17.0 | 18.0 | 15.0 | 17.0 | 15.0 | 18.0
Entity history retrieval | getEntityDetail | 20.0 | -- | 17.0 | -- | 18.0 | --
... | getEntityDetailHistory | 22.0 | -- | 19.0 | -- | 19.0 | --
Relationship retrieval | getRelationship | 18.0 | 19.0 | 15.0 | 19.0 | 16.0 | 19.0
... | isRelationshipKnown | 18.0 | 20.0 | 16.0 | 19.0 | 16.0 | 20.0
Relationship history retrieval | getRelationship | 21.0 | -- | 19.0 | -- | 19.0 | --
... | getRelationshipHistory | 22.0 | -- | 20.0 | -- | 20.0 | --
Entity history search | findEntities | 64.0 | -- | 76.5 | -- | 112.5 | --
... | findEntitiesByProperty | 31.0 | -- | 31.0 | -- | 34.0 | --
... | findEntitiesByPropertyValue | 54.0 | -- | 69.0 | -- | 109.5 | --
Relationship history search | findRelationships | 28.0 | -- | 30.0 | -- | 40.0 | --
... | findRelationshipsByProperty | 31.0 | -- | 37.0 | -- | 48.0 | --
... | findRelationshipsByPropertyValue | 55.0 | -- | 75.0 | -- | 116.0 | --
Graph queries | getEntityNeighborhood | 27.0 | -- | 24.0 | -- | 23.0 | --
... | getLinkingEntities | 21.0 | -- | 23.0 | -- | 25.0 | --
... | getRelatedEntities | 546.0 | -- | 871.0 | -- | 1415.0 | --
... | getRelationshipsForEntity | 26.0 | -- | 24.0 | -- | 24.0 | --
Graph history queries | getEntityNeighborhood | 27.0 | -- | 23.0 | -- | 23.0 | --
... | getLinkingEntities | 21.0 | -- | 23.0 | -- | 25.0 | --
... | getRelatedEntities | 548.5 | -- | 875.0 | -- | 1410.5 | --
... | getRelationshipsForEntity | 24.0 | -- | 22.0 | -- | 22.0 | --
Entity re-home | reHomeEntity | 58.5 | 731.5 | 43.0 | 722.0 | 40.0 | 748.5
Relationship re-home | reHomeRelationship | 56.0 | 363.0 | 39.0 | 358.0 | 37.0 | 383.0
Entity declassify | declassifyEntity | 80.0 | 1225.5 | 56.0 | 1308.0 | 56.0 | 1368.5
... | purgeClassificationReferenceCopy | 65.0 | -- | 50.0 | -- | 48.0 | --
Entity re-identify | reIdentifyEntity | 61.0 | 1711.0 | 48.0 | 1725.5 | 47.0 | 1752.0
Relationship re-identify | reIdentifyRelationship | 50.0 | 779.0 | 40.0 | 799.5 | 38.0 | 794.0
Relationship delete | deleteRelationship | 48.0 | 362.0 | 37.0 | 375.0 | 38.0 | 400.0
Entity delete | deleteEntity | 56.0 | 738.0 | 42.0 | 763.0 | 42.0 | 790.0
Entity restore | restoreEntity | 44.0 | 769.0 | 37.0 | 815.0 | 36.0 | 786.0
Relationship restore | restoreRelationship | 43.0 | 339.0 | 33.0 | 380.0 | 36.0 | 423.5
Relationship purge | purgeRelationship | 38.0 | 125.0 | 28.0 | 162.5 | 29.0 | 184.0
... | purgeRelationshipReferenceCopy | 28.0 | 104.0 | 21.0 | 100.0 | 22.0 | 112.0
Entity purge | purgeEntity | 55.0 | 234.0 | 35.0 | 315.0 | 41.0 | 355.0
... | purgeEntityReferenceCopy | 32.0 | 243.0 | 21.0 | 218.0 | 24.0 | 230.0

## Reproducibility

### Re-running the tests

Two Helm charts are provided, that were used to automate the execution of these suites against the Crux repository connector:

- [The Helm chart used to execute the CTS suite :material-github:](https://github.com/odpi/egeria-connector-crux/tree/main/cts/charts/ec-cts-crux){ target=gh }
- [The Helm chart used to execute the PTS suite :material-github:](https://github.com/odpi/egeria-connector-crux/tree/main/cts/charts/ec-pts-crux){ target=gh }

These use a default configuration for the Crux repository where Lucene is used as a text index and RocksDB is used for all persistence: index store, document store and transaction log. No additional tuning of any parameters (Crux or RocksDB) is applied: they use all of their default settings.

### Data points

The [`cts/results` :material-github:](https://github.com/odpi/egeria-connector-crux/tree/main/cts/results){ target-gh } directory in the code repository for the connector contains results of running the suites against the Crux connector. For each test suite execution, you will find the following details:

- `openmetadata_cts_summary.json` - a summary of the results of each profile
- Description of the k8s environment
    - `deployment` - details of the deployed components used for the test
    - `configmap.yaml` - details of the variables used within the components of the test
- The OMAG server configurations:
    - `omag.server.crux.config` - the configuration of the Crux connector (proxy)
    - `omag.server.cts.config` - the configuration of the test workbench
- The cohort registrations:
    - `cohort.coco.crux.local` - the local Crux connector (proxy) cohort registration information
    - `cohort.coco.crux.remote` - the cohort members considered remote from the Crux connector (proxy)'s perspective
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
