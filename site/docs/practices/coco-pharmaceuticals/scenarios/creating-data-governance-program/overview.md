<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Creating a data governance program

![Icon](/practices/coco-pharmaceuticals/personas/jules-keeper.png)

[Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) is the Chief Data Officer (CDO) for Coco Pharmaceuticals. He is responsible for improving the management and use of their information. This includes the information governance program.

When Jules joined Coco Pharmaceuticals the rules for handling data were documented on an internal website. They defined how researchers should manage data for clinical trials in order to be compliant with FDA regulations.

A recent fraud incident with a bogus supplier and demands to use more data by the clinical research teams showed that the company should have a more focused approach to information governance - and so Jules was appointed CDO.

In this scenario we walk through the steps that Jules takes to set up a governance program for Coco Pharmaceuticals.  This includes:

* Defining classification schemes for information, technology capability, roles and activities.

* Defining policies and rules that specify how information of each classification should be handled when working with a particular classification of technology or performing a certain classification of activity in a particular context.

* Making the governance program actionable by assigning governance roles and responsibilities, providing education and commissioning new IT projects to improve the automation of the information landscape.


## Data governance policies

The governance policies are divided into three main groups:

* *Principles*: Data governance principles define the high-level goals and approaches of the information governance program.  They are defined by the program leaders and provide the terms of reference for all decisions made as part of the information governance program.
* *Obligations*: Obligations define policies that have been delegated from other governance focus areas and domains.   The data governance program supports not just the implementation of obligations, but also provides the mechanisms for measuring compliance, reporting exceptions and supporting auditing in the terms of the delegated policies.
* *Approaches*: Approaches describe the standards that have been adopted by the data governance program to increase consistency and remove unnecessary mapping between different implementations.

## Establishing the data governance principles

As the CDO, Jules first establishes the top-level data governance policies.  These are called the governance principles since they underpin all other data governance decisions.

The principles are defined as follows:

* Information is a company asset.  It will be managed according to the prescribed governance policies.
* Information is identified and classified. All information stored by the company will be identified and classified according to its sensitivity and content.  This classification will determine how the information will be governed.
* Information is a sharable resource and should be made available for all legitimate needs of the company.
* Information is owned.  There is an individual responsible for the appropriate management and governance of each information collection.
* Information users are identified. An individual will be identified and be accountable for each access and change they make to information.
* Information users are responsible. Individuals are responsible for safeguarding the information that they own, access and use.
* Decision makers are responsible for ensuring they are using information of appropriate integrity for their work.
* Information is kept as long as it is needed.  Information that is no longer needed will be disposed of appropriately.
* Information is protected. Information is secured from unauthorized access and use.
* Information quality is everyone’s responsibility.  Information is validated and where necessary it is corrected and made complete.
* Information is managed in a cost effective manner.   This is achieved through a well-defined information architecture that follows standards and best practices.
* Information and analytics will be only be used for approved, ethical purposes.

The governance principles are added to open metadata using the [Governance Officer](/services/omvs/governance-officer/overview) API.

Ivor and Faith have governance leadership roles in other governance domains.  The principles that Jules is defining need to tie into their work. 

Jules works with other members of the company to define more detailed policies and rules in the metadata catalog.  He considers:

* How do they define KPIs and their status?

* How do they automate the measurement and monitoring of these principles.

For example, for the principle *Information users are identified* Ivor may define additional security principles such as

* *Everyone has their own user logon*
* *Passwords must be changed frequently*
* *passwords must be secure*


## Data policy driving the governance lifecycle

1. Jules Keeper establishes a set of information governance principles that will be the foundation of the governance program.  These are widely reviewed and agreed and loaded into the governance catalog.
2. Jules works with Ivor Padlock (Security) and Faith Keeper (Auditor) to expand the definitions of the principles to cover the security and audit requirements around information.
3. Each of the information owners, such as Tom Tally (Accounts Manager), Tessa Tube (Lead Researcher) and Harry Hopeful (Sales) work with Jules and Erin Overview (Information Architect) to consider how these principles should be implemented for their information.  They flesh out more detailed policies and rules that they will follow.  Again these are documented in the Governance catalog.
4. Erin and Peter Profile (Information Analyst) ensure information is classified correctly so they are assigned to the correct policies and rules.  The classification involves creating a basic definition to the information sources and classifying them according to their content. 
5. For important sources, Peter uses the survey framework is used to initiate deeper analysis of the information sources.   He sets this analysis up to run over night when the load on the systems is low.
6. Erin asks Polly Tasker (IT Project Manager) to get her team to implement some new quality rules and exception management capability to support the program.
7. Individuals are given responsibility for correcting errors that are found in particular types of data.  For example, Harry Hopeful (Sales) becomes responsible for data about his customers.  He is notified when issues are discovered and he must fix them as soon as possible.
8. The summaries of the rules execution and exceptions detected are recorded for Jules to review.  He is looking for continual improvement.  He reviews the results with Erin and they plan further improvements.


--8<-- "snippets/abbr.md"
