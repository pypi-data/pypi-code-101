'''
# logzio-kinesisshipper-kinesisshipper-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Logzio::KinesisShipper::KinesisShipper::MODULE` v1.2.0.

## Description

Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Logzio::KinesisShipper::KinesisShipper::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/Logzio-KinesisShipper-KinesisShipper-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Logzio::KinesisShipper::KinesisShipper::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-kinesisshipper-kinesisshipper-module+v1.2.0).
* Issues related to `Logzio::KinesisShipper::KinesisShipper::MODULE` should be reported to the [publisher](undefined).

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


class CfnKinesisShipperModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModule",
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
        parameters: typing.Optional["CfnKinesisShipperModulePropsParameters"] = None,
        resources: typing.Optional["CfnKinesisShipperModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Logzio::KinesisShipper::KinesisShipper::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnKinesisShipperModuleProps(
            parameters=parameters, resources=resources
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnKinesisShipperModuleProps":
        '''Resource props.'''
        return typing.cast("CfnKinesisShipperModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnKinesisShipperModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnKinesisShipperModulePropsParameters"] = None,
        resources: typing.Optional["CfnKinesisShipperModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnKinesisShipperModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnKinesisShipperModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnKinesisShipperModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnKinesisShipperModulePropsParameters"]:
        '''
        :schema: CfnKinesisShipperModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnKinesisShipperModulePropsResources"]:
        '''
        :schema: CfnKinesisShipperModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParameters",
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
class CfnKinesisShipperModulePropsParameters:
    def __init__(
        self,
        *,
        kinesis_stream: typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStream"] = None,
        kinesis_stream_batch_size: typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize"] = None,
        kinesis_stream_starting_position: typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition"] = None,
        logzio_compress: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioCompress"] = None,
        logzio_format: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioFormat"] = None,
        logzio_messages_array: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioMessagesArray"] = None,
        logzio_region: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioRegion"] = None,
        logzio_token: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioToken"] = None,
        logzio_type: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioType"] = None,
        logzio_url: typing.Optional["CfnKinesisShipperModulePropsParametersLogzioUrl"] = None,
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

        :schema: CfnKinesisShipperModulePropsParameters
        '''
        if isinstance(kinesis_stream, dict):
            kinesis_stream = CfnKinesisShipperModulePropsParametersKinesisStream(**kinesis_stream)
        if isinstance(kinesis_stream_batch_size, dict):
            kinesis_stream_batch_size = CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize(**kinesis_stream_batch_size)
        if isinstance(kinesis_stream_starting_position, dict):
            kinesis_stream_starting_position = CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition(**kinesis_stream_starting_position)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnKinesisShipperModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_format, dict):
            logzio_format = CfnKinesisShipperModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_messages_array, dict):
            logzio_messages_array = CfnKinesisShipperModulePropsParametersLogzioMessagesArray(**logzio_messages_array)
        if isinstance(logzio_region, dict):
            logzio_region = CfnKinesisShipperModulePropsParametersLogzioRegion(**logzio_region)
        if isinstance(logzio_token, dict):
            logzio_token = CfnKinesisShipperModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnKinesisShipperModulePropsParametersLogzioType(**logzio_type)
        if isinstance(logzio_url, dict):
            logzio_url = CfnKinesisShipperModulePropsParametersLogzioUrl(**logzio_url)
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
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStream"]:
        '''Enter a Kinesis stream to listen for updates on.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStream
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStream"], result)

    @builtins.property
    def kinesis_stream_batch_size(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize"]:
        '''The largest number of records that will be read from your stream at once.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStreamBatchSize
        '''
        result = self._values.get("kinesis_stream_batch_size")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize"], result)

    @builtins.property
    def kinesis_stream_starting_position(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition"]:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStreamStartingPosition
        '''
        result = self._values.get("kinesis_stream_starting_position")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioCOMPRESS
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_format(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioFormat"]:
        '''json or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioFORMAT
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_messages_array(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioMessagesArray"]:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioMessagesArray
        '''
        result = self._values.get("logzio_messages_array")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioMessagesArray"], result)

    @builtins.property
    def logzio_region(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioRegion"]:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :schema: CfnKinesisShipperModulePropsParameters#LogzioREGION
        '''
        result = self._values.get("logzio_region")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioRegion"], result)

    @builtins.property
    def logzio_token(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioToken"]:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

        :schema: CfnKinesisShipperModulePropsParameters#LogzioTOKEN
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnKinesisShipperModulePropsParameters#LogzioTYPE
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioType"], result)

    @builtins.property
    def logzio_url(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioUrl"]:
        '''Deprecated.

        Use LogzioREGION instead

        :schema: CfnKinesisShipperModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStream:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enter a Kinesis stream to listen for updates on.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStream
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStream#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStream#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The largest number of records that will be read from your stream at once.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioCompress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioCompress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioCompress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''json or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioMessagesArray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioMessagesArray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioMessagesArray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Deprecated.

        Use LogzioREGION instead

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_kinesis_lambda": "logzioKinesisLambda",
        "logzio_kinesis_lambda_kinesis_stream": "logzioKinesisLambdaKinesisStream",
        "logzio_kinesis_lambda_role": "logzioKinesisLambdaRole",
    },
)
class CfnKinesisShipperModulePropsResources:
    def __init__(
        self,
        *,
        logzio_kinesis_lambda: typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda"] = None,
        logzio_kinesis_lambda_kinesis_stream: typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream"] = None,
        logzio_kinesis_lambda_role: typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole"] = None,
    ) -> None:
        '''
        :param logzio_kinesis_lambda: 
        :param logzio_kinesis_lambda_kinesis_stream: 
        :param logzio_kinesis_lambda_role: 

        :schema: CfnKinesisShipperModulePropsResources
        '''
        if isinstance(logzio_kinesis_lambda, dict):
            logzio_kinesis_lambda = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda(**logzio_kinesis_lambda)
        if isinstance(logzio_kinesis_lambda_kinesis_stream, dict):
            logzio_kinesis_lambda_kinesis_stream = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream(**logzio_kinesis_lambda_kinesis_stream)
        if isinstance(logzio_kinesis_lambda_role, dict):
            logzio_kinesis_lambda_role = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole(**logzio_kinesis_lambda_role)
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
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambda
        '''
        result = self._values.get("logzio_kinesis_lambda")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda"], result)

    @builtins.property
    def logzio_kinesis_lambda_kinesis_stream(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambdaKinesisStream
        '''
        result = self._values.get("logzio_kinesis_lambda_kinesis_stream")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream"], result)

    @builtins.property
    def logzio_kinesis_lambda_role(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambdaRole
        '''
        result = self._values.get("logzio_kinesis_lambda_role")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKinesisShipperModule",
    "CfnKinesisShipperModuleProps",
    "CfnKinesisShipperModulePropsParameters",
    "CfnKinesisShipperModulePropsParametersKinesisStream",
    "CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize",
    "CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition",
    "CfnKinesisShipperModulePropsParametersLogzioCompress",
    "CfnKinesisShipperModulePropsParametersLogzioFormat",
    "CfnKinesisShipperModulePropsParametersLogzioMessagesArray",
    "CfnKinesisShipperModulePropsParametersLogzioRegion",
    "CfnKinesisShipperModulePropsParametersLogzioToken",
    "CfnKinesisShipperModulePropsParametersLogzioType",
    "CfnKinesisShipperModulePropsParametersLogzioUrl",
    "CfnKinesisShipperModulePropsResources",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole",
]

publication.publish()
