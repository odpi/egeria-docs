<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Programming Languages

## Java

Egeria's runtime and clients are written in Java.

Java is a strongly-typed, compiled language. The resulting object code runs in a virtual machine called the *Java Virtual Machine* (JVM).

The JVM is supported on most operating systems and so Java programs can run with the same behavior on almost any machine. This portability of code is why Java is used for the Egeria runtime (the [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform)) and the clients.

If you want to run Egeria you need to install the *Java Runtime Environment* (JRE). To build and test Egeria, you need the *Java Development Kit* (JDK) installed. The JDK also contains the runtime environment (JRE).

There are various JDK's available, and you may even have one pre-installed on your system.

!!! cli "Check for a pre-installed Java"
    ```shell
    java -version
    ```

Egeria requires Java 11 as a minimum level. Language constructs up to Java 11 are permitted, but not above. We use the [Adoptium (formerly AdoptOpenJDK) :material-dock-window:](https://adoptopenjdk.net){ target=jdk } distribution. Official images and maven artifacts are built with this level. Additionally, code must compile and run on the current latest Java release. This is validated before any code can be merged.

Java can be installed by:

1. Downloading the *OpenJDK 11 (LTS) HotSpot* JVM from [Adoptium :material-dock-window:](https://adoptopenjdk.net){ target=jdk }.
2. Running the installer that is downloaded.

Alternatively, JDK's may be found on your operating system install repositories or via third party tools like [HomeBrew :material-dock-window:](https://brew.sh) on MacOS.

Also, you must ensure `JAVA_HOME` is set, and pointing to a JDK. If this is not done, an error such as `Failed to execute goal org.apache.maven.plugins:maven-javadoc-plugin:3.1.1:jar (attach-javadocs) on project open-connector-framework: MavenReportException: Error while generating Javadoc: Unable to find javadoc command: The environment variable JAVA_HOME is not correctly set.` will be seen as the Javadoc Maven plugin depends on this value to work correctly.

## Python

Python is an interpreted programming language. It is favored by data scientists and script writers because it supports writing in snippets where variables can be created on the fly and are typically global.

Python is used in much of the educational material.
For example, Egeria uses Python in the [hands-on labs](/egeria-docs/education/open-metadata-labs) since it is the native language of the [Jupyter Notebooks](/egeria-docs/education/tutorials/jupyter-tutorial/overview) environment we use for the labs.



## Markdown

Markdown is a simple tagging language that generates HTML webpages. We use it for documentation (this page is written in Markdown for example), in GitHub comments and in the [Jupyter Notebooks](/egeria-docs/education/tutorials/jupyter-tutorial/overview) that form the teaching material for the [hand-on labs](/egeria-docs/education/open-metadata-labs).

GitHub provides [a useful summary for Markdown :material-dock-window:](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf){ target=gh } and our own [documentation guide](/egeria-docs/guides/documentation/guide) provides Egeria-specific formatting and stylistic pointers, as well as further information on the system we use to translate such `.md` files into the website you are currently reading.

--8<-- "snippets/abbr.md"
