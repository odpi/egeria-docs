/* SPDX-License-Identifier: CC-BY-4.0 */
/* Copyright Contributors to the Egeria project. */

/**
 * redirects to the same location but https protocol if the host is egeria-project.org
 */
if (location.host === 'egeria-project.org' && location.protocol !== 'https:') {
    location.replace(`https:${location.href.substring(location.protocol.length)}`);
}