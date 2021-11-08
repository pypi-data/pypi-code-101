'''
# AWS CDK CloudFormation Constructs for AWSQS::Kubernetes::Resource

Applys a YAML manifest to the specified Kubernetes cluster

## References

* [Documentation](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-amazon-eks.git)

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


class CfnResource(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-resource.CfnResource",
):
    '''A CloudFormation ``AWSQS::Kubernetes::Resource``.

    :cloudformationResource: AWSQS::Kubernetes::Resource
    :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        manifest: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWSQS::Kubernetes::Resource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Name of the EKS cluster.
        :param manifest: Text representation of the kubernetes yaml manifests to apply to the cluster.
        :param namespace: Kubernetes namespace.
        :param url: Url to the kubernetes yaml manifests to apply to the cluster. Urls starting with s3:// will be fetched using an authenticated S3 read.
        '''
        props = CfnResourceProps(
            cluster_name=cluster_name, manifest=manifest, namespace=namespace, url=url
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCfnId")
    def attr_cfn_id(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.CfnId``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCfnId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.Name``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResourceVersion")
    def attr_resource_version(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.ResourceVersion``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSelfLink")
    def attr_self_link(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.SelfLink``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelfLink"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.Uid``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnResourceProps":
        '''Resource props.'''
        return typing.cast("CfnResourceProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-resource.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "manifest": "manifest",
        "namespace": "namespace",
        "url": "url",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        manifest: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Applys a YAML manifest to the specified Kubernetes cluster.

        :param cluster_name: Name of the EKS cluster.
        :param manifest: Text representation of the kubernetes yaml manifests to apply to the cluster.
        :param namespace: Kubernetes namespace.
        :param url: Url to the kubernetes yaml manifests to apply to the cluster. Urls starting with s3:// will be fetched using an authenticated S3 read.

        :schema: CfnResourceProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
        }
        if manifest is not None:
            self._values["manifest"] = manifest
        if namespace is not None:
            self._values["namespace"] = namespace
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Name of the EKS cluster.

        :schema: CfnResourceProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manifest(self) -> typing.Optional[builtins.str]:
        '''Text representation of the kubernetes yaml manifests to apply to the cluster.

        :schema: CfnResourceProps#Manifest
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Kubernetes namespace.

        :schema: CfnResourceProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Url to the kubernetes yaml manifests to apply to the cluster.

        Urls starting with s3:// will be fetched using an authenticated S3 read.

        :schema: CfnResourceProps#Url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnResource",
    "CfnResourceProps",
]

publication.publish()
