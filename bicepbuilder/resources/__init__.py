from typing import overload, Literal, Optional, Union, IO, Dict, Any

from ..expressions import BicepExpression, Module

from .aad.domain_service import _aad_domain_service, AadDomainService, AadDomainServiceModule
from .alerts_management.action_rule import _alerts_management_action_rule, AlertsManagementActionRule, AlertsManagementActionRuleModule
from .api_management.service import _api_management_service, ApiManagementService, ApiManagementServiceModule
from .app.container_app import _app_container_app, AppContainerApp, AppContainerAppModule
from .app.job import _app_job, AppJob, AppJobModule
from .app.managed_environment import _app_managed_environment, AppManagedEnvironment, AppManagedEnvironmentModule
from .app_configuration.configuration_store import _app_configuration_store, AppConfigurationStore, AppConfigurationStoreModule
from .automation.automation_account import _automation_account, AutomationAccount, AutomationAccountModule
from .batch.batch_account import _batch_account, BatchAccount, BatchAccountModule
from .cache.redis import _cache_redis, CacheRedis, CacheRedisModule
from .cdn.profile import _cdn_profile, CdnProfile, CdnProfileModule
from .cognitive_services.account import _cognitive_services_account, CognitiveServicesAccount, CognitiveServicesAccountModule
from .communication.communication_service import _communication_service, CommunicationService, CommunicationServiceModule
from .communication.email_service import _communication_email_service, CommunicationEmailService, CommunicationEmailServiceModule
from .compute.availability_set import _compute_availability_set, ComputeAvailabilitySet, ComputeAvailabilitySetModule
from .compute.disk import _compute_disk, ComputeDisk, ComputeDiskModule
from .compute.disk_encryption_set import _compute_disk_encryption_set, ComputeDiskEncryptionSet, ComputeDiskEncryptionSetModule
from .compute.gallery import _compute_gallery, ComputeGallery, ComputeGalleryModule
from .compute.image import _compute_image, ComputeImage, ComputeImageModule
from .compute.proximity_placement_group import _compute_proximity_placement_group, ComputeProximityPlacementGroup, ComputeProximityPlacementGroupModule
from .compute.ssh_public_key import _compute_ssh_public_key, ComputeSshPublicKey, ComputeSshPublicKeyModule
from .compute.virtual_machine import _compute_virtual_machine, ComputeVirtualMachine, ComputeVirtualMachineModule
from .compute.virtual_machine_scale_set import _compute_virtual_machine_scale_set, ComputeVirtualMachineScaleSet, ComputeVirtualMachineScaleSetModule
from .consumption.budget import _consumption_budget, ConsumptionBudget, ConsumptionBudgetModule
from .container_instance.container_group import _container_instance_container_group, ContainerInstanceContainerGroup, ContainerInstanceContainerGroupModule
from .container_registry.registry import _container_registry, ContainerRegistry, ContainerRegistryModule
from .container_service.managed_cluster import _container_service_managed_cluster, ContainerServiceManagedCluster, ContainerServiceManagedClusterModule
from .data_factory.factory import _data_factory, DataFactory, DataFactoryModule
from .data_protection.backup_vault import _data_protection_backup_vault, DataProtectionBackupVault, DataProtectionBackupVaultModule
from .databricks.access_connector import _databricks_access_connector, DatabricksAccessConnector, DatabricksAccessConnectorModule
from .databricks.workspace import _databricks_workspace, DatabricksWorkspace, DatabricksWorkspaceModule
from .db_for_my_sql.flexible_server import _db_for_my_sql_flexible_server, DbForMySqlFlexibleServer, DbForMySqlFlexibleServerModule
from .db_for_postgre_sql.flexible_server import _db_for_postgre_sql_flexible_server, DbForPostgreSqlFlexibleServer, DbForPostgreSqlFlexibleServerModule
from .desktop_virtualization.application_group import _desktop_virtualization_application_group, DesktopVirtualizationApplicationGroup, DesktopVirtualizationApplicationGroupModule
from .desktop_virtualization.host_pool import _desktop_virtualization_host_pool, DesktopVirtualizationHostPool, DesktopVirtualizationHostPoolModule
from .desktop_virtualization.scaling_plan import _desktop_virtualization_scaling_plan, DesktopVirtualizationScalingPlan, DesktopVirtualizationScalingPlanModule
from .desktop_virtualization.workspace import _desktop_virtualization_workspace, DesktopVirtualizationWorkspace, DesktopVirtualizationWorkspaceModule
from .dev_ops_infrastructure.pool import _dev_ops_infrastructure_pool, DevOpsInfrastructurePool, DevOpsInfrastructurePoolModule
from .dev_test_lab.lab import _dev_test_lab, DevTestLab, DevTestLabModule
from .digital_twins.digital_twins_instance import _digital_twins_instance, DigitalTwinsInstance, DigitalTwinsInstanceModule
from .document_db.database_account import _document_db_database_account, DocumentDbDatabaseAccount, DocumentDbDatabaseAccountModule
from .document_db.mongo_cluster import _document_db_mongo_cluster, DocumentDbMongoCluster, DocumentDbMongoClusterModule
from .elastic_san.elastic_san import _elastic_san, ElasticSan, ElasticSanModule
from .event_grid.domain import _event_grid_domain, EventGridDomain, EventGridDomainModule
from .event_grid.namespace import _event_grid_namespace, EventGridNamespace, EventGridNamespaceModule
from .event_grid.system_topic import _event_grid_system_topic, EventGridSystemTopic, EventGridSystemTopicModule
from .event_grid.topic import _event_grid_topic, EventGridTopic, EventGridTopicModule
from .event_hub.namespace import _event_hub_namespace, EventHubNamespace, EventHubNamespaceModule
from .fabric.capacity import _fabric_capacity, FabricCapacity, FabricCapacityModule
from .hybrid_compute.machine import _hybrid_compute_machine, HybridComputeMachine, HybridComputeMachineModule
from .insights.action_group import _insights_action_group, InsightsActionGroup, InsightsActionGroupModule
from .insights.activity_log_alert import _insights_activity_log_alert, InsightsActivityLogAlert, InsightsActivityLogAlertModule
from .insights.component import _insights_component, InsightsComponent, InsightsComponentModule
from .insights.data_collection_endpoint import _insights_data_collection_endpoint, InsightsDataCollectionEndpoint, InsightsDataCollectionEndpointModule
from .insights.data_collection_rule import _insights_data_collection_rule, InsightsDataCollectionRule, InsightsDataCollectionRuleModule
from .insights.diagnostic_setting import _insights_diagnostic_setting, InsightsDiagnosticSetting, InsightsDiagnosticSettingModule
from .insights.metric_alert import _insights_metric_alert, InsightsMetricAlert, InsightsMetricAlertModule
from .insights.private_link_scope import _insights_private_link_scope, InsightsPrivateLinkScope, InsightsPrivateLinkScopeModule
from .insights.scheduled_query_rule import _insights_scheduled_query_rule, InsightsScheduledQueryRule, InsightsScheduledQueryRuleModule
from .insights.webtest import _insights_webtest, InsightsWebtest, InsightsWebtestModule
from .key_vault.vault import _key_vault, KeyVault, KeyVaultModule
from .kubernetes_configuration.extension import _kubernetes_configuration_extension, KubernetesConfigurationExtension, KubernetesConfigurationExtensionModule
from .kubernetes_configuration.flux_configuration import _kubernetes_configuration_flux_configuration, KubernetesConfigurationFluxConfiguration, KubernetesConfigurationFluxConfigurationModule
from .kusto.cluster import _kusto_cluster, KustoCluster, KustoClusterModule
from .load_test_service.load_test import _load_test_service_load_test, LoadTestServiceLoadTest, LoadTestServiceLoadTestModule
from .logic.workflow import _logic_workflow, LogicWorkflow, LogicWorkflowModule
from .machine_learning_services.workspace import _machine_learning_services_workspace, MachineLearningServicesWorkspace, MachineLearningServicesWorkspaceModule
from .maintenance.maintenance_configuration import _maintenance_configuration, MaintenanceConfiguration, MaintenanceConfigurationModule
from .managed_identity.user_assigned_identity import _managed_identity_user_assigned_identity, ManagedIdentityUserAssignedIdentity, ManagedIdentityUserAssignedIdentityModule
from .management.management_group import _management_group, ManagementGroup, ManagementGroupModule
from .net_app.net_app_account import _net_app_account, NetAppAccount, NetAppAccountModule
from .network.application_gateway import _network_application_gateway, NetworkApplicationGateway, NetworkApplicationGatewayModule
from .network.application_gateway_web_application_firewall_policy import _network_application_gateway_web_application_firewall_policy, NetworkApplicationGatewayWebApplicationFirewallPolicy, NetworkApplicationGatewayWebApplicationFirewallPolicyModule
from .network.application_security_group import _network_application_security_group, NetworkApplicationSecurityGroup, NetworkApplicationSecurityGroupModule
from .network.azure_firewall import _network_azure_firewall, NetworkAzureFirewall, NetworkAzureFirewallModule
from .network.bastion_host import _network_bastion_host, NetworkBastionHost, NetworkBastionHostModule
from .network.connection import _network_connection, NetworkConnection, NetworkConnectionModule
from .network.ddos_protection_plan import _network_ddos_protection_plan, NetworkDdosProtectionPlan, NetworkDdosProtectionPlanModule
from .network.dns_forwarding_ruleset import _network_dns_forwarding_ruleset, NetworkDnsForwardingRuleset, NetworkDnsForwardingRulesetModule
from .network.dns_resolver import _network_dns_resolver, NetworkDnsResolver, NetworkDnsResolverModule
from .network.dns_zone import _network_dns_zone, NetworkDnsZone, NetworkDnsZoneModule
from .network.express_route_circuit import _network_express_route_circuit, NetworkExpressRouteCircuit, NetworkExpressRouteCircuitModule
from .network.express_route_gateway import _network_express_route_gateway, NetworkExpressRouteGateway, NetworkExpressRouteGatewayModule
from .network.firewall_policy import _network_firewall_policy, NetworkFirewallPolicy, NetworkFirewallPolicyModule
from .network.front_door import _network_front_door, NetworkFrontDoor, NetworkFrontDoorModule
from .network.front_door_web_application_firewall_policy import _network_front_door_web_application_firewall_policy, NetworkFrontDoorWebApplicationFirewallPolicy, NetworkFrontDoorWebApplicationFirewallPolicyModule
from .network.ip_group import _network_ip_group, NetworkIpGroup, NetworkIpGroupModule
from .network.load_balancer import _network_load_balancer, NetworkLoadBalancer, NetworkLoadBalancerModule
from .network.local_network_gateway import _network_local_network_gateway, NetworkLocalNetworkGateway, NetworkLocalNetworkGatewayModule
from .network.nat_gateway import _network_nat_gateway, NetworkNatGateway, NetworkNatGatewayModule
from .network.network_interface import _network_interface, NetworkInterface, NetworkInterfaceModule
from .network.network_manager import _network_manager, NetworkManager, NetworkManagerModule
from .network.network_security_group import _network_security_group, NetworkSecurityGroup, NetworkSecurityGroupModule
from .network.network_watcher import _network_watcher, NetworkWatcher, NetworkWatcherModule
from .network.p2s_vpn_gateway import _network_p2s_vpn_gateway, NetworkP2SVpnGateway, NetworkP2SVpnGatewayModule
from .network.private_dns_zone import _network_private_dns_zone, NetworkPrivateDnsZone, NetworkPrivateDnsZoneModule
from .network.private_endpoint import _network_private_endpoint, NetworkPrivateEndpoint, NetworkPrivateEndpointModule
from .network.private_link_service import _network_private_link_service, NetworkPrivateLinkService, NetworkPrivateLinkServiceModule
from .network.public_ip_address import _network_public_ip_address, NetworkPublicIpAddress, NetworkPublicIpAddressModule
from .network.public_ip_prefix import _network_public_ip_prefix, NetworkPublicIpPrefix, NetworkPublicIpPrefixModule
from .network.route_table import _network_route_table, NetworkRouteTable, NetworkRouteTableModule
from .network.service_endpoint_policy import _network_service_endpoint_policy, NetworkServiceEndpointPolicy, NetworkServiceEndpointPolicyModule
from .network.trafficmanagerprofile import _network_trafficmanagerprofile, NetworkTrafficmanagerprofile, NetworkTrafficmanagerprofileModule
from .network.virtual_hub import _network_virtual_hub, NetworkVirtualHub, NetworkVirtualHubModule
from .network.virtual_network_gateway import _network_virtual_network_gateway, NetworkVirtualNetworkGateway, NetworkVirtualNetworkGatewayModule
from .network.virtual_wan import _network_virtual_wan, NetworkVirtualWan, NetworkVirtualWanModule
from .network.vpn_gateway import _network_vpn_gateway, NetworkVpnGateway, NetworkVpnGatewayModule
from .network.vpn_server_configuration import _network_vpn_server_configuration, NetworkVpnServerConfiguration, NetworkVpnServerConfigurationModule
from .network.vpn_site import _network_vpn_site, NetworkVpnSite, NetworkVpnSiteModule
from .operational_insights.workspace import _operational_insights_workspace, OperationalInsightsWorkspace, OperationalInsightsWorkspaceModule
from .operations_management.solution import _operations_management_solution, OperationsManagementSolution, OperationsManagementSolutionModule
from .portal.dashboard import _portal_dashboard, PortalDashboard, PortalDashboardModule
from .power_bi_dedicated.capacity import _power_bi_dedicated_capacity, PowerBiDedicatedCapacity, PowerBiDedicatedCapacityModule
from .purview.account import _purview_account, PurviewAccount, PurviewAccountModule
from .recovery_services.vault import _recovery_services_vault, RecoveryServicesVault, RecoveryServicesVaultModule
from .resource_graph.query import _resource_graph_query, ResourceGraphQuery, ResourceGraphQueryModule
from .resources.deployment_script import _resources_deployment_script, ResourcesDeploymentScript, ResourcesDeploymentScriptModule
from .resources.resource_group import _resource_group, ResourceGroup, ResourceGroupModule
from .search.search_service import _search_service, SearchService, SearchServiceModule
from .service_bus.namespace import _service_bus_namespace, ServiceBusNamespace, ServiceBusNamespaceModule
from .service_fabric.cluster import _service_fabric_cluster, ServiceFabricCluster, ServiceFabricClusterModule
from .service_networking.traffic_controller import _service_networking_traffic_controller, ServiceNetworkingTrafficController, ServiceNetworkingTrafficControllerModule
from .sql.instance_pool import _sql_instance_pool, SqlInstancePool, SqlInstancePoolModule
from .sql.managed_instance import _sql_managed_instance, SqlManagedInstance, SqlManagedInstanceModule
from .sql.server import _sql_server, SqlServer, SqlServerModule
from .storage.storage_account import _storage_account, StorageAccount, StorageAccountModule
from .virtual_machine_images.image_template import _virtual_machine_image_template, VirtualMachineImageTemplate, VirtualMachineImageTemplateModule
from .web.hosting_environment import _web_hosting_environment, WebHostingEnvironment, WebHostingEnvironmentModule
from .web.serverfarm import _web_serverfarm, WebServerfarm, WebServerfarmModule
from .web.site import _web_site, WebSite, WebSiteModule
from .web.static_site import _web_static_site, WebStaticSite, WebStaticSiteModule

