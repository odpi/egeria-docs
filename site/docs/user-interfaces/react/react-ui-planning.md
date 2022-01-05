<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# React UI planning

Ensure you have set up the Egeria servers you need to run the UI. A simple setup is described [here](./prereqs.md).

If you are following the [checklist](./react-ui-setup.md) you should have completed the following tasks before proceeding.

- [x] [Plan your Egeria topology](../../planning/guide/) - including how many platforms, how many servers, cohort and connectors
- [ ] [Plan your UI](./react-ui-planning) *which UI capabilities you require using the information on this page.*
- [ ] Start Egeria platform(s)
- [ ] [Configure metadata server platform](../../admin/configuring-the-omag-server-platform) if required (some of the Kubenetes images already configure a metadata server platform)
- [ ] [Configure and start metadata access store server](../../admin/servers/configuring-a-metadata-access-store)  if required (some of the Kubenetes images already configure a metadata access store server)

- [ ] [Configure and start view services](../../admin-services/view-server)  for each of the UI capabilities you require. The name of the UI capability is the same as the name of the view service.
- [ ] [Configure and run the presentation server](./configure-and-run-presentation-server)
- [ ] Validate that the presentation server is running as expected.

At this stage you will have planned the Egeria OMAG Server platform(s) and Egeria Servers you are using. We are now going to 
show how the servers need to be setup for the Egeria React User Interface. 

TODO
- simplified picture
- what needs to point to what
- 



