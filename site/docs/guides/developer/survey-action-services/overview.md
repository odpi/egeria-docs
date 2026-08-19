<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing a Survey Action Service

A [survey action service](/concepts/survey-action-service) analyses the content of a [digital resource](/concepts/digital-resource) and records what it finds as [annotations](/concepts/survey-report/#annotations) in a [survey report](/concepts/survey-report) attached to the resource's [asset](/concepts/asset).  It does not change the asset itself - it reports, and leaves the decision about what to do with its findings to a [governance action service](/guides/developer/governance-action-services/overview) or a steward.

It is implemented as a specialized [Open Connector Framework (OCF)](/frameworks/ocf/overview) connector. This means it has two parts to it: a *connector provider* that is responsible for creating a new instance of the survey action service and the *survey action service implementation* (that is the *connector implementation* in the OCF terminology.)

??? education "What the framework gives you"
    The [Open Survey Framework (OSF)](/frameworks/osf/overview) describes the annotation types, the structure of a survey report, and the kinds of analysis a survey can perform.  This page covers how to build one.

## Dependencies

The interfaces and base classes of the connector provider and survey action service implementation are provided by the [Open Survey Framework (OSF)](/frameworks/osf/overview).  This means you need to include the following Egeria modules in your build script:

* [Open Connector Framework (OCF)](/frameworks/ocf/overview) - basic connector interfaces.
* [Open Survey Framework (OSF)](/frameworks/osf/overview) - the survey action service base classes, the survey context and the annotation store.
* [Open Metadata Framework (OMF)](/frameworks/omf/overview) - the open metadata clients, properties and types used by the context.
* [Open Governance Framework (OGF)](/frameworks/ogf/overview) - the connector provider base class, guards and completion status.
* [Audit Log Framework (ALF)](/frameworks/alf/overview) - for audit logging and exceptions.
* The digital resource connector(s) used to gain access to the digital resource being analysed.

=== "Gradle dependencies"
    ```groovy
    dependencies {
        compileOnly 'org.odpi.egeria:audit-log-framework'
        compileOnly 'org.odpi.egeria:open-connector-framework'
        compileOnly 'org.odpi.egeria:open-metadata-framework'
        compileOnly 'org.odpi.egeria:open-governance-framework'
        compileOnly 'org.odpi.egeria:open-survey-framework'
        compileOnly '...digital resource connector...'
    }
    ```
=== "Maven dependencies"
    ```xml
        <dependencies>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>audit-log-framework</artifactId>
                <scope>provided</scope>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-connector-framework</artifactId>
                <scope>provided</scope>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-metadata-framework</artifactId>
                <scope>provided</scope>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-governance-framework</artifactId>
                <scope>provided</scope>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-survey-framework</artifactId>
                <scope>provided</scope>
            </dependency>

            <dependency>
                  :
               Digital resource connectors need to be included
                  :
            </dependency>

        </dependencies>
    ```

!!! tip "Use provided scope"
    Notice the `<scope>provided</scope>` setting (`compileOnly` in Gradle).  This keeps the Egeria libraries out of your connector's jar file, so your connector can run with any level of Egeria that supports this type of connector.  Without it, duplicate Egeria classes are loaded into the OMAG Server Platform and it is not certain which version runs.

## Connector provider for a survey action service

Each connector provider for a survey action service extends [`SurveyActionServiceProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/SurveyActionServiceProvider.java){ target=gh }, which in turn extends `GovernanceServiceProviderBase` and `OpenConnectorProviderBase`.

This assumes the survey action service implementation class is instantiated with the default constructor, so all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method, plus the request parameters and action targets supplied when it is run.

The descriptive information about the connector is supplied through an implementation of the [`OpenConnectorDefinition` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/OpenConnectorDefinition.java){ target=gh } interface - the connector type GUID, qualified name, display name, description, wiki page, audit log component identifier and development status.  Defining these as an enum keeps the descriptions of all the connectors in your library together.  Egeria's own connectors use the `EgeriaOpenConnectorDefinition` enum for this.

The constructor then declares what this particular survey does.  This is the *specification* that a tool uses to offer the survey to a user and to validate how it is being called:

| Field | Description |
|---|---|
| `supportedActionTargetTypes` | The elements the survey expects to be given, each with a name, description, open metadata type and [deployed implementation type](/concepts/deployed-implementation-type). |
| `supportedAnalysisSteps` | The [analysis steps](#analysis-steps) this survey performs, so a caller can ask it to stop early. |
| `producedAnnotationTypes` | The [annotation](/concepts/survey-report/#annotations) types this survey can produce, with their descriptions, so a consumer knows what to expect in the survey report. |
| `supportedTechnologyTypes` | The technologies this survey knows how to analyse. |
| `supportedRequestTypes` / `supportedRequestParameters` | The request types and request parameters that change its behaviour. |
| `producedGuards` | The [guards](/concepts/guard) it can return. |
| `supportedConfigurationProperties` | Full descriptions of any configuration properties on its connection. |

The `SurveyActionServiceProvider` constructor already sets `supportedRequestParameters`, `producedGuards` and `producedActionTargetTypes` to the OSF standard values, so you only override the ones your service changes.

Here is the complete connector provider for the [File Survey Action Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/file-survey-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/surveyaction/surveyfile/FileSurveyServiceProvider.java){ target=gh }:

```java
public class FileSurveyServiceProvider extends SurveyActionServiceProvider
{
    private static final String connectorClass = "org.odpi.openmetadata.adapters.connectors.surveyaction.surveyfile.FileSurveyService";

    static final String FILE_TARGET_PROPERTY             = "fileToSurvey";
    static final String FILE_TARGET_PROPERTY_DESCRIPTION = "The DataFile asset that describes the physical file to survey.";

    public FileSurveyServiceProvider()
    {
        super(EgeriaOpenConnectorDefinition.FILE_SURVEY_SERVICE,
              connectorClass,
              null);

        supportedActionTargetTypes = new ArrayList<>();

        ActionTargetType actionTargetType = new ActionTargetType();

        actionTargetType.setName(FILE_TARGET_PROPERTY);
        actionTargetType.setDescription(FILE_TARGET_PROPERTY_DESCRIPTION);
        actionTargetType.setOpenMetadataTypeName(DeployedImplementationType.FILE.getAssociatedTypeName());
        actionTargetType.setDeployedImplementationType(DeployedImplementationType.FILE.getDeployedImplementationType());

        super.supportedActionTargetTypes.add(actionTargetType);

        super.supportedAnalysisSteps  = AnalysisStep.getAnalysisStepTypes(new AnalysisStep[] {
                                            AnalysisStep.CHECK_ASSET, AnalysisStep.MEASURE_RESOURCE});
        super.producedAnnotationTypes = SurveyFileAnnotationType.getFileSurveyAnnotationTypeTypes();
        super.supportedTechnologyTypes = SupportedTechnologyType.getSupportedTechnologyTypes(
                                            new DeployedImplementationTypeDefinition[]{DeployedImplementationType.DATA_FILE});
    }
}
```

## Survey action service implementation

The survey action service implementation inherits from [`SurveyActionServiceConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/SurveyActionServiceConnector.java){ target=gh }.

This base class handles the survey context, any nested connectors and the audit log.  The following variables are set up:

* `surveyActionServiceName` - the qualified name of the survey action service from the open metadata definition.  Use it in audit log messages and exceptions.
* `surveyContext` - the [survey context](#survey-context) that provides methods for querying and storing survey metadata.
* `auditLog` - audit logging destination.
* `connector` - a slot for the [digital resource connector](/concepts/digital-resource-connector) used to read the resource; the base class disconnects it for you.
* `embeddedConnectors` - connectors created from connections nested in the survey action service connection.  These are typically survey action services that are embedded because this survey action service is a [survey action pipeline](#survey-action-pipelines).
* `propertyHelper` - utility for reading values out of open metadata elements.

There are two methods that you need to implement:

* `start()` - this method is where all the work takes place. It retrieves any configuration properties from the connection, uses the survey context to access the asset and its [connector to the digital resource](/concepts/digital-resource-connector).  As it analyses the content of the digital resource, it adds its results to the annotation store retrieved from the survey context.  The annotations are immediately stored in one of the open metadata repositories.  Always call `super.start()` first - it validates that the survey context has been set up.

* `disconnect()` - this method is called either because the survey action service has completed running, or because its server is shutting down.  The survey action service implementation should release any resources it is using - for example by calling the disconnect method on the digital resource connector it is using.

Here is the complete implementation of the [File Survey Action Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/file-survey-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/surveyaction/surveyfile/FileSurveyService.java){ target=gh }:

```java
public class FileSurveyService extends SurveyActionServiceConnector
{
    @Override
    public void start() throws ConnectorCheckedException, UserNotAuthorizedException
    {
        final String methodName = "start";

        super.start();

        try
        {
            AnnotationStore annotationStore = surveyContext.getAnnotationStore();

            /*
             * The asset should have a special connector for files.  If the connector is wrong,
             * the cast will fail.
             */
            connector = performCheckAssetAnalysisStep(BasicFileStore.class, OpenMetadataType.DATA_FILE.typeName);
            BasicFileStore assetConnector = (BasicFileStore)connector;

            File file = assetConnector.getFile();

            annotationStore.setAnalysisStep(AnalysisStep.MEASURE_RESOURCE.getName());

            FileStatsExtractor fileStatsExtractor = new FileStatsExtractor(file,
                                                                           surveyContext.getFileClassifier(null, null, null),
                                                                           this);

            AnnotationProperties measurementAnnotation = fileStatsExtractor.getAnnotation();

            if (measurementAnnotation != null)
            {
                annotationStore.addAnnotation(measurementAnnotation, surveyContext.getAssetGUID());
            }
        }
        catch (ConnectorCheckedException error)
        {
            throw error;
        }
        catch (Exception error)
        {
            super.handleUnexpectedException(methodName, error);
        }
    }


    @Override
    public void disconnect() throws ConnectorCheckedException
    {
        if (connector != null)
        {
            connector.disconnect();
        }

        super.disconnect();
    }
}
```

### Helper methods on the base class

`SurveyActionServiceConnector` supplies methods that keep all survey action services behaving consistently:

* `performCheckAssetAnalysisStep(expectedConnectorClass, expectedAssetType)` records the *Check Asset* analysis step, validates that the action target is the expected open metadata type, creates the resource connector from the asset's connection and checks that it is the class the survey needs.  There is also an overload that takes just the expected asset type name.  Failures produce standard error messages rather than a raw `ClassCastException`.
* `handleUnexpectedException(methodName, error)` wraps an unexpected exception in a `ConnectorCheckedException` with a standard message.
* `getRootSchemaType(assetElement)` and `throwMissingSchemaType(assetGUID)` help surveys that need the asset's schema.
* `writePropertyListInventory()`, `writeNameListInventory()`, `writeNameCountInventory()` and `writeNameDescriptionInventory()` write an inventory to a CSV file and return the *Resource Profile Log* annotation that points to it.  Use these when the results are too large to store directly in open metadata.
* `getJSONProperties(properties)` converts a properties object to a JSON string, for annotations that carry structured payloads.
* `setUpAnnotation(annotation, annotationType)` fills in the standard fields of an annotation from its [annotation type](#annotation-types) definition.

### Analysis steps

A survey is divided into named *analysis steps* - `Check Asset`, `Measure Resource`, `Schema Extraction`, `Profile Data`, `Produce Inventory`, `Schema Validation`, `Data Validation` and others, defined by the [`AnalysisStep` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/controls/AnalysisStep.java){ target=gh } enum.

Call `annotationStore.setAnalysisStep(...)` as your service moves from one step to the next.  Every annotation created after that call is tagged with the step, which lets a consumer of the survey report understand where each finding came from, and lets a caller use the `finalAnalysisStep` request parameter to ask for a cheaper, partial survey.  Declare the steps your service supports in `supportedAnalysisSteps` on the connector provider.

### Annotation types

Rather than building annotations ad hoc, define the annotations your survey produces as an enum of *annotation types* - name, description, the open metadata annotation type it maps to, the analysis step that produces it, and the metrics it carries.  Egeria's own definitions are in [`SurveyFileAnnotationType`, `SurveyFolderAnnotationType`, `SurveyDatabaseAnnotationType` and `SurveyResourceManagerAnnotationType` :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/controls){ target=gh }.

The `measurements` package of the OSF provides ready-made metric definitions for files, directories, and relational databases, schemas, tables and columns - use these where they fit, so that measurements taken by different surveys can be compared.

## Survey Context

The survey context provides the *survey action service* with access to information about the survey request along with the open metadata repository interfaces.

![Structure of the survey context](/frameworks/osf/survey-context.svg)

`SurveyContext` extends `ConnectorContextBase` - the same base class used by the [integration context](/guides/developer/integration-connectors/integration-context) and the [governance action context](/guides/developer/governance-action-services/overview).  This means a survey action service has the full set of open metadata clients available to it (`getAssetClient()`, `getSchemaTypeClient()`, `getGlossaryTermClient()`, `getOpenMetadataStore()` and the rest), plus the file classifier, the name-case converters, and the ability to raise [To Dos](/concepts/to-do), [incident reports](/concepts/incident-report) and context events.

On top of that, it adds the survey-specific methods:

| Method | Purpose |
|---|---|
| `getAssetGUID()` | The unique identifier of the asset being surveyed. |
| `getAssetStore()` | The [survey asset store](#survey-asset-store). |
| `getAnnotationStore()` | The [annotation store](#annotation-store). |
| `getRequestParameters()` | The name-value properties supplied when the survey was requested. |
| `getActionTargetElements()` | Any additional elements the survey was given to work with. |
| `getRequesterUserId()` | Who asked for the survey. |
| `elementShouldBeSurveyed(name, excluded, included)` | Applies the standard include/exclude list semantics, so all surveys filter consistently. |
| `recordCompletionStatus(...)` | Declares that the survey has finished - see [completion](#completing-the-survey). |

### Annotation Store

The survey annotation store provides a survey action service with access to the [annotations](/concepts/survey-report/#annotations) created about a specific asset both from past invocations of survey action services and those created during the current execution.

The survey report itself is created for you when the service starts; the annotation store writes into it.  Its methods are:

* `addAnnotation(annotationProperties, elementGUID)` - store an annotation and link it to the element it describes.  Annotations are stored immediately, so a long-running survey's findings can be read before it completes.
* `addAnnotationExtension(parentAnnotationGUID, ...)` - add an annotation that elaborates on another one.
* `updateAnnotation()` / `deleteAnnotation()` / `getAnnotation()`.
* `getAnnotationsForElement()`, `getNewAnnotations()`, `getExtendedAnnotations()` - retrieve what is already there, including annotations from earlier surveys.
* `linkRequestForActionTarget()` - point a *Request for Action* annotation at the element that needs attention.
* `setAnalysisStep()` - see [analysis steps](#analysis-steps).
* `setReportQualifiedName()`, `setReportDisplayName()`, `setSurveyDescription()`, `setSurveyPurpose()`, `setCompletionMessage()` - describe the report for the people who will read it.

### Survey Asset Store

The survey asset store gives access to the asset being surveyed and to the digital resource behind it:

* `getAssetGUID()`, `getAssetProperties()`, `getQualifiedName()` - the open metadata describing the resource.
* `getConnectorToAsset()` - create a [digital resource connector](/concepts/digital-resource-connector) from the asset's connection.  In most services this is reached indirectly through `performCheckAssetAnalysisStep()`.
* `getConnectorByConnection(connection)` - create a connector from a connection the survey has located itself.
* `addCSVFileToCatalog(...)` - catalog a CSV file that the survey has produced, such as an inventory log.

### Open Metadata Store

Provides access to all types of open metadata through the [Open Metadata Framework (OMF)](/frameworks/omf/overview), via `getOpenMetadataStore()` and the typed clients described above.

## Completing the survey

A survey action service runs as an [engine action](/concepts/engine-action), so it finishes by recording a completion status and one or more [guards](/concepts/guard):

```java
        surveyContext.recordCompletionStatus(SurveyActionGuard.SURVEY_COMPLETED.getCompletionStatus(),
                                             List.of(SurveyActionGuard.SURVEY_COMPLETED.getName()),
                                             null,
                                             null,
                                             completionMessage);
```

The OSF defines the standard guards in [`SurveyActionGuard` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/controls/SurveyActionGuard.java){ target=gh }.  Each carries the completion status that normally goes with it, so the two cannot drift apart:

| Guard | Completion status | Meaning |
|---|---|---|
| `survey-completed` | ACTIONED | The survey completed successfully.  The survey report is attached to the asset. |
| `survey-invalid` | INVALID | The survey did not run because the supplied information (such as the asset) is invalid for this type of survey. |
| `survey-failed` | FAILED | An unexpected error occurred during the survey process.  The survey report is incomplete. |
| `data-certified` / `data-not-certified` | ACTIONED | Used by surveys that run quality checks and certify the data. |
| `missing-certification-type` / `missing-schema-type` | INVALID | The information needed to validate the data was not supplied. |

A service that does not call `recordCompletionStatus()` is treated as having completed successfully when `start()` returns.  Declaring the status explicitly is better, because the guards are what a [governance action process](/concepts/governance-action-process) uses to decide what runs next.

## Survey action pipelines

A *survey action pipeline* is a survey action service that runs other survey action services.  Extend [`SurveyActionPipelineConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/SurveyActionPipelineConnector.java){ target=gh } and implement `runSurveyPipeline()`.  The nested services are supplied as embedded connections in the pipeline's [virtual connection](/concepts/connection/#virtual-connections), and the base class turns them into `SurveyActionServiceConnector` instances for you.

The OSF ships [`SequentialSurveyPipeline` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey/SequentialSurveyPipeline.java){ target=gh }, which runs each embedded survey in turn against the same survey context, so all of their annotations land in one survey report.

## Deploying and running your survey action service

Package your connector provider and implementation in a jar file, and add it (with any third party client libraries it needs) to the [OMAG Server Platform](/concepts/omag-server-platform) class path - the easiest way is to copy the jar files into the `extra` directory of the platform's [assembly](/education/tutorials/building-egeria-tutorial/overview).

Survey action services are then grouped into [survey action engines](/concepts/survey-action-engine), which map a [governance request type](/concepts/governance-request-type) to the survey action service that should run.  These definitions are created as part of a [governance engine pack](/guides/developer/open-metadata-archives/creating-governance-engine-packs) or through the [Asset Maker](/services/omvs/asset-maker/overview) API, and are stored in the open metadata repositories.

Survey action engines are hosted by the [Survey Action OMES](/services/omes/survey-action/overview) running in an [engine host](/concepts/engine-host).  See [configuring the engine services in the engine host](/guides/admin/servers/by-section/engine-host-services-section) in the administration guide.

## Example implementations

The definition of the connector interfaces for survey action services is in the [open-survey-framework :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/open-survey-framework/src/main/java/org/odpi/openmetadata/frameworks/opensurvey){ target=gh } module.

Implementations of survey action services are listed on the [survey action service concept page](/concepts/survey-action-service) and include:

* [file-survey-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/file-survey-connectors){ target=gh } - surveys of a file, a CSV file and a directory (folder).
* [Apache Kafka server survey :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/apachekafka/survey){ target=gh } and [Apache Atlas survey :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/apacheatlas/survey){ target=gh } - surveys of a running server.
* [Unity Catalog surveys :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/unity-catalog-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/unitycatalog/survey){ target=gh } - surveys at each level of a catalog hierarchy.

??? education "Further information"
    - [Open Survey Framework (OSF)](/frameworks/osf/overview) - annotation types, survey report structure and the types of analysis a survey performs.
    - [Writing a governance action service](/guides/developer/governance-action-services/overview) - for acting on what a survey finds.
    - [Survey report](/concepts/survey-report) - what a survey produces.

---8<-- "snippets/abbr.md"
