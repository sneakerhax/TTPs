# Data Sources - Certificates

Sonar(data can be found [here](https://scans.io/))

```zgrep -a -F \.site.com * ```

Searching sonar data

```https://crt.sh/?q=%.site.com```

Search certificate transparency(Comodo)

```https://censys.io/certificates/report?q=<domain>&field=parsed.subject.common_name.raw&max_buckets=500```

Create report in censys for domain certificates
