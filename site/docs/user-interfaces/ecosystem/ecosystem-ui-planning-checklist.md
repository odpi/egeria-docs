# Egeria UI planning


## Planning checklist

- [ ] [Plan](/guides/planning/overview) your Egeria topology- including how many platforms, how many servers, cohort and connectors
- [ ] [Plan your UI](/user-interfaces/ecosystem/ecosystem-ui-planning) which UI capabilities you require.
- [ ] Start one (or more) Egeria platforms either
  * locally using a development setup (where you compile the code and run it as a jar file)
  * Using a Kubenetes image
    * this can be using a coco image 
    * a preconfigured simple image 
    * an empty simple image
    * your own custom Kubenetes image
- [ ] [Configure a metadata server platform](/guides/admin/configuring-the-omag-server-platform)  if required (some of the Kubenetes images already configure a metadata server platform)    
- [ ] [Configure and start a metadata access store server](/guides/admin/servers/configuring-a-metadata-access-store) if required (some of the Kubenetes images already configure a metadata access store server)
- [ ] [Configure and start view services](/guides/admin/servers/configuring-a-view-server)  for each of the UI capabilities you require. The name of the UI capability is the same as the name of the view service. 
- [ ] [Configure and run the presentation server](/user-interfaces/ecosystem/configure-and-run-presentation-server) 
- [ ] Validate that the presentation server is running as expected. Using the following guides:
    * [Resource explorer guide](/guides/ecosystem-ui/rex-user-guide)
    * [Type explorer guide](/guides/ecosystem-ui/tex-user-guide)
    * [Dino guide](/guides/ecosystem-ui/dino-user-guide)
    * [Glossary Author guide](/guides/ecosystem-ui/glossary-author-user-guide)
    * [Server Author guide](/guides/ecosystem-ui/server-author-user-guide)



