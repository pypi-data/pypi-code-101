'''
# jfrog-vpc-multiaz-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Vpc::MultiAz::MODULE` v1.6.0.

## Description

Schema for Module Fragment of type JFrog::Vpc::MultiAz::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Vpc::MultiAz::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Vpc-MultiAz-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Vpc::MultiAz::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-vpc-multiaz-module+v1.6.0).
* Issues related to `JFrog::Vpc::MultiAz::MODULE` should be reported to the [publisher](undefined).

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


class CfnMultiAzModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModule",
):
    '''A CloudFormation ``JFrog::Vpc::MultiAz::MODULE``.

    :cloudformationResource: JFrog::Vpc::MultiAz::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnMultiAzModulePropsParameters"] = None,
        resources: typing.Optional["CfnMultiAzModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Vpc::MultiAz::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnMultiAzModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMultiAzModuleProps":
        '''Resource props.'''
        return typing.cast("CfnMultiAzModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnMultiAzModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnMultiAzModulePropsParameters"] = None,
        resources: typing.Optional["CfnMultiAzModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type JFrog::Vpc::MultiAz::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnMultiAzModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnMultiAzModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnMultiAzModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnMultiAzModulePropsParameters"]:
        '''
        :schema: CfnMultiAzModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnMultiAzModulePropsResources"]:
        '''
        :schema: CfnMultiAzModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone1": "availabilityZone1",
        "availability_zone2": "availabilityZone2",
        "create_nat_gateways": "createNatGateways",
        "create_private_subnets": "createPrivateSubnets",
        "create_public_subnets": "createPublicSubnets",
        "private_subnet1_acidr": "privateSubnet1Acidr",
        "private_subnet2_acidr": "privateSubnet2Acidr",
        "private_subnet_a_tag1": "privateSubnetATag1",
        "private_subnet_a_tag2": "privateSubnetATag2",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet_tag1": "publicSubnetTag1",
        "public_subnet_tag2": "publicSubnetTag2",
        "vpccidr": "vpccidr",
        "vpc_tenancy": "vpcTenancy",
    },
)
class CfnMultiAzModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zone1: typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone2"] = None,
        create_nat_gateways: typing.Optional["CfnMultiAzModulePropsParametersCreateNatGateways"] = None,
        create_private_subnets: typing.Optional["CfnMultiAzModulePropsParametersCreatePrivateSubnets"] = None,
        create_public_subnets: typing.Optional["CfnMultiAzModulePropsParametersCreatePublicSubnets"] = None,
        private_subnet1_acidr: typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet1Acidr"] = None,
        private_subnet2_acidr: typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet2Acidr"] = None,
        private_subnet_a_tag1: typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag1"] = None,
        private_subnet_a_tag2: typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag2"] = None,
        public_subnet1_cidr: typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet_tag1: typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag1"] = None,
        public_subnet_tag2: typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag2"] = None,
        vpccidr: typing.Optional["CfnMultiAzModulePropsParametersVpccidr"] = None,
        vpc_tenancy: typing.Optional["CfnMultiAzModulePropsParametersVpcTenancy"] = None,
    ) -> None:
        '''
        :param availability_zone1: Availability Zone 1 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param availability_zone2: Availability Zone 2 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param create_nat_gateways: Set to false when creating only private subnets. If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.
        :param create_private_subnets: Set to false to create only public subnets. If false, the CIDR parameters for ALL private subnets will be ignored.
        :param create_public_subnets: Set to false to create only private subnets. If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored
        :param private_subnet1_acidr: CIDR block for private subnet 1A located in Availability Zone 1.
        :param private_subnet2_acidr: CIDR block for private subnet 2A located in Availability Zone 2.
        :param private_subnet_a_tag1: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_a_tag2: tag to add to private subnets A, in format Key=Value (Optional).
        :param public_subnet1_cidr: CIDR block for the public DMZ subnet 1 located in Availability Zone 1.
        :param public_subnet2_cidr: CIDR block for the public DMZ subnet 2 located in Availability Zone 2.
        :param public_subnet_tag1: tag to add to public subnets, in format Key=Value (Optional).
        :param public_subnet_tag2: tag to add to public subnets, in format Key=Value (Optional).
        :param vpccidr: CIDR block for the VPC.
        :param vpc_tenancy: The allowed tenancy of instances launched into the VPC.

        :schema: CfnMultiAzModulePropsParameters
        '''
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnMultiAzModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnMultiAzModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(create_nat_gateways, dict):
            create_nat_gateways = CfnMultiAzModulePropsParametersCreateNatGateways(**create_nat_gateways)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnMultiAzModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_public_subnets, dict):
            create_public_subnets = CfnMultiAzModulePropsParametersCreatePublicSubnets(**create_public_subnets)
        if isinstance(private_subnet1_acidr, dict):
            private_subnet1_acidr = CfnMultiAzModulePropsParametersPrivateSubnet1Acidr(**private_subnet1_acidr)
        if isinstance(private_subnet2_acidr, dict):
            private_subnet2_acidr = CfnMultiAzModulePropsParametersPrivateSubnet2Acidr(**private_subnet2_acidr)
        if isinstance(private_subnet_a_tag1, dict):
            private_subnet_a_tag1 = CfnMultiAzModulePropsParametersPrivateSubnetATag1(**private_subnet_a_tag1)
        if isinstance(private_subnet_a_tag2, dict):
            private_subnet_a_tag2 = CfnMultiAzModulePropsParametersPrivateSubnetATag2(**private_subnet_a_tag2)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnMultiAzModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnMultiAzModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet_tag1, dict):
            public_subnet_tag1 = CfnMultiAzModulePropsParametersPublicSubnetTag1(**public_subnet_tag1)
        if isinstance(public_subnet_tag2, dict):
            public_subnet_tag2 = CfnMultiAzModulePropsParametersPublicSubnetTag2(**public_subnet_tag2)
        if isinstance(vpccidr, dict):
            vpccidr = CfnMultiAzModulePropsParametersVpccidr(**vpccidr)
        if isinstance(vpc_tenancy, dict):
            vpc_tenancy = CfnMultiAzModulePropsParametersVpcTenancy(**vpc_tenancy)
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_zone1 is not None:
            self._values["availability_zone1"] = availability_zone1
        if availability_zone2 is not None:
            self._values["availability_zone2"] = availability_zone2
        if create_nat_gateways is not None:
            self._values["create_nat_gateways"] = create_nat_gateways
        if create_private_subnets is not None:
            self._values["create_private_subnets"] = create_private_subnets
        if create_public_subnets is not None:
            self._values["create_public_subnets"] = create_public_subnets
        if private_subnet1_acidr is not None:
            self._values["private_subnet1_acidr"] = private_subnet1_acidr
        if private_subnet2_acidr is not None:
            self._values["private_subnet2_acidr"] = private_subnet2_acidr
        if private_subnet_a_tag1 is not None:
            self._values["private_subnet_a_tag1"] = private_subnet_a_tag1
        if private_subnet_a_tag2 is not None:
            self._values["private_subnet_a_tag2"] = private_subnet_a_tag2
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet_tag1 is not None:
            self._values["public_subnet_tag1"] = public_subnet_tag1
        if public_subnet_tag2 is not None:
            self._values["public_subnet_tag2"] = public_subnet_tag2
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr
        if vpc_tenancy is not None:
            self._values["vpc_tenancy"] = vpc_tenancy

    @builtins.property
    def availability_zone1(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnMultiAzModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnMultiAzModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def create_nat_gateways(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersCreateNatGateways"]:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :schema: CfnMultiAzModulePropsParameters#CreateNATGateways
        '''
        result = self._values.get("create_nat_gateways")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersCreateNatGateways"], result)

    @builtins.property
    def create_private_subnets(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersCreatePrivateSubnets"]:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :schema: CfnMultiAzModulePropsParameters#CreatePrivateSubnets
        '''
        result = self._values.get("create_private_subnets")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersCreatePrivateSubnets"], result)

    @builtins.property
    def create_public_subnets(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersCreatePublicSubnets"]:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :schema: CfnMultiAzModulePropsParameters#CreatePublicSubnets
        '''
        result = self._values.get("create_public_subnets")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersCreatePublicSubnets"], result)

    @builtins.property
    def private_subnet1_acidr(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet1Acidr"]:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :schema: CfnMultiAzModulePropsParameters#PrivateSubnet1ACIDR
        '''
        result = self._values.get("private_subnet1_acidr")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet1Acidr"], result)

    @builtins.property
    def private_subnet2_acidr(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet2Acidr"]:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :schema: CfnMultiAzModulePropsParameters#PrivateSubnet2ACIDR
        '''
        result = self._values.get("private_subnet2_acidr")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnet2Acidr"], result)

    @builtins.property
    def private_subnet_a_tag1(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag1"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnMultiAzModulePropsParameters#PrivateSubnetATag1
        '''
        result = self._values.get("private_subnet_a_tag1")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag1"], result)

    @builtins.property
    def private_subnet_a_tag2(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag2"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnMultiAzModulePropsParameters#PrivateSubnetATag2
        '''
        result = self._values.get("private_subnet_a_tag2")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPrivateSubnetATag2"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :schema: CfnMultiAzModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :schema: CfnMultiAzModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet_tag1(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag1"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnMultiAzModulePropsParameters#PublicSubnetTag1
        '''
        result = self._values.get("public_subnet_tag1")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag1"], result)

    @builtins.property
    def public_subnet_tag2(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag2"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnMultiAzModulePropsParameters#PublicSubnetTag2
        '''
        result = self._values.get("public_subnet_tag2")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersPublicSubnetTag2"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnMultiAzModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        :schema: CfnMultiAzModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersVpccidr"], result)

    @builtins.property
    def vpc_tenancy(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsParametersVpcTenancy"]:
        '''The allowed tenancy of instances launched into the VPC.

        :schema: CfnMultiAzModulePropsParameters#VPCTenancy
        '''
        result = self._values.get("vpc_tenancy")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsParametersVpcTenancy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersAvailabilityZone1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersAvailabilityZone2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersCreateNatGateways",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersCreateNatGateways:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersCreateNatGateways
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreateNatGateways#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreateNatGateways#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersCreateNatGateways(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersCreatePrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersCreatePrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersCreatePrivateSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreatePrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreatePrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersCreatePrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersCreatePublicSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersCreatePublicSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersCreatePublicSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreatePublicSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersCreatePublicSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersCreatePublicSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPrivateSubnet1Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPrivateSubnet1Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPrivateSubnet1Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnet1Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnet1Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPrivateSubnet1Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPrivateSubnet2Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPrivateSubnet2Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPrivateSubnet2Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnet2Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnet2Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPrivateSubnet2Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPrivateSubnetATag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPrivateSubnetATag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPrivateSubnetATag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPrivateSubnetATag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPrivateSubnetATag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPrivateSubnetATag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPrivateSubnetATag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPublicSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPublicSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPublicSubnetTag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPublicSubnetTag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPublicSubnetTag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersPublicSubnetTag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersPublicSubnetTag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersPublicSubnetTag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersPublicSubnetTag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersVpcTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersVpcTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The allowed tenancy of instances launched into the VPC.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersVpcTenancy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersVpcTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersVpcTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersVpcTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnMultiAzModulePropsParametersVpccidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnMultiAzModulePropsParametersVpccidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersVpccidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnMultiAzModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "dhcp_options": "dhcpOptions",
        "internet_gateway": "internetGateway",
        "nat1_eip": "nat1Eip",
        "nat2_eip": "nat2Eip",
        "nat_gateway1": "natGateway1",
        "nat_gateway2": "natGateway2",
        "private_subnet1_a": "privateSubnet1A",
        "private_subnet1_a_route": "privateSubnet1ARoute",
        "private_subnet1_a_route_table": "privateSubnet1ARouteTable",
        "private_subnet1_a_route_table_association": "privateSubnet1ARouteTableAssociation",
        "private_subnet2_a": "privateSubnet2A",
        "private_subnet2_a_route": "privateSubnet2ARoute",
        "private_subnet2_a_route_table": "privateSubnet2ARouteTable",
        "private_subnet2_a_route_table_association": "privateSubnet2ARouteTableAssociation",
        "public_subnet1": "publicSubnet1",
        "public_subnet1_route_table_association": "publicSubnet1RouteTableAssociation",
        "public_subnet2": "publicSubnet2",
        "public_subnet2_route_table_association": "publicSubnet2RouteTableAssociation",
        "public_subnet_route": "publicSubnetRoute",
        "public_subnet_route_table": "publicSubnetRouteTable",
        "s3_vpc_endpoint": "s3VpcEndpoint",
        "vpc": "vpc",
        "vpcdhcp_options_association": "vpcdhcpOptionsAssociation",
        "vpc_gateway_attachment": "vpcGatewayAttachment",
    },
)
class CfnMultiAzModulePropsResources:
    def __init__(
        self,
        *,
        dhcp_options: typing.Optional["CfnMultiAzModulePropsResourcesDhcpOptions"] = None,
        internet_gateway: typing.Optional["CfnMultiAzModulePropsResourcesInternetGateway"] = None,
        nat1_eip: typing.Optional["CfnMultiAzModulePropsResourcesNat1Eip"] = None,
        nat2_eip: typing.Optional["CfnMultiAzModulePropsResourcesNat2Eip"] = None,
        nat_gateway1: typing.Optional["CfnMultiAzModulePropsResourcesNatGateway1"] = None,
        nat_gateway2: typing.Optional["CfnMultiAzModulePropsResourcesNatGateway2"] = None,
        private_subnet1_a: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1A"] = None,
        private_subnet1_a_route: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute"] = None,
        private_subnet1_a_route_table: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable"] = None,
        private_subnet1_a_route_table_association: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation"] = None,
        private_subnet2_a: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2A"] = None,
        private_subnet2_a_route: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute"] = None,
        private_subnet2_a_route_table: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable"] = None,
        private_subnet2_a_route_table_association: typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation"] = None,
        public_subnet1: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1"] = None,
        public_subnet1_route_table_association: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation"] = None,
        public_subnet2: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2"] = None,
        public_subnet2_route_table_association: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation"] = None,
        public_subnet_route: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRoute"] = None,
        public_subnet_route_table: typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRouteTable"] = None,
        s3_vpc_endpoint: typing.Optional["CfnMultiAzModulePropsResourcesS3VpcEndpoint"] = None,
        vpc: typing.Optional["CfnMultiAzModulePropsResourcesVpc"] = None,
        vpcdhcp_options_association: typing.Optional["CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation"] = None,
        vpc_gateway_attachment: typing.Optional["CfnMultiAzModulePropsResourcesVpcGatewayAttachment"] = None,
    ) -> None:
        '''
        :param dhcp_options: 
        :param internet_gateway: 
        :param nat1_eip: 
        :param nat2_eip: 
        :param nat_gateway1: 
        :param nat_gateway2: 
        :param private_subnet1_a: 
        :param private_subnet1_a_route: 
        :param private_subnet1_a_route_table: 
        :param private_subnet1_a_route_table_association: 
        :param private_subnet2_a: 
        :param private_subnet2_a_route: 
        :param private_subnet2_a_route_table: 
        :param private_subnet2_a_route_table_association: 
        :param public_subnet1: 
        :param public_subnet1_route_table_association: 
        :param public_subnet2: 
        :param public_subnet2_route_table_association: 
        :param public_subnet_route: 
        :param public_subnet_route_table: 
        :param s3_vpc_endpoint: 
        :param vpc: 
        :param vpcdhcp_options_association: 
        :param vpc_gateway_attachment: 

        :schema: CfnMultiAzModulePropsResources
        '''
        if isinstance(dhcp_options, dict):
            dhcp_options = CfnMultiAzModulePropsResourcesDhcpOptions(**dhcp_options)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnMultiAzModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(nat1_eip, dict):
            nat1_eip = CfnMultiAzModulePropsResourcesNat1Eip(**nat1_eip)
        if isinstance(nat2_eip, dict):
            nat2_eip = CfnMultiAzModulePropsResourcesNat2Eip(**nat2_eip)
        if isinstance(nat_gateway1, dict):
            nat_gateway1 = CfnMultiAzModulePropsResourcesNatGateway1(**nat_gateway1)
        if isinstance(nat_gateway2, dict):
            nat_gateway2 = CfnMultiAzModulePropsResourcesNatGateway2(**nat_gateway2)
        if isinstance(private_subnet1_a, dict):
            private_subnet1_a = CfnMultiAzModulePropsResourcesPrivateSubnet1A(**private_subnet1_a)
        if isinstance(private_subnet1_a_route, dict):
            private_subnet1_a_route = CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute(**private_subnet1_a_route)
        if isinstance(private_subnet1_a_route_table, dict):
            private_subnet1_a_route_table = CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable(**private_subnet1_a_route_table)
        if isinstance(private_subnet1_a_route_table_association, dict):
            private_subnet1_a_route_table_association = CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation(**private_subnet1_a_route_table_association)
        if isinstance(private_subnet2_a, dict):
            private_subnet2_a = CfnMultiAzModulePropsResourcesPrivateSubnet2A(**private_subnet2_a)
        if isinstance(private_subnet2_a_route, dict):
            private_subnet2_a_route = CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute(**private_subnet2_a_route)
        if isinstance(private_subnet2_a_route_table, dict):
            private_subnet2_a_route_table = CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable(**private_subnet2_a_route_table)
        if isinstance(private_subnet2_a_route_table_association, dict):
            private_subnet2_a_route_table_association = CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation(**private_subnet2_a_route_table_association)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnMultiAzModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnMultiAzModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnMultiAzModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnMultiAzModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(s3_vpc_endpoint, dict):
            s3_vpc_endpoint = CfnMultiAzModulePropsResourcesS3VpcEndpoint(**s3_vpc_endpoint)
        if isinstance(vpc, dict):
            vpc = CfnMultiAzModulePropsResourcesVpc(**vpc)
        if isinstance(vpcdhcp_options_association, dict):
            vpcdhcp_options_association = CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation(**vpcdhcp_options_association)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnMultiAzModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
        self._values: typing.Dict[str, typing.Any] = {}
        if dhcp_options is not None:
            self._values["dhcp_options"] = dhcp_options
        if internet_gateway is not None:
            self._values["internet_gateway"] = internet_gateway
        if nat1_eip is not None:
            self._values["nat1_eip"] = nat1_eip
        if nat2_eip is not None:
            self._values["nat2_eip"] = nat2_eip
        if nat_gateway1 is not None:
            self._values["nat_gateway1"] = nat_gateway1
        if nat_gateway2 is not None:
            self._values["nat_gateway2"] = nat_gateway2
        if private_subnet1_a is not None:
            self._values["private_subnet1_a"] = private_subnet1_a
        if private_subnet1_a_route is not None:
            self._values["private_subnet1_a_route"] = private_subnet1_a_route
        if private_subnet1_a_route_table is not None:
            self._values["private_subnet1_a_route_table"] = private_subnet1_a_route_table
        if private_subnet1_a_route_table_association is not None:
            self._values["private_subnet1_a_route_table_association"] = private_subnet1_a_route_table_association
        if private_subnet2_a is not None:
            self._values["private_subnet2_a"] = private_subnet2_a
        if private_subnet2_a_route is not None:
            self._values["private_subnet2_a_route"] = private_subnet2_a_route
        if private_subnet2_a_route_table is not None:
            self._values["private_subnet2_a_route_table"] = private_subnet2_a_route_table
        if private_subnet2_a_route_table_association is not None:
            self._values["private_subnet2_a_route_table_association"] = private_subnet2_a_route_table_association
        if public_subnet1 is not None:
            self._values["public_subnet1"] = public_subnet1
        if public_subnet1_route_table_association is not None:
            self._values["public_subnet1_route_table_association"] = public_subnet1_route_table_association
        if public_subnet2 is not None:
            self._values["public_subnet2"] = public_subnet2
        if public_subnet2_route_table_association is not None:
            self._values["public_subnet2_route_table_association"] = public_subnet2_route_table_association
        if public_subnet_route is not None:
            self._values["public_subnet_route"] = public_subnet_route
        if public_subnet_route_table is not None:
            self._values["public_subnet_route_table"] = public_subnet_route_table
        if s3_vpc_endpoint is not None:
            self._values["s3_vpc_endpoint"] = s3_vpc_endpoint
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpcdhcp_options_association is not None:
            self._values["vpcdhcp_options_association"] = vpcdhcp_options_association
        if vpc_gateway_attachment is not None:
            self._values["vpc_gateway_attachment"] = vpc_gateway_attachment

    @builtins.property
    def dhcp_options(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesDhcpOptions"]:
        '''
        :schema: CfnMultiAzModulePropsResources#DHCPOptions
        '''
        result = self._values.get("dhcp_options")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesDhcpOptions"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnMultiAzModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def nat1_eip(self) -> typing.Optional["CfnMultiAzModulePropsResourcesNat1Eip"]:
        '''
        :schema: CfnMultiAzModulePropsResources#NAT1EIP
        '''
        result = self._values.get("nat1_eip")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesNat1Eip"], result)

    @builtins.property
    def nat2_eip(self) -> typing.Optional["CfnMultiAzModulePropsResourcesNat2Eip"]:
        '''
        :schema: CfnMultiAzModulePropsResources#NAT2EIP
        '''
        result = self._values.get("nat2_eip")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesNat2Eip"], result)

    @builtins.property
    def nat_gateway1(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesNatGateway1"]:
        '''
        :schema: CfnMultiAzModulePropsResources#NATGateway1
        '''
        result = self._values.get("nat_gateway1")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesNatGateway1"], result)

    @builtins.property
    def nat_gateway2(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesNatGateway2"]:
        '''
        :schema: CfnMultiAzModulePropsResources#NATGateway2
        '''
        result = self._values.get("nat_gateway2")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesNatGateway2"], result)

    @builtins.property
    def private_subnet1_a(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1A"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet1A
        '''
        result = self._values.get("private_subnet1_a")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1A"], result)

    @builtins.property
    def private_subnet1_a_route(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet1ARoute
        '''
        result = self._values.get("private_subnet1_a_route")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute"], result)

    @builtins.property
    def private_subnet1_a_route_table(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet1ARouteTable
        '''
        result = self._values.get("private_subnet1_a_route_table")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable"], result)

    @builtins.property
    def private_subnet1_a_route_table_association(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet1ARouteTableAssociation
        '''
        result = self._values.get("private_subnet1_a_route_table_association")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet2_a(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2A"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet2A
        '''
        result = self._values.get("private_subnet2_a")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2A"], result)

    @builtins.property
    def private_subnet2_a_route(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet2ARoute
        '''
        result = self._values.get("private_subnet2_a_route")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute"], result)

    @builtins.property
    def private_subnet2_a_route_table(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet2ARouteTable
        '''
        result = self._values.get("private_subnet2_a_route_table")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable"], result)

    @builtins.property
    def private_subnet2_a_route_table_association(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PrivateSubnet2ARouteTableAssociation
        '''
        result = self._values.get("private_subnet2_a_route_table_association")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation"], result)

    @builtins.property
    def public_subnet1(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnMultiAzModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def s3_vpc_endpoint(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesS3VpcEndpoint"]:
        '''
        :schema: CfnMultiAzModulePropsResources#S3VPCEndpoint
        '''
        result = self._values.get("s3_vpc_endpoint")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesS3VpcEndpoint"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnMultiAzModulePropsResourcesVpc"]:
        '''
        :schema: CfnMultiAzModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesVpc"], result)

    @builtins.property
    def vpcdhcp_options_association(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation"]:
        '''
        :schema: CfnMultiAzModulePropsResources#VPCDHCPOptionsAssociation
        '''
        result = self._values.get("vpcdhcp_options_association")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnMultiAzModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnMultiAzModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnMultiAzModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesDhcpOptions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesDhcpOptions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesDhcpOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesDhcpOptions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesDhcpOptions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesDhcpOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesInternetGateway
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesNat1Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesNat1Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesNat1Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesNat1Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesNat1Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesNat1Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesNat2Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesNat2Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesNat2Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesNat2Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesNat2Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesNat2Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesNatGateway1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesNatGateway1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesNatGateway1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesNatGateway1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesNatGateway1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesNatGateway1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesNatGateway2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesNatGateway2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesNatGateway2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesNatGateway2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesNatGateway2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesNatGateway2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet1A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet1A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet1A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet2A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet2A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet2A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesS3VpcEndpoint",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesS3VpcEndpoint:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesS3VpcEndpoint
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesS3VpcEndpoint#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesS3VpcEndpoint#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesS3VpcEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesVpc
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesVpcGatewayAttachment
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMultiAzModule",
    "CfnMultiAzModuleProps",
    "CfnMultiAzModulePropsParameters",
    "CfnMultiAzModulePropsParametersAvailabilityZone1",
    "CfnMultiAzModulePropsParametersAvailabilityZone2",
    "CfnMultiAzModulePropsParametersCreateNatGateways",
    "CfnMultiAzModulePropsParametersCreatePrivateSubnets",
    "CfnMultiAzModulePropsParametersCreatePublicSubnets",
    "CfnMultiAzModulePropsParametersPrivateSubnet1Acidr",
    "CfnMultiAzModulePropsParametersPrivateSubnet2Acidr",
    "CfnMultiAzModulePropsParametersPrivateSubnetATag1",
    "CfnMultiAzModulePropsParametersPrivateSubnetATag2",
    "CfnMultiAzModulePropsParametersPublicSubnet1Cidr",
    "CfnMultiAzModulePropsParametersPublicSubnet2Cidr",
    "CfnMultiAzModulePropsParametersPublicSubnetTag1",
    "CfnMultiAzModulePropsParametersPublicSubnetTag2",
    "CfnMultiAzModulePropsParametersVpcTenancy",
    "CfnMultiAzModulePropsParametersVpccidr",
    "CfnMultiAzModulePropsResources",
    "CfnMultiAzModulePropsResourcesDhcpOptions",
    "CfnMultiAzModulePropsResourcesInternetGateway",
    "CfnMultiAzModulePropsResourcesNat1Eip",
    "CfnMultiAzModulePropsResourcesNat2Eip",
    "CfnMultiAzModulePropsResourcesNatGateway1",
    "CfnMultiAzModulePropsResourcesNatGateway2",
    "CfnMultiAzModulePropsResourcesPrivateSubnet1A",
    "CfnMultiAzModulePropsResourcesPrivateSubnet1ARoute",
    "CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTable",
    "CfnMultiAzModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    "CfnMultiAzModulePropsResourcesPrivateSubnet2A",
    "CfnMultiAzModulePropsResourcesPrivateSubnet2ARoute",
    "CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTable",
    "CfnMultiAzModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    "CfnMultiAzModulePropsResourcesPublicSubnet1",
    "CfnMultiAzModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnMultiAzModulePropsResourcesPublicSubnet2",
    "CfnMultiAzModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnMultiAzModulePropsResourcesPublicSubnetRoute",
    "CfnMultiAzModulePropsResourcesPublicSubnetRouteTable",
    "CfnMultiAzModulePropsResourcesS3VpcEndpoint",
    "CfnMultiAzModulePropsResourcesVpc",
    "CfnMultiAzModulePropsResourcesVpcGatewayAttachment",
    "CfnMultiAzModulePropsResourcesVpcdhcpOptionsAssociation",
]

publication.publish()
