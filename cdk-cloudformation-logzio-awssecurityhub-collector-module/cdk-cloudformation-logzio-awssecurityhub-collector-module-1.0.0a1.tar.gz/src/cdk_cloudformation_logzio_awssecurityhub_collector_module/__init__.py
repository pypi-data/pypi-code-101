'''
# AWS CDK CloudFormation Constructs for logzio::awsSecurityHub::collector::MODULE

Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE

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


class CfnModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModule",
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
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``logzio::awsSecurityHub::collector::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnModuleProps":
        '''Resource props.'''
        return typing.cast("CfnModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnModulePropsParameters"]:
        '''
        :schema: CfnModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnModulePropsResources"]:
        '''
        :schema: CfnModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_listener": "logzioListener",
        "logzio_log_level": "logzioLogLevel",
        "logzio_operations_token": "logzioOperationsToken",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        logzio_listener: typing.Optional["CfnModulePropsParametersLogzioListener"] = None,
        logzio_log_level: typing.Optional["CfnModulePropsParametersLogzioLogLevel"] = None,
        logzio_operations_token: typing.Optional["CfnModulePropsParametersLogzioOperationsToken"] = None,
    ) -> None:
        '''
        :param logzio_listener: Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.
        :param logzio_log_level: Log level for the function.
        :param logzio_operations_token: Your Logz.io operations token.

        :schema: CfnModulePropsParameters
        '''
        if isinstance(logzio_listener, dict):
            logzio_listener = CfnModulePropsParametersLogzioListener(**logzio_listener)
        if isinstance(logzio_log_level, dict):
            logzio_log_level = CfnModulePropsParametersLogzioLogLevel(**logzio_log_level)
        if isinstance(logzio_operations_token, dict):
            logzio_operations_token = CfnModulePropsParametersLogzioOperationsToken(**logzio_operations_token)
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
    ) -> typing.Optional["CfnModulePropsParametersLogzioListener"]:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :schema: CfnModulePropsParameters#logzioListener
        '''
        result = self._values.get("logzio_listener")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioListener"], result)

    @builtins.property
    def logzio_log_level(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioLogLevel"]:
        '''Log level for the function.

        :schema: CfnModulePropsParameters#logzioLogLevel
        '''
        result = self._values.get("logzio_log_level")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioLogLevel"], result)

    @builtins.property
    def logzio_operations_token(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioOperationsToken"]:
        '''Your Logz.io operations token.

        :schema: CfnModulePropsParameters#logzioOperationsToken
        '''
        result = self._values.get("logzio_operations_token")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioOperationsToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsParametersLogzioListener",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioListener:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioListener
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioListener#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioListener#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsParametersLogzioLogLevel",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioLogLevel:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Log level for the function.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioLogLevel
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioLogLevel#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioLogLevel#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioLogLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsParametersLogzioOperationsToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioOperationsToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io operations token.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioOperationsToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioOperationsToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioOperationsToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioOperationsToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "event_rule": "eventRule",
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permissions": "lambdaPermissions",
        "logzio_security_hub_collector": "logzioSecurityHubCollector",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        event_rule: typing.Optional["CfnModulePropsResourcesEventRule"] = None,
        lambda_iam_role: typing.Optional["CfnModulePropsResourcesLambdaIamRole"] = None,
        lambda_permissions: typing.Optional["CfnModulePropsResourcesLambdaPermissions"] = None,
        logzio_security_hub_collector: typing.Optional["CfnModulePropsResourcesLogzioSecurityHubCollector"] = None,
    ) -> None:
        '''
        :param event_rule: 
        :param lambda_iam_role: 
        :param lambda_permissions: 
        :param logzio_security_hub_collector: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(event_rule, dict):
            event_rule = CfnModulePropsResourcesEventRule(**event_rule)
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permissions, dict):
            lambda_permissions = CfnModulePropsResourcesLambdaPermissions(**lambda_permissions)
        if isinstance(logzio_security_hub_collector, dict):
            logzio_security_hub_collector = CfnModulePropsResourcesLogzioSecurityHubCollector(**logzio_security_hub_collector)
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
    def event_rule(self) -> typing.Optional["CfnModulePropsResourcesEventRule"]:
        '''
        :schema: CfnModulePropsResources#eventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEventRule"], result)

    @builtins.property
    def lambda_iam_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permissions(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLambdaPermissions"]:
        '''
        :schema: CfnModulePropsResources#lambdaPermissions
        '''
        result = self._values.get("lambda_permissions")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLambdaPermissions"], result)

    @builtins.property
    def logzio_security_hub_collector(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioSecurityHubCollector"]:
        '''
        :schema: CfnModulePropsResources#logzioSecurityHubCollector
        '''
        result = self._values.get("logzio_security_hub_collector")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioSecurityHubCollector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesEventRule
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLambdaIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsResourcesLambdaPermissions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLambdaPermissions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLambdaPermissions
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLambdaPermissions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLambdaPermissions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLambdaPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnModulePropsResourcesLogzioSecurityHubCollector",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioSecurityHubCollector:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioSecurityHubCollector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioSecurityHubCollector#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioSecurityHubCollector#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioSecurityHubCollector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersLogzioListener",
    "CfnModulePropsParametersLogzioLogLevel",
    "CfnModulePropsParametersLogzioOperationsToken",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesEventRule",
    "CfnModulePropsResourcesLambdaIamRole",
    "CfnModulePropsResourcesLambdaPermissions",
    "CfnModulePropsResourcesLogzioSecurityHubCollector",
]

publication.publish()
