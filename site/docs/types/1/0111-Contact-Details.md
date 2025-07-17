<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0111 Contact Details

Contact details link actors to the mechanism that can be used to contact them.  There is one instance of contact details for each communication mechanism.  For example, if a person has an email address and a phone number, there would be two contact detail entities attached to the profile for this person. 

![UML](0111-Contact-Details.svg)

## ContactMethodType enum

The *ContactMethodType* enum defines some common communication mechanisms.

* EMAIL - email
* PHONE - landline or mobile
* CHAT - instant messaging
* PROFILE - add message to actor profile
* ACCOUNT - via an application account
* OTHER - another type of contact method

## ContactDetails entity
 
* The *ContactDetails* entity is a [Referenceable](/types/0/0010-Base-Model) that describes the mechanisms to contact an [actor](/types/1/0110-Actors) - this is typically linked to actor profiles for people and teams.

- *contactMethodType* - the type of communication method.  If OTHER is used, the *contactType* can be used to describe another mechanism.

- contactType* - an alternative way to describe the communication mechanism.
  
- *contactMethodService* - the type of service to call to invoke this contact method.

- *contactMethodValue* - the address or account name or number to use for this contact method.
 
## ContactThrough Relationship

The *ContactThrough* relationship links a referenceable to its contact details.

--8<-- "snippets/abbr.md"
