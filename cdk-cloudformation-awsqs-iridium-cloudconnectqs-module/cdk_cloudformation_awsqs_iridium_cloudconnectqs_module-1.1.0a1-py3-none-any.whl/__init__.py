'''
# AWS CDK CloudFormation Constructs for AWSQS::Iridium::CloudConnectQS::MODULE

Schema for Module Fragment of type AWSQS::Iridium::CloudConnectQS::MODULE

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
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModule",
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
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``AWSQS::Iridium::CloudConnectQS::MODULE``.

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
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type AWSQS::Iridium::CloudConnectQS::MODULE.

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
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "iridium_role_arn": "iridiumRoleArn",
        "mobile_originated_queue_name": "mobileOriginatedQueueName",
        "mobile_terminated_confirmation_queue_name": "mobileTerminatedConfirmationQueueName",
        "mobile_terminated_error_queue_name": "mobileTerminatedErrorQueueName",
        "mobile_terminated_queue_name": "mobileTerminatedQueueName",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        iridium_role_arn: typing.Optional["CfnModulePropsParametersIridiumRoleArn"] = None,
        mobile_originated_queue_name: typing.Optional["CfnModulePropsParametersMobileOriginatedQueueName"] = None,
        mobile_terminated_confirmation_queue_name: typing.Optional["CfnModulePropsParametersMobileTerminatedConfirmationQueueName"] = None,
        mobile_terminated_error_queue_name: typing.Optional["CfnModulePropsParametersMobileTerminatedErrorQueueName"] = None,
        mobile_terminated_queue_name: typing.Optional["CfnModulePropsParametersMobileTerminatedQueueName"] = None,
    ) -> None:
        '''
        :param iridium_role_arn: Amazon Resource Number (ARN) of the role in the Iridium AWS account.
        :param mobile_originated_queue_name: Name of the mobile-originated queue in Amazon SQS.
        :param mobile_terminated_confirmation_queue_name: Name of the mobile-terminated confirmation queue in Amazon SQS.
        :param mobile_terminated_error_queue_name: Name of the mobile-terminated error queue in Amazon SQS.
        :param mobile_terminated_queue_name: Name of the mobile-terminated queue in Amazon SQS.

        :schema: CfnModulePropsParameters
        '''
        if isinstance(iridium_role_arn, dict):
            iridium_role_arn = CfnModulePropsParametersIridiumRoleArn(**iridium_role_arn)
        if isinstance(mobile_originated_queue_name, dict):
            mobile_originated_queue_name = CfnModulePropsParametersMobileOriginatedQueueName(**mobile_originated_queue_name)
        if isinstance(mobile_terminated_confirmation_queue_name, dict):
            mobile_terminated_confirmation_queue_name = CfnModulePropsParametersMobileTerminatedConfirmationQueueName(**mobile_terminated_confirmation_queue_name)
        if isinstance(mobile_terminated_error_queue_name, dict):
            mobile_terminated_error_queue_name = CfnModulePropsParametersMobileTerminatedErrorQueueName(**mobile_terminated_error_queue_name)
        if isinstance(mobile_terminated_queue_name, dict):
            mobile_terminated_queue_name = CfnModulePropsParametersMobileTerminatedQueueName(**mobile_terminated_queue_name)
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
    ) -> typing.Optional["CfnModulePropsParametersIridiumRoleArn"]:
        '''Amazon Resource Number (ARN) of the role in the Iridium AWS account.

        :schema: CfnModulePropsParameters#IridiumRoleARN
        '''
        result = self._values.get("iridium_role_arn")
        return typing.cast(typing.Optional["CfnModulePropsParametersIridiumRoleArn"], result)

    @builtins.property
    def mobile_originated_queue_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMobileOriginatedQueueName"]:
        '''Name of the mobile-originated queue in Amazon SQS.

        :schema: CfnModulePropsParameters#MobileOriginatedQueueName
        '''
        result = self._values.get("mobile_originated_queue_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersMobileOriginatedQueueName"], result)

    @builtins.property
    def mobile_terminated_confirmation_queue_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMobileTerminatedConfirmationQueueName"]:
        '''Name of the mobile-terminated confirmation queue in Amazon SQS.

        :schema: CfnModulePropsParameters#MobileTerminatedConfirmationQueueName
        '''
        result = self._values.get("mobile_terminated_confirmation_queue_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersMobileTerminatedConfirmationQueueName"], result)

    @builtins.property
    def mobile_terminated_error_queue_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMobileTerminatedErrorQueueName"]:
        '''Name of the mobile-terminated error queue in Amazon SQS.

        :schema: CfnModulePropsParameters#MobileTerminatedErrorQueueName
        '''
        result = self._values.get("mobile_terminated_error_queue_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersMobileTerminatedErrorQueueName"], result)

    @builtins.property
    def mobile_terminated_queue_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMobileTerminatedQueueName"]:
        '''Name of the mobile-terminated queue in Amazon SQS.

        :schema: CfnModulePropsParameters#MobileTerminatedQueueName
        '''
        result = self._values.get("mobile_terminated_queue_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersMobileTerminatedQueueName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParametersIridiumRoleArn",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersIridiumRoleArn:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon Resource Number (ARN) of the role in the Iridium AWS account.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersIridiumRoleArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersIridiumRoleArn#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersIridiumRoleArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersIridiumRoleArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParametersMobileOriginatedQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMobileOriginatedQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-originated queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMobileOriginatedQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileOriginatedQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileOriginatedQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMobileOriginatedQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParametersMobileTerminatedConfirmationQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMobileTerminatedConfirmationQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated confirmation queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMobileTerminatedConfirmationQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedConfirmationQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedConfirmationQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMobileTerminatedConfirmationQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParametersMobileTerminatedErrorQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMobileTerminatedErrorQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated error queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMobileTerminatedErrorQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedErrorQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedErrorQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMobileTerminatedErrorQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsParametersMobileTerminatedQueueName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMobileTerminatedQueueName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the mobile-terminated queue in Amazon SQS.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMobileTerminatedQueueName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedQueueName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMobileTerminatedQueueName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMobileTerminatedQueueName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResources",
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
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        mobile_originated_sqs_queue: typing.Optional["CfnModulePropsResourcesMobileOriginatedSqsQueue"] = None,
        mobile_terminated_confirmation_sqs_queue: typing.Optional["CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue"] = None,
        mobile_terminated_error_sqs_queue: typing.Optional["CfnModulePropsResourcesMobileTerminatedErrorSqsQueue"] = None,
        mobile_terminated_sqs_queue: typing.Optional["CfnModulePropsResourcesMobileTerminatedSqsQueue"] = None,
        sqs_cross_account_role: typing.Optional["CfnModulePropsResourcesSqsCrossAccountRole"] = None,
        sqs_queue_cross_account_policy: typing.Optional["CfnModulePropsResourcesSqsQueueCrossAccountPolicy"] = None,
    ) -> None:
        '''
        :param mobile_originated_sqs_queue: 
        :param mobile_terminated_confirmation_sqs_queue: 
        :param mobile_terminated_error_sqs_queue: 
        :param mobile_terminated_sqs_queue: 
        :param sqs_cross_account_role: 
        :param sqs_queue_cross_account_policy: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(mobile_originated_sqs_queue, dict):
            mobile_originated_sqs_queue = CfnModulePropsResourcesMobileOriginatedSqsQueue(**mobile_originated_sqs_queue)
        if isinstance(mobile_terminated_confirmation_sqs_queue, dict):
            mobile_terminated_confirmation_sqs_queue = CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue(**mobile_terminated_confirmation_sqs_queue)
        if isinstance(mobile_terminated_error_sqs_queue, dict):
            mobile_terminated_error_sqs_queue = CfnModulePropsResourcesMobileTerminatedErrorSqsQueue(**mobile_terminated_error_sqs_queue)
        if isinstance(mobile_terminated_sqs_queue, dict):
            mobile_terminated_sqs_queue = CfnModulePropsResourcesMobileTerminatedSqsQueue(**mobile_terminated_sqs_queue)
        if isinstance(sqs_cross_account_role, dict):
            sqs_cross_account_role = CfnModulePropsResourcesSqsCrossAccountRole(**sqs_cross_account_role)
        if isinstance(sqs_queue_cross_account_policy, dict):
            sqs_queue_cross_account_policy = CfnModulePropsResourcesSqsQueueCrossAccountPolicy(**sqs_queue_cross_account_policy)
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
    ) -> typing.Optional["CfnModulePropsResourcesMobileOriginatedSqsQueue"]:
        '''
        :schema: CfnModulePropsResources#MobileOriginatedSQSQueue
        '''
        result = self._values.get("mobile_originated_sqs_queue")
        return typing.cast(typing.Optional["CfnModulePropsResourcesMobileOriginatedSqsQueue"], result)

    @builtins.property
    def mobile_terminated_confirmation_sqs_queue(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue"]:
        '''
        :schema: CfnModulePropsResources#MobileTerminatedConfirmationSQSQueue
        '''
        result = self._values.get("mobile_terminated_confirmation_sqs_queue")
        return typing.cast(typing.Optional["CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue"], result)

    @builtins.property
    def mobile_terminated_error_sqs_queue(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesMobileTerminatedErrorSqsQueue"]:
        '''
        :schema: CfnModulePropsResources#MobileTerminatedErrorSQSQueue
        '''
        result = self._values.get("mobile_terminated_error_sqs_queue")
        return typing.cast(typing.Optional["CfnModulePropsResourcesMobileTerminatedErrorSqsQueue"], result)

    @builtins.property
    def mobile_terminated_sqs_queue(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesMobileTerminatedSqsQueue"]:
        '''
        :schema: CfnModulePropsResources#MobileTerminatedSQSQueue
        '''
        result = self._values.get("mobile_terminated_sqs_queue")
        return typing.cast(typing.Optional["CfnModulePropsResourcesMobileTerminatedSqsQueue"], result)

    @builtins.property
    def sqs_cross_account_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSqsCrossAccountRole"]:
        '''
        :schema: CfnModulePropsResources#SQSCrossAccountRole
        '''
        result = self._values.get("sqs_cross_account_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSqsCrossAccountRole"], result)

    @builtins.property
    def sqs_queue_cross_account_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSqsQueueCrossAccountPolicy"]:
        '''
        :schema: CfnModulePropsResources#SQSQueueCrossAccountPolicy
        '''
        result = self._values.get("sqs_queue_cross_account_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSqsQueueCrossAccountPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesMobileOriginatedSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesMobileOriginatedSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesMobileOriginatedSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesMobileOriginatedSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesMobileOriginatedSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesMobileOriginatedSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesMobileTerminatedErrorSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesMobileTerminatedErrorSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesMobileTerminatedErrorSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedErrorSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedErrorSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesMobileTerminatedErrorSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesMobileTerminatedSqsQueue",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesMobileTerminatedSqsQueue:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesMobileTerminatedSqsQueue
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedSqsQueue#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesMobileTerminatedSqsQueue#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesMobileTerminatedSqsQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesSqsCrossAccountRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSqsCrossAccountRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSqsCrossAccountRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSqsCrossAccountRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSqsCrossAccountRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSqsCrossAccountRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-iridium-cloudconnectqs-module.CfnModulePropsResourcesSqsQueueCrossAccountPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSqsQueueCrossAccountPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSqsQueueCrossAccountPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSqsQueueCrossAccountPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSqsQueueCrossAccountPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSqsQueueCrossAccountPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersIridiumRoleArn",
    "CfnModulePropsParametersMobileOriginatedQueueName",
    "CfnModulePropsParametersMobileTerminatedConfirmationQueueName",
    "CfnModulePropsParametersMobileTerminatedErrorQueueName",
    "CfnModulePropsParametersMobileTerminatedQueueName",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesMobileOriginatedSqsQueue",
    "CfnModulePropsResourcesMobileTerminatedConfirmationSqsQueue",
    "CfnModulePropsResourcesMobileTerminatedErrorSqsQueue",
    "CfnModulePropsResourcesMobileTerminatedSqsQueue",
    "CfnModulePropsResourcesSqsCrossAccountRole",
    "CfnModulePropsResourcesSqsQueueCrossAccountPolicy",
]

publication.publish()
