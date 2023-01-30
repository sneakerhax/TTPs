# Lookup

```
nslookup
>set type=cname
>domain.com
```

Lookup different record types for domain name (e.g. a,mx,ns)

```
dig +short <hostname>
```

Forward lookup on hostname

```
dig +short -x <ip_address>
```

Reverse Lookup on ip address

```
Resolve-DnsName <hostname>
```

Lookup hostname with Powershell

```
nmap --resolve-all -sL <site>
```

Resolve all ipv4 addresses for website [Reference](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/still-scanning-ip-addresses-you-re-doing-it-wrong/)

```
nmap --resolve-all -sL -6 <site>
```

Resolve all ipv6 addresses for a website [Reference](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/still-scanning-ip-addresses-you-re-doing-it-wrong/)
