'''
# awsqs-iridium-cloudconnectqs-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::Iridium::CloudConnectQS::MODULE` v1.1.0.

## Description

Schema for Module Fragment of type AWSQS::Iridium::CloudConnectQS::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::Iridium::CloudConnectQS::MODULE \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-Iridium-CloudConnectQS-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::Iridium::CloudConnectQS::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-iridium-cloudconnectqs-module+v1.1.0).
* Issues related to `AWSQS::Iridium::CloudConnectQS::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudConnectQsModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModule",
):
    '''A CloudFormation ``AWSQS::Iridium::CloudConnectQS::MODULE``.

    :cloudformationResource: AWSQS::Iridium::CloudConnectQS::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnCloudConnectQsModulePropsParameters"] = None,
        resources: typing.Optional["CfnCloudConnectQsModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``AWSQS::Iridium::CloudConnectQS::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnCloudConnectQsModuleProps(
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
    def props(self) -> "CfnCloudConnectQsModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudConnectQsModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCloudConnectQsModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnCloudConnectQsModulePropsParameters"] = None,
        resources: typing.Optional["CfnCloudConnectQsModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type AWSQS::Iridium::CloudConnectQS::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCloudConnectQsModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCloudConnectQsModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCloudConnectQsModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCloudConnectQsModulePropsParameters"]:
        '''
        :schema: CfnCloudConnectQsModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCloudConnectQsModulePropsResources"]:
        '''
        :schema: CfnCloudConnectQsModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "iridium_role_arn": "iridiumRoleArn",
        "mobile_originated_queue_name": "mobileOriginatedQueueName",
        "mobile_terminated_confirmation_queue_name": "mobileTerminatedConfirmationQueueName",
        "mobile_terminated_error_queue_name": "mobileTerminatedErrorQueueName",
        "mobile_terminated_queue_name": "mobileTerminatedQueueName",
    },
)
class CfnCloudConnectQsModulePropsParameters:
    def __init__(
        self,
        *,
        iridium_role_arn: typing.Optional["CfnCloudConnectQsModulePropsParametersIridiumRoleArn"] = None,
        mobile_originated_queue_name: typing.Optional["CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName"] = None,
        mobile_terminated_confirmation_queue_name: typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName"] = None,
        mobile_terminated_error_queue_name: typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName"] = None,
        mobile_terminated_queue_name: typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName"] = None,
    ) -> None:
        '''
        :param iridium_role_arn: Amazon Resource Number (ARN) of the role in the Iridium AWS account.
        :param mobile_originated_queue_name: Name of the mobile-originated queue in Amazon SQS.
        :param mobile_terminated_confirmation_queue_name: Name of the mobile-terminated confirmation queue in Amazon SQS.
        :param mobile_terminated_error_queue_name: Name of the mobile-terminated error queue in Amazon SQS.
        :param mobile_terminated_queue_name: Name of the mobile-terminated queue in Amazon SQS.

        :schema: CfnCloudConnectQsModulePropsParameters
        '''
        if isinstance(iridium_role_arn, dict):
            iridium_role_arn = CfnCloudConnectQsModulePropsParametersIridiumRoleArn(**iridium_role_arn)
        if isinstance(mobile_originated_queue_name, dict):
            mobile_originated_queue_name = CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName(**mobile_originated_queue_name)
        if isinstance(mobile_terminated_confirmation_queue_name, dict):
            mobile_terminated_confirmation_queue_name = CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName(**mobile_terminated_confirmation_queue_name)
        if isinstance(mobile_terminated_error_queue_name, dict):
            mobile_terminated_error_queue_name = CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName(**mobile_terminated_error_queue_name)
        if isinstance(mobile_terminated_queue_name, dict):
            mobile_terminated_queue_name = CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName(**mobile_terminated_queue_name)
        self._values: typing.Dict[str, typing.Any] = {}
        if iridium_role_arn is not None:
            self._values["iridium_role_arn"] = iridium_role_arn
        if mobile_originated_queue_name is not None:
            self._values["mobile_originated_queue_name"] = mobile_originated_queue_name
        if mobile_terminated_confirmation_queue_name is not None:
            self._values["mobile_terminated_confirmation_queue_name"] = mobile_terminated_confirmation_queue_name
        if mobile_terminated_error_queue_name is not None:
            self._values["mobile_terminated_error_queue_name"] = mobile_terminated_error_queue_name
        if mobile_terminated_queue_name is not None:
            self._values["mobile_terminated_queue_name"] = mobile_terminated_queue_name

    @builtins.property
    def iridium_role_arn(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsParametersIridiumRoleArn"]:
        '''Amazon Resource Number (ARN) of the role in the Iridium AWS account.

        :schema: CfnCloudConnectQsModulePropsParameters#IridiumRoleARN
        '''
        result = self._values.get("iridium_role_arn")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParametersIridiumRoleArn"], result)

    @builtins.property
    def mobile_originated_queue_name(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName"]:
        '''Name of the mobile-originated queue in Amazon SQS.

        :schema: CfnCloudConnectQsModulePropsParameters#MobileOriginatedQueueName
        '''
        result = self._values.get("mobile_originated_queue_name")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName"], result)

    @builtins.property
    def mobile_terminated_confirmation_queue_name(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName"]:
        '''Name of the mobile-terminated confirmation queue in Amazon SQS.

        :schema: CfnCloudConnectQsModulePropsParameters#MobileTerminatedConfirmationQueueName
        '''
        result = self._values.get("mobile_terminated_confirmation_queue_name")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName"], result)

    @builtins.property
    def mobile_terminated_error_queue_name(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName"]:
        '''Name of the mobile-terminated error queue in Amazon SQS.

        :schema: CfnCloudConnectQsModulePropsParameters#MobileTerminatedErrorQueueName
        '''
        result = self._values.get("mobile_terminated_error_queue_name")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName"], result)

    @builtins.property
    def mobile_terminated_queue_name(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName"]:
        '''Name of the mobile-terminated queue in Amazon SQS.

        :schema: CfnCloudConnectQsModulePropsParameters#MobileTerminatedQueueName
        '''
        result = self._values.get("mobile_terminated_queue_name")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParametersIridiumRoleArn",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudConnectQsModulePropsParametersIridiumRoleArn:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon Resource Number (ARN) of the role in the Iridium AWS account.

        :param description: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsParametersIridiumRoleArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersIridiumRoleArn#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersIridiumRoleArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParametersIridiumRoleArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-originated queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated confirmation queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated error queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "mobile_originated_sqs_queue": "mobileOriginatedSqsQueue",
        "mobile_terminated_confirmation_sqs_queue": "mobileTerminatedConfirmationSqsQueue",
        "mobile_terminated_error_sqs_queue": "mobileTerminatedErrorSqsQueue",
        "mobile_terminated_sqs_queue": "mobileTerminatedSqsQueue",
        "sqs_cross_account_role": "sqsCrossAccountRole",
        "sqs_queue_cross_account_policy": "sqsQueueCrossAccountPolicy",
    },
)
class CfnCloudConnectQsModulePropsResources:
    def __init__(
        self,
        *,
        mobile_originated_sqs_queue: typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue"] = None,
        mobile_terminated_confirmation_sqs_queue: typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue"] = None,
        mobile_terminated_error_sqs_queue: typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue"] = None,
        mobile_terminated_sqs_queue: typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue"] = None,
        sqs_cross_account_role: typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole"] = None,
        sqs_queue_cross_account_policy: typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy"] = None,
    ) -> None:
        '''
        :param mobile_originated_sqs_queue: 
        :param mobile_terminated_confirmation_sqs_queue: 
        :param mobile_terminated_error_sqs_queue: 
        :param mobile_terminated_sqs_queue: 
        :param sqs_cross_account_role: 
        :param sqs_queue_cross_account_policy: 

        :schema: CfnCloudConnectQsModulePropsResources
        '''
        if isinstance(mobile_originated_sqs_queue, dict):
            mobile_originated_sqs_queue = CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue(**mobile_originated_sqs_queue)
        if isinstance(mobile_terminated_confirmation_sqs_queue, dict):
            mobile_terminated_confirmation_sqs_queue = CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue(**mobile_terminated_confirmation_sqs_queue)
        if isinstance(mobile_terminated_error_sqs_queue, dict):
            mobile_terminated_error_sqs_queue = CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue(**mobile_terminated_error_sqs_queue)
        if isinstance(mobile_terminated_sqs_queue, dict):
            mobile_terminated_sqs_queue = CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue(**mobile_terminated_sqs_queue)
        if isinstance(sqs_cross_account_role, dict):
            sqs_cross_account_role = CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole(**sqs_cross_account_role)
        if isinstance(sqs_queue_cross_account_policy, dict):
            sqs_queue_cross_account_policy = CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy(**sqs_queue_cross_account_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if mobile_originated_sqs_queue is not None:
            self._values["mobile_originated_sqs_queue"] = mobile_originated_sqs_queue
        if mobile_terminated_confirmation_sqs_queue is not None:
            self._values["mobile_terminated_confirmation_sqs_queue"] = mobile_terminated_confirmation_sqs_queue
        if mobile_terminated_error_sqs_queue is not None:
            self._values["mobile_terminated_error_sqs_queue"] = mobile_terminated_error_sqs_queue
        if mobile_terminated_sqs_queue is not None:
            self._values["mobile_terminated_sqs_queue"] = mobile_terminated_sqs_queue
        if sqs_cross_account_role is not None:
            self._values["sqs_cross_account_role"] = sqs_cross_account_role
        if sqs_queue_cross_account_policy is not None:
            self._values["sqs_queue_cross_account_policy"] = sqs_queue_cross_account_policy

    @builtins.property
    def mobile_originated_sqs_queue(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#MobileOriginatedSQSQueue
        '''
        result = self._values.get("mobile_originated_sqs_queue")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue"], result)

    @builtins.property
    def mobile_terminated_confirmation_sqs_queue(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#MobileTerminatedConfirmationSQSQueue
        '''
        result = self._values.get("mobile_terminated_confirmation_sqs_queue")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue"], result)

    @builtins.property
    def mobile_terminated_error_sqs_queue(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#MobileTerminatedErrorSQSQueue
        '''
        result = self._values.get("mobile_terminated_error_sqs_queue")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue"], result)

    @builtins.property
    def mobile_terminated_sqs_queue(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#MobileTerminatedSQSQueue
        '''
        result = self._values.get("mobile_terminated_sqs_queue")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue"], result)

    @builtins.property
    def sqs_cross_account_role(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#SQSCrossAccountRole
        '''
        result = self._values.get("sqs_cross_account_role")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole"], result)

    @builtins.property
    def sqs_queue_cross_account_policy(
        self,
    ) -> typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy"]:
        '''
        :schema: CfnCloudConnectQsModulePropsResources#SQSQueueCrossAccountPolicy
        '''
        result = self._values.get("sqs_queue_cross_account_policy")
        return typing.cast(typing.Optional["CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudConnectQsModule",
    "CfnCloudConnectQsModuleProps",
    "CfnCloudConnectQsModulePropsParameters",
    "CfnCloudConnectQsModulePropsParametersIridiumRoleArn",
    "CfnCloudConnectQsModulePropsParametersMobileOriginatedQueueName",
    "CfnCloudConnectQsModulePropsParametersMobileTerminatedConfirmationQueueName",
    "CfnCloudConnectQsModulePropsParametersMobileTerminatedErrorQueueName",
    "CfnCloudConnectQsModulePropsParametersMobileTerminatedQueueName",
    "CfnCloudConnectQsModulePropsResources",
    "CfnCloudConnectQsModulePropsResourcesMobileOriginatedSqsQueue",
    "CfnCloudConnectQsModulePropsResourcesMobileTerminatedConfirmationSqsQueue",
    "CfnCloudConnectQsModulePropsResourcesMobileTerminatedErrorSqsQueue",
    "CfnCloudConnectQsModulePropsResourcesMobileTerminatedSqsQueue",
    "CfnCloudConnectQsModulePropsResourcesSqsCrossAccountRole",
    "CfnCloudConnectQsModulePropsResourcesSqsQueueCrossAccountPolicy",
]

publication.publish()
