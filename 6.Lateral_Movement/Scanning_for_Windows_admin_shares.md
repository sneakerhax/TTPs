# Scanning for Windows admin shares

**Description:** This entry describes how to scan for admin shares. When able to view the admin shares this is an indicator of having admin access to the machine

**Requirements:** Powershell

## Powershell

```powershell
$machines = Get-Content <file>
$machines | ForEach-Object {dir \\$_\c$}
```

Scan remote machines for c$ admin acess

## Refernces
*none