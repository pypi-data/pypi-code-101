'''
# AWS CDK CloudFormation Constructs for Logzio::KinesisShipper::KinesisShipper::MODULE

Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE

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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModule",
):
    '''A CloudFormation ``Logzio::KinesisShipper::KinesisShipper::MODULE``.

    :cloudformationResource: Logzio::KinesisShipper::KinesisShipper::MODULE
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
        '''Create a new ``Logzio::KinesisShipper::KinesisShipper::MODULE``.

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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE.

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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "kinesis_stream": "kinesisStream",
        "kinesis_stream_batch_size": "kinesisStreamBatchSize",
        "kinesis_stream_starting_position": "kinesisStreamStartingPosition",
        "logzio_compress": "logzioCompress",
        "logzio_format": "logzioFormat",
        "logzio_messages_array": "logzioMessagesArray",
        "logzio_region": "logzioRegion",
        "logzio_token": "logzioToken",
        "logzio_type": "logzioType",
        "logzio_url": "logzioUrl",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        kinesis_stream: typing.Optional["CfnModulePropsParametersKinesisStream"] = None,
        kinesis_stream_batch_size: typing.Optional["CfnModulePropsParametersKinesisStreamBatchSize"] = None,
        kinesis_stream_starting_position: typing.Optional["CfnModulePropsParametersKinesisStreamStartingPosition"] = None,
        logzio_compress: typing.Optional["CfnModulePropsParametersLogzioCompress"] = None,
        logzio_format: typing.Optional["CfnModulePropsParametersLogzioFormat"] = None,
        logzio_messages_array: typing.Optional["CfnModulePropsParametersLogzioMessagesArray"] = None,
        logzio_region: typing.Optional["CfnModulePropsParametersLogzioRegion"] = None,
        logzio_token: typing.Optional["CfnModulePropsParametersLogzioToken"] = None,
        logzio_type: typing.Optional["CfnModulePropsParametersLogzioType"] = None,
        logzio_url: typing.Optional["CfnModulePropsParametersLogzioUrl"] = None,
    ) -> None:
        '''
        :param kinesis_stream: Enter a Kinesis stream to listen for updates on.
        :param kinesis_stream_batch_size: The largest number of records that will be read from your stream at once.
        :param kinesis_stream_starting_position: The position in the stream to start reading from. For more information, see ShardIteratorType in the Amazon Kinesis API Reference.
        :param logzio_compress: If true, the Lambda will send compressed logs. If false, the Lambda will send uncompressed logs.
        :param logzio_format: json or text. If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.
        :param logzio_messages_array: Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages. For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.
        :param logzio_region: Two-letter region code, or blank for US East (Northern Virginia). This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table
        :param logzio_token: The token of the account you want to ship to. Can be found at https://app.logz.io/#/dashboard/settings/general
        :param logzio_type: The log type you'll use with this Lambda. Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type
        :param logzio_url: Deprecated. Use LogzioREGION instead

        :schema: CfnModulePropsParameters
        '''
        if isinstance(kinesis_stream, dict):
            kinesis_stream = CfnModulePropsParametersKinesisStream(**kinesis_stream)
        if isinstance(kinesis_stream_batch_size, dict):
            kinesis_stream_batch_size = CfnModulePropsParametersKinesisStreamBatchSize(**kinesis_stream_batch_size)
        if isinstance(kinesis_stream_starting_position, dict):
            kinesis_stream_starting_position = CfnModulePropsParametersKinesisStreamStartingPosition(**kinesis_stream_starting_position)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_format, dict):
            logzio_format = CfnModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_messages_array, dict):
            logzio_messages_array = CfnModulePropsParametersLogzioMessagesArray(**logzio_messages_array)
        if isinstance(logzio_region, dict):
            logzio_region = CfnModulePropsParametersLogzioRegion(**logzio_region)
        if isinstance(logzio_token, dict):
            logzio_token = CfnModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnModulePropsParametersLogzioType(**logzio_type)
        if isinstance(logzio_url, dict):
            logzio_url = CfnModulePropsParametersLogzioUrl(**logzio_url)
        self._values: typing.Dict[str, typing.Any] = {}
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if kinesis_stream_batch_size is not None:
            self._values["kinesis_stream_batch_size"] = kinesis_stream_batch_size
        if kinesis_stream_starting_position is not None:
            self._values["kinesis_stream_starting_position"] = kinesis_stream_starting_position
        if logzio_compress is not None:
            self._values["logzio_compress"] = logzio_compress
        if logzio_format is not None:
            self._values["logzio_format"] = logzio_format
        if logzio_messages_array is not None:
            self._values["logzio_messages_array"] = logzio_messages_array
        if logzio_region is not None:
            self._values["logzio_region"] = logzio_region
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_type is not None:
            self._values["logzio_type"] = logzio_type
        if logzio_url is not None:
            self._values["logzio_url"] = logzio_url

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["CfnModulePropsParametersKinesisStream"]:
        '''Enter a Kinesis stream to listen for updates on.

        :schema: CfnModulePropsParameters#KinesisStream
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["CfnModulePropsParametersKinesisStream"], result)

    @builtins.property
    def kinesis_stream_batch_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersKinesisStreamBatchSize"]:
        '''The largest number of records that will be read from your stream at once.

        :schema: CfnModulePropsParameters#KinesisStreamBatchSize
        '''
        result = self._values.get("kinesis_stream_batch_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersKinesisStreamBatchSize"], result)

    @builtins.property
    def kinesis_stream_starting_position(
        self,
    ) -> typing.Optional["CfnModulePropsParametersKinesisStreamStartingPosition"]:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :schema: CfnModulePropsParameters#KinesisStreamStartingPosition
        '''
        result = self._values.get("kinesis_stream_starting_position")
        return typing.cast(typing.Optional["CfnModulePropsParametersKinesisStreamStartingPosition"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnModulePropsParameters#LogzioCOMPRESS
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_format(self) -> typing.Optional["CfnModulePropsParametersLogzioFormat"]:
        '''json or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnModulePropsParameters#LogzioFORMAT
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_messages_array(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLogzioMessagesArray"]:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :schema: CfnModulePropsParameters#LogzioMessagesArray
        '''
        result = self._values.get("logzio_messages_array")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioMessagesArray"], result)

    @builtins.property
    def logzio_region(self) -> typing.Optional["CfnModulePropsParametersLogzioRegion"]:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :schema: CfnModulePropsParameters#LogzioREGION
        '''
        result = self._values.get("logzio_region")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioRegion"], result)

    @builtins.property
    def logzio_token(self) -> typing.Optional["CfnModulePropsParametersLogzioToken"]:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

        :schema: CfnModulePropsParameters#LogzioTOKEN
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(self) -> typing.Optional["CfnModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnModulePropsParameters#LogzioTYPE
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioType"], result)

    @builtins.property
    def logzio_url(self) -> typing.Optional["CfnModulePropsParametersLogzioUrl"]:
        '''Deprecated.

        Use LogzioREGION instead

        :schema: CfnModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKinesisStream:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enter a Kinesis stream to listen for updates on.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersKinesisStream
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStream#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStream#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersKinesisStreamBatchSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKinesisStreamBatchSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The largest number of records that will be read from your stream at once.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersKinesisStreamBatchSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStreamBatchSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStreamBatchSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKinesisStreamBatchSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersKinesisStreamStartingPosition",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKinesisStreamStartingPosition:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersKinesisStreamStartingPosition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStreamStartingPosition#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKinesisStreamStartingPosition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKinesisStreamStartingPosition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioCompress",
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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''json or text.

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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioMessagesArray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioMessagesArray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioMessagesArray
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioMessagesArray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioMessagesArray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioMessagesArray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioRegion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioType",
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
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Deprecated.

        Use LogzioREGION instead

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogzioUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogzioUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogzioUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_kinesis_lambda": "logzioKinesisLambda",
        "logzio_kinesis_lambda_kinesis_stream": "logzioKinesisLambdaKinesisStream",
        "logzio_kinesis_lambda_role": "logzioKinesisLambdaRole",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        logzio_kinesis_lambda: typing.Optional["CfnModulePropsResourcesLogzioKinesisLambda"] = None,
        logzio_kinesis_lambda_kinesis_stream: typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream"] = None,
        logzio_kinesis_lambda_role: typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaRole"] = None,
    ) -> None:
        '''
        :param logzio_kinesis_lambda: 
        :param logzio_kinesis_lambda_kinesis_stream: 
        :param logzio_kinesis_lambda_role: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(logzio_kinesis_lambda, dict):
            logzio_kinesis_lambda = CfnModulePropsResourcesLogzioKinesisLambda(**logzio_kinesis_lambda)
        if isinstance(logzio_kinesis_lambda_kinesis_stream, dict):
            logzio_kinesis_lambda_kinesis_stream = CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream(**logzio_kinesis_lambda_kinesis_stream)
        if isinstance(logzio_kinesis_lambda_role, dict):
            logzio_kinesis_lambda_role = CfnModulePropsResourcesLogzioKinesisLambdaRole(**logzio_kinesis_lambda_role)
        self._values: typing.Dict[str, typing.Any] = {}
        if logzio_kinesis_lambda is not None:
            self._values["logzio_kinesis_lambda"] = logzio_kinesis_lambda
        if logzio_kinesis_lambda_kinesis_stream is not None:
            self._values["logzio_kinesis_lambda_kinesis_stream"] = logzio_kinesis_lambda_kinesis_stream
        if logzio_kinesis_lambda_role is not None:
            self._values["logzio_kinesis_lambda_role"] = logzio_kinesis_lambda_role

    @builtins.property
    def logzio_kinesis_lambda(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioKinesisLambda"]:
        '''
        :schema: CfnModulePropsResources#LogzioKinesisLambda
        '''
        result = self._values.get("logzio_kinesis_lambda")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioKinesisLambda"], result)

    @builtins.property
    def logzio_kinesis_lambda_kinesis_stream(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream"]:
        '''
        :schema: CfnModulePropsResources#LogzioKinesisLambdaKinesisStream
        '''
        result = self._values.get("logzio_kinesis_lambda_kinesis_stream")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream"], result)

    @builtins.property
    def logzio_kinesis_lambda_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaRole"]:
        '''
        :schema: CfnModulePropsResources#LogzioKinesisLambdaRole
        '''
        result = self._values.get("logzio_kinesis_lambda_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLogzioKinesisLambdaRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsResourcesLogzioKinesisLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioKinesisLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioKinesisLambda
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioKinesisLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnModulePropsResourcesLogzioKinesisLambdaRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLogzioKinesisLambdaRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLogzioKinesisLambdaRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambdaRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLogzioKinesisLambdaRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLogzioKinesisLambdaRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersKinesisStream",
    "CfnModulePropsParametersKinesisStreamBatchSize",
    "CfnModulePropsParametersKinesisStreamStartingPosition",
    "CfnModulePropsParametersLogzioCompress",
    "CfnModulePropsParametersLogzioFormat",
    "CfnModulePropsParametersLogzioMessagesArray",
    "CfnModulePropsParametersLogzioRegion",
    "CfnModulePropsParametersLogzioToken",
    "CfnModulePropsParametersLogzioType",
    "CfnModulePropsParametersLogzioUrl",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesLogzioKinesisLambda",
    "CfnModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    "CfnModulePropsResourcesLogzioKinesisLambdaRole",
]

publication.publish()
