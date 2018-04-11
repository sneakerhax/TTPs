## Nmap

```nmap -sn -n T4 192.168.1.1/24```

Ping scan with no dns resolution

```nmap -sS -p1-65535 -T5 --open --reason 192.168.1.1/24 -oA output```

Scan all ports quickly to get initital ports open(Run T4/T3 into same file to make sure no ports missed)

```nmap -sV -p<ports> --script=banner 192.168.1.1/24```

Service version and banner grab on range of ports

```nmap -A -T5 -oA output 192.168.1.1/24```

Aggressive scan for quick results

```nmap -p139,445 --script=smb,msrpc,smb-enum-shares,smb-enum-users 192.168.1.1```

Enumerate smb with NSE Scripts

```OSX:  nse(){ find /usr/local/share/nmap/scripts/ -iname "*$1*" | cut -c32- | cut -d'.' -f1;i}```
```Linux: nse(){ find /usr/share/nmap/scripts/ -iname *$1* -printf '%P\n';}``` - hecky

Setup custom functions for searching nse scripts

```nse search```

Example usage of custom nse function
