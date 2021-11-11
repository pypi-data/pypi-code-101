'''
# registry-test-resource1-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `REGISTRY::TEST::RESOURCE1::MODULE` v1.5.0.

## Description

Schema for Module Fragment of type REGISTRY::TEST::RESOURCE::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name REGISTRY::TEST::RESOURCE1::MODULE \
  --publisher-id 4686b5f994c8b12636b1af16ce88b8e2d2e75c8c \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/4686b5f994c8b12636b1af16ce88b8e2d2e75c8c/REGISTRY-TEST-RESOURCE1-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `REGISTRY::TEST::RESOURCE1::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fregistry-test-resource1-module+v1.5.0).
* Issues related to `REGISTRY::TEST::RESOURCE1::MODULE` should be reported to the [publisher](undefined).

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


class CfnResource1Module(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1Module",
):
    '''A CloudFormation ``REGISTRY::TEST::RESOURCE1::MODULE``.

    :cloudformationResource: REGISTRY::TEST::RESOURCE1::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnResource1ModulePropsParameters"] = None,
        resources: typing.Optional["CfnResource1ModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``REGISTRY::TEST::RESOURCE1::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnResource1ModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnResource1ModuleProps":
        '''Resource props.'''
        return typing.cast("CfnResource1ModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnResource1ModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnResource1ModulePropsParameters"] = None,
        resources: typing.Optional["CfnResource1ModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type REGISTRY::TEST::RESOURCE::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnResource1ModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnResource1ModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnResource1ModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnResource1ModulePropsParameters"]:
        '''
        :schema: CfnResource1ModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnResource1ModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnResource1ModulePropsResources"]:
        '''
        :schema: CfnResource1ModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnResource1ModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName"},
)
class CfnResource1ModulePropsParameters:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional["CfnResource1ModulePropsParametersBucketName"] = None,
    ) -> None:
        '''
        :param bucket_name: Name for the bucket.

        :schema: CfnResource1ModulePropsParameters
        '''
        if isinstance(bucket_name, dict):
            bucket_name = CfnResource1ModulePropsParametersBucketName(**bucket_name)
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name

    @builtins.property
    def bucket_name(
        self,
    ) -> typing.Optional["CfnResource1ModulePropsParametersBucketName"]:
        '''Name for the bucket.

        :schema: CfnResource1ModulePropsParameters#BucketName
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional["CfnResource1ModulePropsParametersBucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsParametersBucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnResource1ModulePropsParametersBucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name for the bucket.

        :param description: 
        :param type: 

        :schema: CfnResource1ModulePropsParametersBucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnResource1ModulePropsParametersBucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnResource1ModulePropsParametersBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsParametersBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket": "s3Bucket"},
)
class CfnResource1ModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional["CfnResource1ModulePropsResourcesS3Bucket"] = None,
    ) -> None:
        '''
        :param s3_bucket: 

        :schema: CfnResource1ModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnResource1ModulePropsResourcesS3Bucket(**s3_bucket)
        self._values: typing.Dict[str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnResource1ModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnResource1ModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnResource1ModulePropsResourcesS3Bucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnResource1ModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnResource1ModulePropsResourcesS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnResource1ModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnResource1ModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnResource1Module",
    "CfnResource1ModuleProps",
    "CfnResource1ModulePropsParameters",
    "CfnResource1ModulePropsParametersBucketName",
    "CfnResource1ModulePropsResources",
    "CfnResource1ModulePropsResourcesS3Bucket",
]

publication.publish()
