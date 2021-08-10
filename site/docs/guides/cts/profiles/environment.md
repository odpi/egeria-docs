---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Environment profile

Does not actually run any tests, but rather gathers statistics about the environment in which the other
performance tests were executed.

This profile currently collects the following information about the technology under test in which the performance
tests were executed:

???+ discovered "Discovered properties"
    **Test configuration**

    | Property  | Description |
    |---|---|
    | `instancesPerType` | the number of instances the test should attempt to create, per type definition |
    | `maxSearchResults` | the number of results per page to retrieve for search queries |
    | `waitBetweenScenarios` | the time (in seconds) to wait between write and read phases of the performance tests |

    **Egeria statistics**

    | Property  | Description |
    |---|---|
    | `totalEntitiesCreated` | the total number of entity instances that were created by the performance tests |
    | `totalEntitiesFound` | the total number of entity instances that were found in the environment (created + pre-existing) |
    | `totalRelationshipsCreated` | the total number of relationship instances that were created by the performance tests |
    | `totalRelationshipsFound` | the total number of relationship instances that were found in the environment (created + pre-existing) |

    **Runtime environment information**
    !!! attention "Caveat"
        Currently these are captured only for the [OMAG Server Platform](/egeria/concepts/omag-server-platform) that is actually running the CTS suite
        itself. If the technology under test is running under this same OMAG Server Platform, then these will still be useful;
        however, if the technology under test is running on a separate OMAG Server Platform or via a remote system, these will
        likely be of very limited value.

    | Property  | Description |
    |---|---|
    | `operatingSystem` | details about the operating system (name and version) |
    | `operatingSystemArchitecture` | the operating system's architecture |
    | `operatingSystemAvailableProcessors` | the number of processors available, according to the operating system (likely to include hyperthreads) |
    | `operatingSystemLoadAverage` | current load average from the operating system |
    | `heapUsage` | current heap memory usage out of total heap memory available (in bytes) |
    | `nonHeapUsage` | current non-heap memory usage out of total non-heap memory available (in bytes) |
    | `jvmSpec` | details about the Java virtual machine specification |
    | `jvmImplementation` | details about the Java virtual machine implementation |

--8<-- "snippets/abbr.md"
