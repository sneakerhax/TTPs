# Misc - Bash One Liners

```
while read site;do curl -ILk $site/jmx-console 2>/dev/null; done < sites.txt
```

Find jmx-consoles or other directory from list of sites

```
while read ip;do response=$(whois $ip | grep OrgName) && printf "[+]ip address: $ip \n[+]$response \n\n"; done < iplist.txt
```

Get whois orgname from list of ip address

```
while read site;do status=$(curl -I $site 2>/dev/null | head -1) && echo $site $status; done < iplist.txt
```

Get status code from list of ip address

```
while read ip;do nmap -n -sL $ip | grep "report for" | cut -d " " -f5 >> iplistoutput;done < iplist.txt
```

Get list of ip addresses from list of cidr blocks in text file

```
curl https://cmyip.com/ 2>&1 | grep "My IP Address" | cut -d'>' -f2 | cut -d'<' -f1
```

Get public ip address from command line
