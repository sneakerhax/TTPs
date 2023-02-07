# Discovering Docker registry api

**Description:** This entry describes how to perform recon to discovery the Docker registry API

**Requirements:** curl

## Common Docker registry api ports

* 5000
* 5001

## Discovering the Docker registry API

```
curl -Ik <host>:<port>/v2/_catalog
```

Use curl to display the hosted images

## Pulling down image manifest to discovery secrets

```
curl http://192.168.4.35:1235/v2/<user>/<image>/manifests/latest | grep --color -i <search_term>
```

curl the image manifest and search for secrets.

  
## References
* [Docker Registry Engine API Reference](https://docs.docker.com/registry/spec/api/)