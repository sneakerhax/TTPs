# Dump Keyvault secret Powershell

**Description:** This entry details how to authenticate to an Azure account with Powershell, list keyvaults, and dump a password in plain text 

**Requirements:** AZ Powershell

## Retrieve a single secret

```Connect-AzAccount```

Authenticate to Azure account

```Get-AzKeyVaultSecret```

List all secrets

```Get-AzKeyVaultSecret -VaultName '<keyvault_name>' -Name '<secret_name>' -AsPlainText```

Dump secret as plain text

## References
* https://docs.microsoft.com/en-us/powershell/module/az.keyvault/get-azkeyvaultsecret?view=azps-6.1.0
