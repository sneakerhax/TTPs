# Docker commands

```docker pull```

Pull down Docker image

```docker images```

List all built images

```docker ps -a```

List all containers

```docker build -t <image_name> <location of Dockerfile>```

Building/Updating a docker image

```docker run -t -d <image>```

Create persistent container

```docker run -it <image_name> <argument>```

Running a docker image that contains an ENTRYPOINT and accepts arguments

```docker exec -it <container_name> <command_name>```

Run command inside of docker container eg. /bin/bash (must have persistent container)

```docker rm <container_name>```

Destroy container

```docker rmi <image_name>```

Destroy image



