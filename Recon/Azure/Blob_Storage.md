# Blob Storage

**Description:** This entry describes how to discover blob storage targets

**Requirements:** Browser, gobuster

## Discovering blob storage targets with web browser

```
https://<name>.blob.core.windows.net
```

Searching for Azure blob storage (Name must be between 3-24 characters)

## Discovering blob storage targets with gobuster

```
gobuster -m dns -u "blob.core.windows.net" -i -t 100 -fw -w <wordlist>
```

Discover blob storage account name (from Blue Cloud of Death by Bryce Kunz)

```
gobuster -m dir -u "https://<storage_account_name>.blob.core.windows.net/<container_name>/<blobname>" -i -t 100 -e -s 200,204 -w <wordlist>
```

Discover container names and blobs

## References
* [BSides Nashville 2018 Red 00 Blue Cloud of Death Red Teaming Azure Bryce Kunz](https://www.youtube.com/watch?v=DPcMuRP3P7A) - Bryce Kunz
