from typing import overload, Literal, Optional, Union, IO, Dict, Any, TYPE_CHECKING

from .._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
    BicepExpression,
    Module,
    Deployment,
    Output,
)

if TYPE_CHECKING:
    from .aad.domain_service import AadDomainService, AadDomainServiceModule
    from .alerts_management.action_rule import AlertsManagementActionRule, AlertsManagementActionRuleModule
    from .api_management.service import ApiManagementService, ApiManagementServiceModule
    from .app.container_app import AppContainerApp, AppContainerAppModule
    from .app.job import AppJob, AppJobModule
    from .app.managed_environment import AppManagedEnvironment, AppManagedEnvironmentModule
    from .app_configuration.configuration_store import AppConfigurationStore, AppConfigurationStoreModule
    from .automation.automation_account import AutomationAccount, AutomationAccountModule
    from .batch.batch_account import BatchAccount, BatchAccountModule
    from .cache.redis import CacheRedis, CacheRedisModule
    from .cdn.profile import CdnProfile, CdnProfileModule
    from .cognitive_services.account import CognitiveServicesAccount, CognitiveServicesAccountModule
    from .communication.communication_service import CommunicationService, CommunicationServiceModule
    from .communication.email_service import CommunicationEmailService, CommunicationEmailServiceModule
    from .compute.availability_set import ComputeAvailabilitySet, ComputeAvailabilitySetModule
    from .compute.disk import ComputeDisk, ComputeDiskModule
    from .compute.disk_encryption_set import ComputeDiskEncryptionSet, ComputeDiskEncryptionSetModule
    from .compute.gallery import ComputeGallery, ComputeGalleryModule
    from .compute.image import ComputeImage, ComputeImageModule
    from .compute.proximity_placement_group import ComputeProximityPlacementGroup, ComputeProximityPlacementGroupModule
    from .compute.ssh_public_key import ComputeSshPublicKey, ComputeSshPublicKeyModule
    from .compute.virtual_machine import ComputeVirtualMachine, ComputeVirtualMachineModule
    from .compute.virtual_machine_scale_set import ComputeVirtualMachineScaleSet, ComputeVirtualMachineScaleSetModule
    from .consumption.budget import ConsumptionBudget, ConsumptionBudgetModule
    from .container_instance.container_group import ContainerInstanceContainerGroup, ContainerInstanceContainerGroupModule
    from .container_registry.registry import ContainerRegistry, ContainerRegistryModule
    from .container_service.managed_cluster import ContainerServiceManagedCluster, ContainerServiceManagedClusterModule
    from .data_factory.factory import DataFactory, DataFactoryModule
    from .data_protection.backup_vault import DataProtectionBackupVault, DataProtectionBackupVaultModule
    from .databricks.access_connector import DatabricksAccessConnector, DatabricksAccessConnectorModule
    from .databricks.workspace import DatabricksWorkspace, DatabricksWorkspaceModule
    from .db_for_my_sql.flexible_server import DbForMySqlFlexibleServer, DbForMySqlFlexibleServerModule
    from .db_for_postgre_sql.flexible_server import DbForPostgreSqlFlexibleServer, DbForPostgreSqlFlexibleServerModule
    from .desktop_virtualization.application_group import DesktopVirtualizationApplicationGroup, DesktopVirtualizationApplicationGroupModule
    from .desktop_virtualization.host_pool import DesktopVirtualizationHostPool, DesktopVirtualizationHostPoolModule
    from .desktop_virtualization.scaling_plan import DesktopVirtualizationScalingPlan, DesktopVirtualizationScalingPlanModule
    from .desktop_virtualization.workspace import DesktopVirtualizationWorkspace, DesktopVirtualizationWorkspaceModule
    from .dev_ops_infrastructure.pool import DevOpsInfrastructurePool, DevOpsInfrastructurePoolModule
    from .dev_test_lab.lab import DevTestLab, DevTestLabModule
    from .digital_twins.digital_twins_instance import DigitalTwinsInstance, DigitalTwinsInstanceModule
    from .document_db.database_account import DocumentDbDatabaseAccount, DocumentDbDatabaseAccountModule
    from .document_db.mongo_cluster import DocumentDbMongoCluster, DocumentDbMongoClusterModule
    from .elastic_san.elastic_san import ElasticSan, ElasticSanModule
    from .event_grid.domain import EventGridDomain, EventGridDomainModule
    from .event_grid.namespace import EventGridNamespace, EventGridNamespaceModule
    from .event_grid.system_topic import EventGridSystemTopic, EventGridSystemTopicModule
    from .event_grid.topic import EventGridTopic, EventGridTopicModule
    from .event_hub.namespace import EventHubNamespace, EventHubNamespaceModule
    from .fabric.capacity import FabricCapacity, FabricCapacityModule
    from .hybrid_compute.machine import HybridComputeMachine, HybridComputeMachineModule
    from .insights.action_group import InsightsActionGroup, InsightsActionGroupModule
    from .insights.activity_log_alert import InsightsActivityLogAlert, InsightsActivityLogAlertModule
    from .insights.component import InsightsComponent, InsightsComponentModule
    from .insights.data_collection_endpoint import InsightsDataCollectionEndpoint, InsightsDataCollectionEndpointModule
    from .insights.data_collection_rule import InsightsDataCollectionRule, InsightsDataCollectionRuleModule
    from .insights.diagnostic_setting import InsightsDiagnosticSetting, InsightsDiagnosticSettingModule
    from .insights.metric_alert import InsightsMetricAlert, InsightsMetricAlertModule
    from .insights.private_link_scope import InsightsPrivateLinkScope, InsightsPrivateLinkScopeModule
    from .insights.scheduled_query_rule import InsightsScheduledQueryRule, InsightsScheduledQueryRuleModule
    from .insights.webtest import InsightsWebtest, InsightsWebtestModule
    from .key_vault.vault import KeyVault, KeyVaultModule
    from .kubernetes_configuration.extension import KubernetesConfigurationExtension, KubernetesConfigurationExtensionModule
    from .kubernetes_configuration.flux_configuration import KubernetesConfigurationFluxConfiguration, KubernetesConfigurationFluxConfigurationModule
    from .kusto.cluster import KustoCluster, KustoClusterModule
    from .load_test_service.load_test import LoadTestServiceLoadTest, LoadTestServiceLoadTestModule
    from .logic.workflow import LogicWorkflow, LogicWorkflowModule
    from .machine_learning_services.workspace import MachineLearningServicesWorkspace, MachineLearningServicesWorkspaceModule
    from .maintenance.maintenance_configuration import MaintenanceConfiguration, MaintenanceConfigurationModule
    from .managed_identity.user_assigned_identity import ManagedIdentityUserAssignedIdentity, ManagedIdentityUserAssignedIdentityModule
    from .management.management_group import ManagementGroup, ManagementGroupModule
    from .net_app.net_app_account import NetAppAccount, NetAppAccountModule
    from .network.application_gateway import NetworkApplicationGateway, NetworkApplicationGatewayModule
    from .network.application_gateway_web_application_firewall_policy import NetworkApplicationGatewayWebApplicationFirewallPolicy, NetworkApplicationGatewayWebApplicationFirewallPolicyModule
    from .network.application_security_group import NetworkApplicationSecurityGroup, NetworkApplicationSecurityGroupModule
    from .network.azure_firewall import NetworkAzureFirewall, NetworkAzureFirewallModule
    from .network.bastion_host import NetworkBastionHost, NetworkBastionHostModule
    from .network.connection import NetworkConnection, NetworkConnectionModule
    from .network.ddos_protection_plan import NetworkDdosProtectionPlan, NetworkDdosProtectionPlanModule
    from .network.dns_forwarding_ruleset import NetworkDnsForwardingRuleset, NetworkDnsForwardingRulesetModule
    from .network.dns_resolver import NetworkDnsResolver, NetworkDnsResolverModule
    from .network.dns_zone import NetworkDnsZone, NetworkDnsZoneModule
    from .network.express_route_circuit import NetworkExpressRouteCircuit, NetworkExpressRouteCircuitModule
    from .network.express_route_gateway import NetworkExpressRouteGateway, NetworkExpressRouteGatewayModule
    from .network.firewall_policy import NetworkFirewallPolicy, NetworkFirewallPolicyModule
    from .network.front_door import NetworkFrontDoor, NetworkFrontDoorModule
    from .network.front_door_web_application_firewall_policy import NetworkFrontDoorWebApplicationFirewallPolicy, NetworkFrontDoorWebApplicationFirewallPolicyModule
    from .network.ip_group import NetworkIpGroup, NetworkIpGroupModule
    from .network.load_balancer import NetworkLoadBalancer, NetworkLoadBalancerModule
    from .network.local_network_gateway import NetworkLocalNetworkGateway, NetworkLocalNetworkGatewayModule
    from .network.nat_gateway import NetworkNatGateway, NetworkNatGatewayModule
    from .network.network_interface import NetworkInterface, NetworkInterfaceModule
    from .network.network_manager import NetworkManager, NetworkManagerModule
    from .network.network_security_group import NetworkSecurityGroup, NetworkSecurityGroupModule
    from .network.network_watcher import NetworkWatcher, NetworkWatcherModule
    from .network.p2s_vpn_gateway import NetworkP2SVpnGateway, NetworkP2SVpnGatewayModule
    from .network.private_dns_zone import NetworkPrivateDnsZone, NetworkPrivateDnsZoneModule
    from .network.private_endpoint import NetworkPrivateEndpoint, NetworkPrivateEndpointModule
    from .network.private_link_service import NetworkPrivateLinkService, NetworkPrivateLinkServiceModule
    from .network.public_ip_address import NetworkPublicIpAddress, NetworkPublicIpAddressModule
    from .network.public_ip_prefix import NetworkPublicIpPrefix, NetworkPublicIpPrefixModule
    from .network.route_table import NetworkRouteTable, NetworkRouteTableModule
    from .network.service_endpoint_policy import NetworkServiceEndpointPolicy, NetworkServiceEndpointPolicyModule
    from .network.trafficmanagerprofile import NetworkTrafficmanagerprofile, NetworkTrafficmanagerprofileModule
    from .network.virtual_hub import NetworkVirtualHub, NetworkVirtualHubModule
    from .network.virtual_network_gateway import NetworkVirtualNetworkGateway, NetworkVirtualNetworkGatewayModule
    from .network.virtual_wan import NetworkVirtualWan, NetworkVirtualWanModule
    from .network.vpn_gateway import NetworkVpnGateway, NetworkVpnGatewayModule
    from .network.vpn_server_configuration import NetworkVpnServerConfiguration, NetworkVpnServerConfigurationModule
    from .network.vpn_site import NetworkVpnSite, NetworkVpnSiteModule
    from .operational_insights.workspace import OperationalInsightsWorkspace, OperationalInsightsWorkspaceModule
    from .operations_management.solution import OperationsManagementSolution, OperationsManagementSolutionModule
    from .portal.dashboard import PortalDashboard, PortalDashboardModule
    from .power_bi_dedicated.capacity import PowerBiDedicatedCapacity, PowerBiDedicatedCapacityModule
    from .purview.account import PurviewAccount, PurviewAccountModule
    from .recovery_services.vault import RecoveryServicesVault, RecoveryServicesVaultModule
    from .resource_graph.query import ResourceGraphQuery, ResourceGraphQueryModule
    from .resources.deployment_script import ResourcesDeploymentScript, ResourcesDeploymentScriptModule
    from .resources.resource_group import ResourceGroup, ResourceGroupModule
    from .search.search_service import SearchService, SearchServiceModule
    from .service_bus.namespace import ServiceBusNamespace, ServiceBusNamespaceModule
    from .service_fabric.cluster import ServiceFabricCluster, ServiceFabricClusterModule
    from .service_networking.traffic_controller import ServiceNetworkingTrafficController, ServiceNetworkingTrafficControllerModule
    from .sql.instance_pool import SqlInstancePool, SqlInstancePoolModule
    from .sql.managed_instance import SqlManagedInstance, SqlManagedInstanceModule
    from .sql.server import SqlServer, SqlServerModule
    from .storage.storage_account import StorageAccount, StorageAccountModule
    from .virtual_machine_images.image_template import VirtualMachineImageTemplate, VirtualMachineImageTemplateModule
    from .web.hosting_environment import WebHostingEnvironment, WebHostingEnvironmentModule
    from .web.serverfarm import WebServerfarm, WebServerfarmModule
    from .web.site import WebSite, WebSiteModule
    from .web.static_site import WebStaticSite, WebStaticSiteModule



