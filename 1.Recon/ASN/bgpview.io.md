# BGPView.io

**Description:** This entry describes how to lookup ASN records on bgpview.io

**Requirements:** browser, curl, jq

## Section

```
curl -Lk https://bgpview.io/search/<search>
```

Search for ASN ranges with search term

```
curl -Lk "https://api.bgpview.io/search?query_term=adobe" | jq '.data.asns[] | .asn, .name'
```

Search term and pull out ASN ID and name

```
curl -Lk "https://api.bgpview.io/search?query_term=adobe" | jq '.data.ipv4_prefixes[].prefix'
```

Seearch term and pull out all ip ranges
  
## References
* [BGP faq](https://bgpview.io/faq)