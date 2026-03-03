<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Security Officer API

The Security Officer API supports the configuration of security in the open metadata ecosystem. This includes configuring users that wish to connect to the open metadata ecosystem and controlling their visibility to open metadata.

## Managing the User Directory

Access to open metadata is secured using a bearer token passed on each API request.  The bearer token is an encrypted string that identifies the user.  

```
eyJraWQiOiJjNTU2Mjc2NC01NjNhLTQ3NGItOWUwNC1hZjQwYWM5YTgzMjMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoiZ2FyeWdlZWtlIiwiZXhwIjoxNzcyNTczNTM5LCJpYXQiOjE3NzI1Njk5MzksImRpc3BsYXlOYW1lIjoiR2FyeSBHZWVrZSJ9.NCcePbF6DxLT7p1Apm76zJEiHmuAiLFvZ6m4fw5EaRaJK0n4n0bRoKIINPL8ok9EaEgYDZ_cbUcsuFqoOjizITDoakBEnvIg5iwvSr_DKcXBg08EoP9_W0ebeW0Gxxed40TIUFDnOaMT6wO4co5xXkKKFzJCSzfIUXtSu7M5uzBOSWDys3LXzIBZiNu8kE2tOvII5pyCCEX4ex1LfyqpmH35ChG87gBdLDUkPQo_R9N8wdbE7Wdc5Z-PbnA5lz3fjmmlyZlII3kui26etbfVV3gHFz4K1eget3fnCsocJ0wCF6PtsPyDpohXREnCB7Et2g5UFInzn13NpkU_6n-QcQ

```
> **Figure 1:** An example of a bearer token.

The user *logs on* to the open metadata ecosystem by providing their *account user Id* and password.  A bearer token is returned to the user, saved and used to authenticate subsequent API calls.

??? info "Code sample - requesting a bearer token"

    === "REST"
        ```
        POST {{baseURL}}/api/token
        Content-Type: application/json
        
        {
        "userId" : "garygeeke",
        "password" : "secret"
        }
        
        > {% client.global.set("garyToken", response.body); %}
        ```
 
    === "Python"
         ```
         from pyegeria import SecurityOfficer
         
         security_officer = SecurityOfficer(view_server, url, user_id, user_pwd)
         token = security_officer.create_egeria_bearer_token()
         ```

Each bearer token lasts an hour before it expires.  Then the user is required to log on again to receive a new bearer token.

The user directory defines the users that are approved to log on to the open metadata ecosystem, the secrets (such as password) used to verify the identity of a user when they log on, and the security roles and groups they are assigned to, authorizing them to access particular subsets of open metadata and issue certain commands.  The definition of a user is called a *user account* and is identified by their *account user Id*.

![Using bearer tokens to secure API requests](using-bearer-tokens.svg)
> **Figure 2:** Using bearer tokens to secure API requests

The implementation of the user directory is accessed through a [secrets store connector](/concepts/secrets-store-connector).  The Security Officer API is able to retrieve, add, and update the user accounts for an [OMAG Server Platform](/concepts/omag-server-platform) by connecting to the platform's secrets store connector that is managing its user directory.

### Inside the User Directory

The default set-up of Egeria includes a user directory populated with [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) users. For example, this is the user account for Gary Geeke, Coco Pharmaceuticals' head of IT.

```json
{
  "class": "UserAccountResponse",
  "requestId": "ee6952ac-2fb1-4c27-a359-288d7863706a",
  "relatedHTTPCode": 200,
  "userAccount": {
    "userName": "Gary Geeke",
    "securityRoles": [
      "serverAdministrator",
      "infrastructureTeam",
      "governanceOfficer",
      "manager",
      "openMetadataMember"
    ],
    "userAccountStatus": "AVAILABLE",
    "secrets": {
      "clearPassword": "secret"
    },
    "userId": "garygeeke"
  }
}
```
> **Figure 2:** Gary Geeke's user account

It was retrieved from the user directory using the *getUserAccount* Security Officer API call.  This call requires the unique identifier (GUID) of the OMAG Server Platform, which may be extracted using the [Runtime Manager API](/services/omvs/runtime-manager/overview).

??? info "Code sample - retrieving a user account"

    === "REST"
         ```
         ###
         # Retrieve the platform GUID
         # https://egeria-project.org/types/0037-Software-Server-Platforms/
         
         ###
         # @name getPlatformsByName
         # Returns the list of platforms with a particular name. The name is specified in the filter.
         POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/runtime-manager/platforms/by-name
         Authorization: Bearer {{garyToken}}
         Content-Type: application/json
         
         {
         "filter" : "Local OMAG Server Platform"
         }
         
         > {% client.global.set("omagServerPlatformGUID", response.body.elements[0].elementHeader.guid); %}
         
         ###
         ## Retrieve Gary's user account
         GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/security-officer/platforms/{{omagServerPlatformGUID}}/user-accounts/garygeeke
         Authorization: Bearer {{garyToken}}
         ```
 
    === "Python"
         ```
         Python example to follow
         ```

A user may retrieve their own user account.  A user with a security role of `serverAdministrator` such as Gary Geeke, can also retrieve the user account of any other user.  The `serverAdministrator` security role also allows new users to be added to the user directory, updated and deleted.

### Creating or Updating a User Account

The next code sample creates a new account for Freddie Mercury (account user id is `freddiemercury`).  

