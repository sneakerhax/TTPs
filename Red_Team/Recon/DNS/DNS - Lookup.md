# DNS - Lookup

```
nslookup
>set type=all
>domain.com
```

Lookup CNAMES for domain name

```dig +short -x <ip_address> ```

Reverse Lookup on ip address

```Resolve-DnsName <hostname>```

Lookup hostname with Powershell

```nmap --resolve-all -sL <site>```

Resolve all ipv4 addresses for website [Reference](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/still-scanning-ip-addresses-you-re-doing-it-wrong/)

```nmap --resolve-all -sL -6 <site>```

Resolve all ipv6 addresses for a website [Reference](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/still-scanning-ip-addresses-you-re-doing-it-wrong/)
