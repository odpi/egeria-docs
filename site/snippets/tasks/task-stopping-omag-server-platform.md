<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Stopping the OMAG Server Platform

Once you have [Stopped your OMAG server](/education/tutorials/omag-server-tutorial/task-stopping-omag-server) you can stop the [OMAG Server Platform](/concepts/omag-server-platform) using the following command (this is request **10.** in Postman).

```
POST https://localhost:9443/open-metadata/admin-services/users/garygeeke/server-platform/instance
```

There is no response from the request because the platform exits before it sends the response.


