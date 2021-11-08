'''
# AWS CDK CloudFormation Constructs for TrendMicro::CloudOneContainer::Helm

Deploys Trend Micro Cloud One Container Security into EKS clusters using helm.

## References

* [Documentation](https://github.com/trendmicro/cloudone-container-security-helm/blob/master/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-trend-micro-cloudone-helm-resource-provider.git)

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


class CfnHelm(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/trendmicro-cloudonecontainer-helm.CfnHelm",
):
    '''A CloudFormation ``TrendMicro::CloudOneContainer::Helm``.

    :cloudformationResource: TrendMicro::CloudOneContainer::Helm
    :link: https://github.com/aws-quickstart/quickstart-trend-micro-cloudone-helm-resource-provider.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        chart: typing.Optional[builtins.str] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional["CfnHelmPropsVpcConfiguration"] = None,
    ) -> None:
        '''Create a new ``TrendMicro::CloudOneContainer::Helm``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param chart: Chart name.
        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Values to provide to the helm chart, note that an API key is required. For supported values and documentation see: https://github.com/trendmicro/cloudone-container-security-helm/blob/master/values.yaml
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.
        '''
        props = CfnHelmProps(
            chart=chart,
            cluster_id=cluster_id,
            kube_config=kube_config,
            name=name,
            namespace=namespace,
            role_arn=role_arn,
            time_out=time_out,
            value_override_url=value_override_url,
            values=values,
            value_yaml=value_yaml,
            version=version,
            vpc_configuration=vpc_configuration,
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
        '''Attribute ``TrendMicro::CloudOneContainer::Helm.ID``.

        :link: https://github.com/aws-quickstart/quickstart-trend-micro-cloudone-helm-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnHelmProps":
        '''Resource props.'''
        return typing.cast("CfnHelmProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/trendmicro-cloudonecontainer-helm.CfnHelmProps",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "cluster_id": "clusterId",
        "kube_config": "kubeConfig",
        "name": "name",
        "namespace": "namespace",
        "role_arn": "roleArn",
        "time_out": "timeOut",
        "value_override_url": "valueOverrideUrl",
        "values": "values",
        "value_yaml": "valueYaml",
        "version": "version",
        "vpc_configuration": "vpcConfiguration",
    },
)
class CfnHelmProps:
    def __init__(
        self,
        *,
        chart: typing.Optional[builtins.str] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional["CfnHelmPropsVpcConfiguration"] = None,
    ) -> None:
        '''Deploys Trend Micro Cloud One Container Security into EKS clusters using helm.

        :param chart: Chart name.
        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Values to provide to the helm chart, note that an API key is required. For supported values and documentation see: https://github.com/trendmicro/cloudone-container-security-helm/blob/master/values.yaml
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.

        :schema: CfnHelmProps
        '''
        if isinstance(vpc_configuration, dict):
            vpc_configuration = CfnHelmPropsVpcConfiguration(**vpc_configuration)
        self._values: typing.Dict[str, typing.Any] = {}
        if chart is not None:
            self._values["chart"] = chart
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if kube_config is not None:
            self._values["kube_config"] = kube_config
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if time_out is not None:
            self._values["time_out"] = time_out
        if value_override_url is not None:
            self._values["value_override_url"] = value_override_url
        if values is not None:
            self._values["values"] = values
        if value_yaml is not None:
            self._values["value_yaml"] = value_yaml
        if version is not None:
            self._values["version"] = version
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def chart(self) -> typing.Optional[builtins.str]:
        '''Chart name.

        :schema: CfnHelmProps#Chart
        '''
        result = self._values.get("chart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''EKS cluster name.

        :schema: CfnHelmProps#ClusterID
        '''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kube_config(self) -> typing.Optional[builtins.str]:
        '''Secrets Manager ARN for kubeconfig file.

        :schema: CfnHelmProps#KubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name for the helm release.

        :schema: CfnHelmProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to use with helm.

        Created if doesn't exist and default will be used if not provided

        :schema: CfnHelmProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''IAM to use with EKS cluster authentication, if not resource execution role will be used.

        :schema: CfnHelmProps#RoleArn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_out(self) -> typing.Optional[jsii.Number]:
        '''Timeout for resource provider.

        Default 60 mins

        :schema: CfnHelmProps#TimeOut
        '''
        result = self._values.get("time_out")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value_override_url(self) -> typing.Optional[builtins.str]:
        '''Custom Value Yaml file can optionally be specified.

        :schema: CfnHelmProps#ValueOverrideURL
        '''
        result = self._values.get("value_override_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Any:
        '''Values to provide to the helm chart, note that an API key is required.

        For supported values and documentation see: https://github.com/trendmicro/cloudone-container-security-helm/blob/master/values.yaml

        :schema: CfnHelmProps#Values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Any, result)

    @builtins.property
    def value_yaml(self) -> typing.Optional[builtins.str]:
        '''String representation of a values.yaml file.

        :schema: CfnHelmProps#ValueYaml
        '''
        result = self._values.get("value_yaml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version can be specified, if not latest will be used.

        :schema: CfnHelmProps#Version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_configuration(self) -> typing.Optional["CfnHelmPropsVpcConfiguration"]:
        '''For network connectivity to Cluster inside VPC.

        :schema: CfnHelmProps#VPCConfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["CfnHelmPropsVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHelmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/trendmicro-cloudonecontainer-helm.CfnHelmPropsVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class CfnHelmPropsVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''For network connectivity to Cluster inside VPC.

        :param security_group_ids: Specify one or more security groups.
        :param subnet_ids: Specify one or more subnets.

        :schema: CfnHelmPropsVpcConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more security groups.

        :schema: CfnHelmPropsVpcConfiguration#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more subnets.

        :schema: CfnHelmPropsVpcConfiguration#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHelmPropsVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnHelm",
    "CfnHelmProps",
    "CfnHelmPropsVpcConfiguration",
]

publication.publish()
