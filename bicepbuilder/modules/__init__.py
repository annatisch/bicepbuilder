from .aad.domain_service import domain_service as aad_domain_service
from .alerts_management.action_rule import action_rule as alerts_management_action_rule
from .api_management.service import service as api_management_service
from .app.container_app import container_app as app_container_app
from .app.job import job as app_job
from .app.managed_environment import managed_environment as app_managed_environment
from .app_configuration.configuration_store import configuration_store as app_configuration_store
from .automation.automation_account import automation_account as automation_account
from .batch.batch_account import batch_account as batch_account
from .cache.redis import redis as cache_redis
from .cdn.profile import profile as cdn_profile
from .cognitive_services.account import account as cognitive_services_account
from .communication.communication_service import communication_service as communication_service
from .communication.email_service import email_service as communication_email_service
from .compute.availability_set import availability_set as compute_availability_set
from .compute.disk import disk as compute_disk
from .compute.disk_encryption_set import disk_encryption_set as compute_disk_encryption_set
from .compute.gallery import gallery as compute_gallery
from .compute.image import image as compute_image
from .compute.proximity_placement_group import proximity_placement_group as compute_proximity_placement_group
from .compute.ssh_public_key import ssh_public_key as compute_ssh_public_key
from .compute.virtual_machine import virtual_machine as compute_virtual_machine
from .compute.virtual_machine_scale_set import virtual_machine_scale_set as compute_virtual_machine_scale_set
from .consumption.budget import budget as consumption_budget
from .container_instance.container_group import container_group as container_instance_container_group
from .container_registry.registry import registry as container_registry_registry
from .container_service.managed_cluster import managed_cluster as container_service_managed_cluster
from .data_factory.factory import factory as data_factory_factory
from .data_protection.backup_vault import backup_vault as data_protection_backup_vault
from .databricks.access_connector import access_connector as databricks_access_connector
from .databricks.workspace import workspace as databricks_workspace
from .db_for_my_sql.flexible_server import flexible_server as db_for_my_sql_flexible_server
from .db_for_postgre_sql.flexible_server import flexible_server as db_for_postgre_sql_flexible_server
from .desktop_virtualization.application_group import application_group as desktop_virtualization_application_group
from .desktop_virtualization.host_pool import host_pool as desktop_virtualization_host_pool
from .desktop_virtualization.scaling_plan import scaling_plan as desktop_virtualization_scaling_plan
from .desktop_virtualization.workspace import workspace as desktop_virtualization_workspace
from .dev_ops_infrastructure.pool import pool as dev_ops_infrastructure_pool
from .dev_test_lab.lab import lab as dev_test_lab_lab
from .digital_twins.digital_twins_instance import digital_twins_instance as digital_twins_instance
from .document_db.database_account import database_account as document_db_database_account
from .document_db.mongo_cluster import mongo_cluster as document_db_mongo_cluster
from .elastic_san.elastic_san import elastic_san as elastic_san
from .event_grid.domain import domain as event_grid_domain
from .event_grid.namespace import namespace as event_grid_namespace
from .event_grid.system_topic import system_topic as event_grid_system_topic
from .event_grid.topic import topic as event_grid_topic
from .event_hub.namespace import namespace as event_hub_namespace
from .fabric.capacity import capacity as fabric_capacity
from .hybrid_compute.machine import machine as hybrid_compute_machine
from .insights.action_group import action_group as insights_action_group
from .insights.activity_log_alert import activity_log_alert as insights_activity_log_alert
from .insights.component import component as insights_component
from .insights.data_collection_endpoint import data_collection_endpoint as insights_data_collection_endpoint
from .insights.data_collection_rule import data_collection_rule as insights_data_collection_rule
from .insights.diagnostic_setting import diagnostic_setting as insights_diagnostic_setting
from .insights.metric_alert import metric_alert as insights_metric_alert
from .insights.private_link_scope import private_link_scope as insights_private_link_scope
from .insights.scheduled_query_rule import scheduled_query_rule as insights_scheduled_query_rule
from .insights.webtest import webtest as insights_webtest
from .key_vault.vault import vault as key_vault_vault
from .kubernetes_configuration.extension import extension as kubernetes_configuration_extension
from .kubernetes_configuration.flux_configuration import flux_configuration as kubernetes_configuration_flux_configuration
from .kusto.cluster import cluster as kusto_cluster
from .load_test_service.load_test import load_test as load_test_service_load_test
from .logic.workflow import workflow as logic_workflow
from .machine_learning_services.workspace import workspace as machine_learning_services_workspace
from .maintenance.maintenance_configuration import maintenance_configuration as maintenance_configuration
from .managed_identity.user_assigned_identity import user_assigned_identity as managed_identity_user_assigned_identity
from .management.management_group import management_group as management_group
from .net_app.net_app_account import net_app_account as net_app_account
from .network.application_gateway import application_gateway as network_application_gateway
from .network.application_gateway_web_application_firewall_policy import application_gateway_web_application_firewall_policy as network_application_gateway_web_application_firewall_policy
from .network.application_security_group import application_security_group as network_application_security_group
from .network.azure_firewall import azure_firewall as network_azure_firewall
from .network.bastion_host import bastion_host as network_bastion_host
from .network.connection import connection as network_connection
from .network.ddos_protection_plan import ddos_protection_plan as network_ddos_protection_plan
from .network.dns_forwarding_ruleset import dns_forwarding_ruleset as network_dns_forwarding_ruleset
from .network.dns_resolver import dns_resolver as network_dns_resolver
from .network.dns_zone import dns_zone as network_dns_zone
from .network.express_route_circuit import express_route_circuit as network_express_route_circuit
from .network.express_route_gateway import express_route_gateway as network_express_route_gateway
from .network.firewall_policy import firewall_policy as network_firewall_policy
from .network.front_door import front_door as network_front_door
from .network.front_door_web_application_firewall_policy import front_door_web_application_firewall_policy as network_front_door_web_application_firewall_policy
from .network.ip_group import ip_group as network_ip_group
from .network.load_balancer import load_balancer as network_load_balancer
from .network.local_network_gateway import local_network_gateway as network_local_network_gateway
from .network.nat_gateway import nat_gateway as network_nat_gateway
from .network.network_interface import network_interface as network_interface
from .network.network_manager import network_manager as network_manager
from .network.network_security_group import network_security_group as network_security_group
from .network.network_watcher import network_watcher as network_watcher
from .network.p2s_vpn_gateway import p2s_vpn_gateway as network_p2s_vpn_gateway
from .network.private_dns_zone import private_dns_zone as network_private_dns_zone
from .network.private_endpoint import private_endpoint as network_private_endpoint
from .network.private_link_service import private_link_service as network_private_link_service
from .network.public_ip_address import public_ip_address as network_public_ip_address
from .network.public_ip_prefix import public_ip_prefix as network_public_ip_prefix
from .network.route_table import route_table as network_route_table
from .network.service_endpoint_policy import service_endpoint_policy as network_service_endpoint_policy
from .network.trafficmanagerprofile import trafficmanagerprofile as network_trafficmanagerprofile
from .network.virtual_hub import virtual_hub as network_virtual_hub
from .network.virtual_network_gateway import virtual_network_gateway as network_virtual_network_gateway
from .network.virtual_wan import virtual_wan as network_virtual_wan
from .network.vpn_gateway import vpn_gateway as network_vpn_gateway
from .network.vpn_server_configuration import vpn_server_configuration as network_vpn_server_configuration
from .network.vpn_site import vpn_site as network_vpn_site
from .operational_insights.workspace import workspace as operational_insights_workspace
from .operations_management.solution import solution as operations_management_solution
from .portal.dashboard import dashboard as portal_dashboard
from .power_bi_dedicated.capacity import capacity as power_bi_dedicated_capacity
from .purview.account import account as purview_account
from .recovery_services.vault import vault as recovery_services_vault
from .resource_graph.query import query as resource_graph_query
from .resources.deployment_script import deployment_script as resources_deployment_script
from .resources.resource_group import resource_group as resources_resource_group
from .search.search_service import search_service as search_service
from .service_bus.namespace import namespace as service_bus_namespace
from .service_fabric.cluster import cluster as service_fabric_cluster
from .service_networking.traffic_controller import traffic_controller as service_networking_traffic_controller
from .sql.instance_pool import instance_pool as sql_instance_pool
from .sql.managed_instance import managed_instance as sql_managed_instance
from .sql.server import server as sql_server
from .storage.storage_account import storage_account as storage_account
from .virtual_machine_images.image_template import image_template as virtual_machine_images_image_template
from .web.hosting_environment import hosting_environment as web_hosting_environment
from .web.serverfarm import serverfarm as web_serverfarm
from .web.site import site as web_site
from .web.static_site import static_site as web_static_site