__all__ = [
    'AadDomainService'
    'AadDomainServiceModule'
    'AlertsManagementActionRule'
    'AlertsManagementActionRuleModule'
    'ApiManagementService'
    'ApiManagementServiceModule'
    'AppContainerApp'
    'AppContainerAppModule'
    'AppJob'
    'AppJobModule'
    'AppManagedEnvironment'
    'AppManagedEnvironmentModule'
    'AppConfigurationStore'
    'AppConfigurationStoreModule'
    'AutomationAccount'
    'AutomationAccountModule'
    'BatchAccount'
    'BatchAccountModule'
    'CacheRedis'
    'CacheRedisModule'
    'CdnProfile'
    'CdnProfileModule'
    'CognitiveServicesAccount'
    'CognitiveServicesAccountModule'
    'CommunicationService'
    'CommunicationServiceModule'
    'CommunicationEmailService'
    'CommunicationEmailServiceModule'
    'ComputeAvailabilitySet'
    'ComputeAvailabilitySetModule'
    'ComputeDisk'
    'ComputeDiskModule'
    'ComputeDiskEncryptionSet'
    'ComputeDiskEncryptionSetModule'
    'ComputeGallery'
    'ComputeGalleryModule'
    'ComputeImage'
    'ComputeImageModule'
    'ComputeProximityPlacementGroup'
    'ComputeProximityPlacementGroupModule'
    'ComputeSshPublicKey'
    'ComputeSshPublicKeyModule'
    'ComputeVirtualMachine'
    'ComputeVirtualMachineModule'
    'ComputeVirtualMachineScaleSet'
    'ComputeVirtualMachineScaleSetModule'
    'ConsumptionBudget'
    'ConsumptionBudgetModule'
    'ContainerInstanceContainerGroup'
    'ContainerInstanceContainerGroupModule'
    'ContainerRegistry'
    'ContainerRegistryModule'
    'ContainerServiceManagedCluster'
    'ContainerServiceManagedClusterModule'
    'DataFactory'
    'DataFactoryModule'
    'DataProtectionBackupVault'
    'DataProtectionBackupVaultModule'
    'DatabricksAccessConnector'
    'DatabricksAccessConnectorModule'
    'DatabricksWorkspace'
    'DatabricksWorkspaceModule'
    'DbForMySqlFlexibleServer'
    'DbForMySqlFlexibleServerModule'
    'DbForPostgreSqlFlexibleServer'
    'DbForPostgreSqlFlexibleServerModule'
    'DesktopVirtualizationApplicationGroup'
    'DesktopVirtualizationApplicationGroupModule'
    'DesktopVirtualizationHostPool'
    'DesktopVirtualizationHostPoolModule'
    'DesktopVirtualizationScalingPlan'
    'DesktopVirtualizationScalingPlanModule'
    'DesktopVirtualizationWorkspace'
    'DesktopVirtualizationWorkspaceModule'
    'DevOpsInfrastructurePool'
    'DevOpsInfrastructurePoolModule'
    'DevTestLab'
    'DevTestLabModule'
    'DigitalTwinsInstance'
    'DigitalTwinsInstanceModule'
    'DocumentDbDatabaseAccount'
    'DocumentDbDatabaseAccountModule'
    'DocumentDbMongoCluster'
    'DocumentDbMongoClusterModule'
    'ElasticSan'
    'ElasticSanModule'
    'EventGridDomain'
    'EventGridDomainModule'
    'EventGridNamespace'
    'EventGridNamespaceModule'
    'EventGridSystemTopic'
    'EventGridSystemTopicModule'
    'EventGridTopic'
    'EventGridTopicModule'
    'EventHubNamespace'
    'EventHubNamespaceModule'
    'FabricCapacity'
    'FabricCapacityModule'
    'HybridComputeMachine'
    'HybridComputeMachineModule'
    'InsightsActionGroup'
    'InsightsActionGroupModule'
    'InsightsActivityLogAlert'
    'InsightsActivityLogAlertModule'
    'InsightsComponent'
    'InsightsComponentModule'
    'InsightsDataCollectionEndpoint'
    'InsightsDataCollectionEndpointModule'
    'InsightsDataCollectionRule'
    'InsightsDataCollectionRuleModule'
    'InsightsDiagnosticSetting'
    'InsightsDiagnosticSettingModule'
    'InsightsMetricAlert'
    'InsightsMetricAlertModule'
    'InsightsPrivateLinkScope'
    'InsightsPrivateLinkScopeModule'
    'InsightsScheduledQueryRule'
    'InsightsScheduledQueryRuleModule'
    'InsightsWebtest'
    'InsightsWebtestModule'
    'KeyVault'
    'KeyVaultModule'
    'KubernetesConfigurationExtension'
    'KubernetesConfigurationExtensionModule'
    'KubernetesConfigurationFluxConfiguration'
    'KubernetesConfigurationFluxConfigurationModule'
    'KustoCluster'
    'KustoClusterModule'
    'LoadTestServiceLoadTest'
    'LoadTestServiceLoadTestModule'
    'LogicWorkflow'
    'LogicWorkflowModule'
    'MachineLearningServicesWorkspace'
    'MachineLearningServicesWorkspaceModule'
    'MaintenanceConfiguration'
    'MaintenanceConfigurationModule'
    'ManagedIdentityUserAssignedIdentity'
    'ManagedIdentityUserAssignedIdentityModule'
    'ManagementGroup'
    'ManagementGroupModule'
    'NetAppAccount'
    'NetAppAccountModule'
    'NetworkApplicationGateway'
    'NetworkApplicationGatewayModule'
    'NetworkApplicationGatewayWebApplicationFirewallPolicy'
    'NetworkApplicationGatewayWebApplicationFirewallPolicyModule'
    'NetworkApplicationSecurityGroup'
    'NetworkApplicationSecurityGroupModule'
    'NetworkAzureFirewall'
    'NetworkAzureFirewallModule'
    'NetworkBastionHost'
    'NetworkBastionHostModule'
    'NetworkConnection'
    'NetworkConnectionModule'
    'NetworkDdosProtectionPlan'
    'NetworkDdosProtectionPlanModule'
    'NetworkDnsForwardingRuleset'
    'NetworkDnsForwardingRulesetModule'
    'NetworkDnsResolver'
    'NetworkDnsResolverModule'
    'NetworkDnsZone'
    'NetworkDnsZoneModule'
    'NetworkExpressRouteCircuit'
    'NetworkExpressRouteCircuitModule'
    'NetworkExpressRouteGateway'
    'NetworkExpressRouteGatewayModule'
    'NetworkFirewallPolicy'
    'NetworkFirewallPolicyModule'
    'NetworkFrontDoor'
    'NetworkFrontDoorModule'
    'NetworkFrontDoorWebApplicationFirewallPolicy'
    'NetworkFrontDoorWebApplicationFirewallPolicyModule'
    'NetworkIpGroup'
    'NetworkIpGroupModule'
    'NetworkLoadBalancer'
    'NetworkLoadBalancerModule'
    'NetworkLocalNetworkGateway'
    'NetworkLocalNetworkGatewayModule'
    'NetworkNatGateway'
    'NetworkNatGatewayModule'
    'NetworkInterface'
    'NetworkInterfaceModule'
    'NetworkManager'
    'NetworkManagerModule'
    'NetworkSecurityGroup'
    'NetworkSecurityGroupModule'
    'NetworkWatcher'
    'NetworkWatcherModule'
    'NetworkP2SVpnGateway'
    'NetworkP2SVpnGatewayModule'
    'NetworkPrivateDnsZone'
    'NetworkPrivateDnsZoneModule'
    'NetworkPrivateEndpoint'
    'NetworkPrivateEndpointModule'
    'NetworkPrivateLinkService'
    'NetworkPrivateLinkServiceModule'
    'NetworkPublicIpAddress'
    'NetworkPublicIpAddressModule'
    'NetworkPublicIpPrefix'
    'NetworkPublicIpPrefixModule'
    'NetworkRouteTable'
    'NetworkRouteTableModule'
    'NetworkServiceEndpointPolicy'
    'NetworkServiceEndpointPolicyModule'
    'NetworkTrafficmanagerprofile'
    'NetworkTrafficmanagerprofileModule'
    'NetworkVirtualHub'
    'NetworkVirtualHubModule'
    'NetworkVirtualNetworkGateway'
    'NetworkVirtualNetworkGatewayModule'
    'NetworkVirtualWan'
    'NetworkVirtualWanModule'
    'NetworkVpnGateway'
    'NetworkVpnGatewayModule'
    'NetworkVpnServerConfiguration'
    'NetworkVpnServerConfigurationModule'
    'NetworkVpnSite'
    'NetworkVpnSiteModule'
    'OperationalInsightsWorkspace'
    'OperationalInsightsWorkspaceModule'
    'OperationsManagementSolution'
    'OperationsManagementSolutionModule'
    'PortalDashboard'
    'PortalDashboardModule'
    'PowerBiDedicatedCapacity'
    'PowerBiDedicatedCapacityModule'
    'PurviewAccount'
    'PurviewAccountModule'
    'RecoveryServicesVault'
    'RecoveryServicesVaultModule'
    'ResourceGraphQuery'
    'ResourceGraphQueryModule'
    'ResourcesDeploymentScript'
    'ResourcesDeploymentScriptModule'
    'ResourceGroup'
    'ResourceGroupModule'
    'SearchService'
    'SearchServiceModule'
    'ServiceBusNamespace'
    'ServiceBusNamespaceModule'
    'ServiceFabricCluster'
    'ServiceFabricClusterModule'
    'ServiceNetworkingTrafficController'
    'ServiceNetworkingTrafficControllerModule'
    'SqlInstancePool'
    'SqlInstancePoolModule'
    'SqlManagedInstance'
    'SqlManagedInstanceModule'
    'SqlServer'
    'SqlServerModule'
    'StorageAccount'
    'StorageAccountModule'
    'VirtualMachineImageTemplate'
    'VirtualMachineImageTemplateModule'
    'WebHostingEnvironment'
    'WebHostingEnvironmentModule'
    'WebServerfarm'
    'WebServerfarmModule'
    'WebSite'
    'WebSiteModule'
    'WebStaticSite'
    'WebStaticSiteModule'
]

