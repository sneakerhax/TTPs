# HTTPX

**Description:** This entry descrribes ways to use http for recon

**Mitre Att&ck:** hhttps://attack.mitre.org/techniques/T1595/

**Requirements:** httpx

## Usage examples

```
echo <site.com> | httpx -sc -title -server -fr -sr -store-chain
```

Run httpx with status code, page title, following redirects, storing response, and storing redirect chain

```
echo <site.com> | httpx -sc -title -server -fr -location -td -ip -cname
```

Run httpx with status code, page title, following redirects, listing location, display technologies, display ip, display cname
  
## References
* https://github.com/projectdiscovery/httpx
