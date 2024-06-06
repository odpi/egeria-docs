<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Lookup registration

Lookup registration submitted by an external tool.

More examples can be found in the
[sample collection](samples/collections/DataEngine-process_endpoints.postman_collection.json)

```
GET {serverURLRoot}/servers/{serverName}/open-metadata/access-services/data-engine/users/{userId}/software-server-capabilities/{engineQualifiedName}
```

`GUIDResponse` - response containing the external tool guid, with status and error message if failing.


---8<-- "snippets/abbr.md"







