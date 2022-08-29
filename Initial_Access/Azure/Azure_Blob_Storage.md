# Azure - Blob Storage

### Searching blog storage

File types that may contain secrets:
* Search inside blob storage for .publishsetting file which contains an encoded certificate with management credentials
* Search inside blob storage for XML files
* Search inside blog storage for .config files or web.config files or app.config

Look for the following in files:
* SAS URI - Is used to grant access to blob storage files (Use Azure Storage Explorer)
* Connection String - Used to connect to storage
* Account name and key - Used to administer account

Grep VHDS files for shadow hashes (Download VHD and run the following grep):
Select-String ":0:99999:" <file>.vhd -ca

**Reference:**
* [Blue Cloud of Death Red Teaming Azure](https://www.youtube.com/watch?v=DPcMuRP3P7A) - Bryce Kunz
