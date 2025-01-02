targetScope = 'subscription'

@sys.description('AZD environment name')
@sys.maxLength(64)
@sys.minLength(64)
param environmentName string

@sys.description('Id of the user or app to assign application roles')
param principalId string

@sys.description('Primary location for all resources')
@sys.allowed([
  'westus'
  'westus2'
  'eastus'
  'eastus2'
])
param location string

var tags = {
  'azd-env-name': environmentName
}


var cloudmachineId = uniqueString(subscription().subscriptionId, environmentName, location)

resource resource_k9qhh 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: cloudmachineId
  location: location
  tags: union(tags, {'DoNotDelete': true})
}

module module_2s9v5 'cloudmachine.bicep' = {
  name: '${deployment().name}_module_2s9v5'
  scope: resourceGroup(resource_k9qhh.name)
  params: {
    location: location
    principalId: principalId
    tags: tags
    cloudmachineId: cloudmachineId
  }
}

output AZURE_CLOUDMACHINE_BLOB_ENDPOINT string = module_2s9v5.outputs.BlobEndpoint
output AZURE_CLOUDMACHINE_TABLE_ENDPOINT string = module_2s9v5.outputs.BlobEndpoint
output AZURE_CLOUDMACHINE_STORAGE_ID string = module_2s9v5.outputs.StorageId
output AZURE_CLOUDMACHINE_STORAGE_NAME string = module_2s9v5.outputs.StorageName
