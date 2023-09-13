<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

=== "Supported Platforms - linux, macOS"

    Egeria currently supports building on *nix, Linux & Linux-like operating systems such as MacOS.
     
    Our official build pipelines are based on x86_64 architecture, but it is expected the build will run on other architectures, subject to the availability of the required tools and interpreters/jvms/runtimes on that platform (for example Java, Python, Docker/containerd/k8s etc).

=== "Additional Platforms - Windows"

    Currently, the Egeria team does not regularly test or use Windows, so there may be areas that are not documented as well, or not work. We would welcome any interested developers who use Windows on a daily basis to join us and help improve this area!

    On Windows, you should use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) Version 2 or above, and install a Linux distribution such as Ubuntu. This avoids issues we have seen with path separators, symbolic links, slow I/O performance, long path names. WSL version 2 should be used, not version 1, due to differences in file I/O (emulation). The docs above explain how to switch from v1 to v2.
     
    From the command line everything should work just as for macOS & linux, including building and running Egeria since a full linux distribution is being used, with a linux kernel.

    However, IDE use may be a little different. Some IDEs can run the GUI in Windows natively, and then use the WSL environment to perform build and execution.

    With IntelliJ the following process is most likely to work:

     * Ensure an Ubuntu environment is setup using WSL2
     * Install a java sdk, and maven as for mac/linux
     * ensure a build at the command line works ok 
     * Install IntelliJ community edition on Windows. Using the latest version (2022.1 at time of writing) is recommended as WSL support is a new area
     * Create a new project 'from existing sources' and ensure you point to //wsl$/..... (path in linux environment)
     * After a few warnings as IntelliJ detects the code, your SDK should be set automatically to the linux java version 

    Jetbrains have a [WSL2 support article](https://www.jetbrains.com/help/idea/how-to-use-wsl-development-environment-in-product.html){ target=jb } which elaborates these instructions in more detail

    Another option would be to run the IDE itself directly within the linux environment, and share the display via X11, VNC, or another form of remote desktop.  This is likely to work, but could perform sluggishly. Microsoft are improving this area with [WSLg](https://www.google.com/search?client=safari&rls=en&q=wslg&ie=UTF-8&oe=UTF-8){ target=gh } , but this requires very new software, and dedicated graphics to work well. It's also outside the scope of this summary.

    Egeria provides both maven and gradle build scripts. On Windows we've seen issues with maven which can cause IntelliJ to be busy or unresponsive for hours. If this happens you could try to use the gradle build instead. To do this in IntelliJ:

     * Navigate to your maven tool window,click the top level maven project 'Egeria' & 'Unlink Maven Projects' - and confirm.
     * In the left project tree right-click on the top level build.gradle and 'Link gradle project' 

    Yet another option to use IntelliJ is to make use of [Remote Development](https://www.jetbrains.com/remote-development/){ target=jb }. With this configuration you would use a seperate linux system, and connect remotely. This is beyond the scope of these docs.

    Feedback on Windows, offers to help, clarification on the steps can be directed to [odpi/egeria-docs#335](https://github.com/odpi/egeria-docs/issues/335){ target=gh }
