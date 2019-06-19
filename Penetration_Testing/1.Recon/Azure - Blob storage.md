## Azure - Blob storage

```https://<name>.blob.core.windows.net```

Searching for Azure storage(blob)(Name must be between 3-24 characters)

```gobuster -m dns -u "blob.core.windows.net" -i -t 100 -fw -w <wordlist>```

Discover blob storage account name (from Blue Cloud of Death by Bryce Kunz)

```gobuster -m dir -u "https://<storage_account_name>.blob.core.windows.net/<container_name>/<blobname>" -i -t 100 -e -s 200,204 -w <wordlist>```

Discover container names and blobs (from Blue Cloud of Death by Bryce Kunz)
