<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Secrets

The following GitHub secrets are defined within the ODPi organization for use across the Egeria project.

In some cases they may be overriden at the local repository, but this is generally just by legacy.

To update, go to [https://github.com/organizations/odpi/settings/secrets/actions](https://github.com/organizations/odpi/settings/secrets/actions) . This is only available to organization admins.

| Secret Name | Description                                | Usage | Notes                                                 |
| ----------- |--------------------------------------------| ----- |-------------------------------------------------------|
| DOCKER_HUB_ACCESS_TOKEN | Access token for login to docker.io        | Publishing container images |
| DOCKER_HUB_USERNAME | Username for login to docker.io            | Publishing container images | Should be 'odpi'                                      |
| NPM_TOKEN | Access token for login to npm registry     | Publishing UI components |
| OSSRH_GPG_KEYID | GPG key ID for signing artifacts           | Publishing Maven artifacts | Use value under 'pub' after running `gpg --list-keys` 
| OSSRH_GPG_PASSPHRASE | GPG passphrase for signing artifacts       | Publishing Maven artifacts |
| OSSRH_GPG_PRIVATE_KEY | GPG private key for signing artifacts      | Publishing Maven artifacts | `gpg --export-secret-keys myemal@gmail.com \| base64` |
| OSSRH_TOKEN | Access token for login to Maven Central    | Publishing Maven artifacts | Generate by going to https://oss.sonatype.org, login, go to top left, click dropdown -> profile then select 'user token' in dropdown, and generate
| OSSRH_USERNAME | Username for login to Maven Central        | Publishing Maven artifacts | 'planetf1' - update along with token if changed       
| QUAY_IO_ACCESS_TOKEN | Access token for login to quay.io          | Publishing container images |
| QUAY_IO_USERNAME | Username for login to quay.io              | Publishing container images | Should be 'odpi'                                      |
| SONARCLOUD | Access token for login to SonarCloud (old) | Publishing code quality reports | no longer used                                        
| SONAR_TOKEN | Access token for login to SonarCloud (new) | Publishing code quality reports | no longer used                                        

--8<-- "snippets/abbr.md"
