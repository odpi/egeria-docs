# Egeria 6.3: our additions to the egeria-docs release notes

For Mandy, 2026-11-16. These add to your text in odpi/egeria-docs and don't change it:
- **Part A:** boxes for `site/snippets/release-notes/6-3.md`, just before "### Upgrade notes", in the same layout as the 6.1 and 6.2 boxes.
- **Part B:** bullets for that file's "### Upgrade notes".
- **Part C:** additions to `site/docs/release-notes/november-2026.md`.

Part B assumes odpi/egeria-workspaces#887 (the 6.3 bundle) is merged. Until then the Egeria Workspaces floor is pyegeria 6.2.42, with 6.3.0 recommended.

---

## Part A: boxes for `site/snippets/release-notes/6-3.md`

??? functional "Enhancements to the Egeria Workspaces"
    [Egeria Workspaces](/egeria-workspaces) has kept up with the new features in Egeria 6.3. Its portal now holds more of its content in Egeria, and is clearer about what its numbers mean.

    - **Dashboards and report specifications are held in Egeria**, organized in folders by the tools that use them. They can be shared, secured by governance zone and reused. Users and teams can still create and manage their own local dashboards. Egeria Explorer shows a *Used by* row for each report specification.
    - **The Overview only shows numbers it has measured.** Counts cover the whole repository, and a card says "not measured" rather than showing a guess. Results also say when more may exist.
    - **Relationships and classifications are grouped by [purpose](/concepts/relationship-purpose)** in [Egeria Explorer](/user-interfaces/egeria-explorer/overview), the [Data Mesh](/user-interfaces/data-mesh/overview) view and [The Catalog](/user-interfaces/the-catalog/overview).
    - Egeria Explorer has a new **Statements of Applicability** view. For each [statement of applicability](/services/omvs/security-officer/overview/#statements-of-applicability), it shows an implementation summary and a table of its controls, which you can sort and filter.
    - **The Resource Browser** gives each resource a page showing what it contains and what it means, with work lists and team sharing. The Catalog has a tab for each kind of infrastructure, and its lists page to the end.
    - **The [Lineage Explorer](/user-interfaces/lineage-explorer/overview)** lets you choose how many hops to show, and every diagram has an Expand button that opens a viewer you can pan and zoom.
    - **Columns and panes across the portal can be resized**, and your choices are remembered.
    - **Airflow and Marquez start with the demo**, and Airflow's Open Lineage events flow into Egeria.
    - **New tutorials** cover saved queries, analytic functions, report specifications and local dashboards, with worked examples.
    - **A new `egeria-upgrade-reset` tool** plans and performs an upgrade or reset of the quickstart's Egeria step by step, with a verified backup. The quickstart now runs the released Egeria 6.3 image.
    - We continue to harden the portal environment. Its ports are bound to the local machine by default (`--lan` opens them), bearer tokens last two hours, and the database used by the AI applications no longer has a default password.

??? functional "Enhancements to Dr.Egeria and pyegeria"
    - [Dr.Egeria](/user-interfaces/dr-egeria/overview) has new commands and templates for statements of applicability, business capabilities, report specifications, measurements and dashboards, and for setting an element's governance zones.
    - Reports can be produced as documents and as DCAT catalogs, and as structured tables that the portal displays the same way everywhere.
    - [pyegeria](/concepts/pyegeria) follows Egeria's paging rules: when a result can't be confirmed complete, a count says "at least N" rather than giving a total that might be wrong. With pyegeria 6.3.0 on Egeria 6.3, pyegeria can tell when it has read to the end of a result.
    - pyegeria has a new authoring API for report specifications, reports and dashboard sheets, with private drafts and published versions.
    - A value that wasn't measured is reported as not measured, never as 0.
    - [pyegeria 6.3.0](https://github.com/odpi/egeria-python/releases/tag/v6.3.0){target=blank} is the release that matches Egeria 6.3.

??? functional "Technical preview: AI applications on Trellis"
    [Trellis](/concepts/trellis) is released alongside Egeria 6.3 as the *6.3 Tech Preview*.

    * **Resource Explorer** now publishes what it finds into Egeria, in the right governance zones, and checks that it arrived. Its surveys run on Egeria's own engine host, and each survey step sends an Open Lineage event. It is also clearer about what an answer is based on, and says when something could not be determined.
    * **Egeria Advisor** reads and authors the same dashboards and report specifications held in Egeria as the portal does.
    * **Studio** is a new application for authoring report specifications, reports and dashboard sheets, with Egeria Advisor available as a panel for AI-assisted authoring.
    * When you rate an answer, you can say why. An administrator reviews the feedback and can trace a problem back to a gap in the documents behind it.

    !!! attention "Technical preview - we are looking for feedback"
        Resource Explorer, Egeria Advisor and Studio are technical previews. They are under active development, their behaviour and the metadata they create may change between releases, and the answers produced by the language models are not always accurate. Please try them and tell us what works for you.

??? functional "Refreshed Coco Pharmaceuticals content"
    The [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) content now includes a sample ISO/IEC 27001 statement of applicability for Coco's information security management system, a Chief Data Officer dashboard, security and sustainability reference data, and Airflow pipelines that load Coco's data products.

## Part B: bullets for "### Upgrade notes" in `6-3.md`

- **Egeria Workspaces** needs pyegeria 6.3.0 or later.
- **Upgrading the quickstart:** use `egeria-upgrade-reset` (`plan` first, then `apply`). `--stable` picks the newest released Egeria; `--latest` is now another name for `--stable`, so it does the same.
- **Report specifications held in Egeria** are read from the portal's consumer folder. See the Egeria Workspaces release notes for the one-time step on an existing Egeria.
- **The shared PostgreSQL restarts once.** The first time the shared infrastructure starts after this upgrade, its PostgreSQL container is recreated, because its configuration gained a setting. Data is kept. Stop anything that uses the database first.
- **The AI applications' database has no default password.** A new install gets a generated one (`PGVECTOR_PASSWORD` in `compose-configs/shared-infra/.env`). If your `egeria_advisor` database user still has the old well-known password, change it as the shared-infra README describes, and give the AI applications the new value.

## Part C: additions to `site/docs/release-notes/november-2026.md`

**C1.** One bullet added to the "Egeria Workspaces" list, after "Dashboards and report specifications are now held in Egeria…":

- **The Overview only shows numbers it has measured**, and results say when more may exist.

**C2.** One bullet added after it, linking to the security section:

- **Statements of applicability can be explored in Egeria Explorer**, starting with Coco's sample for ISO/IEC 27001. It shows how far each control has been implemented.

**C3.** A new section after "Egeria Workspaces":

> ## Technical preview: Resource Explorer, Egeria Advisor and Studio
>
> The AI applications on Trellis are released alongside Egeria 6.3 as a technical preview. Resource Explorer now publishes what it finds into Egeria and runs its surveys on Egeria's own engine host. Egeria Advisor works with the same dashboards and report specifications held in Egeria as the portal does, and the new Studio application is for authoring them. You can try Resource Explorer and Egeria Advisor on the [live demo](https://egeria.pdr-associates.com){target=blank}. Please tell us what works for you.

**C4.** One sentence added to the "pyegeria and Dr.Egeria" section:

Install or upgrade with `pip install -U pyegeria`. The [pyegeria release notes](https://github.com/odpi/egeria-python/tree/main/docs/release-notes){target=blank} describe each release.

**C5 (optional).** Two screenshots of the Statements of Applicability view (Erin Overview, Egeria Explorer) for the "SCREENSHOT NEEDED" placeholder: `november-2026-statement-of-applicability.jpg` and `november-2026-statement-of-applicability-controls.jpg`.
