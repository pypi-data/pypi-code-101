'''
# AWS CDK CloudFormation Constructs for AWSQS::VPC::VPCQS::MODULE

Schema for Module Fragment of type AWSQS::VPC::VPCQS::MODULE

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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModule",
):
    '''A CloudFormation ``AWSQS::VPC::VPCQS::MODULE``.

    :cloudformationResource: AWSQS::VPC::VPCQS::MODULE
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
        '''Create a new ``AWSQS::VPC::VPCQS::MODULE``.

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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type AWSQS::VPC::VPCQS::MODULE.

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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "create_additional_private_subnets": "createAdditionalPrivateSubnets",
        "create_nat_gateways": "createNatGateways",
        "create_private_subnets": "createPrivateSubnets",
        "create_public_subnets": "createPublicSubnets",
        "create_vpc_flow_logs_to_cloud_watch": "createVpcFlowLogsToCloudWatch",
        "number_of_a_zs": "numberOfAZs",
        "private_subnet1_acidr": "privateSubnet1Acidr",
        "private_subnet1_bcidr": "privateSubnet1Bcidr",
        "private_subnet2_acidr": "privateSubnet2Acidr",
        "private_subnet2_bcidr": "privateSubnet2Bcidr",
        "private_subnet3_acidr": "privateSubnet3Acidr",
        "private_subnet3_bcidr": "privateSubnet3Bcidr",
        "private_subnet4_acidr": "privateSubnet4Acidr",
        "private_subnet4_bcidr": "privateSubnet4Bcidr",
        "private_subnet_a_tag1": "privateSubnetATag1",
        "private_subnet_a_tag2": "privateSubnetATag2",
        "private_subnet_a_tag3": "privateSubnetATag3",
        "private_subnet_b_tag1": "privateSubnetBTag1",
        "private_subnet_b_tag2": "privateSubnetBTag2",
        "private_subnet_b_tag3": "privateSubnetBTag3",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet3_cidr": "publicSubnet3Cidr",
        "public_subnet4_cidr": "publicSubnet4Cidr",
        "public_subnet_tag1": "publicSubnetTag1",
        "public_subnet_tag2": "publicSubnetTag2",
        "public_subnet_tag3": "publicSubnetTag3",
        "vpccidr": "vpccidr",
        "vpc_flow_logs_cloud_watch_kms_key": "vpcFlowLogsCloudWatchKmsKey",
        "vpc_flow_logs_log_format": "vpcFlowLogsLogFormat",
        "vpc_flow_logs_log_group_retention": "vpcFlowLogsLogGroupRetention",
        "vpc_flow_logs_max_aggregation_interval": "vpcFlowLogsMaxAggregationInterval",
        "vpc_flow_logs_traffic_type": "vpcFlowLogsTrafficType",
        "vpc_tenancy": "vpcTenancy",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional["CfnModulePropsParametersAvailabilityZones"] = None,
        create_additional_private_subnets: typing.Optional["CfnModulePropsParametersCreateAdditionalPrivateSubnets"] = None,
        create_nat_gateways: typing.Optional["CfnModulePropsParametersCreateNatGateways"] = None,
        create_private_subnets: typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"] = None,
        create_public_subnets: typing.Optional["CfnModulePropsParametersCreatePublicSubnets"] = None,
        create_vpc_flow_logs_to_cloud_watch: typing.Optional["CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch"] = None,
        number_of_a_zs: typing.Optional["CfnModulePropsParametersNumberOfAZs"] = None,
        private_subnet1_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Acidr"] = None,
        private_subnet1_bcidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Bcidr"] = None,
        private_subnet2_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Acidr"] = None,
        private_subnet2_bcidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Bcidr"] = None,
        private_subnet3_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet3Acidr"] = None,
        private_subnet3_bcidr: typing.Optional["CfnModulePropsParametersPrivateSubnet3Bcidr"] = None,
        private_subnet4_acidr: typing.Optional["CfnModulePropsParametersPrivateSubnet4Acidr"] = None,
        private_subnet4_bcidr: typing.Optional["CfnModulePropsParametersPrivateSubnet4Bcidr"] = None,
        private_subnet_a_tag1: typing.Optional["CfnModulePropsParametersPrivateSubnetATag1"] = None,
        private_subnet_a_tag2: typing.Optional["CfnModulePropsParametersPrivateSubnetATag2"] = None,
        private_subnet_a_tag3: typing.Optional["CfnModulePropsParametersPrivateSubnetATag3"] = None,
        private_subnet_b_tag1: typing.Optional["CfnModulePropsParametersPrivateSubnetBTag1"] = None,
        private_subnet_b_tag2: typing.Optional["CfnModulePropsParametersPrivateSubnetBTag2"] = None,
        private_subnet_b_tag3: typing.Optional["CfnModulePropsParametersPrivateSubnetBTag3"] = None,
        public_subnet1_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet3_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"] = None,
        public_subnet4_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"] = None,
        public_subnet_tag1: typing.Optional["CfnModulePropsParametersPublicSubnetTag1"] = None,
        public_subnet_tag2: typing.Optional["CfnModulePropsParametersPublicSubnetTag2"] = None,
        public_subnet_tag3: typing.Optional["CfnModulePropsParametersPublicSubnetTag3"] = None,
        vpccidr: typing.Optional["CfnModulePropsParametersVpccidr"] = None,
        vpc_flow_logs_cloud_watch_kms_key: typing.Optional["CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey"] = None,
        vpc_flow_logs_log_format: typing.Optional["CfnModulePropsParametersVpcFlowLogsLogFormat"] = None,
        vpc_flow_logs_log_group_retention: typing.Optional["CfnModulePropsParametersVpcFlowLogsLogGroupRetention"] = None,
        vpc_flow_logs_max_aggregation_interval: typing.Optional["CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval"] = None,
        vpc_flow_logs_traffic_type: typing.Optional["CfnModulePropsParametersVpcFlowLogsTrafficType"] = None,
        vpc_tenancy: typing.Optional["CfnModulePropsParametersVpcTenancy"] = None,
    ) -> None:
        '''
        :param availability_zones: List of Availability Zones to use for the subnets in the VPC. Note: The logical order is preserved.
        :param create_additional_private_subnets: Set to true to create a network ACL protected subnet in each Availability Zone. If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.
        :param create_nat_gateways: Set to false when creating only private subnets. If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.
        :param create_private_subnets: Set to false to create only public subnets. If false, the CIDR parameters for ALL private subnets will be ignored.
        :param create_public_subnets: Set to false to create only private subnets. If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored
        :param create_vpc_flow_logs_to_cloud_watch: Set to true to create VPC flow logs for the VPC and publish them to CloudWatch. If false, VPC flow logs will not be created.
        :param number_of_a_zs: Number of Availability Zones to use in the VPC. This must match your selections in the list of Availability Zones parameter.
        :param private_subnet1_acidr: CIDR block for private subnet 1A located in Availability Zone 1.
        :param private_subnet1_bcidr: CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.
        :param private_subnet2_acidr: CIDR block for private subnet 2A located in Availability Zone 2.
        :param private_subnet2_bcidr: CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.
        :param private_subnet3_acidr: CIDR block for private subnet 3A located in Availability Zone 3.
        :param private_subnet3_bcidr: CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.
        :param private_subnet4_acidr: CIDR block for private subnet 4A located in Availability Zone 4.
        :param private_subnet4_bcidr: CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.
        :param private_subnet_a_tag1: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_a_tag2: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_a_tag3: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_b_tag1: tag to add to private subnets B, in format Key=Value (Optional).
        :param private_subnet_b_tag2: tag to add to private subnets B, in format Key=Value (Optional).
        :param private_subnet_b_tag3: tag to add to private subnets B, in format Key=Value (Optional).
        :param public_subnet1_cidr: CIDR block for the public DMZ subnet 1 located in Availability Zone 1.
        :param public_subnet2_cidr: CIDR block for the public DMZ subnet 2 located in Availability Zone 2.
        :param public_subnet3_cidr: CIDR block for the public DMZ subnet 3 located in Availability Zone 3.
        :param public_subnet4_cidr: CIDR block for the public DMZ subnet 4 located in Availability Zone 4.
        :param public_subnet_tag1: tag to add to public subnets, in format Key=Value (Optional).
        :param public_subnet_tag2: tag to add to public subnets, in format Key=Value (Optional).
        :param public_subnet_tag3: tag to add to public subnets, in format Key=Value (Optional).
        :param vpccidr: CIDR block for the VPC.
        :param vpc_flow_logs_cloud_watch_kms_key: (Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.
        :param vpc_flow_logs_log_format: The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.
        :param vpc_flow_logs_log_group_retention: Number of days to retain the VPC Flow Logs in CloudWatch.
        :param vpc_flow_logs_max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        :param vpc_flow_logs_traffic_type: The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        :param vpc_tenancy: The allowed tenancy of instances launched into the VPC.

        :schema: CfnModulePropsParameters
        '''
        if isinstance(availability_zones, dict):
            availability_zones = CfnModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(create_additional_private_subnets, dict):
            create_additional_private_subnets = CfnModulePropsParametersCreateAdditionalPrivateSubnets(**create_additional_private_subnets)
        if isinstance(create_nat_gateways, dict):
            create_nat_gateways = CfnModulePropsParametersCreateNatGateways(**create_nat_gateways)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_public_subnets, dict):
            create_public_subnets = CfnModulePropsParametersCreatePublicSubnets(**create_public_subnets)
        if isinstance(create_vpc_flow_logs_to_cloud_watch, dict):
            create_vpc_flow_logs_to_cloud_watch = CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch(**create_vpc_flow_logs_to_cloud_watch)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(private_subnet1_acidr, dict):
            private_subnet1_acidr = CfnModulePropsParametersPrivateSubnet1Acidr(**private_subnet1_acidr)
        if isinstance(private_subnet1_bcidr, dict):
            private_subnet1_bcidr = CfnModulePropsParametersPrivateSubnet1Bcidr(**private_subnet1_bcidr)
        if isinstance(private_subnet2_acidr, dict):
            private_subnet2_acidr = CfnModulePropsParametersPrivateSubnet2Acidr(**private_subnet2_acidr)
        if isinstance(private_subnet2_bcidr, dict):
            private_subnet2_bcidr = CfnModulePropsParametersPrivateSubnet2Bcidr(**private_subnet2_bcidr)
        if isinstance(private_subnet3_acidr, dict):
            private_subnet3_acidr = CfnModulePropsParametersPrivateSubnet3Acidr(**private_subnet3_acidr)
        if isinstance(private_subnet3_bcidr, dict):
            private_subnet3_bcidr = CfnModulePropsParametersPrivateSubnet3Bcidr(**private_subnet3_bcidr)
        if isinstance(private_subnet4_acidr, dict):
            private_subnet4_acidr = CfnModulePropsParametersPrivateSubnet4Acidr(**private_subnet4_acidr)
        if isinstance(private_subnet4_bcidr, dict):
            private_subnet4_bcidr = CfnModulePropsParametersPrivateSubnet4Bcidr(**private_subnet4_bcidr)
        if isinstance(private_subnet_a_tag1, dict):
            private_subnet_a_tag1 = CfnModulePropsParametersPrivateSubnetATag1(**private_subnet_a_tag1)
        if isinstance(private_subnet_a_tag2, dict):
            private_subnet_a_tag2 = CfnModulePropsParametersPrivateSubnetATag2(**private_subnet_a_tag2)
        if isinstance(private_subnet_a_tag3, dict):
            private_subnet_a_tag3 = CfnModulePropsParametersPrivateSubnetATag3(**private_subnet_a_tag3)
        if isinstance(private_subnet_b_tag1, dict):
            private_subnet_b_tag1 = CfnModulePropsParametersPrivateSubnetBTag1(**private_subnet_b_tag1)
        if isinstance(private_subnet_b_tag2, dict):
            private_subnet_b_tag2 = CfnModulePropsParametersPrivateSubnetBTag2(**private_subnet_b_tag2)
        if isinstance(private_subnet_b_tag3, dict):
            private_subnet_b_tag3 = CfnModulePropsParametersPrivateSubnetBTag3(**private_subnet_b_tag3)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(public_subnet4_cidr, dict):
            public_subnet4_cidr = CfnModulePropsParametersPublicSubnet4Cidr(**public_subnet4_cidr)
        if isinstance(public_subnet_tag1, dict):
            public_subnet_tag1 = CfnModulePropsParametersPublicSubnetTag1(**public_subnet_tag1)
        if isinstance(public_subnet_tag2, dict):
            public_subnet_tag2 = CfnModulePropsParametersPublicSubnetTag2(**public_subnet_tag2)
        if isinstance(public_subnet_tag3, dict):
            public_subnet_tag3 = CfnModulePropsParametersPublicSubnetTag3(**public_subnet_tag3)
        if isinstance(vpccidr, dict):
            vpccidr = CfnModulePropsParametersVpccidr(**vpccidr)
        if isinstance(vpc_flow_logs_cloud_watch_kms_key, dict):
            vpc_flow_logs_cloud_watch_kms_key = CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey(**vpc_flow_logs_cloud_watch_kms_key)
        if isinstance(vpc_flow_logs_log_format, dict):
            vpc_flow_logs_log_format = CfnModulePropsParametersVpcFlowLogsLogFormat(**vpc_flow_logs_log_format)
        if isinstance(vpc_flow_logs_log_group_retention, dict):
            vpc_flow_logs_log_group_retention = CfnModulePropsParametersVpcFlowLogsLogGroupRetention(**vpc_flow_logs_log_group_retention)
        if isinstance(vpc_flow_logs_max_aggregation_interval, dict):
            vpc_flow_logs_max_aggregation_interval = CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval(**vpc_flow_logs_max_aggregation_interval)
        if isinstance(vpc_flow_logs_traffic_type, dict):
            vpc_flow_logs_traffic_type = CfnModulePropsParametersVpcFlowLogsTrafficType(**vpc_flow_logs_traffic_type)
        if isinstance(vpc_tenancy, dict):
            vpc_tenancy = CfnModulePropsParametersVpcTenancy(**vpc_tenancy)
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if create_additional_private_subnets is not None:
            self._values["create_additional_private_subnets"] = create_additional_private_subnets
        if create_nat_gateways is not None:
            self._values["create_nat_gateways"] = create_nat_gateways
        if create_private_subnets is not None:
            self._values["create_private_subnets"] = create_private_subnets
        if create_public_subnets is not None:
            self._values["create_public_subnets"] = create_public_subnets
        if create_vpc_flow_logs_to_cloud_watch is not None:
            self._values["create_vpc_flow_logs_to_cloud_watch"] = create_vpc_flow_logs_to_cloud_watch
        if number_of_a_zs is not None:
            self._values["number_of_a_zs"] = number_of_a_zs
        if private_subnet1_acidr is not None:
            self._values["private_subnet1_acidr"] = private_subnet1_acidr
        if private_subnet1_bcidr is not None:
            self._values["private_subnet1_bcidr"] = private_subnet1_bcidr
        if private_subnet2_acidr is not None:
            self._values["private_subnet2_acidr"] = private_subnet2_acidr
        if private_subnet2_bcidr is not None:
            self._values["private_subnet2_bcidr"] = private_subnet2_bcidr
        if private_subnet3_acidr is not None:
            self._values["private_subnet3_acidr"] = private_subnet3_acidr
        if private_subnet3_bcidr is not None:
            self._values["private_subnet3_bcidr"] = private_subnet3_bcidr
        if private_subnet4_acidr is not None:
            self._values["private_subnet4_acidr"] = private_subnet4_acidr
        if private_subnet4_bcidr is not None:
            self._values["private_subnet4_bcidr"] = private_subnet4_bcidr
        if private_subnet_a_tag1 is not None:
            self._values["private_subnet_a_tag1"] = private_subnet_a_tag1
        if private_subnet_a_tag2 is not None:
            self._values["private_subnet_a_tag2"] = private_subnet_a_tag2
        if private_subnet_a_tag3 is not None:
            self._values["private_subnet_a_tag3"] = private_subnet_a_tag3
        if private_subnet_b_tag1 is not None:
            self._values["private_subnet_b_tag1"] = private_subnet_b_tag1
        if private_subnet_b_tag2 is not None:
            self._values["private_subnet_b_tag2"] = private_subnet_b_tag2
        if private_subnet_b_tag3 is not None:
            self._values["private_subnet_b_tag3"] = private_subnet_b_tag3
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet3_cidr is not None:
            self._values["public_subnet3_cidr"] = public_subnet3_cidr
        if public_subnet4_cidr is not None:
            self._values["public_subnet4_cidr"] = public_subnet4_cidr
        if public_subnet_tag1 is not None:
            self._values["public_subnet_tag1"] = public_subnet_tag1
        if public_subnet_tag2 is not None:
            self._values["public_subnet_tag2"] = public_subnet_tag2
        if public_subnet_tag3 is not None:
            self._values["public_subnet_tag3"] = public_subnet_tag3
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr
        if vpc_flow_logs_cloud_watch_kms_key is not None:
            self._values["vpc_flow_logs_cloud_watch_kms_key"] = vpc_flow_logs_cloud_watch_kms_key
        if vpc_flow_logs_log_format is not None:
            self._values["vpc_flow_logs_log_format"] = vpc_flow_logs_log_format
        if vpc_flow_logs_log_group_retention is not None:
            self._values["vpc_flow_logs_log_group_retention"] = vpc_flow_logs_log_group_retention
        if vpc_flow_logs_max_aggregation_interval is not None:
            self._values["vpc_flow_logs_max_aggregation_interval"] = vpc_flow_logs_max_aggregation_interval
        if vpc_flow_logs_traffic_type is not None:
            self._values["vpc_flow_logs_traffic_type"] = vpc_flow_logs_traffic_type
        if vpc_tenancy is not None:
            self._values["vpc_tenancy"] = vpc_tenancy

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZones"]:
        '''List of Availability Zones to use for the subnets in the VPC.

        Note: The logical order is preserved.

        :schema: CfnModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def create_additional_private_subnets(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreateAdditionalPrivateSubnets"]:
        '''Set to true to create a network ACL protected subnet in each Availability Zone.

        If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.

        :schema: CfnModulePropsParameters#CreateAdditionalPrivateSubnets
        '''
        result = self._values.get("create_additional_private_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreateAdditionalPrivateSubnets"], result)

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
    def create_vpc_flow_logs_to_cloud_watch(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch"]:
        '''Set to true to create VPC flow logs for the VPC and publish them to CloudWatch.

        If false, VPC flow logs will not be created.

        :schema: CfnModulePropsParameters#CreateVPCFlowLogsToCloudWatch
        '''
        result = self._values.get("create_vpc_flow_logs_to_cloud_watch")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch"], result)

    @builtins.property
    def number_of_a_zs(self) -> typing.Optional["CfnModulePropsParametersNumberOfAZs"]:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.

        :schema: CfnModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumberOfAZs"], result)

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
    def private_subnet1_bcidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Bcidr"]:
        '''CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.

        :schema: CfnModulePropsParameters#PrivateSubnet1BCIDR
        '''
        result = self._values.get("private_subnet1_bcidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Bcidr"], result)

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
    def private_subnet2_bcidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Bcidr"]:
        '''CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.

        :schema: CfnModulePropsParameters#PrivateSubnet2BCIDR
        '''
        result = self._values.get("private_subnet2_bcidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Bcidr"], result)

    @builtins.property
    def private_subnet3_acidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet3Acidr"]:
        '''CIDR block for private subnet 3A located in Availability Zone 3.

        :schema: CfnModulePropsParameters#PrivateSubnet3ACIDR
        '''
        result = self._values.get("private_subnet3_acidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet3Acidr"], result)

    @builtins.property
    def private_subnet3_bcidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet3Bcidr"]:
        '''CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.

        :schema: CfnModulePropsParameters#PrivateSubnet3BCIDR
        '''
        result = self._values.get("private_subnet3_bcidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet3Bcidr"], result)

    @builtins.property
    def private_subnet4_acidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet4Acidr"]:
        '''CIDR block for private subnet 4A located in Availability Zone 4.

        :schema: CfnModulePropsParameters#PrivateSubnet4ACIDR
        '''
        result = self._values.get("private_subnet4_acidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet4Acidr"], result)

    @builtins.property
    def private_subnet4_bcidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet4Bcidr"]:
        '''CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.

        :schema: CfnModulePropsParameters#PrivateSubnet4BCIDR
        '''
        result = self._values.get("private_subnet4_bcidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet4Bcidr"], result)

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
    def private_subnet_a_tag3(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetATag3"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetATag3
        '''
        result = self._values.get("private_subnet_a_tag3")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetATag3"], result)

    @builtins.property
    def private_subnet_b_tag1(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetBTag1"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetBTag1
        '''
        result = self._values.get("private_subnet_b_tag1")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetBTag1"], result)

    @builtins.property
    def private_subnet_b_tag2(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetBTag2"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetBTag2
        '''
        result = self._values.get("private_subnet_b_tag2")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetBTag2"], result)

    @builtins.property
    def private_subnet_b_tag3(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnetBTag3"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PrivateSubnetBTag3
        '''
        result = self._values.get("private_subnet_b_tag3")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnetBTag3"], result)

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
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"]:
        '''CIDR block for the public DMZ subnet 3 located in Availability Zone 3.

        :schema: CfnModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def public_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"]:
        '''CIDR block for the public DMZ subnet 4 located in Availability Zone 4.

        :schema: CfnModulePropsParameters#PublicSubnet4CIDR
        '''
        result = self._values.get("public_subnet4_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"], result)

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
    def public_subnet_tag3(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnetTag3"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnModulePropsParameters#PublicSubnetTag3
        '''
        result = self._values.get("public_subnet_tag3")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnetTag3"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        :schema: CfnModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpccidr"], result)

    @builtins.property
    def vpc_flow_logs_cloud_watch_kms_key(
        self,
    ) -> typing.Optional["CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey"]:
        '''(Optional) KMS Key ARN to use for encrypting the VPC flow logs data.

        If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.

        :schema: CfnModulePropsParameters#VPCFlowLogsCloudWatchKMSKey
        '''
        result = self._values.get("vpc_flow_logs_cloud_watch_kms_key")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey"], result)

    @builtins.property
    def vpc_flow_logs_log_format(
        self,
    ) -> typing.Optional["CfnModulePropsParametersVpcFlowLogsLogFormat"]:
        '''The fields to include in the flow log record, in the order in which they should appear.

        Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.

        :schema: CfnModulePropsParameters#VPCFlowLogsLogFormat
        '''
        result = self._values.get("vpc_flow_logs_log_format")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcFlowLogsLogFormat"], result)

    @builtins.property
    def vpc_flow_logs_log_group_retention(
        self,
    ) -> typing.Optional["CfnModulePropsParametersVpcFlowLogsLogGroupRetention"]:
        '''Number of days to retain the VPC Flow Logs in CloudWatch.

        :schema: CfnModulePropsParameters#VPCFlowLogsLogGroupRetention
        '''
        result = self._values.get("vpc_flow_logs_log_group_retention")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcFlowLogsLogGroupRetention"], result)

    @builtins.property
    def vpc_flow_logs_max_aggregation_interval(
        self,
    ) -> typing.Optional["CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval"]:
        '''The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record.

        You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).

        :schema: CfnModulePropsParameters#VPCFlowLogsMaxAggregationInterval
        '''
        result = self._values.get("vpc_flow_logs_max_aggregation_interval")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval"], result)

    @builtins.property
    def vpc_flow_logs_traffic_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersVpcFlowLogsTrafficType"]:
        '''The type of traffic to log.

        You can log traffic that the resource accepts or rejects, or all traffic.

        :schema: CfnModulePropsParameters#VPCFlowLogsTrafficType
        '''
        result = self._values.get("vpc_flow_logs_traffic_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcFlowLogsTrafficType"], result)

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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZones:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''List of Availability Zones to use for the subnets in the VPC.

        Note: The logical order is preserved.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZones
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZones#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZones#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersCreateAdditionalPrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreateAdditionalPrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to true to create a network ACL protected subnet in each Availability Zone.

        If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreateAdditionalPrivateSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateAdditionalPrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateAdditionalPrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreateAdditionalPrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersCreateNatGateways",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersCreatePrivateSubnets",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersCreatePublicSubnets",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to true to create VPC flow logs for the VPC and publish them to CloudWatch.

        If false, VPC flow logs will not be created.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNumberOfAZs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNumberOfAZs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumberOfAZs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumberOfAZs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNumberOfAZs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet1Acidr",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet1Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Bcidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet1Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet2Acidr",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet2Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Bcidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet2Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet3Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet3Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3A located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet3Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet3Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet3Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet3Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet3Bcidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet3Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet4Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet4Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4A located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet4Acidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet4Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnet4Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet4Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet4Bcidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet4Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetATag1",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetATag2",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetATag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetATag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetATag3
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetATag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetATag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetBTag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetBTag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetBTag1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetBTag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetBTag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetBTag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetBTag2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetBTag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPrivateSubnetBTag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnetBTag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnetBTag3
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnetBTag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnetBTag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnet1Cidr",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnet2Cidr",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 3 located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 4 located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet4Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnetTag1",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnetTag2",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersPublicSubnetTag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnetTag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnetTag3
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnetTag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnetTag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(Optional) KMS Key ARN to use for encrypting the VPC flow logs data.

        If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcFlowLogsLogFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcFlowLogsLogFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The fields to include in the flow log record, in the order in which they should appear.

        Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcFlowLogsLogFormat
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsLogFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsLogFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcFlowLogsLogFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcFlowLogsLogGroupRetention",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcFlowLogsLogGroupRetention:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of days to retain the VPC Flow Logs in CloudWatch.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcFlowLogsLogGroupRetention
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsLogGroupRetention#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsLogGroupRetention#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcFlowLogsLogGroupRetention(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record.

        You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcFlowLogsTrafficType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcFlowLogsTrafficType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The type of traffic to log.

        You can log traffic that the resource accepts or rejects, or all traffic.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcFlowLogsTrafficType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsTrafficType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcFlowLogsTrafficType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcFlowLogsTrafficType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpcTenancy",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsParametersVpccidr",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "dhcp_options": "dhcpOptions",
        "internet_gateway": "internetGateway",
        "nat1_eip": "nat1Eip",
        "nat2_eip": "nat2Eip",
        "nat3_eip": "nat3Eip",
        "nat4_eip": "nat4Eip",
        "nat_gateway1": "natGateway1",
        "nat_gateway2": "natGateway2",
        "nat_gateway3": "natGateway3",
        "nat_gateway4": "natGateway4",
        "private_subnet1_a": "privateSubnet1A",
        "private_subnet1_a_route": "privateSubnet1ARoute",
        "private_subnet1_a_route_table": "privateSubnet1ARouteTable",
        "private_subnet1_a_route_table_association": "privateSubnet1ARouteTableAssociation",
        "private_subnet1_b": "privateSubnet1B",
        "private_subnet1_b_network_acl": "privateSubnet1BNetworkAcl",
        "private_subnet1_b_network_acl_association": "privateSubnet1BNetworkAclAssociation",
        "private_subnet1_b_network_acl_entry_inbound": "privateSubnet1BNetworkAclEntryInbound",
        "private_subnet1_b_network_acl_entry_outbound": "privateSubnet1BNetworkAclEntryOutbound",
        "private_subnet1_b_route": "privateSubnet1BRoute",
        "private_subnet1_b_route_table": "privateSubnet1BRouteTable",
        "private_subnet1_b_route_table_association": "privateSubnet1BRouteTableAssociation",
        "private_subnet2_a": "privateSubnet2A",
        "private_subnet2_a_route": "privateSubnet2ARoute",
        "private_subnet2_a_route_table": "privateSubnet2ARouteTable",
        "private_subnet2_a_route_table_association": "privateSubnet2ARouteTableAssociation",
        "private_subnet2_b": "privateSubnet2B",
        "private_subnet2_b_network_acl": "privateSubnet2BNetworkAcl",
        "private_subnet2_b_network_acl_association": "privateSubnet2BNetworkAclAssociation",
        "private_subnet2_b_network_acl_entry_inbound": "privateSubnet2BNetworkAclEntryInbound",
        "private_subnet2_b_network_acl_entry_outbound": "privateSubnet2BNetworkAclEntryOutbound",
        "private_subnet2_b_route": "privateSubnet2BRoute",
        "private_subnet2_b_route_table": "privateSubnet2BRouteTable",
        "private_subnet2_b_route_table_association": "privateSubnet2BRouteTableAssociation",
        "private_subnet3_a": "privateSubnet3A",
        "private_subnet3_a_route": "privateSubnet3ARoute",
        "private_subnet3_a_route_table": "privateSubnet3ARouteTable",
        "private_subnet3_a_route_table_association": "privateSubnet3ARouteTableAssociation",
        "private_subnet3_b": "privateSubnet3B",
        "private_subnet3_b_network_acl": "privateSubnet3BNetworkAcl",
        "private_subnet3_b_network_acl_association": "privateSubnet3BNetworkAclAssociation",
        "private_subnet3_b_network_acl_entry_inbound": "privateSubnet3BNetworkAclEntryInbound",
        "private_subnet3_b_network_acl_entry_outbound": "privateSubnet3BNetworkAclEntryOutbound",
        "private_subnet3_b_route": "privateSubnet3BRoute",
        "private_subnet3_b_route_table": "privateSubnet3BRouteTable",
        "private_subnet3_b_route_table_association": "privateSubnet3BRouteTableAssociation",
        "private_subnet4_a": "privateSubnet4A",
        "private_subnet4_a_route": "privateSubnet4ARoute",
        "private_subnet4_a_route_table": "privateSubnet4ARouteTable",
        "private_subnet4_a_route_table_association": "privateSubnet4ARouteTableAssociation",
        "private_subnet4_b": "privateSubnet4B",
        "private_subnet4_b_network_acl": "privateSubnet4BNetworkAcl",
        "private_subnet4_b_network_acl_association": "privateSubnet4BNetworkAclAssociation",
        "private_subnet4_b_network_acl_entry_inbound": "privateSubnet4BNetworkAclEntryInbound",
        "private_subnet4_b_network_acl_entry_outbound": "privateSubnet4BNetworkAclEntryOutbound",
        "private_subnet4_b_route": "privateSubnet4BRoute",
        "private_subnet4_b_route_table": "privateSubnet4BRouteTable",
        "private_subnet4_b_route_table_association": "privateSubnet4BRouteTableAssociation",
        "public_subnet1": "publicSubnet1",
        "public_subnet1_route_table_association": "publicSubnet1RouteTableAssociation",
        "public_subnet2": "publicSubnet2",
        "public_subnet2_route_table_association": "publicSubnet2RouteTableAssociation",
        "public_subnet3": "publicSubnet3",
        "public_subnet3_route_table_association": "publicSubnet3RouteTableAssociation",
        "public_subnet4": "publicSubnet4",
        "public_subnet4_route_table_association": "publicSubnet4RouteTableAssociation",
        "public_subnet_route": "publicSubnetRoute",
        "public_subnet_route_table": "publicSubnetRouteTable",
        "s3_vpc_endpoint": "s3VpcEndpoint",
        "vpc": "vpc",
        "vpcdhcp_options_association": "vpcdhcpOptionsAssociation",
        "vpc_flow_logs_log_group": "vpcFlowLogsLogGroup",
        "vpc_flow_logs_role": "vpcFlowLogsRole",
        "vpc_flow_logs_to_cloud_watch": "vpcFlowLogsToCloudWatch",
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
        nat3_eip: typing.Optional["CfnModulePropsResourcesNat3Eip"] = None,
        nat4_eip: typing.Optional["CfnModulePropsResourcesNat4Eip"] = None,
        nat_gateway1: typing.Optional["CfnModulePropsResourcesNatGateway1"] = None,
        nat_gateway2: typing.Optional["CfnModulePropsResourcesNatGateway2"] = None,
        nat_gateway3: typing.Optional["CfnModulePropsResourcesNatGateway3"] = None,
        nat_gateway4: typing.Optional["CfnModulePropsResourcesNatGateway4"] = None,
        private_subnet1_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet1A"] = None,
        private_subnet1_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARoute"] = None,
        private_subnet1_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTable"] = None,
        private_subnet1_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation"] = None,
        private_subnet1_b: typing.Optional["CfnModulePropsResourcesPrivateSubnet1B"] = None,
        private_subnet1_b_network_acl: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAcl"] = None,
        private_subnet1_b_network_acl_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation"] = None,
        private_subnet1_b_network_acl_entry_inbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound"] = None,
        private_subnet1_b_network_acl_entry_outbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound"] = None,
        private_subnet1_b_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRoute"] = None,
        private_subnet1_b_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTable"] = None,
        private_subnet1_b_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation"] = None,
        private_subnet2_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet2A"] = None,
        private_subnet2_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARoute"] = None,
        private_subnet2_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTable"] = None,
        private_subnet2_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation"] = None,
        private_subnet2_b: typing.Optional["CfnModulePropsResourcesPrivateSubnet2B"] = None,
        private_subnet2_b_network_acl: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAcl"] = None,
        private_subnet2_b_network_acl_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation"] = None,
        private_subnet2_b_network_acl_entry_inbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound"] = None,
        private_subnet2_b_network_acl_entry_outbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound"] = None,
        private_subnet2_b_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRoute"] = None,
        private_subnet2_b_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTable"] = None,
        private_subnet2_b_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation"] = None,
        private_subnet3_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet3A"] = None,
        private_subnet3_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARoute"] = None,
        private_subnet3_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTable"] = None,
        private_subnet3_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation"] = None,
        private_subnet3_b: typing.Optional["CfnModulePropsResourcesPrivateSubnet3B"] = None,
        private_subnet3_b_network_acl: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAcl"] = None,
        private_subnet3_b_network_acl_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation"] = None,
        private_subnet3_b_network_acl_entry_inbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound"] = None,
        private_subnet3_b_network_acl_entry_outbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound"] = None,
        private_subnet3_b_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRoute"] = None,
        private_subnet3_b_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTable"] = None,
        private_subnet3_b_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation"] = None,
        private_subnet4_a: typing.Optional["CfnModulePropsResourcesPrivateSubnet4A"] = None,
        private_subnet4_a_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARoute"] = None,
        private_subnet4_a_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTable"] = None,
        private_subnet4_a_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation"] = None,
        private_subnet4_b: typing.Optional["CfnModulePropsResourcesPrivateSubnet4B"] = None,
        private_subnet4_b_network_acl: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAcl"] = None,
        private_subnet4_b_network_acl_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation"] = None,
        private_subnet4_b_network_acl_entry_inbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound"] = None,
        private_subnet4_b_network_acl_entry_outbound: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound"] = None,
        private_subnet4_b_route: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRoute"] = None,
        private_subnet4_b_route_table: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTable"] = None,
        private_subnet4_b_route_table_association: typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation"] = None,
        public_subnet1: typing.Optional["CfnModulePropsResourcesPublicSubnet1"] = None,
        public_subnet1_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"] = None,
        public_subnet2: typing.Optional["CfnModulePropsResourcesPublicSubnet2"] = None,
        public_subnet2_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"] = None,
        public_subnet3: typing.Optional["CfnModulePropsResourcesPublicSubnet3"] = None,
        public_subnet3_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"] = None,
        public_subnet4: typing.Optional["CfnModulePropsResourcesPublicSubnet4"] = None,
        public_subnet4_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet4RouteTableAssociation"] = None,
        public_subnet_route: typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"] = None,
        public_subnet_route_table: typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"] = None,
        s3_vpc_endpoint: typing.Optional["CfnModulePropsResourcesS3VpcEndpoint"] = None,
        vpc: typing.Optional["CfnModulePropsResourcesVpc"] = None,
        vpcdhcp_options_association: typing.Optional["CfnModulePropsResourcesVpcdhcpOptionsAssociation"] = None,
        vpc_flow_logs_log_group: typing.Optional["CfnModulePropsResourcesVpcFlowLogsLogGroup"] = None,
        vpc_flow_logs_role: typing.Optional["CfnModulePropsResourcesVpcFlowLogsRole"] = None,
        vpc_flow_logs_to_cloud_watch: typing.Optional["CfnModulePropsResourcesVpcFlowLogsToCloudWatch"] = None,
        vpc_gateway_attachment: typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"] = None,
    ) -> None:
        '''
        :param dhcp_options: 
        :param internet_gateway: 
        :param nat1_eip: 
        :param nat2_eip: 
        :param nat3_eip: 
        :param nat4_eip: 
        :param nat_gateway1: 
        :param nat_gateway2: 
        :param nat_gateway3: 
        :param nat_gateway4: 
        :param private_subnet1_a: 
        :param private_subnet1_a_route: 
        :param private_subnet1_a_route_table: 
        :param private_subnet1_a_route_table_association: 
        :param private_subnet1_b: 
        :param private_subnet1_b_network_acl: 
        :param private_subnet1_b_network_acl_association: 
        :param private_subnet1_b_network_acl_entry_inbound: 
        :param private_subnet1_b_network_acl_entry_outbound: 
        :param private_subnet1_b_route: 
        :param private_subnet1_b_route_table: 
        :param private_subnet1_b_route_table_association: 
        :param private_subnet2_a: 
        :param private_subnet2_a_route: 
        :param private_subnet2_a_route_table: 
        :param private_subnet2_a_route_table_association: 
        :param private_subnet2_b: 
        :param private_subnet2_b_network_acl: 
        :param private_subnet2_b_network_acl_association: 
        :param private_subnet2_b_network_acl_entry_inbound: 
        :param private_subnet2_b_network_acl_entry_outbound: 
        :param private_subnet2_b_route: 
        :param private_subnet2_b_route_table: 
        :param private_subnet2_b_route_table_association: 
        :param private_subnet3_a: 
        :param private_subnet3_a_route: 
        :param private_subnet3_a_route_table: 
        :param private_subnet3_a_route_table_association: 
        :param private_subnet3_b: 
        :param private_subnet3_b_network_acl: 
        :param private_subnet3_b_network_acl_association: 
        :param private_subnet3_b_network_acl_entry_inbound: 
        :param private_subnet3_b_network_acl_entry_outbound: 
        :param private_subnet3_b_route: 
        :param private_subnet3_b_route_table: 
        :param private_subnet3_b_route_table_association: 
        :param private_subnet4_a: 
        :param private_subnet4_a_route: 
        :param private_subnet4_a_route_table: 
        :param private_subnet4_a_route_table_association: 
        :param private_subnet4_b: 
        :param private_subnet4_b_network_acl: 
        :param private_subnet4_b_network_acl_association: 
        :param private_subnet4_b_network_acl_entry_inbound: 
        :param private_subnet4_b_network_acl_entry_outbound: 
        :param private_subnet4_b_route: 
        :param private_subnet4_b_route_table: 
        :param private_subnet4_b_route_table_association: 
        :param public_subnet1: 
        :param public_subnet1_route_table_association: 
        :param public_subnet2: 
        :param public_subnet2_route_table_association: 
        :param public_subnet3: 
        :param public_subnet3_route_table_association: 
        :param public_subnet4: 
        :param public_subnet4_route_table_association: 
        :param public_subnet_route: 
        :param public_subnet_route_table: 
        :param s3_vpc_endpoint: 
        :param vpc: 
        :param vpcdhcp_options_association: 
        :param vpc_flow_logs_log_group: 
        :param vpc_flow_logs_role: 
        :param vpc_flow_logs_to_cloud_watch: 
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
        if isinstance(nat3_eip, dict):
            nat3_eip = CfnModulePropsResourcesNat3Eip(**nat3_eip)
        if isinstance(nat4_eip, dict):
            nat4_eip = CfnModulePropsResourcesNat4Eip(**nat4_eip)
        if isinstance(nat_gateway1, dict):
            nat_gateway1 = CfnModulePropsResourcesNatGateway1(**nat_gateway1)
        if isinstance(nat_gateway2, dict):
            nat_gateway2 = CfnModulePropsResourcesNatGateway2(**nat_gateway2)
        if isinstance(nat_gateway3, dict):
            nat_gateway3 = CfnModulePropsResourcesNatGateway3(**nat_gateway3)
        if isinstance(nat_gateway4, dict):
            nat_gateway4 = CfnModulePropsResourcesNatGateway4(**nat_gateway4)
        if isinstance(private_subnet1_a, dict):
            private_subnet1_a = CfnModulePropsResourcesPrivateSubnet1A(**private_subnet1_a)
        if isinstance(private_subnet1_a_route, dict):
            private_subnet1_a_route = CfnModulePropsResourcesPrivateSubnet1ARoute(**private_subnet1_a_route)
        if isinstance(private_subnet1_a_route_table, dict):
            private_subnet1_a_route_table = CfnModulePropsResourcesPrivateSubnet1ARouteTable(**private_subnet1_a_route_table)
        if isinstance(private_subnet1_a_route_table_association, dict):
            private_subnet1_a_route_table_association = CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation(**private_subnet1_a_route_table_association)
        if isinstance(private_subnet1_b, dict):
            private_subnet1_b = CfnModulePropsResourcesPrivateSubnet1B(**private_subnet1_b)
        if isinstance(private_subnet1_b_network_acl, dict):
            private_subnet1_b_network_acl = CfnModulePropsResourcesPrivateSubnet1BNetworkAcl(**private_subnet1_b_network_acl)
        if isinstance(private_subnet1_b_network_acl_association, dict):
            private_subnet1_b_network_acl_association = CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation(**private_subnet1_b_network_acl_association)
        if isinstance(private_subnet1_b_network_acl_entry_inbound, dict):
            private_subnet1_b_network_acl_entry_inbound = CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound(**private_subnet1_b_network_acl_entry_inbound)
        if isinstance(private_subnet1_b_network_acl_entry_outbound, dict):
            private_subnet1_b_network_acl_entry_outbound = CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound(**private_subnet1_b_network_acl_entry_outbound)
        if isinstance(private_subnet1_b_route, dict):
            private_subnet1_b_route = CfnModulePropsResourcesPrivateSubnet1BRoute(**private_subnet1_b_route)
        if isinstance(private_subnet1_b_route_table, dict):
            private_subnet1_b_route_table = CfnModulePropsResourcesPrivateSubnet1BRouteTable(**private_subnet1_b_route_table)
        if isinstance(private_subnet1_b_route_table_association, dict):
            private_subnet1_b_route_table_association = CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation(**private_subnet1_b_route_table_association)
        if isinstance(private_subnet2_a, dict):
            private_subnet2_a = CfnModulePropsResourcesPrivateSubnet2A(**private_subnet2_a)
        if isinstance(private_subnet2_a_route, dict):
            private_subnet2_a_route = CfnModulePropsResourcesPrivateSubnet2ARoute(**private_subnet2_a_route)
        if isinstance(private_subnet2_a_route_table, dict):
            private_subnet2_a_route_table = CfnModulePropsResourcesPrivateSubnet2ARouteTable(**private_subnet2_a_route_table)
        if isinstance(private_subnet2_a_route_table_association, dict):
            private_subnet2_a_route_table_association = CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation(**private_subnet2_a_route_table_association)
        if isinstance(private_subnet2_b, dict):
            private_subnet2_b = CfnModulePropsResourcesPrivateSubnet2B(**private_subnet2_b)
        if isinstance(private_subnet2_b_network_acl, dict):
            private_subnet2_b_network_acl = CfnModulePropsResourcesPrivateSubnet2BNetworkAcl(**private_subnet2_b_network_acl)
        if isinstance(private_subnet2_b_network_acl_association, dict):
            private_subnet2_b_network_acl_association = CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation(**private_subnet2_b_network_acl_association)
        if isinstance(private_subnet2_b_network_acl_entry_inbound, dict):
            private_subnet2_b_network_acl_entry_inbound = CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound(**private_subnet2_b_network_acl_entry_inbound)
        if isinstance(private_subnet2_b_network_acl_entry_outbound, dict):
            private_subnet2_b_network_acl_entry_outbound = CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound(**private_subnet2_b_network_acl_entry_outbound)
        if isinstance(private_subnet2_b_route, dict):
            private_subnet2_b_route = CfnModulePropsResourcesPrivateSubnet2BRoute(**private_subnet2_b_route)
        if isinstance(private_subnet2_b_route_table, dict):
            private_subnet2_b_route_table = CfnModulePropsResourcesPrivateSubnet2BRouteTable(**private_subnet2_b_route_table)
        if isinstance(private_subnet2_b_route_table_association, dict):
            private_subnet2_b_route_table_association = CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation(**private_subnet2_b_route_table_association)
        if isinstance(private_subnet3_a, dict):
            private_subnet3_a = CfnModulePropsResourcesPrivateSubnet3A(**private_subnet3_a)
        if isinstance(private_subnet3_a_route, dict):
            private_subnet3_a_route = CfnModulePropsResourcesPrivateSubnet3ARoute(**private_subnet3_a_route)
        if isinstance(private_subnet3_a_route_table, dict):
            private_subnet3_a_route_table = CfnModulePropsResourcesPrivateSubnet3ARouteTable(**private_subnet3_a_route_table)
        if isinstance(private_subnet3_a_route_table_association, dict):
            private_subnet3_a_route_table_association = CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation(**private_subnet3_a_route_table_association)
        if isinstance(private_subnet3_b, dict):
            private_subnet3_b = CfnModulePropsResourcesPrivateSubnet3B(**private_subnet3_b)
        if isinstance(private_subnet3_b_network_acl, dict):
            private_subnet3_b_network_acl = CfnModulePropsResourcesPrivateSubnet3BNetworkAcl(**private_subnet3_b_network_acl)
        if isinstance(private_subnet3_b_network_acl_association, dict):
            private_subnet3_b_network_acl_association = CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation(**private_subnet3_b_network_acl_association)
        if isinstance(private_subnet3_b_network_acl_entry_inbound, dict):
            private_subnet3_b_network_acl_entry_inbound = CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound(**private_subnet3_b_network_acl_entry_inbound)
        if isinstance(private_subnet3_b_network_acl_entry_outbound, dict):
            private_subnet3_b_network_acl_entry_outbound = CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound(**private_subnet3_b_network_acl_entry_outbound)
        if isinstance(private_subnet3_b_route, dict):
            private_subnet3_b_route = CfnModulePropsResourcesPrivateSubnet3BRoute(**private_subnet3_b_route)
        if isinstance(private_subnet3_b_route_table, dict):
            private_subnet3_b_route_table = CfnModulePropsResourcesPrivateSubnet3BRouteTable(**private_subnet3_b_route_table)
        if isinstance(private_subnet3_b_route_table_association, dict):
            private_subnet3_b_route_table_association = CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation(**private_subnet3_b_route_table_association)
        if isinstance(private_subnet4_a, dict):
            private_subnet4_a = CfnModulePropsResourcesPrivateSubnet4A(**private_subnet4_a)
        if isinstance(private_subnet4_a_route, dict):
            private_subnet4_a_route = CfnModulePropsResourcesPrivateSubnet4ARoute(**private_subnet4_a_route)
        if isinstance(private_subnet4_a_route_table, dict):
            private_subnet4_a_route_table = CfnModulePropsResourcesPrivateSubnet4ARouteTable(**private_subnet4_a_route_table)
        if isinstance(private_subnet4_a_route_table_association, dict):
            private_subnet4_a_route_table_association = CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation(**private_subnet4_a_route_table_association)
        if isinstance(private_subnet4_b, dict):
            private_subnet4_b = CfnModulePropsResourcesPrivateSubnet4B(**private_subnet4_b)
        if isinstance(private_subnet4_b_network_acl, dict):
            private_subnet4_b_network_acl = CfnModulePropsResourcesPrivateSubnet4BNetworkAcl(**private_subnet4_b_network_acl)
        if isinstance(private_subnet4_b_network_acl_association, dict):
            private_subnet4_b_network_acl_association = CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation(**private_subnet4_b_network_acl_association)
        if isinstance(private_subnet4_b_network_acl_entry_inbound, dict):
            private_subnet4_b_network_acl_entry_inbound = CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound(**private_subnet4_b_network_acl_entry_inbound)
        if isinstance(private_subnet4_b_network_acl_entry_outbound, dict):
            private_subnet4_b_network_acl_entry_outbound = CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound(**private_subnet4_b_network_acl_entry_outbound)
        if isinstance(private_subnet4_b_route, dict):
            private_subnet4_b_route = CfnModulePropsResourcesPrivateSubnet4BRoute(**private_subnet4_b_route)
        if isinstance(private_subnet4_b_route_table, dict):
            private_subnet4_b_route_table = CfnModulePropsResourcesPrivateSubnet4BRouteTable(**private_subnet4_b_route_table)
        if isinstance(private_subnet4_b_route_table_association, dict):
            private_subnet4_b_route_table_association = CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation(**private_subnet4_b_route_table_association)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet3, dict):
            public_subnet3 = CfnModulePropsResourcesPublicSubnet3(**public_subnet3)
        if isinstance(public_subnet3_route_table_association, dict):
            public_subnet3_route_table_association = CfnModulePropsResourcesPublicSubnet3RouteTableAssociation(**public_subnet3_route_table_association)
        if isinstance(public_subnet4, dict):
            public_subnet4 = CfnModulePropsResourcesPublicSubnet4(**public_subnet4)
        if isinstance(public_subnet4_route_table_association, dict):
            public_subnet4_route_table_association = CfnModulePropsResourcesPublicSubnet4RouteTableAssociation(**public_subnet4_route_table_association)
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
        if isinstance(vpc_flow_logs_log_group, dict):
            vpc_flow_logs_log_group = CfnModulePropsResourcesVpcFlowLogsLogGroup(**vpc_flow_logs_log_group)
        if isinstance(vpc_flow_logs_role, dict):
            vpc_flow_logs_role = CfnModulePropsResourcesVpcFlowLogsRole(**vpc_flow_logs_role)
        if isinstance(vpc_flow_logs_to_cloud_watch, dict):
            vpc_flow_logs_to_cloud_watch = CfnModulePropsResourcesVpcFlowLogsToCloudWatch(**vpc_flow_logs_to_cloud_watch)
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
        if nat3_eip is not None:
            self._values["nat3_eip"] = nat3_eip
        if nat4_eip is not None:
            self._values["nat4_eip"] = nat4_eip
        if nat_gateway1 is not None:
            self._values["nat_gateway1"] = nat_gateway1
        if nat_gateway2 is not None:
            self._values["nat_gateway2"] = nat_gateway2
        if nat_gateway3 is not None:
            self._values["nat_gateway3"] = nat_gateway3
        if nat_gateway4 is not None:
            self._values["nat_gateway4"] = nat_gateway4
        if private_subnet1_a is not None:
            self._values["private_subnet1_a"] = private_subnet1_a
        if private_subnet1_a_route is not None:
            self._values["private_subnet1_a_route"] = private_subnet1_a_route
        if private_subnet1_a_route_table is not None:
            self._values["private_subnet1_a_route_table"] = private_subnet1_a_route_table
        if private_subnet1_a_route_table_association is not None:
            self._values["private_subnet1_a_route_table_association"] = private_subnet1_a_route_table_association
        if private_subnet1_b is not None:
            self._values["private_subnet1_b"] = private_subnet1_b
        if private_subnet1_b_network_acl is not None:
            self._values["private_subnet1_b_network_acl"] = private_subnet1_b_network_acl
        if private_subnet1_b_network_acl_association is not None:
            self._values["private_subnet1_b_network_acl_association"] = private_subnet1_b_network_acl_association
        if private_subnet1_b_network_acl_entry_inbound is not None:
            self._values["private_subnet1_b_network_acl_entry_inbound"] = private_subnet1_b_network_acl_entry_inbound
        if private_subnet1_b_network_acl_entry_outbound is not None:
            self._values["private_subnet1_b_network_acl_entry_outbound"] = private_subnet1_b_network_acl_entry_outbound
        if private_subnet1_b_route is not None:
            self._values["private_subnet1_b_route"] = private_subnet1_b_route
        if private_subnet1_b_route_table is not None:
            self._values["private_subnet1_b_route_table"] = private_subnet1_b_route_table
        if private_subnet1_b_route_table_association is not None:
            self._values["private_subnet1_b_route_table_association"] = private_subnet1_b_route_table_association
        if private_subnet2_a is not None:
            self._values["private_subnet2_a"] = private_subnet2_a
        if private_subnet2_a_route is not None:
            self._values["private_subnet2_a_route"] = private_subnet2_a_route
        if private_subnet2_a_route_table is not None:
            self._values["private_subnet2_a_route_table"] = private_subnet2_a_route_table
        if private_subnet2_a_route_table_association is not None:
            self._values["private_subnet2_a_route_table_association"] = private_subnet2_a_route_table_association
        if private_subnet2_b is not None:
            self._values["private_subnet2_b"] = private_subnet2_b
        if private_subnet2_b_network_acl is not None:
            self._values["private_subnet2_b_network_acl"] = private_subnet2_b_network_acl
        if private_subnet2_b_network_acl_association is not None:
            self._values["private_subnet2_b_network_acl_association"] = private_subnet2_b_network_acl_association
        if private_subnet2_b_network_acl_entry_inbound is not None:
            self._values["private_subnet2_b_network_acl_entry_inbound"] = private_subnet2_b_network_acl_entry_inbound
        if private_subnet2_b_network_acl_entry_outbound is not None:
            self._values["private_subnet2_b_network_acl_entry_outbound"] = private_subnet2_b_network_acl_entry_outbound
        if private_subnet2_b_route is not None:
            self._values["private_subnet2_b_route"] = private_subnet2_b_route
        if private_subnet2_b_route_table is not None:
            self._values["private_subnet2_b_route_table"] = private_subnet2_b_route_table
        if private_subnet2_b_route_table_association is not None:
            self._values["private_subnet2_b_route_table_association"] = private_subnet2_b_route_table_association
        if private_subnet3_a is not None:
            self._values["private_subnet3_a"] = private_subnet3_a
        if private_subnet3_a_route is not None:
            self._values["private_subnet3_a_route"] = private_subnet3_a_route
        if private_subnet3_a_route_table is not None:
            self._values["private_subnet3_a_route_table"] = private_subnet3_a_route_table
        if private_subnet3_a_route_table_association is not None:
            self._values["private_subnet3_a_route_table_association"] = private_subnet3_a_route_table_association
        if private_subnet3_b is not None:
            self._values["private_subnet3_b"] = private_subnet3_b
        if private_subnet3_b_network_acl is not None:
            self._values["private_subnet3_b_network_acl"] = private_subnet3_b_network_acl
        if private_subnet3_b_network_acl_association is not None:
            self._values["private_subnet3_b_network_acl_association"] = private_subnet3_b_network_acl_association
        if private_subnet3_b_network_acl_entry_inbound is not None:
            self._values["private_subnet3_b_network_acl_entry_inbound"] = private_subnet3_b_network_acl_entry_inbound
        if private_subnet3_b_network_acl_entry_outbound is not None:
            self._values["private_subnet3_b_network_acl_entry_outbound"] = private_subnet3_b_network_acl_entry_outbound
        if private_subnet3_b_route is not None:
            self._values["private_subnet3_b_route"] = private_subnet3_b_route
        if private_subnet3_b_route_table is not None:
            self._values["private_subnet3_b_route_table"] = private_subnet3_b_route_table
        if private_subnet3_b_route_table_association is not None:
            self._values["private_subnet3_b_route_table_association"] = private_subnet3_b_route_table_association
        if private_subnet4_a is not None:
            self._values["private_subnet4_a"] = private_subnet4_a
        if private_subnet4_a_route is not None:
            self._values["private_subnet4_a_route"] = private_subnet4_a_route
        if private_subnet4_a_route_table is not None:
            self._values["private_subnet4_a_route_table"] = private_subnet4_a_route_table
        if private_subnet4_a_route_table_association is not None:
            self._values["private_subnet4_a_route_table_association"] = private_subnet4_a_route_table_association
        if private_subnet4_b is not None:
            self._values["private_subnet4_b"] = private_subnet4_b
        if private_subnet4_b_network_acl is not None:
            self._values["private_subnet4_b_network_acl"] = private_subnet4_b_network_acl
        if private_subnet4_b_network_acl_association is not None:
            self._values["private_subnet4_b_network_acl_association"] = private_subnet4_b_network_acl_association
        if private_subnet4_b_network_acl_entry_inbound is not None:
            self._values["private_subnet4_b_network_acl_entry_inbound"] = private_subnet4_b_network_acl_entry_inbound
        if private_subnet4_b_network_acl_entry_outbound is not None:
            self._values["private_subnet4_b_network_acl_entry_outbound"] = private_subnet4_b_network_acl_entry_outbound
        if private_subnet4_b_route is not None:
            self._values["private_subnet4_b_route"] = private_subnet4_b_route
        if private_subnet4_b_route_table is not None:
            self._values["private_subnet4_b_route_table"] = private_subnet4_b_route_table
        if private_subnet4_b_route_table_association is not None:
            self._values["private_subnet4_b_route_table_association"] = private_subnet4_b_route_table_association
        if public_subnet1 is not None:
            self._values["public_subnet1"] = public_subnet1
        if public_subnet1_route_table_association is not None:
            self._values["public_subnet1_route_table_association"] = public_subnet1_route_table_association
        if public_subnet2 is not None:
            self._values["public_subnet2"] = public_subnet2
        if public_subnet2_route_table_association is not None:
            self._values["public_subnet2_route_table_association"] = public_subnet2_route_table_association
        if public_subnet3 is not None:
            self._values["public_subnet3"] = public_subnet3
        if public_subnet3_route_table_association is not None:
            self._values["public_subnet3_route_table_association"] = public_subnet3_route_table_association
        if public_subnet4 is not None:
            self._values["public_subnet4"] = public_subnet4
        if public_subnet4_route_table_association is not None:
            self._values["public_subnet4_route_table_association"] = public_subnet4_route_table_association
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
        if vpc_flow_logs_log_group is not None:
            self._values["vpc_flow_logs_log_group"] = vpc_flow_logs_log_group
        if vpc_flow_logs_role is not None:
            self._values["vpc_flow_logs_role"] = vpc_flow_logs_role
        if vpc_flow_logs_to_cloud_watch is not None:
            self._values["vpc_flow_logs_to_cloud_watch"] = vpc_flow_logs_to_cloud_watch
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
    def nat3_eip(self) -> typing.Optional["CfnModulePropsResourcesNat3Eip"]:
        '''
        :schema: CfnModulePropsResources#NAT3EIP
        '''
        result = self._values.get("nat3_eip")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNat3Eip"], result)

    @builtins.property
    def nat4_eip(self) -> typing.Optional["CfnModulePropsResourcesNat4Eip"]:
        '''
        :schema: CfnModulePropsResources#NAT4EIP
        '''
        result = self._values.get("nat4_eip")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNat4Eip"], result)

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
    def nat_gateway3(self) -> typing.Optional["CfnModulePropsResourcesNatGateway3"]:
        '''
        :schema: CfnModulePropsResources#NATGateway3
        '''
        result = self._values.get("nat_gateway3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNatGateway3"], result)

    @builtins.property
    def nat_gateway4(self) -> typing.Optional["CfnModulePropsResourcesNatGateway4"]:
        '''
        :schema: CfnModulePropsResources#NATGateway4
        '''
        result = self._values.get("nat_gateway4")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNatGateway4"], result)

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
    def private_subnet1_b(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1B"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1B
        '''
        result = self._values.get("private_subnet1_b")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1B"], result)

    @builtins.property
    def private_subnet1_b_network_acl(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAcl"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BNetworkAcl
        '''
        result = self._values.get("private_subnet1_b_network_acl")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAcl"], result)

    @builtins.property
    def private_subnet1_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet1_b_network_acl_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet1_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet1_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet1_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet1_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet1_b_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BRoute
        '''
        result = self._values.get("private_subnet1_b_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRoute"], result)

    @builtins.property
    def private_subnet1_b_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BRouteTable
        '''
        result = self._values.get("private_subnet1_b_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTable"], result)

    @builtins.property
    def private_subnet1_b_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1BRouteTableAssociation
        '''
        result = self._values.get("private_subnet1_b_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation"], result)

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
    def private_subnet2_b(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2B"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2B
        '''
        result = self._values.get("private_subnet2_b")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2B"], result)

    @builtins.property
    def private_subnet2_b_network_acl(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAcl"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BNetworkAcl
        '''
        result = self._values.get("private_subnet2_b_network_acl")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAcl"], result)

    @builtins.property
    def private_subnet2_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet2_b_network_acl_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet2_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet2_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet2_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet2_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet2_b_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BRoute
        '''
        result = self._values.get("private_subnet2_b_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRoute"], result)

    @builtins.property
    def private_subnet2_b_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BRouteTable
        '''
        result = self._values.get("private_subnet2_b_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTable"], result)

    @builtins.property
    def private_subnet2_b_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2BRouteTableAssociation
        '''
        result = self._values.get("private_subnet2_b_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation"], result)

    @builtins.property
    def private_subnet3_a(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3A"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3A
        '''
        result = self._values.get("private_subnet3_a")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3A"], result)

    @builtins.property
    def private_subnet3_a_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3ARoute
        '''
        result = self._values.get("private_subnet3_a_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARoute"], result)

    @builtins.property
    def private_subnet3_a_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3ARouteTable
        '''
        result = self._values.get("private_subnet3_a_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTable"], result)

    @builtins.property
    def private_subnet3_a_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3ARouteTableAssociation
        '''
        result = self._values.get("private_subnet3_a_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet3_b(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3B"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3B
        '''
        result = self._values.get("private_subnet3_b")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3B"], result)

    @builtins.property
    def private_subnet3_b_network_acl(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAcl"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BNetworkAcl
        '''
        result = self._values.get("private_subnet3_b_network_acl")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAcl"], result)

    @builtins.property
    def private_subnet3_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet3_b_network_acl_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet3_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet3_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet3_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet3_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet3_b_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BRoute
        '''
        result = self._values.get("private_subnet3_b_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRoute"], result)

    @builtins.property
    def private_subnet3_b_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BRouteTable
        '''
        result = self._values.get("private_subnet3_b_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTable"], result)

    @builtins.property
    def private_subnet3_b_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3BRouteTableAssociation
        '''
        result = self._values.get("private_subnet3_b_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation"], result)

    @builtins.property
    def private_subnet4_a(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4A"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4A
        '''
        result = self._values.get("private_subnet4_a")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4A"], result)

    @builtins.property
    def private_subnet4_a_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4ARoute
        '''
        result = self._values.get("private_subnet4_a_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARoute"], result)

    @builtins.property
    def private_subnet4_a_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4ARouteTable
        '''
        result = self._values.get("private_subnet4_a_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTable"], result)

    @builtins.property
    def private_subnet4_a_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4ARouteTableAssociation
        '''
        result = self._values.get("private_subnet4_a_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet4_b(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4B"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4B
        '''
        result = self._values.get("private_subnet4_b")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4B"], result)

    @builtins.property
    def private_subnet4_b_network_acl(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAcl"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BNetworkAcl
        '''
        result = self._values.get("private_subnet4_b_network_acl")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAcl"], result)

    @builtins.property
    def private_subnet4_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet4_b_network_acl_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet4_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet4_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet4_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet4_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet4_b_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRoute"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BRoute
        '''
        result = self._values.get("private_subnet4_b_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRoute"], result)

    @builtins.property
    def private_subnet4_b_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BRouteTable
        '''
        result = self._values.get("private_subnet4_b_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTable"], result)

    @builtins.property
    def private_subnet4_b_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4BRouteTableAssociation
        '''
        result = self._values.get("private_subnet4_b_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation"], result)

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
    def public_subnet3(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet3"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet3
        '''
        result = self._values.get("public_subnet3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet3"], result)

    @builtins.property
    def public_subnet3_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet3RouteTableAssociation
        '''
        result = self._values.get("public_subnet3_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"], result)

    @builtins.property
    def public_subnet4(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet4"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet4
        '''
        result = self._values.get("public_subnet4")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet4"], result)

    @builtins.property
    def public_subnet4_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet4RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet4RouteTableAssociation
        '''
        result = self._values.get("public_subnet4_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet4RouteTableAssociation"], result)

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
    def vpc_flow_logs_log_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcFlowLogsLogGroup"]:
        '''
        :schema: CfnModulePropsResources#VPCFlowLogsLogGroup
        '''
        result = self._values.get("vpc_flow_logs_log_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcFlowLogsLogGroup"], result)

    @builtins.property
    def vpc_flow_logs_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcFlowLogsRole"]:
        '''
        :schema: CfnModulePropsResources#VPCFlowLogsRole
        '''
        result = self._values.get("vpc_flow_logs_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcFlowLogsRole"], result)

    @builtins.property
    def vpc_flow_logs_to_cloud_watch(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcFlowLogsToCloudWatch"]:
        '''
        :schema: CfnModulePropsResources#VPCFlowLogsToCloudWatch
        '''
        result = self._values.get("vpc_flow_logs_to_cloud_watch")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcFlowLogsToCloudWatch"], result)

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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesDhcpOptions",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesInternetGateway",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNat1Eip",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNat2Eip",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNat3Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNat3Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNat3Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNat3Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNat3Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNat3Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNat4Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNat4Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNat4Eip
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNat4Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNat4Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNat4Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNatGateway1",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNatGateway2",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNatGateway3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNatGateway3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNatGateway3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNatGateway3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNatGateway3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNatGateway3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesNatGateway4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNatGateway4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNatGateway4
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNatGateway4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNatGateway4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNatGateway4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1A",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1ARoute",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1ARouteTable",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1B
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAcl
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2A",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2ARoute",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2ARouteTable",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2B
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAcl
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3B
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAcl
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4A
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4ARoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4B
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAcl
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet1",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet2",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet3RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet3RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet3RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet4
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnet4RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet4RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet4RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet4RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet4RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet4RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnetRoute",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesPublicSubnetRouteTable",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesS3VpcEndpoint",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpc",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpcFlowLogsLogGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcFlowLogsLogGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcFlowLogsLogGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsLogGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsLogGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcFlowLogsLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpcFlowLogsRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcFlowLogsRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcFlowLogsRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcFlowLogsRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpcFlowLogsToCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcFlowLogsToCloudWatch:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcFlowLogsToCloudWatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsToCloudWatch#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcFlowLogsToCloudWatch#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcFlowLogsToCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpcGatewayAttachment",
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
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnModulePropsResourcesVpcdhcpOptionsAssociation",
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
    "CfnModulePropsParametersAvailabilityZones",
    "CfnModulePropsParametersCreateAdditionalPrivateSubnets",
    "CfnModulePropsParametersCreateNatGateways",
    "CfnModulePropsParametersCreatePrivateSubnets",
    "CfnModulePropsParametersCreatePublicSubnets",
    "CfnModulePropsParametersCreateVpcFlowLogsToCloudWatch",
    "CfnModulePropsParametersNumberOfAZs",
    "CfnModulePropsParametersPrivateSubnet1Acidr",
    "CfnModulePropsParametersPrivateSubnet1Bcidr",
    "CfnModulePropsParametersPrivateSubnet2Acidr",
    "CfnModulePropsParametersPrivateSubnet2Bcidr",
    "CfnModulePropsParametersPrivateSubnet3Acidr",
    "CfnModulePropsParametersPrivateSubnet3Bcidr",
    "CfnModulePropsParametersPrivateSubnet4Acidr",
    "CfnModulePropsParametersPrivateSubnet4Bcidr",
    "CfnModulePropsParametersPrivateSubnetATag1",
    "CfnModulePropsParametersPrivateSubnetATag2",
    "CfnModulePropsParametersPrivateSubnetATag3",
    "CfnModulePropsParametersPrivateSubnetBTag1",
    "CfnModulePropsParametersPrivateSubnetBTag2",
    "CfnModulePropsParametersPrivateSubnetBTag3",
    "CfnModulePropsParametersPublicSubnet1Cidr",
    "CfnModulePropsParametersPublicSubnet2Cidr",
    "CfnModulePropsParametersPublicSubnet3Cidr",
    "CfnModulePropsParametersPublicSubnet4Cidr",
    "CfnModulePropsParametersPublicSubnetTag1",
    "CfnModulePropsParametersPublicSubnetTag2",
    "CfnModulePropsParametersPublicSubnetTag3",
    "CfnModulePropsParametersVpcFlowLogsCloudWatchKmsKey",
    "CfnModulePropsParametersVpcFlowLogsLogFormat",
    "CfnModulePropsParametersVpcFlowLogsLogGroupRetention",
    "CfnModulePropsParametersVpcFlowLogsMaxAggregationInterval",
    "CfnModulePropsParametersVpcFlowLogsTrafficType",
    "CfnModulePropsParametersVpcTenancy",
    "CfnModulePropsParametersVpccidr",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesDhcpOptions",
    "CfnModulePropsResourcesInternetGateway",
    "CfnModulePropsResourcesNat1Eip",
    "CfnModulePropsResourcesNat2Eip",
    "CfnModulePropsResourcesNat3Eip",
    "CfnModulePropsResourcesNat4Eip",
    "CfnModulePropsResourcesNatGateway1",
    "CfnModulePropsResourcesNatGateway2",
    "CfnModulePropsResourcesNatGateway3",
    "CfnModulePropsResourcesNatGateway4",
    "CfnModulePropsResourcesPrivateSubnet1A",
    "CfnModulePropsResourcesPrivateSubnet1ARoute",
    "CfnModulePropsResourcesPrivateSubnet1ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet1B",
    "CfnModulePropsResourcesPrivateSubnet1BNetworkAcl",
    "CfnModulePropsResourcesPrivateSubnet1BNetworkAclAssociation",
    "CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound",
    "CfnModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound",
    "CfnModulePropsResourcesPrivateSubnet1BRoute",
    "CfnModulePropsResourcesPrivateSubnet1BRouteTable",
    "CfnModulePropsResourcesPrivateSubnet1BRouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet2A",
    "CfnModulePropsResourcesPrivateSubnet2ARoute",
    "CfnModulePropsResourcesPrivateSubnet2ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet2B",
    "CfnModulePropsResourcesPrivateSubnet2BNetworkAcl",
    "CfnModulePropsResourcesPrivateSubnet2BNetworkAclAssociation",
    "CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound",
    "CfnModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound",
    "CfnModulePropsResourcesPrivateSubnet2BRoute",
    "CfnModulePropsResourcesPrivateSubnet2BRouteTable",
    "CfnModulePropsResourcesPrivateSubnet2BRouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet3A",
    "CfnModulePropsResourcesPrivateSubnet3ARoute",
    "CfnModulePropsResourcesPrivateSubnet3ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet3ARouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet3B",
    "CfnModulePropsResourcesPrivateSubnet3BNetworkAcl",
    "CfnModulePropsResourcesPrivateSubnet3BNetworkAclAssociation",
    "CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound",
    "CfnModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound",
    "CfnModulePropsResourcesPrivateSubnet3BRoute",
    "CfnModulePropsResourcesPrivateSubnet3BRouteTable",
    "CfnModulePropsResourcesPrivateSubnet3BRouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet4A",
    "CfnModulePropsResourcesPrivateSubnet4ARoute",
    "CfnModulePropsResourcesPrivateSubnet4ARouteTable",
    "CfnModulePropsResourcesPrivateSubnet4ARouteTableAssociation",
    "CfnModulePropsResourcesPrivateSubnet4B",
    "CfnModulePropsResourcesPrivateSubnet4BNetworkAcl",
    "CfnModulePropsResourcesPrivateSubnet4BNetworkAclAssociation",
    "CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound",
    "CfnModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound",
    "CfnModulePropsResourcesPrivateSubnet4BRoute",
    "CfnModulePropsResourcesPrivateSubnet4BRouteTable",
    "CfnModulePropsResourcesPrivateSubnet4BRouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet1",
    "CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet2",
    "CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet3",
    "CfnModulePropsResourcesPublicSubnet3RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet4",
    "CfnModulePropsResourcesPublicSubnet4RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnetRoute",
    "CfnModulePropsResourcesPublicSubnetRouteTable",
    "CfnModulePropsResourcesS3VpcEndpoint",
    "CfnModulePropsResourcesVpc",
    "CfnModulePropsResourcesVpcFlowLogsLogGroup",
    "CfnModulePropsResourcesVpcFlowLogsRole",
    "CfnModulePropsResourcesVpcFlowLogsToCloudWatch",
    "CfnModulePropsResourcesVpcGatewayAttachment",
    "CfnModulePropsResourcesVpcdhcpOptionsAssociation",
]

publication.publish()
