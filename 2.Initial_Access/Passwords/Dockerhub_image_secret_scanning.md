# Dockerhub image secret scanning

**Description:** This entry describes how to scan an organizations Docker hub images for secrets

**Requirements:** curl, deepfence, docker

## Pulling and secret scanning an organizations image secrets

```
curl -s "https://hub.docker.com/v2/repositories/<org_name>/?page_size=100" | jq -r '.results|.[]|.name'
```

Pull a list of public images for an organization from Docker hub

```
docker run -it --rm --name=deepfence-secretscanner -v /Users/sneakerhax/RedTeam/Adobe/Scans/DockerHub:/home/deepfence/output -v /var/run/docker.sock:/var/run/docker.sock deepfenceio/secretscanner -image-name <image_name>
```

Running secret scanning

```
docker history <image_name>
```

View build layer steps

```
docker save <image_name>
```

Dump image layers

```
tar -tvf <image_tar_file>
```

View file contents of tar file

```
tar -xvf <image_tar_file>
```

Untar image tar file to view contents
  
## References
* [Github - SecretScanner](https://github.com/deepfence/SecretScanner)
* [Docker docs - docker save](https://docs.docker.com/engine/reference/commandline/save/)
