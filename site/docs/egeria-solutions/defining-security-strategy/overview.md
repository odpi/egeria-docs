<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Defining Security Strategy

The purpose of defining your security strategy is to clarify what it means to have a secure system and to provide practical guidance to everyone on what they need to do to keep the organization secure.

A security strategy that lives only in a document tends to be read once and then forgotten.  This solution captures the strategy as linked [governance definitions](/concepts/governance-definition) in Egeria instead.  Each policy is linked to the reason it exists and to the controls that show whether it is being followed, so the strategy can be navigated, measured and audited, and it can be connected to the other governance programs in the organization.

## Start from an established framework

There is no need to invent a security program from scratch.  Established frameworks, such as the ISO/IEC 27001 standard for an information security management system (ISMS), the NIST Cybersecurity Framework, and the guidance published by [OWASP](https://owasp.org/), describe what a well-run security program does and provide reference sets of controls.  Building on one of these gives you a structure that auditors, partners and regulators recognise, and frees your security experts to concentrate on the aspects that are unique to your business.

The framework you choose becomes a [certification type](/types/4/0482-Certifications) if you plan to be certified against it, or a [regulation](/types/4/0405-Governance-Drivers) or external reference if it is guidance you are following.

## The structure of a security strategy

The governance definitions fall into four layers.

???+ info "Drivers - why security matters to this organization"
    [Governance drivers](/types/4/0405-Governance-Drivers) describe the reasons for the strategy.  They include *business imperatives* (for example, the need to be cyber resilient), *threats* (for example, a cyber-attack on operations or data), and *regulations* that impose security requirements.  Drivers are often shared with other governance domains, so check whether they have already been defined before creating new ones.

???+ info "Risks - what could actually go wrong"
    [Risks](/types/4/0415-Governance-Responses) turn an abstract threat into a concrete, assessable consequence for this organization, rated for likelihood and impact.  "Cyber-attack" is a threat; "ransomware could encrypt the manufacturing control systems and halt production" is a risk.  Each risk records the implications that must be true for the organization to be able to say it has responded, and it is the risks that the policies are written against.  The [*ScopedBy*](/types/1/0120-Assignment-Scopes) relationship links a risk to the systems, assets, teams or other elements it applies to.  The [Threat Modelling](/egeria-solutions/threat-modelling/overview) solution describes how to find them.

???+ info "Policies - how the organization responds"
    [Governance policies](/types/4/0415-Governance-Responses) set out the response:

    * *Principles* state the beliefs that guide decisions, such as "security controls are selected according to an assessment of risk".
    * *Obligations* state what must be done, such as "every information asset must be inventoried and classified" or "staff must complete annual security awareness training".
    * *Approaches* describe how the organization chooses to operate, such as running the ISMS as a continuous plan-do-check-act cycle.

    Each policy is linked to the drivers it responds to with the [*GovernanceResponse*](/types/4/0415-Governance-Responses) relationship, and related policies are linked to one another with the *GovernancePolicyLink* relationship.

???+ info "Controls - how compliance is achieved and measured"
    [Governance controls](/types/4/0420-Governance-Controls) implement the policies.  They include technical controls, [organizational controls](/types/4/0440-Organizational-Controls) such as [governance roles](/types/4/0445-Governance-Roles) and responsibilities, certifications, and *governance metrics* that measure whether a policy is being followed - for example the percentage of applicable controls that are implemented, the mean time to contain an incident, or the training completion rate.  Each control is linked to the policy it implements with the [*GovernanceMechanism*](/types/4/0420-Governance-Controls) relationship.

!!! summary "Usage"
    Following the links from any control back through the policy to the risk and threat behind it answers the question *why do we do this?*  Following them forwards from a risk shows *what are we doing about it, and is it working?*  A risk with no policy, or a policy with no control, is a gap that is visible in the model.

## Security levels and classification

Most security strategies define a set of levels that systems and data are organized into, depending on how sensitive or critical they are.  The strategy then sets out what a system owner must do at each level - for example, the strength of authentication required, how often access is reviewed, whether data must be encrypted, and how quickly patches must be applied.  This means that individual owners do not have to work out the right protection for each system from first principles.

Egeria's [governed data classifications](/types/4/0422-Governed-Data-Classifications) - *Confidentiality*, *Criticality*, *Impact* and *Retention* - can be attached to assets and other elements to record the level that applies.  The values used for each level are defined as [valid metadata values](/guides/planning/valid-values/overview), so they can be tailored to your strategy.  Where a security engine needs to act on the classification, [security tags](/concepts/security-tags) and [governance zones](/features/governance-zoning/overview) carry it to the point of enforcement.

If personal data is classified separately by the privacy team, the two schemes need to be kept consistent so that assets that hold both kinds of sensitive information are protected coherently.  Linking the related obligations in Egeria makes that dependency explicit.

## Security as a shared responsibility

A security strategy cannot be delivered by the security team alone.  When the obligations are written down it quickly becomes clear how much depends on other teams:

* the asset inventory depends on the IT infrastructure team's knowledge of what systems are running - and keeping it current depends on [proactive cataloguing](/egeria-solutions/proactive-cataloguing/overview) as systems are deployed.
* revoking the access of people who leave depends on human resources notifying the security team.
* assessing suppliers depends on the finance and procurement teams knowing who the third parties are.
* security awareness depends on education reaching every employee and contractor.

Recording these as links between the security definitions and the definitions in other governance domains turns assumptions into explicit commitments.  It also helps to bake security into the way the business works, in the same way as data governance, rather than treating it as a layer applied on top.  The [governance domains](/concepts/governance-domain) and the governance folios that collect each leader's definitions make it easy for each team to see its part.

## Creating the definitions

The definitions are typically written as [Dr.Egeria](/user-interfaces/dr-egeria/overview) Markdown documents, which can be reviewed and edited by the security team before they are loaded into Egeria.  They can also be maintained through the [Governance Officer API](/services/omvs/governance-officer/overview), and viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview).  The [Security Officer API](/services/omvs/security-officer/overview) is used to set up the governance zones and security access controls that protect open metadata itself.

## Example

[Building a data security strategy](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview) shows how Coco Pharmaceuticals' security team builds its strategy around ISO/IEC 27001, linking the new principle, obligations, approach, certification and metrics to the drivers and risks that the governance leaders had already defined.

--8<-- "snippets/abbr.md"
