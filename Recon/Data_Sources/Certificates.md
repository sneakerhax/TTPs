# Certificates

**Description:** This entry describes how to use data sources to dicover certicate data

**Requirements:** zgrep

## Searching for certificate data

Open Data (data can be found [here](https://opendata.rapid7.com/))

```
zgrep -a -F \.site.com *
```

Searching sonar or other certificate data for site information

```
https://crt.sh/?q=%.site.com
```

Search certificate transparency(Comodo)

```
https://censys.io/certificates/report?q=<domain>&field=parsed.subject.common_name.raw&max_buckets=500
```

Create report in censys for domain certificates

  
## References
* [Censys Search Docs](https://search.censys.io/search/language?resource=hosts)