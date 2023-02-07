# Bash One Liners

**Description:** This entry describes various ways to use bash one liners to perform recon

**Requirements:** bash, curl

## Using Bash for recon

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

```
cat targets.txt | gxargs -d '\n' -n1 -I % curl -ILk  %
```

Use file of targets and pipe them to xargs (OSX gxargs which is gnu xargs installed with brew) to be used as arguments to other tools

```
while read subdomain;do nslookup $subdomain.sneakerhax.com; done < dns-wordlist.txt
```

Basic nslookup subdomain brute force

```
while read dir; do status_code=$(curl -w "%{http_code}" -o /dev/null http://<ip_address>:<port>/$dir 2>/dev/null) && printf "[*] $status_code $dir \n"; done < "Discovery/Web-Content/versioning_metafiles.txt"
```

Get directory status code for directory brute force
  
## References
* [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)