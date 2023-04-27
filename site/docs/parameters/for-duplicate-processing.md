<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The `forDuplicateProcessing` boolean parameter indicates whether the caller is part of the deduplication governance function or not.  Most callers set `forDuplicateProcessing` to `false`.  When it is true, all the automated merging of identified duplicate elements is skipped and the elements are returned as stored.  This allows the deduplication function to set up the relationships and classifications that control the deduplication process.


