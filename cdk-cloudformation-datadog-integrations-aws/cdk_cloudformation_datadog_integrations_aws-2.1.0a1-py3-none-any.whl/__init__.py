'''
# AWS CDK CloudFormation Constructs for Datadog::Integrations::AWS

Datadog AWS Integration 2.1.0

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


class CfnAws(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-integrations-aws.CfnAws",
):
    '''A CloudFormation ``Datadog::Integrations::AWS``.

    :cloudformationResource: Datadog::Integrations::AWS
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        access_key_id: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
        account_specific_namespace_rules: typing.Any = None,
        external_id_secret_name: typing.Optional[builtins.str] = None,
        filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Datadog::Integrations::AWS``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param access_key_id: If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.
        :param account_id: Your AWS Account ID without dashes.
        :param account_specific_namespace_rules: An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.
        :param external_id_secret_name: The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``. Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource. Default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.
        :param filter_tags: The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.
        :param host_tags: Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.
        :param role_name: Your Datadog role delegation name.
        '''
        props = CfnAwsProps(
            access_key_id=access_key_id,
            account_id=account_id,
            account_specific_namespace_rules=account_specific_namespace_rules,
            external_id_secret_name=external_id_secret_name,
            filter_tags=filter_tags,
            host_tags=host_tags,
            role_name=role_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIntegrationID")
    def attr_integration_id(self) -> builtins.str:
        '''Attribute ``Datadog::Integrations::AWS.IntegrationID``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationID"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnAwsProps":
        '''Resource props.'''
        return typing.cast("CfnAwsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-integrations-aws.CfnAwsProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "account_id": "accountId",
        "account_specific_namespace_rules": "accountSpecificNamespaceRules",
        "external_id_secret_name": "externalIdSecretName",
        "filter_tags": "filterTags",
        "host_tags": "hostTags",
        "role_name": "roleName",
    },
)
class CfnAwsProps:
    def __init__(
        self,
        *,
        access_key_id: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
        account_specific_namespace_rules: typing.Any = None,
        external_id_secret_name: typing.Optional[builtins.str] = None,
        filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Datadog AWS Integration 2.1.0.

        :param access_key_id: If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.
        :param account_id: Your AWS Account ID without dashes.
        :param account_specific_namespace_rules: An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.
        :param external_id_secret_name: The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``. Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource. Default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.
        :param filter_tags: The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.
        :param host_tags: Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.
        :param role_name: Your Datadog role delegation name.

        :schema: CfnAwsProps
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if access_key_id is not None:
            self._values["access_key_id"] = access_key_id
        if account_id is not None:
            self._values["account_id"] = account_id
        if account_specific_namespace_rules is not None:
            self._values["account_specific_namespace_rules"] = account_specific_namespace_rules
        if external_id_secret_name is not None:
            self._values["external_id_secret_name"] = external_id_secret_name
        if filter_tags is not None:
            self._values["filter_tags"] = filter_tags
        if host_tags is not None:
            self._values["host_tags"] = host_tags
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def access_key_id(self) -> typing.Optional[builtins.str]:
        '''If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.

        :schema: CfnAwsProps#AccessKeyID
        '''
        result = self._values.get("access_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Your AWS Account ID without dashes.

        :schema: CfnAwsProps#AccountID
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_specific_namespace_rules(self) -> typing.Any:
        '''An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.

        :schema: CfnAwsProps#AccountSpecificNamespaceRules
        '''
        result = self._values.get("account_specific_namespace_rules")
        return typing.cast(typing.Any, result)

    @builtins.property
    def external_id_secret_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``.

        Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource.

        :default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.

        :schema: CfnAwsProps#ExternalIDSecretName
        '''
        result = self._values.get("external_id_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.

        :schema: CfnAwsProps#FilterTags
        '''
        result = self._values.get("filter_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.

        :schema: CfnAwsProps#HostTags
        '''
        result = self._values.get("host_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''Your Datadog role delegation name.

        :schema: CfnAwsProps#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAwsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAws",
    "CfnAwsProps",
]

publication.publish()
