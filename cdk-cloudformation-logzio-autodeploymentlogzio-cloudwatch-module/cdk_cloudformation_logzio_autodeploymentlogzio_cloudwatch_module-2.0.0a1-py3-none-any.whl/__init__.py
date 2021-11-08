'''
# AWS CDK CloudFormation Constructs for logzio::autoDeploymentLogzio::CloudWatch::MODULE

Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE

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
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModule",
):
    '''A CloudFormation ``logzio::autoDeploymentLogzio::CloudWatch::MODULE``.

    :cloudformationResource: logzio::autoDeploymentLogzio::CloudWatch::MODULE
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
        '''Create a new ``logzio::autoDeploymentLogzio::CloudWatch::MODULE``.

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
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE.

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
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "log_group": "logGroup",
        "logzio_compress": "logzioCompress",
        "logzio_enrich": "logzioEnrich",
        "logzio_format": "logzioFormat",
        "logzio_listener_url": "logzioListenerUrl",
        "logzio_send_all": "logzioSendAll",
        "logzio_token": "logzioToken",
        "logzio_type": "logzioType",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        log_group: typing.Optional["CfnModulePropsParametersLogGroup"] = None,
        logzio_compress: typing.Optional["CfnModulePropsParametersLogzioCompress"] = None,
        logzio_enrich: typing.Optional["CfnModulePropsParametersLogzioEnrich"] = None,
        logzio_format: typing.Optional["CfnModulePropsParametersLogzioFormat"] = None,
        logzio_listener_url: typing.Optional["CfnModulePropsParametersLogzioListenerUrl"] = None,
        logzio_send_all: typing.Optional["CfnModulePropsParametersLogzioSendAll"] = None,
        logzio_token: typing.Optional["CfnModulePropsParametersLogzioToken"] = None,
        logzio_type: typing.Optional["CfnModulePropsParametersLogzioType"] = None,
    ) -> None:
        '''
        :param log_group: CloudWatch Log Group name from where you want to send logs.
        :param logzio_compress: If true, the Lambda will send compressed logs. If false, the Lambda will send uncompressed logs.
        :param logzio_enrich: Enriches the CloudWatch events with custom properties at ship time. The format is ``key1=value1;key2=value2``. By default is empty.
        :param logzio_format: JSON or text. If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.
        :param logzio_listener_url: The Logz.io listener URL fot your region.
        :param logzio_send_all: By default, we do not send logs of type START, END, REPORT. Choose true to send all log types.
        :param logzio_token: Logz.io account token.
        :param logzio_type: The log type you'll use with this Lambda. Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnModulePropsParameters
        '''
        if isinstance(log_group, dict):
            log_group = CfnModulePropsParametersLogGroup(**log_group)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_enrich, dict):
            logzio_enrich = CfnModulePropsParametersLogzioEnrich(**logzio_enrich)
        if isinstance(logzio_format, dict):
            logzio_format = CfnModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_listener_url, dict):
            logzio_listener_url = CfnModulePropsParametersLogzioListenerUrl(**logzio_listener_url)
        if isinstance(logzio_send_all, dict):
            logzio_send_all = CfnModulePropsParametersLogzioSendAll(**logzio_send_all)
        if isinstance(logzio_token, dict):
            logzio_token = CfnModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnModulePropsParametersLogzioType(**logzio_type)
        self._values: typing.Dict[str, typing.Any] = {}
        if log_group is not None:
            self._values["log_group"] = log_group
        if logzio_compress is not None:
            self._values["logzio_compress"] = logzio_compress
        if logzio_enrich is not None:
            self._values["logzio_enrich"] = logzio_enrich
        if logzio_format is not None:
            self._values["logzio_format"] = logzio_format
        if logzio_listener_url is not None:
            self._values["logzio_listener_url"] = logzio_listener_url
        if logzio_send_all is not None:
            self._values["logzio_send_all"] = logzio_send_all
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_type is not None:
            self._values["logzio_type"] = logzio_type

    @builtins.property
    def log_group(self) -> typing.Optional["CfnModulePropsParametersLogGroup"]:
        '''CloudWatch Log Group name from where you want to send logs.

        :schema: CfnModulePropsParameters#LogGroup
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogGroup"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnModulePropsParameters#LogzioCompress
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_enrich(self) -> typing.Optional["CfnModulePropsParametersLogzioEnrich"]:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :schema: CfnModulePropsParameters#LogzioEnrich
        '''
        result = self._values.get("logzio_enrich")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioEnrich"], result)

    @builtins.property
    def logzio_format(self) -> typing.Optional["CfnModulePropsParametersLogzioFormat"]:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnModulePropsParameters#LogzioFormat
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_listener_url(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioListenerUrl"]:
        '''The Logz.io listener URL fot your region.

        :schema: CfnModulePropsParameters#LogzioListenerUrl
        '''
        result = self._values.get("logzio_listener_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioListenerUrl"], result)

    @builtins.property
    def logzio_send_all(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioSendAll"]:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :schema: CfnModulePropsParameters#LogzioSendAll
        '''
        result = self._values.get("logzio_send_all")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioSendAll"], result)

    @builtins.property
    def logzio_token(self) -> typing.Optional["CfnModulePropsParametersLogzioToken"]:
        '''Logz.io account token.

        :schema: CfnModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(self) -> typing.Optional["CfnModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnModulePropsParameters#LogzioType
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogGroup",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogGroup:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CloudWatch Log Group name from where you want to send logs.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogGroup#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioCompress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioCompress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioCompress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioCompress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioCompress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioCompress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioEnrich",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioEnrich:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioEnrich
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioEnrich#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioEnrich#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioEnrich(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioFormat
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioListenerUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioListenerUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL fot your region.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioListenerUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioListenerUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioListenerUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioListenerUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioSendAll",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioSendAll:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioSendAll
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioSendAll#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioSendAll#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioSendAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logz.io account token.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsParametersLogzioType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permission": "lambdaPermission",
        "logzio_cloudwatch_logs_lambda": "logzioCloudwatchLogsLambda",
        "logzio_subscription_filter": "logzioSubscriptionFilter",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        lambda_iam_role: typing.Optional["CfnModulePropsResourcesLambdaIamRole"] = None,
        lambda_permission: typing.Optional["CfnModulePropsResourcesLambdaPermission"] = None,
        logzio_cloudwatch_logs_lambda: typing.Optional["CfnModulePropsResourcesLogzioCloudwatchLogsLambda"] = None,
        logzio_subscription_filter: typing.Optional["CfnModulePropsResourcesLogzioSubscriptionFilter"] = None,
    ) -> None:
        '''
        :param lambda_iam_role: 
        :param lambda_permission: 
        :param logzio_cloudwatch_logs_lambda: 
        :param logzio_subscription_filter: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(logzio_cloudwatch_logs_lambda, dict):
            logzio_cloudwatch_logs_lambda = CfnModulePropsResourcesLogzioCloudwatchLogsLambda(**logzio_cloudwatch_logs_lambda)
        if isinstance(logzio_subscription_filter, dict):
            logzio_subscription_filter = CfnModulePropsResourcesLogzioSubscriptionFilter(**logzio_subscription_filter)
        self._values: typing.Dict[str, typing.Any] = {}
        if lambda_iam_role is not None:
            self._values["lambda_iam_role"] = lambda_iam_role
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission
        if logzio_cloudwatch_logs_lambda is not None:
            self._values["logzio_cloudwatch_logs_lambda"] = logzio_cloudwatch_logs_lambda
        if logzio_subscription_filter is not None:
            self._values["logzio_subscription_filter"] = logzio_subscription_filter

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
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLambdaPermission"], result)

    @builtins.property
    def logzio_cloudwatch_logs_lambda(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioCloudwatchLogsLambda"]:
        '''
        :schema: CfnModulePropsResources#LogzioCloudwatchLogsLambda
        '''
        result = self._values.get("logzio_cloudwatch_logs_lambda")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioCloudwatchLogsLambda"], result)

    @builtins.property
    def logzio_subscription_filter(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioSubscriptionFilter"]:
        '''
        :schema: CfnModulePropsResources#LogzioSubscriptionFilter
        '''
        result = self._values.get("logzio_subscription_filter")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioSubscriptionFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsResourcesLambdaIamRole",
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
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLambdaPermission
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsResourcesLogzioCloudwatchLogsLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioCloudwatchLogsLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioCloudwatchLogsLambda
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioCloudwatchLogsLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioCloudwatchLogsLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioCloudwatchLogsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnModulePropsResourcesLogzioSubscriptionFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioSubscriptionFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioSubscriptionFilter
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioSubscriptionFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioSubscriptionFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioSubscriptionFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersLogGroup",
    "CfnModulePropsParametersLogzioCompress",
    "CfnModulePropsParametersLogzioEnrich",
    "CfnModulePropsParametersLogzioFormat",
    "CfnModulePropsParametersLogzioListenerUrl",
    "CfnModulePropsParametersLogzioSendAll",
    "CfnModulePropsParametersLogzioToken",
    "CfnModulePropsParametersLogzioType",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesLambdaIamRole",
    "CfnModulePropsResourcesLambdaPermission",
    "CfnModulePropsResourcesLogzioCloudwatchLogsLambda",
    "CfnModulePropsResourcesLogzioSubscriptionFilter",
]

publication.publish()
