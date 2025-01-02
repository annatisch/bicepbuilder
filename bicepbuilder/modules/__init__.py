from typing import overload, Literal, Optional, Union, IO, Dict, Any
from ..expressions import BicepExpression, Module
from .aad.domain_service import aad_domain_service, AadDomainService, AadDomainServiceBicep
from .alerts_management.action_rule import alerts_management_action_rule, AlertsManagementActionRule, AlertsManagementActionRuleBicep
from .api_management.service import api_management_service, ApiManagementService, ApiManagementServiceBicep
from .app.container_app import app_container_app, AppContainerApp, AppContainerAppBicep
from .app.job import app_job, AppJob, AppJobBicep
from .app.managed_environment import app_managed_environment, AppManagedEnvironment, AppManagedEnvironmentBicep
from .app_configuration.configuration_store import app_configuration_store, AppConfigurationStore, AppConfigurationStoreBicep
from .automation.automation_account import automation_account, AutomationAccount, AutomationAccountBicep
from .batch.batch_account import batch_account, BatchAccount, BatchAccountBicep
from .cache.redis import cache_redis, CacheRedis, CacheRedisBicep
from .cdn.profile import cdn_profile, CdnProfile, CdnProfileBicep
from .cognitive_services.account import cognitive_services_account, CognitiveServicesAccount, CognitiveServicesAccountBicep
from .communication.communication_service import communication_service, CommunicationService, CommunicationServiceBicep
from .communication.email_service import communication_email_service, CommunicationEmailService, CommunicationEmailServiceBicep
from .compute.availability_set import compute_availability_set, ComputeAvailabilitySet, ComputeAvailabilitySetBicep
from .compute.disk import compute_disk, ComputeDisk, ComputeDiskBicep
from .compute.disk_encryption_set import compute_disk_encryption_set, ComputeDiskEncryptionSet, ComputeDiskEncryptionSetBicep
from .compute.gallery import compute_gallery, ComputeGallery, ComputeGalleryBicep
from .compute.image import compute_image, ComputeImage, ComputeImageBicep
from .compute.proximity_placement_group import compute_proximity_placement_group, ComputeProximityPlacementGroup, ComputeProximityPlacementGroupBicep
from .compute.ssh_public_key import compute_ssh_public_key, ComputeSshPublicKey, ComputeSshPublicKeyBicep
from .compute.virtual_machine import compute_virtual_machine, ComputeVirtualMachine, ComputeVirtualMachineBicep
from .compute.virtual_machine_scale_set import compute_virtual_machine_scale_set, ComputeVirtualMachineScaleSet, ComputeVirtualMachineScaleSetBicep
from .consumption.budget import consumption_budget, ConsumptionBudget, ConsumptionBudgetBicep
from .container_instance.container_group import container_instance_container_group, ContainerInstanceContainerGroup, ContainerInstanceContainerGroupBicep
from .container_registry.registry import container_registry, ContainerRegistry, ContainerRegistryBicep
from .container_service.managed_cluster import container_service_managed_cluster, ContainerServiceManagedCluster, ContainerServiceManagedClusterBicep
from .data_factory.factory import data_factory, DataFactory, DataFactoryBicep
from .data_protection.backup_vault import data_protection_backup_vault, DataProtectionBackupVault, DataProtectionBackupVaultBicep
from .databricks.access_connector import databricks_access_connector, DatabricksAccessConnector, DatabricksAccessConnectorBicep
from .databricks.workspace import databricks_workspace, DatabricksWorkspace, DatabricksWorkspaceBicep
from .db_for_my_sql.flexible_server import db_for_my_sql_flexible_server, DbForMySqlFlexibleServer, DbForMySqlFlexibleServerBicep
from .db_for_postgre_sql.flexible_server import db_for_postgre_sql_flexible_server, DbForPostgreSqlFlexibleServer, DbForPostgreSqlFlexibleServerBicep
from .desktop_virtualization.application_group import desktop_virtualization_application_group, DesktopVirtualizationApplicationGroup, DesktopVirtualizationApplicationGroupBicep
from .desktop_virtualization.host_pool import desktop_virtualization_host_pool, DesktopVirtualizationHostPool, DesktopVirtualizationHostPoolBicep
from .desktop_virtualization.scaling_plan import desktop_virtualization_scaling_plan, DesktopVirtualizationScalingPlan, DesktopVirtualizationScalingPlanBicep
from .desktop_virtualization.workspace import desktop_virtualization_workspace, DesktopVirtualizationWorkspace, DesktopVirtualizationWorkspaceBicep
from .dev_ops_infrastructure.pool import dev_ops_infrastructure_pool, DevOpsInfrastructurePool, DevOpsInfrastructurePoolBicep
from .dev_test_lab.lab import dev_test_lab, DevTestLab, DevTestLabBicep
from .digital_twins.digital_twins_instance import digital_twins_instance, DigitalTwinsInstance, DigitalTwinsInstanceBicep
from .document_db.database_account import document_db_database_account, DocumentDbDatabaseAccount, DocumentDbDatabaseAccountBicep
from .document_db.mongo_cluster import document_db_mongo_cluster, DocumentDbMongoCluster, DocumentDbMongoClusterBicep
from .elastic_san.elastic_san import elastic_san, ElasticSan, ElasticSanBicep
from .event_grid.domain import event_grid_domain, EventGridDomain, EventGridDomainBicep
from .event_grid.namespace import event_grid_namespace, EventGridNamespace, EventGridNamespaceBicep
from .event_grid.system_topic import event_grid_system_topic, EventGridSystemTopic, EventGridSystemTopicBicep
from .event_grid.topic import event_grid_topic, EventGridTopic, EventGridTopicBicep
from .event_hub.namespace import event_hub_namespace, EventHubNamespace, EventHubNamespaceBicep
from .fabric.capacity import fabric_capacity, FabricCapacity, FabricCapacityBicep
from .hybrid_compute.machine import hybrid_compute_machine, HybridComputeMachine, HybridComputeMachineBicep
from .insights.action_group import insights_action_group, InsightsActionGroup, InsightsActionGroupBicep
from .insights.activity_log_alert import insights_activity_log_alert, InsightsActivityLogAlert, InsightsActivityLogAlertBicep
from .insights.component import insights_component, InsightsComponent, InsightsComponentBicep
from .insights.data_collection_endpoint import insights_data_collection_endpoint, InsightsDataCollectionEndpoint, InsightsDataCollectionEndpointBicep
from .insights.data_collection_rule import insights_data_collection_rule, InsightsDataCollectionRule, InsightsDataCollectionRuleBicep
from .insights.diagnostic_setting import insights_diagnostic_setting, InsightsDiagnosticSetting, InsightsDiagnosticSettingBicep
from .insights.metric_alert import insights_metric_alert, InsightsMetricAlert, InsightsMetricAlertBicep
from .insights.private_link_scope import insights_private_link_scope, InsightsPrivateLinkScope, InsightsPrivateLinkScopeBicep
from .insights.scheduled_query_rule import insights_scheduled_query_rule, InsightsScheduledQueryRule, InsightsScheduledQueryRuleBicep
from .insights.webtest import insights_webtest, InsightsWebtest, InsightsWebtestBicep
from .key_vault.vault import key_vault, KeyVault, KeyVaultBicep
from .kubernetes_configuration.extension import kubernetes_configuration_extension, KubernetesConfigurationExtension, KubernetesConfigurationExtensionBicep
from .kubernetes_configuration.flux_configuration import kubernetes_configuration_flux_configuration, KubernetesConfigurationFluxConfiguration, KubernetesConfigurationFluxConfigurationBicep
from .kusto.cluster import kusto_cluster, KustoCluster, KustoClusterBicep
from .load_test_service.load_test import load_test_service_load_test, LoadTestServiceLoadTest, LoadTestServiceLoadTestBicep
from .logic.workflow import logic_workflow, LogicWorkflow, LogicWorkflowBicep
from .machine_learning_services.workspace import machine_learning_services_workspace, MachineLearningServicesWorkspace, MachineLearningServicesWorkspaceBicep
from .maintenance.maintenance_configuration import maintenance_configuration, MaintenanceConfiguration, MaintenanceConfigurationBicep
from .managed_identity.user_assigned_identity import managed_identity_user_assigned_identity, ManagedIdentityUserAssignedIdentity, ManagedIdentityUserAssignedIdentityBicep
from .management.management_group import management_group, ManagementGroup, ManagementGroupBicep
from .net_app.net_app_account import net_app_account, NetAppAccount, NetAppAccountBicep
from .network.application_gateway import network_application_gateway, NetworkApplicationGateway, NetworkApplicationGatewayBicep
from .network.application_gateway_web_application_firewall_policy import network_application_gateway_web_application_firewall_policy, NetworkApplicationGatewayWebApplicationFirewallPolicy, NetworkApplicationGatewayWebApplicationFirewallPolicyBicep
from .network.application_security_group import network_application_security_group, NetworkApplicationSecurityGroup, NetworkApplicationSecurityGroupBicep
from .network.azure_firewall import network_azure_firewall, NetworkAzureFirewall, NetworkAzureFirewallBicep
from .network.bastion_host import network_bastion_host, NetworkBastionHost, NetworkBastionHostBicep
from .network.connection import network_connection, NetworkConnection, NetworkConnectionBicep
from .network.ddos_protection_plan import network_ddos_protection_plan, NetworkDdosProtectionPlan, NetworkDdosProtectionPlanBicep
from .network.dns_forwarding_ruleset import network_dns_forwarding_ruleset, NetworkDnsForwardingRuleset, NetworkDnsForwardingRulesetBicep
from .network.dns_resolver import network_dns_resolver, NetworkDnsResolver, NetworkDnsResolverBicep
from .network.dns_zone import network_dns_zone, NetworkDnsZone, NetworkDnsZoneBicep
from .network.express_route_circuit import network_express_route_circuit, NetworkExpressRouteCircuit, NetworkExpressRouteCircuitBicep
from .network.express_route_gateway import network_express_route_gateway, NetworkExpressRouteGateway, NetworkExpressRouteGatewayBicep
from .network.firewall_policy import network_firewall_policy, NetworkFirewallPolicy, NetworkFirewallPolicyBicep
from .network.front_door import network_front_door, NetworkFrontDoor, NetworkFrontDoorBicep
from .network.front_door_web_application_firewall_policy import network_front_door_web_application_firewall_policy, NetworkFrontDoorWebApplicationFirewallPolicy, NetworkFrontDoorWebApplicationFirewallPolicyBicep
from .network.ip_group import network_ip_group, NetworkIpGroup, NetworkIpGroupBicep
from .network.load_balancer import network_load_balancer, NetworkLoadBalancer, NetworkLoadBalancerBicep
from .network.local_network_gateway import network_local_network_gateway, NetworkLocalNetworkGateway, NetworkLocalNetworkGatewayBicep
from .network.nat_gateway import network_nat_gateway, NetworkNatGateway, NetworkNatGatewayBicep
from .network.network_interface import network_interface, NetworkInterface, NetworkInterfaceBicep
from .network.network_manager import network_manager, NetworkManager, NetworkManagerBicep
from .network.network_security_group import network_security_group, NetworkSecurityGroup, NetworkSecurityGroupBicep
from .network.network_watcher import network_watcher, NetworkWatcher, NetworkWatcherBicep
from .network.p2s_vpn_gateway import network_p2s_vpn_gateway, NetworkP2SVpnGateway, NetworkP2SVpnGatewayBicep
from .network.private_dns_zone import network_private_dns_zone, NetworkPrivateDnsZone, NetworkPrivateDnsZoneBicep
from .network.private_endpoint import network_private_endpoint, NetworkPrivateEndpoint, NetworkPrivateEndpointBicep
from .network.private_link_service import network_private_link_service, NetworkPrivateLinkService, NetworkPrivateLinkServiceBicep
from .network.public_ip_address import network_public_ip_address, NetworkPublicIpAddress, NetworkPublicIpAddressBicep
from .network.public_ip_prefix import network_public_ip_prefix, NetworkPublicIpPrefix, NetworkPublicIpPrefixBicep
from .network.route_table import network_route_table, NetworkRouteTable, NetworkRouteTableBicep
from .network.service_endpoint_policy import network_service_endpoint_policy, NetworkServiceEndpointPolicy, NetworkServiceEndpointPolicyBicep
from .network.trafficmanagerprofile import network_trafficmanagerprofile, NetworkTrafficmanagerprofile, NetworkTrafficmanagerprofileBicep
from .network.virtual_hub import network_virtual_hub, NetworkVirtualHub, NetworkVirtualHubBicep
from .network.virtual_network_gateway import network_virtual_network_gateway, NetworkVirtualNetworkGateway, NetworkVirtualNetworkGatewayBicep
from .network.virtual_wan import network_virtual_wan, NetworkVirtualWan, NetworkVirtualWanBicep
from .network.vpn_gateway import network_vpn_gateway, NetworkVpnGateway, NetworkVpnGatewayBicep
from .network.vpn_server_configuration import network_vpn_server_configuration, NetworkVpnServerConfiguration, NetworkVpnServerConfigurationBicep
from .network.vpn_site import network_vpn_site, NetworkVpnSite, NetworkVpnSiteBicep
from .operational_insights.workspace import operational_insights_workspace, OperationalInsightsWorkspace, OperationalInsightsWorkspaceBicep
from .operations_management.solution import operations_management_solution, OperationsManagementSolution, OperationsManagementSolutionBicep
from .portal.dashboard import portal_dashboard, PortalDashboard, PortalDashboardBicep
from .power_bi_dedicated.capacity import power_bi_dedicated_capacity, PowerBiDedicatedCapacity, PowerBiDedicatedCapacityBicep
from .purview.account import purview_account, PurviewAccount, PurviewAccountBicep
from .recovery_services.vault import recovery_services_vault, RecoveryServicesVault, RecoveryServicesVaultBicep
from .resource_graph.query import resource_graph_query, ResourceGraphQuery, ResourceGraphQueryBicep
from .resources.deployment_script import resources_deployment_script, ResourcesDeploymentScript, ResourcesDeploymentScriptBicep
from .resources.resource_group import resource_group, ResourceGroup, ResourceGroupBicep
from .search.search_service import search_service, SearchService, SearchServiceBicep
from .service_bus.namespace import service_bus_namespace, ServiceBusNamespace, ServiceBusNamespaceBicep
from .service_fabric.cluster import service_fabric_cluster, ServiceFabricCluster, ServiceFabricClusterBicep
from .service_networking.traffic_controller import service_networking_traffic_controller, ServiceNetworkingTrafficController, ServiceNetworkingTrafficControllerBicep
from .sql.instance_pool import sql_instance_pool, SqlInstancePool, SqlInstancePoolBicep
from .sql.managed_instance import sql_managed_instance, SqlManagedInstance, SqlManagedInstanceBicep
from .sql.server import sql_server, SqlServer, SqlServerBicep
from .storage.storage_account import storage_account, StorageAccount, StorageAccountBicep
from .virtual_machine_images.image_template import virtual_machine_image_template, VirtualMachineImageTemplate, VirtualMachineImageTemplateBicep
from .web.hosting_environment import web_hosting_environment, WebHostingEnvironment, WebHostingEnvironmentBicep
from .web.serverfarm import web_serverfarm, WebServerfarm, WebServerfarmBicep
from .web.site import web_site, WebSite, WebSiteBicep
from .web.static_site import web_static_site, WebStaticSite, WebStaticSiteBicep

