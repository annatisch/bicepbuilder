
from bicepbuilder import infra
from bicepbuilder.expressions import ResourceGroup, Take, UnionString, UniqueString, Subscription
from bicepbuilder.resources import StorageAccount, ServiceBusNamespace

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

        storage_params: StorageAccount = {
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
        storage = cloudmachine_module.add("storage_account", storage_params)

        servicebus_params: ServiceBusNamespace = {
            "name": cm_id.format(prefix="antisch"),
            "location": location,
            "tags": tags,
            "skuObject": {"name": "Standard"},
            "authorizationRules": [
                {
                    "name": Take(UniqueString(rg.id).format(prefix='cm_sb_auth_rule_'), 50),
                    "rights": ["Listen", "Manage", "Send"]
                }
            ],
            "roleAssignments": [
                {
                    "roleDefinitionIdOrName": "Azure Service Bus Data Owner",
                    "principalType": "User",
                    "principalId": principal_id
                },
                {
                    "roleDefinitionIdOrName": "Azure Service Bus Data Owner",
                    "principalType": "ServicePrincipal",
                    "principalId": managed_identity.principal_id
                }
            ],
            "topics": [
                {
                    "name": "cm_internal_topic",
                    "defaultMessageTimeToLive": "P14D",
                    "maxMessageSizeInKilobytes": 256,
                    "enableBatchedOperations": True,
                    "requiresDuplicateDetection": False,
                    "supportOrdering": True,
                    "status": "Active",
                    "subscriptions": [
                        {
                            "name": "cm_internal_subscription",
                            "deadLetteringOnFilterEvaluationExceptions": True,
                            "deadLetteringOnMessageExpiration": True,
                            "defaultMessageTimeToLive": "P14D",
                            "enableBatchedOperations": True,
                            "isClientAffine": False,
                            "lockDuration": "PT30S",
                            "maxDeliveryCount": 10,
                            "requiresSession": False,
                            "status": "Active"
                        }
                    ]
                },
                {
                    "name": "cm_default_topic",
                    "defaultMessageTimeToLive": "P14D",
                    "maxMessageSizeInKilobytes": 256,
                    "enableBatchedOperations": True,
                    "requiresDuplicateDetection": False,
                    "supportOrdering": True,
                    "status": "Active",
                    "subscriptions": [
                        {
                            "name": "cm_default_subscription",
                            "deadLetteringOnFilterEvaluationExceptions": True,
                            "deadLetteringOnMessageExpiration": True,
                            "defaultMessageTimeToLive": "P14D",
                            "enableBatchedOperations": True,
                            "isClientAffine": False,
                            "lockDuration": "PT30S",
                            "maxDeliveryCount": 10,
                            "requiresSession": False,
                            "status": "Active"
                        }
                    ]
                }
            ]
        }

        servicebus = cloudmachine_module.add("service_bus_namespace", servicebus_params)
        
        cloudmachine_module.output("BlobEndpoint", storage.outputs["primaryBlobEndpoint"])
        cloudmachine_module.output("TableEndpoint", storage.outputs["serviceEndpoints"].get("table", "string"))
        cloudmachine_module.output("StorageId", storage.outputs["resourceId"])
        cloudmachine_module.output("StorageName", storage.outputs["name"])
        cloudmachine_module.output("ServiceBusId", servicebus.outputs["resourceId"])
        cloudmachine_module.output("ServiceBusName", servicebus.outputs["name"])

    deployment.output("AZURE_CLOUDMACHINE_BLOB_ENDPOINT", cloudmachine_module.outputs["BlobEndpoint"])
    deployment.output("AZURE_CLOUDMACHINE_TABLE_ENDPOINT", cloudmachine_module.outputs["BlobEndpoint"])
    deployment.output("AZURE_CLOUDMACHINE_STORAGE_ID", cloudmachine_module.outputs["StorageId"])
    deployment.output("AZURE_CLOUDMACHINE_STORAGE_NAME", cloudmachine_module.outputs["StorageName"])
