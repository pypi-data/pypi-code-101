'''
# logzio-autodeploymentlogzio-cloudwatch-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `logzio::autoDeploymentLogzio::CloudWatch::MODULE` v2.0.0.

## Description

Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name logzio::autoDeploymentLogzio::CloudWatch::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/logzio-autoDeploymentLogzio-CloudWatch-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `logzio::autoDeploymentLogzio::CloudWatch::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-autodeploymentlogzio-cloudwatch-module+v2.0.0).
* Issues related to `logzio::autoDeploymentLogzio::CloudWatch::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudWatchModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModule",
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
        parameters: typing.Optional["CfnCloudWatchModulePropsParameters"] = None,
        resources: typing.Optional["CfnCloudWatchModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``logzio::autoDeploymentLogzio::CloudWatch::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnCloudWatchModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudWatchModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudWatchModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCloudWatchModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnCloudWatchModulePropsParameters"] = None,
        resources: typing.Optional["CfnCloudWatchModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCloudWatchModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCloudWatchModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCloudWatchModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCloudWatchModulePropsParameters"]:
        '''
        :schema: CfnCloudWatchModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCloudWatchModulePropsResources"]:
        '''
        :schema: CfnCloudWatchModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParameters",
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
class CfnCloudWatchModulePropsParameters:
    def __init__(
        self,
        *,
        log_group: typing.Optional["CfnCloudWatchModulePropsParametersLogGroup"] = None,
        logzio_compress: typing.Optional["CfnCloudWatchModulePropsParametersLogzioCompress"] = None,
        logzio_enrich: typing.Optional["CfnCloudWatchModulePropsParametersLogzioEnrich"] = None,
        logzio_format: typing.Optional["CfnCloudWatchModulePropsParametersLogzioFormat"] = None,
        logzio_listener_url: typing.Optional["CfnCloudWatchModulePropsParametersLogzioListenerUrl"] = None,
        logzio_send_all: typing.Optional["CfnCloudWatchModulePropsParametersLogzioSendAll"] = None,
        logzio_token: typing.Optional["CfnCloudWatchModulePropsParametersLogzioToken"] = None,
        logzio_type: typing.Optional["CfnCloudWatchModulePropsParametersLogzioType"] = None,
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

        :schema: CfnCloudWatchModulePropsParameters
        '''
        if isinstance(log_group, dict):
            log_group = CfnCloudWatchModulePropsParametersLogGroup(**log_group)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnCloudWatchModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_enrich, dict):
            logzio_enrich = CfnCloudWatchModulePropsParametersLogzioEnrich(**logzio_enrich)
        if isinstance(logzio_format, dict):
            logzio_format = CfnCloudWatchModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_listener_url, dict):
            logzio_listener_url = CfnCloudWatchModulePropsParametersLogzioListenerUrl(**logzio_listener_url)
        if isinstance(logzio_send_all, dict):
            logzio_send_all = CfnCloudWatchModulePropsParametersLogzioSendAll(**logzio_send_all)
        if isinstance(logzio_token, dict):
            logzio_token = CfnCloudWatchModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnCloudWatchModulePropsParametersLogzioType(**logzio_type)
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
    def log_group(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogGroup"]:
        '''CloudWatch Log Group name from where you want to send logs.

        :schema: CfnCloudWatchModulePropsParameters#LogGroup
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogGroup"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnCloudWatchModulePropsParameters#LogzioCompress
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_enrich(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioEnrich"]:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :schema: CfnCloudWatchModulePropsParameters#LogzioEnrich
        '''
        result = self._values.get("logzio_enrich")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioEnrich"], result)

    @builtins.property
    def logzio_format(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioFormat"]:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnCloudWatchModulePropsParameters#LogzioFormat
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_listener_url(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioListenerUrl"]:
        '''The Logz.io listener URL fot your region.

        :schema: CfnCloudWatchModulePropsParameters#LogzioListenerUrl
        '''
        result = self._values.get("logzio_listener_url")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioListenerUrl"], result)

    @builtins.property
    def logzio_send_all(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioSendAll"]:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :schema: CfnCloudWatchModulePropsParameters#LogzioSendAll
        '''
        result = self._values.get("logzio_send_all")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioSendAll"], result)

    @builtins.property
    def logzio_token(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioToken"]:
        '''Logz.io account token.

        :schema: CfnCloudWatchModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnCloudWatchModulePropsParameters#LogzioType
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogGroup",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogGroup:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CloudWatch Log Group name from where you want to send logs.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogGroup#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioCompress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioCompress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioCompress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioCompress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioCompress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioCompress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioEnrich",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioEnrich:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioEnrich(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioFormat
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioListenerUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioListenerUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL fot your region.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioListenerUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioSendAll",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioSendAll:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioSendAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logz.io account token.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permission": "lambdaPermission",
        "logzio_cloudwatch_logs_lambda": "logzioCloudwatchLogsLambda",
        "logzio_subscription_filter": "logzioSubscriptionFilter",
    },
)
class CfnCloudWatchModulePropsResources:
    def __init__(
        self,
        *,
        lambda_iam_role: typing.Optional["CfnCloudWatchModulePropsResourcesLambdaIamRole"] = None,
        lambda_permission: typing.Optional["CfnCloudWatchModulePropsResourcesLambdaPermission"] = None,
        logzio_cloudwatch_logs_lambda: typing.Optional["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda"] = None,
        logzio_subscription_filter: typing.Optional["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter"] = None,
    ) -> None:
        '''
        :param lambda_iam_role: 
        :param lambda_permission: 
        :param logzio_cloudwatch_logs_lambda: 
        :param logzio_subscription_filter: 

        :schema: CfnCloudWatchModulePropsResources
        '''
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnCloudWatchModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnCloudWatchModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(logzio_cloudwatch_logs_lambda, dict):
            logzio_cloudwatch_logs_lambda = CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda(**logzio_cloudwatch_logs_lambda)
        if isinstance(logzio_subscription_filter, dict):
            logzio_subscription_filter = CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter(**logzio_subscription_filter)
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
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLambdaPermission"], result)

    @builtins.property
    def logzio_cloudwatch_logs_lambda(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LogzioCloudwatchLogsLambda
        '''
        result = self._values.get("logzio_cloudwatch_logs_lambda")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda"], result)

    @builtins.property
    def logzio_subscription_filter(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LogzioSubscriptionFilter
        '''
        result = self._values.get("logzio_subscription_filter")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudWatchModule",
    "CfnCloudWatchModuleProps",
    "CfnCloudWatchModulePropsParameters",
    "CfnCloudWatchModulePropsParametersLogGroup",
    "CfnCloudWatchModulePropsParametersLogzioCompress",
    "CfnCloudWatchModulePropsParametersLogzioEnrich",
    "CfnCloudWatchModulePropsParametersLogzioFormat",
    "CfnCloudWatchModulePropsParametersLogzioListenerUrl",
    "CfnCloudWatchModulePropsParametersLogzioSendAll",
    "CfnCloudWatchModulePropsParametersLogzioToken",
    "CfnCloudWatchModulePropsParametersLogzioType",
    "CfnCloudWatchModulePropsResources",
    "CfnCloudWatchModulePropsResourcesLambdaIamRole",
    "CfnCloudWatchModulePropsResourcesLambdaPermission",
    "CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda",
    "CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter",
]

publication.publish()