__all__ = [
    'aad_domain_service'
    'AadDomainService'
    'AadDomainServiceBicep'
    'alerts_management_action_rule'
    'AlertsManagementActionRule'
    'AlertsManagementActionRuleBicep'
    'api_management_service'
    'ApiManagementService'
    'ApiManagementServiceBicep'
    'app_container_app'
    'AppContainerApp'
    'AppContainerAppBicep'
    'app_job'
    'AppJob'
    'AppJobBicep'
    'app_managed_environment'
    'AppManagedEnvironment'
    'AppManagedEnvironmentBicep'
    'app_configuration_store'
    'AppConfigurationStore'
    'AppConfigurationStoreBicep'
    'automation_account'
    'AutomationAccount'
    'AutomationAccountBicep'
    'batch_account'
    'BatchAccount'
    'BatchAccountBicep'
    'cache_redis'
    'CacheRedis'
    'CacheRedisBicep'
    'cdn_profile'
    'CdnProfile'
    'CdnProfileBicep'
    'cognitive_services_account'
    'CognitiveServicesAccount'
    'CognitiveServicesAccountBicep'
    'communication_service'
    'CommunicationService'
    'CommunicationServiceBicep'
    'communication_email_service'
    'CommunicationEmailService'
    'CommunicationEmailServiceBicep'
    'compute_availability_set'
    'ComputeAvailabilitySet'
    'ComputeAvailabilitySetBicep'
    'compute_disk'
    'ComputeDisk'
    'ComputeDiskBicep'
    'compute_disk_encryption_set'
    'ComputeDiskEncryptionSet'
    'ComputeDiskEncryptionSetBicep'
    'compute_gallery'
    'ComputeGallery'
    'ComputeGalleryBicep'
    'compute_image'
    'ComputeImage'
    'ComputeImageBicep'
    'compute_proximity_placement_group'
    'ComputeProximityPlacementGroup'
    'ComputeProximityPlacementGroupBicep'
    'compute_ssh_public_key'
    'ComputeSshPublicKey'
    'ComputeSshPublicKeyBicep'
    'compute_virtual_machine'
    'ComputeVirtualMachine'
    'ComputeVirtualMachineBicep'
    'compute_virtual_machine_scale_set'
    'ComputeVirtualMachineScaleSet'
    'ComputeVirtualMachineScaleSetBicep'
    'consumption_budget'
    'ConsumptionBudget'
    'ConsumptionBudgetBicep'
    'container_instance_container_group'
    'ContainerInstanceContainerGroup'
    'ContainerInstanceContainerGroupBicep'
    'container_registry'
    'ContainerRegistry'
    'ContainerRegistryBicep'
    'container_service_managed_cluster'
    'ContainerServiceManagedCluster'
    'ContainerServiceManagedClusterBicep'
    'data_factory'
    'DataFactory'
    'DataFactoryBicep'
    'data_protection_backup_vault'
    'DataProtectionBackupVault'
    'DataProtectionBackupVaultBicep'
    'databricks_access_connector'
    'DatabricksAccessConnector'
    'DatabricksAccessConnectorBicep'
    'databricks_workspace'
    'DatabricksWorkspace'
    'DatabricksWorkspaceBicep'
    'db_for_my_sql_flexible_server'
    'DbForMySqlFlexibleServer'
    'DbForMySqlFlexibleServerBicep'
    'db_for_postgre_sql_flexible_server'
    'DbForPostgreSqlFlexibleServer'
    'DbForPostgreSqlFlexibleServerBicep'
    'desktop_virtualization_application_group'
    'DesktopVirtualizationApplicationGroup'
    'DesktopVirtualizationApplicationGroupBicep'
    'desktop_virtualization_host_pool'
    'DesktopVirtualizationHostPool'
    'DesktopVirtualizationHostPoolBicep'
    'desktop_virtualization_scaling_plan'
    'DesktopVirtualizationScalingPlan'
    'DesktopVirtualizationScalingPlanBicep'
    'desktop_virtualization_workspace'
    'DesktopVirtualizationWorkspace'
    'DesktopVirtualizationWorkspaceBicep'
    'dev_ops_infrastructure_pool'
    'DevOpsInfrastructurePool'
    'DevOpsInfrastructurePoolBicep'
    'dev_test_lab'
    'DevTestLab'
    'DevTestLabBicep'
    'digital_twins_instance'
    'DigitalTwinsInstance'
    'DigitalTwinsInstanceBicep'
    'document_db_database_account'
    'DocumentDbDatabaseAccount'
    'DocumentDbDatabaseAccountBicep'
    'document_db_mongo_cluster'
    'DocumentDbMongoCluster'
    'DocumentDbMongoClusterBicep'
    'elastic_san'
    'ElasticSan'
    'ElasticSanBicep'
    'event_grid_domain'
    'EventGridDomain'
    'EventGridDomainBicep'
    'event_grid_namespace'
    'EventGridNamespace'
    'EventGridNamespaceBicep'
    'event_grid_system_topic'
    'EventGridSystemTopic'
    'EventGridSystemTopicBicep'
    'event_grid_topic'
    'EventGridTopic'
    'EventGridTopicBicep'
    'event_hub_namespace'
    'EventHubNamespace'
    'EventHubNamespaceBicep'
    'fabric_capacity'
    'FabricCapacity'
    'FabricCapacityBicep'
    'hybrid_compute_machine'
    'HybridComputeMachine'
    'HybridComputeMachineBicep'
    'insights_action_group'
    'InsightsActionGroup'
    'InsightsActionGroupBicep'
    'insights_activity_log_alert'
    'InsightsActivityLogAlert'
    'InsightsActivityLogAlertBicep'
    'insights_component'
    'InsightsComponent'
    'InsightsComponentBicep'
    'insights_data_collection_endpoint'
    'InsightsDataCollectionEndpoint'
    'InsightsDataCollectionEndpointBicep'
    'insights_data_collection_rule'
    'InsightsDataCollectionRule'
    'InsightsDataCollectionRuleBicep'
    'insights_diagnostic_setting'
    'InsightsDiagnosticSetting'
    'InsightsDiagnosticSettingBicep'
    'insights_metric_alert'
    'InsightsMetricAlert'
    'InsightsMetricAlertBicep'
    'insights_private_link_scope'
    'InsightsPrivateLinkScope'
    'InsightsPrivateLinkScopeBicep'
    'insights_scheduled_query_rule'
    'InsightsScheduledQueryRule'
    'InsightsScheduledQueryRuleBicep'
    'insights_webtest'
    'InsightsWebtest'
    'InsightsWebtestBicep'
    'key_vault'
    'KeyVault'
    'KeyVaultBicep'
    'kubernetes_configuration_extension'
    'KubernetesConfigurationExtension'
    'KubernetesConfigurationExtensionBicep'
    'kubernetes_configuration_flux_configuration'
    'KubernetesConfigurationFluxConfiguration'
    'KubernetesConfigurationFluxConfigurationBicep'
    'kusto_cluster'
    'KustoCluster'
    'KustoClusterBicep'
    'load_test_service_load_test'
    'LoadTestServiceLoadTest'
    'LoadTestServiceLoadTestBicep'
    'logic_workflow'
    'LogicWorkflow'
    'LogicWorkflowBicep'
    'machine_learning_services_workspace'
    'MachineLearningServicesWorkspace'
    'MachineLearningServicesWorkspaceBicep'
    'maintenance_configuration'
    'MaintenanceConfiguration'
    'MaintenanceConfigurationBicep'
    'managed_identity_user_assigned_identity'
    'ManagedIdentityUserAssignedIdentity'
    'ManagedIdentityUserAssignedIdentityBicep'
    'management_group'
    'ManagementGroup'
    'ManagementGroupBicep'
    'net_app_account'
    'NetAppAccount'
    'NetAppAccountBicep'
    'network_application_gateway'
    'NetworkApplicationGateway'
    'NetworkApplicationGatewayBicep'
    'network_application_gateway_web_application_firewall_policy'
    'NetworkApplicationGatewayWebApplicationFirewallPolicy'
    'NetworkApplicationGatewayWebApplicationFirewallPolicyBicep'
    'network_application_security_group'
    'NetworkApplicationSecurityGroup'
    'NetworkApplicationSecurityGroupBicep'
    'network_azure_firewall'
    'NetworkAzureFirewall'
    'NetworkAzureFirewallBicep'
    'network_bastion_host'
    'NetworkBastionHost'
    'NetworkBastionHostBicep'
    'network_connection'
    'NetworkConnection'
    'NetworkConnectionBicep'
    'network_ddos_protection_plan'
    'NetworkDdosProtectionPlan'
    'NetworkDdosProtectionPlanBicep'
    'network_dns_forwarding_ruleset'
    'NetworkDnsForwardingRuleset'
    'NetworkDnsForwardingRulesetBicep'
    'network_dns_resolver'
    'NetworkDnsResolver'
    'NetworkDnsResolverBicep'
    'network_dns_zone'
    'NetworkDnsZone'
    'NetworkDnsZoneBicep'
    'network_express_route_circuit'
    'NetworkExpressRouteCircuit'
    'NetworkExpressRouteCircuitBicep'
    'network_express_route_gateway'
    'NetworkExpressRouteGateway'
    'NetworkExpressRouteGatewayBicep'
    'network_firewall_policy'
    'NetworkFirewallPolicy'
    'NetworkFirewallPolicyBicep'
    'network_front_door'
    'NetworkFrontDoor'
    'NetworkFrontDoorBicep'
    'network_front_door_web_application_firewall_policy'
    'NetworkFrontDoorWebApplicationFirewallPolicy'
    'NetworkFrontDoorWebApplicationFirewallPolicyBicep'
    'network_ip_group'
    'NetworkIpGroup'
    'NetworkIpGroupBicep'
    'network_load_balancer'
    'NetworkLoadBalancer'
    'NetworkLoadBalancerBicep'
    'network_local_network_gateway'
    'NetworkLocalNetworkGateway'
    'NetworkLocalNetworkGatewayBicep'
    'network_nat_gateway'
    'NetworkNatGateway'
    'NetworkNatGatewayBicep'
    'network_interface'
    'NetworkInterface'
    'NetworkInterfaceBicep'
    'network_manager'
    'NetworkManager'
    'NetworkManagerBicep'
    'network_security_group'
    'NetworkSecurityGroup'
    'NetworkSecurityGroupBicep'
    'network_watcher'
    'NetworkWatcher'
    'NetworkWatcherBicep'
    'network_p2s_vpn_gateway'
    'NetworkP2SVpnGateway'
    'NetworkP2SVpnGatewayBicep'
    'network_private_dns_zone'
    'NetworkPrivateDnsZone'
    'NetworkPrivateDnsZoneBicep'
    'network_private_endpoint'
    'NetworkPrivateEndpoint'
    'NetworkPrivateEndpointBicep'
    'network_private_link_service'
    'NetworkPrivateLinkService'
    'NetworkPrivateLinkServiceBicep'
    'network_public_ip_address'
    'NetworkPublicIpAddress'
    'NetworkPublicIpAddressBicep'
    'network_public_ip_prefix'
    'NetworkPublicIpPrefix'
    'NetworkPublicIpPrefixBicep'
    'network_route_table'
    'NetworkRouteTable'
    'NetworkRouteTableBicep'
    'network_service_endpoint_policy'
    'NetworkServiceEndpointPolicy'
    'NetworkServiceEndpointPolicyBicep'
    'network_trafficmanagerprofile'
    'NetworkTrafficmanagerprofile'
    'NetworkTrafficmanagerprofileBicep'
    'network_virtual_hub'
    'NetworkVirtualHub'
    'NetworkVirtualHubBicep'
    'network_virtual_network_gateway'
    'NetworkVirtualNetworkGateway'
    'NetworkVirtualNetworkGatewayBicep'
    'network_virtual_wan'
    'NetworkVirtualWan'
    'NetworkVirtualWanBicep'
    'network_vpn_gateway'
    'NetworkVpnGateway'
    'NetworkVpnGatewayBicep'
    'network_vpn_server_configuration'
    'NetworkVpnServerConfiguration'
    'NetworkVpnServerConfigurationBicep'
    'network_vpn_site'
    'NetworkVpnSite'
    'NetworkVpnSiteBicep'
    'operational_insights_workspace'
    'OperationalInsightsWorkspace'
    'OperationalInsightsWorkspaceBicep'
    'operations_management_solution'
    'OperationsManagementSolution'
    'OperationsManagementSolutionBicep'
    'portal_dashboard'
    'PortalDashboard'
    'PortalDashboardBicep'
    'power_bi_dedicated_capacity'
    'PowerBiDedicatedCapacity'
    'PowerBiDedicatedCapacityBicep'
    'purview_account'
    'PurviewAccount'
    'PurviewAccountBicep'
    'recovery_services_vault'
    'RecoveryServicesVault'
    'RecoveryServicesVaultBicep'
    'resource_graph_query'
    'ResourceGraphQuery'
    'ResourceGraphQueryBicep'
    'resources_deployment_script'
    'ResourcesDeploymentScript'
    'ResourcesDeploymentScriptBicep'
    'resource_group'
    'ResourceGroup'
    'ResourceGroupBicep'
    'search_service'
    'SearchService'
    'SearchServiceBicep'
    'service_bus_namespace'
    'ServiceBusNamespace'
    'ServiceBusNamespaceBicep'
    'service_fabric_cluster'
    'ServiceFabricCluster'
    'ServiceFabricClusterBicep'
    'service_networking_traffic_controller'
    'ServiceNetworkingTrafficController'
    'ServiceNetworkingTrafficControllerBicep'
    'sql_instance_pool'
    'SqlInstancePool'
    'SqlInstancePoolBicep'
    'sql_managed_instance'
    'SqlManagedInstance'
    'SqlManagedInstanceBicep'
    'sql_server'
    'SqlServer'
    'SqlServerBicep'
    'storage_account'
    'StorageAccount'
    'StorageAccountBicep'
    'virtual_machine_image_template'
    'VirtualMachineImageTemplate'
    'VirtualMachineImageTemplateBicep'
    'web_hosting_environment'
    'WebHostingEnvironment'
    'WebHostingEnvironmentBicep'
    'web_serverfarm'
    'WebServerfarm'
    'WebServerfarmBicep'
    'web_site'
    'WebSite'
    'WebSiteBicep'
    'web_static_site'
    'WebStaticSite'
    'WebStaticSiteBicep'
]