??? info "Code sample - Creating or updating a user account"

    === "REST"
         ```
         ###
         
         # @name: setUserAccount
         POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/security-officer/platforms/{{omagServerPlatformGUID}}/user-accounts
         Authorization: Bearer {{garyToken}}
         Content-Type: application/json
         
         {
             "class" : "UserAccountRequestBody",
             "userAccount": {
                 "class" : "OpenMetadataUserAccount",
                 "userId": "freddiemercury",
                 "userName": "Freddie Mercury",
                 "userAccountType": "EXTERNAL",
                 "employeeNumber": "",
                 "employeeType": "",
                 "givenName": "Freddie",
                 "surname": "Mercury",
                 "email": "freddiemercury@queen.com",
                 "securityRoles": ["openMetadataMember"],
                 "zoneAccess": {
                    "music" : [
                        "READ",
                        "CREATE",
                        "UPDATE_PROPERTIES",
                        "DELETE",
                        "ATTACH",
                        "DETACH",
                        "ADD_MEMBER",
                        "DELETE_MEMBER",
                        "ADD_FEEDBACK",
                        "DELETE_FEEDBACK",
                        "CLASSIFY",
                        "DECLASSIFY",
                        "PUBLISH"]
                 },
                 "userAccountStatus": "CREDENTIALS_EXPIRED",
                 "secrets": {
                    "clearPassword" : "itsakindofmagic"
                 }
             }
         }
         
         ```
 
    === "Python"
         ```
         Python example to follow
         ```

Notice that the status of the user account is set to `CREDENTIALS_EXPIRED`.  This will force the new user to change their password on their first login.  Also notice that the initial password is stored in the clear text.  When the user logs on and supplies a new password, their new password is encrypted in the user directory to keep it private to the user.

### Deleting a User Account

The full list of account statuses are:

* `AVAILABLE` - the user account is available for use.
* `CREDENTIALS_EXPIRED` - the user account has expired and requires a new password.
* `LOCKED` - The user account is in use but is temporarily locked.  The user cannot logon until the lock is removed.
* `DISABLED` - the user account is disabled and cannot be used.

When a user is to be removed from the system, the account can be set to `DISABLED` status, or completely deleted.

??? info "Code sample - deleting a user account"

    === "REST"
         ```
         ###
         ## Deleting Freddie's user account
         DELETE {{baseURL}}/servers/{{viewServer}}/api/open-metadata/security-officer/platforms/{{omagServerPlatformGUID}}/user-accounts/freddiemercury
         Authorization: Bearer {{garyToken}}
         ```
 
    === "Python"
         ```
         Python example to follow
         ```

### Unauthorized Users

If the user is not authorized to perform operations on a user account, the server will return the following error:

```json
{
  "class": "VoidResponse",
  "requestId": "d84938bd-4cf1-4f8c-a7c8-9496a9301850",
  "relatedHTTPCode": 403,
  "exceptionClassName": "org.odpi.openmetadata.frameworks.openmetadata.ffdc.UserNotAuthorizedException",
  "exceptionSubclassName": "org.odpi.openmetadata.frameworks.openmetadata.ffdc.UserNotAuthorizedException",
  "actionDescription": "validateUserAsOperatorForPlatform",
  "exceptionErrorMessage": "OMAG-PLATFORM-SECURITY-403-001 User calliequartile is not authorized to issue Operator request to Coco Pharmaceuticals Platform",
  "exceptionErrorMessageId": "OMAG-PLATFORM-SECURITY-403-001",
  "exceptionErrorMessageParameters": [
    "calliequartile",
    "Operator",
    "Coco Pharmaceuticals Platform"
  ],
  "exceptionSystemAction": "The system cannot process a request from the user because they do not have access to the requested platform services.  The request fails with a UserNotAuthorizedException exception.",
  "exceptionUserAction": "Determine if this is a configuration error, a mistake or the platform is under attack.  Correct any configuration error and re-run the request, if it is a valid request; otherwise contact your security team.",
  "exceptionProperties": {
    "userId": "calliequartile"
  }
}
```
???+ info "Further information"
    * User accounts and secrets store connectors are defined by the [Open Connector Framework (OCF)](/frameworks/ocf/overview).
    * A new user can create their own profile to showcase their roles and achievements using the [My Profile API](/services/omvs/my-profile/overview).
    * The [Egeria-coco-manage-users.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/security-officer/Egeria-coco-manage-users.http) HTTP Client Collection walks through the process of onboarding a new user into the Egeria platform.

??? info "More on the Coco Pharmaceuticals user directory"
    The user directory is stored in a YAML file (`coco-user-directory.omsecrets`) in the local file system.  This file is configured in the `application.properties` file of the [OMAG Server Platform](/guides/admin/configuring-the-omag-server-platform).

    ```yaml
    ###############################################
    ### Set up the platform metadata security connector that provides authorization
    ### for platform administration, server operations and diagnostic calls.
    ### By default, there is no platform metadata security connector.
    ### The values below are for a sample platform metadata security connector based off of Coco Pharmaceutical persona
    ###############################################
    platform.security.provider=org.odpi.openmetadata.metadatasecurity.accessconnector.OpenMetadataAccessSecurityProvider
    platform.security.name=Coco Pharmaceuticals Platform
    platform.security.secrets.provider=org.odpi.openmetadata.adapters.connectors.secretsstore.yaml.YAMLSecretsStoreProvider
    platform.security.secrets.location=loading-bay/secrets/coco-user-directory.omsecrets
    platform.security.secrets.collection=userDirectory
    ```
    
    Therefore, it is straight-forward to create your own user directory and configure it in the `application.properties` file.




## Managing the Security Controls

--8<-- "snippets/work-in-progress.md"


???+ info "Further information"
    * Governance Zones, security groups and security access controls are managed using the capabilities of the [Governance Officer API](/services/omvs/governance-officer/overview).

---8<-- "snippets/abbr.md"






