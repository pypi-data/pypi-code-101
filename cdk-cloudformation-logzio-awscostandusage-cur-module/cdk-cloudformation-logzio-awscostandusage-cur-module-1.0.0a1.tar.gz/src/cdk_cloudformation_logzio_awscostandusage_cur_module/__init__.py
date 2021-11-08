'''
# AWS CDK CloudFormation Constructs for Logzio::awsCostAndUsage::cur::MODULE

Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE

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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModule",
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
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Logzio::awsCostAndUsage::cur::MODULE``.

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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE.

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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParameters",
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
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        cloud_watch_event_schedule_expression: typing.Optional["CfnModulePropsParametersCloudWatchEventScheduleExpression"] = None,
        lambda_memory_size: typing.Optional["CfnModulePropsParametersLambdaMemorySize"] = None,
        lambda_timeout: typing.Optional["CfnModulePropsParametersLambdaTimeout"] = None,
        logzio_token: typing.Optional["CfnModulePropsParametersLogzioToken"] = None,
        logzio_url: typing.Optional["CfnModulePropsParametersLogzioUrl"] = None,
        report_additional_schema_elements: typing.Optional["CfnModulePropsParametersReportAdditionalSchemaElements"] = None,
        report_name: typing.Optional["CfnModulePropsParametersReportName"] = None,
        report_prefix: typing.Optional["CfnModulePropsParametersReportPrefix"] = None,
        report_time_unit: typing.Optional["CfnModulePropsParametersReportTimeUnit"] = None,
        s3_bucket_name: typing.Optional["CfnModulePropsParametersS3BucketName"] = None,
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

        :schema: CfnModulePropsParameters
        '''
        if isinstance(cloud_watch_event_schedule_expression, dict):
            cloud_watch_event_schedule_expression = CfnModulePropsParametersCloudWatchEventScheduleExpression(**cloud_watch_event_schedule_expression)
        if isinstance(lambda_memory_size, dict):
            lambda_memory_size = CfnModulePropsParametersLambdaMemorySize(**lambda_memory_size)
        if isinstance(lambda_timeout, dict):
            lambda_timeout = CfnModulePropsParametersLambdaTimeout(**lambda_timeout)
        if isinstance(logzio_token, dict):
            logzio_token = CfnModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_url, dict):
            logzio_url = CfnModulePropsParametersLogzioUrl(**logzio_url)
        if isinstance(report_additional_schema_elements, dict):
            report_additional_schema_elements = CfnModulePropsParametersReportAdditionalSchemaElements(**report_additional_schema_elements)
        if isinstance(report_name, dict):
            report_name = CfnModulePropsParametersReportName(**report_name)
        if isinstance(report_prefix, dict):
            report_prefix = CfnModulePropsParametersReportPrefix(**report_prefix)
        if isinstance(report_time_unit, dict):
            report_time_unit = CfnModulePropsParametersReportTimeUnit(**report_time_unit)
        if isinstance(s3_bucket_name, dict):
            s3_bucket_name = CfnModulePropsParametersS3BucketName(**s3_bucket_name)
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
    ) -> typing.Optional["CfnModulePropsParametersCloudWatchEventScheduleExpression"]:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :schema: CfnModulePropsParameters#CloudWatchEventScheduleExpression
        '''
        result = self._values.get("cloud_watch_event_schedule_expression")
        return typing.cast(typing.Optional["CfnModulePropsParametersCloudWatchEventScheduleExpression"], result)

    @builtins.property
    def lambda_memory_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLambdaMemorySize"]:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :schema: CfnModulePropsParameters#LambdaMemorySize
        '''
        result = self._values.get("lambda_memory_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersLambdaMemorySize"], result)

    @builtins.property
    def lambda_timeout(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLambdaTimeout"]:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :schema: CfnModulePropsParameters#LambdaTimeout
        '''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional["CfnModulePropsParametersLambdaTimeout"], result)

    @builtins.property
    def logzio_token(self) -> typing.Optional["CfnModulePropsParametersLogzioToken"]:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

        :schema: CfnModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_url(self) -> typing.Optional["CfnModulePropsParametersLogzioUrl"]:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

        :schema: CfnModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogzioUrl"], result)

    @builtins.property
    def report_additional_schema_elements(
        self,
    ) -> typing.Optional["CfnModulePropsParametersReportAdditionalSchemaElements"]:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :schema: CfnModulePropsParameters#ReportAdditionalSchemaElements
        '''
        result = self._values.get("report_additional_schema_elements")
        return typing.cast(typing.Optional["CfnModulePropsParametersReportAdditionalSchemaElements"], result)

    @builtins.property
    def report_name(self) -> typing.Optional["CfnModulePropsParametersReportName"]:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :schema: CfnModulePropsParameters#ReportName
        '''
        result = self._values.get("report_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersReportName"], result)

    @builtins.property
    def report_prefix(self) -> typing.Optional["CfnModulePropsParametersReportPrefix"]:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :schema: CfnModulePropsParameters#ReportPrefix
        '''
        result = self._values.get("report_prefix")
        return typing.cast(typing.Optional["CfnModulePropsParametersReportPrefix"], result)

    @builtins.property
    def report_time_unit(
        self,
    ) -> typing.Optional["CfnModulePropsParametersReportTimeUnit"]:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :schema: CfnModulePropsParameters#ReportTimeUnit
        '''
        result = self._values.get("report_time_unit")
        return typing.cast(typing.Optional["CfnModulePropsParametersReportTimeUnit"], result)

    @builtins.property
    def s3_bucket_name(self) -> typing.Optional["CfnModulePropsParametersS3BucketName"]:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :schema: CfnModulePropsParameters#S3BucketName
        '''
        result = self._values.get("s3_bucket_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersS3BucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersCloudWatchEventScheduleExpression",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCloudWatchEventScheduleExpression:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCloudWatchEventScheduleExpression
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCloudWatchEventScheduleExpression#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCloudWatchEventScheduleExpression#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCloudWatchEventScheduleExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersLambdaMemorySize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLambdaMemorySize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLambdaMemorySize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLambdaMemorySize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLambdaMemorySize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLambdaMemorySize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersLambdaTimeout",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLambdaTimeout:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLambdaTimeout
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLambdaTimeout#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLambdaTimeout#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLambdaTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersReportAdditionalSchemaElements",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersReportAdditionalSchemaElements:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersReportAdditionalSchemaElements
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportAdditionalSchemaElements#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportAdditionalSchemaElements#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersReportAdditionalSchemaElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersReportName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersReportName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersReportName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersReportName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersReportPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersReportPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersReportPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersReportPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersReportTimeUnit",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersReportTimeUnit:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersReportTimeUnit
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportTimeUnit#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReportTimeUnit#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersReportTimeUnit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsParametersS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResources",
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
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        cur: typing.Optional["CfnModulePropsResourcesCur"] = None,
        event_rule: typing.Optional["CfnModulePropsResourcesEventRule"] = None,
        iam_role: typing.Optional["CfnModulePropsResourcesIamRole"] = None,
        lambda_function: typing.Optional["CfnModulePropsResourcesLambdaFunction"] = None,
        lambda_permission: typing.Optional["CfnModulePropsResourcesLambdaPermission"] = None,
        s3_bucket: typing.Optional["CfnModulePropsResourcesS3Bucket"] = None,
        s3_bucket_policy: typing.Optional["CfnModulePropsResourcesS3BucketPolicy"] = None,
    ) -> None:
        '''
        :param cur: 
        :param event_rule: 
        :param iam_role: 
        :param lambda_function: 
        :param lambda_permission: 
        :param s3_bucket: 
        :param s3_bucket_policy: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(cur, dict):
            cur = CfnModulePropsResourcesCur(**cur)
        if isinstance(event_rule, dict):
            event_rule = CfnModulePropsResourcesEventRule(**event_rule)
        if isinstance(iam_role, dict):
            iam_role = CfnModulePropsResourcesIamRole(**iam_role)
        if isinstance(lambda_function, dict):
            lambda_function = CfnModulePropsResourcesLambdaFunction(**lambda_function)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnModulePropsResourcesS3Bucket(**s3_bucket)
        if isinstance(s3_bucket_policy, dict):
            s3_bucket_policy = CfnModulePropsResourcesS3BucketPolicy(**s3_bucket_policy)
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
    def cur(self) -> typing.Optional["CfnModulePropsResourcesCur"]:
        '''
        :schema: CfnModulePropsResources#CUR
        '''
        result = self._values.get("cur")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCur"], result)

    @builtins.property
    def event_rule(self) -> typing.Optional["CfnModulePropsResourcesEventRule"]:
        '''
        :schema: CfnModulePropsResources#EventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEventRule"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnModulePropsResourcesIamRole"]:
        '''
        :schema: CfnModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesIamRole"], result)

    @builtins.property
    def lambda_function(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLambdaFunction"]:
        '''
        :schema: CfnModulePropsResources#LambdaFunction
        '''
        result = self._values.get("lambda_function")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLambdaFunction"], result)

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
    def s3_bucket(self) -> typing.Optional["CfnModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnModulePropsResourcesS3Bucket"], result)

    @builtins.property
    def s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesS3BucketPolicy"]:
        '''
        :schema: CfnModulePropsResources#S3BucketPolicy
        '''
        result = self._values.get("s3_bucket_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesS3BucketPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesCur",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCur:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCur
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCur#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCur#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCur(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesEventRule",
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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLambdaFunction
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesLambdaPermission",
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
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnModulePropsResourcesS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesS3BucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersCloudWatchEventScheduleExpression",
    "CfnModulePropsParametersLambdaMemorySize",
    "CfnModulePropsParametersLambdaTimeout",
    "CfnModulePropsParametersLogzioToken",
    "CfnModulePropsParametersLogzioUrl",
    "CfnModulePropsParametersReportAdditionalSchemaElements",
    "CfnModulePropsParametersReportName",
    "CfnModulePropsParametersReportPrefix",
    "CfnModulePropsParametersReportTimeUnit",
    "CfnModulePropsParametersS3BucketName",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesCur",
    "CfnModulePropsResourcesEventRule",
    "CfnModulePropsResourcesIamRole",
    "CfnModulePropsResourcesLambdaFunction",
    "CfnModulePropsResourcesLambdaPermission",
    "CfnModulePropsResourcesS3Bucket",
    "CfnModulePropsResourcesS3BucketPolicy",
]

publication.publish()
