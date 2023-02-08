# CMD

**Description:** This entry described how to look for privilege escalation opportunities using the Windows command line

**Requirements:** cmd (windows)

## Checking current permissions

```
whoami /groups
```

Windows - to check integrity level and permissions

## Checking patch level

```
winver
```

Check Windows version to match kb for missing patches

```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

Using WMIC to check for installed patches

```
systeminfo.exe
```

Check for missing patches

  
## References
* none