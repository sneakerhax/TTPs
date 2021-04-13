# Windows - CMD

Using the Windows command line to search for privilige escalation

### Check current privileges

```whoami /groups ```

Windows - to check integrity level and permissions

### Patch Level

```winver```

Check Windows version to match kb for missing patches

```wmic qfe get Caption,Description,HotFixID,InstalledOn```

Using WMIC to check for installed patches

```systeminfo.exe```

Check for missing patches (CMD)
