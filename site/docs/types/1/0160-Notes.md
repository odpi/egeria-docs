<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0160 Note Logs

[*Notifications*](/types/1/0135-Actions-For-People) provide additional information about a [Referenceable](/types/0/0010-Base-Model/#referenceable) object. They are used by resource owners and stewards to document the current status of their resources. Engines that are performing processing on the resources may also write notifications to the note log. The note log can be attached to any referenceable metadata object.

![UML](0160-Notes.svg)

## NoteLog entity

A *NoteLog* entity provides a collection point for actions about a particular subject or element.

## AttachedNoteLog relationship

The *AttachedNoteLog* connects a note log to one or more elements that are described in the note log's entries. A referenceable object can have many note logs linked off of it.  If the note log is linked to only one referenceable, it may also be anchored to the referenceable so it is deleted with the referenceable.

## AttachedNoteLogEntry relationship

The *AttachedNoteLogEntry* connects a note log to an [Action](/types/0/0013-Actions) (typically a [Notification](/types/1/0135-Actions-For-People)). A note log can have many actions linked off of it. These actions may, or may not be anchored to the note log.

--8<-- "snippets/abbr.md"
