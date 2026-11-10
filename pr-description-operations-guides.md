## Operations, monitoring, diagnostic, security and planning guides

The Operations Guide dates from when the REST API was the only way to run Egeria.  This PR rewrites it for the current options, adds a Monitoring and Tuning Guide and a Security Guide, brings the Diagnostic Guide up to date with the current servers and infrastructure, and turns the Planning Guide into the entry point that ties them all together.

### Operations Guide (`guides/operations/overview.md`)

Rewritten.  It now covers:

* **Ways to operate Egeria** - a comparison of the Egeria Operations portal card, the `hey_egeria` commands, pyegeria (scripts and Jupyter notebooks) and the REST APIs.
* **Egeria Operations in the portal** - screenshots of the Servers, Integration Connectors, Governance Engines and Engine Actions tabs, with what each tab shows and lets you change.
* **hey_egeria** show and tell commands, **pyegeria** classes with a sample script, and **REST API** examples using bearer tokens.
* **Running and tuning integration connectors**:
    * what each connector status means;
    * refreshing and restarting connectors;
    * tuning `refreshTimeInterval` and the other registration properties;
    * tuning catalog targets (configuration properties, `permittedSynchronization`, `deleteMethod`);
    * when a change takes effect - a sequence diagram showing which changes cause a refresh and which cause a reinitialize.
    * A warning that Runtime Manager updates are held in memory only.
* **Operating servers and governance engines.**

The nav entry is renamed from "Operate OMAG Server Platform" to "Operating Egeria".

### Monitoring and Tuning Guide (new, `guides/monitoring/`)

* What to watch, and the audit log: destinations, choosing severities, and the audit log report API.
* Monitoring and tuning **Apache Kafka**: settings, topic names and consumer groups.
* Monitoring and tuning **PostgreSQL**: repository connector settings, the connection budget, monitoring SQL, and vacuuming.
* Maintenance tasks:
    * PostgreSQL backups with `pg_dump`, plus configuration documents and keystores;
    * cleaning up audit log files;
    * managing soft-deleted metadata.
* `purge-deleted-elements.py` - a downloadable example script for purging soft-deleted elements from a cron job or other DevOps tool:
    * it uses only the Python standard library;
    * it takes a retention policy per type;
    * it runs as a dry run by default, with `--purge` and `--max-purges` options;
    * it skips reference copies;
    * it reads the password only from an environment variable.

### Diagnostic Guide

* **Overview** - a new "Where to start" table that sends each symptom to the right page, and an updated problem classification.
* **Diagnostic sources** - rewritten: audit log message prefixes, status reports, engine actions, corrected Actuator and Prometheus information, and developer logging.
* **Diagnostic APIs** - filled in (was a stub).  It covers platform, server, connector, governance engine, audit log, cohort and repository calls, with real responses from the quickstart.
* **PostgreSQL and Kafka diagnostic guide** (new) - message identifiers, start-up and runtime failures, slow requests, events not sent or received, and the build-up of empty consumer groups.
* **Metadata access store diagnostic guide** and **cohort errors** - filled in (were stubs).
* **Integration daemon diagnostic guide** - explains that integration groups are configured through open metadata, with links to the tuning sections of the Operations Guide.

### Security Guide (new, `guides/security/overview.md`)

Written for a security expert assuring a deployment.  It covers:

* the layers of protection a request passes through;
* TLS and certificates;
* users, passwords and bearer tokens;
* the platform and server metadata security connectors;
* governance zones and secrets stores;
* security audit logging;
* a hardening checklist;
* a list of places where the existing documentation and the code disagree.

Related corrections to existing pages:

* `server.ssl-key-store` / `server.ssl-key-alias` corrected to `server.ssl.key-store` / `server.ssl.key-alias`.
* `strict.ssl` described correctly: it defaults to `true`, and `false` turns off verification.
* `rsa.key-id` described correctly.
* The configuration document advice no longer says to switch storage to clear text.
* The security connector examples now use the Open Metadata Access Security Connector instead of the retired Coco Pharmaceuticals samples.

### Planning Guide

* A new **Planning the whole deployment** section, with a diagram and a table of decisions covering:
    * starting point, runtime and servers, infrastructure;
    * connectors and content, configuration, security;
    * user interfaces, operation, monitoring and maintenance;
    * problem determination and the metadata ecosystem.

    Each row points to the guide with the detail.
* The runtime deployment checklist gains items for PostgreSQL, Kafka, the purge policy, operations and security hardening.  The "More detail to follow" placeholder is replaced with next steps.

### Other fixes

* Links to the old `#starting-and-stopping-an-omag-server` / `#operating-an-omag-server` anchors now point to `/guides/operations/overview#operating-servers`.
* Fixed broken anchors in the runtime planning page and `ffdc.md`, and the metadata provenance link in the common REST API errors page.
* Nav entries added for the Monitoring and Tuning Guide, the Security Guide, and the PostgreSQL and Kafka diagnostic page.

### Checks

* `mkdocs build` raises no warnings for the changed pages.
* Every absolute link and anchor in the changed pages resolves against the built site.
* The new and edited pages are pure ASCII.
* The purge script has been run against the quickstart in dry-run mode only.

### Not in this PR

* The older operations pages (starting and stopping a server, platform origin service, adding an archive to a running server) still use REST URLs with `/users/{userId}/`.
* pyegeria bugs found while writing the Operations Guide are reported separately to the pyegeria team.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
