from bicepbuilder import infra
from bicepbuilder.expressions import ResourceGroup, UnionString, UniqueString, Subscription, Union
from bicepbuilder.modules import StorageAccount

with infra() as deployment:
    env_name = deployment.param(
        "environmentName",
        "string",
        description="AZD environment name",
        min_length=1,
        max_length=64
    )
    principal_id = deployment.param(
        "principalId",
        "string",
        description="Id of the user or app to assign application roles",
    )
    location = deployment.param(
        "location",
        "string",
        allowed=["westus", "westus2", "eastus", "eastus2"],
        description="Primary location for all resources"
    )
    tags = deployment.var("tags", "object", {'azd-env-name': env_name})
    cm_id = deployment.var(
        "cloudmachineId",
        "string",
        UniqueString(Subscription().subscription_id, env_name, location)
    )

    rg = deployment.resource_group(
        name=cm_id,
        location=location,
        tags=UnionString(tags, {'DoNotDelete': True}))

    with deployment.module("cloudmachine", scope=rg) as cloudmachine_module:
        cloudmachine_module.param(location, default=ResourceGroup().location)
        cloudmachine_module.param(principal_id)
        cloudmachine_module.param(tags)
        cloudmachine_module.param(cm_id)

        managed_identity = cloudmachine_module.managed_identity(
            name=cm_id.format(prefix="antisch"),
            tags=tags,
            location=location
        )

        params: StorageAccount = {
            "skuName": "Premium_LRS",
            "name": cm_id.format(prefix="antisch"),
            "location": location,
            "tags": tags,
            "accessTier": "Hot",
            "kind": "StorageV2",
            "managedIdentities": {
                "userAssignedResourceIds": [
                    managed_identity.id
                ]
            },
            "allowBlobPublicAccess": False,
            "enableHierarchicalNamespace": True,
            "tableServices": {"tables": []},
            "blobServices": {
                "containers": [{"name": "Default"}]
            },
            "roleAssignments": [
                {
                    "roleDefinitionIdOrName": "Storage Blob Data Contributor",
                    "principalType": "User",
                    "principalId": principal_id
                },
                {
                    "roleDefinitionIdOrName": "Storage Blob Data Contributor",
                    "principalType": "ServicePrincipal",
                    "principalId": managed_identity.principal_id
                },
                {
                    "roleDefinitionIdOrName": "Storage Table Data Contributor",
                    "principalType": "User",
                    "principalId": principal_id,
                },
                {
                    "roleDefinitionIdOrName": "Storage Table Data Contributor",
                    "principalType": "ServicePrincipal",
                    "principalId": managed_identity.principal_id
                }
            ]
        }

        storage = cloudmachine_module.add(
            "storage_account",
            params,
            )
        #rg.output(storage["outputs"]["primaryBlobEndpoint"])






# targetScope = 'subscription'

# @minLength(1)
# @maxLength(64)
# @description('AZD environment name')
# param environmentName string

# @description('Id of the user or app to assign application roles')
# param principalId string

# @minLength(1)
# @description('Primary location for all resources')
# param location string

# var tags = { 'azd-env-name': environmentName }
# var cloudmachineId = uniqueString(subscription().subscriptionId, environmentName, location)
