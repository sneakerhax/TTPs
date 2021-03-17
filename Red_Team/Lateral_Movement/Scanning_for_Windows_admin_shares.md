# Scanning for Windows admin shares

Description: This entry details how to scan for admin shares to identify machines that can be accessed with local admin access

Mitre Att&ck: https://attack.mitre.org/techniques/T1021/002/

Requirements: Powershell

## Powershell

```
$machines = Get-Content <file>
$machines | ForEach-Object {dir \\$_\c$}
```
