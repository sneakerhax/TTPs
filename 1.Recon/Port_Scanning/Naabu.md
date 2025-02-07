# Naabu

**Description:** This entry describes how to use Naabu to perform port scans

**Requirements:** naabu

## Naabu SYN scan for faster scans

```
sudo naabu -v --rate 10000 -scan-type s -p <ports> -host <target>
```

Requires root privs for SYN scan
  
## References
* [Github - Naabu](https://github.com/projectdiscovery/naabu)
