<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Logon problems

When a user logs on, if all is well, they receive a bearer token.  If, however, the user
is unable to log on, there are several potential causes to investigate.  This guide
provides a step-by-step approach to diagnosing and resolving common logon issues.

There are two places where diagnostics are logged:

* An error is returned on the logon request with a 401 HTTP error.
* Debug logging is written to the console.

This means that the error can be diagnosed by the team running the platform, or the client-side team.

## The user does have an account

This is the error returned to the requester if the user does not have an account.

```json
{
  "class": "FFDCResponseBase",
  "relatedHTTPCode": 401,
  "exceptionClassName": "org.springframework.security.authentication.AuthenticationServiceException",
  "exceptionErrorMessage": "User account not found for user: freddiemercury.",
  "exceptionSystemAction": "The system is unable to authenticate the calling user and an error is returned.",
  "exceptionUserAction": "Check the status of the user's account and credentials and try again."
}
```
This is the console logging:
```
Security OPEN-METADATA-SECURITY-0022 User freddiemercury is not recognized
16:53:51.158 [https-jsse-nio-9443-exec-4] ERROR o.o.o.userauthn.LoginController - User account not found for user: freddiemercury.
16:53:51.160 [https-jsse-nio-9443-exec-4] ERROR o.o.o.u.AuthenticationExceptionHandler - Authentication error: User account not found for user: freddiemercury.
org.springframework.security.authentication.AuthenticationServiceException: User account not found for user: freddiemercury.
	at org.odpi.openmetadata.userauthn.LoginController.platformToken(LoginController.java:136)
	at jdk.internal.reflect.GeneratedMethodAccessor544.invoke(Unknown Source)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:205)
	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:150)
	at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)
	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:884)

```

## The user is using the wrong password

This is the error returned to the requester if the user is using the wrong password.

```json
{
  "class": "FFDCResponseBase",
  "relatedHTTPCode": 401,
  "exceptionClassName": "org.springframework.security.authentication.AuthenticationServiceException",
  "exceptionErrorMessage": "User authentication failed for user: calliequartile - Bad credentials",
  "exceptionSystemAction": "The system is unable to authenticate the calling user and an error is returned.",
  "exceptionUserAction": "Check the status of the user's account and credentials and try again."
}
```

This is the console logging:

```bash
16:55:21.807 [https-jsse-nio-9443-exec-2] ERROR o.o.o.userauthn.LoginController - User authentication failed for user: calliequartile - Bad credentials
16:55:21.808 [https-jsse-nio-9443-exec-2] ERROR o.o.o.u.AuthenticationExceptionHandler - Authentication error: User authentication failed for user: calliequartile - Bad credentials
org.springframework.security.authentication.AuthenticationServiceException: User authentication failed for user: calliequartile - Bad credentials
	at org.odpi.openmetadata.userauthn.LoginController.platformToken(LoginController.java:90)
	at jdk.internal.reflect.GeneratedMethodAccessor544.invoke(Unknown Source)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:205)
	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:150)
	at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)
	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:884)
```

## The user's credentials are expired

This is the error returned to the requester if the user's credentials have expired.

```json
{
  "class": "FFDCResponseBase",
  "relatedHTTPCode": 401,
  "exceptionClassName": "org.springframework.security.authentication.AuthenticationServiceException",
  "exceptionErrorMessage": "Credentials expired for user: freddiemercury.",
  "exceptionSystemAction": "The system is unable to authenticate the calling user and an error is returned.",
  "exceptionUserAction": "Check the status of the user's account and credentials and try again."
}
```
This is the console logging:
```bash
Security OPEN-METADATA-SECURITY-0024 User freddiemercury has expired credentials
16:56:52.602 [https-jsse-nio-9443-exec-11] ERROR o.o.o.userauthn.LoginController - Credentials expired for user: freddiemercury.
16:56:52.602 [https-jsse-nio-9443-exec-11] ERROR o.o.o.u.AuthenticationExceptionHandler - Authentication error: Credentials expired for user: freddiemercury.
org.springframework.security.authentication.AuthenticationServiceException: Credentials expired for user: freddiemercury.
	at org.odpi.openmetadata.userauthn.LoginController.platformToken(LoginController.java:130)
	at jdk.internal.reflect.GeneratedMethodAccessor544.invoke(Unknown Source)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:205)
	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:150)
	at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)
	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:884)
```

--8<-- "snippets/abbr.md"
