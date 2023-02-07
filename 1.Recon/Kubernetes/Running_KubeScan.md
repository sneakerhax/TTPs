# Running KubeScan

**Description:** KubeScan is a tool used to scan Kubernetes cluster for risky RBAC configurations

**Requirements:** docker

## Scanning using Kubernetes configuration file

```
docker run -it --rm -e CONF_PATH=/config -v ~/.kube:/tmp cyberark/kubiscan
```

Starting the container and mounting a volume with the Kubernetes cluster config file only

```bash
root@45366b596c8d:/#kubescan -a
```

Check for all risky roles

## References
* https://github.com/cyberark/KubiScan