## Azure Key Vault - Soft Delete and Purge Protection

Ref:

### Enable soft delete on existing KV

($resource = Get-AzResource -ResourceId (Get-AzKeyVault -VaultName "ContosoVault").ResourceId).Properties | Add-Member -MemberType "NoteProperty" -Name "enableSoftDelete" -Value "true"

Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties

### Delete and recover an entire KV

Remove-AzKeyVault -VaultName 'ContosoVault'

Get-AzKeyVault -InRemovedState

Undo-AzKeyVaultRemoval -VaultName ContosoVault -ResourceGroupName ContosoRG -Location westus

### Delete and recover an individual object

Remove-AzKeyVaultKey -VaultName ContosoVault -Name ContosoFirstKey

Get-AzKeyVaultKey -VaultName ContosoVault -InRemovedState

Undo-AzKeyVaultKeyRemoval -VaultName ContosoVault -Name ContosoFirstKey
