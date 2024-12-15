from bicepbuilder import infra

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
    deployment.var("tags", {'azd-env-name': env_name})




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