class AddResourceMixin:
    bicep: Optional[IO[str]]

    @overload
    def add(
            self,
            resource: Literal['AadDomainService', 'aad_domain_service'],
            params: AadDomainService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AadDomainServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AlertsManagementActionRule', 'alerts_management_action_rule'],
            params: AlertsManagementActionRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AlertsManagementActionRuleBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ApiManagementService', 'api_management_service'],
            params: ApiManagementService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ApiManagementServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AppContainerApp', 'app_container_app'],
            params: AppContainerApp,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppContainerAppBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AppJob', 'app_job'],
            params: AppJob,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppJobBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AppManagedEnvironment', 'app_managed_environment'],
            params: AppManagedEnvironment,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppManagedEnvironmentBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AppConfigurationStore', 'app_configuration_store'],
            params: AppConfigurationStore,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AppConfigurationStoreBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['AutomationAccount', 'automation_account'],
            params: AutomationAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> AutomationAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['BatchAccount', 'batch_account'],
            params: BatchAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> BatchAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['CacheRedis', 'cache_redis'],
            params: CacheRedis,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CacheRedisBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['CdnProfile', 'cdn_profile'],
            params: CdnProfile,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CdnProfileBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['CognitiveServicesAccount', 'cognitive_services_account'],
            params: CognitiveServicesAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CognitiveServicesAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['CommunicationService', 'communication_service'],
            params: CommunicationService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CommunicationServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['CommunicationEmailService', 'communication_email_service'],
            params: CommunicationEmailService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> CommunicationEmailServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeAvailabilitySet', 'compute_availability_set'],
            params: ComputeAvailabilitySet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeAvailabilitySetBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeDisk', 'compute_disk'],
            params: ComputeDisk,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeDiskBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeDiskEncryptionSet', 'compute_disk_encryption_set'],
            params: ComputeDiskEncryptionSet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeDiskEncryptionSetBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeGallery', 'compute_gallery'],
            params: ComputeGallery,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeGalleryBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeImage', 'compute_image'],
            params: ComputeImage,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeImageBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeProximityPlacementGroup', 'compute_proximity_placement_group'],
            params: ComputeProximityPlacementGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeProximityPlacementGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeSshPublicKey', 'compute_ssh_public_key'],
            params: ComputeSshPublicKey,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeSshPublicKeyBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeVirtualMachine', 'compute_virtual_machine'],
            params: ComputeVirtualMachine,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeVirtualMachineBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ComputeVirtualMachineScaleSet', 'compute_virtual_machine_scale_set'],
            params: ComputeVirtualMachineScaleSet,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ComputeVirtualMachineScaleSetBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ConsumptionBudget', 'consumption_budget'],
            params: ConsumptionBudget,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ConsumptionBudgetBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ContainerInstanceContainerGroup', 'container_instance_container_group'],
            params: ContainerInstanceContainerGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerInstanceContainerGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ContainerRegistry', 'container_registry'],
            params: ContainerRegistry,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerRegistryBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ContainerServiceManagedCluster', 'container_service_managed_cluster'],
            params: ContainerServiceManagedCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ContainerServiceManagedClusterBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DataFactory', 'data_factory'],
            params: DataFactory,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DataFactoryBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DataProtectionBackupVault', 'data_protection_backup_vault'],
            params: DataProtectionBackupVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DataProtectionBackupVaultBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DatabricksAccessConnector', 'databricks_access_connector'],
            params: DatabricksAccessConnector,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DatabricksAccessConnectorBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DatabricksWorkspace', 'databricks_workspace'],
            params: DatabricksWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DatabricksWorkspaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DbForMySqlFlexibleServer', 'db_for_my_sql_flexible_server'],
            params: DbForMySqlFlexibleServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DbForMySqlFlexibleServerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DbForPostgreSqlFlexibleServer', 'db_for_postgre_sql_flexible_server'],
            params: DbForPostgreSqlFlexibleServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DbForPostgreSqlFlexibleServerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DesktopVirtualizationApplicationGroup', 'desktop_virtualization_application_group'],
            params: DesktopVirtualizationApplicationGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationApplicationGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DesktopVirtualizationHostPool', 'desktop_virtualization_host_pool'],
            params: DesktopVirtualizationHostPool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationHostPoolBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DesktopVirtualizationScalingPlan', 'desktop_virtualization_scaling_plan'],
            params: DesktopVirtualizationScalingPlan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationScalingPlanBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DesktopVirtualizationWorkspace', 'desktop_virtualization_workspace'],
            params: DesktopVirtualizationWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DesktopVirtualizationWorkspaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DevOpsInfrastructurePool', 'dev_ops_infrastructure_pool'],
            params: DevOpsInfrastructurePool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DevOpsInfrastructurePoolBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DevTestLab', 'dev_test_lab'],
            params: DevTestLab,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DevTestLabBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DigitalTwinsInstance', 'digital_twins_instance'],
            params: DigitalTwinsInstance,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DigitalTwinsInstanceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DocumentDbDatabaseAccount', 'document_db_database_account'],
            params: DocumentDbDatabaseAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DocumentDbDatabaseAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['DocumentDbMongoCluster', 'document_db_mongo_cluster'],
            params: DocumentDbMongoCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> DocumentDbMongoClusterBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ElasticSan', 'elastic_san'],
            params: ElasticSan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ElasticSanBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['EventGridDomain', 'event_grid_domain'],
            params: EventGridDomain,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridDomainBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['EventGridNamespace', 'event_grid_namespace'],
            params: EventGridNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridNamespaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['EventGridSystemTopic', 'event_grid_system_topic'],
            params: EventGridSystemTopic,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridSystemTopicBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['EventGridTopic', 'event_grid_topic'],
            params: EventGridTopic,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventGridTopicBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['EventHubNamespace', 'event_hub_namespace'],
            params: EventHubNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> EventHubNamespaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['FabricCapacity', 'fabric_capacity'],
            params: FabricCapacity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> FabricCapacityBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['HybridComputeMachine', 'hybrid_compute_machine'],
            params: HybridComputeMachine,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> HybridComputeMachineBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsActionGroup', 'insights_action_group'],
            params: InsightsActionGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsActionGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsActivityLogAlert', 'insights_activity_log_alert'],
            params: InsightsActivityLogAlert,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsActivityLogAlertBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsComponent', 'insights_component'],
            params: InsightsComponent,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsComponentBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsDataCollectionEndpoint', 'insights_data_collection_endpoint'],
            params: InsightsDataCollectionEndpoint,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDataCollectionEndpointBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsDataCollectionRule', 'insights_data_collection_rule'],
            params: InsightsDataCollectionRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDataCollectionRuleBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsDiagnosticSetting', 'insights_diagnostic_setting'],
            params: InsightsDiagnosticSetting,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsDiagnosticSettingBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsMetricAlert', 'insights_metric_alert'],
            params: InsightsMetricAlert,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsMetricAlertBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsPrivateLinkScope', 'insights_private_link_scope'],
            params: InsightsPrivateLinkScope,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsPrivateLinkScopeBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsScheduledQueryRule', 'insights_scheduled_query_rule'],
            params: InsightsScheduledQueryRule,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsScheduledQueryRuleBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['InsightsWebtest', 'insights_webtest'],
            params: InsightsWebtest,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> InsightsWebtestBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['KeyVault', 'key_vault'],
            params: KeyVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KeyVaultBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['KubernetesConfigurationExtension', 'kubernetes_configuration_extension'],
            params: KubernetesConfigurationExtension,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KubernetesConfigurationExtensionBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['KubernetesConfigurationFluxConfiguration', 'kubernetes_configuration_flux_configuration'],
            params: KubernetesConfigurationFluxConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KubernetesConfigurationFluxConfigurationBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['KustoCluster', 'kusto_cluster'],
            params: KustoCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> KustoClusterBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['LoadTestServiceLoadTest', 'load_test_service_load_test'],
            params: LoadTestServiceLoadTest,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> LoadTestServiceLoadTestBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['LogicWorkflow', 'logic_workflow'],
            params: LogicWorkflow,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> LogicWorkflowBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['MachineLearningServicesWorkspace', 'machine_learning_services_workspace'],
            params: MachineLearningServicesWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> MachineLearningServicesWorkspaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['MaintenanceConfiguration', 'maintenance_configuration'],
            params: MaintenanceConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> MaintenanceConfigurationBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ManagedIdentityUserAssignedIdentity', 'managed_identity_user_assigned_identity'],
            params: ManagedIdentityUserAssignedIdentity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ManagedIdentityUserAssignedIdentityBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ManagementGroup', 'management_group'],
            params: ManagementGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ManagementGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetAppAccount', 'net_app_account'],
            params: NetAppAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetAppAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkApplicationGateway', 'network_application_gateway'],
            params: NetworkApplicationGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkApplicationGatewayWebApplicationFirewallPolicy', 'network_application_gateway_web_application_firewall_policy'],
            params: NetworkApplicationGatewayWebApplicationFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationGatewayWebApplicationFirewallPolicyBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkApplicationSecurityGroup', 'network_application_security_group'],
            params: NetworkApplicationSecurityGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkApplicationSecurityGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkAzureFirewall', 'network_azure_firewall'],
            params: NetworkAzureFirewall,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkAzureFirewallBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkBastionHost', 'network_bastion_host'],
            params: NetworkBastionHost,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkBastionHostBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkConnection', 'network_connection'],
            params: NetworkConnection,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkConnectionBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkDdosProtectionPlan', 'network_ddos_protection_plan'],
            params: NetworkDdosProtectionPlan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDdosProtectionPlanBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkDnsForwardingRuleset', 'network_dns_forwarding_ruleset'],
            params: NetworkDnsForwardingRuleset,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsForwardingRulesetBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkDnsResolver', 'network_dns_resolver'],
            params: NetworkDnsResolver,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsResolverBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkDnsZone', 'network_dns_zone'],
            params: NetworkDnsZone,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkDnsZoneBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkExpressRouteCircuit', 'network_express_route_circuit'],
            params: NetworkExpressRouteCircuit,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkExpressRouteCircuitBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkExpressRouteGateway', 'network_express_route_gateway'],
            params: NetworkExpressRouteGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkExpressRouteGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkFirewallPolicy', 'network_firewall_policy'],
            params: NetworkFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFirewallPolicyBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkFrontDoor', 'network_front_door'],
            params: NetworkFrontDoor,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFrontDoorBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkFrontDoorWebApplicationFirewallPolicy', 'network_front_door_web_application_firewall_policy'],
            params: NetworkFrontDoorWebApplicationFirewallPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkFrontDoorWebApplicationFirewallPolicyBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkIpGroup', 'network_ip_group'],
            params: NetworkIpGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkIpGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkLoadBalancer', 'network_load_balancer'],
            params: NetworkLoadBalancer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkLoadBalancerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkLocalNetworkGateway', 'network_local_network_gateway'],
            params: NetworkLocalNetworkGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkLocalNetworkGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkNatGateway', 'network_nat_gateway'],
            params: NetworkNatGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '1.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkNatGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkInterface', 'network_interface'],
            params: NetworkInterface,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkInterfaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkManager', 'network_manager'],
            params: NetworkManager,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkManagerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkSecurityGroup', 'network_security_group'],
            params: NetworkSecurityGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkSecurityGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkWatcher', 'network_watcher'],
            params: NetworkWatcher,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkWatcherBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkP2SVpnGateway', 'network_p2s_vpn_gateway'],
            params: NetworkP2SVpnGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkP2SVpnGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkPrivateDnsZone', 'network_private_dns_zone'],
            params: NetworkPrivateDnsZone,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateDnsZoneBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkPrivateEndpoint', 'network_private_endpoint'],
            params: NetworkPrivateEndpoint,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateEndpointBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkPrivateLinkService', 'network_private_link_service'],
            params: NetworkPrivateLinkService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPrivateLinkServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkPublicIpAddress', 'network_public_ip_address'],
            params: NetworkPublicIpAddress,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.7.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPublicIpAddressBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkPublicIpPrefix', 'network_public_ip_prefix'],
            params: NetworkPublicIpPrefix,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkPublicIpPrefixBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkRouteTable', 'network_route_table'],
            params: NetworkRouteTable,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkRouteTableBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkServiceEndpointPolicy', 'network_service_endpoint_policy'],
            params: NetworkServiceEndpointPolicy,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkServiceEndpointPolicyBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkTrafficmanagerprofile', 'network_trafficmanagerprofile'],
            params: NetworkTrafficmanagerprofile,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkTrafficmanagerprofileBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVirtualHub', 'network_virtual_hub'],
            params: NetworkVirtualHub,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualHubBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVirtualNetworkGateway', 'network_virtual_network_gateway'],
            params: NetworkVirtualNetworkGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualNetworkGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVirtualWan', 'network_virtual_wan'],
            params: NetworkVirtualWan,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVirtualWanBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVpnGateway', 'network_vpn_gateway'],
            params: NetworkVpnGateway,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnGatewayBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVpnServerConfiguration', 'network_vpn_server_configuration'],
            params: NetworkVpnServerConfiguration,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnServerConfigurationBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['NetworkVpnSite', 'network_vpn_site'],
            params: NetworkVpnSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> NetworkVpnSiteBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['OperationalInsightsWorkspace', 'operational_insights_workspace'],
            params: OperationalInsightsWorkspace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.9.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> OperationalInsightsWorkspaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['OperationsManagementSolution', 'operations_management_solution'],
            params: OperationsManagementSolution,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> OperationsManagementSolutionBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['PortalDashboard', 'portal_dashboard'],
            params: PortalDashboard,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PortalDashboardBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['PowerBiDedicatedCapacity', 'power_bi_dedicated_capacity'],
            params: PowerBiDedicatedCapacity,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PowerBiDedicatedCapacityBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['PurviewAccount', 'purview_account'],
            params: PurviewAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> PurviewAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['RecoveryServicesVault', 'recovery_services_vault'],
            params: RecoveryServicesVault,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> RecoveryServicesVaultBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ResourceGraphQuery', 'resource_graph_query'],
            params: ResourceGraphQuery,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourceGraphQueryBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ResourcesDeploymentScript', 'resources_deployment_script'],
            params: ResourcesDeploymentScript,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.5.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourcesDeploymentScriptBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ResourceGroup', 'resource_group'],
            params: ResourceGroup,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ResourceGroupBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['SearchService', 'search_service'],
            params: SearchService,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.8.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SearchServiceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ServiceBusNamespace', 'service_bus_namespace'],
            params: ServiceBusNamespace,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.10.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceBusNamespaceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ServiceFabricCluster', 'service_fabric_cluster'],
            params: ServiceFabricCluster,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceFabricClusterBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['ServiceNetworkingTrafficController', 'service_networking_traffic_controller'],
            params: ServiceNetworkingTrafficController,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> ServiceNetworkingTrafficControllerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['SqlInstancePool', 'sql_instance_pool'],
            params: SqlInstancePool,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlInstancePoolBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['SqlManagedInstance', 'sql_managed_instance'],
            params: SqlManagedInstance,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.1.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlManagedInstanceBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['SqlServer', 'sql_server'],
            params: SqlServer,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.11.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> SqlServerBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['StorageAccount', 'storage_account'],
            params: StorageAccount,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.14.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> StorageAccountBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['VirtualMachineImageTemplate', 'virtual_machine_image_template'],
            params: VirtualMachineImageTemplate,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.4.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> VirtualMachineImageTemplateBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['WebHostingEnvironment', 'web_hosting_environment'],
            params: WebHostingEnvironment,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.2.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebHostingEnvironmentBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['WebServerfarm', 'web_serverfarm'],
            params: WebServerfarm,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.3.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebServerfarmBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['WebSite', 'web_site'],
            params: WebSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.12.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebSiteBicep:
        ...

    @overload
    def add(
            self,
            resource: Literal['WebStaticSite', 'web_static_site'],
            params: WebStaticSite,
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '0.6.0',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> WebStaticSiteBicep:
        ...

    def add(self, resource: str, params: Dict[str, Any], **kwargs) -> Module:
        try:
            return globals()[resource](self.bicep, params, **kwargs)
        except KeyError:
            raise ValueError(f"Unrecognized resource: '{resource}'.")

