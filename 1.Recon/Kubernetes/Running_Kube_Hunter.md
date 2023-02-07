# Running Kube Hunter

**Description:** Kube-Hunter is a tool used to scan Kubernetes cluster for security weaknesses

**Requirements:** docker

## Scanning a remote Kuberntes cluster

```
docker run -it --rm --network host aquasec/kube-hunter --remote <kubernetes_cluster>
```

Running a scan on a remote Kubernetes cluster

## Scanning your local Docker desktop Kubernetes cluster

```
docker run -it --rm --network host aquasec/kube-hunter --interface
```

Run a scan on network interfaces (easier for local Kubernetes scans)

## References
* https://github.com/aquasecurity/kube-hunter