# Kubernetes

## Remote

```
kubectl cluster-info
```

Get cluster info

```
kubectl <command> --kubeconfig ~/.kube/config
```

Using a kubeconfig file to access a remote API and run commands

```
kubectl --token=<bearer_token> --server https://kubernetes.site.com:<port> <command>
```

Using kubectl and bearer token (JWT) with specified server api to run commands

```
curl -kv -H "Authorization: Bearer <bearer_token>" https://kubernetes.site.com:<port>/api/v1/namespaces
```

Access Kubernetes API with bearer token (JWT)

```
curl https://kubernetes.site.com:<port>/api
```

Check for the existance of the kubernetes api secure port

*Other relevant [ports](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire) for interacting with kubernetes*

```
curl -k https://kubernetes.site.com:<port>/version
```

Get api version

```
kubectl get --raw='/readyz?verbose'
```

Health check the API server

## Run

```
kubectl run <name> --image alpine
```

Deploy a single pod

## Create

```
kubectl create deployment <deployment_name> --image=<image_name>
```

Create deployment

```
kubectl create deployment <name> --image=alpine --replicas 3 -- ping 1.1.1.1
```

Create deployment with 3 replica pods and override the default command to run ping

```
kubectl create deployment <name> --image=nginx -o yaml --dry-run=client
```

Check deployment but don't spin up any resources. This will create a yaml file for deployment

## Apply

```
kubectl apply -f <file_name>.yml --dry-run
```

Shows output for the deployment without actually running

```
kubectl apply -f <file_name>.yml --server-dry-run
```

Shows output for deployment by checking API (If deployment exists it will list changes)

## Diff

```
kubectl diff -f <file_name>.yml
```

Compare differences between current deployment and yml deployment

## Scale

```
kubectl scale deployment/<deployment_name> --replicas 5
```

Scaling to 5 replicas

## Expose

```
kubectl expose deployment/<deployment_name> --port 8080
```

Expose port inside Kubenetes cluster

```
kubectl expose deployment/<deployment_name> --port 8080 --name <name> --type NodePort
```

Expose port outside cluster (Used for Docker Desktop)

## Get

```
kubectl get all
```

List all Kubernetes services and resources (Current namespace)

```
kubectl get services
```

List deployed services

```
kubectl get namespaces
```

List namespaces in your curent context

```
kubectl get all --all-namespaces
```

List all namespaces

```
kubectl get pods --all-namespaces
```

List all pods in all namespaces

```
kubectl get pods -n <namespace>
```

Get all pods in a namespace

```
kubectl get deployment <deployment> -o yaml
```

Get yaml output for deployment (Also works with service, pod, secret)

## Describe

```
kubectl describe node <node_name>
```

Detailed information about a node

## Exec

```
kubectl exec -it <pod_name> -- /bin/bash
```

Drop into interactive bash shell inside pod

```
kubectl exec <pod_name> -- <command>
```

Execute single command inside pod

## Explain

```
kubectl explain services.spec
```

List information about services.spec (yaml spec)

```
kubectl explain <type>
```

Explain a resource type (e.g. node)

## Logs

```
kubectl logs <name> --tail=10
```

Get last 10 logs from pod

```
kubectl logs <name> --tail 1 --follow
```

Follow logs

## Delete

```
kubectl delete deployment <deployment_name>
```

Delete deployment