__all__ = [
'aad_domain_service'
'alerts_management_action_rule'
'api_management_service'
'app_container_app'
'app_job'
'app_managed_environment'
'app_configuration_store'
'automation_account'
'batch_account'
'cache_redis'
'cdn_profile'
'cognitive_services_account'
'communication_service'
'communication_email_service'
'compute_availability_set'
'compute_disk'
'compute_disk_encryption_set'
'compute_gallery'
'compute_image'
'compute_proximity_placement_group'
'compute_ssh_public_key'
'compute_virtual_machine'
'compute_virtual_machine_scale_set'
'consumption_budget'
'container_instance_container_group'
'container_registry_registry'
'container_service_managed_cluster'
'data_factory_factory'
'data_protection_backup_vault'
'databricks_access_connector'
'databricks_workspace'
'db_for_my_sql_flexible_server'
'db_for_postgre_sql_flexible_server'
'desktop_virtualization_application_group'
'desktop_virtualization_host_pool'
'desktop_virtualization_scaling_plan'
'desktop_virtualization_workspace'
'dev_ops_infrastructure_pool'
'dev_test_lab_lab'
'digital_twins_instance'
'document_db_database_account'
'document_db_mongo_cluster'
'elastic_san'
'event_grid_domain'
'event_grid_namespace'
'event_grid_system_topic'
'event_grid_topic'
'event_hub_namespace'
'fabric_capacity'
'hybrid_compute_machine'
'insights_action_group'
'insights_activity_log_alert'
'insights_component'
'insights_data_collection_endpoint'
'insights_data_collection_rule'
'insights_diagnostic_setting'
'insights_metric_alert'
'insights_private_link_scope'
'insights_scheduled_query_rule'
'insights_webtest'
'key_vault_vault'
'kubernetes_configuration_extension'
'kubernetes_configuration_flux_configuration'
'kusto_cluster'
'load_test_service_load_test'
'logic_workflow'
'machine_learning_services_workspace'
'maintenance_configuration'
'managed_identity_user_assigned_identity'
'management_group'
'net_app_account'
'network_application_gateway'
'network_application_gateway_web_application_firewall_policy'
'network_application_security_group'
'network_azure_firewall'
'network_bastion_host'
'network_connection'
'network_ddos_protection_plan'
'network_dns_forwarding_ruleset'
'network_dns_resolver'
'network_dns_zone'
'network_express_route_circuit'
'network_express_route_gateway'
'network_firewall_policy'
'network_front_door'
'network_front_door_web_application_firewall_policy'
'network_ip_group'
'network_load_balancer'
'network_local_network_gateway'
'network_nat_gateway'
'network_interface'
'network_manager'
'network_security_group'
'network_watcher'
'network_p2s_vpn_gateway'
'network_private_dns_zone'
'network_private_endpoint'
'network_private_link_service'
'network_public_ip_address'
'network_public_ip_prefix'
'network_route_table'
'network_service_endpoint_policy'
'network_trafficmanagerprofile'
'network_virtual_hub'
'network_virtual_network_gateway'
'network_virtual_wan'
'network_vpn_gateway'
'network_vpn_server_configuration'
'network_vpn_site'
'operational_insights_workspace'
'operations_management_solution'
'portal_dashboard'
'power_bi_dedicated_capacity'
'purview_account'
'recovery_services_vault'
'resource_graph_query'
'resources_deployment_script'
'resources_resource_group'
'search_service'
'service_bus_namespace'
'service_fabric_cluster'
'service_networking_traffic_controller'
'sql_instance_pool'
'sql_managed_instance'
'sql_server'
'storage_account'
'virtual_machine_images_image_template'
'web_hosting_environment'
'web_serverfarm'
'web_site'
'web_static_site'
]
