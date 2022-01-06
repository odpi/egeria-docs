# Egeria UI planning


## Planning checklist

- [ ] [Plan](../../planning/guide/) your Egeria topology- including how many platforms, how many servers, cohort and connectors
- [ ] [Plan your UI](./react-ui-planning) which UI capabilities you require.
- [ ] Start one (or more) Egeria platforms either
  * locally using a development setup (where you compile the code and run it as a jar file)
  * Using a Kubenetes image
    * this can be using a coco image 
    * a preconfigured simple image 
    * an empty simple image
    * your own custom Kubenetes image
- [ ] [Configure a metadata server platform](../../guides/admin/configuring-the-omag-server-platform.md)  if required (some of the Kubenetes images already configure a metadata server platform)    
- [ ] [Configure and start a metadata access store server](../../guides/admin/servers/configuring-a-metadata-access-store.md) if required (some of the Kubenetes images already configure a metadata access store server)
- [ ] [Configure and start view services](../../guides/admin/servers/configuring-a-view-server.md)  for each of the UI capabilities you require. The name of the UI capability is the same as the name of the view service. 
- [ ] [Configure and run the presentation server](./configure-and-run-presentation-server.md) 
- [ ] Validate that the presentation server is running as expected. Using the followng guides:
    * [Resource explorer guide](../../guides/react-ui/rex-user-guide.md)
    * [Type explorer guide](../../guides/react-ui/tex-user-guide.md)
    * [Dino guide](../../guides/react-ui/dino-user-guide.md)
    * [Glossary Author guide](../../guides/react-ui/glossary-author-user-guide.md)
    * [Server Author guide](../../guides/react-ui/server-author-user-guide.md)



