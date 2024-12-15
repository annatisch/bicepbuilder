from typing import overload, Literal, Optional, Union, IO
from ..expressions import BicepExpression

from .aad.domain_service import domain_service as aad_domain_service, DomainService as AadDomainService, DomainServiceBicep as AadDomainServiceBicep
from .alerts_management.action_rule import action_rule as alerts_management_action_rule, ActionRule as AlertsManagementActionRule, ActionRuleBicep as AlertsManagementActionRuleBicep
from .api_management.service import service as api_management_service, Service as ApiManagementService, ServiceBicep as ApiManagementServiceBicep
from .app.container_app import container_app as app_container_app, ContainerApp as AppContainerApp, ContainerAppBicep as AppContainerAppBicep
from .app.job import job as app_job, Job as AppJob, JobBicep as AppJobBicep
from .app.managed_environment import managed_environment as app_managed_environment, ManagedEnvironment as AppManagedEnvironment, ManagedEnvironmentBicep as AppManagedEnvironmentBicep
from .app_configuration.configuration_store import configuration_store as app_configuration_store, ConfigurationStore as AppConfigurationStore, ConfigurationStoreBicep as AppConfigurationStoreBicep
from .automation.automation_account import automation_account as automation_account, AutomationAccount as AutomationAccount, AutomationAccountBicep as AutomationAccountBicep
from .batch.batch_account import batch_account as batch_account, BatchAccount as BatchAccount, BatchAccountBicep as BatchAccountBicep
from .cache.redis import redis as cache_redis, Redis as CacheRedis, RedisBicep as CacheRedisBicep
from .cdn.profile import profile as cdn_profile, Profile as CdnProfile, ProfileBicep as CdnProfileBicep
from .cognitive_services.account import account as cognitive_services_account, Account as CognitiveServicesAccount, AccountBicep as CognitiveServicesAccountBicep
from .communication.communication_service import communication_service as communication_service, CommunicationService as CommunicationService, CommunicationServiceBicep as CommunicationServiceBicep
from .communication.email_service import email_service as communication_email_service, EmailService as CommunicationEmailService, EmailServiceBicep as CommunicationEmailServiceBicep
from .compute.availability_set import availability_set as compute_availability_set, AvailabilitySet as ComputeAvailabilitySet, AvailabilitySetBicep as ComputeAvailabilitySetBicep
from .compute.disk import disk as compute_disk, Disk as ComputeDisk, DiskBicep as ComputeDiskBicep
from .compute.disk_encryption_set import disk_encryption_set as compute_disk_encryption_set, DiskEncryptionSet as ComputeDiskEncryptionSet, DiskEncryptionSetBicep as ComputeDiskEncryptionSetBicep
from .compute.gallery import gallery as compute_gallery, Gallery as ComputeGallery, GalleryBicep as ComputeGalleryBicep
from .compute.image import image as compute_image, Image as ComputeImage, ImageBicep as ComputeImageBicep
from .compute.proximity_placement_group import proximity_placement_group as compute_proximity_placement_group, ProximityPlacementGroup as ComputeProximityPlacementGroup, ProximityPlacementGroupBicep as ComputeProximityPlacementGroupBicep
from .compute.ssh_public_key import ssh_public_key as compute_ssh_public_key, SshPublicKey as ComputeSshPublicKey, SshPublicKeyBicep as ComputeSshPublicKeyBicep
from .compute.virtual_machine import virtual_machine as compute_virtual_machine, VirtualMachine as ComputeVirtualMachine, VirtualMachineBicep as ComputeVirtualMachineBicep
from .compute.virtual_machine_scale_set import virtual_machine_scale_set as compute_virtual_machine_scale_set, VirtualMachineScaleSet as ComputeVirtualMachineScaleSet, VirtualMachineScaleSetBicep as ComputeVirtualMachineScaleSetBicep
from .consumption.budget import budget as consumption_budget, Budget as ConsumptionBudget, BudgetBicep as ConsumptionBudgetBicep
from .container_instance.container_group import container_group as container_instance_container_group, ContainerGroup as ContainerInstanceContainerGroup, ContainerGroupBicep as ContainerInstanceContainerGroupBicep
from .container_registry.registry import registry as container_registry, Registry as ContainerRegistry, RegistryBicep as ContainerRegistryBicep
from .container_service.managed_cluster import managed_cluster as container_service_managed_cluster, ManagedCluster as ContainerServiceManagedCluster, ManagedClusterBicep as ContainerServiceManagedClusterBicep
from .data_factory.factory import factory as data_factory, Factory as DataFactory, FactoryBicep as DataFactoryBicep
from .data_protection.backup_vault import backup_vault as data_protection_backup_vault, BackupVault as DataProtectionBackupVault, BackupVaultBicep as DataProtectionBackupVaultBicep
from .databricks.access_connector import access_connector as databricks_access_connector, AccessConnector as DatabricksAccessConnector, AccessConnectorBicep as DatabricksAccessConnectorBicep
from .databricks.workspace import workspace as databricks_workspace, Workspace as DatabricksWorkspace, WorkspaceBicep as DatabricksWorkspaceBicep
from .db_for_my_sql.flexible_server import flexible_server as db_for_my_sql_flexible_server, FlexibleServer as DbForMySqlFlexibleServer, FlexibleServerBicep as DbForMySqlFlexibleServerBicep
from .db_for_postgre_sql.flexible_server import flexible_server as db_for_postgre_sql_flexible_server, FlexibleServer as DbForPostgreSqlFlexibleServer, FlexibleServerBicep as DbForPostgreSqlFlexibleServerBicep
from .desktop_virtualization.application_group import application_group as desktop_virtualization_application_group, ApplicationGroup as DesktopVirtualizationApplicationGroup, ApplicationGroupBicep as DesktopVirtualizationApplicationGroupBicep
from .desktop_virtualization.host_pool import host_pool as desktop_virtualization_host_pool, HostPool as DesktopVirtualizationHostPool, HostPoolBicep as DesktopVirtualizationHostPoolBicep
from .desktop_virtualization.scaling_plan import scaling_plan as desktop_virtualization_scaling_plan, ScalingPlan as DesktopVirtualizationScalingPlan, ScalingPlanBicep as DesktopVirtualizationScalingPlanBicep
from .desktop_virtualization.workspace import workspace as desktop_virtualization_workspace, Workspace as DesktopVirtualizationWorkspace, WorkspaceBicep as DesktopVirtualizationWorkspaceBicep
from .dev_ops_infrastructure.pool import pool as dev_ops_infrastructure_pool, Pool as DevOpsInfrastructurePool, PoolBicep as DevOpsInfrastructurePoolBicep
from .dev_test_lab.lab import lab as dev_test_lab, Lab as DevTestLab, LabBicep as DevTestLabBicep
from .digital_twins.digital_twins_instance import digital_twins_instance as digital_twins_instance, DigitalTwinsInstance as DigitalTwinsInstance, DigitalTwinsInstanceBicep as DigitalTwinsInstanceBicep
from .document_db.database_account import database_account as document_db_database_account, DatabaseAccount as DocumentDbDatabaseAccount, DatabaseAccountBicep as DocumentDbDatabaseAccountBicep
from .document_db.mongo_cluster import mongo_cluster as document_db_mongo_cluster, MongoCluster as DocumentDbMongoCluster, MongoClusterBicep as DocumentDbMongoClusterBicep
from .elastic_san.elastic_san import elastic_san as elastic_san, ElasticSan as ElasticSan, ElasticSanBicep as ElasticSanBicep
from .event_grid.domain import domain as event_grid_domain, Domain as EventGridDomain, DomainBicep as EventGridDomainBicep
from .event_grid.namespace import namespace as event_grid_namespace, Namespace as EventGridNamespace, NamespaceBicep as EventGridNamespaceBicep
from .event_grid.system_topic import system_topic as event_grid_system_topic, SystemTopic as EventGridSystemTopic, SystemTopicBicep as EventGridSystemTopicBicep
from .event_grid.topic import topic as event_grid_topic, Topic as EventGridTopic, TopicBicep as EventGridTopicBicep
from .event_hub.namespace import namespace as event_hub_namespace, Namespace as EventHubNamespace, NamespaceBicep as EventHubNamespaceBicep
from .fabric.capacity import capacity as fabric_capacity, Capacity as FabricCapacity, CapacityBicep as FabricCapacityBicep
from .hybrid_compute.machine import machine as hybrid_compute_machine, Machine as HybridComputeMachine, MachineBicep as HybridComputeMachineBicep
from .insights.action_group import action_group as insights_action_group, ActionGroup as InsightsActionGroup, ActionGroupBicep as InsightsActionGroupBicep
from .insights.activity_log_alert import activity_log_alert as insights_activity_log_alert, ActivityLogAlert as InsightsActivityLogAlert, ActivityLogAlertBicep as InsightsActivityLogAlertBicep
from .insights.component import component as insights_component, Component as InsightsComponent, ComponentBicep as InsightsComponentBicep
from .insights.data_collection_endpoint import data_collection_endpoint as insights_data_collection_endpoint, DataCollectionEndpoint as InsightsDataCollectionEndpoint, DataCollectionEndpointBicep as InsightsDataCollectionEndpointBicep
from .insights.data_collection_rule import data_collection_rule as insights_data_collection_rule, DataCollectionRule as InsightsDataCollectionRule, DataCollectionRuleBicep as InsightsDataCollectionRuleBicep
from .insights.diagnostic_setting import diagnostic_setting as insights_diagnostic_setting, DiagnosticSetting as InsightsDiagnosticSetting, DiagnosticSettingBicep as InsightsDiagnosticSettingBicep
from .insights.metric_alert import metric_alert as insights_metric_alert, MetricAlert as InsightsMetricAlert, MetricAlertBicep as InsightsMetricAlertBicep
from .insights.private_link_scope import private_link_scope as insights_private_link_scope, PrivateLinkScope as InsightsPrivateLinkScope, PrivateLinkScopeBicep as InsightsPrivateLinkScopeBicep
from .insights.scheduled_query_rule import scheduled_query_rule as insights_scheduled_query_rule, ScheduledQueryRule as InsightsScheduledQueryRule, ScheduledQueryRuleBicep as InsightsScheduledQueryRuleBicep
from .insights.webtest import webtest as insights_webtest, Webtest as InsightsWebtest, WebtestBicep as InsightsWebtestBicep
from .key_vault.vault import vault as key_vault, Vault as KeyVault, VaultBicep as KeyVaultBicep
from .kubernetes_configuration.extension import extension as kubernetes_configuration_extension, Extension as KubernetesConfigurationExtension, ExtensionBicep as KubernetesConfigurationExtensionBicep
from .kubernetes_configuration.flux_configuration import flux_configuration as kubernetes_configuration_flux_configuration, FluxConfiguration as KubernetesConfigurationFluxConfiguration, FluxConfigurationBicep as KubernetesConfigurationFluxConfigurationBicep
from .kusto.cluster import cluster as kusto_cluster, Cluster as KustoCluster, ClusterBicep as KustoClusterBicep
from .load_test_service.load_test import load_test as load_test_service_load_test, LoadTest as LoadTestServiceLoadTest, LoadTestBicep as LoadTestServiceLoadTestBicep
from .logic.workflow import workflow as logic_workflow, Workflow as LogicWorkflow, WorkflowBicep as LogicWorkflowBicep
from .machine_learning_services.workspace import workspace as machine_learning_services_workspace, Workspace as MachineLearningServicesWorkspace, WorkspaceBicep as MachineLearningServicesWorkspaceBicep
from .maintenance.maintenance_configuration import maintenance_configuration as maintenance_configuration, MaintenanceConfiguration as MaintenanceConfiguration, MaintenanceConfigurationBicep as MaintenanceConfigurationBicep
from .managed_identity.user_assigned_identity import user_assigned_identity as managed_identity_user_assigned_identity, UserAssignedIdentity as ManagedIdentityUserAssignedIdentity, UserAssignedIdentityBicep as ManagedIdentityUserAssignedIdentityBicep
from .management.management_group import management_group as management_group, ManagementGroup as ManagementGroup, ManagementGroupBicep as ManagementGroupBicep
from .net_app.net_app_account import net_app_account as net_app_account, NetAppAccount as NetAppAccount, NetAppAccountBicep as NetAppAccountBicep
from .network.application_gateway import application_gateway as network_application_gateway, ApplicationGateway as NetworkApplicationGateway, ApplicationGatewayBicep as NetworkApplicationGatewayBicep
from .network.application_gateway_web_application_firewall_policy import application_gateway_web_application_firewall_policy as network_application_gateway_web_application_firewall_policy, ApplicationGatewayWebApplicationFirewallPolicy as NetworkApplicationGatewayWebApplicationFirewallPolicy, ApplicationGatewayWebApplicationFirewallPolicyBicep as NetworkApplicationGatewayWebApplicationFirewallPolicyBicep
from .network.application_security_group import application_security_group as network_application_security_group, ApplicationSecurityGroup as NetworkApplicationSecurityGroup, ApplicationSecurityGroupBicep as NetworkApplicationSecurityGroupBicep
from .network.azure_firewall import azure_firewall as network_azure_firewall, AzureFirewall as NetworkAzureFirewall, AzureFirewallBicep as NetworkAzureFirewallBicep
from .network.bastion_host import bastion_host as network_bastion_host, BastionHost as NetworkBastionHost, BastionHostBicep as NetworkBastionHostBicep
from .network.connection import connection as network_connection, Connection as NetworkConnection, ConnectionBicep as NetworkConnectionBicep
from .network.ddos_protection_plan import ddos_protection_plan as network_ddos_protection_plan, DdosProtectionPlan as NetworkDdosProtectionPlan, DdosProtectionPlanBicep as NetworkDdosProtectionPlanBicep
from .network.dns_forwarding_ruleset import dns_forwarding_ruleset as network_dns_forwarding_ruleset, DnsForwardingRuleset as NetworkDnsForwardingRuleset, DnsForwardingRulesetBicep as NetworkDnsForwardingRulesetBicep
from .network.dns_resolver import dns_resolver as network_dns_resolver, DnsResolver as NetworkDnsResolver, DnsResolverBicep as NetworkDnsResolverBicep
from .network.dns_zone import dns_zone as network_dns_zone, DnsZone as NetworkDnsZone, DnsZoneBicep as NetworkDnsZoneBicep
from .network.express_route_circuit import express_route_circuit as network_express_route_circuit, ExpressRouteCircuit as NetworkExpressRouteCircuit, ExpressRouteCircuitBicep as NetworkExpressRouteCircuitBicep
from .network.express_route_gateway import express_route_gateway as network_express_route_gateway, ExpressRouteGateway as NetworkExpressRouteGateway, ExpressRouteGatewayBicep as NetworkExpressRouteGatewayBicep
from .network.firewall_policy import firewall_policy as network_firewall_policy, FirewallPolicy as NetworkFirewallPolicy, FirewallPolicyBicep as NetworkFirewallPolicyBicep
from .network.front_door import front_door as network_front_door, FrontDoor as NetworkFrontDoor, FrontDoorBicep as NetworkFrontDoorBicep
from .network.front_door_web_application_firewall_policy import front_door_web_application_firewall_policy as network_front_door_web_application_firewall_policy, FrontDoorWebApplicationFirewallPolicy as NetworkFrontDoorWebApplicationFirewallPolicy, FrontDoorWebApplicationFirewallPolicyBicep as NetworkFrontDoorWebApplicationFirewallPolicyBicep
from .network.ip_group import ip_group as network_ip_group, IpGroup as NetworkIpGroup, IpGroupBicep as NetworkIpGroupBicep
from .network.load_balancer import load_balancer as network_load_balancer, LoadBalancer as NetworkLoadBalancer, LoadBalancerBicep as NetworkLoadBalancerBicep
from .network.local_network_gateway import local_network_gateway as network_local_network_gateway, LocalNetworkGateway as NetworkLocalNetworkGateway, LocalNetworkGatewayBicep as NetworkLocalNetworkGatewayBicep
from .network.nat_gateway import nat_gateway as network_nat_gateway, NatGateway as NetworkNatGateway, NatGatewayBicep as NetworkNatGatewayBicep
from .network.network_interface import network_interface as network_interface, NetworkInterface as NetworkInterface, NetworkInterfaceBicep as NetworkInterfaceBicep
from .network.network_manager import network_manager as network_manager, NetworkManager as NetworkManager, NetworkManagerBicep as NetworkManagerBicep
from .network.network_security_group import network_security_group as network_security_group, NetworkSecurityGroup as NetworkSecurityGroup, NetworkSecurityGroupBicep as NetworkSecurityGroupBicep
from .network.network_watcher import network_watcher as network_watcher, NetworkWatcher as NetworkWatcher, NetworkWatcherBicep as NetworkWatcherBicep
from .network.p2s_vpn_gateway import p2s_vpn_gateway as network_p2s_vpn_gateway, P2SVpnGateway as NetworkP2SVpnGateway, P2SVpnGatewayBicep as NetworkP2SVpnGatewayBicep
from .network.private_dns_zone import private_dns_zone as network_private_dns_zone, PrivateDnsZone as NetworkPrivateDnsZone, PrivateDnsZoneBicep as NetworkPrivateDnsZoneBicep
from .network.private_endpoint import private_endpoint as network_private_endpoint, PrivateEndpoint as NetworkPrivateEndpoint, PrivateEndpointBicep as NetworkPrivateEndpointBicep
from .network.private_link_service import private_link_service as network_private_link_service, PrivateLinkService as NetworkPrivateLinkService, PrivateLinkServiceBicep as NetworkPrivateLinkServiceBicep
from .network.public_ip_address import public_ip_address as network_public_ip_address, PublicIpAddress as NetworkPublicIpAddress, PublicIpAddressBicep as NetworkPublicIpAddressBicep
from .network.public_ip_prefix import public_ip_prefix as network_public_ip_prefix, PublicIpPrefix as NetworkPublicIpPrefix, PublicIpPrefixBicep as NetworkPublicIpPrefixBicep
from .network.route_table import route_table as network_route_table, RouteTable as NetworkRouteTable, RouteTableBicep as NetworkRouteTableBicep
from .network.service_endpoint_policy import service_endpoint_policy as network_service_endpoint_policy, ServiceEndpointPolicy as NetworkServiceEndpointPolicy, ServiceEndpointPolicyBicep as NetworkServiceEndpointPolicyBicep
from .network.trafficmanagerprofile import trafficmanagerprofile as network_trafficmanagerprofile, Trafficmanagerprofile as NetworkTrafficmanagerprofile, TrafficmanagerprofileBicep as NetworkTrafficmanagerprofileBicep
from .network.virtual_hub import virtual_hub as network_virtual_hub, VirtualHub as NetworkVirtualHub, VirtualHubBicep as NetworkVirtualHubBicep
from .network.virtual_network_gateway import virtual_network_gateway as network_virtual_network_gateway, VirtualNetworkGateway as NetworkVirtualNetworkGateway, VirtualNetworkGatewayBicep as NetworkVirtualNetworkGatewayBicep
from .network.virtual_wan import virtual_wan as network_virtual_wan, VirtualWan as NetworkVirtualWan, VirtualWanBicep as NetworkVirtualWanBicep
from .network.vpn_gateway import vpn_gateway as network_vpn_gateway, VpnGateway as NetworkVpnGateway, VpnGatewayBicep as NetworkVpnGatewayBicep
from .network.vpn_server_configuration import vpn_server_configuration as network_vpn_server_configuration, VpnServerConfiguration as NetworkVpnServerConfiguration, VpnServerConfigurationBicep as NetworkVpnServerConfigurationBicep
from .network.vpn_site import vpn_site as network_vpn_site, VpnSite as NetworkVpnSite, VpnSiteBicep as NetworkVpnSiteBicep
from .operational_insights.workspace import workspace as operational_insights_workspace, Workspace as OperationalInsightsWorkspace, WorkspaceBicep as OperationalInsightsWorkspaceBicep
from .operations_management.solution import solution as operations_management_solution, Solution as OperationsManagementSolution, SolutionBicep as OperationsManagementSolutionBicep
from .portal.dashboard import dashboard as portal_dashboard, Dashboard as PortalDashboard, DashboardBicep as PortalDashboardBicep
from .power_bi_dedicated.capacity import capacity as power_bi_dedicated_capacity, Capacity as PowerBiDedicatedCapacity, CapacityBicep as PowerBiDedicatedCapacityBicep
from .purview.account import account as purview_account, Account as PurviewAccount, AccountBicep as PurviewAccountBicep
from .recovery_services.vault import vault as recovery_services_vault, Vault as RecoveryServicesVault, VaultBicep as RecoveryServicesVaultBicep
from .resource_graph.query import query as resource_graph_query, Query as ResourceGraphQuery, QueryBicep as ResourceGraphQueryBicep
from .resources.deployment_script import deployment_script as resources_deployment_script, DeploymentScript as ResourcesDeploymentScript, DeploymentScriptBicep as ResourcesDeploymentScriptBicep
from .resources.resource_group import resource_group as resource_group, ResourceGroup as ResourceGroup, ResourceGroupBicep as ResourceGroupBicep
from .search.search_service import search_service as search_service, SearchService as SearchService, SearchServiceBicep as SearchServiceBicep
from .service_bus.namespace import namespace as service_bus_namespace, Namespace as ServiceBusNamespace, NamespaceBicep as ServiceBusNamespaceBicep
from .service_fabric.cluster import cluster as service_fabric_cluster, Cluster as ServiceFabricCluster, ClusterBicep as ServiceFabricClusterBicep
from .service_networking.traffic_controller import traffic_controller as service_networking_traffic_controller, TrafficController as ServiceNetworkingTrafficController, TrafficControllerBicep as ServiceNetworkingTrafficControllerBicep
from .sql.instance_pool import instance_pool as sql_instance_pool, InstancePool as SqlInstancePool, InstancePoolBicep as SqlInstancePoolBicep
from .sql.managed_instance import managed_instance as sql_managed_instance, ManagedInstance as SqlManagedInstance, ManagedInstanceBicep as SqlManagedInstanceBicep
from .sql.server import server as sql_server, Server as SqlServer, ServerBicep as SqlServerBicep
from .storage.storage_account import storage_account as storage_account, StorageAccount as StorageAccount, StorageAccountBicep as StorageAccountBicep
from .virtual_machine_images.image_template import image_template as virtual_machine_image_template, ImageTemplate as VirtualMachineImageTemplate, ImageTemplateBicep as VirtualMachineImageTemplateBicep
from .web.hosting_environment import hosting_environment as web_hosting_environment, HostingEnvironment as WebHostingEnvironment, HostingEnvironmentBicep as WebHostingEnvironmentBicep
from .web.serverfarm import serverfarm as web_serverfarm, Serverfarm as WebServerfarm, ServerfarmBicep as WebServerfarmBicep
from .web.site import site as web_site, Site as WebSite, SiteBicep as WebSiteBicep
from .web.static_site import static_site as web_static_site, StaticSite as WebStaticSite, StaticSiteBicep as WebStaticSiteBicep

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

class ResourceMixin:
    bicep: IO[str]

    def add(self, resource, params, **kwargs):
        return globals()[resource](self.bicep, params, **kwargs)
