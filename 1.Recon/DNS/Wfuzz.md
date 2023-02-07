# Wfuzz

**Description:** This entry describes how to use Wfuzz to discover subdomains

**Requirements:** python, wfuzz

## Run Wfuzz

```
wfuzz -H 'Host: FUZZ.site.com' -w <wordlist> -u site.com --hh <remove string> -hc 404
```

Fuzz DNS with wfuzz (hide 404)
  
## References
* [Wfuzz Github](https://github.com/xmendez/wfuzz)
* [Wfuzz Docs](https://wfuzz.readthedocs.io/en/latest/)