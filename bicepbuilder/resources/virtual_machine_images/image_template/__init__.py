from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    name: str
    """The name (as GUID) of the role assignment. If not provided, a GUID will be generated."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class InVMValidation(TypedDict, total=False):
    """A list of validators that will be performed on the image. Azure Image Builder supports File, PowerShell and Shell validators."""
    type: Required[Literal['File', 'PowerShell', 'Shell']]
    """The type of validation."""
    destination: str
    """Destination of the file."""
    inline: List[object]
    """Array of commands to be run, separated by commas."""
    name: str
    """Friendly Name to provide context on what this validation step does."""
    runAsSystem: bool
    """If specified, the PowerShell script will be run with elevated privileges using the Local System user. Can only be true when the runElevated field above is set to true."""
    runElevated: bool
    """If specified, the PowerShell script will be run with elevated privileges."""
    scriptUri: str
    """URI of the PowerShell script to be run for validation. It can be a github link, Azure Storage URI, etc."""
    sha256Checksum: str
    """Value of sha256 checksum of the file, you generate this locally, and then Image Builder will checksum and validate."""
    sourceUri: str
    """The source URI of the file."""
    validExitCodes: List[object]
    """Valid codes that can be returned from the script/inline command, this avoids reported failure of the script/inline command."""


class ValidationProce(TypedDict, total=False):
    """Configuration options and list of validations to be performed on the resulting image."""
    continueDistributeOnFailure: bool
    """If validation fails and this field is set to false, output image(s) will not be distributed. This is the default behavior. If validation fails and this field is set to true, output image(s) will still be distributed. Please use this option with caution as it may result in bad images being distributed for use. In either case (true or false), the end to end image run will be reported as having failed in case of a validation failure. [Note: This field has no effect if validation succeeds.]."""
    inVMValidations: List['InVMValidation']
    """A list of validators that will be performed on the image. Azure Image Builder supports File, PowerShell and Shell validators."""
    sourceValidationOnly: bool
    """If this field is set to true, the image specified in the 'source' section will directly be validated. No separate build will be run to generate and then validate a customized image. Not supported when performing customizations, validations or distributions on the image."""


class VirtualMachineImageTemplate(TypedDict, total=False):
    """"""
    distributions: Required[List[object]]
    """The distribution targets where the image output needs to go to."""
    imageSource: Required[Dict[str, object]]
    """Image source definition in object format."""
    managedIdentities: Required['ManagedIdentity']
    """The managed identity definition for this resource."""
    name: Required[str]
    """The name prefix of the Image Template to be built by the Azure Image Builder service."""
    buildTimeoutInMinutes: int
    """The image build timeout in minutes. 0 means the default 240 minutes."""
    customizationSteps: List[object]
    """Customization steps to be run when building the VM image."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    optimizeVmBoot: Literal['Disabled', 'Enabled']
    """The optimize property can be enabled while creating a VM image and allows VM optimization to improve image creation time."""
    osDiskSizeGB: int
    """Specifies the size of OS disk."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    stagingResourceGroupResourceId: str
    """Resource ID of the staging resource group in the same subscription and location as the image template that will be used to build the image."""
    subnetResourceId: str
    """Resource ID of an already existing subnet, e.g.: /subscriptions/"""
    tags: Dict[str, object]
    """Tags of the resource."""
    validationProcess: 'ValidationProce'
    """Configuration options and list of validations to be performed on the resulting image."""
    vmSize: str
    """Specifies the size for the VM."""
    vmUserAssignedIdentities: List[object]
    """List of User-Assigned Identities associated to the Build VM for accessing Azure resources such as Key Vaults from your customizer scripts. Be aware, the user assigned identities specified in the 'managedIdentities' parameter must have the 'Managed Identity Operator' role assignment on all the user assigned identities specified in this parameter for Azure Image Builder to be able to associate them to the build VM."""
    baseTime: str
    """Do not provide a value! This date is used to generate a unique image template name."""


class VirtualMachineImageTemplateOutputs(TypedDict, total=False):
    """Outputs for VirtualMachineImageTemplate"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The full name of the deployed image template."""
    namePrefix: Output[Literal['string']]
    """The prefix of the image template name provided as input."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the image template was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the image template."""
    runThisCommand: Output[Literal['string']]
    """The command to run in order to trigger the image build."""


class VirtualMachineImageTemplateModule(Module):
    outputs: VirtualMachineImageTemplateOutputs