def _aad_domain_service(
        bicep: IO[str],
        params: 'AadDomainService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AadDomainServiceModule':
    symbol = "aad_domain_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/aad/domain-service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .aad.domain_service import AadDomainServiceModule
    output = AadDomainServiceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _alerts_management_action_rule(
        bicep: IO[str],
        params: 'AlertsManagementActionRule',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AlertsManagementActionRuleModule':
    symbol = "alerts_management_action_rule_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/alerts-management/action-rule:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .alerts_management.action_rule import AlertsManagementActionRuleModule
    output = AlertsManagementActionRuleModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _api_management_service(
        bicep: IO[str],
        params: 'ApiManagementService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ApiManagementServiceModule':
    symbol = "api_management_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/api-management/service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .api_management.service import ApiManagementServiceModule
    output = ApiManagementServiceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _app_container_app(
        bicep: IO[str],
        params: 'AppContainerApp',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AppContainerAppModule':
    symbol = "app_container_app_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/container-app:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .app.container_app import AppContainerAppModule
    output = AppContainerAppModule(symbol)
    output.outputs = {
        'fqdn': Output(symbol, 'fqdn', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _app_job(
        bicep: IO[str],
        params: 'AppJob',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AppJobModule':
    symbol = "app_job_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/job:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .app.job import AppJobModule
    output = AppJobModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _app_managed_environment(
        bicep: IO[str],
        params: 'AppManagedEnvironment',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AppManagedEnvironmentModule':
    symbol = "app_managed_environment_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/managed-environment:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .app.managed_environment import AppManagedEnvironmentModule
    output = AppManagedEnvironmentModule(symbol)
    output.outputs = {
        'defaultDomain': Output(symbol, 'defaultDomain', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'staticIp': Output(symbol, 'staticIp', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _app_configuration_store(
        bicep: IO[str],
        params: 'AppConfigurationStore',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AppConfigurationStoreModule':
    symbol = "app_configuration_store_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app-configuration/configuration-store:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .app_configuration.configuration_store import AppConfigurationStoreModule
    output = AppConfigurationStoreModule(symbol)
    output.outputs = {
        'endpoint': Output(symbol, 'endpoint', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _automation_account(
        bicep: IO[str],
        params: 'AutomationAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'AutomationAccountModule':
    symbol = "automation_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/automation/automation-account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .automation.automation_account import AutomationAccountModule
    output = AutomationAccountModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _batch_account(
        bicep: IO[str],
        params: 'BatchAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'BatchAccountModule':
    symbol = "batch_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/batch/batch-account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .batch.batch_account import BatchAccountModule
    output = BatchAccountModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _cache_redis(
        bicep: IO[str],
        params: 'CacheRedis',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'CacheRedisModule':
    symbol = "cache_redis_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/cache/redis:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .cache.redis import CacheRedisModule
    output = CacheRedisModule(symbol)
    output.outputs = {
        'hostName': Output(symbol, 'hostName', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'sslPort': Output(symbol, 'sslPort', 'int'),
        'subnetResourceId': Output(symbol, 'subnetResourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _cdn_profile(
        bicep: IO[str],
        params: 'CdnProfile',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'CdnProfileModule':
    symbol = "cdn_profile_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/cdn/profile:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .cdn.profile import CdnProfileModule
    output = CdnProfileModule(symbol)
    output.outputs = {
        'endpointId': Output(symbol, 'endpointId', 'string'),
        'endpointName': Output(symbol, 'endpointName', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'profileType': Output(symbol, 'profileType', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        'uri': Output(symbol, 'uri', 'string'),
    }

    return output

def _cognitive_services_account(
        bicep: IO[str],
        params: 'CognitiveServicesAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'CognitiveServicesAccountModule':
    symbol = "cognitive_services_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/cognitive-services/account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .cognitive_services.account import CognitiveServicesAccountModule
    output = CognitiveServicesAccountModule(symbol)
    output.outputs = {
        'endpoint': Output(symbol, 'endpoint', 'string'),
        'endpoints': Output(symbol, 'endpoints', 'object'),
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _communication_service(
        bicep: IO[str],
        params: 'CommunicationService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'CommunicationServiceModule':
    symbol = "communication_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/communication/communication-service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .communication.communication_service import CommunicationServiceModule
    output = CommunicationServiceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _communication_email_service(
        bicep: IO[str],
        params: 'CommunicationEmailService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'CommunicationEmailServiceModule':
    symbol = "communication_email_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/communication/email-service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .communication.email_service import CommunicationEmailServiceModule
    output = CommunicationEmailServiceModule(symbol)
    output.outputs = {
        'domainNamess': Output(symbol, 'domainNamess', 'array'),
        'domainResourceIds': Output(symbol, 'domainResourceIds', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_availability_set(
        bicep: IO[str],
        params: 'ComputeAvailabilitySet',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeAvailabilitySetModule':
    symbol = "compute_availability_set_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/availability-set:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.availability_set import ComputeAvailabilitySetModule
    output = ComputeAvailabilitySetModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_disk(
        bicep: IO[str],
        params: 'ComputeDisk',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeDiskModule':
    symbol = "compute_disk_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/disk:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.disk import ComputeDiskModule
    output = ComputeDiskModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_disk_encryption_set(
        bicep: IO[str],
        params: 'ComputeDiskEncryptionSet',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeDiskEncryptionSetModule':
    symbol = "compute_disk_encryption_set_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/disk-encryption-set:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.disk_encryption_set import ComputeDiskEncryptionSetModule
    output = ComputeDiskEncryptionSetModule(symbol)
    output.outputs = {
        'identities': Output(symbol, 'identities', 'object'),
        'keyVaultName': Output(symbol, 'keyVaultName', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _compute_gallery(
        bicep: IO[str],
        params: 'ComputeGallery',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeGalleryModule':
    symbol = "compute_gallery_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/gallery:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.gallery import ComputeGalleryModule
    output = ComputeGalleryModule(symbol)
    output.outputs = {
        'imageResourceIds': Output(symbol, 'imageResourceIds', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_image(
        bicep: IO[str],
        params: 'ComputeImage',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeImageModule':
    symbol = "compute_image_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/image:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.image import ComputeImageModule
    output = ComputeImageModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_proximity_placement_group(
        bicep: IO[str],
        params: 'ComputeProximityPlacementGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeProximityPlacementGroupModule':
    symbol = "compute_proximity_placement_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/proximity-placement-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.proximity_placement_group import ComputeProximityPlacementGroupModule
    output = ComputeProximityPlacementGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_ssh_public_key(
        bicep: IO[str],
        params: 'ComputeSshPublicKey',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeSshPublicKeyModule':
    symbol = "compute_ssh_public_key_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/ssh-public-key:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.ssh_public_key import ComputeSshPublicKeyModule
    output = ComputeSshPublicKeyModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _compute_virtual_machine(
        bicep: IO[str],
        params: 'ComputeVirtualMachine',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.10.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeVirtualMachineModule':
    symbol = "compute_virtual_machine_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/virtual-machine:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.virtual_machine import ComputeVirtualMachineModule
    output = ComputeVirtualMachineModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _compute_virtual_machine_scale_set(
        bicep: IO[str],
        params: 'ComputeVirtualMachineScaleSet',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ComputeVirtualMachineScaleSetModule':
    symbol = "compute_virtual_machine_scale_set_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/virtual-machine-scale-set:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .compute.virtual_machine_scale_set import ComputeVirtualMachineScaleSetModule
    output = ComputeVirtualMachineScaleSetModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _consumption_budget(
        bicep: IO[str],
        params: 'ConsumptionBudget',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ConsumptionBudgetModule':
    symbol = "consumption_budget_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/consumption/budget:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .consumption.budget import ConsumptionBudgetModule
    output = ConsumptionBudgetModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'subscriptionName': Output(symbol, 'subscriptionName', 'string'),
    }

    return output

def _container_instance_container_group(
        bicep: IO[str],
        params: 'ContainerInstanceContainerGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ContainerInstanceContainerGroupModule':
    symbol = "container_instance_container_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/container-instance/container-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .container_instance.container_group import ContainerInstanceContainerGroupModule
    output = ContainerInstanceContainerGroupModule(symbol)
    output.outputs = {
        'iPv4Address': Output(symbol, 'iPv4Address', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _container_registry(
        bicep: IO[str],
        params: 'ContainerRegistry',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ContainerRegistryModule':
    symbol = "container_registry_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/container-registry/registry:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .container_registry.registry import ContainerRegistryModule
    output = ContainerRegistryModule(symbol)
    output.outputs = {
        'credentialSetsResourceIds': Output(symbol, 'credentialSetsResourceIds', 'array'),
        'credentialSetsSystemAssignedMIPrincipalIds': Output(symbol, 'credentialSetsSystemAssignedMIPrincipalIds', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'loginServer': Output(symbol, 'loginServer', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _container_service_managed_cluster(
        bicep: IO[str],
        params: 'ContainerServiceManagedCluster',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ContainerServiceManagedClusterModule':
    symbol = "container_service_managed_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/container-service/managed-cluster:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .container_service.managed_cluster import ContainerServiceManagedClusterModule
    output = ContainerServiceManagedClusterModule(symbol)
    output.outputs = {
        'addonProfiles': Output(symbol, 'addonProfiles', 'object'),
        'controlPlaneFQDN': Output(symbol, 'controlPlaneFQDN', 'string'),
        'ingressApplicationGatewayIdentityObjectId': Output(symbol, 'ingressApplicationGatewayIdentityObjectId', 'string'),
        'keyvaultIdentityClientId': Output(symbol, 'keyvaultIdentityClientId', 'string'),
        'keyvaultIdentityObjectId': Output(symbol, 'keyvaultIdentityObjectId', 'string'),
        'kubeletIdentityClientId': Output(symbol, 'kubeletIdentityClientId', 'string'),
        'kubeletIdentityObjectId': Output(symbol, 'kubeletIdentityObjectId', 'string'),
        'kubeletIdentityResourceId': Output(symbol, 'kubeletIdentityResourceId', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'oidcIssuerUrl': Output(symbol, 'oidcIssuerUrl', 'string'),
        'omsagentIdentityObjectId': Output(symbol, 'omsagentIdentityObjectId', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        'webAppRoutingIdentityObjectId': Output(symbol, 'webAppRoutingIdentityObjectId', 'string'),
    }

    return output

def _data_factory(
        bicep: IO[str],
        params: 'DataFactory',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DataFactoryModule':
    symbol = "data_factory_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/data-factory/factory:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .data_factory.factory import DataFactoryModule
    output = DataFactoryModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _data_protection_backup_vault(
        bicep: IO[str],
        params: 'DataProtectionBackupVault',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DataProtectionBackupVaultModule':
    symbol = "data_protection_backup_vault_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/data-protection/backup-vault:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .data_protection.backup_vault import DataProtectionBackupVaultModule
    output = DataProtectionBackupVaultModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _databricks_access_connector(
        bicep: IO[str],
        params: 'DatabricksAccessConnector',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DatabricksAccessConnectorModule':
    symbol = "databricks_access_connector_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/databricks/access-connector:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .databricks.access_connector import DatabricksAccessConnectorModule
    output = DatabricksAccessConnectorModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _databricks_workspace(
        bicep: IO[str],
        params: 'DatabricksWorkspace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DatabricksWorkspaceModule':
    symbol = "databricks_workspace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/databricks/workspace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .databricks.workspace import DatabricksWorkspaceModule
    output = DatabricksWorkspaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'managedResourceGroupName': Output(symbol, 'managedResourceGroupName', 'string'),
        'managedResourceGroupResourceId': Output(symbol, 'managedResourceGroupResourceId', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'storageAccountName': Output(symbol, 'storageAccountName', 'string'),
        'storageAccountResourceId': Output(symbol, 'storageAccountResourceId', 'string'),
        'storagePrivateEndpoints': Output(symbol, 'storagePrivateEndpoints', 'array'),
        'workspaceResourceId': Output(symbol, 'workspaceResourceId', 'string'),
        'workspaceUrl': Output(symbol, 'workspaceUrl', 'string'),
    }

    return output

def _db_for_my_sql_flexible_server(
        bicep: IO[str],
        params: 'DbForMySqlFlexibleServer',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DbForMySqlFlexibleServerModule':
    symbol = "db_for_my_sql_flexible_server_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/db-for-my-sql/flexible-server:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .db_for_my_sql.flexible_server import DbForMySqlFlexibleServerModule
    output = DbForMySqlFlexibleServerModule(symbol)
    output.outputs = {
        'fqdn': Output(symbol, 'fqdn', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _db_for_postgre_sql_flexible_server(
        bicep: IO[str],
        params: 'DbForPostgreSqlFlexibleServer',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DbForPostgreSqlFlexibleServerModule':
    symbol = "db_for_postgre_sql_flexible_server_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/db-for-postgre-sql/flexible-server:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .db_for_postgre_sql.flexible_server import DbForPostgreSqlFlexibleServerModule
    output = DbForPostgreSqlFlexibleServerModule(symbol)
    output.outputs = {
        'fqdn': Output(symbol, 'fqdn', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _desktop_virtualization_application_group(
        bicep: IO[str],
        params: 'DesktopVirtualizationApplicationGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DesktopVirtualizationApplicationGroupModule':
    symbol = "desktop_virtualization_application_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/desktop-virtualization/application-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .desktop_virtualization.application_group import DesktopVirtualizationApplicationGroupModule
    output = DesktopVirtualizationApplicationGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _desktop_virtualization_host_pool(
        bicep: IO[str],
        params: 'DesktopVirtualizationHostPool',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DesktopVirtualizationHostPoolModule':
    symbol = "desktop_virtualization_host_pool_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/desktop-virtualization/host-pool:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .desktop_virtualization.host_pool import DesktopVirtualizationHostPoolModule
    output = DesktopVirtualizationHostPoolModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _desktop_virtualization_scaling_plan(
        bicep: IO[str],
        params: 'DesktopVirtualizationScalingPlan',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DesktopVirtualizationScalingPlanModule':
    symbol = "desktop_virtualization_scaling_plan_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/desktop-virtualization/scaling-plan:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .desktop_virtualization.scaling_plan import DesktopVirtualizationScalingPlanModule
    output = DesktopVirtualizationScalingPlanModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _desktop_virtualization_workspace(
        bicep: IO[str],
        params: 'DesktopVirtualizationWorkspace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DesktopVirtualizationWorkspaceModule':
    symbol = "desktop_virtualization_workspace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/desktop-virtualization/workspace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .desktop_virtualization.workspace import DesktopVirtualizationWorkspaceModule
    output = DesktopVirtualizationWorkspaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _dev_ops_infrastructure_pool(
        bicep: IO[str],
        params: 'DevOpsInfrastructurePool',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DevOpsInfrastructurePoolModule':
    symbol = "dev_ops_infrastructure_pool_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/dev-ops-infrastructure/pool:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .dev_ops_infrastructure.pool import DevOpsInfrastructurePoolModule
    output = DevOpsInfrastructurePoolModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _dev_test_lab(
        bicep: IO[str],
        params: 'DevTestLab',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DevTestLabModule':
    symbol = "dev_test_lab_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/dev-test-lab/lab:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .dev_test_lab.lab import DevTestLabModule
    output = DevTestLabModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        'uniqueIdentifier': Output(symbol, 'uniqueIdentifier', 'string'),
    }

    return output

def _digital_twins_instance(
        bicep: IO[str],
        params: 'DigitalTwinsInstance',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DigitalTwinsInstanceModule':
    symbol = "digital_twins_instance_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/digital-twins/digital-twins-instance:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .digital_twins.digital_twins_instance import DigitalTwinsInstanceModule
    output = DigitalTwinsInstanceModule(symbol)
    output.outputs = {
        'hostname': Output(symbol, 'hostname', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _document_db_database_account(
        bicep: IO[str],
        params: 'DocumentDbDatabaseAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.10.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DocumentDbDatabaseAccountModule':
    symbol = "document_db_database_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/document-db/database-account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .document_db.database_account import DocumentDbDatabaseAccountModule
    output = DocumentDbDatabaseAccountModule(symbol)
    output.outputs = {
        'endpoint': Output(symbol, 'endpoint', 'string'),
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _document_db_mongo_cluster(
        bicep: IO[str],
        params: 'DocumentDbMongoCluster',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'DocumentDbMongoClusterModule':
    symbol = "document_db_mongo_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/document-db/mongo-cluster:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .document_db.mongo_cluster import DocumentDbMongoClusterModule
    output = DocumentDbMongoClusterModule(symbol)
    output.outputs = {
        'connectionStringKey': Output(symbol, 'connectionStringKey', 'string'),
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'firewallRules': Output(symbol, 'firewallRules', 'array'),
        'mongoClusterResourceId': Output(symbol, 'mongoClusterResourceId', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _elastic_san(
        bicep: IO[str],
        params: 'ElasticSan',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ElasticSanModule':
    symbol = "elastic_san_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/elastic-san/elastic-san:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .elastic_san.elastic_san import ElasticSanModule
    output = ElasticSanModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'volumeGroups': Output(symbol, 'volumeGroups', 'array'),
    }

    return output

def _event_grid_domain(
        bicep: IO[str],
        params: 'EventGridDomain',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'EventGridDomainModule':
    symbol = "event_grid_domain_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-grid/domain:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .event_grid.domain import EventGridDomainModule
    output = EventGridDomainModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _event_grid_namespace(
        bicep: IO[str],
        params: 'EventGridNamespace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'EventGridNamespaceModule':
    symbol = "event_grid_namespace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-grid/namespace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .event_grid.namespace import EventGridNamespaceModule
    output = EventGridNamespaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        'topicResourceIds': Output(symbol, 'topicResourceIds', 'array'),
    }

    return output

def _event_grid_system_topic(
        bicep: IO[str],
        params: 'EventGridSystemTopic',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'EventGridSystemTopicModule':
    symbol = "event_grid_system_topic_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-grid/system-topic:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .event_grid.system_topic import EventGridSystemTopicModule
    output = EventGridSystemTopicModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _event_grid_topic(
        bicep: IO[str],
        params: 'EventGridTopic',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'EventGridTopicModule':
    symbol = "event_grid_topic_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-grid/topic:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .event_grid.topic import EventGridTopicModule
    output = EventGridTopicModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _event_hub_namespace(
        bicep: IO[str],
        params: 'EventHubNamespace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'EventHubNamespaceModule':
    symbol = "event_hub_namespace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-hub/namespace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .event_hub.namespace import EventHubNamespaceModule
    output = EventHubNamespaceModule(symbol)
    output.outputs = {
        'eventHubResourceIds': Output(symbol, 'eventHubResourceIds', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _fabric_capacity(
        bicep: IO[str],
        params: 'FabricCapacity',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'FabricCapacityModule':
    symbol = "fabric_capacity_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/fabric/capacity:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .fabric.capacity import FabricCapacityModule
    output = FabricCapacityModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _hybrid_compute_machine(
        bicep: IO[str],
        params: 'HybridComputeMachine',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'HybridComputeMachineModule':
    symbol = "hybrid_compute_machine_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/hybrid-compute/machine:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .hybrid_compute.machine import HybridComputeMachineModule
    output = HybridComputeMachineModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _insights_action_group(
        bicep: IO[str],
        params: 'InsightsActionGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsActionGroupModule':
    symbol = "insights_action_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/action-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.action_group import InsightsActionGroupModule
    output = InsightsActionGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_activity_log_alert(
        bicep: IO[str],
        params: 'InsightsActivityLogAlert',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsActivityLogAlertModule':
    symbol = "insights_activity_log_alert_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/activity-log-alert:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.activity_log_alert import InsightsActivityLogAlertModule
    output = InsightsActivityLogAlertModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_component(
        bicep: IO[str],
        params: 'InsightsComponent',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsComponentModule':
    symbol = "insights_component_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/component:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.component import InsightsComponentModule
    output = InsightsComponentModule(symbol)
    output.outputs = {
        'applicationId': Output(symbol, 'applicationId', 'string'),
        'connectionString': Output(symbol, 'connectionString', 'string'),
        'instrumentationKey': Output(symbol, 'instrumentationKey', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_data_collection_endpoint(
        bicep: IO[str],
        params: 'InsightsDataCollectionEndpoint',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsDataCollectionEndpointModule':
    symbol = "insights_data_collection_endpoint_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/data-collection-endpoint:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.data_collection_endpoint import InsightsDataCollectionEndpointModule
    output = InsightsDataCollectionEndpointModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_data_collection_rule(
        bicep: IO[str],
        params: 'InsightsDataCollectionRule',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsDataCollectionRuleModule':
    symbol = "insights_data_collection_rule_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/data-collection-rule:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.data_collection_rule import InsightsDataCollectionRuleModule
    output = InsightsDataCollectionRuleModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _insights_diagnostic_setting(
        bicep: IO[str],
        params: 'InsightsDiagnosticSetting',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsDiagnosticSettingModule':
    symbol = "insights_diagnostic_setting_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/diagnostic-setting:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.diagnostic_setting import InsightsDiagnosticSettingModule
    output = InsightsDiagnosticSettingModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'subscriptionName': Output(symbol, 'subscriptionName', 'string'),
    }

    return output

def _insights_metric_alert(
        bicep: IO[str],
        params: 'InsightsMetricAlert',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsMetricAlertModule':
    symbol = "insights_metric_alert_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/metric-alert:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.metric_alert import InsightsMetricAlertModule
    output = InsightsMetricAlertModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_private_link_scope(
        bicep: IO[str],
        params: 'InsightsPrivateLinkScope',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsPrivateLinkScopeModule':
    symbol = "insights_private_link_scope_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/private-link-scope:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.private_link_scope import InsightsPrivateLinkScopeModule
    output = InsightsPrivateLinkScopeModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_scheduled_query_rule(
        bicep: IO[str],
        params: 'InsightsScheduledQueryRule',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsScheduledQueryRuleModule':
    symbol = "insights_scheduled_query_rule_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/scheduled-query-rule:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.scheduled_query_rule import InsightsScheduledQueryRuleModule
    output = InsightsScheduledQueryRuleModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _insights_webtest(
        bicep: IO[str],
        params: 'InsightsWebtest',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'InsightsWebtestModule':
    symbol = "insights_webtest_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/webtest:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .insights.webtest import InsightsWebtestModule
    output = InsightsWebtestModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _key_vault(
        bicep: IO[str],
        params: 'KeyVault',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'KeyVaultModule':
    symbol = "key_vault_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/key-vault/vault:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .key_vault.vault import KeyVaultModule
    output = KeyVaultModule(symbol)
    output.outputs = {
        'keys': Output(symbol, 'keys', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'secrets': Output(symbol, 'secrets', 'array'),
        'uri': Output(symbol, 'uri', 'string'),
    }

    return output

def _kubernetes_configuration_extension(
        bicep: IO[str],
        params: 'KubernetesConfigurationExtension',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'KubernetesConfigurationExtensionModule':
    symbol = "kubernetes_configuration_extension_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/kubernetes-configuration/extension:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .kubernetes_configuration.extension import KubernetesConfigurationExtensionModule
    output = KubernetesConfigurationExtensionModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _kubernetes_configuration_flux_configuration(
        bicep: IO[str],
        params: 'KubernetesConfigurationFluxConfiguration',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'KubernetesConfigurationFluxConfigurationModule':
    symbol = "kubernetes_configuration_flux_configuration_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/kubernetes-configuration/flux-configuration:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .kubernetes_configuration.flux_configuration import KubernetesConfigurationFluxConfigurationModule
    output = KubernetesConfigurationFluxConfigurationModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _kusto_cluster(
        bicep: IO[str],
        params: 'KustoCluster',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'KustoClusterModule':
    symbol = "kusto_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/kusto/cluster:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .kusto.cluster import KustoClusterModule
    output = KustoClusterModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _load_test_service_load_test(
        bicep: IO[str],
        params: 'LoadTestServiceLoadTest',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'LoadTestServiceLoadTestModule':
    symbol = "load_test_service_load_test_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/load-test-service/load-test:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .load_test_service.load_test import LoadTestServiceLoadTestModule
    output = LoadTestServiceLoadTestModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _logic_workflow(
        bicep: IO[str],
        params: 'LogicWorkflow',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'LogicWorkflowModule':
    symbol = "logic_workflow_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/logic/workflow:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .logic.workflow import LogicWorkflowModule
    output = LogicWorkflowModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _machine_learning_services_workspace(
        bicep: IO[str],
        params: 'MachineLearningServicesWorkspace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'MachineLearningServicesWorkspaceModule':
    symbol = "machine_learning_services_workspace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/machine-learning-services/workspace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .machine_learning_services.workspace import MachineLearningServicesWorkspaceModule
    output = MachineLearningServicesWorkspaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _maintenance_configuration(
        bicep: IO[str],
        params: 'MaintenanceConfiguration',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'MaintenanceConfigurationModule':
    symbol = "maintenance_configuration_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/maintenance/maintenance-configuration:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .maintenance.maintenance_configuration import MaintenanceConfigurationModule
    output = MaintenanceConfigurationModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _managed_identity_user_assigned_identity(
        bicep: IO[str],
        params: 'ManagedIdentityUserAssignedIdentity',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ManagedIdentityUserAssignedIdentityModule':
    symbol = "managed_identity_user_assigned_identity_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/managed-identity/user-assigned-identity:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .managed_identity.user_assigned_identity import ManagedIdentityUserAssignedIdentityModule
    output = ManagedIdentityUserAssignedIdentityModule(symbol)
    output.outputs = {
        'clientId': Output(symbol, 'clientId', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'principalId': Output(symbol, 'principalId', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _management_group(
        bicep: IO[str],
        params: 'ManagementGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ManagementGroupModule':
    symbol = "management_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/management/management-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .management.management_group import ManagementGroupModule
    output = ManagementGroupModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _net_app_account(
        bicep: IO[str],
        params: 'NetAppAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetAppAccountModule':
    symbol = "net_app_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/net-app/net-app-account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .net_app.net_app_account import NetAppAccountModule
    output = NetAppAccountModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'volumeResourceId': Output(symbol, 'volumeResourceId', 'string'),
    }

    return output

def _network_application_gateway(
        bicep: IO[str],
        params: 'NetworkApplicationGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkApplicationGatewayModule':
    symbol = "network_application_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/application-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.application_gateway import NetworkApplicationGatewayModule
    output = NetworkApplicationGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_application_gateway_web_application_firewall_policy(
        bicep: IO[str],
        params: 'NetworkApplicationGatewayWebApplicationFirewallPolicy',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkApplicationGatewayWebApplicationFirewallPolicyModule':
    symbol = "network_application_gateway_web_application_firewall_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/application-gateway-web-application-firewall-policy:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.application_gateway_web_application_firewall_policy import NetworkApplicationGatewayWebApplicationFirewallPolicyModule
    output = NetworkApplicationGatewayWebApplicationFirewallPolicyModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_application_security_group(
        bicep: IO[str],
        params: 'NetworkApplicationSecurityGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkApplicationSecurityGroupModule':
    symbol = "network_application_security_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/application-security-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.application_security_group import NetworkApplicationSecurityGroupModule
    output = NetworkApplicationSecurityGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_azure_firewall(
        bicep: IO[str],
        params: 'NetworkAzureFirewall',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkAzureFirewallModule':
    symbol = "network_azure_firewall_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/azure-firewall:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.azure_firewall import NetworkAzureFirewallModule
    output = NetworkAzureFirewallModule(symbol)
    output.outputs = {
        'applicationRuleCollections': Output(symbol, 'applicationRuleCollections', 'array'),
        'ipConfAzureFirewallSubnet': Output(symbol, 'ipConfAzureFirewallSubnet', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'natRuleCollections': Output(symbol, 'natRuleCollections', 'array'),
        'networkRuleCollections': Output(symbol, 'networkRuleCollections', 'array'),
        'privateIp': Output(symbol, 'privateIp', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_bastion_host(
        bicep: IO[str],
        params: 'NetworkBastionHost',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkBastionHostModule':
    symbol = "network_bastion_host_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/bastion-host:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.bastion_host import NetworkBastionHostModule
    output = NetworkBastionHostModule(symbol)
    output.outputs = {
        'ipConfAzureBastionSubnet': Output(symbol, 'ipConfAzureBastionSubnet', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_connection(
        bicep: IO[str],
        params: 'NetworkConnection',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkConnectionModule':
    symbol = "network_connection_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/connection:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.connection import NetworkConnectionModule
    output = NetworkConnectionModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_ddos_protection_plan(
        bicep: IO[str],
        params: 'NetworkDdosProtectionPlan',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkDdosProtectionPlanModule':
    symbol = "network_ddos_protection_plan_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/ddos-protection-plan:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.ddos_protection_plan import NetworkDdosProtectionPlanModule
    output = NetworkDdosProtectionPlanModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_dns_forwarding_ruleset(
        bicep: IO[str],
        params: 'NetworkDnsForwardingRuleset',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkDnsForwardingRulesetModule':
    symbol = "network_dns_forwarding_ruleset_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/dns-forwarding-ruleset:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.dns_forwarding_ruleset import NetworkDnsForwardingRulesetModule
    output = NetworkDnsForwardingRulesetModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_dns_resolver(
        bicep: IO[str],
        params: 'NetworkDnsResolver',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkDnsResolverModule':
    symbol = "network_dns_resolver_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/dns-resolver:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.dns_resolver import NetworkDnsResolverModule
    output = NetworkDnsResolverModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_dns_zone(
        bicep: IO[str],
        params: 'NetworkDnsZone',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkDnsZoneModule':
    symbol = "network_dns_zone_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/dns-zone:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.dns_zone import NetworkDnsZoneModule
    output = NetworkDnsZoneModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'nameServers': Output(symbol, 'nameServers', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_express_route_circuit(
        bicep: IO[str],
        params: 'NetworkExpressRouteCircuit',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkExpressRouteCircuitModule':
    symbol = "network_express_route_circuit_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/express-route-circuit:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.express_route_circuit import NetworkExpressRouteCircuitModule
    output = NetworkExpressRouteCircuitModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'serviceKey': Output(symbol, 'serviceKey', 'string'),
    }

    return output

def _network_express_route_gateway(
        bicep: IO[str],
        params: 'NetworkExpressRouteGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkExpressRouteGatewayModule':
    symbol = "network_express_route_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/express-route-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.express_route_gateway import NetworkExpressRouteGatewayModule
    output = NetworkExpressRouteGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_firewall_policy(
        bicep: IO[str],
        params: 'NetworkFirewallPolicy',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkFirewallPolicyModule':
    symbol = "network_firewall_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/firewall-policy:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.firewall_policy import NetworkFirewallPolicyModule
    output = NetworkFirewallPolicyModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_front_door(
        bicep: IO[str],
        params: 'NetworkFrontDoor',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkFrontDoorModule':
    symbol = "network_front_door_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/front-door:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.front_door import NetworkFrontDoorModule
    output = NetworkFrontDoorModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_front_door_web_application_firewall_policy(
        bicep: IO[str],
        params: 'NetworkFrontDoorWebApplicationFirewallPolicy',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkFrontDoorWebApplicationFirewallPolicyModule':
    symbol = "network_front_door_web_application_firewall_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/front-door-web-application-firewall-policy:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.front_door_web_application_firewall_policy import NetworkFrontDoorWebApplicationFirewallPolicyModule
    output = NetworkFrontDoorWebApplicationFirewallPolicyModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_ip_group(
        bicep: IO[str],
        params: 'NetworkIpGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkIpGroupModule':
    symbol = "network_ip_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/ip-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.ip_group import NetworkIpGroupModule
    output = NetworkIpGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_load_balancer(
        bicep: IO[str],
        params: 'NetworkLoadBalancer',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkLoadBalancerModule':
    symbol = "network_load_balancer_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/load-balancer:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.load_balancer import NetworkLoadBalancerModule
    output = NetworkLoadBalancerModule(symbol)
    output.outputs = {
        'backendpools': Output(symbol, 'backendpools', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_local_network_gateway(
        bicep: IO[str],
        params: 'NetworkLocalNetworkGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkLocalNetworkGatewayModule':
    symbol = "network_local_network_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/local-network-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.local_network_gateway import NetworkLocalNetworkGatewayModule
    output = NetworkLocalNetworkGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_nat_gateway(
        bicep: IO[str],
        params: 'NetworkNatGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '1.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkNatGatewayModule':
    symbol = "network_nat_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/nat-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.nat_gateway import NetworkNatGatewayModule
    output = NetworkNatGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_interface(
        bicep: IO[str],
        params: 'NetworkInterface',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkInterfaceModule':
    symbol = "network_interface_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/network-interface:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.network_interface import NetworkInterfaceModule
    output = NetworkInterfaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_manager(
        bicep: IO[str],
        params: 'NetworkManager',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkManagerModule':
    symbol = "network_manager_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/network-manager:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.network_manager import NetworkManagerModule
    output = NetworkManagerModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_security_group(
        bicep: IO[str],
        params: 'NetworkSecurityGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkSecurityGroupModule':
    symbol = "network_security_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/network-security-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.network_security_group import NetworkSecurityGroupModule
    output = NetworkSecurityGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_watcher(
        bicep: IO[str],
        params: 'NetworkWatcher',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkWatcherModule':
    symbol = "network_watcher_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/network-watcher:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.network_watcher import NetworkWatcherModule
    output = NetworkWatcherModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_p2s_vpn_gateway(
        bicep: IO[str],
        params: 'NetworkP2SVpnGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkP2SVpnGatewayModule':
    symbol = "network_p2s_vpn_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/p2s-vpn-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.p2s_vpn_gateway import NetworkP2SVpnGatewayModule
    output = NetworkP2SVpnGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_private_dns_zone(
        bicep: IO[str],
        params: 'NetworkPrivateDnsZone',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkPrivateDnsZoneModule':
    symbol = "network_private_dns_zone_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/private-dns-zone:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.private_dns_zone import NetworkPrivateDnsZoneModule
    output = NetworkPrivateDnsZoneModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_private_endpoint(
        bicep: IO[str],
        params: 'NetworkPrivateEndpoint',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkPrivateEndpointModule':
    symbol = "network_private_endpoint_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/private-endpoint:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.private_endpoint import NetworkPrivateEndpointModule
    output = NetworkPrivateEndpointModule(symbol)
    output.outputs = {
        'customDnsConfig': Output(symbol, 'customDnsConfig', 'array'),
        'groupId': Output(symbol, 'groupId', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'networkInterfaceResourceIds': Output(symbol, 'networkInterfaceResourceIds', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_private_link_service(
        bicep: IO[str],
        params: 'NetworkPrivateLinkService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkPrivateLinkServiceModule':
    symbol = "network_private_link_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/private-link-service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.private_link_service import NetworkPrivateLinkServiceModule
    output = NetworkPrivateLinkServiceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_public_ip_address(
        bicep: IO[str],
        params: 'NetworkPublicIpAddress',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.7.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkPublicIpAddressModule':
    symbol = "network_public_ip_address_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/public-ip-address:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.public_ip_address import NetworkPublicIpAddressModule
    output = NetworkPublicIpAddressModule(symbol)
    output.outputs = {
        'ipAddress': Output(symbol, 'ipAddress', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_public_ip_prefix(
        bicep: IO[str],
        params: 'NetworkPublicIpPrefix',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkPublicIpPrefixModule':
    symbol = "network_public_ip_prefix_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/public-ip-prefix:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.public_ip_prefix import NetworkPublicIpPrefixModule
    output = NetworkPublicIpPrefixModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_route_table(
        bicep: IO[str],
        params: 'NetworkRouteTable',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkRouteTableModule':
    symbol = "network_route_table_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/route-table:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.route_table import NetworkRouteTableModule
    output = NetworkRouteTableModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_service_endpoint_policy(
        bicep: IO[str],
        params: 'NetworkServiceEndpointPolicy',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkServiceEndpointPolicyModule':
    symbol = "network_service_endpoint_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/service-endpoint-policy:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.service_endpoint_policy import NetworkServiceEndpointPolicyModule
    output = NetworkServiceEndpointPolicyModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_trafficmanagerprofile(
        bicep: IO[str],
        params: 'NetworkTrafficmanagerprofile',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkTrafficmanagerprofileModule':
    symbol = "network_trafficmanagerprofile_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/trafficmanagerprofile:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.trafficmanagerprofile import NetworkTrafficmanagerprofileModule
    output = NetworkTrafficmanagerprofileModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_virtual_hub(
        bicep: IO[str],
        params: 'NetworkVirtualHub',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVirtualHubModule':
    symbol = "network_virtual_hub_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/virtual-hub:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.virtual_hub import NetworkVirtualHubModule
    output = NetworkVirtualHubModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_virtual_network_gateway(
        bicep: IO[str],
        params: 'NetworkVirtualNetworkGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVirtualNetworkGatewayModule':
    symbol = "network_virtual_network_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/virtual-network-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.virtual_network_gateway import NetworkVirtualNetworkGatewayModule
    output = NetworkVirtualNetworkGatewayModule(symbol)
    output.outputs = {
        'activeActive': Output(symbol, 'activeActive', 'bool'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_virtual_wan(
        bicep: IO[str],
        params: 'NetworkVirtualWan',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVirtualWanModule':
    symbol = "network_virtual_wan_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/virtual-wan:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.virtual_wan import NetworkVirtualWanModule
    output = NetworkVirtualWanModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_vpn_gateway(
        bicep: IO[str],
        params: 'NetworkVpnGateway',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVpnGatewayModule':
    symbol = "network_vpn_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-gateway:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.vpn_gateway import NetworkVpnGatewayModule
    output = NetworkVpnGatewayModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_vpn_server_configuration(
        bicep: IO[str],
        params: 'NetworkVpnServerConfiguration',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVpnServerConfigurationModule':
    symbol = "network_vpn_server_configuration_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-server-configuration:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.vpn_server_configuration import NetworkVpnServerConfigurationModule
    output = NetworkVpnServerConfigurationModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _network_vpn_site(
        bicep: IO[str],
        params: 'NetworkVpnSite',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'NetworkVpnSiteModule':
    symbol = "network_vpn_site_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-site:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .network.vpn_site import NetworkVpnSiteModule
    output = NetworkVpnSiteModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _operational_insights_workspace(
        bicep: IO[str],
        params: 'OperationalInsightsWorkspace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'OperationalInsightsWorkspaceModule':
    symbol = "operational_insights_workspace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/operational-insights/workspace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .operational_insights.workspace import OperationalInsightsWorkspaceModule
    output = OperationalInsightsWorkspaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'logAnalyticsWorkspaceId': Output(symbol, 'logAnalyticsWorkspaceId', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _operations_management_solution(
        bicep: IO[str],
        params: 'OperationsManagementSolution',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'OperationsManagementSolutionModule':
    symbol = "operations_management_solution_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/operations-management/solution:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .operations_management.solution import OperationsManagementSolutionModule
    output = OperationsManagementSolutionModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _portal_dashboard(
        bicep: IO[str],
        params: 'PortalDashboard',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'PortalDashboardModule':
    symbol = "portal_dashboard_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/portal/dashboard:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .portal.dashboard import PortalDashboardModule
    output = PortalDashboardModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _power_bi_dedicated_capacity(
        bicep: IO[str],
        params: 'PowerBiDedicatedCapacity',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'PowerBiDedicatedCapacityModule':
    symbol = "power_bi_dedicated_capacity_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/power-bi-dedicated/capacity:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .power_bi_dedicated.capacity import PowerBiDedicatedCapacityModule
    output = PowerBiDedicatedCapacityModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _purview_account(
        bicep: IO[str],
        params: 'PurviewAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'PurviewAccountModule':
    symbol = "purview_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/purview/account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .purview.account import PurviewAccountModule
    output = PurviewAccountModule(symbol)
    output.outputs = {
        'accountPrivateEndpoints': Output(symbol, 'accountPrivateEndpoints', 'array'),
        'eventHubPrivateEndpoints': Output(symbol, 'eventHubPrivateEndpoints', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'managedEventHubId': Output(symbol, 'managedEventHubId', 'string'),
        'managedResourceGroupId': Output(symbol, 'managedResourceGroupId', 'string'),
        'managedResourceGroupName': Output(symbol, 'managedResourceGroupName', 'string'),
        'managedStorageAccountId': Output(symbol, 'managedStorageAccountId', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'portalPrivateEndpoints': Output(symbol, 'portalPrivateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'storageBlobPrivateEndpoints': Output(symbol, 'storageBlobPrivateEndpoints', 'array'),
        'storageQueuePrivateEndpoints': Output(symbol, 'storageQueuePrivateEndpoints', 'array'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _recovery_services_vault(
        bicep: IO[str],
        params: 'RecoveryServicesVault',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'RecoveryServicesVaultModule':
    symbol = "recovery_services_vault_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/recovery-services/vault:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .recovery_services.vault import RecoveryServicesVaultModule
    output = RecoveryServicesVaultModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _resource_graph_query(
        bicep: IO[str],
        params: 'ResourceGraphQuery',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ResourceGraphQueryModule':
    symbol = "resource_graph_query_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/resource-graph/query:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .resource_graph.query import ResourceGraphQueryModule
    output = ResourceGraphQueryModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _resources_deployment_script(
        bicep: IO[str],
        params: 'ResourcesDeploymentScript',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ResourcesDeploymentScriptModule':
    symbol = "resources_deployment_script_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/resources/deployment-script:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .resources.deployment_script import ResourcesDeploymentScriptModule
    output = ResourcesDeploymentScriptModule(symbol)
    output.outputs = {
        'deploymentScriptLogs': Output(symbol, 'deploymentScriptLogs', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'outputs': Output(symbol, 'outputs', 'object'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _resource_group(
        bicep: IO[str],
        params: 'ResourceGroup',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ResourceGroupModule':
    symbol = "resource_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/resources/resource-group:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .resources.resource_group import ResourceGroupModule
    output = ResourceGroupModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _search_service(
        bicep: IO[str],
        params: 'SearchService',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'SearchServiceModule':
    symbol = "search_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/search/search-service:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .search.search_service import SearchServiceModule
    output = SearchServiceModule(symbol)
    output.outputs = {
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _service_bus_namespace(
        bicep: IO[str],
        params: 'ServiceBusNamespace',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.10.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ServiceBusNamespaceModule':
    symbol = "service_bus_namespace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/service-bus/namespace:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .service_bus.namespace import ServiceBusNamespaceModule
    output = ServiceBusNamespaceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _service_fabric_cluster(
        bicep: IO[str],
        params: 'ServiceFabricCluster',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ServiceFabricClusterModule':
    symbol = "service_fabric_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/service-fabric/cluster:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .service_fabric.cluster import ServiceFabricClusterModule
    output = ServiceFabricClusterModule(symbol)
    output.outputs = {
        'endpoint': Output(symbol, 'endpoint', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _service_networking_traffic_controller(
        bicep: IO[str],
        params: 'ServiceNetworkingTrafficController',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'ServiceNetworkingTrafficControllerModule':
    symbol = "service_networking_traffic_controller_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/service-networking/traffic-controller:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .service_networking.traffic_controller import ServiceNetworkingTrafficControllerModule
    output = ServiceNetworkingTrafficControllerModule(symbol)
    output.outputs = {
        'associations': Output(symbol, 'associations', 'array'),
        'configurationEndpoints': Output(symbol, 'configurationEndpoints', 'array'),
        'frontends': Output(symbol, 'frontends', 'array'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _sql_instance_pool(
        bicep: IO[str],
        params: 'SqlInstancePool',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'SqlInstancePoolModule':
    symbol = "sql_instance_pool_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/sql/instance-pool:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .sql.instance_pool import SqlInstancePoolModule
    output = SqlInstancePoolModule(symbol)
    output.outputs = {
        'instancePoolLocation': Output(symbol, 'instancePoolLocation', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _sql_managed_instance(
        bicep: IO[str],
        params: 'SqlManagedInstance',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'SqlManagedInstanceModule':
    symbol = "sql_managed_instance_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/sql/managed-instance:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .sql.managed_instance import SqlManagedInstanceModule
    output = SqlManagedInstanceModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _sql_server(
        bicep: IO[str],
        params: 'SqlServer',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'SqlServerModule':
    symbol = "sql_server_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/sql/server:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .sql.server import SqlServerModule
    output = SqlServerModule(symbol)
    output.outputs = {
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'fullyQualifiedDomainName': Output(symbol, 'fullyQualifiedDomainName', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _storage_account(
        bicep: IO[str],
        params: 'StorageAccount',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.14.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'StorageAccountModule':
    symbol = "storage_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/storage/storage-account:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .storage.storage_account import StorageAccountModule
    output = StorageAccountModule(symbol)
    output.outputs = {
        'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'primaryBlobEndpoint': Output(symbol, 'primaryBlobEndpoint', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'serviceEndpoints': Output(symbol, 'serviceEndpoints', 'object'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _virtual_machine_image_template(
        bicep: IO[str],
        params: 'VirtualMachineImageTemplate',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'VirtualMachineImageTemplateModule':
    symbol = "virtual_machine_image_template_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/virtual-machine-images/image-template:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .virtual_machine_images.image_template import VirtualMachineImageTemplateModule
    output = VirtualMachineImageTemplateModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'namePrefix': Output(symbol, 'namePrefix', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'runThisCommand': Output(symbol, 'runThisCommand', 'string'),
    }

    return output

def _web_hosting_environment(
        bicep: IO[str],
        params: 'WebHostingEnvironment',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'WebHostingEnvironmentModule':
    symbol = "web_hosting_environment_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/web/hosting-environment:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .web.hosting_environment import WebHostingEnvironmentModule
    output = WebHostingEnvironmentModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _web_serverfarm(
        bicep: IO[str],
        params: 'WebServerfarm',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'WebServerfarmModule':
    symbol = "web_serverfarm_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/web/serverfarm:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .web.serverfarm import WebServerfarmModule
    output = WebServerfarmModule(symbol)
    output.outputs = {
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output

def _web_site(
        bicep: IO[str],
        params: 'WebSite',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.12.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'WebSiteModule':
    symbol = "web_site_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/web/site:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .web.site import WebSiteModule
    output = WebSiteModule(symbol)
    output.outputs = {
        'customDomainVerificationId': Output(symbol, 'customDomainVerificationId', 'string'),
        'defaultHostname': Output(symbol, 'defaultHostname', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'slotPrivateEndpoints': Output(symbol, 'slotPrivateEndpoints', 'array'),
        'slotResourceIds': Output(symbol, 'slotResourceIds', 'array'),
        'slots': Output(symbol, 'slots', 'array'),
        'slotSystemAssignedMIPrincipalIds': Output(symbol, 'slotSystemAssignedMIPrincipalIds', 'array'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output

def _web_static_site(
        bicep: IO[str],
        params: 'WebStaticSite',
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'WebStaticSiteModule':
    symbol = "web_static_site_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/web/static-site:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")

    from .web.static_site import WebStaticSiteModule
    output = WebStaticSiteModule(symbol)
    output.outputs = {
        'defaultHostname': Output(symbol, 'defaultHostname', 'string'),
        'location': Output(symbol, 'location', 'string'),
        'name': Output(symbol, 'name', 'string'),
        'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
        'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
    }

    return output
class _AddResourceMixin:
    bicep: IO[str]

    @overload
    def add(
            self,
            resource: Literal['aad_domain_service'],
            params: 'AadDomainService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AadDomainServiceModule':
        """Deploy AadDomainService resource.

        :param resource: The name of the resource to deploy: 'aad_domain_service'
        :paramtype resource: ~typing.Literal['aad_domain_service']
        :param params: The properties of the aad_domain_service resource.
        :paramtype params: ~bicepbuilder.resources.aad.domain_service.AadDomainService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AadDomainService resource.
        :rtype: ~bicepbuilder.resources.aad.domain_service.AadDomainServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['alerts_management_action_rule'],
            params: 'AlertsManagementActionRule',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AlertsManagementActionRuleModule':
        """Deploy AlertsManagementActionRule resource.

        :param resource: The name of the resource to deploy: 'alerts_management_action_rule'
        :paramtype resource: ~typing.Literal['alerts_management_action_rule']
        :param params: The properties of the alerts_management_action_rule resource.
        :paramtype params: ~bicepbuilder.resources.alerts_management.action_rule.AlertsManagementActionRule
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AlertsManagementActionRule resource.
        :rtype: ~bicepbuilder.resources.alerts_management.action_rule.AlertsManagementActionRuleModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['api_management_service'],
            params: 'ApiManagementService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ApiManagementServiceModule':
        """Deploy ApiManagementService resource.

        :param resource: The name of the resource to deploy: 'api_management_service'
        :paramtype resource: ~typing.Literal['api_management_service']
        :param params: The properties of the api_management_service resource.
        :paramtype params: ~bicepbuilder.resources.api_management.service.ApiManagementService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ApiManagementService resource.
        :rtype: ~bicepbuilder.resources.api_management.service.ApiManagementServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['app_container_app'],
            params: 'AppContainerApp',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AppContainerAppModule':
        """Deploy AppContainerApp resource.

        :param resource: The name of the resource to deploy: 'app_container_app'
        :paramtype resource: ~typing.Literal['app_container_app']
        :param params: The properties of the app_container_app resource.
        :paramtype params: ~bicepbuilder.resources.app.container_app.AppContainerApp
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.11.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AppContainerApp resource.
        :rtype: ~bicepbuilder.resources.app.container_app.AppContainerAppModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['app_job'],
            params: 'AppJob',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AppJobModule':
        """Deploy AppJob resource.

        :param resource: The name of the resource to deploy: 'app_job'
        :paramtype resource: ~typing.Literal['app_job']
        :param params: The properties of the app_job resource.
        :paramtype params: ~bicepbuilder.resources.app.job.AppJob
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AppJob resource.
        :rtype: ~bicepbuilder.resources.app.job.AppJobModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['app_managed_environment'],
            params: 'AppManagedEnvironment',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AppManagedEnvironmentModule':
        """Deploy AppManagedEnvironment resource.

        :param resource: The name of the resource to deploy: 'app_managed_environment'
        :paramtype resource: ~typing.Literal['app_managed_environment']
        :param params: The properties of the app_managed_environment resource.
        :paramtype params: ~bicepbuilder.resources.app.managed_environment.AppManagedEnvironment
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.8.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AppManagedEnvironment resource.
        :rtype: ~bicepbuilder.resources.app.managed_environment.AppManagedEnvironmentModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['app_configuration_store'],
            params: 'AppConfigurationStore',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AppConfigurationStoreModule':
        """Deploy AppConfigurationStore resource.

        :param resource: The name of the resource to deploy: 'app_configuration_store'
        :paramtype resource: ~typing.Literal['app_configuration_store']
        :param params: The properties of the app_configuration_store resource.
        :paramtype params: ~bicepbuilder.resources.app_configuration.configuration_store.AppConfigurationStore
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AppConfigurationStore resource.
        :rtype: ~bicepbuilder.resources.app_configuration.configuration_store.AppConfigurationStoreModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['automation_account'],
            params: 'AutomationAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'AutomationAccountModule':
        """Deploy AutomationAccount resource.

        :param resource: The name of the resource to deploy: 'automation_account'
        :paramtype resource: ~typing.Literal['automation_account']
        :param params: The properties of the automation_account resource.
        :paramtype params: ~bicepbuilder.resources.automation.automation_account.AutomationAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.11.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the AutomationAccount resource.
        :rtype: ~bicepbuilder.resources.automation.automation_account.AutomationAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['batch_account'],
            params: 'BatchAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'BatchAccountModule':
        """Deploy BatchAccount resource.

        :param resource: The name of the resource to deploy: 'batch_account'
        :paramtype resource: ~typing.Literal['batch_account']
        :param params: The properties of the batch_account resource.
        :paramtype params: ~bicepbuilder.resources.batch.batch_account.BatchAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the BatchAccount resource.
        :rtype: ~bicepbuilder.resources.batch.batch_account.BatchAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['cache_redis'],
            params: 'CacheRedis',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'CacheRedisModule':
        """Deploy CacheRedis resource.

        :param resource: The name of the resource to deploy: 'cache_redis'
        :paramtype resource: ~typing.Literal['cache_redis']
        :param params: The properties of the cache_redis resource.
        :paramtype params: ~bicepbuilder.resources.cache.redis.CacheRedis
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.8.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the CacheRedis resource.
        :rtype: ~bicepbuilder.resources.cache.redis.CacheRedisModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['cdn_profile'],
            params: 'CdnProfile',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'CdnProfileModule':
        """Deploy CdnProfile resource.

        :param resource: The name of the resource to deploy: 'cdn_profile'
        :paramtype resource: ~typing.Literal['cdn_profile']
        :param params: The properties of the cdn_profile resource.
        :paramtype params: ~bicepbuilder.resources.cdn.profile.CdnProfile
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.8.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the CdnProfile resource.
        :rtype: ~bicepbuilder.resources.cdn.profile.CdnProfileModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['cognitive_services_account'],
            params: 'CognitiveServicesAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'CognitiveServicesAccountModule':
        """Deploy CognitiveServicesAccount resource.

        :param resource: The name of the resource to deploy: 'cognitive_services_account'
        :paramtype resource: ~typing.Literal['cognitive_services_account']
        :param params: The properties of the cognitive_services_account resource.
        :paramtype params: ~bicepbuilder.resources.cognitive_services.account.CognitiveServicesAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the CognitiveServicesAccount resource.
        :rtype: ~bicepbuilder.resources.cognitive_services.account.CognitiveServicesAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['communication_service'],
            params: 'CommunicationService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'CommunicationServiceModule':
        """Deploy CommunicationService resource.

        :param resource: The name of the resource to deploy: 'communication_service'
        :paramtype resource: ~typing.Literal['communication_service']
        :param params: The properties of the communication_service resource.
        :paramtype params: ~bicepbuilder.resources.communication.communication_service.CommunicationService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the CommunicationService resource.
        :rtype: ~bicepbuilder.resources.communication.communication_service.CommunicationServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['communication_email_service'],
            params: 'CommunicationEmailService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'CommunicationEmailServiceModule':
        """Deploy CommunicationEmailService resource.

        :param resource: The name of the resource to deploy: 'communication_email_service'
        :paramtype resource: ~typing.Literal['communication_email_service']
        :param params: The properties of the communication_email_service resource.
        :paramtype params: ~bicepbuilder.resources.communication.email_service.CommunicationEmailService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the CommunicationEmailService resource.
        :rtype: ~bicepbuilder.resources.communication.email_service.CommunicationEmailServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_availability_set'],
            params: 'ComputeAvailabilitySet',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeAvailabilitySetModule':
        """Deploy ComputeAvailabilitySet resource.

        :param resource: The name of the resource to deploy: 'compute_availability_set'
        :paramtype resource: ~typing.Literal['compute_availability_set']
        :param params: The properties of the compute_availability_set resource.
        :paramtype params: ~bicepbuilder.resources.compute.availability_set.ComputeAvailabilitySet
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeAvailabilitySet resource.
        :rtype: ~bicepbuilder.resources.compute.availability_set.ComputeAvailabilitySetModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_disk'],
            params: 'ComputeDisk',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeDiskModule':
        """Deploy ComputeDisk resource.

        :param resource: The name of the resource to deploy: 'compute_disk'
        :paramtype resource: ~typing.Literal['compute_disk']
        :param params: The properties of the compute_disk resource.
        :paramtype params: ~bicepbuilder.resources.compute.disk.ComputeDisk
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeDisk resource.
        :rtype: ~bicepbuilder.resources.compute.disk.ComputeDiskModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_disk_encryption_set'],
            params: 'ComputeDiskEncryptionSet',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeDiskEncryptionSetModule':
        """Deploy ComputeDiskEncryptionSet resource.

        :param resource: The name of the resource to deploy: 'compute_disk_encryption_set'
        :paramtype resource: ~typing.Literal['compute_disk_encryption_set']
        :param params: The properties of the compute_disk_encryption_set resource.
        :paramtype params: ~bicepbuilder.resources.compute.disk_encryption_set.ComputeDiskEncryptionSet
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeDiskEncryptionSet resource.
        :rtype: ~bicepbuilder.resources.compute.disk_encryption_set.ComputeDiskEncryptionSetModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_gallery'],
            params: 'ComputeGallery',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeGalleryModule':
        """Deploy ComputeGallery resource.

        :param resource: The name of the resource to deploy: 'compute_gallery'
        :paramtype resource: ~typing.Literal['compute_gallery']
        :param params: The properties of the compute_gallery resource.
        :paramtype params: ~bicepbuilder.resources.compute.gallery.ComputeGallery
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.8.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeGallery resource.
        :rtype: ~bicepbuilder.resources.compute.gallery.ComputeGalleryModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_image'],
            params: 'ComputeImage',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeImageModule':
        """Deploy ComputeImage resource.

        :param resource: The name of the resource to deploy: 'compute_image'
        :paramtype resource: ~typing.Literal['compute_image']
        :param params: The properties of the compute_image resource.
        :paramtype params: ~bicepbuilder.resources.compute.image.ComputeImage
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeImage resource.
        :rtype: ~bicepbuilder.resources.compute.image.ComputeImageModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_proximity_placement_group'],
            params: 'ComputeProximityPlacementGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeProximityPlacementGroupModule':
        """Deploy ComputeProximityPlacementGroup resource.

        :param resource: The name of the resource to deploy: 'compute_proximity_placement_group'
        :paramtype resource: ~typing.Literal['compute_proximity_placement_group']
        :param params: The properties of the compute_proximity_placement_group resource.
        :paramtype params: ~bicepbuilder.resources.compute.proximity_placement_group.ComputeProximityPlacementGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeProximityPlacementGroup resource.
        :rtype: ~bicepbuilder.resources.compute.proximity_placement_group.ComputeProximityPlacementGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_ssh_public_key'],
            params: 'ComputeSshPublicKey',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeSshPublicKeyModule':
        """Deploy ComputeSshPublicKey resource.

        :param resource: The name of the resource to deploy: 'compute_ssh_public_key'
        :paramtype resource: ~typing.Literal['compute_ssh_public_key']
        :param params: The properties of the compute_ssh_public_key resource.
        :paramtype params: ~bicepbuilder.resources.compute.ssh_public_key.ComputeSshPublicKey
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeSshPublicKey resource.
        :rtype: ~bicepbuilder.resources.compute.ssh_public_key.ComputeSshPublicKeyModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_virtual_machine'],
            params: 'ComputeVirtualMachine',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeVirtualMachineModule':
        """Deploy ComputeVirtualMachine resource.

        :param resource: The name of the resource to deploy: 'compute_virtual_machine'
        :paramtype resource: ~typing.Literal['compute_virtual_machine']
        :param params: The properties of the compute_virtual_machine resource.
        :paramtype params: ~bicepbuilder.resources.compute.virtual_machine.ComputeVirtualMachine
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.10.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeVirtualMachine resource.
        :rtype: ~bicepbuilder.resources.compute.virtual_machine.ComputeVirtualMachineModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_virtual_machine_scale_set'],
            params: 'ComputeVirtualMachineScaleSet',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ComputeVirtualMachineScaleSetModule':
        """Deploy ComputeVirtualMachineScaleSet resource.

        :param resource: The name of the resource to deploy: 'compute_virtual_machine_scale_set'
        :paramtype resource: ~typing.Literal['compute_virtual_machine_scale_set']
        :param params: The properties of the compute_virtual_machine_scale_set resource.
        :paramtype params: ~bicepbuilder.resources.compute.virtual_machine_scale_set.ComputeVirtualMachineScaleSet
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ComputeVirtualMachineScaleSet resource.
        :rtype: ~bicepbuilder.resources.compute.virtual_machine_scale_set.ComputeVirtualMachineScaleSetModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['consumption_budget'],
            params: 'ConsumptionBudget',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ConsumptionBudgetModule':
        """Deploy ConsumptionBudget resource.

        :param resource: The name of the resource to deploy: 'consumption_budget'
        :paramtype resource: ~typing.Literal['consumption_budget']
        :param params: The properties of the consumption_budget resource.
        :paramtype params: ~bicepbuilder.resources.consumption.budget.ConsumptionBudget
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ConsumptionBudget resource.
        :rtype: ~bicepbuilder.resources.consumption.budget.ConsumptionBudgetModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['container_instance_container_group'],
            params: 'ContainerInstanceContainerGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ContainerInstanceContainerGroupModule':
        """Deploy ContainerInstanceContainerGroup resource.

        :param resource: The name of the resource to deploy: 'container_instance_container_group'
        :paramtype resource: ~typing.Literal['container_instance_container_group']
        :param params: The properties of the container_instance_container_group resource.
        :paramtype params: ~bicepbuilder.resources.container_instance.container_group.ContainerInstanceContainerGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ContainerInstanceContainerGroup resource.
        :rtype: ~bicepbuilder.resources.container_instance.container_group.ContainerInstanceContainerGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['container_registry'],
            params: 'ContainerRegistry',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ContainerRegistryModule':
        """Deploy ContainerRegistry resource.

        :param resource: The name of the resource to deploy: 'container_registry'
        :paramtype resource: ~typing.Literal['container_registry']
        :param params: The properties of the container_registry resource.
        :paramtype params: ~bicepbuilder.resources.container_registry.registry.ContainerRegistry
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ContainerRegistry resource.
        :rtype: ~bicepbuilder.resources.container_registry.registry.ContainerRegistryModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['container_service_managed_cluster'],
            params: 'ContainerServiceManagedCluster',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ContainerServiceManagedClusterModule':
        """Deploy ContainerServiceManagedCluster resource.

        :param resource: The name of the resource to deploy: 'container_service_managed_cluster'
        :paramtype resource: ~typing.Literal['container_service_managed_cluster']
        :param params: The properties of the container_service_managed_cluster resource.
        :paramtype params: ~bicepbuilder.resources.container_service.managed_cluster.ContainerServiceManagedCluster
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ContainerServiceManagedCluster resource.
        :rtype: ~bicepbuilder.resources.container_service.managed_cluster.ContainerServiceManagedClusterModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['data_factory'],
            params: 'DataFactory',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DataFactoryModule':
        """Deploy DataFactory resource.

        :param resource: The name of the resource to deploy: 'data_factory'
        :paramtype resource: ~typing.Literal['data_factory']
        :param params: The properties of the data_factory resource.
        :paramtype params: ~bicepbuilder.resources.data_factory.factory.DataFactory
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DataFactory resource.
        :rtype: ~bicepbuilder.resources.data_factory.factory.DataFactoryModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['data_protection_backup_vault'],
            params: 'DataProtectionBackupVault',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DataProtectionBackupVaultModule':
        """Deploy DataProtectionBackupVault resource.

        :param resource: The name of the resource to deploy: 'data_protection_backup_vault'
        :paramtype resource: ~typing.Literal['data_protection_backup_vault']
        :param params: The properties of the data_protection_backup_vault resource.
        :paramtype params: ~bicepbuilder.resources.data_protection.backup_vault.DataProtectionBackupVault
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DataProtectionBackupVault resource.
        :rtype: ~bicepbuilder.resources.data_protection.backup_vault.DataProtectionBackupVaultModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['databricks_access_connector'],
            params: 'DatabricksAccessConnector',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DatabricksAccessConnectorModule':
        """Deploy DatabricksAccessConnector resource.

        :param resource: The name of the resource to deploy: 'databricks_access_connector'
        :paramtype resource: ~typing.Literal['databricks_access_connector']
        :param params: The properties of the databricks_access_connector resource.
        :paramtype params: ~bicepbuilder.resources.databricks.access_connector.DatabricksAccessConnector
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DatabricksAccessConnector resource.
        :rtype: ~bicepbuilder.resources.databricks.access_connector.DatabricksAccessConnectorModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['databricks_workspace'],
            params: 'DatabricksWorkspace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DatabricksWorkspaceModule':
        """Deploy DatabricksWorkspace resource.

        :param resource: The name of the resource to deploy: 'databricks_workspace'
        :paramtype resource: ~typing.Literal['databricks_workspace']
        :param params: The properties of the databricks_workspace resource.
        :paramtype params: ~bicepbuilder.resources.databricks.workspace.DatabricksWorkspace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DatabricksWorkspace resource.
        :rtype: ~bicepbuilder.resources.databricks.workspace.DatabricksWorkspaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['db_for_my_sql_flexible_server'],
            params: 'DbForMySqlFlexibleServer',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DbForMySqlFlexibleServerModule':
        """Deploy DbForMySqlFlexibleServer resource.

        :param resource: The name of the resource to deploy: 'db_for_my_sql_flexible_server'
        :paramtype resource: ~typing.Literal['db_for_my_sql_flexible_server']
        :param params: The properties of the db_for_my_sql_flexible_server resource.
        :paramtype params: ~bicepbuilder.resources.db_for_my_sql.flexible_server.DbForMySqlFlexibleServer
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DbForMySqlFlexibleServer resource.
        :rtype: ~bicepbuilder.resources.db_for_my_sql.flexible_server.DbForMySqlFlexibleServerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['db_for_postgre_sql_flexible_server'],
            params: 'DbForPostgreSqlFlexibleServer',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DbForPostgreSqlFlexibleServerModule':
        """Deploy DbForPostgreSqlFlexibleServer resource.

        :param resource: The name of the resource to deploy: 'db_for_postgre_sql_flexible_server'
        :paramtype resource: ~typing.Literal['db_for_postgre_sql_flexible_server']
        :param params: The properties of the db_for_postgre_sql_flexible_server resource.
        :paramtype params: ~bicepbuilder.resources.db_for_postgre_sql.flexible_server.DbForPostgreSqlFlexibleServer
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DbForPostgreSqlFlexibleServer resource.
        :rtype: ~bicepbuilder.resources.db_for_postgre_sql.flexible_server.DbForPostgreSqlFlexibleServerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_application_group'],
            params: 'DesktopVirtualizationApplicationGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DesktopVirtualizationApplicationGroupModule':
        """Deploy DesktopVirtualizationApplicationGroup resource.

        :param resource: The name of the resource to deploy: 'desktop_virtualization_application_group'
        :paramtype resource: ~typing.Literal['desktop_virtualization_application_group']
        :param params: The properties of the desktop_virtualization_application_group resource.
        :paramtype params: ~bicepbuilder.resources.desktop_virtualization.application_group.DesktopVirtualizationApplicationGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DesktopVirtualizationApplicationGroup resource.
        :rtype: ~bicepbuilder.resources.desktop_virtualization.application_group.DesktopVirtualizationApplicationGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_host_pool'],
            params: 'DesktopVirtualizationHostPool',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DesktopVirtualizationHostPoolModule':
        """Deploy DesktopVirtualizationHostPool resource.

        :param resource: The name of the resource to deploy: 'desktop_virtualization_host_pool'
        :paramtype resource: ~typing.Literal['desktop_virtualization_host_pool']
        :param params: The properties of the desktop_virtualization_host_pool resource.
        :paramtype params: ~bicepbuilder.resources.desktop_virtualization.host_pool.DesktopVirtualizationHostPool
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DesktopVirtualizationHostPool resource.
        :rtype: ~bicepbuilder.resources.desktop_virtualization.host_pool.DesktopVirtualizationHostPoolModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_scaling_plan'],
            params: 'DesktopVirtualizationScalingPlan',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DesktopVirtualizationScalingPlanModule':
        """Deploy DesktopVirtualizationScalingPlan resource.

        :param resource: The name of the resource to deploy: 'desktop_virtualization_scaling_plan'
        :paramtype resource: ~typing.Literal['desktop_virtualization_scaling_plan']
        :param params: The properties of the desktop_virtualization_scaling_plan resource.
        :paramtype params: ~bicepbuilder.resources.desktop_virtualization.scaling_plan.DesktopVirtualizationScalingPlan
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DesktopVirtualizationScalingPlan resource.
        :rtype: ~bicepbuilder.resources.desktop_virtualization.scaling_plan.DesktopVirtualizationScalingPlanModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_workspace'],
            params: 'DesktopVirtualizationWorkspace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DesktopVirtualizationWorkspaceModule':
        """Deploy DesktopVirtualizationWorkspace resource.

        :param resource: The name of the resource to deploy: 'desktop_virtualization_workspace'
        :paramtype resource: ~typing.Literal['desktop_virtualization_workspace']
        :param params: The properties of the desktop_virtualization_workspace resource.
        :paramtype params: ~bicepbuilder.resources.desktop_virtualization.workspace.DesktopVirtualizationWorkspace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DesktopVirtualizationWorkspace resource.
        :rtype: ~bicepbuilder.resources.desktop_virtualization.workspace.DesktopVirtualizationWorkspaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['dev_ops_infrastructure_pool'],
            params: 'DevOpsInfrastructurePool',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DevOpsInfrastructurePoolModule':
        """Deploy DevOpsInfrastructurePool resource.

        :param resource: The name of the resource to deploy: 'dev_ops_infrastructure_pool'
        :paramtype resource: ~typing.Literal['dev_ops_infrastructure_pool']
        :param params: The properties of the dev_ops_infrastructure_pool resource.
        :paramtype params: ~bicepbuilder.resources.dev_ops_infrastructure.pool.DevOpsInfrastructurePool
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DevOpsInfrastructurePool resource.
        :rtype: ~bicepbuilder.resources.dev_ops_infrastructure.pool.DevOpsInfrastructurePoolModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['dev_test_lab'],
            params: 'DevTestLab',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DevTestLabModule':
        """Deploy DevTestLab resource.

        :param resource: The name of the resource to deploy: 'dev_test_lab'
        :paramtype resource: ~typing.Literal['dev_test_lab']
        :param params: The properties of the dev_test_lab resource.
        :paramtype params: ~bicepbuilder.resources.dev_test_lab.lab.DevTestLab
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DevTestLab resource.
        :rtype: ~bicepbuilder.resources.dev_test_lab.lab.DevTestLabModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['digital_twins_instance'],
            params: 'DigitalTwinsInstance',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DigitalTwinsInstanceModule':
        """Deploy DigitalTwinsInstance resource.

        :param resource: The name of the resource to deploy: 'digital_twins_instance'
        :paramtype resource: ~typing.Literal['digital_twins_instance']
        :param params: The properties of the digital_twins_instance resource.
        :paramtype params: ~bicepbuilder.resources.digital_twins.digital_twins_instance.DigitalTwinsInstance
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DigitalTwinsInstance resource.
        :rtype: ~bicepbuilder.resources.digital_twins.digital_twins_instance.DigitalTwinsInstanceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['document_db_database_account'],
            params: 'DocumentDbDatabaseAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DocumentDbDatabaseAccountModule':
        """Deploy DocumentDbDatabaseAccount resource.

        :param resource: The name of the resource to deploy: 'document_db_database_account'
        :paramtype resource: ~typing.Literal['document_db_database_account']
        :param params: The properties of the document_db_database_account resource.
        :paramtype params: ~bicepbuilder.resources.document_db.database_account.DocumentDbDatabaseAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.10.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DocumentDbDatabaseAccount resource.
        :rtype: ~bicepbuilder.resources.document_db.database_account.DocumentDbDatabaseAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['document_db_mongo_cluster'],
            params: 'DocumentDbMongoCluster',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'DocumentDbMongoClusterModule':
        """Deploy DocumentDbMongoCluster resource.

        :param resource: The name of the resource to deploy: 'document_db_mongo_cluster'
        :paramtype resource: ~typing.Literal['document_db_mongo_cluster']
        :param params: The properties of the document_db_mongo_cluster resource.
        :paramtype params: ~bicepbuilder.resources.document_db.mongo_cluster.DocumentDbMongoCluster
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the DocumentDbMongoCluster resource.
        :rtype: ~bicepbuilder.resources.document_db.mongo_cluster.DocumentDbMongoClusterModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['elastic_san'],
            params: 'ElasticSan',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ElasticSanModule':
        """Deploy ElasticSan resource.

        :param resource: The name of the resource to deploy: 'elastic_san'
        :paramtype resource: ~typing.Literal['elastic_san']
        :param params: The properties of the elastic_san resource.
        :paramtype params: ~bicepbuilder.resources.elastic_san.elastic_san.ElasticSan
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ElasticSan resource.
        :rtype: ~bicepbuilder.resources.elastic_san.elastic_san.ElasticSanModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_domain'],
            params: 'EventGridDomain',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'EventGridDomainModule':
        """Deploy EventGridDomain resource.

        :param resource: The name of the resource to deploy: 'event_grid_domain'
        :paramtype resource: ~typing.Literal['event_grid_domain']
        :param params: The properties of the event_grid_domain resource.
        :paramtype params: ~bicepbuilder.resources.event_grid.domain.EventGridDomain
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the EventGridDomain resource.
        :rtype: ~bicepbuilder.resources.event_grid.domain.EventGridDomainModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_namespace'],
            params: 'EventGridNamespace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'EventGridNamespaceModule':
        """Deploy EventGridNamespace resource.

        :param resource: The name of the resource to deploy: 'event_grid_namespace'
        :paramtype resource: ~typing.Literal['event_grid_namespace']
        :param params: The properties of the event_grid_namespace resource.
        :paramtype params: ~bicepbuilder.resources.event_grid.namespace.EventGridNamespace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the EventGridNamespace resource.
        :rtype: ~bicepbuilder.resources.event_grid.namespace.EventGridNamespaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_system_topic'],
            params: 'EventGridSystemTopic',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'EventGridSystemTopicModule':
        """Deploy EventGridSystemTopic resource.

        :param resource: The name of the resource to deploy: 'event_grid_system_topic'
        :paramtype resource: ~typing.Literal['event_grid_system_topic']
        :param params: The properties of the event_grid_system_topic resource.
        :paramtype params: ~bicepbuilder.resources.event_grid.system_topic.EventGridSystemTopic
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the EventGridSystemTopic resource.
        :rtype: ~bicepbuilder.resources.event_grid.system_topic.EventGridSystemTopicModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_topic'],
            params: 'EventGridTopic',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'EventGridTopicModule':
        """Deploy EventGridTopic resource.

        :param resource: The name of the resource to deploy: 'event_grid_topic'
        :paramtype resource: ~typing.Literal['event_grid_topic']
        :param params: The properties of the event_grid_topic resource.
        :paramtype params: ~bicepbuilder.resources.event_grid.topic.EventGridTopic
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the EventGridTopic resource.
        :rtype: ~bicepbuilder.resources.event_grid.topic.EventGridTopicModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['event_hub_namespace'],
            params: 'EventHubNamespace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'EventHubNamespaceModule':
        """Deploy EventHubNamespace resource.

        :param resource: The name of the resource to deploy: 'event_hub_namespace'
        :paramtype resource: ~typing.Literal['event_hub_namespace']
        :param params: The properties of the event_hub_namespace resource.
        :paramtype params: ~bicepbuilder.resources.event_hub.namespace.EventHubNamespace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the EventHubNamespace resource.
        :rtype: ~bicepbuilder.resources.event_hub.namespace.EventHubNamespaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['fabric_capacity'],
            params: 'FabricCapacity',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'FabricCapacityModule':
        """Deploy FabricCapacity resource.

        :param resource: The name of the resource to deploy: 'fabric_capacity'
        :paramtype resource: ~typing.Literal['fabric_capacity']
        :param params: The properties of the fabric_capacity resource.
        :paramtype params: ~bicepbuilder.resources.fabric.capacity.FabricCapacity
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the FabricCapacity resource.
        :rtype: ~bicepbuilder.resources.fabric.capacity.FabricCapacityModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['hybrid_compute_machine'],
            params: 'HybridComputeMachine',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'HybridComputeMachineModule':
        """Deploy HybridComputeMachine resource.

        :param resource: The name of the resource to deploy: 'hybrid_compute_machine'
        :paramtype resource: ~typing.Literal['hybrid_compute_machine']
        :param params: The properties of the hybrid_compute_machine resource.
        :paramtype params: ~bicepbuilder.resources.hybrid_compute.machine.HybridComputeMachine
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the HybridComputeMachine resource.
        :rtype: ~bicepbuilder.resources.hybrid_compute.machine.HybridComputeMachineModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_action_group'],
            params: 'InsightsActionGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsActionGroupModule':
        """Deploy InsightsActionGroup resource.

        :param resource: The name of the resource to deploy: 'insights_action_group'
        :paramtype resource: ~typing.Literal['insights_action_group']
        :param params: The properties of the insights_action_group resource.
        :paramtype params: ~bicepbuilder.resources.insights.action_group.InsightsActionGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsActionGroup resource.
        :rtype: ~bicepbuilder.resources.insights.action_group.InsightsActionGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_activity_log_alert'],
            params: 'InsightsActivityLogAlert',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsActivityLogAlertModule':
        """Deploy InsightsActivityLogAlert resource.

        :param resource: The name of the resource to deploy: 'insights_activity_log_alert'
        :paramtype resource: ~typing.Literal['insights_activity_log_alert']
        :param params: The properties of the insights_activity_log_alert resource.
        :paramtype params: ~bicepbuilder.resources.insights.activity_log_alert.InsightsActivityLogAlert
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsActivityLogAlert resource.
        :rtype: ~bicepbuilder.resources.insights.activity_log_alert.InsightsActivityLogAlertModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_component'],
            params: 'InsightsComponent',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsComponentModule':
        """Deploy InsightsComponent resource.

        :param resource: The name of the resource to deploy: 'insights_component'
        :paramtype resource: ~typing.Literal['insights_component']
        :param params: The properties of the insights_component resource.
        :paramtype params: ~bicepbuilder.resources.insights.component.InsightsComponent
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsComponent resource.
        :rtype: ~bicepbuilder.resources.insights.component.InsightsComponentModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_data_collection_endpoint'],
            params: 'InsightsDataCollectionEndpoint',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsDataCollectionEndpointModule':
        """Deploy InsightsDataCollectionEndpoint resource.

        :param resource: The name of the resource to deploy: 'insights_data_collection_endpoint'
        :paramtype resource: ~typing.Literal['insights_data_collection_endpoint']
        :param params: The properties of the insights_data_collection_endpoint resource.
        :paramtype params: ~bicepbuilder.resources.insights.data_collection_endpoint.InsightsDataCollectionEndpoint
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsDataCollectionEndpoint resource.
        :rtype: ~bicepbuilder.resources.insights.data_collection_endpoint.InsightsDataCollectionEndpointModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_data_collection_rule'],
            params: 'InsightsDataCollectionRule',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsDataCollectionRuleModule':
        """Deploy InsightsDataCollectionRule resource.

        :param resource: The name of the resource to deploy: 'insights_data_collection_rule'
        :paramtype resource: ~typing.Literal['insights_data_collection_rule']
        :param params: The properties of the insights_data_collection_rule resource.
        :paramtype params: ~bicepbuilder.resources.insights.data_collection_rule.InsightsDataCollectionRule
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsDataCollectionRule resource.
        :rtype: ~bicepbuilder.resources.insights.data_collection_rule.InsightsDataCollectionRuleModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_diagnostic_setting'],
            params: 'InsightsDiagnosticSetting',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsDiagnosticSettingModule':
        """Deploy InsightsDiagnosticSetting resource.

        :param resource: The name of the resource to deploy: 'insights_diagnostic_setting'
        :paramtype resource: ~typing.Literal['insights_diagnostic_setting']
        :param params: The properties of the insights_diagnostic_setting resource.
        :paramtype params: ~bicepbuilder.resources.insights.diagnostic_setting.InsightsDiagnosticSetting
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsDiagnosticSetting resource.
        :rtype: ~bicepbuilder.resources.insights.diagnostic_setting.InsightsDiagnosticSettingModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_metric_alert'],
            params: 'InsightsMetricAlert',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsMetricAlertModule':
        """Deploy InsightsMetricAlert resource.

        :param resource: The name of the resource to deploy: 'insights_metric_alert'
        :paramtype resource: ~typing.Literal['insights_metric_alert']
        :param params: The properties of the insights_metric_alert resource.
        :paramtype params: ~bicepbuilder.resources.insights.metric_alert.InsightsMetricAlert
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsMetricAlert resource.
        :rtype: ~bicepbuilder.resources.insights.metric_alert.InsightsMetricAlertModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_private_link_scope'],
            params: 'InsightsPrivateLinkScope',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsPrivateLinkScopeModule':
        """Deploy InsightsPrivateLinkScope resource.

        :param resource: The name of the resource to deploy: 'insights_private_link_scope'
        :paramtype resource: ~typing.Literal['insights_private_link_scope']
        :param params: The properties of the insights_private_link_scope resource.
        :paramtype params: ~bicepbuilder.resources.insights.private_link_scope.InsightsPrivateLinkScope
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsPrivateLinkScope resource.
        :rtype: ~bicepbuilder.resources.insights.private_link_scope.InsightsPrivateLinkScopeModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_scheduled_query_rule'],
            params: 'InsightsScheduledQueryRule',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsScheduledQueryRuleModule':
        """Deploy InsightsScheduledQueryRule resource.

        :param resource: The name of the resource to deploy: 'insights_scheduled_query_rule'
        :paramtype resource: ~typing.Literal['insights_scheduled_query_rule']
        :param params: The properties of the insights_scheduled_query_rule resource.
        :paramtype params: ~bicepbuilder.resources.insights.scheduled_query_rule.InsightsScheduledQueryRule
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsScheduledQueryRule resource.
        :rtype: ~bicepbuilder.resources.insights.scheduled_query_rule.InsightsScheduledQueryRuleModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_webtest'],
            params: 'InsightsWebtest',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'InsightsWebtestModule':
        """Deploy InsightsWebtest resource.

        :param resource: The name of the resource to deploy: 'insights_webtest'
        :paramtype resource: ~typing.Literal['insights_webtest']
        :param params: The properties of the insights_webtest resource.
        :paramtype params: ~bicepbuilder.resources.insights.webtest.InsightsWebtest
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the InsightsWebtest resource.
        :rtype: ~bicepbuilder.resources.insights.webtest.InsightsWebtestModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['key_vault'],
            params: 'KeyVault',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'KeyVaultModule':
        """Deploy KeyVault resource.

        :param resource: The name of the resource to deploy: 'key_vault'
        :paramtype resource: ~typing.Literal['key_vault']
        :param params: The properties of the key_vault resource.
        :paramtype params: ~bicepbuilder.resources.key_vault.vault.KeyVault
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.11.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the KeyVault resource.
        :rtype: ~bicepbuilder.resources.key_vault.vault.KeyVaultModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['kubernetes_configuration_extension'],
            params: 'KubernetesConfigurationExtension',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'KubernetesConfigurationExtensionModule':
        """Deploy KubernetesConfigurationExtension resource.

        :param resource: The name of the resource to deploy: 'kubernetes_configuration_extension'
        :paramtype resource: ~typing.Literal['kubernetes_configuration_extension']
        :param params: The properties of the kubernetes_configuration_extension resource.
        :paramtype params: ~bicepbuilder.resources.kubernetes_configuration.extension.KubernetesConfigurationExtension
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the KubernetesConfigurationExtension resource.
        :rtype: ~bicepbuilder.resources.kubernetes_configuration.extension.KubernetesConfigurationExtensionModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['kubernetes_configuration_flux_configuration'],
            params: 'KubernetesConfigurationFluxConfiguration',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'KubernetesConfigurationFluxConfigurationModule':
        """Deploy KubernetesConfigurationFluxConfiguration resource.

        :param resource: The name of the resource to deploy: 'kubernetes_configuration_flux_configuration'
        :paramtype resource: ~typing.Literal['kubernetes_configuration_flux_configuration']
        :param params: The properties of the kubernetes_configuration_flux_configuration resource.
        :paramtype params: ~bicepbuilder.resources.kubernetes_configuration.flux_configuration.KubernetesConfigurationFluxConfiguration
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the KubernetesConfigurationFluxConfiguration resource.
        :rtype: ~bicepbuilder.resources.kubernetes_configuration.flux_configuration.KubernetesConfigurationFluxConfigurationModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['kusto_cluster'],
            params: 'KustoCluster',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'KustoClusterModule':
        """Deploy KustoCluster resource.

        :param resource: The name of the resource to deploy: 'kusto_cluster'
        :paramtype resource: ~typing.Literal['kusto_cluster']
        :param params: The properties of the kusto_cluster resource.
        :paramtype params: ~bicepbuilder.resources.kusto.cluster.KustoCluster
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the KustoCluster resource.
        :rtype: ~bicepbuilder.resources.kusto.cluster.KustoClusterModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['load_test_service_load_test'],
            params: 'LoadTestServiceLoadTest',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'LoadTestServiceLoadTestModule':
        """Deploy LoadTestServiceLoadTest resource.

        :param resource: The name of the resource to deploy: 'load_test_service_load_test'
        :paramtype resource: ~typing.Literal['load_test_service_load_test']
        :param params: The properties of the load_test_service_load_test resource.
        :paramtype params: ~bicepbuilder.resources.load_test_service.load_test.LoadTestServiceLoadTest
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the LoadTestServiceLoadTest resource.
        :rtype: ~bicepbuilder.resources.load_test_service.load_test.LoadTestServiceLoadTestModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['logic_workflow'],
            params: 'LogicWorkflow',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'LogicWorkflowModule':
        """Deploy LogicWorkflow resource.

        :param resource: The name of the resource to deploy: 'logic_workflow'
        :paramtype resource: ~typing.Literal['logic_workflow']
        :param params: The properties of the logic_workflow resource.
        :paramtype params: ~bicepbuilder.resources.logic.workflow.LogicWorkflow
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the LogicWorkflow resource.
        :rtype: ~bicepbuilder.resources.logic.workflow.LogicWorkflowModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['machine_learning_services_workspace'],
            params: 'MachineLearningServicesWorkspace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'MachineLearningServicesWorkspaceModule':
        """Deploy MachineLearningServicesWorkspace resource.

        :param resource: The name of the resource to deploy: 'machine_learning_services_workspace'
        :paramtype resource: ~typing.Literal['machine_learning_services_workspace']
        :param params: The properties of the machine_learning_services_workspace resource.
        :paramtype params: ~bicepbuilder.resources.machine_learning_services.workspace.MachineLearningServicesWorkspace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the MachineLearningServicesWorkspace resource.
        :rtype: ~bicepbuilder.resources.machine_learning_services.workspace.MachineLearningServicesWorkspaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['maintenance_configuration'],
            params: 'MaintenanceConfiguration',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'MaintenanceConfigurationModule':
        """Deploy MaintenanceConfiguration resource.

        :param resource: The name of the resource to deploy: 'maintenance_configuration'
        :paramtype resource: ~typing.Literal['maintenance_configuration']
        :param params: The properties of the maintenance_configuration resource.
        :paramtype params: ~bicepbuilder.resources.maintenance.maintenance_configuration.MaintenanceConfiguration
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the MaintenanceConfiguration resource.
        :rtype: ~bicepbuilder.resources.maintenance.maintenance_configuration.MaintenanceConfigurationModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['managed_identity_user_assigned_identity'],
            params: 'ManagedIdentityUserAssignedIdentity',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ManagedIdentityUserAssignedIdentityModule':
        """Deploy ManagedIdentityUserAssignedIdentity resource.

        :param resource: The name of the resource to deploy: 'managed_identity_user_assigned_identity'
        :paramtype resource: ~typing.Literal['managed_identity_user_assigned_identity']
        :param params: The properties of the managed_identity_user_assigned_identity resource.
        :paramtype params: ~bicepbuilder.resources.managed_identity.user_assigned_identity.ManagedIdentityUserAssignedIdentity
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ManagedIdentityUserAssignedIdentity resource.
        :rtype: ~bicepbuilder.resources.managed_identity.user_assigned_identity.ManagedIdentityUserAssignedIdentityModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['management_group'],
            params: 'ManagementGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ManagementGroupModule':
        """Deploy ManagementGroup resource.

        :param resource: The name of the resource to deploy: 'management_group'
        :paramtype resource: ~typing.Literal['management_group']
        :param params: The properties of the management_group resource.
        :paramtype params: ~bicepbuilder.resources.management.management_group.ManagementGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ManagementGroup resource.
        :rtype: ~bicepbuilder.resources.management.management_group.ManagementGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['net_app_account'],
            params: 'NetAppAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetAppAccountModule':
        """Deploy NetAppAccount resource.

        :param resource: The name of the resource to deploy: 'net_app_account'
        :paramtype resource: ~typing.Literal['net_app_account']
        :param params: The properties of the net_app_account resource.
        :paramtype params: ~bicepbuilder.resources.net_app.net_app_account.NetAppAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetAppAccount resource.
        :rtype: ~bicepbuilder.resources.net_app.net_app_account.NetAppAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_gateway'],
            params: 'NetworkApplicationGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkApplicationGatewayModule':
        """Deploy NetworkApplicationGateway resource.

        :param resource: The name of the resource to deploy: 'network_application_gateway'
        :paramtype resource: ~typing.Literal['network_application_gateway']
        :param params: The properties of the network_application_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.application_gateway.NetworkApplicationGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkApplicationGateway resource.
        :rtype: ~bicepbuilder.resources.network.application_gateway.NetworkApplicationGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_gateway_web_application_firewall_policy'],
            params: 'NetworkApplicationGatewayWebApplicationFirewallPolicy',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkApplicationGatewayWebApplicationFirewallPolicyModule':
        """Deploy NetworkApplicationGatewayWebApplicationFirewallPolicy resource.

        :param resource: The name of the resource to deploy: 'network_application_gateway_web_application_firewall_policy'
        :paramtype resource: ~typing.Literal['network_application_gateway_web_application_firewall_policy']
        :param params: The properties of the network_application_gateway_web_application_firewall_policy resource.
        :paramtype params: ~bicepbuilder.resources.network.application_gateway_web_application_firewall_policy.NetworkApplicationGatewayWebApplicationFirewallPolicy
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkApplicationGatewayWebApplicationFirewallPolicy resource.
        :rtype: ~bicepbuilder.resources.network.application_gateway_web_application_firewall_policy.NetworkApplicationGatewayWebApplicationFirewallPolicyModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_security_group'],
            params: 'NetworkApplicationSecurityGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkApplicationSecurityGroupModule':
        """Deploy NetworkApplicationSecurityGroup resource.

        :param resource: The name of the resource to deploy: 'network_application_security_group'
        :paramtype resource: ~typing.Literal['network_application_security_group']
        :param params: The properties of the network_application_security_group resource.
        :paramtype params: ~bicepbuilder.resources.network.application_security_group.NetworkApplicationSecurityGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkApplicationSecurityGroup resource.
        :rtype: ~bicepbuilder.resources.network.application_security_group.NetworkApplicationSecurityGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_azure_firewall'],
            params: 'NetworkAzureFirewall',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkAzureFirewallModule':
        """Deploy NetworkAzureFirewall resource.

        :param resource: The name of the resource to deploy: 'network_azure_firewall'
        :paramtype resource: ~typing.Literal['network_azure_firewall']
        :param params: The properties of the network_azure_firewall resource.
        :paramtype params: ~bicepbuilder.resources.network.azure_firewall.NetworkAzureFirewall
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkAzureFirewall resource.
        :rtype: ~bicepbuilder.resources.network.azure_firewall.NetworkAzureFirewallModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_bastion_host'],
            params: 'NetworkBastionHost',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkBastionHostModule':
        """Deploy NetworkBastionHost resource.

        :param resource: The name of the resource to deploy: 'network_bastion_host'
        :paramtype resource: ~typing.Literal['network_bastion_host']
        :param params: The properties of the network_bastion_host resource.
        :paramtype params: ~bicepbuilder.resources.network.bastion_host.NetworkBastionHost
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkBastionHost resource.
        :rtype: ~bicepbuilder.resources.network.bastion_host.NetworkBastionHostModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_connection'],
            params: 'NetworkConnection',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkConnectionModule':
        """Deploy NetworkConnection resource.

        :param resource: The name of the resource to deploy: 'network_connection'
        :paramtype resource: ~typing.Literal['network_connection']
        :param params: The properties of the network_connection resource.
        :paramtype params: ~bicepbuilder.resources.network.connection.NetworkConnection
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkConnection resource.
        :rtype: ~bicepbuilder.resources.network.connection.NetworkConnectionModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_ddos_protection_plan'],
            params: 'NetworkDdosProtectionPlan',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkDdosProtectionPlanModule':
        """Deploy NetworkDdosProtectionPlan resource.

        :param resource: The name of the resource to deploy: 'network_ddos_protection_plan'
        :paramtype resource: ~typing.Literal['network_ddos_protection_plan']
        :param params: The properties of the network_ddos_protection_plan resource.
        :paramtype params: ~bicepbuilder.resources.network.ddos_protection_plan.NetworkDdosProtectionPlan
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkDdosProtectionPlan resource.
        :rtype: ~bicepbuilder.resources.network.ddos_protection_plan.NetworkDdosProtectionPlanModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_forwarding_ruleset'],
            params: 'NetworkDnsForwardingRuleset',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkDnsForwardingRulesetModule':
        """Deploy NetworkDnsForwardingRuleset resource.

        :param resource: The name of the resource to deploy: 'network_dns_forwarding_ruleset'
        :paramtype resource: ~typing.Literal['network_dns_forwarding_ruleset']
        :param params: The properties of the network_dns_forwarding_ruleset resource.
        :paramtype params: ~bicepbuilder.resources.network.dns_forwarding_ruleset.NetworkDnsForwardingRuleset
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkDnsForwardingRuleset resource.
        :rtype: ~bicepbuilder.resources.network.dns_forwarding_ruleset.NetworkDnsForwardingRulesetModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_resolver'],
            params: 'NetworkDnsResolver',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkDnsResolverModule':
        """Deploy NetworkDnsResolver resource.

        :param resource: The name of the resource to deploy: 'network_dns_resolver'
        :paramtype resource: ~typing.Literal['network_dns_resolver']
        :param params: The properties of the network_dns_resolver resource.
        :paramtype params: ~bicepbuilder.resources.network.dns_resolver.NetworkDnsResolver
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkDnsResolver resource.
        :rtype: ~bicepbuilder.resources.network.dns_resolver.NetworkDnsResolverModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_zone'],
            params: 'NetworkDnsZone',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkDnsZoneModule':
        """Deploy NetworkDnsZone resource.

        :param resource: The name of the resource to deploy: 'network_dns_zone'
        :paramtype resource: ~typing.Literal['network_dns_zone']
        :param params: The properties of the network_dns_zone resource.
        :paramtype params: ~bicepbuilder.resources.network.dns_zone.NetworkDnsZone
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkDnsZone resource.
        :rtype: ~bicepbuilder.resources.network.dns_zone.NetworkDnsZoneModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_express_route_circuit'],
            params: 'NetworkExpressRouteCircuit',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkExpressRouteCircuitModule':
        """Deploy NetworkExpressRouteCircuit resource.

        :param resource: The name of the resource to deploy: 'network_express_route_circuit'
        :paramtype resource: ~typing.Literal['network_express_route_circuit']
        :param params: The properties of the network_express_route_circuit resource.
        :paramtype params: ~bicepbuilder.resources.network.express_route_circuit.NetworkExpressRouteCircuit
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkExpressRouteCircuit resource.
        :rtype: ~bicepbuilder.resources.network.express_route_circuit.NetworkExpressRouteCircuitModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_express_route_gateway'],
            params: 'NetworkExpressRouteGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkExpressRouteGatewayModule':
        """Deploy NetworkExpressRouteGateway resource.

        :param resource: The name of the resource to deploy: 'network_express_route_gateway'
        :paramtype resource: ~typing.Literal['network_express_route_gateway']
        :param params: The properties of the network_express_route_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.express_route_gateway.NetworkExpressRouteGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkExpressRouteGateway resource.
        :rtype: ~bicepbuilder.resources.network.express_route_gateway.NetworkExpressRouteGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_firewall_policy'],
            params: 'NetworkFirewallPolicy',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkFirewallPolicyModule':
        """Deploy NetworkFirewallPolicy resource.

        :param resource: The name of the resource to deploy: 'network_firewall_policy'
        :paramtype resource: ~typing.Literal['network_firewall_policy']
        :param params: The properties of the network_firewall_policy resource.
        :paramtype params: ~bicepbuilder.resources.network.firewall_policy.NetworkFirewallPolicy
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkFirewallPolicy resource.
        :rtype: ~bicepbuilder.resources.network.firewall_policy.NetworkFirewallPolicyModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_front_door'],
            params: 'NetworkFrontDoor',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkFrontDoorModule':
        """Deploy NetworkFrontDoor resource.

        :param resource: The name of the resource to deploy: 'network_front_door'
        :paramtype resource: ~typing.Literal['network_front_door']
        :param params: The properties of the network_front_door resource.
        :paramtype params: ~bicepbuilder.resources.network.front_door.NetworkFrontDoor
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkFrontDoor resource.
        :rtype: ~bicepbuilder.resources.network.front_door.NetworkFrontDoorModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_front_door_web_application_firewall_policy'],
            params: 'NetworkFrontDoorWebApplicationFirewallPolicy',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkFrontDoorWebApplicationFirewallPolicyModule':
        """Deploy NetworkFrontDoorWebApplicationFirewallPolicy resource.

        :param resource: The name of the resource to deploy: 'network_front_door_web_application_firewall_policy'
        :paramtype resource: ~typing.Literal['network_front_door_web_application_firewall_policy']
        :param params: The properties of the network_front_door_web_application_firewall_policy resource.
        :paramtype params: ~bicepbuilder.resources.network.front_door_web_application_firewall_policy.NetworkFrontDoorWebApplicationFirewallPolicy
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkFrontDoorWebApplicationFirewallPolicy resource.
        :rtype: ~bicepbuilder.resources.network.front_door_web_application_firewall_policy.NetworkFrontDoorWebApplicationFirewallPolicyModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_ip_group'],
            params: 'NetworkIpGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkIpGroupModule':
        """Deploy NetworkIpGroup resource.

        :param resource: The name of the resource to deploy: 'network_ip_group'
        :paramtype resource: ~typing.Literal['network_ip_group']
        :param params: The properties of the network_ip_group resource.
        :paramtype params: ~bicepbuilder.resources.network.ip_group.NetworkIpGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkIpGroup resource.
        :rtype: ~bicepbuilder.resources.network.ip_group.NetworkIpGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_load_balancer'],
            params: 'NetworkLoadBalancer',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkLoadBalancerModule':
        """Deploy NetworkLoadBalancer resource.

        :param resource: The name of the resource to deploy: 'network_load_balancer'
        :paramtype resource: ~typing.Literal['network_load_balancer']
        :param params: The properties of the network_load_balancer resource.
        :paramtype params: ~bicepbuilder.resources.network.load_balancer.NetworkLoadBalancer
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkLoadBalancer resource.
        :rtype: ~bicepbuilder.resources.network.load_balancer.NetworkLoadBalancerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_local_network_gateway'],
            params: 'NetworkLocalNetworkGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkLocalNetworkGatewayModule':
        """Deploy NetworkLocalNetworkGateway resource.

        :param resource: The name of the resource to deploy: 'network_local_network_gateway'
        :paramtype resource: ~typing.Literal['network_local_network_gateway']
        :param params: The properties of the network_local_network_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.local_network_gateway.NetworkLocalNetworkGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkLocalNetworkGateway resource.
        :rtype: ~bicepbuilder.resources.network.local_network_gateway.NetworkLocalNetworkGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_nat_gateway'],
            params: 'NetworkNatGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '1.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkNatGatewayModule':
        """Deploy NetworkNatGateway resource.

        :param resource: The name of the resource to deploy: 'network_nat_gateway'
        :paramtype resource: ~typing.Literal['network_nat_gateway']
        :param params: The properties of the network_nat_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.nat_gateway.NetworkNatGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '1.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkNatGateway resource.
        :rtype: ~bicepbuilder.resources.network.nat_gateway.NetworkNatGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_interface'],
            params: 'NetworkInterface',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkInterfaceModule':
        """Deploy NetworkInterface resource.

        :param resource: The name of the resource to deploy: 'network_interface'
        :paramtype resource: ~typing.Literal['network_interface']
        :param params: The properties of the network_interface resource.
        :paramtype params: ~bicepbuilder.resources.network.network_interface.NetworkInterface
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkInterface resource.
        :rtype: ~bicepbuilder.resources.network.network_interface.NetworkInterfaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_manager'],
            params: 'NetworkManager',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkManagerModule':
        """Deploy NetworkManager resource.

        :param resource: The name of the resource to deploy: 'network_manager'
        :paramtype resource: ~typing.Literal['network_manager']
        :param params: The properties of the network_manager resource.
        :paramtype params: ~bicepbuilder.resources.network.network_manager.NetworkManager
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkManager resource.
        :rtype: ~bicepbuilder.resources.network.network_manager.NetworkManagerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_security_group'],
            params: 'NetworkSecurityGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkSecurityGroupModule':
        """Deploy NetworkSecurityGroup resource.

        :param resource: The name of the resource to deploy: 'network_security_group'
        :paramtype resource: ~typing.Literal['network_security_group']
        :param params: The properties of the network_security_group resource.
        :paramtype params: ~bicepbuilder.resources.network.network_security_group.NetworkSecurityGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkSecurityGroup resource.
        :rtype: ~bicepbuilder.resources.network.network_security_group.NetworkSecurityGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_watcher'],
            params: 'NetworkWatcher',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkWatcherModule':
        """Deploy NetworkWatcher resource.

        :param resource: The name of the resource to deploy: 'network_watcher'
        :paramtype resource: ~typing.Literal['network_watcher']
        :param params: The properties of the network_watcher resource.
        :paramtype params: ~bicepbuilder.resources.network.network_watcher.NetworkWatcher
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkWatcher resource.
        :rtype: ~bicepbuilder.resources.network.network_watcher.NetworkWatcherModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_p2s_vpn_gateway'],
            params: 'NetworkP2SVpnGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkP2SVpnGatewayModule':
        """Deploy NetworkP2SVpnGateway resource.

        :param resource: The name of the resource to deploy: 'network_p2s_vpn_gateway'
        :paramtype resource: ~typing.Literal['network_p2s_vpn_gateway']
        :param params: The properties of the network_p2s_vpn_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.p2s_vpn_gateway.NetworkP2SVpnGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkP2SVpnGateway resource.
        :rtype: ~bicepbuilder.resources.network.p2s_vpn_gateway.NetworkP2SVpnGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_dns_zone'],
            params: 'NetworkPrivateDnsZone',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkPrivateDnsZoneModule':
        """Deploy NetworkPrivateDnsZone resource.

        :param resource: The name of the resource to deploy: 'network_private_dns_zone'
        :paramtype resource: ~typing.Literal['network_private_dns_zone']
        :param params: The properties of the network_private_dns_zone resource.
        :paramtype params: ~bicepbuilder.resources.network.private_dns_zone.NetworkPrivateDnsZone
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkPrivateDnsZone resource.
        :rtype: ~bicepbuilder.resources.network.private_dns_zone.NetworkPrivateDnsZoneModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_endpoint'],
            params: 'NetworkPrivateEndpoint',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkPrivateEndpointModule':
        """Deploy NetworkPrivateEndpoint resource.

        :param resource: The name of the resource to deploy: 'network_private_endpoint'
        :paramtype resource: ~typing.Literal['network_private_endpoint']
        :param params: The properties of the network_private_endpoint resource.
        :paramtype params: ~bicepbuilder.resources.network.private_endpoint.NetworkPrivateEndpoint
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkPrivateEndpoint resource.
        :rtype: ~bicepbuilder.resources.network.private_endpoint.NetworkPrivateEndpointModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_link_service'],
            params: 'NetworkPrivateLinkService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkPrivateLinkServiceModule':
        """Deploy NetworkPrivateLinkService resource.

        :param resource: The name of the resource to deploy: 'network_private_link_service'
        :paramtype resource: ~typing.Literal['network_private_link_service']
        :param params: The properties of the network_private_link_service resource.
        :paramtype params: ~bicepbuilder.resources.network.private_link_service.NetworkPrivateLinkService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkPrivateLinkService resource.
        :rtype: ~bicepbuilder.resources.network.private_link_service.NetworkPrivateLinkServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_public_ip_address'],
            params: 'NetworkPublicIpAddress',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkPublicIpAddressModule':
        """Deploy NetworkPublicIpAddress resource.

        :param resource: The name of the resource to deploy: 'network_public_ip_address'
        :paramtype resource: ~typing.Literal['network_public_ip_address']
        :param params: The properties of the network_public_ip_address resource.
        :paramtype params: ~bicepbuilder.resources.network.public_ip_address.NetworkPublicIpAddress
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.7.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkPublicIpAddress resource.
        :rtype: ~bicepbuilder.resources.network.public_ip_address.NetworkPublicIpAddressModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_public_ip_prefix'],
            params: 'NetworkPublicIpPrefix',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkPublicIpPrefixModule':
        """Deploy NetworkPublicIpPrefix resource.

        :param resource: The name of the resource to deploy: 'network_public_ip_prefix'
        :paramtype resource: ~typing.Literal['network_public_ip_prefix']
        :param params: The properties of the network_public_ip_prefix resource.
        :paramtype params: ~bicepbuilder.resources.network.public_ip_prefix.NetworkPublicIpPrefix
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkPublicIpPrefix resource.
        :rtype: ~bicepbuilder.resources.network.public_ip_prefix.NetworkPublicIpPrefixModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_route_table'],
            params: 'NetworkRouteTable',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkRouteTableModule':
        """Deploy NetworkRouteTable resource.

        :param resource: The name of the resource to deploy: 'network_route_table'
        :paramtype resource: ~typing.Literal['network_route_table']
        :param params: The properties of the network_route_table resource.
        :paramtype params: ~bicepbuilder.resources.network.route_table.NetworkRouteTable
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkRouteTable resource.
        :rtype: ~bicepbuilder.resources.network.route_table.NetworkRouteTableModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_service_endpoint_policy'],
            params: 'NetworkServiceEndpointPolicy',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkServiceEndpointPolicyModule':
        """Deploy NetworkServiceEndpointPolicy resource.

        :param resource: The name of the resource to deploy: 'network_service_endpoint_policy'
        :paramtype resource: ~typing.Literal['network_service_endpoint_policy']
        :param params: The properties of the network_service_endpoint_policy resource.
        :paramtype params: ~bicepbuilder.resources.network.service_endpoint_policy.NetworkServiceEndpointPolicy
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkServiceEndpointPolicy resource.
        :rtype: ~bicepbuilder.resources.network.service_endpoint_policy.NetworkServiceEndpointPolicyModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_trafficmanagerprofile'],
            params: 'NetworkTrafficmanagerprofile',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkTrafficmanagerprofileModule':
        """Deploy NetworkTrafficmanagerprofile resource.

        :param resource: The name of the resource to deploy: 'network_trafficmanagerprofile'
        :paramtype resource: ~typing.Literal['network_trafficmanagerprofile']
        :param params: The properties of the network_trafficmanagerprofile resource.
        :paramtype params: ~bicepbuilder.resources.network.trafficmanagerprofile.NetworkTrafficmanagerprofile
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkTrafficmanagerprofile resource.
        :rtype: ~bicepbuilder.resources.network.trafficmanagerprofile.NetworkTrafficmanagerprofileModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_hub'],
            params: 'NetworkVirtualHub',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVirtualHubModule':
        """Deploy NetworkVirtualHub resource.

        :param resource: The name of the resource to deploy: 'network_virtual_hub'
        :paramtype resource: ~typing.Literal['network_virtual_hub']
        :param params: The properties of the network_virtual_hub resource.
        :paramtype params: ~bicepbuilder.resources.network.virtual_hub.NetworkVirtualHub
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVirtualHub resource.
        :rtype: ~bicepbuilder.resources.network.virtual_hub.NetworkVirtualHubModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_network_gateway'],
            params: 'NetworkVirtualNetworkGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVirtualNetworkGatewayModule':
        """Deploy NetworkVirtualNetworkGateway resource.

        :param resource: The name of the resource to deploy: 'network_virtual_network_gateway'
        :paramtype resource: ~typing.Literal['network_virtual_network_gateway']
        :param params: The properties of the network_virtual_network_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.virtual_network_gateway.NetworkVirtualNetworkGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVirtualNetworkGateway resource.
        :rtype: ~bicepbuilder.resources.network.virtual_network_gateway.NetworkVirtualNetworkGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_wan'],
            params: 'NetworkVirtualWan',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVirtualWanModule':
        """Deploy NetworkVirtualWan resource.

        :param resource: The name of the resource to deploy: 'network_virtual_wan'
        :paramtype resource: ~typing.Literal['network_virtual_wan']
        :param params: The properties of the network_virtual_wan resource.
        :paramtype params: ~bicepbuilder.resources.network.virtual_wan.NetworkVirtualWan
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVirtualWan resource.
        :rtype: ~bicepbuilder.resources.network.virtual_wan.NetworkVirtualWanModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_gateway'],
            params: 'NetworkVpnGateway',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVpnGatewayModule':
        """Deploy NetworkVpnGateway resource.

        :param resource: The name of the resource to deploy: 'network_vpn_gateway'
        :paramtype resource: ~typing.Literal['network_vpn_gateway']
        :param params: The properties of the network_vpn_gateway resource.
        :paramtype params: ~bicepbuilder.resources.network.vpn_gateway.NetworkVpnGateway
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVpnGateway resource.
        :rtype: ~bicepbuilder.resources.network.vpn_gateway.NetworkVpnGatewayModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_server_configuration'],
            params: 'NetworkVpnServerConfiguration',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVpnServerConfigurationModule':
        """Deploy NetworkVpnServerConfiguration resource.

        :param resource: The name of the resource to deploy: 'network_vpn_server_configuration'
        :paramtype resource: ~typing.Literal['network_vpn_server_configuration']
        :param params: The properties of the network_vpn_server_configuration resource.
        :paramtype params: ~bicepbuilder.resources.network.vpn_server_configuration.NetworkVpnServerConfiguration
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVpnServerConfiguration resource.
        :rtype: ~bicepbuilder.resources.network.vpn_server_configuration.NetworkVpnServerConfigurationModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_site'],
            params: 'NetworkVpnSite',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'NetworkVpnSiteModule':
        """Deploy NetworkVpnSite resource.

        :param resource: The name of the resource to deploy: 'network_vpn_site'
        :paramtype resource: ~typing.Literal['network_vpn_site']
        :param params: The properties of the network_vpn_site resource.
        :paramtype params: ~bicepbuilder.resources.network.vpn_site.NetworkVpnSite
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the NetworkVpnSite resource.
        :rtype: ~bicepbuilder.resources.network.vpn_site.NetworkVpnSiteModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['operational_insights_workspace'],
            params: 'OperationalInsightsWorkspace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'OperationalInsightsWorkspaceModule':
        """Deploy OperationalInsightsWorkspace resource.

        :param resource: The name of the resource to deploy: 'operational_insights_workspace'
        :paramtype resource: ~typing.Literal['operational_insights_workspace']
        :param params: The properties of the operational_insights_workspace resource.
        :paramtype params: ~bicepbuilder.resources.operational_insights.workspace.OperationalInsightsWorkspace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.9.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the OperationalInsightsWorkspace resource.
        :rtype: ~bicepbuilder.resources.operational_insights.workspace.OperationalInsightsWorkspaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['operations_management_solution'],
            params: 'OperationsManagementSolution',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'OperationsManagementSolutionModule':
        """Deploy OperationsManagementSolution resource.

        :param resource: The name of the resource to deploy: 'operations_management_solution'
        :paramtype resource: ~typing.Literal['operations_management_solution']
        :param params: The properties of the operations_management_solution resource.
        :paramtype params: ~bicepbuilder.resources.operations_management.solution.OperationsManagementSolution
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the OperationsManagementSolution resource.
        :rtype: ~bicepbuilder.resources.operations_management.solution.OperationsManagementSolutionModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['portal_dashboard'],
            params: 'PortalDashboard',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'PortalDashboardModule':
        """Deploy PortalDashboard resource.

        :param resource: The name of the resource to deploy: 'portal_dashboard'
        :paramtype resource: ~typing.Literal['portal_dashboard']
        :param params: The properties of the portal_dashboard resource.
        :paramtype params: ~bicepbuilder.resources.portal.dashboard.PortalDashboard
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the PortalDashboard resource.
        :rtype: ~bicepbuilder.resources.portal.dashboard.PortalDashboardModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['power_bi_dedicated_capacity'],
            params: 'PowerBiDedicatedCapacity',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'PowerBiDedicatedCapacityModule':
        """Deploy PowerBiDedicatedCapacity resource.

        :param resource: The name of the resource to deploy: 'power_bi_dedicated_capacity'
        :paramtype resource: ~typing.Literal['power_bi_dedicated_capacity']
        :param params: The properties of the power_bi_dedicated_capacity resource.
        :paramtype params: ~bicepbuilder.resources.power_bi_dedicated.capacity.PowerBiDedicatedCapacity
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the PowerBiDedicatedCapacity resource.
        :rtype: ~bicepbuilder.resources.power_bi_dedicated.capacity.PowerBiDedicatedCapacityModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['purview_account'],
            params: 'PurviewAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'PurviewAccountModule':
        """Deploy PurviewAccount resource.

        :param resource: The name of the resource to deploy: 'purview_account'
        :paramtype resource: ~typing.Literal['purview_account']
        :param params: The properties of the purview_account resource.
        :paramtype params: ~bicepbuilder.resources.purview.account.PurviewAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the PurviewAccount resource.
        :rtype: ~bicepbuilder.resources.purview.account.PurviewAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['recovery_services_vault'],
            params: 'RecoveryServicesVault',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'RecoveryServicesVaultModule':
        """Deploy RecoveryServicesVault resource.

        :param resource: The name of the resource to deploy: 'recovery_services_vault'
        :paramtype resource: ~typing.Literal['recovery_services_vault']
        :param params: The properties of the recovery_services_vault resource.
        :paramtype params: ~bicepbuilder.resources.recovery_services.vault.RecoveryServicesVault
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the RecoveryServicesVault resource.
        :rtype: ~bicepbuilder.resources.recovery_services.vault.RecoveryServicesVaultModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['resource_graph_query'],
            params: 'ResourceGraphQuery',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ResourceGraphQueryModule':
        """Deploy ResourceGraphQuery resource.

        :param resource: The name of the resource to deploy: 'resource_graph_query'
        :paramtype resource: ~typing.Literal['resource_graph_query']
        :param params: The properties of the resource_graph_query resource.
        :paramtype params: ~bicepbuilder.resources.resource_graph.query.ResourceGraphQuery
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ResourceGraphQuery resource.
        :rtype: ~bicepbuilder.resources.resource_graph.query.ResourceGraphQueryModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['resources_deployment_script'],
            params: 'ResourcesDeploymentScript',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ResourcesDeploymentScriptModule':
        """Deploy ResourcesDeploymentScript resource.

        :param resource: The name of the resource to deploy: 'resources_deployment_script'
        :paramtype resource: ~typing.Literal['resources_deployment_script']
        :param params: The properties of the resources_deployment_script resource.
        :paramtype params: ~bicepbuilder.resources.resources.deployment_script.ResourcesDeploymentScript
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.5.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ResourcesDeploymentScript resource.
        :rtype: ~bicepbuilder.resources.resources.deployment_script.ResourcesDeploymentScriptModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['resource_group'],
            params: 'ResourceGroup',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ResourceGroupModule':
        """Deploy ResourceGroup resource.

        :param resource: The name of the resource to deploy: 'resource_group'
        :paramtype resource: ~typing.Literal['resource_group']
        :param params: The properties of the resource_group resource.
        :paramtype params: ~bicepbuilder.resources.resources.resource_group.ResourceGroup
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ResourceGroup resource.
        :rtype: ~bicepbuilder.resources.resources.resource_group.ResourceGroupModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['search_service'],
            params: 'SearchService',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'SearchServiceModule':
        """Deploy SearchService resource.

        :param resource: The name of the resource to deploy: 'search_service'
        :paramtype resource: ~typing.Literal['search_service']
        :param params: The properties of the search_service resource.
        :paramtype params: ~bicepbuilder.resources.search.search_service.SearchService
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.8.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the SearchService resource.
        :rtype: ~bicepbuilder.resources.search.search_service.SearchServiceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['service_bus_namespace'],
            params: 'ServiceBusNamespace',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ServiceBusNamespaceModule':
        """Deploy ServiceBusNamespace resource.

        :param resource: The name of the resource to deploy: 'service_bus_namespace'
        :paramtype resource: ~typing.Literal['service_bus_namespace']
        :param params: The properties of the service_bus_namespace resource.
        :paramtype params: ~bicepbuilder.resources.service_bus.namespace.ServiceBusNamespace
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.10.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ServiceBusNamespace resource.
        :rtype: ~bicepbuilder.resources.service_bus.namespace.ServiceBusNamespaceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['service_fabric_cluster'],
            params: 'ServiceFabricCluster',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ServiceFabricClusterModule':
        """Deploy ServiceFabricCluster resource.

        :param resource: The name of the resource to deploy: 'service_fabric_cluster'
        :paramtype resource: ~typing.Literal['service_fabric_cluster']
        :param params: The properties of the service_fabric_cluster resource.
        :paramtype params: ~bicepbuilder.resources.service_fabric.cluster.ServiceFabricCluster
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ServiceFabricCluster resource.
        :rtype: ~bicepbuilder.resources.service_fabric.cluster.ServiceFabricClusterModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['service_networking_traffic_controller'],
            params: 'ServiceNetworkingTrafficController',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'ServiceNetworkingTrafficControllerModule':
        """Deploy ServiceNetworkingTrafficController resource.

        :param resource: The name of the resource to deploy: 'service_networking_traffic_controller'
        :paramtype resource: ~typing.Literal['service_networking_traffic_controller']
        :param params: The properties of the service_networking_traffic_controller resource.
        :paramtype params: ~bicepbuilder.resources.service_networking.traffic_controller.ServiceNetworkingTrafficController
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the ServiceNetworkingTrafficController resource.
        :rtype: ~bicepbuilder.resources.service_networking.traffic_controller.ServiceNetworkingTrafficControllerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_instance_pool'],
            params: 'SqlInstancePool',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'SqlInstancePoolModule':
        """Deploy SqlInstancePool resource.

        :param resource: The name of the resource to deploy: 'sql_instance_pool'
        :paramtype resource: ~typing.Literal['sql_instance_pool']
        :param params: The properties of the sql_instance_pool resource.
        :paramtype params: ~bicepbuilder.resources.sql.instance_pool.SqlInstancePool
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the SqlInstancePool resource.
        :rtype: ~bicepbuilder.resources.sql.instance_pool.SqlInstancePoolModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_managed_instance'],
            params: 'SqlManagedInstance',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'SqlManagedInstanceModule':
        """Deploy SqlManagedInstance resource.

        :param resource: The name of the resource to deploy: 'sql_managed_instance'
        :paramtype resource: ~typing.Literal['sql_managed_instance']
        :param params: The properties of the sql_managed_instance resource.
        :paramtype params: ~bicepbuilder.resources.sql.managed_instance.SqlManagedInstance
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.1.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the SqlManagedInstance resource.
        :rtype: ~bicepbuilder.resources.sql.managed_instance.SqlManagedInstanceModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_server'],
            params: 'SqlServer',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'SqlServerModule':
        """Deploy SqlServer resource.

        :param resource: The name of the resource to deploy: 'sql_server'
        :paramtype resource: ~typing.Literal['sql_server']
        :param params: The properties of the sql_server resource.
        :paramtype params: ~bicepbuilder.resources.sql.server.SqlServer
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.11.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the SqlServer resource.
        :rtype: ~bicepbuilder.resources.sql.server.SqlServerModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['storage_account'],
            params: 'StorageAccount',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.14.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'StorageAccountModule':
        """Deploy StorageAccount resource.

        :param resource: The name of the resource to deploy: 'storage_account'
        :paramtype resource: ~typing.Literal['storage_account']
        :param params: The properties of the storage_account resource.
        :paramtype params: ~bicepbuilder.resources.storage.storage_account.StorageAccount
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.14.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the StorageAccount resource.
        :rtype: ~bicepbuilder.resources.storage.storage_account.StorageAccountModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['virtual_machine_image_template'],
            params: 'VirtualMachineImageTemplate',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'VirtualMachineImageTemplateModule':
        """Deploy VirtualMachineImageTemplate resource.

        :param resource: The name of the resource to deploy: 'virtual_machine_image_template'
        :paramtype resource: ~typing.Literal['virtual_machine_image_template']
        :param params: The properties of the virtual_machine_image_template resource.
        :paramtype params: ~bicepbuilder.resources.virtual_machine_images.image_template.VirtualMachineImageTemplate
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.4.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the VirtualMachineImageTemplate resource.
        :rtype: ~bicepbuilder.resources.virtual_machine_images.image_template.VirtualMachineImageTemplateModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['web_hosting_environment'],
            params: 'WebHostingEnvironment',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'WebHostingEnvironmentModule':
        """Deploy WebHostingEnvironment resource.

        :param resource: The name of the resource to deploy: 'web_hosting_environment'
        :paramtype resource: ~typing.Literal['web_hosting_environment']
        :param params: The properties of the web_hosting_environment resource.
        :paramtype params: ~bicepbuilder.resources.web.hosting_environment.WebHostingEnvironment
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.2.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the WebHostingEnvironment resource.
        :rtype: ~bicepbuilder.resources.web.hosting_environment.WebHostingEnvironmentModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['web_serverfarm'],
            params: 'WebServerfarm',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'WebServerfarmModule':
        """Deploy WebServerfarm resource.

        :param resource: The name of the resource to deploy: 'web_serverfarm'
        :paramtype resource: ~typing.Literal['web_serverfarm']
        :param params: The properties of the web_serverfarm resource.
        :paramtype params: ~bicepbuilder.resources.web.serverfarm.WebServerfarm
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.3.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the WebServerfarm resource.
        :rtype: ~bicepbuilder.resources.web.serverfarm.WebServerfarmModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['web_site'],
            params: 'WebSite',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.12.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'WebSiteModule':
        """Deploy WebSite resource.

        :param resource: The name of the resource to deploy: 'web_site'
        :paramtype resource: ~typing.Literal['web_site']
        :param params: The properties of the web_site resource.
        :paramtype params: ~bicepbuilder.resources.web.site.WebSite
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.12.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the WebSite resource.
        :rtype: ~bicepbuilder.resources.web.site.WebSiteModule
        """
        ...

    @overload
    def add(
            self,
            resource: Literal['web_static_site'],
            params: 'WebStaticSite',
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> 'WebStaticSiteModule':
        """Deploy WebStaticSite resource.

        :param resource: The name of the resource to deploy: 'web_static_site'
        :paramtype resource: ~typing.Literal['web_static_site']
        :param params: The properties of the web_static_site resource.
        :paramtype params: ~bicepbuilder.resources.web.static_site.WebStaticSite
        :keyword scope: The scope of the deployed resource. Defaults to the scope of the module.
        :paramtype scope: ~typing.Optional[~bicepbuilder.expressions.BicepExpression]
        :keyword depends_on: Any previous deployments that must be complete before this one can start.
        :paramtype depends_on: ~typing.Optional[~typing.Union[str, ~bicepbuilder.expressions.BicepExpression]]
        :keyword str tag: The public repo version of this module that will be used. Defaults to '0.6.0'.
        :keyword batch_size: The level of concurrency allowed for the deployment of this module.
        :paramtype batch_size: ~typing.Optional[int]
        :keyword description: A description to add to the bicep for this module.
        :paramtype description: ~typing.Optional[str]
        :returns: The module reference for the WebStaticSite resource.
        :rtype: ~bicepbuilder.resources.web.static_site.WebStaticSiteModule
        """
        ...

    def add(self, resource: str, params: Dict[str, Any], **kwargs) -> Module:
        try:
            return globals()['_' + resource](self.bicep, params, **kwargs)
        except KeyError:
            raise ValueError(f"Unrecognized resource: '{resource}'.")

