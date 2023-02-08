# Meterpreter

**Description:** This entry describes how to privilege escalate from a Meterpreter shell on Windows

**Requirements:** metasploit

## Checking permission level using Meterpreter

```
getuid
```

Display the user that the Meterpreter server is running as on the host

```
use post/windows/gather/win_privs
```

This module will print if UAC is enabled, and if the current account is ADMIN enabled. It will also print UID,foreground SESSION ID, is SYSTEM status and current process PRIVILEGES

## Checking for privilege escalation exploits

```
use post/multi/recon/local_exploit_suggester
```

This module suggests local meterpreter exploits that can be used

```
getsystem
```

Attempt to get system privs on Windows system
  
## References
* [Offensive Security - Privilege Escalation](https://www.offensive-security.com/metasploit-unleashed/privilege-escalation/)