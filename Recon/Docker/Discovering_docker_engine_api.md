# Discovering Docker Engine API

**Description:** This entry describes how to perform recon to discovery the Docker engine API

## Common Docker Engine API Ports

* 2375 - Unencrypted
* 2376 - Encrypted

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
* [Docker Engine API Reference](https://docs.docker.com/engine/api/)
* [Metasploit Docs - docker_daemon_tcp module](https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/exploit/linux/http/docker_daemon_tcp.md)