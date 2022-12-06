<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Planning for security

The Egeria runtimes have been designed so that they can be deployed securely.  However, the security of your solution depends on a combination of the deployment environment as well as Egeria itself.

## Understanding the threats to your solution

The first phase in securing your solution is to understand the threats that need to be guarded against.  This understanding is developed through [Threat Modelling](https://owasp.org/www-community/Threat_Modeling){target=_blank}.  **OWASP** has an excellent guidance pave called the [Threat Modelling Process](https://owasp.org/www-community/Threat_Modeling_Process){target=_blank} that explains how to identify the threats that could compromise your system.

*Description of how this applies to the Egeria ecosystem goes here.*

## Threat model baseline for egeria ecosystem


### Step 1: Decompose the Application

To decompose Egeria applications, it is very important to undestand the [OMAG Server Platform](/concepts/omag-server-platform){target=_blank}. This is a java based server application that is designed to run one or more logical application instances called OMAG Servers. Different application components can be configured and combined to provide runtime services and  define the function of a single OMAG Server. This is defined in a configuration document called OMAG Server [Configuration Document](/concepts/configuration-document/){target=_blank}.

Based on this anathomy, we can observe the applicaton behaviour on different levels:

- **Platform** - The physical application, provides the runtime and inbound entry points (opening - ports, enabling encrypted transport)
- **Server** - logical application, exposing rest endpoints, initiating outbound connections to external systems
- **Service** - validating and processing server requests or providing event processing

*(Logical Architecute Diagram)*

#### DFD Diagram explaining server types and general data flows
Some interaction patterns can be already identified based on the high level purpose of the [Types of OMAG Server](/concepts/omag-server/#types-of-omag-server){target=_blank}

#### External dependencies 
#### Entry points, exit points and assets 
#### Trust levels

Steps that are more specific to given use-case

### Step 2: Determine and rank threads
### Step 3: Determine Countermeasures and mitigations

#### Complementing Code Review




!!! education "Further information on Egeria's security features"
    * [Configuring TLS and certificates](/guides/admin/omag-server-platform-transport-level-security)
    * [Metadata security plugins](/features/metadata-security/overview)
    * [Synchronizing security authorization information](/features/synchronized-access-control/overview)

--8<-- "snippets/abbr.md"
