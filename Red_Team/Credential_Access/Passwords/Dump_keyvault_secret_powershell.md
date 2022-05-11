# Dump Keyvault secret Powershell

**Description:** This entry details how to authenticate to an Azure account with Powershell, list keyvaults, and dump a password in plain text 

**Requirements:** AZ Powershell

**Mitre Att&ck:** https://attack.mitre.org/techniques/T1078

## Dump a single secret

```powershell
Connect-AzAccount
```

Authenticate to Azure account

```powershell
Get-AzKeyVault
```

List all vaults

```powershell
Get-AzKeyVaultSecret -VaultName <keyvault_name>
```

List all secrets

```powershell
Get-AzKeyVaultSecret -VaultName '<keyvault_name>' -Name '<secret_name>' -AsPlainText
```

Dump secret as plain text

```powershell
$secret_name = Get-AzKeyVaultSecret -VaultName <keyvault_name> | select Name
$secret_name | ForEach-Object { Get-AzKeyVaultSecret -VaultName '<keyvault_name>' -Name $_.Name -AsPlainText }
```

Generate list of keyvault secrets and dump each one in plaintext

```powershell
$vaults = Get-AzKeyVault | select VaultName
$secret_names = $vaults | ForEach-Object { Get-AzKeyVaultSecret -VaultName $_.VaultName | select VaultName, Name }
$secret_names | ForEach-Object { Get-AzKeyVaultSecret -VaultName $_.VaultName -Name $_.Name -AsPlainText }
```

Generate list of keyvaults, discover all secrets in vaults, dump all passwords from all vaults in plaintext

## References
* https://docs.microsoft.com/en-us/powershell/module/az.keyvault/get-azkeyvaultsecret?view=azps-6.1.0
