# Windows - Powershell

```$PSVersionTable```

Check Powershell version

```Get-WindowsFeatures powershell-v2```

Check to see if Powershell V2 is installed (Server only)

```powershell -version 2```

Downgrade to Powershell v2(Has no amsi/logging)

```tasklist /v```

List all processes

``` Get-AdUser -Filter * -Properties SamAccountName, description | select SamAccountName, description | select -expand $_.results```

Get user and description field from AD to find passwords

```Get-ADUser <username> -properties passwordlastset```

Check password last set

```Invoke-Command -ComputerName server01 -ScriptBlock {Get-Process}```

Run command on remote system ([docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-6))

```Get-ChildItem -Path C:\ -Include *<search_term>* -Recurse -ErrorAction SilentlyContinue```

Search for file recursively
