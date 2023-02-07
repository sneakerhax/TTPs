# Nmap

**Description:** This entry describes how to use Nmap to discover subdomains

**Requirements:** Nmap

## Running Nmap

```
nmap --script dns-brute --script-args dns-brute.domain=<domain>,dns-brute.threads=<number of threads>,dns-brute.hostlist=<wordlist>
```

Subdomain brute force with Nmap dns-brute NSE script

```
nmap --resolve-all -sL <target>
```

Resolve all ipv4 addresses for website

```
nmap --resolve-all -sL -6 <target>
```

Resolve all ipv6 addresses for a website
  
## References
* [Nmap NSE dns-brute](https://nmap.org/nsedoc/scripts/dns-brute.html)
