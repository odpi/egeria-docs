<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Auditing Users

The misuse of user accounts is one of the major causes of security breaches.  Accounts belonging to people who have left, accounts with weak or default passwords, and accounts that nobody can explain all give an attacker a way in that looks like legitimate use.  Regularly reviewing who has access - and removing what is no longer needed - is one of the simplest and most effective security controls there is.

The *Auditing Users* solution helps the security team carry out these reviews for Egeria itself.  Since open metadata describes an organization's systems, data, people and risks, it is a valuable resource that must be kept safe and trusted.  Knowing that every user of Egeria is genuine, accountable and has only the access they need is part of that.

## Users in Egeria

Two different things describe a user in Egeria:

* A **user account** in the OMAG Server Platform's user directory.  This is what the user logs on with.  It holds the user's identifier, their secrets (such as a password), the security roles and groups they belong to, and a status - *Available*, *Locked*, *Credentials expired* or *Disabled*.  The user directory is accessed through a [secrets store connector](/concepts/secrets-store-connector).
* A [**user identity**](/concepts/user-identity) in open metadata.  This links the account's user identifier to a profile of the person, team or digital process that uses it, so that the actions recorded in open metadata can be traced back to who - or what - took them.

When the two match up, every account in use has a known owner, and every action can be attributed.  The audit looks for the places where they do not.

## The audit checks

The OMAG Server Platform cataloguer routinely compares the user directory with open metadata and raises an exception for each problem it finds:

| Exception | What it means | Typical remedy |
|---|---|---|
| *Clear Text Password* | An active user account still has a clear text password, such as the one used to bootstrap a new installation. | Set the account to *Credentials expired* so the user must change the password at their next log on, or disable the account. |
| *Missing User Identity* | An active user account has no corresponding user identity in open metadata, so nobody can tell who it belongs to. | Create the user identity and profile, or disable or remove the account if it is not needed. |
| *Missing User Account* | A user identity in open metadata has no user account, so the person or process it describes cannot connect. | Create the account if access is needed; otherwise this may simply reflect a user who has left. |
| *Missing Zone Access Control* | A [governance zone](/features/governance-zoning/overview) used in open metadata has no security access control in the user directory, so no-one can access the elements that are only in that zone. | Add a security access control for the zone, or remove the zone from the elements that use it. |

A missing user identity is not always an error - people typically create their profile through [My Egeria](/user-interfaces/my-egeria/overview) the first time they log on.  Digital processes, however, need their profiles created for them, and it is good practice to do so in order to simplify the identification of who or what took specific actions.

## Carrying out the review

The exceptions are displayed in [Egeria Audit](/user-interfaces/egeria-audit/overview), which is reached from the Egeria portal.  It also lists the user accounts in the user directory, with options to change their status, disable them or remove them.  This allows the security team to complete a review quickly and to fix what they find as they go.

The same operations are available through the [Security Officer API](/services/omvs/security-officer/overview), which can retrieve, create, update and delete user accounts, and maintain the security access controls for governance zones.  This makes it possible to automate parts of the review, or to integrate it with the organization's own identity management processes - for example, disabling accounts when human resources reports that someone has left.

!!! summary "Usage"
    Auditing users keeps the access to open metadata aligned with the people and processes that genuinely need it.  It turns the obligation that *all users must be authenticated and accountable* into a routine, evidenced check rather than an occasional clean-up.

## Example

[Auditing IT System Users](/practices/coco-pharmaceuticals/scenarios/auditing-it-system-users/overview) shows the Coco Pharmaceuticals security team using Egeria Audit after a fraud in which accounts of employees who had left the company were used to add false supplier records and invoices.  The screenshots in that scenario are taken from the [Quickstart](/egeria-workspaces/quick-start/overview) demo environment.

--8<-- "snippets/abbr.md"
