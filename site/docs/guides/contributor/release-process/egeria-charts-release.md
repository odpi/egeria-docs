<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

### Egeria charts Release process

#### Obtaining releases / artifacts for Egeria charts 

| Location | Usage |
|---|---|
| [Github Egeria charts Release :material-github:](https://github.com/odpi/egeria-charts/releases){ target=gh } | source code in `zip` and `tar.gz` formats |
| `git` | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |
| `git` | `git checkout Vx.y` to get version as-shipped (each release is tagged at the point it is shipped) |

??? success "1. Agree schedule"
    --8<-- "docs/guides/contributor/release-steps/agree-schedule.md"
??? success "2. Track remaining issues and PRs"
    --8<-- "docs/guides/contributor/release-steps/track-outstanding.md"
??? success "3. Create branch"
 
TODO

Notes:

* There is a versioned release for each chart.
* Each chart has a chart.yaml, which contains a version number. If a change is made to the chart then the number needs to change; this can be achieved by x.y.z => x.y.z+1 for example 3.5.1 => 3.5.2   
* Each chart has a values.yaml file. This contains values for the chart, including the react UI tag version.


--8<-- "snippets/abbr.md"
