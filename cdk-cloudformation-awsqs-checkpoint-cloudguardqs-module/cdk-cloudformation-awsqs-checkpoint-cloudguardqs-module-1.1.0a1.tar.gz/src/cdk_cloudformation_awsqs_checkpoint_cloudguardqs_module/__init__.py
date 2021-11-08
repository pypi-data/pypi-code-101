'''
# AWS CDK CloudFormation Constructs for AWSQS::CheckPoint::CloudGuardQS::MODULE

Schema for Module Fragment of type AWSQS::CheckPoint::CloudGuardQS::MODULE

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModule",
):
    '''A CloudFormation ``AWSQS::CheckPoint::CloudGuardQS::MODULE``.

    :cloudformationResource: AWSQS::CheckPoint::CloudGuardQS::MODULE
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
        '''Create a new ``AWSQS::CheckPoint::CloudGuardQS::MODULE``.

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type AWSQS::CheckPoint::CloudGuardQS::MODULE.

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "admin_cidr": "adminCidr",
        "admin_email": "adminEmail",
        "alb_protocol": "albProtocol",
        "allocate_public_address": "allocatePublicAddress",
        "allow_upload_download": "allowUploadDownload",
        "availability_zones": "availabilityZones",
        "certificate": "certificate",
        "cloud_watch": "cloudWatch",
        "control_gateway_over_private_or_public_address": "controlGatewayOverPrivateOrPublicAddress",
        "create_private_subnets": "createPrivateSubnets",
        "create_tgw_subnets": "createTgwSubnets",
        "elb_clients": "elbClients",
        "elb_port": "elbPort",
        "elb_type": "elbType",
        "enable_instance_connect": "enableInstanceConnect",
        "enable_volume_encryption": "enableVolumeEncryption",
        "gateway_instance_type": "gatewayInstanceType",
        "gateway_management": "gatewayManagement",
        "gateway_password_hash": "gatewayPasswordHash",
        "gateways_addresses": "gatewaysAddresses",
        "gateways_blades": "gatewaysBlades",
        "gateway_sic_key": "gatewaySicKey",
        "gateways_max_size": "gatewaysMaxSize",
        "gateways_min_size": "gatewaysMinSize",
        "gateways_policy": "gatewaysPolicy",
        "gateways_target_groups": "gatewaysTargetGroups",
        "gateway_version": "gatewayVersion",
        "key_name": "keyName",
        "load_balancers_type": "loadBalancersType",
        "management_deploy": "managementDeploy",
        "management_hostname": "managementHostname",
        "management_instance_type": "managementInstanceType",
        "management_password_hash": "managementPasswordHash",
        "management_permissions": "managementPermissions",
        "management_predefined_role": "managementPredefinedRole",
        "management_sic_key": "managementSicKey",
        "management_stack_volume_size": "managementStackVolumeSize",
        "management_version": "managementVersion",
        "nlb_protocol": "nlbProtocol",
        "ntp_primary": "ntpPrimary",
        "ntp_secondary": "ntpSecondary",
        "number_of_a_zs": "numberOfAZs",
        "permissions": "permissions",
        "primary_management": "primaryManagement",
        "private_subnet1_cidr": "privateSubnet1Cidr",
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "private_subnet3_cidr": "privateSubnet3Cidr",
        "private_subnet4_cidr": "privateSubnet4Cidr",
        "provision_tag": "provisionTag",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet3_cidr": "publicSubnet3Cidr",
        "public_subnet4_cidr": "publicSubnet4Cidr",
        "security_gateway_volume_size": "securityGatewayVolumeSize",
        "server_ami": "serverAmi",
        "server_instance_type": "serverInstanceType",
        "server_name": "serverName",
        "servers_deploy": "serversDeploy",
        "servers_max_size": "serversMaxSize",
        "servers_min_size": "serversMinSize",
        "servers_target_groups": "serversTargetGroups",
        "service_port": "servicePort",
        "shell_management_stack": "shellManagementStack",
        "shell_security_gateway_stack": "shellSecurityGatewayStack",
        "source_security_group": "sourceSecurityGroup",
        "sts_roles": "stsRoles",
        "tgw_subnet1_cidr": "tgwSubnet1Cidr",
        "tgw_subnet2_cidr": "tgwSubnet2Cidr",
        "tgw_subnet3_cidr": "tgwSubnet3Cidr",
        "tgw_subnet4_cidr": "tgwSubnet4Cidr",
        "trusted_account": "trustedAccount",
        "vpccidr": "vpccidr",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        admin_cidr: typing.Optional["CfnModulePropsParametersAdminCidr"] = None,
        admin_email: typing.Optional["CfnModulePropsParametersAdminEmail"] = None,
        alb_protocol: typing.Optional["CfnModulePropsParametersAlbProtocol"] = None,
        allocate_public_address: typing.Optional["CfnModulePropsParametersAllocatePublicAddress"] = None,
        allow_upload_download: typing.Optional["CfnModulePropsParametersAllowUploadDownload"] = None,
        availability_zones: typing.Optional["CfnModulePropsParametersAvailabilityZones"] = None,
        certificate: typing.Optional["CfnModulePropsParametersCertificate"] = None,
        cloud_watch: typing.Optional["CfnModulePropsParametersCloudWatch"] = None,
        control_gateway_over_private_or_public_address: typing.Optional["CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress"] = None,
        create_private_subnets: typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"] = None,
        create_tgw_subnets: typing.Optional["CfnModulePropsParametersCreateTgwSubnets"] = None,
        elb_clients: typing.Optional["CfnModulePropsParametersElbClients"] = None,
        elb_port: typing.Optional["CfnModulePropsParametersElbPort"] = None,
        elb_type: typing.Optional["CfnModulePropsParametersElbType"] = None,
        enable_instance_connect: typing.Optional["CfnModulePropsParametersEnableInstanceConnect"] = None,
        enable_volume_encryption: typing.Optional["CfnModulePropsParametersEnableVolumeEncryption"] = None,
        gateway_instance_type: typing.Optional["CfnModulePropsParametersGatewayInstanceType"] = None,
        gateway_management: typing.Optional["CfnModulePropsParametersGatewayManagement"] = None,
        gateway_password_hash: typing.Optional["CfnModulePropsParametersGatewayPasswordHash"] = None,
        gateways_addresses: typing.Optional["CfnModulePropsParametersGatewaysAddresses"] = None,
        gateways_blades: typing.Optional["CfnModulePropsParametersGatewaysBlades"] = None,
        gateway_sic_key: typing.Optional["CfnModulePropsParametersGatewaySicKey"] = None,
        gateways_max_size: typing.Optional["CfnModulePropsParametersGatewaysMaxSize"] = None,
        gateways_min_size: typing.Optional["CfnModulePropsParametersGatewaysMinSize"] = None,
        gateways_policy: typing.Optional["CfnModulePropsParametersGatewaysPolicy"] = None,
        gateways_target_groups: typing.Optional["CfnModulePropsParametersGatewaysTargetGroups"] = None,
        gateway_version: typing.Optional["CfnModulePropsParametersGatewayVersion"] = None,
        key_name: typing.Optional["CfnModulePropsParametersKeyName"] = None,
        load_balancers_type: typing.Optional["CfnModulePropsParametersLoadBalancersType"] = None,
        management_deploy: typing.Optional["CfnModulePropsParametersManagementDeploy"] = None,
        management_hostname: typing.Optional["CfnModulePropsParametersManagementHostname"] = None,
        management_instance_type: typing.Optional["CfnModulePropsParametersManagementInstanceType"] = None,
        management_password_hash: typing.Optional["CfnModulePropsParametersManagementPasswordHash"] = None,
        management_permissions: typing.Optional["CfnModulePropsParametersManagementPermissions"] = None,
        management_predefined_role: typing.Optional["CfnModulePropsParametersManagementPredefinedRole"] = None,
        management_sic_key: typing.Optional["CfnModulePropsParametersManagementSicKey"] = None,
        management_stack_volume_size: typing.Optional["CfnModulePropsParametersManagementStackVolumeSize"] = None,
        management_version: typing.Optional["CfnModulePropsParametersManagementVersion"] = None,
        nlb_protocol: typing.Optional["CfnModulePropsParametersNlbProtocol"] = None,
        ntp_primary: typing.Optional["CfnModulePropsParametersNtpPrimary"] = None,
        ntp_secondary: typing.Optional["CfnModulePropsParametersNtpSecondary"] = None,
        number_of_a_zs: typing.Optional["CfnModulePropsParametersNumberOfAZs"] = None,
        permissions: typing.Optional["CfnModulePropsParametersPermissions"] = None,
        primary_management: typing.Optional["CfnModulePropsParametersPrimaryManagement"] = None,
        private_subnet1_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"] = None,
        private_subnet2_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"] = None,
        private_subnet3_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"] = None,
        private_subnet4_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet4Cidr"] = None,
        provision_tag: typing.Optional["CfnModulePropsParametersProvisionTag"] = None,
        public_subnet1_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet3_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"] = None,
        public_subnet4_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"] = None,
        security_gateway_volume_size: typing.Optional["CfnModulePropsParametersSecurityGatewayVolumeSize"] = None,
        server_ami: typing.Optional["CfnModulePropsParametersServerAmi"] = None,
        server_instance_type: typing.Optional["CfnModulePropsParametersServerInstanceType"] = None,
        server_name: typing.Optional["CfnModulePropsParametersServerName"] = None,
        servers_deploy: typing.Optional["CfnModulePropsParametersServersDeploy"] = None,
        servers_max_size: typing.Optional["CfnModulePropsParametersServersMaxSize"] = None,
        servers_min_size: typing.Optional["CfnModulePropsParametersServersMinSize"] = None,
        servers_target_groups: typing.Optional["CfnModulePropsParametersServersTargetGroups"] = None,
        service_port: typing.Optional["CfnModulePropsParametersServicePort"] = None,
        shell_management_stack: typing.Optional["CfnModulePropsParametersShellManagementStack"] = None,
        shell_security_gateway_stack: typing.Optional["CfnModulePropsParametersShellSecurityGatewayStack"] = None,
        source_security_group: typing.Optional["CfnModulePropsParametersSourceSecurityGroup"] = None,
        sts_roles: typing.Optional["CfnModulePropsParametersStsRoles"] = None,
        tgw_subnet1_cidr: typing.Optional["CfnModulePropsParametersTgwSubnet1Cidr"] = None,
        tgw_subnet2_cidr: typing.Optional["CfnModulePropsParametersTgwSubnet2Cidr"] = None,
        tgw_subnet3_cidr: typing.Optional["CfnModulePropsParametersTgwSubnet3Cidr"] = None,
        tgw_subnet4_cidr: typing.Optional["CfnModulePropsParametersTgwSubnet4Cidr"] = None,
        trusted_account: typing.Optional["CfnModulePropsParametersTrustedAccount"] = None,
        vpccidr: typing.Optional["CfnModulePropsParametersVpccidr"] = None,
    ) -> None:
        '''
        :param admin_cidr: Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.
        :param admin_email: Notifications about scaling events will be sent to this email address (optional).
        :param alb_protocol: The protocol to use on the Application Load Balancer. If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS
        :param allocate_public_address: Allocate an elastic IP for the Management. Default: true
        :param allow_upload_download: Automatically download Blade Contracts and other important data. Improve product experience by sending data to Check Point. Default: true
        :param availability_zones: List of Availability Zones (AZs) to use for the subnets in the VPC. Select at least two
        :param certificate: Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).
        :param cloud_watch: Report Check Point specific CloudWatch metrics. Default: false
        :param control_gateway_over_private_or_public_address: Determines if the gateways are provisioned using their private or public address. Default: private. Allowed values: private, public
        :param create_private_subnets: Set to false to create only public subnets. If false, the CIDR parameters for ALL private subnets will be ignored. Default: true
        :param create_tgw_subnets: Set true for creating designated subnets for VPC TGW attachments. If false, the CIDR parameters for the TGW subnets will be ignored. Default: false
        :param elb_clients: Allow clients only from this network to communicate with the Web Servers. Default: 0.0.0.0/0
        :param elb_port: Port for the ELB. Default: 8080
        :param elb_type: The Elasitc Load Balancer Type. Default: none. Allowed values: none, internal, internet-facing
        :param enable_instance_connect: Enable SSH connection over AWS web console. Default: false
        :param enable_volume_encryption: Encrypt Environment instances volume with default AWS KMS key. Default: true
        :param gateway_instance_type: The EC2 instance type for the Security Gateways. Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge
        :param gateway_management: Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address. Default: 'Locally managed'. Allowed values: Locally managed, Over the internet
        :param gateway_password_hash: Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).
        :param gateways_addresses: Allow gateways only from this network to communicate with the Security Management Server.
        :param gateways_blades: Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later). Default: true
        :param gateway_sic_key: The Secure Internal Communication key creates trusted connections between Check Point components. Choose a random string consisting of at least 8 alphanumeric characters.
        :param gateways_max_size: The maximal number of Security Gateways.
        :param gateways_min_size: The minimal number of Security Gateways.
        :param gateways_policy: The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group. Default: Standard
        :param gateways_target_groups: A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).
        :param gateway_version: The version and license to install on the Security Gateways. Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW
        :param key_name: The EC2 Key Pair to allow SSH access to the instances. For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
        :param load_balancers_type: Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading. Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer
        :param management_deploy: Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section. Default: true
        :param management_hostname: (optional). Default: mgmt-aws
        :param management_instance_type: The EC2 instance type of the Security Management Server. Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge
        :param management_password_hash: Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).
        :param management_permissions: IAM role to attach to the instance profile of the Management Server. Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions
        :param management_predefined_role: A predefined IAM role to attach to the instance profile. Ignored if IAM role is not set to 'Use existing'
        :param management_sic_key: Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components. Choose a random string consisting of at least 8 alphanumeric characters
        :param management_stack_volume_size: EBS Volume size of the management server.
        :param management_version: The version and license to install on the Security Management Server. Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT
        :param nlb_protocol: The protocol to use on the Network Load Balancer. If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP
        :param ntp_primary: (optional). Default: 169.254.169.123
        :param ntp_secondary: (optional). Default: 0.pool.ntp.org
        :param number_of_a_zs: Number of Availability Zones to use in the VPC. This must match your selections in the list of Availability Zones parameter. Default: 2
        :param permissions: IAM Permissions for the management server. Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)
        :param primary_management: Determines if this is the primary Management Server or not. Default: true
        :param private_subnet1_cidr: CIDR block for private subnet 1 located in the 1st Availability Zone. Default: 10.0.11.0/24
        :param private_subnet2_cidr: CIDR block for private subnet 2 located in the 2nd Availability Zone. Default: 10.0.21.0/24
        :param private_subnet3_cidr: CIDR block for private subnet 3 located in the 3rd Availability Zone. Default: 10.0.31.0/24
        :param private_subnet4_cidr: CIDR block for private subnet 4 located in the 4th Availability Zone. Default: 10.0.41.0/24
        :param provision_tag: The tag is used by the Security Management Server to automatically provision the Security Gateways. Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart
        :param public_subnet1_cidr: CIDR block for public subnet 1 located in the 1st Availability Zone. If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24
        :param public_subnet2_cidr: CIDR block for public subnet 2 located in the 2nd Availability Zone. Default: 10.0.20.0/24
        :param public_subnet3_cidr: CIDR block for public subnet 3 located in the 3rd Availability Zone. Default: 10.0.30.0/24
        :param public_subnet4_cidr: CIDR block for public subnet 4 located in the 4th Availability Zone. Default: 10.0.40.0/24
        :param security_gateway_volume_size: EBS Volume size of the security gateway server.
        :param server_ami: The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).
        :param server_instance_type: The EC2 instance type for the web servers. Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge
        :param server_name: The servers name tag. Default: Server
        :param servers_deploy: Select true to deploy web servers and an internal Application Load Balancer. If you select false the other parameters of this section will be ignored. Default: false
        :param servers_max_size: The maximal number of servers in the Auto Scaling group. Default: 10
        :param servers_min_size: The minimal number of servers in the Auto Scaling group. Default: 2
        :param servers_target_groups: An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).
        :param service_port: The external Load Balancer listens to this port. Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS
        :param shell_management_stack: Change the admin shell to enable advanced command line configuration. Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh
        :param shell_security_gateway_stack: Change the admin shell to enable advanced command line configuration. Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh
        :param source_security_group: The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.
        :param sts_roles: The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).
        :param tgw_subnet1_cidr: CIDR block for TGW subnet 1 located in Availability Zone 1. Default: 10.0.12.0/24
        :param tgw_subnet2_cidr: CIDR block for TGW subnet 2 located in Availability Zone 2. Default: 10.0.22.0/24
        :param tgw_subnet3_cidr: CIDR block for TGW subnet 3 located in Availability Zone 3. Default: 10.0.32.0/24
        :param tgw_subnet4_cidr: CIDR block for TGW subnet 4 located in Availability Zone 4. Default: 10.0.42.0/24
        :param trusted_account: A 12 digits number that represents the ID of a trusted account. IAM users in this account will be able assume the IAM role and receive the permissions attached to it.
        :param vpccidr: CIDR block for the VPC. Default: 10.0.0.0/16

        :schema: CfnModulePropsParameters
        '''
        if isinstance(admin_cidr, dict):
            admin_cidr = CfnModulePropsParametersAdminCidr(**admin_cidr)
        if isinstance(admin_email, dict):
            admin_email = CfnModulePropsParametersAdminEmail(**admin_email)
        if isinstance(alb_protocol, dict):
            alb_protocol = CfnModulePropsParametersAlbProtocol(**alb_protocol)
        if isinstance(allocate_public_address, dict):
            allocate_public_address = CfnModulePropsParametersAllocatePublicAddress(**allocate_public_address)
        if isinstance(allow_upload_download, dict):
            allow_upload_download = CfnModulePropsParametersAllowUploadDownload(**allow_upload_download)
        if isinstance(availability_zones, dict):
            availability_zones = CfnModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(certificate, dict):
            certificate = CfnModulePropsParametersCertificate(**certificate)
        if isinstance(cloud_watch, dict):
            cloud_watch = CfnModulePropsParametersCloudWatch(**cloud_watch)
        if isinstance(control_gateway_over_private_or_public_address, dict):
            control_gateway_over_private_or_public_address = CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress(**control_gateway_over_private_or_public_address)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_tgw_subnets, dict):
            create_tgw_subnets = CfnModulePropsParametersCreateTgwSubnets(**create_tgw_subnets)
        if isinstance(elb_clients, dict):
            elb_clients = CfnModulePropsParametersElbClients(**elb_clients)
        if isinstance(elb_port, dict):
            elb_port = CfnModulePropsParametersElbPort(**elb_port)
        if isinstance(elb_type, dict):
            elb_type = CfnModulePropsParametersElbType(**elb_type)
        if isinstance(enable_instance_connect, dict):
            enable_instance_connect = CfnModulePropsParametersEnableInstanceConnect(**enable_instance_connect)
        if isinstance(enable_volume_encryption, dict):
            enable_volume_encryption = CfnModulePropsParametersEnableVolumeEncryption(**enable_volume_encryption)
        if isinstance(gateway_instance_type, dict):
            gateway_instance_type = CfnModulePropsParametersGatewayInstanceType(**gateway_instance_type)
        if isinstance(gateway_management, dict):
            gateway_management = CfnModulePropsParametersGatewayManagement(**gateway_management)
        if isinstance(gateway_password_hash, dict):
            gateway_password_hash = CfnModulePropsParametersGatewayPasswordHash(**gateway_password_hash)
        if isinstance(gateways_addresses, dict):
            gateways_addresses = CfnModulePropsParametersGatewaysAddresses(**gateways_addresses)
        if isinstance(gateways_blades, dict):
            gateways_blades = CfnModulePropsParametersGatewaysBlades(**gateways_blades)
        if isinstance(gateway_sic_key, dict):
            gateway_sic_key = CfnModulePropsParametersGatewaySicKey(**gateway_sic_key)
        if isinstance(gateways_max_size, dict):
            gateways_max_size = CfnModulePropsParametersGatewaysMaxSize(**gateways_max_size)
        if isinstance(gateways_min_size, dict):
            gateways_min_size = CfnModulePropsParametersGatewaysMinSize(**gateways_min_size)
        if isinstance(gateways_policy, dict):
            gateways_policy = CfnModulePropsParametersGatewaysPolicy(**gateways_policy)
        if isinstance(gateways_target_groups, dict):
            gateways_target_groups = CfnModulePropsParametersGatewaysTargetGroups(**gateways_target_groups)
        if isinstance(gateway_version, dict):
            gateway_version = CfnModulePropsParametersGatewayVersion(**gateway_version)
        if isinstance(key_name, dict):
            key_name = CfnModulePropsParametersKeyName(**key_name)
        if isinstance(load_balancers_type, dict):
            load_balancers_type = CfnModulePropsParametersLoadBalancersType(**load_balancers_type)
        if isinstance(management_deploy, dict):
            management_deploy = CfnModulePropsParametersManagementDeploy(**management_deploy)
        if isinstance(management_hostname, dict):
            management_hostname = CfnModulePropsParametersManagementHostname(**management_hostname)
        if isinstance(management_instance_type, dict):
            management_instance_type = CfnModulePropsParametersManagementInstanceType(**management_instance_type)
        if isinstance(management_password_hash, dict):
            management_password_hash = CfnModulePropsParametersManagementPasswordHash(**management_password_hash)
        if isinstance(management_permissions, dict):
            management_permissions = CfnModulePropsParametersManagementPermissions(**management_permissions)
        if isinstance(management_predefined_role, dict):
            management_predefined_role = CfnModulePropsParametersManagementPredefinedRole(**management_predefined_role)
        if isinstance(management_sic_key, dict):
            management_sic_key = CfnModulePropsParametersManagementSicKey(**management_sic_key)
        if isinstance(management_stack_volume_size, dict):
            management_stack_volume_size = CfnModulePropsParametersManagementStackVolumeSize(**management_stack_volume_size)
        if isinstance(management_version, dict):
            management_version = CfnModulePropsParametersManagementVersion(**management_version)
        if isinstance(nlb_protocol, dict):
            nlb_protocol = CfnModulePropsParametersNlbProtocol(**nlb_protocol)
        if isinstance(ntp_primary, dict):
            ntp_primary = CfnModulePropsParametersNtpPrimary(**ntp_primary)
        if isinstance(ntp_secondary, dict):
            ntp_secondary = CfnModulePropsParametersNtpSecondary(**ntp_secondary)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(permissions, dict):
            permissions = CfnModulePropsParametersPermissions(**permissions)
        if isinstance(primary_management, dict):
            primary_management = CfnModulePropsParametersPrimaryManagement(**primary_management)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(private_subnet3_cidr, dict):
            private_subnet3_cidr = CfnModulePropsParametersPrivateSubnet3Cidr(**private_subnet3_cidr)
        if isinstance(private_subnet4_cidr, dict):
            private_subnet4_cidr = CfnModulePropsParametersPrivateSubnet4Cidr(**private_subnet4_cidr)
        if isinstance(provision_tag, dict):
            provision_tag = CfnModulePropsParametersProvisionTag(**provision_tag)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(public_subnet4_cidr, dict):
            public_subnet4_cidr = CfnModulePropsParametersPublicSubnet4Cidr(**public_subnet4_cidr)
        if isinstance(security_gateway_volume_size, dict):
            security_gateway_volume_size = CfnModulePropsParametersSecurityGatewayVolumeSize(**security_gateway_volume_size)
        if isinstance(server_ami, dict):
            server_ami = CfnModulePropsParametersServerAmi(**server_ami)
        if isinstance(server_instance_type, dict):
            server_instance_type = CfnModulePropsParametersServerInstanceType(**server_instance_type)
        if isinstance(server_name, dict):
            server_name = CfnModulePropsParametersServerName(**server_name)
        if isinstance(servers_deploy, dict):
            servers_deploy = CfnModulePropsParametersServersDeploy(**servers_deploy)
        if isinstance(servers_max_size, dict):
            servers_max_size = CfnModulePropsParametersServersMaxSize(**servers_max_size)
        if isinstance(servers_min_size, dict):
            servers_min_size = CfnModulePropsParametersServersMinSize(**servers_min_size)
        if isinstance(servers_target_groups, dict):
            servers_target_groups = CfnModulePropsParametersServersTargetGroups(**servers_target_groups)
        if isinstance(service_port, dict):
            service_port = CfnModulePropsParametersServicePort(**service_port)
        if isinstance(shell_management_stack, dict):
            shell_management_stack = CfnModulePropsParametersShellManagementStack(**shell_management_stack)
        if isinstance(shell_security_gateway_stack, dict):
            shell_security_gateway_stack = CfnModulePropsParametersShellSecurityGatewayStack(**shell_security_gateway_stack)
        if isinstance(source_security_group, dict):
            source_security_group = CfnModulePropsParametersSourceSecurityGroup(**source_security_group)
        if isinstance(sts_roles, dict):
            sts_roles = CfnModulePropsParametersStsRoles(**sts_roles)
        if isinstance(tgw_subnet1_cidr, dict):
            tgw_subnet1_cidr = CfnModulePropsParametersTgwSubnet1Cidr(**tgw_subnet1_cidr)
        if isinstance(tgw_subnet2_cidr, dict):
            tgw_subnet2_cidr = CfnModulePropsParametersTgwSubnet2Cidr(**tgw_subnet2_cidr)
        if isinstance(tgw_subnet3_cidr, dict):
            tgw_subnet3_cidr = CfnModulePropsParametersTgwSubnet3Cidr(**tgw_subnet3_cidr)
        if isinstance(tgw_subnet4_cidr, dict):
            tgw_subnet4_cidr = CfnModulePropsParametersTgwSubnet4Cidr(**tgw_subnet4_cidr)
        if isinstance(trusted_account, dict):
            trusted_account = CfnModulePropsParametersTrustedAccount(**trusted_account)
        if isinstance(vpccidr, dict):
            vpccidr = CfnModulePropsParametersVpccidr(**vpccidr)
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_cidr is not None:
            self._values["admin_cidr"] = admin_cidr
        if admin_email is not None:
            self._values["admin_email"] = admin_email
        if alb_protocol is not None:
            self._values["alb_protocol"] = alb_protocol
        if allocate_public_address is not None:
            self._values["allocate_public_address"] = allocate_public_address
        if allow_upload_download is not None:
            self._values["allow_upload_download"] = allow_upload_download
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if certificate is not None:
            self._values["certificate"] = certificate
        if cloud_watch is not None:
            self._values["cloud_watch"] = cloud_watch
        if control_gateway_over_private_or_public_address is not None:
            self._values["control_gateway_over_private_or_public_address"] = control_gateway_over_private_or_public_address
        if create_private_subnets is not None:
            self._values["create_private_subnets"] = create_private_subnets
        if create_tgw_subnets is not None:
            self._values["create_tgw_subnets"] = create_tgw_subnets
        if elb_clients is not None:
            self._values["elb_clients"] = elb_clients
        if elb_port is not None:
            self._values["elb_port"] = elb_port
        if elb_type is not None:
            self._values["elb_type"] = elb_type
        if enable_instance_connect is not None:
            self._values["enable_instance_connect"] = enable_instance_connect
        if enable_volume_encryption is not None:
            self._values["enable_volume_encryption"] = enable_volume_encryption
        if gateway_instance_type is not None:
            self._values["gateway_instance_type"] = gateway_instance_type
        if gateway_management is not None:
            self._values["gateway_management"] = gateway_management
        if gateway_password_hash is not None:
            self._values["gateway_password_hash"] = gateway_password_hash
        if gateways_addresses is not None:
            self._values["gateways_addresses"] = gateways_addresses
        if gateways_blades is not None:
            self._values["gateways_blades"] = gateways_blades
        if gateway_sic_key is not None:
            self._values["gateway_sic_key"] = gateway_sic_key
        if gateways_max_size is not None:
            self._values["gateways_max_size"] = gateways_max_size
        if gateways_min_size is not None:
            self._values["gateways_min_size"] = gateways_min_size
        if gateways_policy is not None:
            self._values["gateways_policy"] = gateways_policy
        if gateways_target_groups is not None:
            self._values["gateways_target_groups"] = gateways_target_groups
        if gateway_version is not None:
            self._values["gateway_version"] = gateway_version
        if key_name is not None:
            self._values["key_name"] = key_name
        if load_balancers_type is not None:
            self._values["load_balancers_type"] = load_balancers_type
        if management_deploy is not None:
            self._values["management_deploy"] = management_deploy
        if management_hostname is not None:
            self._values["management_hostname"] = management_hostname
        if management_instance_type is not None:
            self._values["management_instance_type"] = management_instance_type
        if management_password_hash is not None:
            self._values["management_password_hash"] = management_password_hash
        if management_permissions is not None:
            self._values["management_permissions"] = management_permissions
        if management_predefined_role is not None:
            self._values["management_predefined_role"] = management_predefined_role
        if management_sic_key is not None:
            self._values["management_sic_key"] = management_sic_key
        if management_stack_volume_size is not None:
            self._values["management_stack_volume_size"] = management_stack_volume_size
        if management_version is not None:
            self._values["management_version"] = management_version
        if nlb_protocol is not None:
            self._values["nlb_protocol"] = nlb_protocol
        if ntp_primary is not None:
            self._values["ntp_primary"] = ntp_primary
        if ntp_secondary is not None:
            self._values["ntp_secondary"] = ntp_secondary
        if number_of_a_zs is not None:
            self._values["number_of_a_zs"] = number_of_a_zs
        if permissions is not None:
            self._values["permissions"] = permissions
        if primary_management is not None:
            self._values["primary_management"] = primary_management
        if private_subnet1_cidr is not None:
            self._values["private_subnet1_cidr"] = private_subnet1_cidr
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if private_subnet3_cidr is not None:
            self._values["private_subnet3_cidr"] = private_subnet3_cidr
        if private_subnet4_cidr is not None:
            self._values["private_subnet4_cidr"] = private_subnet4_cidr
        if provision_tag is not None:
            self._values["provision_tag"] = provision_tag
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet3_cidr is not None:
            self._values["public_subnet3_cidr"] = public_subnet3_cidr
        if public_subnet4_cidr is not None:
            self._values["public_subnet4_cidr"] = public_subnet4_cidr
        if security_gateway_volume_size is not None:
            self._values["security_gateway_volume_size"] = security_gateway_volume_size
        if server_ami is not None:
            self._values["server_ami"] = server_ami
        if server_instance_type is not None:
            self._values["server_instance_type"] = server_instance_type
        if server_name is not None:
            self._values["server_name"] = server_name
        if servers_deploy is not None:
            self._values["servers_deploy"] = servers_deploy
        if servers_max_size is not None:
            self._values["servers_max_size"] = servers_max_size
        if servers_min_size is not None:
            self._values["servers_min_size"] = servers_min_size
        if servers_target_groups is not None:
            self._values["servers_target_groups"] = servers_target_groups
        if service_port is not None:
            self._values["service_port"] = service_port
        if shell_management_stack is not None:
            self._values["shell_management_stack"] = shell_management_stack
        if shell_security_gateway_stack is not None:
            self._values["shell_security_gateway_stack"] = shell_security_gateway_stack
        if source_security_group is not None:
            self._values["source_security_group"] = source_security_group
        if sts_roles is not None:
            self._values["sts_roles"] = sts_roles
        if tgw_subnet1_cidr is not None:
            self._values["tgw_subnet1_cidr"] = tgw_subnet1_cidr
        if tgw_subnet2_cidr is not None:
            self._values["tgw_subnet2_cidr"] = tgw_subnet2_cidr
        if tgw_subnet3_cidr is not None:
            self._values["tgw_subnet3_cidr"] = tgw_subnet3_cidr
        if tgw_subnet4_cidr is not None:
            self._values["tgw_subnet4_cidr"] = tgw_subnet4_cidr
        if trusted_account is not None:
            self._values["trusted_account"] = trusted_account
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr

    @builtins.property
    def admin_cidr(self) -> typing.Optional["CfnModulePropsParametersAdminCidr"]:
        '''Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.

        :schema: CfnModulePropsParameters#AdminCIDR
        '''
        result = self._values.get("admin_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersAdminCidr"], result)

    @builtins.property
    def admin_email(self) -> typing.Optional["CfnModulePropsParametersAdminEmail"]:
        '''Notifications about scaling events will be sent to this email address (optional).

        :schema: CfnModulePropsParameters#AdminEmail
        '''
        result = self._values.get("admin_email")
        return typing.cast(typing.Optional["CfnModulePropsParametersAdminEmail"], result)

    @builtins.property
    def alb_protocol(self) -> typing.Optional["CfnModulePropsParametersAlbProtocol"]:
        '''The protocol to use on the Application Load Balancer.

        If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS

        :schema: CfnModulePropsParameters#ALBProtocol
        '''
        result = self._values.get("alb_protocol")
        return typing.cast(typing.Optional["CfnModulePropsParametersAlbProtocol"], result)

    @builtins.property
    def allocate_public_address(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAllocatePublicAddress"]:
        '''Allocate an elastic IP for the Management.

        Default: true

        :schema: CfnModulePropsParameters#AllocatePublicAddress
        '''
        result = self._values.get("allocate_public_address")
        return typing.cast(typing.Optional["CfnModulePropsParametersAllocatePublicAddress"], result)

    @builtins.property
    def allow_upload_download(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAllowUploadDownload"]:
        '''Automatically download Blade Contracts and other important data.

        Improve product experience by sending data to Check Point. Default: true

        :schema: CfnModulePropsParameters#AllowUploadDownload
        '''
        result = self._values.get("allow_upload_download")
        return typing.cast(typing.Optional["CfnModulePropsParametersAllowUploadDownload"], result)

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZones"]:
        '''List of Availability Zones (AZs) to use for the subnets in the VPC.

        Select at least two

        :schema: CfnModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def certificate(self) -> typing.Optional["CfnModulePropsParametersCertificate"]:
        '''Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).

        :schema: CfnModulePropsParameters#Certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["CfnModulePropsParametersCertificate"], result)

    @builtins.property
    def cloud_watch(self) -> typing.Optional["CfnModulePropsParametersCloudWatch"]:
        '''Report Check Point specific CloudWatch metrics.

        Default: false

        :schema: CfnModulePropsParameters#CloudWatch
        '''
        result = self._values.get("cloud_watch")
        return typing.cast(typing.Optional["CfnModulePropsParametersCloudWatch"], result)

    @builtins.property
    def control_gateway_over_private_or_public_address(
        self,
    ) -> typing.Optional["CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress"]:
        '''Determines if the gateways are provisioned using their private or public address.

        Default: private. Allowed values: private, public

        :schema: CfnModulePropsParameters#ControlGatewayOverPrivateOrPublicAddress
        '''
        result = self._values.get("control_gateway_over_private_or_public_address")
        return typing.cast(typing.Optional["CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress"], result)

    @builtins.property
    def create_private_subnets(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"]:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored. Default: true

        :schema: CfnModulePropsParameters#CreatePrivateSubnets
        '''
        result = self._values.get("create_private_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreatePrivateSubnets"], result)

    @builtins.property
    def create_tgw_subnets(
        self,
    ) -> typing.Optional["CfnModulePropsParametersCreateTgwSubnets"]:
        '''Set true for creating designated subnets for VPC TGW attachments.

        If false, the CIDR parameters for the TGW subnets will be ignored. Default: false

        :schema: CfnModulePropsParameters#CreateTgwSubnets
        '''
        result = self._values.get("create_tgw_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersCreateTgwSubnets"], result)

    @builtins.property
    def elb_clients(self) -> typing.Optional["CfnModulePropsParametersElbClients"]:
        '''Allow clients only from this network to communicate with the Web Servers.

        Default: 0.0.0.0/0

        :schema: CfnModulePropsParameters#ELBClients
        '''
        result = self._values.get("elb_clients")
        return typing.cast(typing.Optional["CfnModulePropsParametersElbClients"], result)

    @builtins.property
    def elb_port(self) -> typing.Optional["CfnModulePropsParametersElbPort"]:
        '''Port for the ELB.

        Default: 8080

        :schema: CfnModulePropsParameters#ELBPort
        '''
        result = self._values.get("elb_port")
        return typing.cast(typing.Optional["CfnModulePropsParametersElbPort"], result)

    @builtins.property
    def elb_type(self) -> typing.Optional["CfnModulePropsParametersElbType"]:
        '''The Elasitc Load Balancer Type.

        Default: none. Allowed values: none, internal, internet-facing

        :schema: CfnModulePropsParameters#ELBType
        '''
        result = self._values.get("elb_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersElbType"], result)

    @builtins.property
    def enable_instance_connect(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnableInstanceConnect"]:
        '''Enable SSH connection over AWS web console.

        Default: false

        :schema: CfnModulePropsParameters#EnableInstanceConnect
        '''
        result = self._values.get("enable_instance_connect")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableInstanceConnect"], result)

    @builtins.property
    def enable_volume_encryption(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnableVolumeEncryption"]:
        '''Encrypt Environment instances volume with default AWS KMS key.

        Default: true

        :schema: CfnModulePropsParameters#EnableVolumeEncryption
        '''
        result = self._values.get("enable_volume_encryption")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableVolumeEncryption"], result)

    @builtins.property
    def gateway_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewayInstanceType"]:
        '''The EC2 instance type for the Security Gateways.

        Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge

        :schema: CfnModulePropsParameters#GatewayInstanceType
        '''
        result = self._values.get("gateway_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewayInstanceType"], result)

    @builtins.property
    def gateway_management(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewayManagement"]:
        '''Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address.

        Default: 'Locally managed'. Allowed values: Locally managed, Over the internet

        :schema: CfnModulePropsParameters#GatewayManagement
        '''
        result = self._values.get("gateway_management")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewayManagement"], result)

    @builtins.property
    def gateway_password_hash(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewayPasswordHash"]:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :schema: CfnModulePropsParameters#GatewayPasswordHash
        '''
        result = self._values.get("gateway_password_hash")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewayPasswordHash"], result)

    @builtins.property
    def gateways_addresses(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysAddresses"]:
        '''Allow gateways only from this network to communicate with the Security Management Server.

        :schema: CfnModulePropsParameters#GatewaysAddresses
        '''
        result = self._values.get("gateways_addresses")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysAddresses"], result)

    @builtins.property
    def gateways_blades(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysBlades"]:
        '''Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later).

        Default: true

        :schema: CfnModulePropsParameters#GatewaysBlades
        '''
        result = self._values.get("gateways_blades")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysBlades"], result)

    @builtins.property
    def gateway_sic_key(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaySicKey"]:
        '''The Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters.

        :schema: CfnModulePropsParameters#GatewaySICKey
        '''
        result = self._values.get("gateway_sic_key")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaySicKey"], result)

    @builtins.property
    def gateways_max_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysMaxSize"]:
        '''The maximal number of Security Gateways.

        :schema: CfnModulePropsParameters#GatewaysMaxSize
        '''
        result = self._values.get("gateways_max_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysMaxSize"], result)

    @builtins.property
    def gateways_min_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysMinSize"]:
        '''The minimal number of Security Gateways.

        :schema: CfnModulePropsParameters#GatewaysMinSize
        '''
        result = self._values.get("gateways_min_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysMinSize"], result)

    @builtins.property
    def gateways_policy(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysPolicy"]:
        '''The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group.

        Default: Standard

        :schema: CfnModulePropsParameters#GatewaysPolicy
        '''
        result = self._values.get("gateways_policy")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysPolicy"], result)

    @builtins.property
    def gateways_target_groups(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewaysTargetGroups"]:
        '''A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).

        :schema: CfnModulePropsParameters#GatewaysTargetGroups
        '''
        result = self._values.get("gateways_target_groups")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewaysTargetGroups"], result)

    @builtins.property
    def gateway_version(
        self,
    ) -> typing.Optional["CfnModulePropsParametersGatewayVersion"]:
        '''The version and license to install on the Security Gateways.

        Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW

        :schema: CfnModulePropsParameters#GatewayVersion
        '''
        result = self._values.get("gateway_version")
        return typing.cast(typing.Optional["CfnModulePropsParametersGatewayVersion"], result)

    @builtins.property
    def key_name(self) -> typing.Optional["CfnModulePropsParametersKeyName"]:
        '''The EC2 Key Pair to allow SSH access to the instances.

        For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

        :schema: CfnModulePropsParameters#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersKeyName"], result)

    @builtins.property
    def load_balancers_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersLoadBalancersType"]:
        '''Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading.

        Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer

        :schema: CfnModulePropsParameters#LoadBalancersType
        '''
        result = self._values.get("load_balancers_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersLoadBalancersType"], result)

    @builtins.property
    def management_deploy(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementDeploy"]:
        '''Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section.

        Default: true

        :schema: CfnModulePropsParameters#ManagementDeploy
        '''
        result = self._values.get("management_deploy")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementDeploy"], result)

    @builtins.property
    def management_hostname(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementHostname"]:
        '''(optional).

        Default: mgmt-aws

        :schema: CfnModulePropsParameters#ManagementHostname
        '''
        result = self._values.get("management_hostname")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementHostname"], result)

    @builtins.property
    def management_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementInstanceType"]:
        '''The EC2 instance type of the Security Management Server.

        Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge

        :schema: CfnModulePropsParameters#ManagementInstanceType
        '''
        result = self._values.get("management_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementInstanceType"], result)

    @builtins.property
    def management_password_hash(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementPasswordHash"]:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :schema: CfnModulePropsParameters#ManagementPasswordHash
        '''
        result = self._values.get("management_password_hash")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementPasswordHash"], result)

    @builtins.property
    def management_permissions(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementPermissions"]:
        '''IAM role to attach to the instance profile of the Management Server.

        Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions

        :schema: CfnModulePropsParameters#ManagementPermissions
        '''
        result = self._values.get("management_permissions")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementPermissions"], result)

    @builtins.property
    def management_predefined_role(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementPredefinedRole"]:
        '''A predefined IAM role to attach to the instance profile.

        Ignored if IAM role is not set to 'Use existing'

        :schema: CfnModulePropsParameters#ManagementPredefinedRole
        '''
        result = self._values.get("management_predefined_role")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementPredefinedRole"], result)

    @builtins.property
    def management_sic_key(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementSicKey"]:
        '''Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters

        :schema: CfnModulePropsParameters#ManagementSICKey
        '''
        result = self._values.get("management_sic_key")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementSicKey"], result)

    @builtins.property
    def management_stack_volume_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementStackVolumeSize"]:
        '''EBS Volume size of the management server.

        :schema: CfnModulePropsParameters#ManagementStackVolumeSize
        '''
        result = self._values.get("management_stack_volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementStackVolumeSize"], result)

    @builtins.property
    def management_version(
        self,
    ) -> typing.Optional["CfnModulePropsParametersManagementVersion"]:
        '''The version and license to install on the Security Management Server.

        Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT

        :schema: CfnModulePropsParameters#ManagementVersion
        '''
        result = self._values.get("management_version")
        return typing.cast(typing.Optional["CfnModulePropsParametersManagementVersion"], result)

    @builtins.property
    def nlb_protocol(self) -> typing.Optional["CfnModulePropsParametersNlbProtocol"]:
        '''The protocol to use on the Network Load Balancer.

        If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP

        :schema: CfnModulePropsParameters#NLBProtocol
        '''
        result = self._values.get("nlb_protocol")
        return typing.cast(typing.Optional["CfnModulePropsParametersNlbProtocol"], result)

    @builtins.property
    def ntp_primary(self) -> typing.Optional["CfnModulePropsParametersNtpPrimary"]:
        '''(optional).

        Default: 169.254.169.123

        :schema: CfnModulePropsParameters#NTPPrimary
        '''
        result = self._values.get("ntp_primary")
        return typing.cast(typing.Optional["CfnModulePropsParametersNtpPrimary"], result)

    @builtins.property
    def ntp_secondary(self) -> typing.Optional["CfnModulePropsParametersNtpSecondary"]:
        '''(optional).

        Default: 0.pool.ntp.org

        :schema: CfnModulePropsParameters#NTPSecondary
        '''
        result = self._values.get("ntp_secondary")
        return typing.cast(typing.Optional["CfnModulePropsParametersNtpSecondary"], result)

    @builtins.property
    def number_of_a_zs(self) -> typing.Optional["CfnModulePropsParametersNumberOfAZs"]:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.  Default: 2

        :schema: CfnModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumberOfAZs"], result)

    @builtins.property
    def permissions(self) -> typing.Optional["CfnModulePropsParametersPermissions"]:
        '''IAM Permissions for the management server.

        Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)

        :schema: CfnModulePropsParameters#Permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional["CfnModulePropsParametersPermissions"], result)

    @builtins.property
    def primary_management(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrimaryManagement"]:
        '''Determines if this is the primary Management Server or not.

        Default: true

        :schema: CfnModulePropsParameters#PrimaryManagement
        '''
        result = self._values.get("primary_management")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrimaryManagement"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"]:
        '''CIDR block for private subnet 1 located in the 1st Availability Zone.

        Default: 10.0.11.0/24

        :schema: CfnModulePropsParameters#PrivateSubnet1CIDR
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"]:
        '''CIDR block for private subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.21.0/24

        :schema: CfnModulePropsParameters#PrivateSubnet2CIDR
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def private_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"]:
        '''CIDR block for private subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.31.0/24

        :schema: CfnModulePropsParameters#PrivateSubnet3CIDR
        '''
        result = self._values.get("private_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"], result)

    @builtins.property
    def private_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet4Cidr"]:
        '''CIDR block for private subnet 4 located in the 4th Availability Zone.

        Default: 10.0.41.0/24

        :schema: CfnModulePropsParameters#PrivateSubnet4CIDR
        '''
        result = self._values.get("private_subnet4_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet4Cidr"], result)

    @builtins.property
    def provision_tag(self) -> typing.Optional["CfnModulePropsParametersProvisionTag"]:
        '''The tag is used by the Security Management Server to automatically provision the Security Gateways.

        Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart

        :schema: CfnModulePropsParameters#ProvisionTag
        '''
        result = self._values.get("provision_tag")
        return typing.cast(typing.Optional["CfnModulePropsParametersProvisionTag"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for public subnet 1 located in the 1st Availability Zone.

        If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24

        :schema: CfnModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for public subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.20.0/24

        :schema: CfnModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"]:
        '''CIDR block for public subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.30.0/24

        :schema: CfnModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def public_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"]:
        '''CIDR block for public subnet 4 located in the 4th Availability Zone.

        Default: 10.0.40.0/24

        :schema: CfnModulePropsParameters#PublicSubnet4CIDR
        '''
        result = self._values.get("public_subnet4_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet4Cidr"], result)

    @builtins.property
    def security_gateway_volume_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSecurityGatewayVolumeSize"]:
        '''EBS Volume size of the security gateway server.

        :schema: CfnModulePropsParameters#SecurityGatewayVolumeSize
        '''
        result = self._values.get("security_gateway_volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersSecurityGatewayVolumeSize"], result)

    @builtins.property
    def server_ami(self) -> typing.Optional["CfnModulePropsParametersServerAmi"]:
        '''The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).

        :schema: CfnModulePropsParameters#ServerAMI
        '''
        result = self._values.get("server_ami")
        return typing.cast(typing.Optional["CfnModulePropsParametersServerAmi"], result)

    @builtins.property
    def server_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersServerInstanceType"]:
        '''The EC2 instance type for the web servers.

        Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge

        :schema: CfnModulePropsParameters#ServerInstanceType
        '''
        result = self._values.get("server_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersServerInstanceType"], result)

    @builtins.property
    def server_name(self) -> typing.Optional["CfnModulePropsParametersServerName"]:
        '''The servers name tag.

        Default: Server

        :schema: CfnModulePropsParameters#ServerName
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersServerName"], result)

    @builtins.property
    def servers_deploy(
        self,
    ) -> typing.Optional["CfnModulePropsParametersServersDeploy"]:
        '''Select true to deploy web servers and an internal Application Load Balancer.

        If you select false the other parameters of this section will be ignored. Default: false

        :schema: CfnModulePropsParameters#ServersDeploy
        '''
        result = self._values.get("servers_deploy")
        return typing.cast(typing.Optional["CfnModulePropsParametersServersDeploy"], result)

    @builtins.property
    def servers_max_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersServersMaxSize"]:
        '''The maximal number of servers in the Auto Scaling group.

        Default: 10

        :schema: CfnModulePropsParameters#ServersMaxSize
        '''
        result = self._values.get("servers_max_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersServersMaxSize"], result)

    @builtins.property
    def servers_min_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersServersMinSize"]:
        '''The minimal number of servers in the Auto Scaling group.

        Default: 2

        :schema: CfnModulePropsParameters#ServersMinSize
        '''
        result = self._values.get("servers_min_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersServersMinSize"], result)

    @builtins.property
    def servers_target_groups(
        self,
    ) -> typing.Optional["CfnModulePropsParametersServersTargetGroups"]:
        '''An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).

        :schema: CfnModulePropsParameters#ServersTargetGroups
        '''
        result = self._values.get("servers_target_groups")
        return typing.cast(typing.Optional["CfnModulePropsParametersServersTargetGroups"], result)

    @builtins.property
    def service_port(self) -> typing.Optional["CfnModulePropsParametersServicePort"]:
        '''The external Load Balancer listens to this port.

        Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS

        :schema: CfnModulePropsParameters#ServicePort
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional["CfnModulePropsParametersServicePort"], result)

    @builtins.property
    def shell_management_stack(
        self,
    ) -> typing.Optional["CfnModulePropsParametersShellManagementStack"]:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh

        :schema: CfnModulePropsParameters#ShellManagementStack
        '''
        result = self._values.get("shell_management_stack")
        return typing.cast(typing.Optional["CfnModulePropsParametersShellManagementStack"], result)

    @builtins.property
    def shell_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnModulePropsParametersShellSecurityGatewayStack"]:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh

        :schema: CfnModulePropsParameters#ShellSecurityGatewayStack
        '''
        result = self._values.get("shell_security_gateway_stack")
        return typing.cast(typing.Optional["CfnModulePropsParametersShellSecurityGatewayStack"], result)

    @builtins.property
    def source_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSourceSecurityGroup"]:
        '''The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.

        :schema: CfnModulePropsParameters#SourceSecurityGroup
        '''
        result = self._values.get("source_security_group")
        return typing.cast(typing.Optional["CfnModulePropsParametersSourceSecurityGroup"], result)

    @builtins.property
    def sts_roles(self) -> typing.Optional["CfnModulePropsParametersStsRoles"]:
        '''The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).

        :schema: CfnModulePropsParameters#STSRoles
        '''
        result = self._values.get("sts_roles")
        return typing.cast(typing.Optional["CfnModulePropsParametersStsRoles"], result)

    @builtins.property
    def tgw_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTgwSubnet1Cidr"]:
        '''CIDR block for TGW subnet 1 located in Availability Zone 1.

        Default: 10.0.12.0/24

        :schema: CfnModulePropsParameters#TgwSubnet1CIDR
        '''
        result = self._values.get("tgw_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersTgwSubnet1Cidr"], result)

    @builtins.property
    def tgw_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTgwSubnet2Cidr"]:
        '''CIDR block for TGW subnet 2 located in Availability Zone 2.

        Default: 10.0.22.0/24

        :schema: CfnModulePropsParameters#TgwSubnet2CIDR
        '''
        result = self._values.get("tgw_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersTgwSubnet2Cidr"], result)

    @builtins.property
    def tgw_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTgwSubnet3Cidr"]:
        '''CIDR block for TGW subnet 3 located in Availability Zone 3.

        Default: 10.0.32.0/24

        :schema: CfnModulePropsParameters#TgwSubnet3CIDR
        '''
        result = self._values.get("tgw_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersTgwSubnet3Cidr"], result)

    @builtins.property
    def tgw_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTgwSubnet4Cidr"]:
        '''CIDR block for TGW subnet 4 located in Availability Zone 4.

        Default: 10.0.42.0/24

        :schema: CfnModulePropsParameters#TgwSubnet4CIDR
        '''
        result = self._values.get("tgw_subnet4_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersTgwSubnet4Cidr"], result)

    @builtins.property
    def trusted_account(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTrustedAccount"]:
        '''A 12 digits number that represents the ID of a trusted account.

        IAM users in this account will be able assume the IAM role and receive the permissions attached to it.

        :schema: CfnModulePropsParameters#TrustedAccount
        '''
        result = self._values.get("trusted_account")
        return typing.cast(typing.Optional["CfnModulePropsParametersTrustedAccount"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        Default: 10.0.0.0/16

        :schema: CfnModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpccidr"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAdminCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAdminCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow web, SSH, and graphical clients only from this network to communicate with the Security Management Server.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAdminCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAdminCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAdminCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAdminCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAdminEmail",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAdminEmail:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Notifications about scaling events will be sent to this email address (optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAdminEmail
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAdminEmail#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAdminEmail#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAdminEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAlbProtocol",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAlbProtocol:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The protocol to use on the Application Load Balancer.

        If Network Load Balancer was selected this section will be ignored. Default: HTTP. Allowed values: HTTP, HTTPS

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAlbProtocol
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAlbProtocol#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAlbProtocol#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAlbProtocol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAllocatePublicAddress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAllocatePublicAddress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allocate an elastic IP for the Management.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAllocatePublicAddress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAllocatePublicAddress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAllocatePublicAddress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAllocatePublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAllowUploadDownload",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAllowUploadDownload:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Automatically download Blade Contracts and other important data.

        Improve product experience by sending data to Check Point. Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAllowUploadDownload
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAllowUploadDownload#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAllowUploadDownload#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAllowUploadDownload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZones:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''List of Availability Zones (AZs) to use for the subnets in the VPC.

        Select at least two

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersCertificate",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCertificate:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon Resource Name (ARN) of an HTTPS Certificate, ignored if the selected protocol is HTTP (for the ALBProtocol parameter).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCertificate
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCertificate#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCertificate#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCloudWatch:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Report Check Point specific CloudWatch metrics.

        Default: false

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCloudWatch
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCloudWatch#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCloudWatch#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Determines if the gateways are provisioned using their private or public address.

        Default: private. Allowed values: private, public

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersCreatePrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreatePrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored. Default: true

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersCreateTgwSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersCreateTgwSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set true for creating designated subnets for VPC TGW attachments.

        If false, the CIDR parameters for the TGW subnets will be ignored. Default: false

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersCreateTgwSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateTgwSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersCreateTgwSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersCreateTgwSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersElbClients",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersElbClients:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow clients only from this network to communicate with the Web Servers.

        Default: 0.0.0.0/0

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersElbClients
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbClients#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbClients#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersElbClients(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersElbPort",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersElbPort:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Port for the ELB.

        Default: 8080

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersElbPort
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbPort#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbPort#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersElbPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersElbType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersElbType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Elasitc Load Balancer Type.

        Default: none. Allowed values: none, internal, internet-facing

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersElbType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersElbType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersElbType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersEnableInstanceConnect",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableInstanceConnect:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enable SSH connection over AWS web console.

        Default: false

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableInstanceConnect
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableInstanceConnect#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableInstanceConnect#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableInstanceConnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersEnableVolumeEncryption",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableVolumeEncryption:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Encrypt Environment instances volume with default AWS KMS key.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableVolumeEncryption
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableVolumeEncryption#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableVolumeEncryption#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableVolumeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewayInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the Security Gateways.

        Default: c5.xlarge. Allowed values: c5.xlarge, c5.xlarge, c5.2xlarge, c5.4xlarge, c5.9xlarge, c5.18xlarge, c5n.large, c5n.xlarge, c5n.2xlarge, c5n.4xlarge, c5n.9xlarge, c5n.18xlarge

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewayInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewayManagement",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewayManagement:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select 'Over the internet' if any of the gateways you wish to manage are not directly accessed via their private IP address.

        Default: 'Locally managed'. Allowed values: Locally managed, Over the internet

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewayManagement
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayManagement#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayManagement#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewayManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewayPasswordHash",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewayPasswordHash:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewayPasswordHash
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayPasswordHash#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayPasswordHash#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewayPasswordHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaySicKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaySicKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaySicKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaySicKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaySicKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaySicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewayVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewayVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version and license to install on the Security Gateways.

        Default: R80.40-PAYG-NGTP-GW. Allowed values: R80.40-BYOL-GW, R80.40-PAYG-NGTP-GW, R80.40-PAYG-NGTX-GW, R81-BYOL-GW, R81-PAYG-NGTP-GW, R81-PAYG-NGTX-GW

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewayVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysAddresses",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysAddresses:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allow gateways only from this network to communicate with the Security Management Server.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysAddresses
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysAddresses#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysAddresses#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysBlades",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysBlades:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Turn on the Intrusion Prevention System, Application Control, Anti-Virus and Anti-Bot Blades (these and additional Blades can be manually turned on or off later).

        Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysBlades
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysBlades#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysBlades#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysBlades(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysMaxSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysMaxSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximal number of Security Gateways.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysMaxSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysMaxSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysMaxSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysMaxSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysMinSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysMinSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The minimal number of Security Gateways.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysMinSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysMinSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysMinSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysMinSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysPolicy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysPolicy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name of the Security Policy package to be installed on the gateways in the Security Gateways Auto Scaling group.

        Default: Standard

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysPolicy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysPolicy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersGatewaysTargetGroups",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersGatewaysTargetGroups:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces) (optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersGatewaysTargetGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysTargetGroups#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersGatewaysTargetGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersGatewaysTargetGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersKeyName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKeyName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 Key Pair to allow SSH access to the instances.

        For more detail visit: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersKeyName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKeyName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKeyName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKeyName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersLoadBalancersType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLoadBalancersType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Use Network Load Balancer if you wish to preserve the source IP address and Application Load Balancer if you wish to perform SSL Offloading.

        Default: Network Load Balancer. Allowed values: Network Load Balancer, Application Load Balancer

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLoadBalancersType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLoadBalancersType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLoadBalancersType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLoadBalancersType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementDeploy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementDeploy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select false to use an existing Security Management Server or to deploy one later and to ignore the other parameters of this section.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementDeploy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementDeploy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementDeploy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementHostname",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementHostname:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: mgmt-aws

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementHostname
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementHostname#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementHostname#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type of the Security Management Server.

        Default: m5.xlarge. Allowed values: m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.12xlarge, m5.24xlarge

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementPasswordHash",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementPasswordHash:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Admin user's password hash (use command "openssl passwd -1 PASSWORD" to get the PASSWORD's hash) (optional).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementPasswordHash
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPasswordHash#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPasswordHash#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementPasswordHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementPermissions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementPermissions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''IAM role to attach to the instance profile of the Management Server.

        Default: Create with read permissions. Allowed values: None (configure later), Use existing (specify an existing IAM role name), Create with assume role permissions (specify an STS role ARN), Create with read permissions, Create with read-write permissions

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementPermissions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPermissions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPermissions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementPredefinedRole",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementPredefinedRole:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A predefined IAM role to attach to the instance profile.

        Ignored if IAM role is not set to 'Use existing'

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementPredefinedRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPredefinedRole#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementPredefinedRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementPredefinedRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementSicKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementSicKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Mandatory only if deploying a secondary Management Server, the Secure Internal Communication key creates trusted connections between Check Point components.

        Choose a random string consisting of at least 8 alphanumeric characters

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementSicKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementSicKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementSicKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementSicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementStackVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementStackVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EBS Volume size of the management server.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementStackVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementStackVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementStackVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementStackVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersManagementVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersManagementVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version and license to install on the Security Management Server.

        Default: R80.40-PAYG-MGMT. Allowed values: R80.40-BYOL-MGMT, R80.40-PAYG-MGMT, R81-BYOL-MGMT, R81-PAYG-MGMT

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersManagementVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersManagementVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersManagementVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersNlbProtocol",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNlbProtocol:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The protocol to use on the Network Load Balancer.

        If Application Load Balancer was selected this section will be ignored. Default: TCP. Allowed values: TCP, TLS, UDP, TCP_UDP

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNlbProtocol
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNlbProtocol#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNlbProtocol#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNlbProtocol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersNtpPrimary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNtpPrimary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: 169.254.169.123

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNtpPrimary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNtpPrimary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNtpPrimary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNtpPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersNtpSecondary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNtpSecondary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(optional).

        Default: 0.pool.ntp.org

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNtpSecondary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNtpSecondary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNtpSecondary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNtpSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNumberOfAZs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.  Default: 2

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPermissions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPermissions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''IAM Permissions for the management server.

        Default: Create with read permissions. Allowed values: Create with read permissions Create with read-write permissions Create with assume role permissions (specify an STS role ARN)

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPermissions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPermissions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPermissions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPrimaryManagement",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrimaryManagement:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Determines if this is the primary Management Server or not.

        Default: true

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrimaryManagement
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrimaryManagement#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrimaryManagement#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrimaryManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1 located in the 1st Availability Zone.

        Default: 10.0.11.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.21.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPrivateSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.31.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPrivateSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4 located in the 4th Availability Zone.

        Default: 10.0.41.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet4Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersProvisionTag",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersProvisionTag:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The tag is used by the Security Management Server to automatically provision the Security Gateways.

        Must be up to 12 alphanumeric characters and unique for each Quick Start deployment. Default: quickstart

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersProvisionTag
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersProvisionTag#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersProvisionTag#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersProvisionTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 1 located in the 1st Availability Zone.

        If you choose to deploy a Security Management Server it will be deployed in this subnet. Default: 10.0.10.0/24

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 2 located in the 2nd Availability Zone.

        Default: 10.0.20.0/24

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 3 located in the 3rd Availability Zone.

        Default: 10.0.30.0/24

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersPublicSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for public subnet 4 located in the 4th Availability Zone.

        Default: 10.0.40.0/24

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersSecurityGatewayVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersSecurityGatewayVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EBS Volume size of the security gateway server.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersSecurityGatewayVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSecurityGatewayVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSecurityGatewayVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSecurityGatewayVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServerAmi",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServerAmi:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Amazon Machine Image ID of a preconfigured web server (e.g. ami-0dc7dc63).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServerAmi
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerAmi#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerAmi#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServerAmi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServerInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServerInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the web servers.

        Default: t3.micro. Allowed values: t3.nano, t3.micro, t3.small, t3.medium, t3.large, t3.xlarge, t3.2xlarge

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServerInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServerInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServerName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServerName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The servers name tag.

        Default: Server

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServerName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServersDeploy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServersDeploy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Select true to deploy web servers and an internal Application Load Balancer.

        If you select false the other parameters of this section will be ignored. Default: false

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServersDeploy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersDeploy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersDeploy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServersDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServersMaxSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServersMaxSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximal number of servers in the Auto Scaling group.

        Default: 10

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServersMaxSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersMaxSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersMaxSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServersMaxSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServersMinSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServersMinSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The minimal number of servers in the Auto Scaling group.

        Default: 2

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServersMinSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersMinSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersMinSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServersMinSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServersTargetGroups",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServersTargetGroups:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An optional list of Target Groups to associate with the Auto Scaling group (comma separated list of ARNs, without spaces).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServersTargetGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersTargetGroups#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServersTargetGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServersTargetGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersServicePort",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersServicePort:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The external Load Balancer listens to this port.

        Leave this field blank to use default ports: 80 for HTTP and 443 for HTTPS

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersServicePort
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServicePort#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersServicePort#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersShellManagementStack",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersShellManagementStack:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed values: /etc/cli.sh, /bin/bash, /bin/csh, /bin/tcsh

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersShellManagementStack
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersShellManagementStack#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersShellManagementStack#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersShellManagementStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersShellSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersShellSecurityGatewayStack:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Change the admin shell to enable advanced command line configuration.

        Default: /etc/cli.sh. Allowed Values: /etc/cli.sh /bin/bash /bin/csh /bin/tcsh

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersShellSecurityGatewayStack
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersShellSecurityGatewayStack#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersShellSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersShellSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersSourceSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersSourceSecurityGroup:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ID of Security Group from which access will be allowed to the instances in this Auto Scaling group.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersSourceSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSourceSecurityGroup#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSourceSecurityGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSourceSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersStsRoles",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersStsRoles:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The IAM role will be able to assume these STS Roles (comma separated list of ARNs, without spaces).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersStsRoles
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersStsRoles#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersStsRoles#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersStsRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersTgwSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersTgwSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 1 located in Availability Zone 1.

        Default: 10.0.12.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersTgwSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTgwSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersTgwSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersTgwSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 2 located in Availability Zone 2.

        Default: 10.0.22.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersTgwSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTgwSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersTgwSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersTgwSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 3 located in Availability Zone 3.

        Default: 10.0.32.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersTgwSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTgwSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersTgwSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersTgwSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for TGW subnet 4 located in Availability Zone 4.

        Default: 10.0.42.0/24

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersTgwSubnet4Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTgwSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTgwSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersTrustedAccount",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersTrustedAccount:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A 12 digits number that represents the ID of a trusted account.

        IAM users in this account will be able assume the IAM role and receive the permissions attached to it.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersTrustedAccount
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTrustedAccount#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTrustedAccount#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTrustedAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpccidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        Default: 10.0.0.0/16

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "address_assoc": "addressAssoc",
        "chkp_gateway_role": "chkpGatewayRole",
        "cmeiam_role": "cmeiamRole",
        "cpu_alarm_high": "cpuAlarmHigh",
        "cpu_alarm_high_security_gateway_stack": "cpuAlarmHighSecurityGatewayStack",
        "cpu_alarm_low": "cpuAlarmLow",
        "cpu_alarm_low_security_gateway_stack": "cpuAlarmLowSecurityGatewayStack",
        "elastic_load_balancer": "elasticLoadBalancer",
        "elb_security_group": "elbSecurityGroup",
        "external_alb_security_group": "externalAlbSecurityGroup",
        "external_lb_listener": "externalLbListener",
        "external_lb_target_group": "externalLbTargetGroup",
        "external_load_balancer": "externalLoadBalancer",
        "gateway_group": "gatewayGroup",
        "gateway_launch_config": "gatewayLaunchConfig",
        "gateway_scale_down_policy": "gatewayScaleDownPolicy",
        "gateway_scale_up_policy": "gatewayScaleUpPolicy",
        "instance_profile": "instanceProfile",
        "instance_profile_security_gateway_stack": "instanceProfileSecurityGatewayStack",
        "internal_lb_listener": "internalLbListener",
        "internal_lb_target_group": "internalLbTargetGroup",
        "internal_load_balancer": "internalLoadBalancer",
        "internal_security_group": "internalSecurityGroup",
        "internet_gateway": "internetGateway",
        "management_instance": "managementInstance",
        "management_ready_condition": "managementReadyCondition",
        "management_ready_handle": "managementReadyHandle",
        "management_security_group": "managementSecurityGroup",
        "notification_topic": "notificationTopic",
        "notification_topic_security_gateway_stack": "notificationTopicSecurityGatewayStack",
        "permissive_security_group": "permissiveSecurityGroup",
        "private_subnet1": "privateSubnet1",
        "private_subnet2": "privateSubnet2",
        "private_subnet3": "privateSubnet3",
        "private_subnet4": "privateSubnet4",
        "public_address": "publicAddress",
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
        "scale_down_policy": "scaleDownPolicy",
        "scale_up_policy": "scaleUpPolicy",
        "servers_group": "serversGroup",
        "servers_launch_configuration": "serversLaunchConfiguration",
        "servers_security_group": "serversSecurityGroup",
        "tgw_subnet1": "tgwSubnet1",
        "tgw_subnet2": "tgwSubnet2",
        "tgw_subnet3": "tgwSubnet3",
        "tgw_subnet4": "tgwSubnet4",
        "vpc": "vpc",
        "vpc_gateway_attachment": "vpcGatewayAttachment",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        address_assoc: typing.Optional["CfnModulePropsResourcesAddressAssoc"] = None,
        chkp_gateway_role: typing.Optional["CfnModulePropsResourcesChkpGatewayRole"] = None,
        cmeiam_role: typing.Optional["CfnModulePropsResourcesCmeiamRole"] = None,
        cpu_alarm_high: typing.Optional["CfnModulePropsResourcesCpuAlarmHigh"] = None,
        cpu_alarm_high_security_gateway_stack: typing.Optional["CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack"] = None,
        cpu_alarm_low: typing.Optional["CfnModulePropsResourcesCpuAlarmLow"] = None,
        cpu_alarm_low_security_gateway_stack: typing.Optional["CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack"] = None,
        elastic_load_balancer: typing.Optional["CfnModulePropsResourcesElasticLoadBalancer"] = None,
        elb_security_group: typing.Optional["CfnModulePropsResourcesElbSecurityGroup"] = None,
        external_alb_security_group: typing.Optional["CfnModulePropsResourcesExternalAlbSecurityGroup"] = None,
        external_lb_listener: typing.Optional["CfnModulePropsResourcesExternalLbListener"] = None,
        external_lb_target_group: typing.Optional["CfnModulePropsResourcesExternalLbTargetGroup"] = None,
        external_load_balancer: typing.Optional["CfnModulePropsResourcesExternalLoadBalancer"] = None,
        gateway_group: typing.Optional["CfnModulePropsResourcesGatewayGroup"] = None,
        gateway_launch_config: typing.Optional["CfnModulePropsResourcesGatewayLaunchConfig"] = None,
        gateway_scale_down_policy: typing.Optional["CfnModulePropsResourcesGatewayScaleDownPolicy"] = None,
        gateway_scale_up_policy: typing.Optional["CfnModulePropsResourcesGatewayScaleUpPolicy"] = None,
        instance_profile: typing.Optional["CfnModulePropsResourcesInstanceProfile"] = None,
        instance_profile_security_gateway_stack: typing.Optional["CfnModulePropsResourcesInstanceProfileSecurityGatewayStack"] = None,
        internal_lb_listener: typing.Optional["CfnModulePropsResourcesInternalLbListener"] = None,
        internal_lb_target_group: typing.Optional["CfnModulePropsResourcesInternalLbTargetGroup"] = None,
        internal_load_balancer: typing.Optional["CfnModulePropsResourcesInternalLoadBalancer"] = None,
        internal_security_group: typing.Optional["CfnModulePropsResourcesInternalSecurityGroup"] = None,
        internet_gateway: typing.Optional["CfnModulePropsResourcesInternetGateway"] = None,
        management_instance: typing.Optional["CfnModulePropsResourcesManagementInstance"] = None,
        management_ready_condition: typing.Optional["CfnModulePropsResourcesManagementReadyCondition"] = None,
        management_ready_handle: typing.Optional["CfnModulePropsResourcesManagementReadyHandle"] = None,
        management_security_group: typing.Optional["CfnModulePropsResourcesManagementSecurityGroup"] = None,
        notification_topic: typing.Optional["CfnModulePropsResourcesNotificationTopic"] = None,
        notification_topic_security_gateway_stack: typing.Optional["CfnModulePropsResourcesNotificationTopicSecurityGatewayStack"] = None,
        permissive_security_group: typing.Optional["CfnModulePropsResourcesPermissiveSecurityGroup"] = None,
        private_subnet1: typing.Optional["CfnModulePropsResourcesPrivateSubnet1"] = None,
        private_subnet2: typing.Optional["CfnModulePropsResourcesPrivateSubnet2"] = None,
        private_subnet3: typing.Optional["CfnModulePropsResourcesPrivateSubnet3"] = None,
        private_subnet4: typing.Optional["CfnModulePropsResourcesPrivateSubnet4"] = None,
        public_address: typing.Optional["CfnModulePropsResourcesPublicAddress"] = None,
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
        scale_down_policy: typing.Optional["CfnModulePropsResourcesScaleDownPolicy"] = None,
        scale_up_policy: typing.Optional["CfnModulePropsResourcesScaleUpPolicy"] = None,
        servers_group: typing.Optional["CfnModulePropsResourcesServersGroup"] = None,
        servers_launch_configuration: typing.Optional["CfnModulePropsResourcesServersLaunchConfiguration"] = None,
        servers_security_group: typing.Optional["CfnModulePropsResourcesServersSecurityGroup"] = None,
        tgw_subnet1: typing.Optional["CfnModulePropsResourcesTgwSubnet1"] = None,
        tgw_subnet2: typing.Optional["CfnModulePropsResourcesTgwSubnet2"] = None,
        tgw_subnet3: typing.Optional["CfnModulePropsResourcesTgwSubnet3"] = None,
        tgw_subnet4: typing.Optional["CfnModulePropsResourcesTgwSubnet4"] = None,
        vpc: typing.Optional["CfnModulePropsResourcesVpc"] = None,
        vpc_gateway_attachment: typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"] = None,
    ) -> None:
        '''
        :param address_assoc: 
        :param chkp_gateway_role: 
        :param cmeiam_role: 
        :param cpu_alarm_high: 
        :param cpu_alarm_high_security_gateway_stack: 
        :param cpu_alarm_low: 
        :param cpu_alarm_low_security_gateway_stack: 
        :param elastic_load_balancer: 
        :param elb_security_group: 
        :param external_alb_security_group: 
        :param external_lb_listener: 
        :param external_lb_target_group: 
        :param external_load_balancer: 
        :param gateway_group: 
        :param gateway_launch_config: 
        :param gateway_scale_down_policy: 
        :param gateway_scale_up_policy: 
        :param instance_profile: 
        :param instance_profile_security_gateway_stack: 
        :param internal_lb_listener: 
        :param internal_lb_target_group: 
        :param internal_load_balancer: 
        :param internal_security_group: 
        :param internet_gateway: 
        :param management_instance: 
        :param management_ready_condition: 
        :param management_ready_handle: 
        :param management_security_group: 
        :param notification_topic: 
        :param notification_topic_security_gateway_stack: 
        :param permissive_security_group: 
        :param private_subnet1: 
        :param private_subnet2: 
        :param private_subnet3: 
        :param private_subnet4: 
        :param public_address: 
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
        :param scale_down_policy: 
        :param scale_up_policy: 
        :param servers_group: 
        :param servers_launch_configuration: 
        :param servers_security_group: 
        :param tgw_subnet1: 
        :param tgw_subnet2: 
        :param tgw_subnet3: 
        :param tgw_subnet4: 
        :param vpc: 
        :param vpc_gateway_attachment: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(address_assoc, dict):
            address_assoc = CfnModulePropsResourcesAddressAssoc(**address_assoc)
        if isinstance(chkp_gateway_role, dict):
            chkp_gateway_role = CfnModulePropsResourcesChkpGatewayRole(**chkp_gateway_role)
        if isinstance(cmeiam_role, dict):
            cmeiam_role = CfnModulePropsResourcesCmeiamRole(**cmeiam_role)
        if isinstance(cpu_alarm_high, dict):
            cpu_alarm_high = CfnModulePropsResourcesCpuAlarmHigh(**cpu_alarm_high)
        if isinstance(cpu_alarm_high_security_gateway_stack, dict):
            cpu_alarm_high_security_gateway_stack = CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack(**cpu_alarm_high_security_gateway_stack)
        if isinstance(cpu_alarm_low, dict):
            cpu_alarm_low = CfnModulePropsResourcesCpuAlarmLow(**cpu_alarm_low)
        if isinstance(cpu_alarm_low_security_gateway_stack, dict):
            cpu_alarm_low_security_gateway_stack = CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack(**cpu_alarm_low_security_gateway_stack)
        if isinstance(elastic_load_balancer, dict):
            elastic_load_balancer = CfnModulePropsResourcesElasticLoadBalancer(**elastic_load_balancer)
        if isinstance(elb_security_group, dict):
            elb_security_group = CfnModulePropsResourcesElbSecurityGroup(**elb_security_group)
        if isinstance(external_alb_security_group, dict):
            external_alb_security_group = CfnModulePropsResourcesExternalAlbSecurityGroup(**external_alb_security_group)
        if isinstance(external_lb_listener, dict):
            external_lb_listener = CfnModulePropsResourcesExternalLbListener(**external_lb_listener)
        if isinstance(external_lb_target_group, dict):
            external_lb_target_group = CfnModulePropsResourcesExternalLbTargetGroup(**external_lb_target_group)
        if isinstance(external_load_balancer, dict):
            external_load_balancer = CfnModulePropsResourcesExternalLoadBalancer(**external_load_balancer)
        if isinstance(gateway_group, dict):
            gateway_group = CfnModulePropsResourcesGatewayGroup(**gateway_group)
        if isinstance(gateway_launch_config, dict):
            gateway_launch_config = CfnModulePropsResourcesGatewayLaunchConfig(**gateway_launch_config)
        if isinstance(gateway_scale_down_policy, dict):
            gateway_scale_down_policy = CfnModulePropsResourcesGatewayScaleDownPolicy(**gateway_scale_down_policy)
        if isinstance(gateway_scale_up_policy, dict):
            gateway_scale_up_policy = CfnModulePropsResourcesGatewayScaleUpPolicy(**gateway_scale_up_policy)
        if isinstance(instance_profile, dict):
            instance_profile = CfnModulePropsResourcesInstanceProfile(**instance_profile)
        if isinstance(instance_profile_security_gateway_stack, dict):
            instance_profile_security_gateway_stack = CfnModulePropsResourcesInstanceProfileSecurityGatewayStack(**instance_profile_security_gateway_stack)
        if isinstance(internal_lb_listener, dict):
            internal_lb_listener = CfnModulePropsResourcesInternalLbListener(**internal_lb_listener)
        if isinstance(internal_lb_target_group, dict):
            internal_lb_target_group = CfnModulePropsResourcesInternalLbTargetGroup(**internal_lb_target_group)
        if isinstance(internal_load_balancer, dict):
            internal_load_balancer = CfnModulePropsResourcesInternalLoadBalancer(**internal_load_balancer)
        if isinstance(internal_security_group, dict):
            internal_security_group = CfnModulePropsResourcesInternalSecurityGroup(**internal_security_group)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(management_instance, dict):
            management_instance = CfnModulePropsResourcesManagementInstance(**management_instance)
        if isinstance(management_ready_condition, dict):
            management_ready_condition = CfnModulePropsResourcesManagementReadyCondition(**management_ready_condition)
        if isinstance(management_ready_handle, dict):
            management_ready_handle = CfnModulePropsResourcesManagementReadyHandle(**management_ready_handle)
        if isinstance(management_security_group, dict):
            management_security_group = CfnModulePropsResourcesManagementSecurityGroup(**management_security_group)
        if isinstance(notification_topic, dict):
            notification_topic = CfnModulePropsResourcesNotificationTopic(**notification_topic)
        if isinstance(notification_topic_security_gateway_stack, dict):
            notification_topic_security_gateway_stack = CfnModulePropsResourcesNotificationTopicSecurityGatewayStack(**notification_topic_security_gateway_stack)
        if isinstance(permissive_security_group, dict):
            permissive_security_group = CfnModulePropsResourcesPermissiveSecurityGroup(**permissive_security_group)
        if isinstance(private_subnet1, dict):
            private_subnet1 = CfnModulePropsResourcesPrivateSubnet1(**private_subnet1)
        if isinstance(private_subnet2, dict):
            private_subnet2 = CfnModulePropsResourcesPrivateSubnet2(**private_subnet2)
        if isinstance(private_subnet3, dict):
            private_subnet3 = CfnModulePropsResourcesPrivateSubnet3(**private_subnet3)
        if isinstance(private_subnet4, dict):
            private_subnet4 = CfnModulePropsResourcesPrivateSubnet4(**private_subnet4)
        if isinstance(public_address, dict):
            public_address = CfnModulePropsResourcesPublicAddress(**public_address)
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
        if isinstance(scale_down_policy, dict):
            scale_down_policy = CfnModulePropsResourcesScaleDownPolicy(**scale_down_policy)
        if isinstance(scale_up_policy, dict):
            scale_up_policy = CfnModulePropsResourcesScaleUpPolicy(**scale_up_policy)
        if isinstance(servers_group, dict):
            servers_group = CfnModulePropsResourcesServersGroup(**servers_group)
        if isinstance(servers_launch_configuration, dict):
            servers_launch_configuration = CfnModulePropsResourcesServersLaunchConfiguration(**servers_launch_configuration)
        if isinstance(servers_security_group, dict):
            servers_security_group = CfnModulePropsResourcesServersSecurityGroup(**servers_security_group)
        if isinstance(tgw_subnet1, dict):
            tgw_subnet1 = CfnModulePropsResourcesTgwSubnet1(**tgw_subnet1)
        if isinstance(tgw_subnet2, dict):
            tgw_subnet2 = CfnModulePropsResourcesTgwSubnet2(**tgw_subnet2)
        if isinstance(tgw_subnet3, dict):
            tgw_subnet3 = CfnModulePropsResourcesTgwSubnet3(**tgw_subnet3)
        if isinstance(tgw_subnet4, dict):
            tgw_subnet4 = CfnModulePropsResourcesTgwSubnet4(**tgw_subnet4)
        if isinstance(vpc, dict):
            vpc = CfnModulePropsResourcesVpc(**vpc)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
        self._values: typing.Dict[str, typing.Any] = {}
        if address_assoc is not None:
            self._values["address_assoc"] = address_assoc
        if chkp_gateway_role is not None:
            self._values["chkp_gateway_role"] = chkp_gateway_role
        if cmeiam_role is not None:
            self._values["cmeiam_role"] = cmeiam_role
        if cpu_alarm_high is not None:
            self._values["cpu_alarm_high"] = cpu_alarm_high
        if cpu_alarm_high_security_gateway_stack is not None:
            self._values["cpu_alarm_high_security_gateway_stack"] = cpu_alarm_high_security_gateway_stack
        if cpu_alarm_low is not None:
            self._values["cpu_alarm_low"] = cpu_alarm_low
        if cpu_alarm_low_security_gateway_stack is not None:
            self._values["cpu_alarm_low_security_gateway_stack"] = cpu_alarm_low_security_gateway_stack
        if elastic_load_balancer is not None:
            self._values["elastic_load_balancer"] = elastic_load_balancer
        if elb_security_group is not None:
            self._values["elb_security_group"] = elb_security_group
        if external_alb_security_group is not None:
            self._values["external_alb_security_group"] = external_alb_security_group
        if external_lb_listener is not None:
            self._values["external_lb_listener"] = external_lb_listener
        if external_lb_target_group is not None:
            self._values["external_lb_target_group"] = external_lb_target_group
        if external_load_balancer is not None:
            self._values["external_load_balancer"] = external_load_balancer
        if gateway_group is not None:
            self._values["gateway_group"] = gateway_group
        if gateway_launch_config is not None:
            self._values["gateway_launch_config"] = gateway_launch_config
        if gateway_scale_down_policy is not None:
            self._values["gateway_scale_down_policy"] = gateway_scale_down_policy
        if gateway_scale_up_policy is not None:
            self._values["gateway_scale_up_policy"] = gateway_scale_up_policy
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile
        if instance_profile_security_gateway_stack is not None:
            self._values["instance_profile_security_gateway_stack"] = instance_profile_security_gateway_stack
        if internal_lb_listener is not None:
            self._values["internal_lb_listener"] = internal_lb_listener
        if internal_lb_target_group is not None:
            self._values["internal_lb_target_group"] = internal_lb_target_group
        if internal_load_balancer is not None:
            self._values["internal_load_balancer"] = internal_load_balancer
        if internal_security_group is not None:
            self._values["internal_security_group"] = internal_security_group
        if internet_gateway is not None:
            self._values["internet_gateway"] = internet_gateway
        if management_instance is not None:
            self._values["management_instance"] = management_instance
        if management_ready_condition is not None:
            self._values["management_ready_condition"] = management_ready_condition
        if management_ready_handle is not None:
            self._values["management_ready_handle"] = management_ready_handle
        if management_security_group is not None:
            self._values["management_security_group"] = management_security_group
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic
        if notification_topic_security_gateway_stack is not None:
            self._values["notification_topic_security_gateway_stack"] = notification_topic_security_gateway_stack
        if permissive_security_group is not None:
            self._values["permissive_security_group"] = permissive_security_group
        if private_subnet1 is not None:
            self._values["private_subnet1"] = private_subnet1
        if private_subnet2 is not None:
            self._values["private_subnet2"] = private_subnet2
        if private_subnet3 is not None:
            self._values["private_subnet3"] = private_subnet3
        if private_subnet4 is not None:
            self._values["private_subnet4"] = private_subnet4
        if public_address is not None:
            self._values["public_address"] = public_address
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
        if scale_down_policy is not None:
            self._values["scale_down_policy"] = scale_down_policy
        if scale_up_policy is not None:
            self._values["scale_up_policy"] = scale_up_policy
        if servers_group is not None:
            self._values["servers_group"] = servers_group
        if servers_launch_configuration is not None:
            self._values["servers_launch_configuration"] = servers_launch_configuration
        if servers_security_group is not None:
            self._values["servers_security_group"] = servers_security_group
        if tgw_subnet1 is not None:
            self._values["tgw_subnet1"] = tgw_subnet1
        if tgw_subnet2 is not None:
            self._values["tgw_subnet2"] = tgw_subnet2
        if tgw_subnet3 is not None:
            self._values["tgw_subnet3"] = tgw_subnet3
        if tgw_subnet4 is not None:
            self._values["tgw_subnet4"] = tgw_subnet4
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_gateway_attachment is not None:
            self._values["vpc_gateway_attachment"] = vpc_gateway_attachment

    @builtins.property
    def address_assoc(self) -> typing.Optional["CfnModulePropsResourcesAddressAssoc"]:
        '''
        :schema: CfnModulePropsResources#AddressAssoc
        '''
        result = self._values.get("address_assoc")
        return typing.cast(typing.Optional["CfnModulePropsResourcesAddressAssoc"], result)

    @builtins.property
    def chkp_gateway_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesChkpGatewayRole"]:
        '''
        :schema: CfnModulePropsResources#ChkpGatewayRole
        '''
        result = self._values.get("chkp_gateway_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesChkpGatewayRole"], result)

    @builtins.property
    def cmeiam_role(self) -> typing.Optional["CfnModulePropsResourcesCmeiamRole"]:
        '''
        :schema: CfnModulePropsResources#CMEIAMRole
        '''
        result = self._values.get("cmeiam_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCmeiamRole"], result)

    @builtins.property
    def cpu_alarm_high(self) -> typing.Optional["CfnModulePropsResourcesCpuAlarmHigh"]:
        '''
        :schema: CfnModulePropsResources#CPUAlarmHigh
        '''
        result = self._values.get("cpu_alarm_high")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCpuAlarmHigh"], result)

    @builtins.property
    def cpu_alarm_high_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack"]:
        '''
        :schema: CfnModulePropsResources#CPUAlarmHighSecurityGatewayStack
        '''
        result = self._values.get("cpu_alarm_high_security_gateway_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack"], result)

    @builtins.property
    def cpu_alarm_low(self) -> typing.Optional["CfnModulePropsResourcesCpuAlarmLow"]:
        '''
        :schema: CfnModulePropsResources#CPUAlarmLow
        '''
        result = self._values.get("cpu_alarm_low")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCpuAlarmLow"], result)

    @builtins.property
    def cpu_alarm_low_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack"]:
        '''
        :schema: CfnModulePropsResources#CPUAlarmLowSecurityGatewayStack
        '''
        result = self._values.get("cpu_alarm_low_security_gateway_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack"], result)

    @builtins.property
    def elastic_load_balancer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesElasticLoadBalancer"]:
        '''
        :schema: CfnModulePropsResources#ElasticLoadBalancer
        '''
        result = self._values.get("elastic_load_balancer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesElasticLoadBalancer"], result)

    @builtins.property
    def elb_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesElbSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#ELBSecurityGroup
        '''
        result = self._values.get("elb_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesElbSecurityGroup"], result)

    @builtins.property
    def external_alb_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesExternalAlbSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#ExternalALBSecurityGroup
        '''
        result = self._values.get("external_alb_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesExternalAlbSecurityGroup"], result)

    @builtins.property
    def external_lb_listener(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesExternalLbListener"]:
        '''
        :schema: CfnModulePropsResources#ExternalLBListener
        '''
        result = self._values.get("external_lb_listener")
        return typing.cast(typing.Optional["CfnModulePropsResourcesExternalLbListener"], result)

    @builtins.property
    def external_lb_target_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesExternalLbTargetGroup"]:
        '''
        :schema: CfnModulePropsResources#ExternalLBTargetGroup
        '''
        result = self._values.get("external_lb_target_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesExternalLbTargetGroup"], result)

    @builtins.property
    def external_load_balancer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesExternalLoadBalancer"]:
        '''
        :schema: CfnModulePropsResources#ExternalLoadBalancer
        '''
        result = self._values.get("external_load_balancer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesExternalLoadBalancer"], result)

    @builtins.property
    def gateway_group(self) -> typing.Optional["CfnModulePropsResourcesGatewayGroup"]:
        '''
        :schema: CfnModulePropsResources#GatewayGroup
        '''
        result = self._values.get("gateway_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesGatewayGroup"], result)

    @builtins.property
    def gateway_launch_config(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesGatewayLaunchConfig"]:
        '''
        :schema: CfnModulePropsResources#GatewayLaunchConfig
        '''
        result = self._values.get("gateway_launch_config")
        return typing.cast(typing.Optional["CfnModulePropsResourcesGatewayLaunchConfig"], result)

    @builtins.property
    def gateway_scale_down_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesGatewayScaleDownPolicy"]:
        '''
        :schema: CfnModulePropsResources#GatewayScaleDownPolicy
        '''
        result = self._values.get("gateway_scale_down_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesGatewayScaleDownPolicy"], result)

    @builtins.property
    def gateway_scale_up_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesGatewayScaleUpPolicy"]:
        '''
        :schema: CfnModulePropsResources#GatewayScaleUpPolicy
        '''
        result = self._values.get("gateway_scale_up_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesGatewayScaleUpPolicy"], result)

    @builtins.property
    def instance_profile(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInstanceProfile"]:
        '''
        :schema: CfnModulePropsResources#InstanceProfile
        '''
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInstanceProfile"], result)

    @builtins.property
    def instance_profile_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInstanceProfileSecurityGatewayStack"]:
        '''
        :schema: CfnModulePropsResources#InstanceProfileSecurityGatewayStack
        '''
        result = self._values.get("instance_profile_security_gateway_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInstanceProfileSecurityGatewayStack"], result)

    @builtins.property
    def internal_lb_listener(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternalLbListener"]:
        '''
        :schema: CfnModulePropsResources#InternalLBListener
        '''
        result = self._values.get("internal_lb_listener")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternalLbListener"], result)

    @builtins.property
    def internal_lb_target_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternalLbTargetGroup"]:
        '''
        :schema: CfnModulePropsResources#InternalLBTargetGroup
        '''
        result = self._values.get("internal_lb_target_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternalLbTargetGroup"], result)

    @builtins.property
    def internal_load_balancer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternalLoadBalancer"]:
        '''
        :schema: CfnModulePropsResources#InternalLoadBalancer
        '''
        result = self._values.get("internal_load_balancer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternalLoadBalancer"], result)

    @builtins.property
    def internal_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternalSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#InternalSecurityGroup
        '''
        result = self._values.get("internal_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternalSecurityGroup"], result)

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
    def management_instance(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesManagementInstance"]:
        '''
        :schema: CfnModulePropsResources#ManagementInstance
        '''
        result = self._values.get("management_instance")
        return typing.cast(typing.Optional["CfnModulePropsResourcesManagementInstance"], result)

    @builtins.property
    def management_ready_condition(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesManagementReadyCondition"]:
        '''
        :schema: CfnModulePropsResources#ManagementReadyCondition
        '''
        result = self._values.get("management_ready_condition")
        return typing.cast(typing.Optional["CfnModulePropsResourcesManagementReadyCondition"], result)

    @builtins.property
    def management_ready_handle(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesManagementReadyHandle"]:
        '''
        :schema: CfnModulePropsResources#ManagementReadyHandle
        '''
        result = self._values.get("management_ready_handle")
        return typing.cast(typing.Optional["CfnModulePropsResourcesManagementReadyHandle"], result)

    @builtins.property
    def management_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesManagementSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#ManagementSecurityGroup
        '''
        result = self._values.get("management_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesManagementSecurityGroup"], result)

    @builtins.property
    def notification_topic(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesNotificationTopic"]:
        '''
        :schema: CfnModulePropsResources#NotificationTopic
        '''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNotificationTopic"], result)

    @builtins.property
    def notification_topic_security_gateway_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesNotificationTopicSecurityGatewayStack"]:
        '''
        :schema: CfnModulePropsResources#NotificationTopicSecurityGatewayStack
        '''
        result = self._values.get("notification_topic_security_gateway_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesNotificationTopicSecurityGatewayStack"], result)

    @builtins.property
    def permissive_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPermissiveSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#PermissiveSecurityGroup
        '''
        result = self._values.get("permissive_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPermissiveSecurityGroup"], result)

    @builtins.property
    def private_subnet1(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet1"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet1
        '''
        result = self._values.get("private_subnet1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet1"], result)

    @builtins.property
    def private_subnet2(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet2"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet2
        '''
        result = self._values.get("private_subnet2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet2"], result)

    @builtins.property
    def private_subnet3(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet3"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet3
        '''
        result = self._values.get("private_subnet3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet3"], result)

    @builtins.property
    def private_subnet4(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPrivateSubnet4"]:
        '''
        :schema: CfnModulePropsResources#PrivateSubnet4
        '''
        result = self._values.get("private_subnet4")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPrivateSubnet4"], result)

    @builtins.property
    def public_address(self) -> typing.Optional["CfnModulePropsResourcesPublicAddress"]:
        '''
        :schema: CfnModulePropsResources#PublicAddress
        '''
        result = self._values.get("public_address")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicAddress"], result)

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
    def scale_down_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesScaleDownPolicy"]:
        '''
        :schema: CfnModulePropsResources#ScaleDownPolicy
        '''
        result = self._values.get("scale_down_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesScaleDownPolicy"], result)

    @builtins.property
    def scale_up_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesScaleUpPolicy"]:
        '''
        :schema: CfnModulePropsResources#ScaleUpPolicy
        '''
        result = self._values.get("scale_up_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesScaleUpPolicy"], result)

    @builtins.property
    def servers_group(self) -> typing.Optional["CfnModulePropsResourcesServersGroup"]:
        '''
        :schema: CfnModulePropsResources#ServersGroup
        '''
        result = self._values.get("servers_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesServersGroup"], result)

    @builtins.property
    def servers_launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesServersLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#ServersLaunchConfiguration
        '''
        result = self._values.get("servers_launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesServersLaunchConfiguration"], result)

    @builtins.property
    def servers_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesServersSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#ServersSecurityGroup
        '''
        result = self._values.get("servers_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesServersSecurityGroup"], result)

    @builtins.property
    def tgw_subnet1(self) -> typing.Optional["CfnModulePropsResourcesTgwSubnet1"]:
        '''
        :schema: CfnModulePropsResources#TgwSubnet1
        '''
        result = self._values.get("tgw_subnet1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesTgwSubnet1"], result)

    @builtins.property
    def tgw_subnet2(self) -> typing.Optional["CfnModulePropsResourcesTgwSubnet2"]:
        '''
        :schema: CfnModulePropsResources#TgwSubnet2
        '''
        result = self._values.get("tgw_subnet2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesTgwSubnet2"], result)

    @builtins.property
    def tgw_subnet3(self) -> typing.Optional["CfnModulePropsResourcesTgwSubnet3"]:
        '''
        :schema: CfnModulePropsResources#TgwSubnet3
        '''
        result = self._values.get("tgw_subnet3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesTgwSubnet3"], result)

    @builtins.property
    def tgw_subnet4(self) -> typing.Optional["CfnModulePropsResourcesTgwSubnet4"]:
        '''
        :schema: CfnModulePropsResources#TgwSubnet4
        '''
        result = self._values.get("tgw_subnet4")
        return typing.cast(typing.Optional["CfnModulePropsResourcesTgwSubnet4"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnModulePropsResourcesVpc"]:
        '''
        :schema: CfnModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpc"], result)

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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesAddressAssoc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesAddressAssoc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesAddressAssoc
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesAddressAssoc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesAddressAssoc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesAddressAssoc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesChkpGatewayRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesChkpGatewayRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesChkpGatewayRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesChkpGatewayRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesChkpGatewayRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesChkpGatewayRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesCmeiamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCmeiamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCmeiamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCmeiamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCmeiamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCmeiamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesCpuAlarmHigh",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCpuAlarmHigh:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCpuAlarmHigh
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmHigh#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmHigh#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCpuAlarmHigh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesCpuAlarmLow",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCpuAlarmLow:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCpuAlarmLow
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmLow#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmLow#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCpuAlarmLow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesElasticLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesElasticLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesElasticLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesElasticLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesElasticLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesElasticLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesElbSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesElbSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesElbSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesElbSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesElbSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesElbSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesExternalAlbSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesExternalAlbSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesExternalAlbSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesExternalAlbSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesExternalAlbSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesExternalAlbSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesExternalLbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesExternalLbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesExternalLbListener
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesExternalLbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesExternalLbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesExternalLbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesExternalLbTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesExternalLbTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesExternalLbTargetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesExternalLbTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesExternalLbTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesExternalLbTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesExternalLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesExternalLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesExternalLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesExternalLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesExternalLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesExternalLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesGatewayGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesGatewayGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesGatewayGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesGatewayGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesGatewayGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesGatewayGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesGatewayLaunchConfig",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesGatewayLaunchConfig:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesGatewayLaunchConfig
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesGatewayLaunchConfig#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesGatewayLaunchConfig#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesGatewayLaunchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesGatewayScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesGatewayScaleDownPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesGatewayScaleDownPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesGatewayScaleDownPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesGatewayScaleDownPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesGatewayScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesGatewayScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesGatewayScaleUpPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesGatewayScaleUpPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesGatewayScaleUpPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesGatewayScaleUpPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesGatewayScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInstanceProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInstanceProfileSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInstanceProfileSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInstanceProfileSecurityGatewayStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInstanceProfileSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInstanceProfileSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInstanceProfileSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInternalLbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternalLbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternalLbListener
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternalLbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternalLbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternalLbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInternalLbTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternalLbTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternalLbTargetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternalLbTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternalLbTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternalLbTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInternalLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternalLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternalLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternalLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternalLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternalLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInternalSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternalSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternalSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternalSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternalSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternalSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesInternetGateway",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesManagementInstance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesManagementInstance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesManagementInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesManagementInstance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesManagementInstance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesManagementInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesManagementReadyCondition",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesManagementReadyCondition:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesManagementReadyCondition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesManagementReadyCondition#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesManagementReadyCondition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesManagementReadyCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesManagementReadyHandle",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesManagementReadyHandle:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesManagementReadyHandle
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesManagementReadyHandle#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesManagementReadyHandle#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesManagementReadyHandle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesManagementSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesManagementSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesManagementSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesManagementSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesManagementSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesManagementSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesNotificationTopic",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNotificationTopic:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNotificationTopic
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNotificationTopic#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNotificationTopic#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNotificationTopic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesNotificationTopicSecurityGatewayStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesNotificationTopicSecurityGatewayStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesNotificationTopicSecurityGatewayStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesNotificationTopicSecurityGatewayStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesNotificationTopicSecurityGatewayStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesNotificationTopicSecurityGatewayStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPermissiveSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPermissiveSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPermissiveSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPermissiveSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPermissiveSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPermissiveSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPrivateSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPrivateSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPrivateSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPrivateSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPrivateSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPrivateSubnet4
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPrivateSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPrivateSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicAddress",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicAddress:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicAddress
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicAddress#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicAddress#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet1",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet2",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet3",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet3RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet4",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnet4RouteTableAssociation",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnetRoute",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesPublicSubnetRouteTable",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesScaleDownPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesScaleDownPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesScaleDownPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesScaleDownPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesScaleUpPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesScaleUpPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesScaleUpPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesScaleUpPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesServersGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesServersGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesServersGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesServersGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesServersGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesServersGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesServersLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesServersLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesServersLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesServersLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesServersLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesServersLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesServersSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesServersSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesServersSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesServersSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesServersSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesServersSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesTgwSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesTgwSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesTgwSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesTgwSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesTgwSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesTgwSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesTgwSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesTgwSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesTgwSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesTgwSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesTgwSubnet3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesTgwSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesTgwSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesTgwSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesTgwSubnet4
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesTgwSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesTgwSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesVpc",
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
    jsii_type="@cdk-cloudformation/awsqs-checkpoint-cloudguardqs-module.CfnModulePropsResourcesVpcGatewayAttachment",
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


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersAdminCidr",
    "CfnModulePropsParametersAdminEmail",
    "CfnModulePropsParametersAlbProtocol",
    "CfnModulePropsParametersAllocatePublicAddress",
    "CfnModulePropsParametersAllowUploadDownload",
    "CfnModulePropsParametersAvailabilityZones",
    "CfnModulePropsParametersCertificate",
    "CfnModulePropsParametersCloudWatch",
    "CfnModulePropsParametersControlGatewayOverPrivateOrPublicAddress",
    "CfnModulePropsParametersCreatePrivateSubnets",
    "CfnModulePropsParametersCreateTgwSubnets",
    "CfnModulePropsParametersElbClients",
    "CfnModulePropsParametersElbPort",
    "CfnModulePropsParametersElbType",
    "CfnModulePropsParametersEnableInstanceConnect",
    "CfnModulePropsParametersEnableVolumeEncryption",
    "CfnModulePropsParametersGatewayInstanceType",
    "CfnModulePropsParametersGatewayManagement",
    "CfnModulePropsParametersGatewayPasswordHash",
    "CfnModulePropsParametersGatewaySicKey",
    "CfnModulePropsParametersGatewayVersion",
    "CfnModulePropsParametersGatewaysAddresses",
    "CfnModulePropsParametersGatewaysBlades",
    "CfnModulePropsParametersGatewaysMaxSize",
    "CfnModulePropsParametersGatewaysMinSize",
    "CfnModulePropsParametersGatewaysPolicy",
    "CfnModulePropsParametersGatewaysTargetGroups",
    "CfnModulePropsParametersKeyName",
    "CfnModulePropsParametersLoadBalancersType",
    "CfnModulePropsParametersManagementDeploy",
    "CfnModulePropsParametersManagementHostname",
    "CfnModulePropsParametersManagementInstanceType",
    "CfnModulePropsParametersManagementPasswordHash",
    "CfnModulePropsParametersManagementPermissions",
    "CfnModulePropsParametersManagementPredefinedRole",
    "CfnModulePropsParametersManagementSicKey",
    "CfnModulePropsParametersManagementStackVolumeSize",
    "CfnModulePropsParametersManagementVersion",
    "CfnModulePropsParametersNlbProtocol",
    "CfnModulePropsParametersNtpPrimary",
    "CfnModulePropsParametersNtpSecondary",
    "CfnModulePropsParametersNumberOfAZs",
    "CfnModulePropsParametersPermissions",
    "CfnModulePropsParametersPrimaryManagement",
    "CfnModulePropsParametersPrivateSubnet1Cidr",
    "CfnModulePropsParametersPrivateSubnet2Cidr",
    "CfnModulePropsParametersPrivateSubnet3Cidr",
    "CfnModulePropsParametersPrivateSubnet4Cidr",
    "CfnModulePropsParametersProvisionTag",
    "CfnModulePropsParametersPublicSubnet1Cidr",
    "CfnModulePropsParametersPublicSubnet2Cidr",
    "CfnModulePropsParametersPublicSubnet3Cidr",
    "CfnModulePropsParametersPublicSubnet4Cidr",
    "CfnModulePropsParametersSecurityGatewayVolumeSize",
    "CfnModulePropsParametersServerAmi",
    "CfnModulePropsParametersServerInstanceType",
    "CfnModulePropsParametersServerName",
    "CfnModulePropsParametersServersDeploy",
    "CfnModulePropsParametersServersMaxSize",
    "CfnModulePropsParametersServersMinSize",
    "CfnModulePropsParametersServersTargetGroups",
    "CfnModulePropsParametersServicePort",
    "CfnModulePropsParametersShellManagementStack",
    "CfnModulePropsParametersShellSecurityGatewayStack",
    "CfnModulePropsParametersSourceSecurityGroup",
    "CfnModulePropsParametersStsRoles",
    "CfnModulePropsParametersTgwSubnet1Cidr",
    "CfnModulePropsParametersTgwSubnet2Cidr",
    "CfnModulePropsParametersTgwSubnet3Cidr",
    "CfnModulePropsParametersTgwSubnet4Cidr",
    "CfnModulePropsParametersTrustedAccount",
    "CfnModulePropsParametersVpccidr",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesAddressAssoc",
    "CfnModulePropsResourcesChkpGatewayRole",
    "CfnModulePropsResourcesCmeiamRole",
    "CfnModulePropsResourcesCpuAlarmHigh",
    "CfnModulePropsResourcesCpuAlarmHighSecurityGatewayStack",
    "CfnModulePropsResourcesCpuAlarmLow",
    "CfnModulePropsResourcesCpuAlarmLowSecurityGatewayStack",
    "CfnModulePropsResourcesElasticLoadBalancer",
    "CfnModulePropsResourcesElbSecurityGroup",
    "CfnModulePropsResourcesExternalAlbSecurityGroup",
    "CfnModulePropsResourcesExternalLbListener",
    "CfnModulePropsResourcesExternalLbTargetGroup",
    "CfnModulePropsResourcesExternalLoadBalancer",
    "CfnModulePropsResourcesGatewayGroup",
    "CfnModulePropsResourcesGatewayLaunchConfig",
    "CfnModulePropsResourcesGatewayScaleDownPolicy",
    "CfnModulePropsResourcesGatewayScaleUpPolicy",
    "CfnModulePropsResourcesInstanceProfile",
    "CfnModulePropsResourcesInstanceProfileSecurityGatewayStack",
    "CfnModulePropsResourcesInternalLbListener",
    "CfnModulePropsResourcesInternalLbTargetGroup",
    "CfnModulePropsResourcesInternalLoadBalancer",
    "CfnModulePropsResourcesInternalSecurityGroup",
    "CfnModulePropsResourcesInternetGateway",
    "CfnModulePropsResourcesManagementInstance",
    "CfnModulePropsResourcesManagementReadyCondition",
    "CfnModulePropsResourcesManagementReadyHandle",
    "CfnModulePropsResourcesManagementSecurityGroup",
    "CfnModulePropsResourcesNotificationTopic",
    "CfnModulePropsResourcesNotificationTopicSecurityGatewayStack",
    "CfnModulePropsResourcesPermissiveSecurityGroup",
    "CfnModulePropsResourcesPrivateSubnet1",
    "CfnModulePropsResourcesPrivateSubnet2",
    "CfnModulePropsResourcesPrivateSubnet3",
    "CfnModulePropsResourcesPrivateSubnet4",
    "CfnModulePropsResourcesPublicAddress",
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
    "CfnModulePropsResourcesScaleDownPolicy",
    "CfnModulePropsResourcesScaleUpPolicy",
    "CfnModulePropsResourcesServersGroup",
    "CfnModulePropsResourcesServersLaunchConfiguration",
    "CfnModulePropsResourcesServersSecurityGroup",
    "CfnModulePropsResourcesTgwSubnet1",
    "CfnModulePropsResourcesTgwSubnet2",
    "CfnModulePropsResourcesTgwSubnet3",
    "CfnModulePropsResourcesTgwSubnet4",
    "CfnModulePropsResourcesVpc",
    "CfnModulePropsResourcesVpcGatewayAttachment",
]

publication.publish()
