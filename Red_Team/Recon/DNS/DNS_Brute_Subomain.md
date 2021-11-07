# DNS Brute - Subdomain

```
amass -d <domain>
```

Amass sub-domain brute

```
gobuster -m dns -u <domain> -w <wordlist> -t 50
```

Gobuster sub-domain brute

```
nmap --script dns-brute --script-args dns-brute.domain=<domain>,dns-brute.threads=<number of threads>,dns-brute.hostlist=<wordlist>
```

Subdomain brute force with Nmap dns-brute NSE script

```
wfuzz -H 'Host: FUZZ.site.com' -w <wordlist> -u site.com --hh <remove string> -hc 404
```

Fuzz DNS with wfuzz (hide 404)
