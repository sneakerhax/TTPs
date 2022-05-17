# Google Dorking

**Description:** This entry shows how to perform Google Dorking to perform recon

**Mitre Att&ck:** [T1593.002](https://attack.mitre.org/techniques/T1593/002/)

**Requirements:** N/A

## Dorking examples

```
site:site.com inurl:/wp-content/
```

Looking for Wordpress sites(Wordpress must expose this directory)

```
inurl:<file_name>.axd filetype:axd site:site.com
```

Look for sensitive files
