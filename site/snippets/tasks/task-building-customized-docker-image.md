<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Building a customized docker image

The top-level directory of the Egeria omag-server-platform assembly contains the following files:

```bash
$ ls
Dockerfile      LICENSE         NOTICE          README.md       assembly      dist
```

The `Dockerfile` contains the properties for building a docker image of all the files under `assembly/platform`.

Once you have the contents of `assembly/platform` as you want them, run the docker command:

```bash
docker build -t egeria-platform:{myversion} -f Dockerfile .
```
replacing `{myversion}` with a tag name for this docker image.  The example below used `latest` as the tag name.

```bash
? docker build -t egeria-platform:latest -f Dockerfile .
[+] Building 44.9s (5/5) FINISHED                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                 0.0s
 => => transferring dockerfile: 3.28kB                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                      0.0s
 => [internal] load metadata for registry.access.redhat.com/ubi9/openjdk-17:latest                                                                   1.5s
 => [1/1] FROM registry.access.redhat.com/ubi9/openjdk-17@sha256:3eded7b50a5ff8a55895c7b70c9dfc6e320363e5812a68747f281f8f4bb323ac                   43.3s
 => => resolve registry.access.redhat.com/ubi9/openjdk-17@sha256:3eded7b50a5ff8a55895c7b70c9dfc6e320363e5812a68747f281f8f4bb323ac                    0.0s
 => => sha256:5cbda490fcb7ab72e85cfba7098858cd3ed6bb15f95687e86979f6d4ac7b2f15 596B / 596B                                                           0.0s
 => => sha256:5b5deb1288720666a590472d9a506500df9ebe3c817e9710327162ccd24c4e22 24.19kB / 24.19kB                                                     0.0s
 => => sha256:62742f27dce5ebff467a57ad6bfa680820f3bc534cc313627f8113246276bf0f 37.83MB / 37.83MB                                                    17.9s
 => => sha256:f008a4f4b21c818e8bbd4e2521eb30ab0f8a43dc259e9e51c0d134641e343acd 110.80MB / 110.80MB                                                  37.5s
 => => sha256:3eded7b50a5ff8a55895c7b70c9dfc6e320363e5812a68747f281f8f4bb323ac 1.47kB / 1.47kB                                                       0.0s
 => => extracting sha256:62742f27dce5ebff467a57ad6bfa680820f3bc534cc313627f8113246276bf0f                                                            2.0s
 => => extracting sha256:f008a4f4b21c818e8bbd4e2521eb30ab0f8a43dc259e9e51c0d134641e343acd                                                            5.5s
 => exporting to image                                                                                                                               0.0s
 => => exporting layers                                                                                                                              0.0s
 => => writing image sha256:5a2c784ed7558dc625d109c04c8b5e78534b270a29d3011eb771fd01724c097f                                                         0.0s
 => => naming to docker.io/library/egeria-platform:latest                                                                                            0.0s

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview
```

The resulting docker image is published to the docker service configured on your local machine.



