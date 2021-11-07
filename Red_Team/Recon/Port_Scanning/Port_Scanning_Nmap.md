# Port Scanning - Nmap

```
nmap -sn -n T4 192.168.1.1/24
```

Ping scan with no dns resolution

```
nmap -sS -p1-65535 -T5 --open --reason 192.168.1.1/24 -oA output
```

Scan all ports quickly to get initital ports open(Run T4/T3 into same file to make sure no ports missed)

```
nmap -sV -p<ports> --script=banner 192.168.1.1/24
```

Service version and banner grab on range of ports

```
nmap -A -T5 -oA output 192.168.1.1/24
```

Aggressive scan for quick results

```
nmap -p139,445 --script=smb,msrpc,smb-enum-shares,smb-enum-users 192.168.1.1
```

Enumerate smb with NSE Scripts

```
nmap -sn -Pn -n --script=shodan-api --script-args 'shodan-api.apikey=XXXX' <target>
```

Lookup target in Shodan without active port scanning

```
nmap -p U:53,T:443 <target>
```

Scan UDP and TCP ports

```
nmap -sUT --top-ports <number> --open <target>
```

Scan top TCP/UDP ports

```
nmap -g 443 -p- <ipaddress>
```

Enter firewall with source port 443 specified to leverage loosely configured firewall rules
