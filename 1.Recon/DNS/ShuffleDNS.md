# ShuffleDNS

**Description:** This entry describes how to use ShuffleDNS to brute force dns records

**Requirements:** shuffledns, docker (optional)

## Running ShuffleDNS to brute force DNS records

```
docker run projectdiscovery/shuffledns -d <target> -r <list_of_resolvers> -w <wordlist>
```

Run ShuffleDNS on target using Docker
  
## References
* [Github - ShuffleDNS](https://github.com/projectdiscovery/shuffledns)