# Sub-domain brute force

```nmap --script dns-brute --script-args dns-brute.domain=<domain>,dns-brute.threads=<number of threads>,dns-brute.hostlist=<wordlist>```

Subdomain brute force with Nmap dns-brute NSE script

```python dnsrecon.py -t brt -D *wordlist* -d *domain*```

Subdomain brute force with dnsrecon
