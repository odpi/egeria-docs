<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2022. -->

# Useful Kubernetes commands

This page gives a few example of useful commands. 

!!! cli "List running pods"
```console
kubectl get pods
```

!!! cli "list active services"
```console
kubectl get pods
```

!!! cli "list all active resources"
```console
kubectl get all
```

!!! cli "Get more details on a pod"
```console
kubectl describe pods <pod-id>
```

!!! cli "get logs from a pod"
```console
kubectl logs <pod-id>
```

!!! cli "kill a pod"
```console
kubectl delete pod <pod-id>
```

!!! cli "setup port forwarding for a pod"
```console
kubectl port-forward pod/<pod-id> <local-port>:<remote-port>
```

!!! cli "setup port forwarding for a service"
```console
kubectl port-forward service/<pod-id> <local-port>:<remote-port>
```


---8<-- "snippets/abbr.md"
