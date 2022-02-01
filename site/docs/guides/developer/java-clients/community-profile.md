<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

## Using the Community Profile OMAS

The Community Profile OMAS is designed to cover many of the administrative tasks relating to managing
information about people, teams and communities.

Most of the interaction with the Community Profile OMAS will be driven by individuals.
 
- All users will be able to manage their [personal profile](/concepts/personal-profile)
  and [lists of favourite assets, projects and communities](/concepts/favorite-things-collection).
  
- All users will be able to manage any [to dos](/concepts/to-do) that have been assigned to them.
  
- All users will be able to create a [community](/concepts/community) and administer it.
  This includes managing members, the communities resources and the notifications sent to the members.
  
- All users can also query the [communities](/concepts/community) and
  [teams](/concepts/organization/#team.md) they are a member of. 

- All users will be able to search for people, teams and communities.

There is also support for an administrator to create and delete personal profiles as individuals join and leave the
organization and also manage the organization's departmental structure.  The assumption is that the organization
already has at least one system that manages this information, and so Community Profile OMAS is designed to be integrated
with existing systems in order to keep the profiles and departmental structure up-to-date.

Below are the list of tasks supported by the Community Profile OMAS.

### One time set up by the administrator

Many organizations already have [a system that maintains information about their employees
and/or customers and/or business partners](/concepts/software-server-capability/#master-data-manager).
The Community Profile OMAS therefore supports an event exchange with such a system
to keep the profiles synchronized. 
The following tasks cover the work of the IT team to integrate the Community Profile
OMAS with other systems.

- [Loading personal profiles of existing members of an organization](#loading-personal-profiles)
  into an open metadata repository.
- [Synchronizing updates to personal profiles from another system](#synchronizing-personal-profiles)
- [Loading the organization's departmental structure](#loading-departmental-structures)
  into an open metadata repository.
- [Synchronizing the organization's departmental structure with another system](#synchronizing-departmental-structure)
- [Capturing karma point plateaus](#capturing-karma-point-plateaus)
  emitted from the Community Profile OMAS [OutTopic](/concepts/out-topic).
- [Synchronizing collaboration activity with another system](#synchronizing-collaboration-activity)



#### Loading personal profiles

Loading the personal profiles of existing members of an organization.


#### Synchronizing personal profiles


#### Loading departmental structures

Loading an organization's departmental structure.


### Synchronizing collaboration activity with another system


### Synchronizing Departmental Structure



### Individuals working with their personal profile

A [personal profile](/concepts/personal-profile) provides a place for
an individual to share information about themselves
with the other people they are collaborating with.

Each personal profile is associated with one or more of the person's userIds.
It is retrieved using one of these userIds.

- [Retrieving my personal profile](#retrieving-my-personal-profile)

For organizations where the personal profile is not loaded from another system (see above)
an individual can maintain their own profile.

- [Creating my personal profile](#creating-my-personal-profile)
- [Updating my personal profile](#updating-my-personal-profile)
- [Removing my personal profile](#removing-my-personal-profile)

Once an individual has a personal profile, they will be awarded [karma points](/concepts/karma-point)
when they contribute content to open metadata.  An individual can query their karma points.

- [Retrieving my karma points](#retrieving-my-karma-points)

The individual can also maintain [collections](/concepts/favorite-things-collection) of their
favourite [Assets](/concepts/asset), [Projects](../../../docs/concepts/project)
and [Communities](/concepts/community) and control notifications
about changes to the contents of these lists.

- [Accessing my favorite assets](#accessing-my-favorite-assets)
- [Managing my favorite assets](#managing-my-favorite-assets)
- [Accessing my favorite projects](#accessing-my-favorite-projects)
- [Managing my favorite projects](#managing-my-favorite-projects)
- [Accessing my favorite communities](#accessing-my-favorite-communities)
- [Managing my favorite communities](#managing-my-favorite-communities).

An individual can link other [resources](/concepts/useful-resource) such as glossaries, and external references to their profile.

- [Finding resources](#finding-a-resource)
- [Accessing my resource list](#accessing-my-resource-list)
- [Managing my resource list](#managing-my-resource-list)
- [Accessing my external reference list](#accessing-my-external-references)
- [Managing my external reference list](#managing-my-external-references)

An individual can create a series of personal notes.  These are like a personal blog.
They are visible to other users who can comment on and review the content.

- [Setting up my personal notes](#setting-up-my-personal-notes)
- [Accessing my personal notes](#accessing-my-personal-notes)
- [Removing my personal notes](#removing-my-personal-notes)
- [Adding a personal note](#adding-a-personal-note)
- [Updating a personal note](#updating-a-personal-note)
- [Removing a personal note](#removing-a-personal-note)

An individual can query the [teams](/concepts/organization/#team) and
[communities](/concepts/community) they belong to.

- [Accessing my communities](#accessing-my-communities)
- [Accessing my teams](#accessing-my-teams)

An individual can access an manage a list of close colleagues
called their [peer network](/concepts/peer-network).

- [Accessing my peer network](#accessing-my-peer-network)
- [Managing my peer network](#managing-my-peer-network)

An individual can query their [roles](/concepts/personal-roles) in the organization
and any [actions (to dos)](/concepts/to-do)
that have been assigned to them as part of one of these roles.

- [Accessing my roles](#accessing-my-roles)
- [Accessing my to dos for each role](#accessing-my-to-dos)
- [Managing to dos](#managing-a-to-do)

An individual can add feedback to their profile and others (see below).

## Providing feedback and content to personal profiles

An individual can send a personal message to themselves, or another user.
This message is attached to the recipient's profile.

- [Sending a personal message](#sending-a-personal-message)
- [Replying to a personal message](#replying-to-a-personal-message)
- [Updating a personal message](#updating-a-personal-message)
- [Removing a personal message](#removing-a-personal-message)

It is possible to add comments, likes and reviews to a personal note.

- [Adding a comment to a personal note](#adding-a-comment-to-a-personal-note)
- [Updating a comment to a personal note](#updating-a-comment)
- [Removing my comment from a personal note](#removing-my-comment-from-a-personal-note)
- [Adding a review to a personal note](#adding-a-review-to-a-personal-note)
- [Updating my review to a personal note](#updating-my-review)
- [Removing my review from a personal note](#removing-my-review)
- [Adding a like to a personal note](#adding-a-like-to-a-personal-note)
- [Removing a like from a personal note](#removing-my-like-from-a-personal-note)

It is possible to create and attach [tags](/concepts/informal-tag) to
personal profiles, personal notes,
and comments either for your personal profile or someone else's.

- [Finding existing tags](#finding-a-tag)
- [Accessing resources attached to a tag](#accessing-tagged-resources)
- [Accessing my tags](#accessing-my-tags)
- [Creating a tag](#creating-a-tag)
- [Attaching a tag](#attaching-a-tag)
- [Detaching my tag](#detaching-my-tag)
- [Detaching a tag from a resource](#detaching-a-tag)
- [Deleting my private tag](#removing-my-tag)
- [Deleting public tags](#removing-a-tag)

## Individuals searching for other people and teams

Below are different ways to locate people in the organization.

- [Finding a Person](#finding-a-person)
- [Querying another's personal profile](#querying-anothers-personal-profile)
- [Navigating the Departmental Structure](#navigating-the-departmental-structure)
- [Finding a Team](#finding-a-team)
- [Accessing my teams](#accessing-my-teams)
- [Viewing Leaders of a Team](#viewing-leaders-of-a-team)
- [Viewing Members of a Team](#viewing-members-of-a-team)


## Communities

[Communities](/concepts/community) collect
together resources, best practices and ideas for a group of people
who are collaborating on a specific topic or skill.

Anyone can create a community.

- [Creating a community](#creating-a-community)

The person creating the community is the [community leader](/concepts/community-leader).
They can then add other people as [community members](/concepts/community-member)
with different [community roles](/concepts/community-roles).

- [Adding a new community member](#adding-a-new-community-member)
- [Changing a community member's role](#changing-community-member-role)
- [Removing a community member](#removing-a-community-member)

Community leaders and [administrators](/concepts/community/#community-administrator)
can remove inappropriate content from a community and close it.

- [Removing a comment from a community](#removing-a-community-comment)
- [Removing a note from a community](#removing-a-community-note)
- [Removing a review from a community](#removing-a-review)
- [Removing a resource from a community](#removing-a-community-resource)
- [Closing a community](#closing-a-community)

Individuals can locate and connect with a community.

- [Finding the communities I am a member of](#accessing-my-communities)
- [Finding a community](#finding-a-community)
- [Querying a community](#querying-a-community)
- [Watching a community](#watching-a-community)
- [Joining a community](#joining-a-community)
- [Leaving a community](#leaving-a-community)

Once someone is a member of a community they can add content to it.

- [Adding a comment to a community](#adding-a-comment-to-a-community)
- [Replying to a community comment](#replying-to-a-comment)
- [Removing my comment from a community](#removing-my-comment-from-a-community)
- [Adding a resource to a community](#adding-a-resource-to-a-resource-list)
- [Creating a community forum](#creating-a-community-forum)
- [Adding a contribution to a community forum](#adding-a-contribution-to-a-forum)
- [Removing my contribution from a community forum](#removing-a-contribution-from-a-forum)

Community content can have feedback attached in the form of tags, reviews and likes.

- [Attaching feedback to a community](#attaching-feedback-to-a-community)
- [Attaching feedback to a community comment](#attaching-feedback-to-a-community-comment)
- [Attaching feedback to a community forum](#attaching-feedback-to-a-community-forum)
- [Attaching feedback to a community forum contribution](#attaching-feedback-to-a-community-forum-contribution)

## Individual commands

### Accessing a useful resource list

It is possible to maintain a list of [useful resources](/concepts/useful-resource)
with a [personal profile](/concepts/personal-profile), a [team](/concepts/organizations/#team)
or a [community](/concepts/community).

First locate the unique identifier (guid) of the element acting as an anchor for the resource.



### Accessing an external references list


### Accessing my communities



### Accessing my external references


### Accessing my favorite assets

### Accessing my favorite communities

### Accessing my favorite projects

### Accessing my peer network

### Accessing my personal roles

### Accessing my resource list

### Accessing my roles


### Accessing my informal tags

[Tags](/concepts/informal-tag) provide an informal way of identifying particular types of resources.

### Accessing the team I am a member of

### Accessing my to dos


### Accessing tagged resources




### Adding a comment

Maybe to a community, community forum contribution


### Adding a comment to a community

Can be added to the community, or to a a forum contribution.

### Adding a comment to a personal note

Can add to personal note linked to your profile or someone else's.


### Adding a Contribution to a Community Forum

### Adding a like to a personal note

Can add like to personal note linked to your profile or someone else's.


### Adding a new community member


### Adding a personal note


### Adding a resource to a resource list


### Adding a review to a personal note

Can add to personal note linked to your profile or someone else's.

### Attaching a tag to a resource



### Attaching feedback to a community

### Attaching feedback to a community comment


### Attaching feedback to a community forum



### Attaching feedback to a community forum contribution



### Capturing karma point plateaus


### Changing a community member role



### Closing a community


### Creating a community



### Creating a community forum



### Creating a tag



### Creating a to do


### Creating my personal profile

If your organization has not already created a personal profile for you then it is possible to
create the profile yourself.

The information that you will need is as follows.  Many of the fields are optional but the
more information that you supply, the easier it will be for people to locate you.

- qualified name - this is a unique identifier for you - for example if you are an employee of
the organization then use your employee number.
- name - this is the name that you want to be known by.
- full name - this is your full legal name.  This is optional.
- job title - this is also optional.
- job description - this is a short paragraph describing what your role is.  It is optional.
- contact details such as email address, phone number social media account.


#### See also

- [Managing my contact details](#managing-my-contact-details)


#### Design note

The Community Profile OMAS will emit an [event](/concepts/out-topic) whenever a new profile is created
using this approach


### Detaching a tag from a resource

Find the resource and detach the tag.

### Detaching my tag from a resource


### Finding a community



### Finding a person


### Finding a resource



### Finding a tag

Find request, then browse results.  Then query?



### Finding a team



### Joining a community

Add a to do on community administrators


### Leaving a community

Add a to-do on a community administrator


### Managing an action (to do)



### Managing my contact details



### Managing my external references


### Managing my favorite assets



### Managing my favorite communities



### Managing my favorite projects


### Managing my peer network


### Managing my resource List


### Navigating the departmental structure of an organization


### Querying a community


### Querying anothers personal profile


### Removing a comment from a community


### Removing a community member



### Removing a community note



### Removing a community resource


### Removing a contribution from a forum


### Removing a like

This is from anything



### Removing a personal message


### Removing a personal note


### Removing a review

Can do if own the thing review is being removed from.



### Removing a public tag

Can do it if not attached to anything



### Removing my comment from a community


### Removing my comment from a personal note

### Removing my like from a personal note



### Removing my personal notes



### Removing my personal profile


### Removing my review

Can do if own the review.


### Removing my tag

### Replying to a comment



### Replying to a personal message


#### Retrieving my karma points

If an individual has a
[Personal profile](/concepts/personal-profile)
the Community Profile OMAS will reward him/her whenever
they contribute to open metadata.
These rewards are in the form of
[karma points](/concepts/karma-point).

The Community Profile OMAS is responsible for maintaining the count of
the karma points.  It does this by listening to the metadata changes
occurring in the metadata repositories and updates the personal
profile of each user making a contribution.

The Community Profile OMAS provides a method/operation
to allow an individual to retrieve their current karma point
total.

The access service option property *KarmaPointPlateau* indicates
the multiple of karma points for an individual that results in
an external event being published - the default is 500.  This
means that when an individual gets to 500 karma points, and event is sent,
and other event is sent when they get to 1000 karma points and so on.
These events can be used to trigger additional recognition activities for
the individuals concerned.







### Retrieving my personal profile

Every user accessing the open metadata ecosystem has a unique user identity (userId).
This identity is used for authentication, authorization and auditing of activity
related to open metadata and governance.

Optionally a user identity can be associated with a
[personal profile](/concepts/personal-profile).
This provides information about the user behind the userId
and aims to improve collaboration across the organization.

#### If you do not have a personal profile

An organization can choose to
[load personal profiles automatically](loading-personal-profiles.md)
Alternatively, it can be left to the individual to
[create their own personal profile](creating-my-personal-profile.md).



### Sending a personal message

Link through to adding a comment or separate method?


### Setting up my personal notes



# Updating a comment



# Updating a personal message


# Updating a personal note


# Updating my personal profile


Include adding another userId to the profile

## See also

- [Managing my contact details](#managing-my-contact-details)



# Updating my review


# Viewing leaders of a team

# Viewing members of a team


# Watching a community

Add yourself as an observer.





--8<-- "snippets/abbr.md"
