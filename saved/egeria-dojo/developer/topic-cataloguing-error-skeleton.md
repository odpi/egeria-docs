<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Add ` implements ExceptionMessageSet` after `public class TopicCataloguingErrorCode`.

Paste this code between the curly braces of the `TopicCataloguingErrorCode` class.

```java linenums="1"
    UNEXPECTED_EXCEPTION(500, "TOPIC-LOGGING-CONNECTOR-500-001",
             "The {0} integration connector received an unexpected exception {1} when cataloguing topics; the error message was: {2}",
             "The connector is unable to catalog one or more topics.",
             "Use the details from the error message to determine the cause of the error and retry the request once it is resolved."),
    ;


    private ExceptionMessageDefinition messageDefinition;


    /**
     * The constructor for TopicCataloguingErrorCode expects to be passed one of the enumeration rows defined in
     * TopicCataloguingErrorCode above.   For example:
     *
     *     TopicCataloguingErrorCode   errorCode = TopicCataloguingErrorCode.ERROR_SENDING_EVENT;
     *
     * This will expand out to the 5 parameters shown below.
     *
     *
     * @param httpErrorCode   error code to use over REST calls
     * @param errorMessageId   unique Id for the message
     * @param errorMessage   text for the message
     * @param systemAction   description of the action taken by the system when the error condition happened
     * @param userAction   instructions for resolving the error
     */
    TopicCataloguingErrorCode(int  httpErrorCode, String errorMessageId, String errorMessage, String systemAction, String userAction)
    {
        this.messageDefinition = new ExceptionMessageDefinition(httpErrorCode,
                                                                errorMessageId,
                                                                errorMessage,
                                                                systemAction,
                                                                userAction);
    }


    /**
     * Retrieve a message definition object for an exception.  This method is used when there are no message inserts.
     *
     * @return message definition object.
     */
    @Override
    public ExceptionMessageDefinition getMessageDefinition()
    {
        return messageDefinition;
    }


    /**
     * Retrieve a message definition object for an exception.  This method is used when there are values to be inserted into the message.
     *
     * @param params array of parameters (all strings).  They are inserted into the message according to the numbering in the message text.
     * @return message definition object.
     */
    @Override
    public ExceptionMessageDefinition getMessageDefinition(String... params)
    {
        messageDefinition.setMessageParameters(params);

        return messageDefinition;
    }


    /**
     * JSON-style toString
     *
     * @return string of property names and values for this enum
     */
    @Override
    public String toString()
    {
        return "TopicCataloguingErrorCode{" +
                       "messageDefinition=" + messageDefinition +
                       '}';
    }
```
The error code for an exception is similar to the audit log message definition since there is a unique message identifier, message, a system action and user response.  Instead of a severity there is a code that follows the conventions used in the HTTP code.  This indicates the severity of the situation.  
