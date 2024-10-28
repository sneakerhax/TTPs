# Discovering Docker Engine API (Docker Daemon)

**Description:** This entry describes how to perform recon to discover the Docker engine API

**Requirements:** curl

## Common Docker Engine API Ports

* 2375 - Unencrypted Docker Daemon access
* 2376 - Encrypted Docker Daemon access
* 4243 - Docker rest API over HTTP
* 4244 - Docker Swarm API (now integrated into Docker API)

## Discovering the Docker engine API

```
curl -Ik <host>:<port>/version
```

Use curl to display the api version

```
Docker:
  Version: 19.03.8
  Kernel Version: 3.10.0-514.10.2.el7.x86_64
  API Version: 1.40
  Go Version: go1.12.17
  OS: linux
```

Example header

## References
* [Docker Engine - API Reference](https://docs.docker.com/engine/api/)
* [Metasploit Docs - docker_daemon_tcp module](https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/exploit/linux/http/docker_daemon_tcp.md)