class _AddResourceMixin:
    bicep: IO[str]

    @overload
    def add(
            self,
            resource: Literal['aad_domain_service'],
            params: AadDomainService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AadDomainServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['alerts_management_action_rule'],
            params: AlertsManagementActionRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AlertsManagementActionRuleModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['api_management_service'],
            params: ApiManagementService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ApiManagementServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['app_container_app'],
            params: AppContainerApp,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppContainerAppModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['app_job'],
            params: AppJob,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppJobModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['app_managed_environment'],
            params: AppManagedEnvironment,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppManagedEnvironmentModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['app_configuration_store'],
            params: AppConfigurationStore,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppConfigurationStoreModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['automation_account'],
            params: AutomationAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AutomationAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['batch_account'],
            params: BatchAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> BatchAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['cache_redis'],
            params: CacheRedis,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CacheRedisModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['cdn_profile'],
            params: CdnProfile,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CdnProfileModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['cognitive_services_account'],
            params: CognitiveServicesAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CognitiveServicesAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['communication_service'],
            params: CommunicationService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CommunicationServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['communication_email_service'],
            params: CommunicationEmailService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CommunicationEmailServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_availability_set'],
            params: ComputeAvailabilitySet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeAvailabilitySetModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_disk'],
            params: ComputeDisk,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeDiskModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_disk_encryption_set'],
            params: ComputeDiskEncryptionSet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeDiskEncryptionSetModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_gallery'],
            params: ComputeGallery,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeGalleryModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_image'],
            params: ComputeImage,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeImageModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_proximity_placement_group'],
            params: ComputeProximityPlacementGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeProximityPlacementGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_ssh_public_key'],
            params: ComputeSshPublicKey,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeSshPublicKeyModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_virtual_machine'],
            params: ComputeVirtualMachine,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeVirtualMachineModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['compute_virtual_machine_scale_set'],
            params: ComputeVirtualMachineScaleSet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeVirtualMachineScaleSetModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['consumption_budget'],
            params: ConsumptionBudget,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ConsumptionBudgetModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['container_instance_container_group'],
            params: ContainerInstanceContainerGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerInstanceContainerGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['container_registry'],
            params: ContainerRegistry,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerRegistryModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['container_service_managed_cluster'],
            params: ContainerServiceManagedCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerServiceManagedClusterModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['data_factory'],
            params: DataFactory,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DataFactoryModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['data_protection_backup_vault'],
            params: DataProtectionBackupVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DataProtectionBackupVaultModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['databricks_access_connector'],
            params: DatabricksAccessConnector,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DatabricksAccessConnectorModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['databricks_workspace'],
            params: DatabricksWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DatabricksWorkspaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['db_for_my_sql_flexible_server'],
            params: DbForMySqlFlexibleServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DbForMySqlFlexibleServerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['db_for_postgre_sql_flexible_server'],
            params: DbForPostgreSqlFlexibleServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DbForPostgreSqlFlexibleServerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_application_group'],
            params: DesktopVirtualizationApplicationGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationApplicationGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_host_pool'],
            params: DesktopVirtualizationHostPool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationHostPoolModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_scaling_plan'],
            params: DesktopVirtualizationScalingPlan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationScalingPlanModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['desktop_virtualization_workspace'],
            params: DesktopVirtualizationWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationWorkspaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['dev_ops_infrastructure_pool'],
            params: DevOpsInfrastructurePool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DevOpsInfrastructurePoolModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['dev_test_lab'],
            params: DevTestLab,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DevTestLabModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['digital_twins_instance'],
            params: DigitalTwinsInstance,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DigitalTwinsInstanceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['document_db_database_account'],
            params: DocumentDbDatabaseAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DocumentDbDatabaseAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['document_db_mongo_cluster'],
            params: DocumentDbMongoCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DocumentDbMongoClusterModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['elastic_san'],
            params: ElasticSan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ElasticSanModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_domain'],
            params: EventGridDomain,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridDomainModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_namespace'],
            params: EventGridNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridNamespaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_system_topic'],
            params: EventGridSystemTopic,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridSystemTopicModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['event_grid_topic'],
            params: EventGridTopic,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridTopicModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['event_hub_namespace'],
            params: EventHubNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventHubNamespaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['fabric_capacity'],
            params: FabricCapacity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> FabricCapacityModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['hybrid_compute_machine'],
            params: HybridComputeMachine,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> HybridComputeMachineModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_action_group'],
            params: InsightsActionGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsActionGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_activity_log_alert'],
            params: InsightsActivityLogAlert,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsActivityLogAlertModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_component'],
            params: InsightsComponent,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsComponentModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_data_collection_endpoint'],
            params: InsightsDataCollectionEndpoint,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDataCollectionEndpointModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_data_collection_rule'],
            params: InsightsDataCollectionRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDataCollectionRuleModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_diagnostic_setting'],
            params: InsightsDiagnosticSetting,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDiagnosticSettingModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_metric_alert'],
            params: InsightsMetricAlert,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsMetricAlertModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_private_link_scope'],
            params: InsightsPrivateLinkScope,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsPrivateLinkScopeModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_scheduled_query_rule'],
            params: InsightsScheduledQueryRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsScheduledQueryRuleModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['insights_webtest'],
            params: InsightsWebtest,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsWebtestModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['key_vault'],
            params: KeyVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KeyVaultModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['kubernetes_configuration_extension'],
            params: KubernetesConfigurationExtension,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KubernetesConfigurationExtensionModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['kubernetes_configuration_flux_configuration'],
            params: KubernetesConfigurationFluxConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KubernetesConfigurationFluxConfigurationModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['kusto_cluster'],
            params: KustoCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KustoClusterModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['load_test_service_load_test'],
            params: LoadTestServiceLoadTest,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> LoadTestServiceLoadTestModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['logic_workflow'],
            params: LogicWorkflow,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> LogicWorkflowModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['machine_learning_services_workspace'],
            params: MachineLearningServicesWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> MachineLearningServicesWorkspaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['maintenance_configuration'],
            params: MaintenanceConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> MaintenanceConfigurationModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['managed_identity_user_assigned_identity'],
            params: ManagedIdentityUserAssignedIdentity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ManagedIdentityUserAssignedIdentityModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['management_group'],
            params: ManagementGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ManagementGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['net_app_account'],
            params: NetAppAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetAppAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_gateway'],
            params: NetworkApplicationGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_gateway_web_application_firewall_policy'],
            params: NetworkApplicationGatewayWebApplicationFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationGatewayWebApplicationFirewallPolicyModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_application_security_group'],
            params: NetworkApplicationSecurityGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationSecurityGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_azure_firewall'],
            params: NetworkAzureFirewall,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkAzureFirewallModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_bastion_host'],
            params: NetworkBastionHost,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkBastionHostModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_connection'],
            params: NetworkConnection,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkConnectionModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_ddos_protection_plan'],
            params: NetworkDdosProtectionPlan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDdosProtectionPlanModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_forwarding_ruleset'],
            params: NetworkDnsForwardingRuleset,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsForwardingRulesetModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_resolver'],
            params: NetworkDnsResolver,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsResolverModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_dns_zone'],
            params: NetworkDnsZone,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsZoneModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_express_route_circuit'],
            params: NetworkExpressRouteCircuit,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkExpressRouteCircuitModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_express_route_gateway'],
            params: NetworkExpressRouteGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkExpressRouteGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_firewall_policy'],
            params: NetworkFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFirewallPolicyModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_front_door'],
            params: NetworkFrontDoor,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFrontDoorModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_front_door_web_application_firewall_policy'],
            params: NetworkFrontDoorWebApplicationFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFrontDoorWebApplicationFirewallPolicyModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_ip_group'],
            params: NetworkIpGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkIpGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_load_balancer'],
            params: NetworkLoadBalancer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkLoadBalancerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_local_network_gateway'],
            params: NetworkLocalNetworkGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkLocalNetworkGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_nat_gateway'],
            params: NetworkNatGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '1.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkNatGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_interface'],
            params: NetworkInterface,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkInterfaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_manager'],
            params: NetworkManager,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkManagerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_security_group'],
            params: NetworkSecurityGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkSecurityGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_watcher'],
            params: NetworkWatcher,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkWatcherModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_p2s_vpn_gateway'],
            params: NetworkP2SVpnGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkP2SVpnGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_dns_zone'],
            params: NetworkPrivateDnsZone,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateDnsZoneModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_endpoint'],
            params: NetworkPrivateEndpoint,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateEndpointModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_private_link_service'],
            params: NetworkPrivateLinkService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateLinkServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_public_ip_address'],
            params: NetworkPublicIpAddress,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPublicIpAddressModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_public_ip_prefix'],
            params: NetworkPublicIpPrefix,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPublicIpPrefixModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_route_table'],
            params: NetworkRouteTable,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkRouteTableModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_service_endpoint_policy'],
            params: NetworkServiceEndpointPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkServiceEndpointPolicyModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_trafficmanagerprofile'],
            params: NetworkTrafficmanagerprofile,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkTrafficmanagerprofileModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_hub'],
            params: NetworkVirtualHub,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualHubModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_network_gateway'],
            params: NetworkVirtualNetworkGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualNetworkGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_virtual_wan'],
            params: NetworkVirtualWan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualWanModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_gateway'],
            params: NetworkVpnGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnGatewayModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_server_configuration'],
            params: NetworkVpnServerConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnServerConfigurationModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['network_vpn_site'],
            params: NetworkVpnSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnSiteModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['operational_insights_workspace'],
            params: OperationalInsightsWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> OperationalInsightsWorkspaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['operations_management_solution'],
            params: OperationsManagementSolution,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> OperationsManagementSolutionModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['portal_dashboard'],
            params: PortalDashboard,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PortalDashboardModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['power_bi_dedicated_capacity'],
            params: PowerBiDedicatedCapacity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PowerBiDedicatedCapacityModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['purview_account'],
            params: PurviewAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PurviewAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['recovery_services_vault'],
            params: RecoveryServicesVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> RecoveryServicesVaultModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['resource_graph_query'],
            params: ResourceGraphQuery,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourceGraphQueryModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['resources_deployment_script'],
            params: ResourcesDeploymentScript,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourcesDeploymentScriptModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['resource_group'],
            params: ResourceGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourceGroupModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['search_service'],
            params: SearchService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SearchServiceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['service_bus_namespace'],
            params: ServiceBusNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceBusNamespaceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['service_fabric_cluster'],
            params: ServiceFabricCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceFabricClusterModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['service_networking_traffic_controller'],
            params: ServiceNetworkingTrafficController,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceNetworkingTrafficControllerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_instance_pool'],
            params: SqlInstancePool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlInstancePoolModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_managed_instance'],
            params: SqlManagedInstance,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlManagedInstanceModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['sql_server'],
            params: SqlServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlServerModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['storage_account'],
            params: StorageAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.14.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> StorageAccountModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['virtual_machine_image_template'],
            params: VirtualMachineImageTemplate,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> VirtualMachineImageTemplateModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['web_hosting_environment'],
            params: WebHostingEnvironment,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebHostingEnvironmentModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['web_serverfarm'],
            params: WebServerfarm,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebServerfarmModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['web_site'],
            params: WebSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.12.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebSiteModule:
        ...

    @overload
    def add(
            self,
            resource: Literal['web_static_site'],
            params: WebStaticSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebStaticSiteModule:
        ...

    def add(self, resource: str, params: Dict[str, Any], **kwargs) -> Module:
        try:
            return globals()['_' + resource](self.bicep, params, **kwargs)
        except KeyError:
            raise ValueError(f"Unrecognized resource: '{resource}'.")

