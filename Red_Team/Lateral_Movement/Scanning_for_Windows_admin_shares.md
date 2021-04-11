# Scanning for Windows admin shares

**Description:** This entry details how to scan for admin shares. If you're able to view the admin shares this is an indicator that you may have admin access to the machine

**Mitre Att&ck:** https://attack.mitre.org/techniques/T1021/002/

**Requirements:** Powershell

## Powershell

```
$machines = Get-Content <file>
$machines | ForEach-Object {dir \\$_\c$}
```
