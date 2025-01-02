param location string = resourceGroup().location

param principalId string

param tags object

param cloudmachineId string

resource resource_rao0o 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'antisch${cloudmachineId}'
  location: location
  tags: tags
}

module storage_account_f2irq 'br/public:avm/res/storage/storage-account:0.14.0' = {
  name: '${deployment().name}_storage_account_f2irq'
  params: {
    skuName: 'Premium_LRS'
    name: 'antisch${cloudmachineId}'
    location: location
    tags: tags
    accessTier: 'Hot'
    kind: 'StorageV2'
    managedIdentities: {
      userAssignedResourceIds: [
        resource_rao0o.id
      ]
    }
    allowBlobPublicAccess: false
    enableHierarchicalNamespace: true
    tableServices: {
      tables: []
    }
    blobServices: {
      containers: [
        {
          name: 'Default'
        }
      ]
    }
    roleAssignments: [
      {
        roleDefinitionIdOrName: 'Storage Blob Data Contributor'
        principalType: 'User'
        principalId: principalId
      }
      {
        roleDefinitionIdOrName: 'Storage Blob Data Contributor'
        principalType: 'ServicePrincipal'
        principalId: resource_rao0o.properties.principalId
      }
      {
        roleDefinitionIdOrName: 'Storage Table Data Contributor'
        principalType: 'User'
        principalId: principalId
      }
      {
        roleDefinitionIdOrName: 'Storage Table Data Contributor'
        principalType: 'ServicePrincipal'
        principalId: resource_rao0o.properties.principalId
      }
    ]
  }
}
module service_bus_namespace_k5x7t 'br/public:avm/res/service-bus/namespace:0.10.0' = {
  name: '${deployment().name}_service_bus_namespace_k5x7t'
  params: {
    name: 'antisch${cloudmachineId}'
    location: location
    tags: tags
    skuObject: {
      name: 'Standard'
    }
    authorizationRules: [
      {
        name: take('cm_sb_auth_rule_${uniqueString(resourceGroup().id)}', 50)
        rights: [
          'Listen'
          'Manage'
          'Send'
        ]
      }
    ]
    roleAssignments: [
      {
        roleDefinitionIdOrName: 'Azure Service Bus Data Owner'
        principalType: 'User'
        principalId: principalId
      }
      {
        roleDefinitionIdOrName: 'Azure Service Bus Data Owner'
        principalType: 'ServicePrincipal'
        principalId: resource_rao0o.properties.principalId
      }
    ]
    topics: [
      {
        name: 'cm_internal_topic'
        defaultMessageTimeToLive: 'P14D'
        maxMessageSizeInKilobytes: 256
        enableBatchedOperations: true
        requiresDuplicateDetection: false
        supportOrdering: true
        status: 'Active'
        subscriptions: [
          {
            name: 'cm_internal_subscription'
            deadLetteringOnFilterEvaluationExceptions: true
            deadLetteringOnMessageExpiration: true
            defaultMessageTimeToLive: 'P14D'
            enableBatchedOperations: true
            isClientAffine: false
            lockDuration: 'PT30S'
            maxDeliveryCount: 10
            requiresSession: false
            status: 'Active'
          }
        ]
      }
      {
        name: 'cm_default_topic'
        defaultMessageTimeToLive: 'P14D'
        maxMessageSizeInKilobytes: 256
        enableBatchedOperations: true
        requiresDuplicateDetection: false
        supportOrdering: true
        status: 'Active'
        subscriptions: [
          {
            name: 'cm_default_subscription'
            deadLetteringOnFilterEvaluationExceptions: true
            deadLetteringOnMessageExpiration: true
            defaultMessageTimeToLive: 'P14D'
            enableBatchedOperations: true
            isClientAffine: false
            lockDuration: 'PT30S'
            maxDeliveryCount: 10
            requiresSession: false
            status: 'Active'
          }
        ]
      }
    ]
  }
}
output BlobEndpoint string = storage_account_f2irq.outputs.primaryBlobEndpoint
output TableEndpoint string = storage_account_f2irq.outputs.serviceEndpoints.table
output StorageId string = storage_account_f2irq.outputs.resourceId
output StorageName string = storage_account_f2irq.outputs.name
output ServiceBusId string = service_bus_namespace_k5x7t.outputs.resourceId
output ServiceBusName string = service_bus_namespace_k5x7t.outputs.name
