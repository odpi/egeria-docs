<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Healthchecks when running Egeria in Kubernetes

There are various API calls that will check the status of Egeria.

These may be typically used in a Kubernetes environment to check if Egeria is ready to service requests. Here we summarize what is available.

## Defining a Kubernetes health check

See also [Kubernetes docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

Kubernetes has 3 types of health checks
- startup -- to confirm a pod has started
- readiness -- to confirm a pod is ready. Typically this will then allow requests to be routed here
- liveness -- to check the pod is still responding to requests in a timely fashion.

Typically pods will be restarted if these health checks do not pass in a specified time period.

Each of these checks can be of several types
- tcpSocket -- this just checks for an open port.
- grpc -- issues grpc call (we do no use grpc in egeria)
- httpGet -- a simple GET. If return is >=200 and <400 it is successful
- exec -- issues a specified command within the container
- 
## Example Egeria API calls

In these examples the [httpie](https://httpie.io) tool will be used as it will print both the response code, and pretty-formatted body by default. Other tools like curl may also be used, but more parsing may be required of the responses.

The examples here were run against the lab charts, using user 'garygeeke'. A simple security plugin is active which restricts user access to api calls.

### Platform
This checks if the *platform* is available.

#### Platform is not running
➜  ~ curl -k -X GET --connect-timeout 5 --max-time 5 "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/admin/server-origin"
Egeria OMAG Server Platform (version 4.1-SNAPSHOT)

#### Platform is running
➜  ~ http --verify=no --pretty=format GET "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/admin/server-origin"
HTTP/1.1 200
Connection: keep-alive
Content-Length: 42
Content-Type: text/plain;charset=UTF-8
Date: Thu, 18 May 2023 17:10:27 GMT
Keep-Alive: timeout=60

Egeria OMAG Server Platform (version 4.0)



### Server

#### Server is not known
```
➜  ~ http --verify=no --pretty=format GET "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/admin/servers/cocoMDS99/instance/status"
HTTP/1.1 200
Connection: keep-alive
Content-Type: application/json
Date: Thu, 18 May 2023 17:08:15 GMT
Keep-Alive: timeout=60
Transfer-Encoding: chunked

{
    "actionDescription": "getActiveServerStatus",
    "class": "OMAGServerStatusResponse",
    "exceptionClassName": "org.odpi.openmetadata.frameworks.connectors.ffdc.InvalidParameterException",
    "exceptionErrorMessage": "OMAG-MULTI-TENANT-404-001 The OMAG Server cocoMDS99 is not available to service a request from user admin",
    "exceptionErrorMessageId": "OMAG-MULTI-TENANT-404-001",
    "exceptionErrorMessageParameters": [
        "cocoMDS99",
        "admin"
    ],
    "exceptionProperties": {
        "parameterName": "serverName",
        "serverName": "cocoMDS99"
    },
    "exceptionSystemAction": "The system is unable to process the request because the server is not running on the called platform.",
    "exceptionUserAction": "Verify that the correct server is being called on the correct platform and that this server is running. Retry the request when the server is available.",
    "relatedHTTPCode": 404
}

```
#### No permission for api call
```
➜  ~ http --verify=no --pretty=format GET "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/admin/servers/cocoMDS5/instance/status"
HTTP/1.1 200
Connection: keep-alive
Content-Type: application/json
Date: Thu, 18 May 2023 17:07:28 GMT
Keep-Alive: timeout=60
Transfer-Encoding: chunked

{
"actionDescription": "validateUserForServer",
"class": "OMAGServerStatusResponse",
"exceptionClassName": "org.odpi.openmetadata.commonservices.ffdc.exceptions.UserNotAuthorizedException",
"exceptionErrorMessage": "OMAG-PLATFORM-SECURITY-403-002 User admin is not authorized to issue a request to server cocoMDS5",
"exceptionSystemAction": "The system is unable to process a request from the user because they do not have access to the requested OMAG server.  The request fails with a UserNotAuthorizedException exception.",
"exceptionUserAction": "Determine whether the user should have access to the server.  If they should have, take steps to add them to the authorized list of users.  If this user should not have access, investigate where the request came from to determine if the system is under attack, or it was a mistake, or the user's tool is not configured to connect to the correct server.",
"relatedHTTPCode": 403
}
```
### Server is available
```
➜  ~ http --verify=no --pretty=format GET "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/garygeeke/servers/cocoMDS2/instance/status"
HTTP/1.1 200
Connection: keep-alive
Content-Type: application/json
Date: Thu, 18 May 2023 17:06:46 GMT
Keep-Alive: timeout=60
Transfer-Encoding: chunked

{
    "class": "OMAGServerStatusResponse",
    "relatedHTTPCode": 200,
    "serverStatus": {
        "serverActiveStatus": "RUNNING",
        "serverName": "cocoMDS2",
        "serverType": "Metadata Access Store",
        "services": [
            {
                "serviceName": "Subject Area OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Security Officer OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Open Metadata Repository Services (OMRS)",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Data Privacy OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Community Profile OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Asset Consumer OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Asset Lineage OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Open Metadata Store Services",
                "serviceStatus": "STARTING"
            },
            {
                "serviceName": "Asset Catalog OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "IT Infrastructure OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Asset Owner OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Connected Asset Services",
                "serviceStatus": "STARTING"
            },
            {
                "serviceName": "Digital Architecture OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Glossary View OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Governance Program OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Project Management OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Governance Engine OMAS",
                "serviceStatus": "RUNNING"
            },
            {
                "serviceName": "Open Integration Service",
                "serviceStatus": "STARTING"
            }
        ]
    }
}
```


## Interpreting the Egeria API calls

A timeout will occur if the platform is not running. 
In all other cases a HTTP 200 will be returned.

Finer grain detail is provided by the 'relatedHTTPCode' field within the response body - this is more similar to what might be expected from a typical status check. For example, Looking at the checks above, all return 200 as the http status code, but vary in terms of the relatedHTTPCode.

Additionally the server status call returns fine-grained information about all the services configured in a server. 

In the simplest case it would be reasonable to define that the server is not available until all services are running.

## what about connectors?

Each service running on the platform may have a dependence on connectors, such as for topics/kafka, or in the case of integration, technology connectors such as to a database. Each connector may behave differently, and in many cases not report any issue for a transient error.

## Formulating a k8s health check

We cannot use a k8s http status check since this returns 200 in most cases. Instead we need to use the 'exec' method. This will run a curl command within the container, and parse out the relatedHTTPCode, returning 0 if we think all is ok

For example
```
curl -k -o - -X GET --connect-timeout 5 --max-time 5 "https://44623abc-eu-gb.lb.appdomain.cloud:9443/open-metadata/admin-services/users/admin/servers/cocoMDS5/instance/status" | grep '.*\"relatedHTTPCode\": 200'
```

This will return 0 (healthcheck passes) if we see an embedded 200 response, and 1 otherwise, therefore satisfying the requirement for a server specific Healthcheck

## Status aggregation

The above example requires that the healthcheck is coded against a specific server. Future work will investigate the answers to:

#### Are all servers on the platform available?


#### Is everything a server provides available?
