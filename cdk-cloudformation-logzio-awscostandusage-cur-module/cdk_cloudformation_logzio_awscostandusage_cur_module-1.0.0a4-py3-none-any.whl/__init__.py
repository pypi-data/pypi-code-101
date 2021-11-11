'''
# logzio-awscostandusage-cur-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Logzio::awsCostAndUsage::cur::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Logzio::awsCostAndUsage::cur::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/Logzio-awsCostAndUsage-cur-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Logzio::awsCostAndUsage::cur::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-awscostandusage-cur-module+v1.0.0).
* Issues related to `Logzio::awsCostAndUsage::cur::MODULE` should be reported to the [publisher](undefined).

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


class CfnCurModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModule",
):
    '''A CloudFormation ``Logzio::awsCostAndUsage::cur::MODULE``.

    :cloudformationResource: Logzio::awsCostAndUsage::cur::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnCurModulePropsParameters"] = None,
        resources: typing.Optional["CfnCurModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Logzio::awsCostAndUsage::cur::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnCurModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCurModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCurModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCurModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnCurModulePropsParameters"] = None,
        resources: typing.Optional["CfnCurModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCurModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCurModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCurModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCurModulePropsParameters"]:
        '''
        :schema: CfnCurModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCurModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCurModulePropsResources"]:
        '''
        :schema: CfnCurModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCurModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_event_schedule_expression": "cloudWatchEventScheduleExpression",
        "lambda_memory_size": "lambdaMemorySize",
        "lambda_timeout": "lambdaTimeout",
        "logzio_token": "logzioToken",
        "logzio_url": "logzioUrl",
        "report_additional_schema_elements": "reportAdditionalSchemaElements",
        "report_name": "reportName",
        "report_prefix": "reportPrefix",
        "report_time_unit": "reportTimeUnit",
        "s3_bucket_name": "s3BucketName",
    },
)
class CfnCurModulePropsParameters:
    def __init__(
        self,
        *,
        cloud_watch_event_schedule_expression: typing.Optional["CfnCurModulePropsParametersCloudWatchEventScheduleExpression"] = None,
        lambda_memory_size: typing.Optional["CfnCurModulePropsParametersLambdaMemorySize"] = None,
        lambda_timeout: typing.Optional["CfnCurModulePropsParametersLambdaTimeout"] = None,
        logzio_token: typing.Optional["CfnCurModulePropsParametersLogzioToken"] = None,
        logzio_url: typing.Optional["CfnCurModulePropsParametersLogzioUrl"] = None,
        report_additional_schema_elements: typing.Optional["CfnCurModulePropsParametersReportAdditionalSchemaElements"] = None,
        report_name: typing.Optional["CfnCurModulePropsParametersReportName"] = None,
        report_prefix: typing.Optional["CfnCurModulePropsParametersReportPrefix"] = None,
        report_time_unit: typing.Optional["CfnCurModulePropsParametersReportTimeUnit"] = None,
        s3_bucket_name: typing.Optional["CfnCurModulePropsParametersS3BucketName"] = None,
    ) -> None:
        '''
        :param cloud_watch_event_schedule_expression: The scheduling expression that determines when and how often the Lambda function runs. We recommend to start with 10 hour rate.
        :param lambda_memory_size: The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.
        :param lambda_timeout: The amount of time that Lambda allows a function to run before stopping it. Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).
        :param logzio_token: Your Logz.io logs token. (Can be retrieved from the Manage Token page.).
        :param logzio_url: The Logz.io listener URL fot your region. (For more details, see the regions page: https://docs.logz.io/user-guide/accounts/account-region.html).
        :param report_additional_schema_elements: Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance. AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.
        :param report_name: The name of report that you want to create. The name must be unique, is case sensitive and can't include spaces.
        :param report_prefix: The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
        :param report_time_unit: The granularity of the line items in the report. (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)
        :param s3_bucket_name: The name for the bucket which will contain the report files. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :schema: CfnCurModulePropsParameters
        '''
        if isinstance(cloud_watch_event_schedule_expression, dict):
            cloud_watch_event_schedule_expression = CfnCurModulePropsParametersCloudWatchEventScheduleExpression(**cloud_watch_event_schedule_expression)
        if isinstance(lambda_memory_size, dict):
            lambda_memory_size = CfnCurModulePropsParametersLambdaMemorySize(**lambda_memory_size)
        if isinstance(lambda_timeout, dict):
            lambda_timeout = CfnCurModulePropsParametersLambdaTimeout(**lambda_timeout)
        if isinstance(logzio_token, dict):
            logzio_token = CfnCurModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_url, dict):
            logzio_url = CfnCurModulePropsParametersLogzioUrl(**logzio_url)
        if isinstance(report_additional_schema_elements, dict):
            report_additional_schema_elements = CfnCurModulePropsParametersReportAdditionalSchemaElements(**report_additional_schema_elements)
        if isinstance(report_name, dict):
            report_name = CfnCurModulePropsParametersReportName(**report_name)
        if isinstance(report_prefix, dict):
            report_prefix = CfnCurModulePropsParametersReportPrefix(**report_prefix)
        if isinstance(report_time_unit, dict):
            report_time_unit = CfnCurModulePropsParametersReportTimeUnit(**report_time_unit)
        if isinstance(s3_bucket_name, dict):
            s3_bucket_name = CfnCurModulePropsParametersS3BucketName(**s3_bucket_name)
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_watch_event_schedule_expression is not None:
            self._values["cloud_watch_event_schedule_expression"] = cloud_watch_event_schedule_expression
        if lambda_memory_size is not None:
            self._values["lambda_memory_size"] = lambda_memory_size
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_url is not None:
            self._values["logzio_url"] = logzio_url
        if report_additional_schema_elements is not None:
            self._values["report_additional_schema_elements"] = report_additional_schema_elements
        if report_name is not None:
            self._values["report_name"] = report_name
        if report_prefix is not None:
            self._values["report_prefix"] = report_prefix
        if report_time_unit is not None:
            self._values["report_time_unit"] = report_time_unit
        if s3_bucket_name is not None:
            self._values["s3_bucket_name"] = s3_bucket_name

    @builtins.property
    def cloud_watch_event_schedule_expression(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersCloudWatchEventScheduleExpression"]:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :schema: CfnCurModulePropsParameters#CloudWatchEventScheduleExpression
        '''
        result = self._values.get("cloud_watch_event_schedule_expression")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersCloudWatchEventScheduleExpression"], result)

    @builtins.property
    def lambda_memory_size(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersLambdaMemorySize"]:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :schema: CfnCurModulePropsParameters#LambdaMemorySize
        '''
        result = self._values.get("lambda_memory_size")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLambdaMemorySize"], result)

    @builtins.property
    def lambda_timeout(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersLambdaTimeout"]:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :schema: CfnCurModulePropsParameters#LambdaTimeout
        '''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLambdaTimeout"], result)

    @builtins.property
    def logzio_token(self) -> typing.Optional["CfnCurModulePropsParametersLogzioToken"]:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

        :schema: CfnCurModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_url(self) -> typing.Optional["CfnCurModulePropsParametersLogzioUrl"]:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

        :schema: CfnCurModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLogzioUrl"], result)

    @builtins.property
    def report_additional_schema_elements(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportAdditionalSchemaElements"]:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :schema: CfnCurModulePropsParameters#ReportAdditionalSchemaElements
        '''
        result = self._values.get("report_additional_schema_elements")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportAdditionalSchemaElements"], result)

    @builtins.property
    def report_name(self) -> typing.Optional["CfnCurModulePropsParametersReportName"]:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :schema: CfnCurModulePropsParameters#ReportName
        '''
        result = self._values.get("report_name")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportName"], result)

    @builtins.property
    def report_prefix(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportPrefix"]:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :schema: CfnCurModulePropsParameters#ReportPrefix
        '''
        result = self._values.get("report_prefix")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportPrefix"], result)

    @builtins.property
    def report_time_unit(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportTimeUnit"]:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :schema: CfnCurModulePropsParameters#ReportTimeUnit
        '''
        result = self._values.get("report_time_unit")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportTimeUnit"], result)

    @builtins.property
    def s3_bucket_name(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersS3BucketName"]:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :schema: CfnCurModulePropsParameters#S3BucketName
        '''
        result = self._values.get("s3_bucket_name")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersS3BucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersCloudWatchEventScheduleExpression",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersCloudWatchEventScheduleExpression:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersCloudWatchEventScheduleExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLambdaMemorySize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLambdaMemorySize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLambdaMemorySize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaMemorySize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaMemorySize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLambdaMemorySize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLambdaTimeout",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLambdaTimeout:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLambdaTimeout
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaTimeout#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaTimeout#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLambdaTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLogzioToken
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLogzioUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLogzioUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportAdditionalSchemaElements",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportAdditionalSchemaElements:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportAdditionalSchemaElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportTimeUnit",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportTimeUnit:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportTimeUnit
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportTimeUnit#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportTimeUnit#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportTimeUnit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "cur": "cur",
        "event_rule": "eventRule",
        "iam_role": "iamRole",
        "lambda_function": "lambdaFunction",
        "lambda_permission": "lambdaPermission",
        "s3_bucket": "s3Bucket",
        "s3_bucket_policy": "s3BucketPolicy",
    },
)
class CfnCurModulePropsResources:
    def __init__(
        self,
        *,
        cur: typing.Optional["CfnCurModulePropsResourcesCur"] = None,
        event_rule: typing.Optional["CfnCurModulePropsResourcesEventRule"] = None,
        iam_role: typing.Optional["CfnCurModulePropsResourcesIamRole"] = None,
        lambda_function: typing.Optional["CfnCurModulePropsResourcesLambdaFunction"] = None,
        lambda_permission: typing.Optional["CfnCurModulePropsResourcesLambdaPermission"] = None,
        s3_bucket: typing.Optional["CfnCurModulePropsResourcesS3Bucket"] = None,
        s3_bucket_policy: typing.Optional["CfnCurModulePropsResourcesS3BucketPolicy"] = None,
    ) -> None:
        '''
        :param cur: 
        :param event_rule: 
        :param iam_role: 
        :param lambda_function: 
        :param lambda_permission: 
        :param s3_bucket: 
        :param s3_bucket_policy: 

        :schema: CfnCurModulePropsResources
        '''
        if isinstance(cur, dict):
            cur = CfnCurModulePropsResourcesCur(**cur)
        if isinstance(event_rule, dict):
            event_rule = CfnCurModulePropsResourcesEventRule(**event_rule)
        if isinstance(iam_role, dict):
            iam_role = CfnCurModulePropsResourcesIamRole(**iam_role)
        if isinstance(lambda_function, dict):
            lambda_function = CfnCurModulePropsResourcesLambdaFunction(**lambda_function)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnCurModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnCurModulePropsResourcesS3Bucket(**s3_bucket)
        if isinstance(s3_bucket_policy, dict):
            s3_bucket_policy = CfnCurModulePropsResourcesS3BucketPolicy(**s3_bucket_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if cur is not None:
            self._values["cur"] = cur
        if event_rule is not None:
            self._values["event_rule"] = event_rule
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if lambda_function is not None:
            self._values["lambda_function"] = lambda_function
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_bucket_policy is not None:
            self._values["s3_bucket_policy"] = s3_bucket_policy

    @builtins.property
    def cur(self) -> typing.Optional["CfnCurModulePropsResourcesCur"]:
        '''
        :schema: CfnCurModulePropsResources#CUR
        '''
        result = self._values.get("cur")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesCur"], result)

    @builtins.property
    def event_rule(self) -> typing.Optional["CfnCurModulePropsResourcesEventRule"]:
        '''
        :schema: CfnCurModulePropsResources#EventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesEventRule"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnCurModulePropsResourcesIamRole"]:
        '''
        :schema: CfnCurModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesIamRole"], result)

    @builtins.property
    def lambda_function(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesLambdaFunction"]:
        '''
        :schema: CfnCurModulePropsResources#LambdaFunction
        '''
        result = self._values.get("lambda_function")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesLambdaFunction"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnCurModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesLambdaPermission"], result)

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnCurModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnCurModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesS3Bucket"], result)

    @builtins.property
    def s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesS3BucketPolicy"]:
        '''
        :schema: CfnCurModulePropsResources#S3BucketPolicy
        '''
        result = self._values.get("s3_bucket_policy")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesS3BucketPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesCur",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesCur:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesCur
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesCur#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesCur#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesCur(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesEventRule
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesLambdaFunction
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesLambdaPermission
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesS3BucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCurModulePropsResourcesS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCurModule",
    "CfnCurModuleProps",
    "CfnCurModulePropsParameters",
    "CfnCurModulePropsParametersCloudWatchEventScheduleExpression",
    "CfnCurModulePropsParametersLambdaMemorySize",
    "CfnCurModulePropsParametersLambdaTimeout",
    "CfnCurModulePropsParametersLogzioToken",
    "CfnCurModulePropsParametersLogzioUrl",
    "CfnCurModulePropsParametersReportAdditionalSchemaElements",
    "CfnCurModulePropsParametersReportName",
    "CfnCurModulePropsParametersReportPrefix",
    "CfnCurModulePropsParametersReportTimeUnit",
    "CfnCurModulePropsParametersS3BucketName",
    "CfnCurModulePropsResources",
    "CfnCurModulePropsResourcesCur",
    "CfnCurModulePropsResourcesEventRule",
    "CfnCurModulePropsResourcesIamRole",
    "CfnCurModulePropsResourcesLambdaFunction",
    "CfnCurModulePropsResourcesLambdaPermission",
    "CfnCurModulePropsResourcesS3Bucket",
    "CfnCurModulePropsResourcesS3BucketPolicy",
]

publication.publish()
