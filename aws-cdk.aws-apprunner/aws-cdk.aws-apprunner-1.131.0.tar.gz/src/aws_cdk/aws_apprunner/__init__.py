'''
# AWS::AppRunner Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_apprunner as apprunner
```

## Introduction

AWS App Runner is a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs, at scale and with no prior infrastructure experience required. Start with your source code or a container image. App Runner automatically builds and deploys the web application and load balances traffic with encryption. App Runner also scales up or down automatically to meet your traffic needs. With App Runner, rather than thinking about servers or scaling, you have more time to focus on your applications.

## Service

The `Service` construct allows you to create AWS App Runner services with `ECR Public`, `ECR` or `Github` with the `source` property in the following scenarios:

* `Source.fromEcr()` - To define the source repository from `ECR`.
* `Source.fromEcrPublic()` - To define the source repository from `ECR Public`.
* `Source.fromGitHub()` - To define the source repository from the `Github repository`.
* `Source.fromAsset()` - To define the source from local asset directory.

## ECR Public

To create a `Service` with ECR Public:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Service(stack, "Service",
    source=Source.from_ecr_public(
        image_configuration={"port": 8000},
        image_identifier="public.ecr.aws/aws-containers/hello-app-runner:latest"
    )
)
```

## ECR

To create a `Service` from an existing ECR repository:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Service(stack, "Service",
    source=Source.from_ecr(
        image_configuration={"port": 80},
        repository=ecr.Repository.from_repository_name(stack, "NginxRepository", "nginx"),
        tag="latest"
    )
)
```

To create a `Service` from local docker image asset directory  built and pushed to Amazon ECR:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
image_asset = assets.DockerImageAsset(stack, "ImageAssets",
    directory=path.join(__dirname, "./docker.assets")
)
Service(stack, "Service",
    source=Source.from_asset(
        image_configuration={"port": 8000},
        asset=image_asset
    )
)
```

## GitHub

To create a `Service` from the GitHub repository, you need to specify an existing App Runner `Connection`.

See [Managing App Runner connections](https://docs.aws.amazon.com/apprunner/latest/dg/manage-connections.html) for more details.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Service(stack, "Service",
    source=Source.from_git_hub(
        repository_url="https://github.com/aws-containers/hello-app-runner",
        branch="main",
        configuration_source=ConfigurationSourceType.REPOSITORY,
        connection=GitHubConnection.from_connection_arn("CONNECTION_ARN")
    )
)
```

Use `codeConfigurationValues` to override configuration values with the `API` configuration source type.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Service(stack, "Service",
    source=Source.from_git_hub(
        repository_url="https://github.com/aws-containers/hello-app-runner",
        branch="main",
        configuration_source=ConfigurationSourceType.API,
        code_configuration_values={
            "runtime": Runtime.PYTHON_3,
            "port": "8000",
            "start_command": "python app.py",
            "build_command": "yum install -y pycairo && pip install -r requirements.txt"
        },
        connection=GitHubConnection.from_connection_arn("CONNECTION_ARN")
    )
)
```

## IAM Roles

You are allowed to define `instanceRole` and `accessRole` for the `Service`.

`instanceRole` - The IAM role that provides permissions to your App Runner service. These are permissions that
your code needs when it calls any AWS APIs.

`accessRole` - The IAM role that grants the App Runner service access to a source repository. It's required for
ECR image repositories (but not for ECR Public repositories). If not defined, a new access role will be generated
when required.

See [App Runner IAM Roles](https://docs.aws.amazon.com/apprunner/latest/dg/security_iam_service-with-iam.html#security_iam_service-with-iam-roles) for more details.
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

import aws_cdk.aws_ecr
import aws_cdk.aws_ecr_assets
import aws_cdk.aws_iam
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.AssetProps",
    jsii_struct_bases=[],
    name_mapping={"asset": "asset", "image_configuration": "imageConfiguration"},
)
class AssetProps:
    def __init__(
        self,
        *,
        asset: aws_cdk.aws_ecr_assets.DockerImageAsset,
        image_configuration: typing.Optional["ImageConfiguration"] = None,
    ) -> None:
        '''(experimental) Properties of the image repository for ``Source.fromAsset()``.

        :param asset: (experimental) Represents the docker image asset.
        :param image_configuration: (experimental) The image configuration for the image built from the asset. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        if isinstance(image_configuration, dict):
            image_configuration = ImageConfiguration(**image_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "asset": asset,
        }
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration

    @builtins.property
    def asset(self) -> aws_cdk.aws_ecr_assets.DockerImageAsset:
        '''(experimental) Represents the docker image asset.

        :stability: experimental
        '''
        result = self._values.get("asset")
        assert result is not None, "Required property 'asset' is missing"
        return typing.cast(aws_cdk.aws_ecr_assets.DockerImageAsset, result)

    @builtins.property
    def image_configuration(self) -> typing.Optional["ImageConfiguration"]:
        '''(experimental) The image configuration for the image built from the asset.

        :default: - no image configuration will be passed. The default ``port`` will be 8080.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
        :stability: experimental
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional["ImageConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnService(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.CfnService",
):
    '''A CloudFormation ``AWS::AppRunner::Service``.

    :cloudformationResource: AWS::AppRunner::Service
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        source_configuration: typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]] = None,
        health_check_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AppRunner::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source_configuration: ``AWS::AppRunner::Service.SourceConfiguration``.
        :param auto_scaling_configuration_arn: ``AWS::AppRunner::Service.AutoScalingConfigurationArn``.
        :param encryption_configuration: ``AWS::AppRunner::Service.EncryptionConfiguration``.
        :param health_check_configuration: ``AWS::AppRunner::Service.HealthCheckConfiguration``.
        :param instance_configuration: ``AWS::AppRunner::Service.InstanceConfiguration``.
        :param service_name: ``AWS::AppRunner::Service.ServiceName``.
        :param tags: ``AWS::AppRunner::Service.Tags``.
        '''
        props = CfnServiceProps(
            source_configuration=source_configuration,
            auto_scaling_configuration_arn=auto_scaling_configuration_arn,
            encryption_configuration=encryption_configuration,
            health_check_configuration=health_check_configuration,
            instance_configuration=instance_configuration,
            service_name=service_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceUrl")
    def attr_service_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable]:
        '''``AWS::AppRunner::Service.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        return typing.cast(typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Union["CfnService.SourceConfigurationProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "sourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.AutoScalingConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationArn"))

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "autoScalingConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.EncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.EncryptionConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.HealthCheckConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]], jsii.get(self, "healthCheckConfiguration"))

    @health_check_configuration.setter
    def health_check_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "healthCheckConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]]:
        '''``AWS::AppRunner::Service.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.InstanceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.ServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_role_arn": "accessRoleArn",
            "connection_arn": "connectionArn",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            access_role_arn: typing.Optional[builtins.str] = None,
            connection_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param access_role_arn: ``CfnService.AuthenticationConfigurationProperty.AccessRoleArn``.
            :param connection_arn: ``CfnService.AuthenticationConfigurationProperty.ConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_role_arn is not None:
                self._values["access_role_arn"] = access_role_arn
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn

        @builtins.property
        def access_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.AuthenticationConfigurationProperty.AccessRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn
            '''
            result = self._values.get("access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.AuthenticationConfigurationProperty.ConnectionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_source": "configurationSource",
            "code_configuration_values": "codeConfigurationValues",
        },
    )
    class CodeConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_source: builtins.str,
            code_configuration_values: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]] = None,
        ) -> None:
            '''
            :param configuration_source: ``CfnService.CodeConfigurationProperty.ConfigurationSource``.
            :param code_configuration_values: ``CfnService.CodeConfigurationProperty.CodeConfigurationValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "configuration_source": configuration_source,
            }
            if code_configuration_values is not None:
                self._values["code_configuration_values"] = code_configuration_values

        @builtins.property
        def configuration_source(self) -> builtins.str:
            '''``CfnService.CodeConfigurationProperty.ConfigurationSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource
            '''
            result = self._values.get("configuration_source")
            assert result is not None, "Required property 'configuration_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def code_configuration_values(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]]:
            '''``CfnService.CodeConfigurationProperty.CodeConfigurationValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues
            '''
            result = self._values.get("code_configuration_values")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationValuesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeConfigurationValuesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "runtime": "runtime",
            "build_command": "buildCommand",
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class CodeConfigurationValuesProperty:
        def __init__(
            self,
            *,
            runtime: builtins.str,
            build_command: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param runtime: ``CfnService.CodeConfigurationValuesProperty.Runtime``.
            :param build_command: ``CfnService.CodeConfigurationValuesProperty.BuildCommand``.
            :param port: ``CfnService.CodeConfigurationValuesProperty.Port``.
            :param runtime_environment_variables: ``CfnService.CodeConfigurationValuesProperty.RuntimeEnvironmentVariables``.
            :param start_command: ``CfnService.CodeConfigurationValuesProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "runtime": runtime,
            }
            if build_command is not None:
                self._values["build_command"] = build_command
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def runtime(self) -> builtins.str:
            '''``CfnService.CodeConfigurationValuesProperty.Runtime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def build_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.BuildCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand
            '''
            result = self._values.get("build_command")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]]:
            '''``CfnService.CodeConfigurationValuesProperty.RuntimeEnvironmentVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.CodeConfigurationValuesProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.CodeRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "source_code_version": "sourceCodeVersion",
            "code_configuration": "codeConfiguration",
        },
    )
    class CodeRepositoryProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            source_code_version: typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"],
            code_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param repository_url: ``CfnService.CodeRepositoryProperty.RepositoryUrl``.
            :param source_code_version: ``CfnService.CodeRepositoryProperty.SourceCodeVersion``.
            :param code_configuration: ``CfnService.CodeRepositoryProperty.CodeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
                "source_code_version": source_code_version,
            }
            if code_configuration is not None:
                self._values["code_configuration"] = code_configuration

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''``CfnService.CodeRepositoryProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_code_version(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"]:
            '''``CfnService.CodeRepositoryProperty.SourceCodeVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion
            '''
            result = self._values.get("source_code_version")
            assert result is not None, "Required property 'source_code_version' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnService.SourceCodeVersionProperty"], result)

        @builtins.property
        def code_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]]:
            '''``CfnService.CodeRepositoryProperty.CodeConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration
            '''
            result = self._values.get("code_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''
            :param kms_key: ``CfnService.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''``CfnService.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.HealthCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval": "interval",
            "path": "path",
            "protocol": "protocol",
            "timeout": "timeout",
            "unhealthy_threshold": "unhealthyThreshold",
        },
    )
    class HealthCheckConfigurationProperty:
        def __init__(
            self,
            *,
            healthy_threshold: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            path: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            timeout: typing.Optional[jsii.Number] = None,
            unhealthy_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param healthy_threshold: ``CfnService.HealthCheckConfigurationProperty.HealthyThreshold``.
            :param interval: ``CfnService.HealthCheckConfigurationProperty.Interval``.
            :param path: ``CfnService.HealthCheckConfigurationProperty.Path``.
            :param protocol: ``CfnService.HealthCheckConfigurationProperty.Protocol``.
            :param timeout: ``CfnService.HealthCheckConfigurationProperty.Timeout``.
            :param unhealthy_threshold: ``CfnService.HealthCheckConfigurationProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if healthy_threshold is not None:
                self._values["healthy_threshold"] = healthy_threshold
            if interval is not None:
                self._values["interval"] = interval
            if path is not None:
                self._values["path"] = path
            if protocol is not None:
                self._values["protocol"] = protocol
            if timeout is not None:
                self._values["timeout"] = timeout
            if unhealthy_threshold is not None:
                self._values["unhealthy_threshold"] = unhealthy_threshold

        @builtins.property
        def healthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.HealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''``CfnService.HealthCheckConfigurationProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''``CfnService.HealthCheckConfigurationProperty.Protocol``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.Timeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigurationProperty.UnhealthyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.ImageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class ImageConfigurationProperty:
        def __init__(
            self,
            *,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param port: ``CfnService.ImageConfigurationProperty.Port``.
            :param runtime_environment_variables: ``CfnService.ImageConfigurationProperty.RuntimeEnvironmentVariables``.
            :param start_command: ``CfnService.ImageConfigurationProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if port is not None:
                self._values["port"] = port
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''``CfnService.ImageConfigurationProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]]:
            '''``CfnService.ImageConfigurationProperty.RuntimeEnvironmentVariables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''``CfnService.ImageConfigurationProperty.StartCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.ImageRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_identifier": "imageIdentifier",
            "image_repository_type": "imageRepositoryType",
            "image_configuration": "imageConfiguration",
        },
    )
    class ImageRepositoryProperty:
        def __init__(
            self,
            *,
            image_identifier: builtins.str,
            image_repository_type: builtins.str,
            image_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param image_identifier: ``CfnService.ImageRepositoryProperty.ImageIdentifier``.
            :param image_repository_type: ``CfnService.ImageRepositoryProperty.ImageRepositoryType``.
            :param image_configuration: ``CfnService.ImageRepositoryProperty.ImageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_identifier": image_identifier,
                "image_repository_type": image_repository_type,
            }
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_identifier(self) -> builtins.str:
            '''``CfnService.ImageRepositoryProperty.ImageIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier
            '''
            result = self._values.get("image_identifier")
            assert result is not None, "Required property 'image_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_repository_type(self) -> builtins.str:
            '''``CfnService.ImageRepositoryProperty.ImageRepositoryType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype
            '''
            result = self._values.get("image_repository_type")
            assert result is not None, "Required property 'image_repository_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]]:
            '''``CfnService.ImageRepositoryProperty.ImageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu": "cpu",
            "instance_role_arn": "instanceRoleArn",
            "memory": "memory",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: typing.Optional[builtins.str] = None,
            instance_role_arn: typing.Optional[builtins.str] = None,
            memory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cpu: ``CfnService.InstanceConfigurationProperty.Cpu``.
            :param instance_role_arn: ``CfnService.InstanceConfigurationProperty.InstanceRoleArn``.
            :param memory: ``CfnService.InstanceConfigurationProperty.Memory``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu is not None:
                self._values["cpu"] = cpu
            if instance_role_arn is not None:
                self._values["instance_role_arn"] = instance_role_arn
            if memory is not None:
                self._values["memory"] = memory

        @builtins.property
        def cpu(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.Cpu``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.InstanceRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn
            '''
            result = self._values.get("instance_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory(self) -> typing.Optional[builtins.str]:
            '''``CfnService.InstanceConfigurationProperty.Memory``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.KeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class KeyValuePairProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnService.KeyValuePairProperty.Name``.
            :param value: ``CfnService.KeyValuePairProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnService.KeyValuePairProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnService.KeyValuePairProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.SourceCodeVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceCodeVersionProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''
            :param type: ``CfnService.SourceCodeVersionProperty.Type``.
            :param value: ``CfnService.SourceCodeVersionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnService.SourceCodeVersionProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnService.SourceCodeVersionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceCodeVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-apprunner.CfnService.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "auto_deployments_enabled": "autoDeploymentsEnabled",
            "code_repository": "codeRepository",
            "image_repository": "imageRepository",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]] = None,
            auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            code_repository: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]] = None,
            image_repository: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]] = None,
        ) -> None:
            '''
            :param authentication_configuration: ``CfnService.SourceConfigurationProperty.AuthenticationConfiguration``.
            :param auto_deployments_enabled: ``CfnService.SourceConfigurationProperty.AutoDeploymentsEnabled``.
            :param code_repository: ``CfnService.SourceConfigurationProperty.CodeRepository``.
            :param image_repository: ``CfnService.SourceConfigurationProperty.ImageRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if auto_deployments_enabled is not None:
                self._values["auto_deployments_enabled"] = auto_deployments_enabled
            if code_repository is not None:
                self._values["code_repository"] = code_repository
            if image_repository is not None:
                self._values["image_repository"] = image_repository

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]]:
            '''``CfnService.SourceConfigurationProperty.AuthenticationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.AuthenticationConfigurationProperty"]], result)

        @builtins.property
        def auto_deployments_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnService.SourceConfigurationProperty.AutoDeploymentsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled
            '''
            result = self._values.get("auto_deployments_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def code_repository(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]]:
            '''``CfnService.SourceConfigurationProperty.CodeRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository
            '''
            result = self._values.get("code_repository")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.CodeRepositoryProperty"]], result)

        @builtins.property
        def image_repository(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]]:
            '''``CfnService.SourceConfigurationProperty.ImageRepository``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository
            '''
            result = self._values.get("image_repository")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.ImageRepositoryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_configuration": "sourceConfiguration",
        "auto_scaling_configuration_arn": "autoScalingConfigurationArn",
        "encryption_configuration": "encryptionConfiguration",
        "health_check_configuration": "healthCheckConfiguration",
        "instance_configuration": "instanceConfiguration",
        "service_name": "serviceName",
        "tags": "tags",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        source_configuration: typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]] = None,
        health_check_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppRunner::Service``.

        :param source_configuration: ``AWS::AppRunner::Service.SourceConfiguration``.
        :param auto_scaling_configuration_arn: ``AWS::AppRunner::Service.AutoScalingConfigurationArn``.
        :param encryption_configuration: ``AWS::AppRunner::Service.EncryptionConfiguration``.
        :param health_check_configuration: ``AWS::AppRunner::Service.HealthCheckConfiguration``.
        :param instance_configuration: ``AWS::AppRunner::Service.InstanceConfiguration``.
        :param service_name: ``AWS::AppRunner::Service.ServiceName``.
        :param tags: ``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source_configuration": source_configuration,
        }
        if auto_scaling_configuration_arn is not None:
            self._values["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            self._values["health_check_configuration"] = health_check_configuration
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if service_name is not None:
            self._values["service_name"] = service_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable]:
        '''``AWS::AppRunner::Service.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        assert result is not None, "Required property 'source_configuration' is missing"
        return typing.cast(typing.Union[CfnService.SourceConfigurationProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.AutoScalingConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        result = self._values.get("auto_scaling_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]]:
        '''``AWS::AppRunner::Service.EncryptionConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.EncryptionConfigurationProperty]], result)

    @builtins.property
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]]:
        '''``AWS::AppRunner::Service.HealthCheckConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        result = self._values.get("health_check_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigurationProperty]], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]]:
        '''``AWS::AppRunner::Service.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.InstanceConfigurationProperty]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppRunner::Service.ServiceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AppRunner::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.CodeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_source": "configurationSource",
        "configuration_values": "configurationValues",
    },
)
class CodeConfiguration:
    def __init__(
        self,
        *,
        configuration_source: "ConfigurationSourceType",
        configuration_values: typing.Optional["CodeConfigurationValues"] = None,
    ) -> None:
        '''(experimental) Describes the configuration that AWS App Runner uses to build and run an App Runner service from a source code repository.

        :param configuration_source: (experimental) The source of the App Runner configuration.
        :param configuration_values: (experimental) The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a apprunner.yaml file in the source code repository (or ignoring the file if it exists). Default: - not specified. Use ``apprunner.yaml`` instead.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
        :stability: experimental
        '''
        if isinstance(configuration_values, dict):
            configuration_values = CodeConfigurationValues(**configuration_values)
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_source": configuration_source,
        }
        if configuration_values is not None:
            self._values["configuration_values"] = configuration_values

    @builtins.property
    def configuration_source(self) -> "ConfigurationSourceType":
        '''(experimental) The source of the App Runner configuration.

        :stability: experimental
        '''
        result = self._values.get("configuration_source")
        assert result is not None, "Required property 'configuration_source' is missing"
        return typing.cast("ConfigurationSourceType", result)

    @builtins.property
    def configuration_values(self) -> typing.Optional["CodeConfigurationValues"]:
        '''(experimental) The basic configuration for building and running the App Runner service.

        Use it to quickly launch an App Runner service without providing a apprunner.yaml file in the
        source code repository (or ignoring the file if it exists).

        :default: - not specified. Use ``apprunner.yaml`` instead.

        :stability: experimental
        '''
        result = self._values.get("configuration_values")
        return typing.cast(typing.Optional["CodeConfigurationValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.CodeConfigurationValues",
    jsii_struct_bases=[],
    name_mapping={
        "runtime": "runtime",
        "build_command": "buildCommand",
        "environment": "environment",
        "port": "port",
        "start_command": "startCommand",
    },
)
class CodeConfigurationValues:
    def __init__(
        self,
        *,
        runtime: "Runtime",
        build_command: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        port: typing.Optional[builtins.str] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Describes the basic configuration needed for building and running an AWS App Runner service.

        This type doesn't support the full set of possible configuration options. Fur full configuration capabilities,
        use a ``apprunner.yaml`` file in the source code repository.

        :param runtime: (experimental) A runtime environment type for building and running an App Runner service. It represents a programming language runtime.
        :param build_command: (experimental) The command App Runner runs to build your application. Default: - no build command.
        :param environment: (experimental) The environment variables that are available to your running App Runner service. Default: - no environment variables.
        :param port: (experimental) The port that your application listens to in the container. Default: 8080
        :param start_command: (experimental) The command App Runner runs to start your application. Default: - no start command.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "runtime": runtime,
        }
        if build_command is not None:
            self._values["build_command"] = build_command
        if environment is not None:
            self._values["environment"] = environment
        if port is not None:
            self._values["port"] = port
        if start_command is not None:
            self._values["start_command"] = start_command

    @builtins.property
    def runtime(self) -> "Runtime":
        '''(experimental) A runtime environment type for building and running an App Runner service.

        It represents
        a programming language runtime.

        :stability: experimental
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast("Runtime", result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''(experimental) The command App Runner runs to build your application.

        :default: - no build command.

        :stability: experimental
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) The environment variables that are available to your running App Runner service.

        :default: - no environment variables.

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''(experimental) The port that your application listens to in the container.

        :default: 8080

        :stability: experimental
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_command(self) -> typing.Optional[builtins.str]:
        '''(experimental) The command App Runner runs to start your application.

        :default: - no start command.

        :stability: experimental
        '''
        result = self._values.get("start_command")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfigurationValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.CodeRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "code_configuration": "codeConfiguration",
        "connection": "connection",
        "repository_url": "repositoryUrl",
        "source_code_version": "sourceCodeVersion",
    },
)
class CodeRepositoryProps:
    def __init__(
        self,
        *,
        code_configuration: CodeConfiguration,
        connection: "GitHubConnection",
        repository_url: builtins.str,
        source_code_version: "SourceCodeVersion",
    ) -> None:
        '''(experimental) Properties of the CodeRepository.

        :param code_configuration: (experimental) Configuration for building and running the service from a source code repository.
        :param connection: (experimental) The App Runner connection for GitHub.
        :param repository_url: (experimental) The location of the repository that contains the source code.
        :param source_code_version: (experimental) The version that should be used within the source code repository.

        :stability: experimental
        '''
        if isinstance(code_configuration, dict):
            code_configuration = CodeConfiguration(**code_configuration)
        if isinstance(source_code_version, dict):
            source_code_version = SourceCodeVersion(**source_code_version)
        self._values: typing.Dict[str, typing.Any] = {
            "code_configuration": code_configuration,
            "connection": connection,
            "repository_url": repository_url,
            "source_code_version": source_code_version,
        }

    @builtins.property
    def code_configuration(self) -> CodeConfiguration:
        '''(experimental) Configuration for building and running the service from a source code repository.

        :stability: experimental
        '''
        result = self._values.get("code_configuration")
        assert result is not None, "Required property 'code_configuration' is missing"
        return typing.cast(CodeConfiguration, result)

    @builtins.property
    def connection(self) -> "GitHubConnection":
        '''(experimental) The App Runner connection for GitHub.

        :stability: experimental
        '''
        result = self._values.get("connection")
        assert result is not None, "Required property 'connection' is missing"
        return typing.cast("GitHubConnection", result)

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''(experimental) The location of the repository that contains the source code.

        :stability: experimental
        '''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_code_version(self) -> "SourceCodeVersion":
        '''(experimental) The version that should be used within the source code repository.

        :stability: experimental
        '''
        result = self._values.get("source_code_version")
        assert result is not None, "Required property 'source_code_version' is missing"
        return typing.cast("SourceCodeVersion", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-apprunner.ConfigurationSourceType")
class ConfigurationSourceType(enum.Enum):
    '''(experimental) The source of the App Runner configuration.

    :stability: experimental
    '''

    REPOSITORY = "REPOSITORY"
    '''(experimental) App Runner reads configuration values from ``the apprunner.yaml`` file in the source code repository and ignores ``configurationValues``.

    :stability: experimental
    '''
    API = "API"
    '''(experimental) App Runner uses configuration values provided in ``configurationValues`` and ignores the ``apprunner.yaml`` file in the source code repository.

    :stability: experimental
    '''


class Cpu(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apprunner.Cpu"):
    '''(experimental) The number of CPU units reserved for each instance of your App Runner service.

    :stability: experimental
    '''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, unit: builtins.str) -> "Cpu":
        '''(experimental) Custom CPU unit.

        :param unit: custom CPU unit.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
        :stability: experimental
        '''
        return typing.cast("Cpu", jsii.sinvoke(cls, "of", [unit]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="ONE_VCPU")
    def ONE_VCPU(cls) -> "Cpu":
        '''(experimental) 1 vCPU.

        :stability: experimental
        '''
        return typing.cast("Cpu", jsii.sget(cls, "ONE_VCPU"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="TWO_VCPU")
    def TWO_VCPU(cls) -> "Cpu":
        '''(experimental) 2 vCPU.

        :stability: experimental
        '''
        return typing.cast("Cpu", jsii.sget(cls, "TWO_VCPU"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        '''(experimental) The unit of CPU.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "unit"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.EcrProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository": "repository",
        "image_configuration": "imageConfiguration",
        "tag": "tag",
    },
)
class EcrProps:
    def __init__(
        self,
        *,
        repository: aws_cdk.aws_ecr.IRepository,
        image_configuration: typing.Optional["ImageConfiguration"] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties of the image repository for ``Source.fromEcr()``.

        :param repository: (experimental) Represents the ECR repository.
        :param image_configuration: (experimental) The image configuration for the image from ECR. Default: - no image configuration will be passed. The default ``port`` will be 8080.
        :param tag: (experimental) Image tag. Default: - 'latest'

        :stability: experimental
        '''
        if isinstance(image_configuration, dict):
            image_configuration = ImageConfiguration(**image_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "repository": repository,
        }
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def repository(self) -> aws_cdk.aws_ecr.IRepository:
        '''(experimental) Represents the ECR repository.

        :stability: experimental
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(aws_cdk.aws_ecr.IRepository, result)

    @builtins.property
    def image_configuration(self) -> typing.Optional["ImageConfiguration"]:
        '''(experimental) The image configuration for the image from ECR.

        :default: - no image configuration will be passed. The default ``port`` will be 8080.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
        :stability: experimental
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional["ImageConfiguration"], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''(experimental) Image tag.

        :default: - 'latest'

        :stability: experimental
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.EcrPublicProps",
    jsii_struct_bases=[],
    name_mapping={
        "image_identifier": "imageIdentifier",
        "image_configuration": "imageConfiguration",
    },
)
class EcrPublicProps:
    def __init__(
        self,
        *,
        image_identifier: builtins.str,
        image_configuration: typing.Optional["ImageConfiguration"] = None,
    ) -> None:
        '''(experimental) Properties of the image repository for ``Source.fromEcrPublic()``.

        :param image_identifier: (experimental) The ECR Public image URI.
        :param image_configuration: (experimental) The image configuration for the image from ECR Public. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        if isinstance(image_configuration, dict):
            image_configuration = ImageConfiguration(**image_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "image_identifier": image_identifier,
        }
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration

    @builtins.property
    def image_identifier(self) -> builtins.str:
        '''(experimental) The ECR Public image URI.

        :stability: experimental
        '''
        result = self._values.get("image_identifier")
        assert result is not None, "Required property 'image_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_configuration(self) -> typing.Optional["ImageConfiguration"]:
        '''(experimental) The image configuration for the image from ECR Public.

        :default: - no image configuration will be passed. The default ``port`` will be 8080.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
        :stability: experimental
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional["ImageConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrPublicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitHubConnection(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.GitHubConnection",
):
    '''(experimental) Represents the App Runner connection that enables the App Runner service to connect to a source repository.

    It's required for GitHub code repositories.

    :stability: experimental
    '''

    def __init__(self, arn: builtins.str) -> None:
        '''
        :param arn: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [arn])

    @jsii.member(jsii_name="fromConnectionArn") # type: ignore[misc]
    @builtins.classmethod
    def from_connection_arn(cls, arn: builtins.str) -> "GitHubConnection":
        '''(experimental) Using existing App Runner connection by specifying the connection ARN.

        :param arn: connection ARN.

        :return: Connection

        :stability: experimental
        '''
        return typing.cast("GitHubConnection", jsii.sinvoke(cls, "fromConnectionArn", [arn]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> builtins.str:
        '''(experimental) The ARN of the Connection for App Runner service to connect to the repository.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "connectionArn"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.GithubRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_source": "configurationSource",
        "connection": "connection",
        "repository_url": "repositoryUrl",
        "branch": "branch",
        "code_configuration_values": "codeConfigurationValues",
    },
)
class GithubRepositoryProps:
    def __init__(
        self,
        *,
        configuration_source: ConfigurationSourceType,
        connection: GitHubConnection,
        repository_url: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        code_configuration_values: typing.Optional[CodeConfigurationValues] = None,
    ) -> None:
        '''(experimental) Properties of the Github repository for ``Source.fromGitHub()``.

        :param configuration_source: (experimental) The source of the App Runner configuration.
        :param connection: (experimental) ARN of the connection to Github. Only required for Github source.
        :param repository_url: (experimental) The location of the repository that contains the source code.
        :param branch: (experimental) The branch name that represents a specific version for the repository. Default: main
        :param code_configuration_values: (experimental) The code configuration values. Will be ignored if configurationSource is ``REPOSITORY``. Default: - no values will be passed. The ``apprunner.yaml`` from the github reopsitory will be used instead.

        :stability: experimental
        '''
        if isinstance(code_configuration_values, dict):
            code_configuration_values = CodeConfigurationValues(**code_configuration_values)
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_source": configuration_source,
            "connection": connection,
            "repository_url": repository_url,
        }
        if branch is not None:
            self._values["branch"] = branch
        if code_configuration_values is not None:
            self._values["code_configuration_values"] = code_configuration_values

    @builtins.property
    def configuration_source(self) -> ConfigurationSourceType:
        '''(experimental) The source of the App Runner configuration.

        :stability: experimental
        '''
        result = self._values.get("configuration_source")
        assert result is not None, "Required property 'configuration_source' is missing"
        return typing.cast(ConfigurationSourceType, result)

    @builtins.property
    def connection(self) -> GitHubConnection:
        '''(experimental) ARN of the connection to Github.

        Only required for Github source.

        :stability: experimental
        '''
        result = self._values.get("connection")
        assert result is not None, "Required property 'connection' is missing"
        return typing.cast(GitHubConnection, result)

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''(experimental) The location of the repository that contains the source code.

        :stability: experimental
        '''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''(experimental) The branch name that represents a specific version for the repository.

        :default: main

        :stability: experimental
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_configuration_values(self) -> typing.Optional[CodeConfigurationValues]:
        '''(experimental) The code configuration values.

        Will be ignored if configurationSource is ``REPOSITORY``.

        :default: - no values will be passed. The ``apprunner.yaml`` from the github reopsitory will be used instead.

        :stability: experimental
        '''
        result = self._values.get("code_configuration_values")
        return typing.cast(typing.Optional[CodeConfigurationValues], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-apprunner.IService")
class IService(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''(experimental) Represents the App Runner Service.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''(experimental) The ARN of the service.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) The Name of the service.

        :stability: experimental
        '''
        ...


class _IServiceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''(experimental) Represents the App Runner Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-apprunner.IService"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''(experimental) The ARN of the service.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) The Name of the service.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IService).__jsii_proxy_class__ = lambda : _IServiceProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.ImageConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "environment": "environment",
        "port": "port",
        "start_command": "startCommand",
    },
)
class ImageConfiguration:
    def __init__(
        self,
        *,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        start_command: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Describes the configuration that AWS App Runner uses to run an App Runner service using an image pulled from a source image repository.

        :param environment: (experimental) Environment variables that are available to your running App Runner service. Default: - no environment variables
        :param port: (experimental) The port that your application listens to in the container. Default: 8080
        :param start_command: (experimental) An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command. Default: - no start command

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if environment is not None:
            self._values["environment"] = environment
        if port is not None:
            self._values["port"] = port
        if start_command is not None:
            self._values["start_command"] = start_command

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Environment variables that are available to your running App Runner service.

        :default: - no environment variables

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The port that your application listens to in the container.

        :default: 8080

        :stability: experimental
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_command(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional command that App Runner runs to start the application in the source image.

        If specified, this command overrides the Docker image’s default start command.

        :default: - no start command

        :stability: experimental
        '''
        result = self._values.get("start_command")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.ImageRepository",
    jsii_struct_bases=[],
    name_mapping={
        "image_identifier": "imageIdentifier",
        "image_repository_type": "imageRepositoryType",
        "image_configuration": "imageConfiguration",
    },
)
class ImageRepository:
    def __init__(
        self,
        *,
        image_identifier: builtins.str,
        image_repository_type: "ImageRepositoryType",
        image_configuration: typing.Optional[ImageConfiguration] = None,
    ) -> None:
        '''(experimental) Describes a source image repository.

        :param image_identifier: (experimental) The identifier of the image. For ``ECR_PUBLIC`` imageRepositoryType, the identifier domain should always be ``public.ecr.aws``. For ``ECR``, the pattern should be ``([0-9]{12}.dkr.ecr.[a-z\\-]+-[0-9]{1}.amazonaws.com\\/.*)``.
        :param image_repository_type: (experimental) The type of the image repository. This reflects the repository provider and whether the repository is private or public.
        :param image_configuration: (experimental) Configuration for running the identified image. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
        :stability: experimental
        '''
        if isinstance(image_configuration, dict):
            image_configuration = ImageConfiguration(**image_configuration)
        self._values: typing.Dict[str, typing.Any] = {
            "image_identifier": image_identifier,
            "image_repository_type": image_repository_type,
        }
        if image_configuration is not None:
            self._values["image_configuration"] = image_configuration

    @builtins.property
    def image_identifier(self) -> builtins.str:
        '''(experimental) The identifier of the image.

        For ``ECR_PUBLIC`` imageRepositoryType, the identifier domain should
        always be ``public.ecr.aws``. For ``ECR``, the pattern should be
        ``([0-9]{12}.dkr.ecr.[a-z\\-]+-[0-9]{1}.amazonaws.com\\/.*)``.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html for more details.
        :stability: experimental
        '''
        result = self._values.get("image_identifier")
        assert result is not None, "Required property 'image_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_repository_type(self) -> "ImageRepositoryType":
        '''(experimental) The type of the image repository.

        This reflects the repository provider and whether
        the repository is private or public.

        :stability: experimental
        '''
        result = self._values.get("image_repository_type")
        assert result is not None, "Required property 'image_repository_type' is missing"
        return typing.cast("ImageRepositoryType", result)

    @builtins.property
    def image_configuration(self) -> typing.Optional[ImageConfiguration]:
        '''(experimental) Configuration for running the identified image.

        :default: - no image configuration will be passed. The default ``port`` will be 8080.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
        :stability: experimental
        '''
        result = self._values.get("image_configuration")
        return typing.cast(typing.Optional[ImageConfiguration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-apprunner.ImageRepositoryType")
class ImageRepositoryType(enum.Enum):
    '''(experimental) The image repository types.

    :stability: experimental
    '''

    ECR_PUBLIC = "ECR_PUBLIC"
    '''(experimental) Amazon ECR Public.

    :stability: experimental
    '''
    ECR = "ECR"
    '''(experimental) Amazon ECR.

    :stability: experimental
    '''


class Memory(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apprunner.Memory"):
    '''(experimental) The amount of memory reserved for each instance of your App Runner service.

    :stability: experimental
    '''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, unit: builtins.str) -> "Memory":
        '''(experimental) Custom Memory unit.

        :param unit: custom Memory unit.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
        :stability: experimental
        '''
        return typing.cast("Memory", jsii.sinvoke(cls, "of", [unit]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="FOUR_GB")
    def FOUR_GB(cls) -> "Memory":
        '''(experimental) 4 GB(for 1 or 2 vCPU).

        :stability: experimental
        '''
        return typing.cast("Memory", jsii.sget(cls, "FOUR_GB"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="THREE_GB")
    def THREE_GB(cls) -> "Memory":
        '''(experimental) 3 GB(for 1 vCPU).

        :stability: experimental
        '''
        return typing.cast("Memory", jsii.sget(cls, "THREE_GB"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="TWO_GB")
    def TWO_GB(cls) -> "Memory":
        '''(experimental) 2 GB(for 1 vCPU).

        :stability: experimental
        '''
        return typing.cast("Memory", jsii.sget(cls, "TWO_GB"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        '''(experimental) The unit of memory.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "unit"))


class Runtime(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apprunner.Runtime"):
    '''(experimental) The code runtimes.

    :stability: experimental
    '''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, name: builtins.str) -> "Runtime":
        '''(experimental) Other runtimes.

        :param name: runtime name.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime for all available runtimes.
        :stability: experimental
        '''
        return typing.cast("Runtime", jsii.sinvoke(cls, "of", [name]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="NODEJS_12")
    def NODEJS_12(cls) -> "Runtime":
        '''(experimental) NodeJS 12.

        :stability: experimental
        '''
        return typing.cast("Runtime", jsii.sget(cls, "NODEJS_12"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="PYTHON_3")
    def PYTHON_3(cls) -> "Runtime":
        '''(experimental) Python 3.

        :stability: experimental
        '''
        return typing.cast("Runtime", jsii.sget(cls, "PYTHON_3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The runtime name.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


class Service(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.Service",
):
    '''(experimental) The App Runner Service.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        source: "Source",
        access_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        cpu: typing.Optional[Cpu] = None,
        instance_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory: typing.Optional[Memory] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param source: (experimental) The source of the repository for the service.
        :param access_role: (experimental) The IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories). Default: - generate a new access role.
        :param cpu: (experimental) The number of CPU units reserved for each instance of your App Runner service. Default: Cpu.ONE_VCPU
        :param instance_role: (experimental) The IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any AWS APIs. Default: - no instance role attached.
        :param memory: (experimental) The amount of memory reserved for each instance of your App Runner service. Default: Memory.TWO_GB
        :param service_name: (experimental) Name of the service. Default: - auto-generated if undefined.

        :stability: experimental
        '''
        props = ServiceProps(
            source=source,
            access_role=access_role,
            cpu=cpu,
            instance_role=instance_role,
            memory=memory,
            service_name=service_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServiceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_service_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service_arn: builtins.str,
        service_name: builtins.str,
        service_status: builtins.str,
        service_url: builtins.str,
    ) -> IService:
        '''(experimental) Import from service attributes.

        :param scope: -
        :param id: -
        :param service_arn: (experimental) The ARN of the service.
        :param service_name: (experimental) The name of the service.
        :param service_status: (experimental) The status of the service.
        :param service_url: (experimental) The URL of the service.

        :stability: experimental
        '''
        attrs = ServiceAttributes(
            service_arn=service_arn,
            service_name=service_name,
            service_status=service_status,
            service_url=service_url,
        )

        return typing.cast(IService, jsii.sinvoke(cls, "fromServiceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromServiceName") # type: ignore[misc]
    @builtins.classmethod
    def from_service_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        service_name: builtins.str,
    ) -> IService:
        '''(experimental) Import from service name.

        :param scope: -
        :param id: -
        :param service_name: -

        :stability: experimental
        '''
        return typing.cast(IService, jsii.sinvoke(cls, "fromServiceName", [scope, id, service_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''(experimental) The ARN of the Service.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''(experimental) The ID of the Service.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) The name of the service.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceStatus")
    def service_status(self) -> builtins.str:
        '''(experimental) The status of the Service.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceUrl")
    def service_url(self) -> builtins.str:
        '''(experimental) The URL of the Service.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceUrl"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.ServiceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "service_arn": "serviceArn",
        "service_name": "serviceName",
        "service_status": "serviceStatus",
        "service_url": "serviceUrl",
    },
)
class ServiceAttributes:
    def __init__(
        self,
        *,
        service_arn: builtins.str,
        service_name: builtins.str,
        service_status: builtins.str,
        service_url: builtins.str,
    ) -> None:
        '''(experimental) Attributes for the App Runner Service.

        :param service_arn: (experimental) The ARN of the service.
        :param service_name: (experimental) The name of the service.
        :param service_status: (experimental) The status of the service.
        :param service_url: (experimental) The URL of the service.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service_arn": service_arn,
            "service_name": service_name,
            "service_status": service_status,
            "service_url": service_url,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''(experimental) The ARN of the service.

        :stability: experimental
        '''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''(experimental) The name of the service.

        :stability: experimental
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_status(self) -> builtins.str:
        '''(experimental) The status of the service.

        :stability: experimental
        '''
        result = self._values.get("service_status")
        assert result is not None, "Required property 'service_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_url(self) -> builtins.str:
        '''(experimental) The URL of the service.

        :stability: experimental
        '''
        result = self._values.get("service_url")
        assert result is not None, "Required property 'service_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.ServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "access_role": "accessRole",
        "cpu": "cpu",
        "instance_role": "instanceRole",
        "memory": "memory",
        "service_name": "serviceName",
    },
)
class ServiceProps:
    def __init__(
        self,
        *,
        source: "Source",
        access_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        cpu: typing.Optional[Cpu] = None,
        instance_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory: typing.Optional[Memory] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties of the AppRunner Service.

        :param source: (experimental) The source of the repository for the service.
        :param access_role: (experimental) The IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories). Default: - generate a new access role.
        :param cpu: (experimental) The number of CPU units reserved for each instance of your App Runner service. Default: Cpu.ONE_VCPU
        :param instance_role: (experimental) The IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any AWS APIs. Default: - no instance role attached.
        :param memory: (experimental) The amount of memory reserved for each instance of your App Runner service. Default: Memory.TWO_GB
        :param service_name: (experimental) Name of the service. Default: - auto-generated if undefined.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if access_role is not None:
            self._values["access_role"] = access_role
        if cpu is not None:
            self._values["cpu"] = cpu
        if instance_role is not None:
            self._values["instance_role"] = instance_role
        if memory is not None:
            self._values["memory"] = memory
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def source(self) -> "Source":
        '''(experimental) The source of the repository for the service.

        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("Source", result)

    @builtins.property
    def access_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role that grants the App Runner service access to a source repository.

        It's required for ECR image repositories (but not for ECR Public repositories).

        :default: - generate a new access role.

        :stability: experimental
        '''
        result = self._values.get("access_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def cpu(self) -> typing.Optional[Cpu]:
        '''(experimental) The number of CPU units reserved for each instance of your App Runner service.

        :default: Cpu.ONE_VCPU

        :stability: experimental
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[Cpu], result)

    @builtins.property
    def instance_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role that provides permissions to your App Runner service.

        These are permissions that your code needs when it calls any AWS APIs.

        :default: - no instance role attached.

        :stability: experimental
        '''
        result = self._values.get("instance_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def memory(self) -> typing.Optional[Memory]:
        '''(experimental) The amount of memory reserved for each instance of your App Runner service.

        :default: Memory.TWO_GB

        :stability: experimental
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[Memory], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the service.

        :default: - auto-generated if undefined.

        :stability: experimental
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Source(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-apprunner.Source",
):
    '''(experimental) Represents the App Runner service source.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset") # type: ignore[misc]
    @builtins.classmethod
    def from_asset(
        cls,
        *,
        asset: aws_cdk.aws_ecr_assets.DockerImageAsset,
        image_configuration: typing.Optional[ImageConfiguration] = None,
    ) -> "AssetSource":
        '''(experimental) Source from local assets.

        :param asset: (experimental) Represents the docker image asset.
        :param image_configuration: (experimental) The image configuration for the image built from the asset. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        props = AssetProps(asset=asset, image_configuration=image_configuration)

        return typing.cast("AssetSource", jsii.sinvoke(cls, "fromAsset", [props]))

    @jsii.member(jsii_name="fromEcr") # type: ignore[misc]
    @builtins.classmethod
    def from_ecr(
        cls,
        *,
        repository: aws_cdk.aws_ecr.IRepository,
        image_configuration: typing.Optional[ImageConfiguration] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> "EcrSource":
        '''(experimental) Source from the ECR repository.

        :param repository: (experimental) Represents the ECR repository.
        :param image_configuration: (experimental) The image configuration for the image from ECR. Default: - no image configuration will be passed. The default ``port`` will be 8080.
        :param tag: (experimental) Image tag. Default: - 'latest'

        :stability: experimental
        '''
        props = EcrProps(
            repository=repository, image_configuration=image_configuration, tag=tag
        )

        return typing.cast("EcrSource", jsii.sinvoke(cls, "fromEcr", [props]))

    @jsii.member(jsii_name="fromEcrPublic") # type: ignore[misc]
    @builtins.classmethod
    def from_ecr_public(
        cls,
        *,
        image_identifier: builtins.str,
        image_configuration: typing.Optional[ImageConfiguration] = None,
    ) -> "EcrPublicSource":
        '''(experimental) Source from the ECR Public repository.

        :param image_identifier: (experimental) The ECR Public image URI.
        :param image_configuration: (experimental) The image configuration for the image from ECR Public. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        props = EcrPublicProps(
            image_identifier=image_identifier, image_configuration=image_configuration
        )

        return typing.cast("EcrPublicSource", jsii.sinvoke(cls, "fromEcrPublic", [props]))

    @jsii.member(jsii_name="fromGitHub") # type: ignore[misc]
    @builtins.classmethod
    def from_git_hub(
        cls,
        *,
        configuration_source: ConfigurationSourceType,
        connection: GitHubConnection,
        repository_url: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        code_configuration_values: typing.Optional[CodeConfigurationValues] = None,
    ) -> "GithubSource":
        '''(experimental) Source from the GitHub repository.

        :param configuration_source: (experimental) The source of the App Runner configuration.
        :param connection: (experimental) ARN of the connection to Github. Only required for Github source.
        :param repository_url: (experimental) The location of the repository that contains the source code.
        :param branch: (experimental) The branch name that represents a specific version for the repository. Default: main
        :param code_configuration_values: (experimental) The code configuration values. Will be ignored if configurationSource is ``REPOSITORY``. Default: - no values will be passed. The ``apprunner.yaml`` from the github reopsitory will be used instead.

        :stability: experimental
        '''
        props = GithubRepositoryProps(
            configuration_source=configuration_source,
            connection=connection,
            repository_url=repository_url,
            branch=branch,
            code_configuration_values=code_configuration_values,
        )

        return typing.cast("GithubSource", jsii.sinvoke(cls, "fromGitHub", [props]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: constructs.Construct) -> "SourceConfig":
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param scope: -

        :stability: experimental
        '''
        ...


class _SourceProxy(Source):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct) -> "SourceConfig":
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param scope: -

        :stability: experimental
        '''
        return typing.cast("SourceConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Source).__jsii_proxy_class__ = lambda : _SourceProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.SourceCodeVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class SourceCodeVersion:
    def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
        '''(experimental) Identifies a version of code that AWS App Runner refers to within a source code repository.

        :param type: (experimental) The type of version identifier.
        :param value: (experimental) A source code version.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''(experimental) The type of version identifier.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''(experimental) A source code version.

        :stability: experimental
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceCodeVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-apprunner.SourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "code_repository": "codeRepository",
        "ecr_repository": "ecrRepository",
        "image_repository": "imageRepository",
    },
)
class SourceConfig:
    def __init__(
        self,
        *,
        code_repository: typing.Optional[CodeRepositoryProps] = None,
        ecr_repository: typing.Optional[aws_cdk.aws_ecr.IRepository] = None,
        image_repository: typing.Optional[ImageRepository] = None,
    ) -> None:
        '''(experimental) Result of binding ``Source`` into a ``Service``.

        :param code_repository: (experimental) The code repository configuration (mutually exclusive with ``imageRepository``). Default: - no code repository.
        :param ecr_repository: (experimental) The ECR repository (required to grant the pull privileges for the iam role). Default: - no ECR repository.
        :param image_repository: (experimental) The image repository configuration (mutually exclusive with ``codeRepository``). Default: - no image repository.

        :stability: experimental
        '''
        if isinstance(code_repository, dict):
            code_repository = CodeRepositoryProps(**code_repository)
        if isinstance(image_repository, dict):
            image_repository = ImageRepository(**image_repository)
        self._values: typing.Dict[str, typing.Any] = {}
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if ecr_repository is not None:
            self._values["ecr_repository"] = ecr_repository
        if image_repository is not None:
            self._values["image_repository"] = image_repository

    @builtins.property
    def code_repository(self) -> typing.Optional[CodeRepositoryProps]:
        '''(experimental) The code repository configuration (mutually exclusive  with ``imageRepository``).

        :default: - no code repository.

        :stability: experimental
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[CodeRepositoryProps], result)

    @builtins.property
    def ecr_repository(self) -> typing.Optional[aws_cdk.aws_ecr.IRepository]:
        '''(experimental) The ECR repository (required to grant the pull privileges for the iam role).

        :default: - no ECR repository.

        :stability: experimental
        '''
        result = self._values.get("ecr_repository")
        return typing.cast(typing.Optional[aws_cdk.aws_ecr.IRepository], result)

    @builtins.property
    def image_repository(self) -> typing.Optional[ImageRepository]:
        '''(experimental) The image repository configuration (mutually exclusive  with ``codeRepository``).

        :default: - no image repository.

        :stability: experimental
        '''
        result = self._values.get("image_repository")
        return typing.cast(typing.Optional[ImageRepository], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AssetSource(
    Source,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.AssetSource",
):
    '''(experimental) Represents the source from local assets.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        asset: aws_cdk.aws_ecr_assets.DockerImageAsset,
        image_configuration: typing.Optional[ImageConfiguration] = None,
    ) -> None:
        '''
        :param asset: (experimental) Represents the docker image asset.
        :param image_configuration: (experimental) The image configuration for the image built from the asset. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        props = AssetProps(asset=asset, image_configuration=image_configuration)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: constructs.Construct) -> SourceConfig:
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param _scope: -

        :stability: experimental
        '''
        return typing.cast(SourceConfig, jsii.invoke(self, "bind", [_scope]))


class EcrPublicSource(
    Source,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.EcrPublicSource",
):
    '''(experimental) Represents the service source from ECR Public.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        image_identifier: builtins.str,
        image_configuration: typing.Optional[ImageConfiguration] = None,
    ) -> None:
        '''
        :param image_identifier: (experimental) The ECR Public image URI.
        :param image_configuration: (experimental) The image configuration for the image from ECR Public. Default: - no image configuration will be passed. The default ``port`` will be 8080.

        :stability: experimental
        '''
        props = EcrPublicProps(
            image_identifier=image_identifier, image_configuration=image_configuration
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: constructs.Construct) -> SourceConfig:
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param _scope: -

        :stability: experimental
        '''
        return typing.cast(SourceConfig, jsii.invoke(self, "bind", [_scope]))


class EcrSource(
    Source,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.EcrSource",
):
    '''(experimental) Represents the service source from ECR.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        repository: aws_cdk.aws_ecr.IRepository,
        image_configuration: typing.Optional[ImageConfiguration] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repository: (experimental) Represents the ECR repository.
        :param image_configuration: (experimental) The image configuration for the image from ECR. Default: - no image configuration will be passed. The default ``port`` will be 8080.
        :param tag: (experimental) Image tag. Default: - 'latest'

        :stability: experimental
        '''
        props = EcrProps(
            repository=repository, image_configuration=image_configuration, tag=tag
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: constructs.Construct) -> SourceConfig:
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param _scope: -

        :stability: experimental
        '''
        return typing.cast(SourceConfig, jsii.invoke(self, "bind", [_scope]))


class GithubSource(
    Source,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-apprunner.GithubSource",
):
    '''(experimental) Represents the service source from a Github repository.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        configuration_source: ConfigurationSourceType,
        connection: GitHubConnection,
        repository_url: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        code_configuration_values: typing.Optional[CodeConfigurationValues] = None,
    ) -> None:
        '''
        :param configuration_source: (experimental) The source of the App Runner configuration.
        :param connection: (experimental) ARN of the connection to Github. Only required for Github source.
        :param repository_url: (experimental) The location of the repository that contains the source code.
        :param branch: (experimental) The branch name that represents a specific version for the repository. Default: main
        :param code_configuration_values: (experimental) The code configuration values. Will be ignored if configurationSource is ``REPOSITORY``. Default: - no values will be passed. The ``apprunner.yaml`` from the github reopsitory will be used instead.

        :stability: experimental
        '''
        props = GithubRepositoryProps(
            configuration_source=configuration_source,
            connection=connection,
            repository_url=repository_url,
            branch=branch,
            code_configuration_values=code_configuration_values,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: constructs.Construct) -> SourceConfig:
        '''(experimental) Called when the Job is initialized to allow this object to bind.

        :param _scope: -

        :stability: experimental
        '''
        return typing.cast(SourceConfig, jsii.invoke(self, "bind", [_scope]))


__all__ = [
    "AssetProps",
    "AssetSource",
    "CfnService",
    "CfnServiceProps",
    "CodeConfiguration",
    "CodeConfigurationValues",
    "CodeRepositoryProps",
    "ConfigurationSourceType",
    "Cpu",
    "EcrProps",
    "EcrPublicProps",
    "EcrPublicSource",
    "EcrSource",
    "GitHubConnection",
    "GithubRepositoryProps",
    "GithubSource",
    "IService",
    "ImageConfiguration",
    "ImageRepository",
    "ImageRepositoryType",
    "Memory",
    "Runtime",
    "Service",
    "ServiceAttributes",
    "ServiceProps",
    "Source",
    "SourceCodeVersion",
    "SourceConfig",
]

publication.publish()
