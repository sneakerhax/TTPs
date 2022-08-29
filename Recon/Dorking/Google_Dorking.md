# Google Dorking

**Description:** This entry describes how to perform Google Dorking to perform recon

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
