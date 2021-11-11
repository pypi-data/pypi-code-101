'''
# logzio-awssecurityhub-collector-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `logzio::awsSecurityHub::collector::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name logzio::awsSecurityHub::collector::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/logzio-awsSecurityHub-collector-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `logzio::awsSecurityHub::collector::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-awssecurityhub-collector-module+v1.0.0).
* Issues related to `logzio::awsSecurityHub::collector::MODULE` should be reported to the [publisher](undefined).

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


class CfnCollectorModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModule",
):
    '''A CloudFormation ``logzio::awsSecurityHub::collector::MODULE``.

    :cloudformationResource: logzio::awsSecurityHub::collector::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnCollectorModulePropsParameters"] = None,
        resources: typing.Optional["CfnCollectorModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``logzio::awsSecurityHub::collector::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnCollectorModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCollectorModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCollectorModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCollectorModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnCollectorModulePropsParameters"] = None,
        resources: typing.Optional["CfnCollectorModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCollectorModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCollectorModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCollectorModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCollectorModulePropsParameters"]:
        '''
        :schema: CfnCollectorModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCollectorModulePropsResources"]:
        '''
        :schema: CfnCollectorModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_listener": "logzioListener",
        "logzio_log_level": "logzioLogLevel",
        "logzio_operations_token": "logzioOperationsToken",
    },
)
class CfnCollectorModulePropsParameters:
    def __init__(
        self,
        *,
        logzio_listener: typing.Optional["CfnCollectorModulePropsParametersLogzioListener"] = None,
        logzio_log_level: typing.Optional["CfnCollectorModulePropsParametersLogzioLogLevel"] = None,
        logzio_operations_token: typing.Optional["CfnCollectorModulePropsParametersLogzioOperationsToken"] = None,
    ) -> None:
        '''
        :param logzio_listener: Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.
        :param logzio_log_level: Log level for the function.
        :param logzio_operations_token: Your Logz.io operations token.

        :schema: CfnCollectorModulePropsParameters
        '''
        if isinstance(logzio_listener, dict):
            logzio_listener = CfnCollectorModulePropsParametersLogzioListener(**logzio_listener)
        if isinstance(logzio_log_level, dict):
            logzio_log_level = CfnCollectorModulePropsParametersLogzioLogLevel(**logzio_log_level)
        if isinstance(logzio_operations_token, dict):
            logzio_operations_token = CfnCollectorModulePropsParametersLogzioOperationsToken(**logzio_operations_token)
        self._values: typing.Dict[str, typing.Any] = {}
        if logzio_listener is not None:
            self._values["logzio_listener"] = logzio_listener
        if logzio_log_level is not None:
            self._values["logzio_log_level"] = logzio_log_level
        if logzio_operations_token is not None:
            self._values["logzio_operations_token"] = logzio_operations_token

    @builtins.property
    def logzio_listener(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioListener"]:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :schema: CfnCollectorModulePropsParameters#logzioListener
        '''
        result = self._values.get("logzio_listener")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioListener"], result)

    @builtins.property
    def logzio_log_level(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioLogLevel"]:
        '''Log level for the function.

        :schema: CfnCollectorModulePropsParameters#logzioLogLevel
        '''
        result = self._values.get("logzio_log_level")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioLogLevel"], result)

    @builtins.property
    def logzio_operations_token(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioOperationsToken"]:
        '''Your Logz.io operations token.

        :schema: CfnCollectorModulePropsParameters#logzioOperationsToken
        '''
        result = self._values.get("logzio_operations_token")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioOperationsToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioListener",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioListener:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioListener
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioListener#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioListener#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioLogLevel",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioLogLevel:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Log level for the function.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioLogLevel
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioLogLevel#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioLogLevel#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioLogLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioOperationsToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioOperationsToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io operations token.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioOperationsToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "event_rule": "eventRule",
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permissions": "lambdaPermissions",
        "logzio_security_hub_collector": "logzioSecurityHubCollector",
    },
)
class CfnCollectorModulePropsResources:
    def __init__(
        self,
        *,
        event_rule: typing.Optional["CfnCollectorModulePropsResourcesEventRule"] = None,
        lambda_iam_role: typing.Optional["CfnCollectorModulePropsResourcesLambdaIamRole"] = None,
        lambda_permissions: typing.Optional["CfnCollectorModulePropsResourcesLambdaPermissions"] = None,
        logzio_security_hub_collector: typing.Optional["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector"] = None,
    ) -> None:
        '''
        :param event_rule: 
        :param lambda_iam_role: 
        :param lambda_permissions: 
        :param logzio_security_hub_collector: 

        :schema: CfnCollectorModulePropsResources
        '''
        if isinstance(event_rule, dict):
            event_rule = CfnCollectorModulePropsResourcesEventRule(**event_rule)
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnCollectorModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permissions, dict):
            lambda_permissions = CfnCollectorModulePropsResourcesLambdaPermissions(**lambda_permissions)
        if isinstance(logzio_security_hub_collector, dict):
            logzio_security_hub_collector = CfnCollectorModulePropsResourcesLogzioSecurityHubCollector(**logzio_security_hub_collector)
        self._values: typing.Dict[str, typing.Any] = {}
        if event_rule is not None:
            self._values["event_rule"] = event_rule
        if lambda_iam_role is not None:
            self._values["lambda_iam_role"] = lambda_iam_role
        if lambda_permissions is not None:
            self._values["lambda_permissions"] = lambda_permissions
        if logzio_security_hub_collector is not None:
            self._values["logzio_security_hub_collector"] = logzio_security_hub_collector

    @builtins.property
    def event_rule(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesEventRule"]:
        '''
        :schema: CfnCollectorModulePropsResources#eventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesEventRule"], result)

    @builtins.property
    def lambda_iam_role(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnCollectorModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permissions(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLambdaPermissions"]:
        '''
        :schema: CfnCollectorModulePropsResources#lambdaPermissions
        '''
        result = self._values.get("lambda_permissions")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLambdaPermissions"], result)

    @builtins.property
    def logzio_security_hub_collector(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector"]:
        '''
        :schema: CfnCollectorModulePropsResources#logzioSecurityHubCollector
        '''
        result = self._values.get("logzio_security_hub_collector")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesEventRule
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCollectorModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLambdaIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLambdaPermissions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLambdaPermissions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLambdaPermissions
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaPermissions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaPermissions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLambdaPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLogzioSecurityHubCollector",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLogzioSecurityHubCollector:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLogzioSecurityHubCollector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCollectorModule",
    "CfnCollectorModuleProps",
    "CfnCollectorModulePropsParameters",
    "CfnCollectorModulePropsParametersLogzioListener",
    "CfnCollectorModulePropsParametersLogzioLogLevel",
    "CfnCollectorModulePropsParametersLogzioOperationsToken",
    "CfnCollectorModulePropsResources",
    "CfnCollectorModulePropsResourcesEventRule",
    "CfnCollectorModulePropsResourcesLambdaIamRole",
    "CfnCollectorModulePropsResourcesLambdaPermissions",
    "CfnCollectorModulePropsResourcesLogzioSecurityHubCollector",
]

publication.publish()
