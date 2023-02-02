# Discovering Docker Engine API

This entry describes how to perform recon to discovery Docker API

## Ports

* 2375 - Unencrypted
* 2376 - Encrypted

## Recon

```
Docker:
  Version: 19.03.8
  Kernel Version: 3.10.0-514.10.2.el7.x86_64
  API Version: 1.40
  Go Version: go1.12.17
  OS: linux
```

Example header

```
curl -Ik <host>:<port>/version
```

Use curl to display the api version
