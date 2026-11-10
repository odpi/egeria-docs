# pyegeria operations commands: issues found 2026-11-10

Found while rewriting the Egeria operations guide against **egeria-python `main` at `9e50cd81a0`** (pyproject version 6.2.30) and a live quickstart platform (Egeria 6.3-SNAPSHOT, `oak2026`).  None of these are in `PYEGERIA_ISSUES.md` yet.  ISSUE-156 fixed the catalog target request *shape*; item 5 is a separate problem with the *defaults*.

Entries follow the tracker's layout so they can be pasted in; numbers are left for the tracker owner to assign.

| # | Command / method | Problem | Severity |
|---|---|---|---|
| 1 | `hey_egeria_ops show integrations --targets` | Command can never be invoked | High - feature unreachable |
| 2 | `hey_egeria_ops tell engine-host refresh` | Option is single-dash and its value is ignored | Medium |
| 3 | `hey_egeria_ops tell servers start` | Server GUID passed in the `display_name` slot | High - start likely fails |
| 4 | `hey_egeria_ops tell servers stop` | Server name passed as a qualified name that never matches | High - stop likely fails |
| 5 | `AutomatedCuration.add_catalog_target` / `update_catalog_target` | Defaults override the connector's settings and reset them on update | High - silent wrong behaviour |
| 6 | `commands/ops/README.md`, `gov_server_actions.py` | Stale and wrong docs/docstrings | Low |

---

### 1. `show integrations --targets` is registered under the name `"--targets"`, so click parses it as an option and the command is unreachable

**Layer:** Pyegeria - **Status:** open - **Found:** 2026-11-10, reproduced with click

**Where:** `commands/cli/egeria_ops.py` around line 400:

```python
@integrations.command("--targets")
@click.pass_context
@click.argument("connector", nargs=1)
def integrations_status(ctx, connector):
```

**What:** a command name that starts with `--` is taken as an option of the parent group.  A minimal click reproduction (same decorators) gives:

```
$ ... integrations --targets X
Error: No such option '--targets'.
```

The command only runs as `integrations -- --targets X`, which nobody will guess.  It is listed in `--help` as a command called `--targets`.  The function also reuses the name `integrations_status`, shadowing the `status` command's function at module level (click has already registered both, so this is a lint problem rather than a runtime one, but it hides the bug).

**Proposed fix:** rename to `@integrations.command("targets")` and rename the function (for example `integrations_targets`).  Check `commands/cli/egeria.py` for the same registration.

---

### 2. `tell engine-host refresh`: option `-engine-host-guid` has a single dash, and its value is never used

**Layer:** Pyegeria - **Status:** open - **Found:** 2026-11-10, reproduced with click

**Where:** `commands/ops/gov_server_actions.py`, `refresh_gov_eng_config` (around line 108):

```python
@click.command("refresh")
@click.option("-engine-host-guid", help="GUID of engine host to refresh.")
@click.pass_context
def refresh_gov_eng_config(ctx, engine_host_guid: str):
    """Start or restart an engine-host from its known configuration"""
    ...
        p_client.refresh_gov_eng_config(None, None, c.engine_host)
```

**What:**
- The conventional `--engine-host-guid` is rejected (`No such option '--engine-host-guid'. Did you mean '-engine-host-guid'?`); only the single-dash form is accepted.
- Whatever is passed, `engine_host_guid` is ignored: the call always refreshes `c.engine_host` by display name.
- The docstring describes a start/restart, but the command reloads the governance engine configuration.

**Proposed fix:** `@click.option("--engine-host-guid", ...)`, pass it as `server_guid` when supplied (falling back to `display_name=c.engine_host`), and change the docstring to "Ask the engine host to reload its governance engine configuration".  Consider a `--engine` option mapping to `gov_engine_name` so a single engine can be refreshed.

---

### 3. `tell servers start` passes the server GUID in the `display_name` position

**Layer:** Pyegeria - **Status:** open - **Found:** 2026-11-10 from source; not run live

**Where:** `commands/ops/gov_server_actions.py`, `start_server` (around line 127):

```python
server_guid = p_client.get_element_guid_by_unique_name(server, "name")
p_client.activate_server_with_stored_config(None, server_guid, organization_name=organization_name)
```

`RuntimeManager.activate_server_with_stored_config(self, server_guid=None, display_name=None, qualified_name=None, timeout=240, organization_name=None, body=None)` - so the GUID lands in `display_name` and `server_guid` is `None`.

**Also:**
- The GUID lookup uses the property `"name"`.  The server elements in a current platform carry `qualifiedName` (`Engine Host Server::https://localhost:9443::qs-engine-host`), `displayName` (`qs-engine-host from Coco Pharmaceuticals on https://localhost:9443`) and `resourceName` (`Coco Pharmaceuticals.qs-engine-host`) - worth checking that a `"name"` lookup finds anything at all.
- `--server` silently defaults to `qs-metadata-store`, so `tell servers start` with no option starts that server.
- The docstring says "Start or restart an engine-host"; it starts any server.

**Proposed fix:** call `activate_server_with_stored_config(server_guid=server_guid, ...)`, or drop the lookup and pass `display_name=server, organization_name=...` so the method's own resolver (which builds the `resourceName` from the organization name) does the work.  Make `--server` required, and fix the docstring.

---

