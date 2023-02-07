# Discovering Kubernetes Dashboards

**Description:** This entry describes how to discovery Kubernetes dashboard

**Requirements:** curl, nmap, metasploit

## Curl

```
$ curl -sL localhost:30632 | grep title
<title>Kubernetes Dashboard</title>
```

## Nmap

```
nmap -sV --script=http-title -p <port> <target>
```

The results of this scan should be "http-title: Kubernetes Dashboard"

## Metasploit

```
msf> use auxiliary/scanner/http/title
msf> set rhost <target>
msf> set rport <port>
msf> set ssl true (optional)
msf> run

[+] [<target>:<port>] [C:200] [R:] [S:] Kubernetes Dashboard
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

The results can also be retreived in notes using "notes -t http.title"