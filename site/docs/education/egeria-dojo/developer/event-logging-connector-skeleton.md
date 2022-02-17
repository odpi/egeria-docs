<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Add ` extends OMRSAuditLogStoreConnectorBase` after `public class EventLoggingConnector`.  This base class provides some useful methods such as `super.validateLogRecord()`.

Paste this code between the curly braces of the `EventLoggingConnector` class.  You can see that the code is very short - no need for a `main` method because that is provided by Egeria's OMAG Server Platform where it runs.

```java linenums="1"

    /**
     * Default constructor used by the connector provider.
     */
    public EventLoggingConnector()
    {
    }


    /**
     * Store the audit log record in the audit log store.
     *
     * @param logRecord  log record to store
     * @return unique identifier assigned to the log record
     * @throws InvalidParameterException indicates that the logRecord parameter is invalid.
     */
    @Override
    public String storeLogRecord(OMRSAuditLogRecord logRecord) throws InvalidParameterException
    {
        final String methodName = "storeLogRecord";

        super.validateLogRecord(logRecord, methodName);

        if (OMRSAuditLogRecordSeverity.EVENT.getName().equals(logRecord.getSeverity()))
        {
            if (logRecord.getAdditionalInformation() != null)
            {
                System.out.println(logRecord.getTimeStamp() + " " + logRecord.getOriginator().getServerName() + " " + logRecord.getSeverity() + " " + logRecord.getMessageId() + " " + logRecord.getMessageText() + "\n   Event Payload: " + logRecord.getAdditionalInformation());
            }
            else
            {
                System.out.println(logRecord.getTimeStamp() + " " + logRecord.getOriginator().getServerName() + " " + logRecord.getSeverity() + " " + logRecord.getMessageId() + " " + logRecord.getMessageText());
            }
        }

        return logRecord.getGUID();
    }

```
The `storeLogRecord` method is called each time an audit log message is logged by any component running in the OMAG Server Platform.