### 4. `tell servers stop` passes the server name as a qualified name that will not match

**Layer:** Pyegeria - **Status:** open - **Found:** 2026-11-10 from source, server names checked live; the stop itself was not run

**Where:** `commands/ops/gov_server_actions.py`, `stop_server` (around line 149):

```python
p_client.shutdown_server(None, server)
```

`RuntimeManager.shutdown_server(self, server_guid=None, qualified_name=None, body=None)` resolves the GUID with `__get_guid__(server_guid, None, "qualifiedName", qualified_name)`.  With `--server qs-engine-host` it looks for `qualifiedName == "qs-engine-host"`, but the live element's qualified name is `Engine Host Server::https://localhost:9443::qs-engine-host`.

**Also:**
- `--server` has no default and is not required, so `tell servers stop` with no option sends `None` for both identifiers.
- The docstring says "Stop an engine-host daemon"; it stops any server.
- `start` and `stop` identify servers differently (GUID lookup by `"name"` versus raw qualified name), so the same `--server` value cannot work for both.
- Left-over commented-out options from the old stand-alone script.

**Proposed fix:** give `shutdown_server` the same `display_name` / `organization_name` resolution that `activate_server_with_stored_config` has, call it with `display_name=server`, make `--server` required, and fix the docstring.  A micro-test asserting the arguments each command passes would catch all of items 2-4.

---

### 5. `AutomatedCuration.add_catalog_target` / `update_catalog_target` always send `permittedSynchronization=BOTH_DIRECTIONS` and `deleteMethod=ARCHIVE`

**Layer:** Pyegeria - **Status:** open - **Found:** 2026-11-10 from source, checked against Egeria `oak2026`

**Where:** `pyegeria/omvs/automated_curation.py`, `add_catalog_target` (line ~4253), `update_catalog_target` (line ~4373) and their async versions:

```python
permitted_sync: str = "BOTH_DIRECTIONS",
delete_method: str = "ARCHIVE",
```

`_catalog_target_properties()` correctly drops `None` values, but these defaults are never `None`, so both fields are written on every call.

**Why it matters:**
- **On add:** Egeria deliberately leaves `permittedSynchronization` unset on a catalog target so that it inherits the connector's value from its *RegisteredIntegrationConnector* registration (`RequestedCatalogTargetsManager` lines 549-551 in the open-integration-framework: `if (newRequestedCatalogTarget.getPermittedSynchronization() == null) newRequestedCatalogTarget.setPermittedSynchronization(integrationContext.getPermittedSynchronization());`).  A connector registered as `FROM_THIRD_PARTY` therefore gets `BOTH_DIRECTIONS` targets when they are added through pyegeria or `hey_egeria_ops tell integration-daemon add-target`, which can push open metadata changes back into a technology the operator meant to treat as read-only.  The forced `ARCHIVE` delete method likewise overrides whatever the connector would otherwise do.
- **On update:** `UpdateRelationshipRequestBody.mergeUpdate` defaults to `true` in Egeria, so other properties survive - but these two are reset on every update.  `hey_egeria_ops tell integration-daemon update-target <guid> <new-name>`, which only intends to rename the target, silently resets both fields.

**Proposed fix:** default both parameters to `None` in the sync and async signatures, and update the docstrings to say "unset - inherit the connector's setting".  Add micro-tests asserting the fields are absent from the body when not supplied.

---

### 6. Stale and wrong documentation in `commands/ops`

**Layer:** Pyegeria (docs) - **Status:** open - **Found:** 2026-11-10

- `commands/ops/README.md` lists files that no longer exist (`get_eng_action_status.py`, `view_eng_action_status.py`, `view_gov_eng_status.py`, `view_integ_daemeon_status.py`, `view_platform_status.py`, `view_server_list.py`, `view_server_status.py`, `view_asset_changes.py`, `view_asset_events.py`) and describes `get_tech_type_elements.py` and `view_coco_status.py`, which are not operations widgets.  The current modules are `monitor_*`, `list_*`, `refresh_integration_daemon.py`, `restart_integration_daemon.py`, `load_archive.py` and `gov_server_actions.py`.
- `commands/ops/gov_server_actions.py`'s module docstring says "This script restarts an integration daemon."  It holds the catalog target, engine-host refresh and server start/stop commands.
- `PYEGERIA_ISSUES.md` (around line 7904) points readers to `hey_egeria_ops start` / `hey_egeria_ops stop` as the replacement for the removed `start_daemon` / `stop_daemon` scripts.  The commands are actually `hey_egeria_ops tell servers start|stop`, and see items 3 and 4.

---

**Not pyegeria, for the Egeria team** (found in the same pass):
- `PostgresConfigurationProperty.REPOSITORY_MODE` is declared with `DataType.DATE` and the example value `"yyyy/MM/dd HH:mm:ss"` - apparently copied from `DEFAULT_AS_OF_TIME` on the line above; it should be a string with values such as `readOnly`.
- `IntegrationConnectorHandler.getRegistrationChange()` (and the handler construction in `IntegrationGroupHandler.refreshRegisteredIntegrationConnector()`) sets `metadataSourceQualifiedName` from `getMetadataCollectionQualifiedName()`, not `getMetadataSourceQualifiedName()`.  A registration that only sets `metadataSourceQualifiedName` - as the Asset Maker samples do - has it ignored.
