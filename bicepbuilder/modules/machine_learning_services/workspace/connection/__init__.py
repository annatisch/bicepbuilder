from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Connection(TypedDict, total=False):
    """"""
    category: Required[Literal['ADLSGen2', 'AIServices', 'AmazonMws', 'AmazonRdsForOracle', 'AmazonRdsForSqlServer', 'AmazonRedshift', 'AmazonS3Compatible', 'ApiKey', 'AzureBlob', 'AzureDatabricksDeltaLake', 'AzureDataExplorer', 'AzureMariaDb', 'AzureMySqlDb', 'AzureOneLake', 'AzureOpenAI', 'AzurePostgresDb', 'AzureSqlDb', 'AzureSqlMi', 'AzureSynapseAnalytics', 'AzureTableStorage', 'BingLLMSearch', 'Cassandra', 'CognitiveSearch', 'CognitiveService', 'Concur', 'ContainerRegistry', 'CosmosDb', 'CosmosDbMongoDbApi', 'Couchbase', 'CustomKeys', 'Db2', 'Drill', 'Dynamics', 'DynamicsAx', 'DynamicsCrm', 'Eloqua', 'FileServer', 'FtpServer', 'GenericContainerRegistry', 'GenericHttp', 'GenericRest', 'Git', 'GoogleAdWords', 'GoogleBigQuery', 'GoogleCloudStorage', 'Greenplum', 'Hbase', 'Hdfs', 'Hive', 'Hubspot', 'Impala', 'Informix', 'Jira', 'Magento', 'MariaDb', 'Marketo', 'MicrosoftAccess', 'MongoDbAtlas', 'MongoDbV2', 'MySql', 'Netezza', 'ODataRest', 'Odbc', 'Office365', 'OpenAI', 'Oracle', 'OracleCloudStorage', 'OracleServiceCloud', 'PayPal', 'Phoenix', 'PostgreSql', 'Presto', 'PythonFeed', 'QuickBooks', 'Redis', 'Responsys', 'S3', 'Salesforce', 'SalesforceMarketingCloud', 'SalesforceServiceCloud', 'SapBw', 'SapCloudForCustomer', 'SapEcc', 'SapHana', 'SapOpenHub', 'SapTable', 'Serp', 'Serverless', 'ServiceNow', 'Sftp', 'SharePointOnlineList', 'Shopify', 'Snowflake', 'Spark', 'SqlServer', 'Square', 'Sybase', 'Teradata', 'Vertica', 'WebTable', 'Xero', 'Zoho']]
    """Category of the connection."""
    connectionProperties: Required[Dict[str, object]]
    """The properties of the connection, specific to the auth type."""
    name: Required[str]
    """Name of the connection to create."""
    target: Required[str]
    """The target of the connection."""
    expiryTime: str
    """The expiry time of the connection."""
    isSharedToAll: bool
    """Indicates whether the connection is shared to all users in the workspace."""
    metadata: Dict[str, object]
    """User metadata for the connection."""
    sharedUserList: List[object]
    """The shared user list of the connection."""
    value: str
    """Value details of the workspace connection."""


class ConnectionOutputs(TypedDict, total=False):
    """Outputs for Connection"""
    name: Output[Literal['string']]
    """The name of the connection."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the connection was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the connection."""


class ConnectionBicep(Module):
    outputs: ConnectionOutputs

