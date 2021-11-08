'''
# AWS CDK CloudFormation Constructs for MongoDB::Atlas::Cluster

The cluster resource provides access to your cluster configurations. The resource lets you create, edit and delete clusters. The resource requires your Project ID.

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :schema: apiKeyDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.AutoScaling",
    jsii_struct_bases=[],
    name_mapping={"compute": "compute", "disk_gb_enabled": "diskGbEnabled"},
)
class AutoScaling:
    def __init__(
        self,
        *,
        compute: typing.Optional["Compute"] = None,
        disk_gb_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param compute: 
        :param disk_gb_enabled: 

        :schema: autoScaling
        '''
        if isinstance(compute, dict):
            compute = Compute(**compute)
        self._values: typing.Dict[str, typing.Any] = {}
        if compute is not None:
            self._values["compute"] = compute
        if disk_gb_enabled is not None:
            self._values["disk_gb_enabled"] = disk_gb_enabled

    @builtins.property
    def compute(self) -> typing.Optional["Compute"]:
        '''
        :schema: autoScaling#Compute
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["Compute"], result)

    @builtins.property
    def disk_gb_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: autoScaling#DiskGBEnabled
        '''
        result = self._values.get("disk_gb_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnCluster",
):
    '''A CloudFormation ``MongoDB::Atlas::Cluster``.

    :cloudformationResource: MongoDB::Atlas::Cluster
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        auto_scaling: typing.Optional[AutoScaling] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional["CfnClusterPropsBiConnector"] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        connection_strings: typing.Optional["ConnectionStrings"] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence["CfnClusterPropsLabels"]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        paused: typing.Optional[builtins.bool] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_backup_enabled: typing.Optional[builtins.bool] = None,
        provider_settings: typing.Optional["CfnClusterPropsProviderSettings"] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        replication_specs: typing.Optional[typing.Sequence["ReplicationSpec"]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the cluster. Once the cluster is created, its name cannot be changed.
        :param api_keys: 
        :param auto_scaling: 
        :param backup_enabled: Applicable only for M10+ clusters. Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.
        :param bi_connector: 
        :param cluster_type: Type of the cluster that you want to create.
        :param connection_strings: Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.
        :param disk_size_gb: Capacity, in gigabytes, of the hosts root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
        :param encryption_at_rest_provider: Set the Encryption at Rest parameter.
        :param labels: Array containing key-value pairs that tag and categorize the cluster.
        :param mongo_db_major_version: Major version of the cluster to deploy.
        :param num_shards: Positive integer that specifies the number of shards to deploy for a sharded cluster.
        :param paused: Flag that indicates whether the cluster is paused or not.
        :param pit_enabled: Flag that indicates if the cluster uses Point-in-Time backups. If set to true, providerBackupEnabled must also be set to true.
        :param project_id: Unique identifier of the project the cluster belongs to.
        :param provider_backup_enabled: Applicable only for M10+ clusters. Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.
        :param provider_settings: 
        :param replication_factor: ReplicationFactor is deprecated. Use replicationSpecs.
        :param replication_specs: Configuration for cluster regions.
        '''
        props = CfnClusterProps(
            name=name,
            api_keys=api_keys,
            auto_scaling=auto_scaling,
            backup_enabled=backup_enabled,
            bi_connector=bi_connector,
            cluster_type=cluster_type,
            connection_strings=connection_strings,
            disk_size_gb=disk_size_gb,
            encryption_at_rest_provider=encryption_at_rest_provider,
            labels=labels,
            mongo_db_major_version=mongo_db_major_version,
            num_shards=num_shards,
            paused=paused,
            pit_enabled=pit_enabled,
            project_id=project_id,
            provider_backup_enabled=provider_backup_enabled,
            provider_settings=provider_settings,
            replication_factor=replication_factor,
            replication_specs=replication_specs,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMongoDBVersion")
    def attr_mongo_db_version(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoDBVersion``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoDBVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMongoURI")
    def attr_mongo_uri(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURI``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURI"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMongoURIUpdated")
    def attr_mongo_uri_updated(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURIUpdated``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURIUpdated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMongoURIWithOptions")
    def attr_mongo_uri_with_options(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURIWithOptions``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURIWithOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSrvAddress")
    def attr_srv_address(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.SrvAddress``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSrvAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.StateName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnClusterProps":
        '''Resource props.'''
        return typing.cast("CfnClusterProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "api_keys": "apiKeys",
        "auto_scaling": "autoScaling",
        "backup_enabled": "backupEnabled",
        "bi_connector": "biConnector",
        "cluster_type": "clusterType",
        "connection_strings": "connectionStrings",
        "disk_size_gb": "diskSizeGb",
        "encryption_at_rest_provider": "encryptionAtRestProvider",
        "labels": "labels",
        "mongo_db_major_version": "mongoDbMajorVersion",
        "num_shards": "numShards",
        "paused": "paused",
        "pit_enabled": "pitEnabled",
        "project_id": "projectId",
        "provider_backup_enabled": "providerBackupEnabled",
        "provider_settings": "providerSettings",
        "replication_factor": "replicationFactor",
        "replication_specs": "replicationSpecs",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        auto_scaling: typing.Optional[AutoScaling] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional["CfnClusterPropsBiConnector"] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        connection_strings: typing.Optional["ConnectionStrings"] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence["CfnClusterPropsLabels"]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        paused: typing.Optional[builtins.bool] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_backup_enabled: typing.Optional[builtins.bool] = None,
        provider_settings: typing.Optional["CfnClusterPropsProviderSettings"] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        replication_specs: typing.Optional[typing.Sequence["ReplicationSpec"]] = None,
    ) -> None:
        '''The cluster resource provides access to your cluster configurations.

        The resource lets you create, edit and delete clusters. The resource requires your Project ID.

        :param name: Name of the cluster. Once the cluster is created, its name cannot be changed.
        :param api_keys: 
        :param auto_scaling: 
        :param backup_enabled: Applicable only for M10+ clusters. Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.
        :param bi_connector: 
        :param cluster_type: Type of the cluster that you want to create.
        :param connection_strings: Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.
        :param disk_size_gb: Capacity, in gigabytes, of the hosts root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
        :param encryption_at_rest_provider: Set the Encryption at Rest parameter.
        :param labels: Array containing key-value pairs that tag and categorize the cluster.
        :param mongo_db_major_version: Major version of the cluster to deploy.
        :param num_shards: Positive integer that specifies the number of shards to deploy for a sharded cluster.
        :param paused: Flag that indicates whether the cluster is paused or not.
        :param pit_enabled: Flag that indicates if the cluster uses Point-in-Time backups. If set to true, providerBackupEnabled must also be set to true.
        :param project_id: Unique identifier of the project the cluster belongs to.
        :param provider_backup_enabled: Applicable only for M10+ clusters. Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.
        :param provider_settings: 
        :param replication_factor: ReplicationFactor is deprecated. Use replicationSpecs.
        :param replication_specs: Configuration for cluster regions.

        :schema: CfnClusterProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if isinstance(auto_scaling, dict):
            auto_scaling = AutoScaling(**auto_scaling)
        if isinstance(bi_connector, dict):
            bi_connector = CfnClusterPropsBiConnector(**bi_connector)
        if isinstance(connection_strings, dict):
            connection_strings = ConnectionStrings(**connection_strings)
        if isinstance(provider_settings, dict):
            provider_settings = CfnClusterPropsProviderSettings(**provider_settings)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if backup_enabled is not None:
            self._values["backup_enabled"] = backup_enabled
        if bi_connector is not None:
            self._values["bi_connector"] = bi_connector
        if cluster_type is not None:
            self._values["cluster_type"] = cluster_type
        if connection_strings is not None:
            self._values["connection_strings"] = connection_strings
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if encryption_at_rest_provider is not None:
            self._values["encryption_at_rest_provider"] = encryption_at_rest_provider
        if labels is not None:
            self._values["labels"] = labels
        if mongo_db_major_version is not None:
            self._values["mongo_db_major_version"] = mongo_db_major_version
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if paused is not None:
            self._values["paused"] = paused
        if pit_enabled is not None:
            self._values["pit_enabled"] = pit_enabled
        if project_id is not None:
            self._values["project_id"] = project_id
        if provider_backup_enabled is not None:
            self._values["provider_backup_enabled"] = provider_backup_enabled
        if provider_settings is not None:
            self._values["provider_settings"] = provider_settings
        if replication_factor is not None:
            self._values["replication_factor"] = replication_factor
        if replication_specs is not None:
            self._values["replication_specs"] = replication_specs

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the cluster.

        Once the cluster is created, its name cannot be changed.

        :schema: CfnClusterProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :schema: CfnClusterProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[AutoScaling]:
        '''
        :schema: CfnClusterProps#AutoScaling
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[AutoScaling], result)

    @builtins.property
    def backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''Applicable only for M10+ clusters.

        Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.

        :schema: CfnClusterProps#BackupEnabled
        '''
        result = self._values.get("backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bi_connector(self) -> typing.Optional["CfnClusterPropsBiConnector"]:
        '''
        :schema: CfnClusterProps#BiConnector
        '''
        result = self._values.get("bi_connector")
        return typing.cast(typing.Optional["CfnClusterPropsBiConnector"], result)

    @builtins.property
    def cluster_type(self) -> typing.Optional[builtins.str]:
        '''Type of the cluster that you want to create.

        :schema: CfnClusterProps#ClusterType
        '''
        result = self._values.get("cluster_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_strings(self) -> typing.Optional["ConnectionStrings"]:
        '''Set of connection strings that your applications use to connect to this cluster.

        Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.

        :schema: CfnClusterProps#ConnectionStrings
        '''
        result = self._values.get("connection_strings")
        return typing.cast(typing.Optional["ConnectionStrings"], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Capacity, in gigabytes, of the hosts root volume.

        Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.

        :schema: CfnClusterProps#DiskSizeGB
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_at_rest_provider(
        self,
    ) -> typing.Optional["CfnClusterPropsEncryptionAtRestProvider"]:
        '''Set the Encryption at Rest parameter.

        :schema: CfnClusterProps#EncryptionAtRestProvider
        '''
        result = self._values.get("encryption_at_rest_provider")
        return typing.cast(typing.Optional["CfnClusterPropsEncryptionAtRestProvider"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["CfnClusterPropsLabels"]]:
        '''Array containing key-value pairs that tag and categorize the cluster.

        :schema: CfnClusterProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["CfnClusterPropsLabels"]], result)

    @builtins.property
    def mongo_db_major_version(self) -> typing.Optional[builtins.str]:
        '''Major version of the cluster to deploy.

        :schema: CfnClusterProps#MongoDBMajorVersion
        '''
        result = self._values.get("mongo_db_major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''Positive integer that specifies the number of shards to deploy for a sharded cluster.

        :schema: CfnClusterProps#NumShards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def paused(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates whether the cluster is paused or not.

        :schema: CfnClusterProps#Paused
        '''
        result = self._values.get("paused")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pit_enabled(self) -> typing.Optional[builtins.bool]:
        '''Flag that indicates if the cluster uses Point-in-Time backups.

        If set to true, providerBackupEnabled must also be set to true.

        :schema: CfnClusterProps#PitEnabled
        '''
        result = self._values.get("pit_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the project the cluster belongs to.

        :schema: CfnClusterProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''Applicable only for M10+ clusters.

        Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.

        :schema: CfnClusterProps#ProviderBackupEnabled
        '''
        result = self._values.get("provider_backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def provider_settings(self) -> typing.Optional["CfnClusterPropsProviderSettings"]:
        '''
        :schema: CfnClusterProps#ProviderSettings
        '''
        result = self._values.get("provider_settings")
        return typing.cast(typing.Optional["CfnClusterPropsProviderSettings"], result)

    @builtins.property
    def replication_factor(self) -> typing.Optional[jsii.Number]:
        '''ReplicationFactor is deprecated.

        Use replicationSpecs.

        :schema: CfnClusterProps#ReplicationFactor
        '''
        result = self._values.get("replication_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replication_specs(self) -> typing.Optional[typing.List["ReplicationSpec"]]:
        '''Configuration for cluster regions.

        :schema: CfnClusterProps#ReplicationSpecs
        '''
        result = self._values.get("replication_specs")
        return typing.cast(typing.Optional[typing.List["ReplicationSpec"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsBiConnector",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "read_preference": "readPreference"},
)
class CfnClusterPropsBiConnector:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        read_preference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: 
        :param read_preference: 

        :schema: CfnClusterPropsBiConnector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_preference is not None:
            self._values["read_preference"] = read_preference

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnClusterPropsBiConnector#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_preference(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsBiConnector#ReadPreference
        '''
        result = self._values.get("read_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsBiConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsEncryptionAtRestProvider"
)
class CfnClusterPropsEncryptionAtRestProvider(enum.Enum):
    '''Set the Encryption at Rest parameter.

    :schema: CfnClusterPropsEncryptionAtRestProvider
    '''

    AWS = "AWS"
    '''AWS.'''
    GCP = "GCP"
    '''GCP.'''
    AZURE = "AZURE"
    '''AZURE.'''
    NONE = "NONE"
    '''NONE.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsLabels",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CfnClusterPropsLabels:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: CfnClusterPropsLabels
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsLabels#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsLabels#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsProviderSettings",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling": "autoScaling",
        "backing_provider_name": "backingProviderName",
        "disk_iops": "diskIops",
        "encrypt_ebs_volume": "encryptEbsVolume",
        "instance_size_name": "instanceSizeName",
        "provider_name": "providerName",
        "region_name": "regionName",
        "volume_type": "volumeType",
    },
)
class CfnClusterPropsProviderSettings:
    def __init__(
        self,
        *,
        auto_scaling: typing.Optional[AutoScaling] = None,
        backing_provider_name: typing.Optional[builtins.str] = None,
        disk_iops: typing.Optional[jsii.Number] = None,
        encrypt_ebs_volume: typing.Optional[builtins.bool] = None,
        instance_size_name: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling: 
        :param backing_provider_name: 
        :param disk_iops: 
        :param encrypt_ebs_volume: 
        :param instance_size_name: 
        :param provider_name: 
        :param region_name: 
        :param volume_type: 

        :schema: CfnClusterPropsProviderSettings
        '''
        if isinstance(auto_scaling, dict):
            auto_scaling = AutoScaling(**auto_scaling)
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if backing_provider_name is not None:
            self._values["backing_provider_name"] = backing_provider_name
        if disk_iops is not None:
            self._values["disk_iops"] = disk_iops
        if encrypt_ebs_volume is not None:
            self._values["encrypt_ebs_volume"] = encrypt_ebs_volume
        if instance_size_name is not None:
            self._values["instance_size_name"] = instance_size_name
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if region_name is not None:
            self._values["region_name"] = region_name
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def auto_scaling(self) -> typing.Optional[AutoScaling]:
        '''
        :schema: CfnClusterPropsProviderSettings#AutoScaling
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[AutoScaling], result)

    @builtins.property
    def backing_provider_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsProviderSettings#BackingProviderName
        '''
        result = self._values.get("backing_provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_iops(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnClusterPropsProviderSettings#DiskIOPS
        '''
        result = self._values.get("disk_iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encrypt_ebs_volume(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnClusterPropsProviderSettings#EncryptEBSVolume
        '''
        result = self._values.get("encrypt_ebs_volume")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_size_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsProviderSettings#InstanceSizeName
        '''
        result = self._values.get("instance_size_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsProviderSettings#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsProviderSettings#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnClusterPropsProviderSettings#VolumeType
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsProviderSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.Compute",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "max_instance_size": "maxInstanceSize",
        "min_instance_size": "minInstanceSize",
        "scale_down_enabled": "scaleDownEnabled",
    },
)
class Compute:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        max_instance_size: typing.Optional[builtins.str] = None,
        min_instance_size: typing.Optional[builtins.str] = None,
        scale_down_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param enabled: 
        :param max_instance_size: 
        :param min_instance_size: 
        :param scale_down_enabled: 

        :schema: compute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if max_instance_size is not None:
            self._values["max_instance_size"] = max_instance_size
        if min_instance_size is not None:
            self._values["min_instance_size"] = min_instance_size
        if scale_down_enabled is not None:
            self._values["scale_down_enabled"] = scale_down_enabled

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: compute#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_instance_size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: compute#MaxInstanceSize
        '''
        result = self._values.get("max_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_instance_size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: compute#MinInstanceSize
        '''
        result = self._values.get("min_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: compute#ScaleDownEnabled
        '''
        result = self._values.get("scale_down_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Compute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ConnectionStrings",
    jsii_struct_bases=[],
    name_mapping={
        "private": "private",
        "private_srv": "privateSrv",
        "standard": "standard",
        "standard_srv": "standardSrv",
    },
)
class ConnectionStrings:
    def __init__(
        self,
        *,
        private: typing.Optional[builtins.str] = None,
        private_srv: typing.Optional[builtins.str] = None,
        standard: typing.Optional[builtins.str] = None,
        standard_srv: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private: 
        :param private_srv: 
        :param standard: 
        :param standard_srv: 

        :schema: connectionStrings
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if private is not None:
            self._values["private"] = private
        if private_srv is not None:
            self._values["private_srv"] = private_srv
        if standard is not None:
            self._values["standard"] = standard
        if standard_srv is not None:
            self._values["standard_srv"] = standard_srv

    @builtins.property
    def private(self) -> typing.Optional[builtins.str]:
        '''
        :schema: connectionStrings#Private
        '''
        result = self._values.get("private")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_srv(self) -> typing.Optional[builtins.str]:
        '''
        :schema: connectionStrings#PrivateSrv
        '''
        result = self._values.get("private_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard(self) -> typing.Optional[builtins.str]:
        '''
        :schema: connectionStrings#Standard
        '''
        result = self._values.get("standard")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard_srv(self) -> typing.Optional[builtins.str]:
        '''
        :schema: connectionStrings#StandardSrv
        '''
        result = self._values.get("standard_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.RegionsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "analytics_nodes": "analyticsNodes",
        "electable_nodes": "electableNodes",
        "priority": "priority",
        "read_only_nodes": "readOnlyNodes",
        "region_name": "regionName",
    },
)
class RegionsConfig:
    def __init__(
        self,
        *,
        analytics_nodes: typing.Optional[jsii.Number] = None,
        electable_nodes: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        read_only_nodes: typing.Optional[jsii.Number] = None,
        region_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analytics_nodes: 
        :param electable_nodes: 
        :param priority: 
        :param read_only_nodes: 
        :param region_name: 

        :schema: regionsConfig
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analytics_nodes is not None:
            self._values["analytics_nodes"] = analytics_nodes
        if electable_nodes is not None:
            self._values["electable_nodes"] = electable_nodes
        if priority is not None:
            self._values["priority"] = priority
        if read_only_nodes is not None:
            self._values["read_only_nodes"] = read_only_nodes
        if region_name is not None:
            self._values["region_name"] = region_name

    @builtins.property
    def analytics_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: regionsConfig#AnalyticsNodes
        '''
        result = self._values.get("analytics_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def electable_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: regionsConfig#ElectableNodes
        '''
        result = self._values.get("electable_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: regionsConfig#Priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: regionsConfig#ReadOnlyNodes
        '''
        result = self._values.get("read_only_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: regionsConfig#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ReplicationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "num_shards": "numShards",
        "regions_config": "regionsConfig",
        "zone_name": "zoneName",
    },
)
class ReplicationSpec:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        regions_config: typing.Optional[typing.Sequence[RegionsConfig]] = None,
        zone_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param num_shards: 
        :param regions_config: 
        :param zone_name: 

        :schema: replicationSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if regions_config is not None:
            self._values["regions_config"] = regions_config
        if zone_name is not None:
            self._values["zone_name"] = zone_name

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: replicationSpec#ID
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: replicationSpec#NumShards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def regions_config(self) -> typing.Optional[typing.List[RegionsConfig]]:
        '''
        :schema: replicationSpec#RegionsConfig
        '''
        result = self._values.get("regions_config")
        return typing.cast(typing.Optional[typing.List[RegionsConfig]], result)

    @builtins.property
    def zone_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: replicationSpec#ZoneName
        '''
        result = self._values.get("zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "AutoScaling",
    "CfnCluster",
    "CfnClusterProps",
    "CfnClusterPropsBiConnector",
    "CfnClusterPropsEncryptionAtRestProvider",
    "CfnClusterPropsLabels",
    "CfnClusterPropsProviderSettings",
    "Compute",
    "ConnectionStrings",
    "RegionsConfig",
    "ReplicationSpec",
]

publication.publish()
