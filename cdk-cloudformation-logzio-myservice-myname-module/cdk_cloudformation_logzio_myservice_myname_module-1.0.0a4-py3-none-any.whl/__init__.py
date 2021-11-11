'''
# logzio-myservice-myname-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Logzio::MyService::MyName::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Logzio::MyService::MyName::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Logzio::MyService::MyName::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/Logzio-MyService-MyName-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Logzio::MyService::MyName::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-myservice-myname-module+v1.0.0).
* Issues related to `Logzio::MyService::MyName::MODULE` should be reported to the [publisher](undefined).

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


class CfnMyNameModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModule",
):
    '''A CloudFormation ``Logzio::MyService::MyName::MODULE``.

    :cloudformationResource: Logzio::MyService::MyName::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnMyNameModulePropsParameters"] = None,
        resources: typing.Optional["CfnMyNameModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Logzio::MyService::MyName::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnMyNameModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMyNameModuleProps":
        '''Resource props.'''
        return typing.cast("CfnMyNameModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnMyNameModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnMyNameModulePropsParameters"] = None,
        resources: typing.Optional["CfnMyNameModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Logzio::MyService::MyName::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnMyNameModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnMyNameModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnMyNameModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnMyNameModulePropsParameters"]:
        '''
        :schema: CfnMyNameModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnMyNameModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnMyNameModulePropsResources"]:
        '''
        :schema: CfnMyNameModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnMyNameModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_listener": "logzioListener",
        "logzio_log_level": "logzioLogLevel",
        "logzio_operations_token": "logzioOperationsToken",
    },
)
class CfnMyNameModulePropsParameters:
    def __init__(
        self,
        *,
        logzio_listener: typing.Optional["CfnMyNameModulePropsParametersLogzioListener"] = None,
        logzio_log_level: typing.Optional["CfnMyNameModulePropsParametersLogzioLogLevel"] = None,
        logzio_operations_token: typing.Optional["CfnMyNameModulePropsParametersLogzioOperationsToken"] = None,
    ) -> None:
        '''
        :param logzio_listener: Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.
        :param logzio_log_level: Log level for the function.
        :param logzio_operations_token: Your Logz.io operations token.

        :schema: CfnMyNameModulePropsParameters
        '''
        if isinstance(logzio_listener, dict):
            logzio_listener = CfnMyNameModulePropsParametersLogzioListener(**logzio_listener)
        if isinstance(logzio_log_level, dict):
            logzio_log_level = CfnMyNameModulePropsParametersLogzioLogLevel(**logzio_log_level)
        if isinstance(logzio_operations_token, dict):
            logzio_operations_token = CfnMyNameModulePropsParametersLogzioOperationsToken(**logzio_operations_token)
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
    ) -> typing.Optional["CfnMyNameModulePropsParametersLogzioListener"]:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :schema: CfnMyNameModulePropsParameters#logzioListener
        '''
        result = self._values.get("logzio_listener")
        return typing.cast(typing.Optional["CfnMyNameModulePropsParametersLogzioListener"], result)

    @builtins.property
    def logzio_log_level(
        self,
    ) -> typing.Optional["CfnMyNameModulePropsParametersLogzioLogLevel"]:
        '''Log level for the function.

        :schema: CfnMyNameModulePropsParameters#logzioLogLevel
        '''
        result = self._values.get("logzio_log_level")
        return typing.cast(typing.Optional["CfnMyNameModulePropsParametersLogzioLogLevel"], result)

    @builtins.property
    def logzio_operations_token(
        self,
    ) -> typing.Optional["CfnMyNameModulePropsParametersLogzioOperationsToken"]:
        '''Your Logz.io operations token.

        :schema: CfnMyNameModulePropsParameters#logzioOperationsToken
        '''
        result = self._values.get("logzio_operations_token")
        return typing.cast(typing.Optional["CfnMyNameModulePropsParametersLogzioOperationsToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsParametersLogzioListener",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMyNameModulePropsParametersLogzioListener:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :param description: 
        :param type: 

        :schema: CfnMyNameModulePropsParametersLogzioListener
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioListener#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioListener#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsParametersLogzioListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsParametersLogzioLogLevel",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMyNameModulePropsParametersLogzioLogLevel:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Log level for the function.

        :param description: 
        :param type: 

        :schema: CfnMyNameModulePropsParametersLogzioLogLevel
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioLogLevel#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioLogLevel#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsParametersLogzioLogLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsParametersLogzioOperationsToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMyNameModulePropsParametersLogzioOperationsToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io operations token.

        :param description: 
        :param type: 

        :schema: CfnMyNameModulePropsParametersLogzioOperationsToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioOperationsToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMyNameModulePropsParametersLogzioOperationsToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsParametersLogzioOperationsToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "event_rule": "eventRule",
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permissions": "lambdaPermissions",
        "logzio_security_hub_collector": "logzioSecurityHubCollector",
    },
)
class CfnMyNameModulePropsResources:
    def __init__(
        self,
        *,
        event_rule: typing.Optional["CfnMyNameModulePropsResourcesEventRule"] = None,
        lambda_iam_role: typing.Optional["CfnMyNameModulePropsResourcesLambdaIamRole"] = None,
        lambda_permissions: typing.Optional["CfnMyNameModulePropsResourcesLambdaPermissions"] = None,
        logzio_security_hub_collector: typing.Optional["CfnMyNameModulePropsResourcesLogzioSecurityHubCollector"] = None,
    ) -> None:
        '''
        :param event_rule: 
        :param lambda_iam_role: 
        :param lambda_permissions: 
        :param logzio_security_hub_collector: 

        :schema: CfnMyNameModulePropsResources
        '''
        if isinstance(event_rule, dict):
            event_rule = CfnMyNameModulePropsResourcesEventRule(**event_rule)
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnMyNameModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permissions, dict):
            lambda_permissions = CfnMyNameModulePropsResourcesLambdaPermissions(**lambda_permissions)
        if isinstance(logzio_security_hub_collector, dict):
            logzio_security_hub_collector = CfnMyNameModulePropsResourcesLogzioSecurityHubCollector(**logzio_security_hub_collector)
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
    def event_rule(self) -> typing.Optional["CfnMyNameModulePropsResourcesEventRule"]:
        '''
        :schema: CfnMyNameModulePropsResources#eventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnMyNameModulePropsResourcesEventRule"], result)

    @builtins.property
    def lambda_iam_role(
        self,
    ) -> typing.Optional["CfnMyNameModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnMyNameModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnMyNameModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permissions(
        self,
    ) -> typing.Optional["CfnMyNameModulePropsResourcesLambdaPermissions"]:
        '''
        :schema: CfnMyNameModulePropsResources#lambdaPermissions
        '''
        result = self._values.get("lambda_permissions")
        return typing.cast(typing.Optional["CfnMyNameModulePropsResourcesLambdaPermissions"], result)

    @builtins.property
    def logzio_security_hub_collector(
        self,
    ) -> typing.Optional["CfnMyNameModulePropsResourcesLogzioSecurityHubCollector"]:
        '''
        :schema: CfnMyNameModulePropsResources#logzioSecurityHubCollector
        '''
        result = self._values.get("logzio_security_hub_collector")
        return typing.cast(typing.Optional["CfnMyNameModulePropsResourcesLogzioSecurityHubCollector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMyNameModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMyNameModulePropsResourcesEventRule
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMyNameModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMyNameModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMyNameModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMyNameModulePropsResourcesLambdaIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMyNameModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMyNameModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsResourcesLambdaPermissions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMyNameModulePropsResourcesLambdaPermissions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMyNameModulePropsResourcesLambdaPermissions
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMyNameModulePropsResourcesLambdaPermissions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMyNameModulePropsResourcesLambdaPermissions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsResourcesLambdaPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-myservice-myname-module.CfnMyNameModulePropsResourcesLogzioSecurityHubCollector",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMyNameModulePropsResourcesLogzioSecurityHubCollector:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMyNameModulePropsResourcesLogzioSecurityHubCollector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMyNameModulePropsResourcesLogzioSecurityHubCollector#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMyNameModulePropsResourcesLogzioSecurityHubCollector#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMyNameModulePropsResourcesLogzioSecurityHubCollector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMyNameModule",
    "CfnMyNameModuleProps",
    "CfnMyNameModulePropsParameters",
    "CfnMyNameModulePropsParametersLogzioListener",
    "CfnMyNameModulePropsParametersLogzioLogLevel",
    "CfnMyNameModulePropsParametersLogzioOperationsToken",
    "CfnMyNameModulePropsResources",
    "CfnMyNameModulePropsResourcesEventRule",
    "CfnMyNameModulePropsResourcesLambdaIamRole",
    "CfnMyNameModulePropsResourcesLambdaPermissions",
    "CfnMyNameModulePropsResourcesLogzioSecurityHubCollector",
]

publication.publish()
