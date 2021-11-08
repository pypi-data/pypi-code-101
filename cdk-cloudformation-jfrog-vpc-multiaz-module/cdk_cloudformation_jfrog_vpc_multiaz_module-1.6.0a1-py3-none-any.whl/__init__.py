'''
# AWS CDK CloudFormation Constructs for JFrog::Vpc::MultiAz::MODULE

Schema for Module Fragment of type JFrog::Vpc::MultiAz::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModule",
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
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Vpc::MultiAz::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Vpc::MultiAz::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParameters",
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
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zone1: typing.Optional["CfnModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnModulePropsParametersAvailabilityZone2"] = None,
        create_nat_gateways: typing.Optional["CfnModulePropsParametersCreateNatGateways"] = None,
        create_private_subnets: typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"] = None,
        create_public_subnets: typing.Optional["CfnModulePropsParametersCreatePublicSubnets"] = None,
        private_subnet1_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Acidr"] = None,
        private_subnet2_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Acidr"] = None,
        private_subnet_a_tag1: typing.Optional["CfnModulePropsParametersPrivateSubnetATag1"] = None,
        private_subnet_a_tag2: typing.Optional["CfnModulePropsParametersPrivateSubnetATag2"] = None,
        public_subnet1_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet_tag1: typing.Optional["CfnModulePropsParametersPublicSubnetTag1"] = None,
        public_subnet_tag2: typing.Optional["CfnModulePropsParametersPublicSubnetTag2"] = None,
        vpccidr: typing.Optional["CfnModulePropsParametersVpccidr"] = None,
        vpc_tenancy: typing.Optional["CfnModulePropsParametersVpcTenancy"] = None,
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

        :schema: CfnModulePropsParameters
        '''
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(create_nat_gateways, dict):
            create_nat_gateways = CfnModulePropsParametersCreateNatGateways(**create_nat_gateways)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_public_subnets, dict):
            create_public_subnets = CfnModulePropsParametersCreatePublicSubnets(**create_public_subnets)
        if isinstance(private_subnet1_acidr, dict):
            private_subnet1_acidr = CfnModulePropsParametersPrivateSubnet1Acidr(**private_subnet1_acidr)
        if isinstance(private_subnet2_acidr, dict):
            private_subnet2_acidr = CfnModulePropsParametersPrivateSubnet2Acidr(**private_subnet2_acidr)
        if isinstance(private_subnet_a_tag1, dict):
            private_subnet_a_tag1 = CfnModulePropsParametersPrivateSubnetATag1(**private_subnet_a_tag1)
        if isinstance(private_subnet_a_tag2, dict):
            private_subnet_a_tag2 = CfnModulePropsParametersPrivateSubnetATag2(**private_subnet_a_tag2)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet_tag1, dict):
            public_subnet_tag1 = CfnModulePropsParametersPublicSubnetTag1(**public_subnet_tag1)
        if isinstance(public_subnet_tag2, dict):
            public_subnet_tag2 = CfnModulePropsParametersPublicSubnetTag2(**public_subnet_tag2)
        if isinstance(vpccidr, dict):
            vpccidr = CfnModulePropsParametersVpccidr(**vpccidr)
        if isinstance(vpc_tenancy, dict):
            vpc_tenancy = CfnModulePropsParametersVpcTenancy(**vpc_tenancy)
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
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def create_nat_gateways(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreateNatGateways"]:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :schema: CfnModulePropsParameters#CreateNATGateways
        '''
        result = self._values.get("create_nat_gateways")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreateNatGateways"], result)

    @builtins.property
    def create_private_subnets(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"]:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :schema: CfnModulePropsParameters#CreatePrivateSubnets
        '''
        result = self._values.get("create_private_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"], result)

    @builtins.property
    def create_public_subnets(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreatePublicSubnets"]:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :schema: CfnModulePropsParameters#CreatePublicSubnets
        '''
        result = self._values.get("create_public_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreatePublicSubnets"], result)

    @builtins.property
    def private_subnet1_acidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Acidr"]:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :schema: CfnModulePropsParameters#PrivateSubnet1ACIDR
        '''
        result = self._values.get("private_subnet1_acidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Acidr"], result)

    @builtins.property
    def private_subnet2_acidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Acidr"]:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :schema: CfnModulePropsParameters#PrivateSubnet2ACIDR
        '''
        result = self._values.get("private_subnet2_acidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Acidr"], result)

    @builtins.property
    def private_subnet_a_tag1(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetATag1"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetATag1
        '''
        result = self._values.get("private_subnet_a_tag1")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetATag1"], result)

    @builtins.property
    def private_subnet_a_tag2(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetATag2"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetATag2
        '''
        result = self._values.get("private_subnet_a_tag2")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetATag2"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :schema: CfnModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :schema: CfnModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet_tag1(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnetTag1"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PublicSubnetTag1
        '''
        result = self._values.get("public_subnet_tag1")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnetTag1"], result)

    @builtins.property
    def public_subnet_tag2(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnetTag2"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PublicSubnetTag2
        '''
        result = self._values.get("public_subnet_tag2")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnetTag2"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        :schema: CfnModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpccidr"], result)

    @builtins.property
    def vpc_tenancy(self) -> typing.Optional["CfnModulePropsParametersVpcTenancy"]:
        '''The allowed tenancy of instances launched into the VPC.

        :schema: CfnModulePropsParameters#VPCTenancy
        '''
        result = self._values.get("vpc_tenancy")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcTenancy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZone1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZone2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersCreateNatGateways",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreateNatGateways:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreateNatGateways
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateNatGateways#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateNatGateways#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreateNatGateways(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersCreatePrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreatePrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreatePrivateSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreatePrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreatePrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreatePrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersCreatePublicSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreatePublicSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreatePublicSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreatePublicSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreatePublicSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreatePublicSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPrivateSubnet1Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet1Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPrivateSubnet2Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet2Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPrivateSubnetATag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetATag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetATag1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetATag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPrivateSubnetATag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetATag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetATag2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetATag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPublicSubnetTag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnetTag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnetTag1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnetTag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersPublicSubnetTag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnetTag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnetTag2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnetTag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersVpcTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The allowed tenancy of instances launched into the VPC.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcTenancy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpccidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpccidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpccidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResources",
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
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        dhcp_options: typing.Optional["CfnModulePropsResourcesDhcpOptions"] = None,
        internet_gateway: typing.Optional["CfnModulePropsResourcesInternetGateway"] = None,
        nat1_eip: typing.Optional["CfnModulePropsResourcesNat1Eip"] = None,
        nat2_eip: typing.Optional["CfnModulePropsResourcesNat2Eip"] = None,
        nat_gateway1: typing.Optional["CfnModulePropsResourcesNatGateway1"] = None,
        nat_gateway2: typing.Optional["CfnModulePropsResourcesNatGateway2"] = None,
        private_subnet1_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet1A"] = None,
        private_subnet1_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARoute"] = None,
        private_subnet1_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTable"] = None,
        private_subnet1_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation"] = None,
        private_subnet2_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet2A"] = None,
        private_subnet2_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARoute"] = None,
        private_subnet2_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTable"] = None,
        private_subnet2_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation"] = None,
        public_subnet1: typing.Optional["CfnModulePropsResourcesPublicSubnet1"] = None,
        public_subnet1_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"] = None,
        public_subnet2: typing.Optional["CfnModulePropsResourcesPublicSubnet2"] = None,
        public_subnet2_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"] = None,
        public_subnet_route: typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"] = None,
        public_subnet_route_table: typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"] = None,
        s3_vpc_endpoint: typing.Optional["CfnModulePropsResourcesS3VpcEndpoint"] = None,
        vpc: typing.Optional["CfnModulePropsResourcesVpc"] = None,
        vpcdhcp_options_association: typing.Optional["CfnModulePropsResourcesVpcdhcpOptionsAssociation"] = None,
        vpc_gateway_attachment: typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"] = None,
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

        :schema: CfnModulePropsResources
        '''
        if isinstance(dhcp_options, dict):
            dhcp_options = CfnModulePropsResourcesDhcpOptions(**dhcp_options)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(nat1_eip, dict):
            nat1_eip = CfnModulePropsResourcesNat1Eip(**nat1_eip)
        if isinstance(nat2_eip, dict):
            nat2_eip = CfnModulePropsResourcesNat2Eip(**nat2_eip)
        if isinstance(nat_gateway1, dict):
            nat_gateway1 = CfnModulePropsResourcesNatGateway1(**nat_gateway1)
        if isinstance(nat_gateway2, dict):
            nat_gateway2 = CfnModulePropsResourcesNatGateway2(**nat_gateway2)
        if isinstance(private_subnet1_a, dict):
            private_subnet1_a = CfnModulePropsResourcesPrivateSubnet1A(**private_subnet1_a)
        if isinstance(private_subnet1_a_route, dict):
            private_subnet1_a_route = CfnModulePropsResourcesPrivateSubnet1ARoute(**private_subnet1_a_route)
        if isinstance(private_subnet1_a_route_table, dict):
            private_subnet1_a_route_table = CfnModulePropsResourcesPrivateSubnet1ARouteTable(**private_subnet1_a_route_table)
        if isinstance(private_subnet1_a_route_table_association, dict):
            private_subnet1_a_route_table_association = CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation(**private_subnet1_a_route_table_association)
        if isinstance(private_subnet2_a, dict):
            private_subnet2_a = CfnModulePropsResourcesPrivateSubnet2A(**private_subnet2_a)
        if isinstance(private_subnet2_a_route, dict):
            private_subnet2_a_route = CfnModulePropsResourcesPrivateSubnet2ARoute(**private_subnet2_a_route)
        if isinstance(private_subnet2_a_route_table, dict):
            private_subnet2_a_route_table = CfnModulePropsResourcesPrivateSubnet2ARouteTable(**private_subnet2_a_route_table)
        if isinstance(private_subnet2_a_route_table_association, dict):
            private_subnet2_a_route_table_association = CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation(**private_subnet2_a_route_table_association)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(s3_vpc_endpoint, dict):
            s3_vpc_endpoint = CfnModulePropsResourcesS3VpcEndpoint(**s3_vpc_endpoint)
        if isinstance(vpc, dict):
            vpc = CfnModulePropsResourcesVpc(**vpc)
        if isinstance(vpcdhcp_options_association, dict):
            vpcdhcp_options_association = CfnModulePropsResourcesVpcdhcpOptionsAssociation(**vpcdhcp_options_association)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
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
    def dhcp_options(self) -> typing.Optional["CfnModulePropsResourcesDhcpOptions"]:
        '''
        :schema: CfnModulePropsResources#DHCPOptions
        '''
        result = self._values.get("dhcp_options")
        return typing.cast(typing.Optional["CfnModulePropsResourcesDhcpOptions"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def nat1_eip(self) -> typing.Optional["CfnModulePropsResourcesNat1Eip"]:
        '''
        :schema: CfnModulePropsResources#NAT1EIP
        '''
        result = self._values.get("nat1_eip")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNat1Eip"], result)

    @builtins.property
    def nat2_eip(self) -> typing.Optional["CfnModulePropsResourcesNat2Eip"]:
        '''
        :schema: CfnModulePropsResources#NAT2EIP
        '''
        result = self._values.get("nat2_eip")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNat2Eip"], result)

    @builtins.property
    def nat_gateway1(self) -> typing.Optional["CfnModulePropsResourcesNatGateway1"]:
        '''
        :schema: CfnModulePropsResources#NATGateway1
        '''
        result = self._values.get("nat_gateway1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNatGateway1"], result)

    @builtins.property
    def nat_gateway2(self) -> typing.Optional["CfnModulePropsResourcesNatGateway2"]:
        '''
        :schema: CfnModulePropsResources#NATGateway2
        '''
        result = self._values.get("nat_gateway2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNatGateway2"], result)

    @builtins.property
    def private_subnet1_a(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1A"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1A
        '''
        result = self._values.get("private_subnet1_a")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1A"], result)

    @builtins.property
    def private_subnet1_a_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1ARoute
        '''
        result = self._values.get("private_subnet1_a_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARoute"], result)

    @builtins.property
    def private_subnet1_a_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1ARouteTable
        '''
        result = self._values.get("private_subnet1_a_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTable"], result)

    @builtins.property
    def private_subnet1_a_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1ARouteTableAssociation
        '''
        result = self._values.get("private_subnet1_a_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet2_a(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2A"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2A
        '''
        result = self._values.get("private_subnet2_a")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2A"], result)

    @builtins.property
    def private_subnet2_a_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2ARoute
        '''
        result = self._values.get("private_subnet2_a_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARoute"], result)

    @builtins.property
    def private_subnet2_a_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2ARouteTable
        '''
        result = self._values.get("private_subnet2_a_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTable"], result)

    @builtins.property
    def private_subnet2_a_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2ARouteTableAssociation
        '''
        result = self._values.get("private_subnet2_a_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation"], result)

    @builtins.property
    def public_subnet1(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def s3_vpc_endpoint(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesS3VpcEndpoint"]:
        '''
        :schema: CfnModulePropsResources#S3VPCEndpoint
        '''
        result = self._values.get("s3_vpc_endpoint")
        return typing.cast(typing.Optional["CfnModulePropsResourcesS3VpcEndpoint"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnModulePropsResourcesVpc"]:
        '''
        :schema: CfnModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpc"], result)

    @builtins.property
    def vpcdhcp_options_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcdhcpOptionsAssociation"]:
        '''
        :schema: CfnModulePropsResources#VPCDHCPOptionsAssociation
        '''
        result = self._values.get("vpcdhcp_options_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcdhcpOptionsAssociation"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesDhcpOptions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesDhcpOptions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesDhcpOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesDhcpOptions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesDhcpOptions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesDhcpOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternetGateway
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesNat1Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNat1Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNat1Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNat1Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNat1Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNat1Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesNat2Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNat2Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNat2Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNat2Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNat2Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNat2Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesNatGateway1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNatGateway1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNatGateway1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNatGateway1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNatGateway1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNatGateway1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesNatGateway2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNatGateway2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNatGateway2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNatGateway2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNatGateway2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNatGateway2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet1A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet1ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet1ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet2A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet2ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet2ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnetRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnetRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesS3VpcEndpoint",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesS3VpcEndpoint:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesS3VpcEndpoint
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesS3VpcEndpoint#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesS3VpcEndpoint#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesS3VpcEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpc
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcGatewayAttachment
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-vpc-multiaz-module.CfnModulePropsResourcesVpcdhcpOptionsAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcdhcpOptionsAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcdhcpOptionsAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcdhcpOptionsAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcdhcpOptionsAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcdhcpOptionsAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersAvailabilityZone1",
    "CfnModulePropsParametersAvailabilityZone2",
    "CfnModulePropsParametersCreateNatGateways",
    "CfnModulePropsParametersCreatePrivateSubnets",
    "CfnModulePropsParametersCreatePublicSubnets",
    "CfnModulePropsParametersPrivateSubnet1Acidr",
    "CfnModulePropsParametersPrivateSubnet2Acidr",
    "CfnModulePropsParametersPrivateSubnetATag1",
    "CfnModulePropsParametersPrivateSubnetATag2",
    "CfnModulePropsParametersPublicSubnet1Cidr",
    "CfnModulePropsParametersPublicSubnet2Cidr",
    "CfnModulePropsParametersPublicSubnetTag1",
    "CfnModulePropsParametersPublicSubnetTag2",
    "CfnModulePropsParametersVpcTenancy",
    "CfnModulePropsParametersVpccidr",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesDhcpOptions",
    "CfnModulePropsResourcesInternetGateway",
    "CfnModulePropsResourcesNat1Eip",
    "CfnModulePropsResourcesNat2Eip",
    "CfnModulePropsResourcesNatGateway1",
    "CfnModulePropsResourcesNatGateway2",
    "CfnModulePropsResourcesPrivateSubnet1A",
    "CfnModulePropsResourcesPrivateSubnet1ARoute",
    "CfnModulePropsResourcesPrivateSubnet1ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet2A",
    "CfnModulePropsResourcesPrivateSubnet2ARoute",
    "CfnModulePropsResourcesPrivateSubnet2ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet1",
    "CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet2",
    "CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnetRoute",
    "CfnModulePropsResourcesPublicSubnetRouteTable",
    "CfnModulePropsResourcesS3VpcEndpoint",
    "CfnModulePropsResourcesVpc",
    "CfnModulePropsResourcesVpcGatewayAttachment",
    "CfnModulePropsResourcesVpcdhcpOptionsAssociation",
]

publication.publish()
