# SMB & Netbios

**Description:** This entry describes how to collect SMB information

**Requirements:** rpcclient, nbtscan, enum4linux, smbmap, smbclient

## Collectin SMB/Netbios information

SMB versions:

* SMB1 – Windows 2000, XP and Windows 2003
* SMB2 – Windows Vista SP1 and Windows 2008
* SMB2.1 – Windows 7 and Windows 2008 R2
* SMB3 – Windows 8+ and Windows 2012+

```
rpcclient -U "" <target>
```

Manual check for null sessions

```
nbtscan
```

Scan network for Netbios name information

```
enum4linux -a <target>
```

Enumerate SMB all checks

```
smbmap -H <target> -R
```

Scan for open SMB shares and recursively list

```
smbclient //10.10.232.87/<share>
smb: \>get <filename>
```

Download file from SMB share

## References
* [RPCclient docs](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html)
* [Kali Tools - rpcclient](https://www.kali.org/tools/samba/#rpcclient)
* [Kali Tools - nbtscan](https://www.kali.org/tools/nbtscan/)
* [Kali Tools - enum4linux](https://www.kali.org/tools/enum4linux/)
* [Kali Tools - smbmap](https://www.kali.org/tools/smbmap/)
* [Kali Tools - smbclient](https://www.kali.org/tools/samba/#smbclient-1)