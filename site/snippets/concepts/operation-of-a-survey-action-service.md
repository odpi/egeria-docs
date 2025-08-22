<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

![Operation of a survey action service](/frameworks/osf/survey-action-service-operation.svg)
    
1. Each time a survey action service runs, Egeria creates a survey report to describe the status and results of the survey action service's execution.  The survey action service is passed a [survey context](/frameworks/osf/overview/#survey-context) that provides access to metadata.
2. The *survey context* is able to supply metadata about the asset and create a connector to the digital resource using the connection information linked to the asset.  The survey action service uses the connector to access the digital resource's contents in order to perform the analysis.
3. The survey action service creates *annotations* to record the results of its analysis. It adds them to the survey context which stores them in open metadata attached to the survey report.
4. The annotations can be reviewed and commented on through an external stewardship process.  This means choices from, for example, a list of potential options proposed by the survey action services, can be verified and the best one selected by an individual expert.  The resulting choices are added to annotation reviews attached to the appropriate annotations.
5. The next time the survey action service runs, a new survey report is created to link new attachments.  
6. The survey context provides access to the existing attachments for that asset along with any annotation reviews.  The survey action services is able to link its new annotations to the existing annotations as an annotation extension.  This means that the stewards can see the history associated with the new information.




