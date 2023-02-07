# Google

**Description:** This entry describes how to perform Google Dorking to perform recon

**Requirements:** browser

## Dorking examples

```
site:site.com inurl:/wp-content/
```

Looking for Wordpress sites (Wordpress must expose this directory)

```
inurl:<file_name>.axd filetype:axd site:site.com
```

Look for axd files which frequently contain passwords

## References
* [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)