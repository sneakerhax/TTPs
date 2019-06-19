# Data Sources - Certificates

Open Data (data can be found [here](https://opendata.rapid7.com/))

```zgrep -a -F \.site.com * ```

Searching sonar data

```https://crt.sh/?q=%.site.com```

Search certificate transparency(Comodo)

```https://censys.io/certificates/report?q=<domain>&field=parsed.subject.common_name.raw&max_buckets=500```

Create report in censys for domain certificates
