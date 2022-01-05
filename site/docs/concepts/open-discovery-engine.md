<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Discovery Engines

An *open discovery engine* is the execution environment for special types of connectors called [open discovery services](/egeria-docs/concepts/open-discovery-service). Each discovery service implements a specific type of analysis.  This analysis is looking into the content of the physical real-world counterpart of an Asset in the metadata repository. The result of its analysis is stored as [Annotations](/egeria-docs/concepts/discovery-analysis-report) and linked off of the asset's description in the metadata repository via a [discovery analysis report](/egeria-docs/concepts/discovery-analysis-report).

The discovery engine configuration defines a set of discovery services.  Its definition is stored in an open metadata repository and maintained through the [Governance Engine OMAS's configuration API](/egeria-docs/services/omas/governance-engine/overview).

Discovery engines are hosted in the [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis/overview) running in an [engine host](/egeria-docs/concepts/engine-host). Engine host servers are deployed close to the physical assets they are analysing.  They connect to the [Discovery Engine OMAS](/egeria-docs/services/omas/discovery-engine/overview) running in a [metadata access server](/egeria docs/concepts/metadata-access-server) both to provide metadata about assets and to store the results of the discovery service's analysis.

## Further reading

Egeria's implementation of the discovery engine is provided by the
[Asset Analysis Open Metadata Engine Service (OMES)](/egeria-docs/services/omes//asset-analysis/overview).


---8<-- "snippets/abbr.md"