from typing import Type, Optional, List
from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.context.aws.aws_environment_context_defaults_merger import AwsEnvironmentContextDefaultsMerger
from cloudrail.knowledge.context.aws.aws_environment_context_enrichment import AwsEnvironmentContextEnrichment
from cloudrail.knowledge.context.aws.cloudformation.aws_cloudformation_context_builder import AwsCloudformationContextBuilder
from cloudrail.knowledge.context.aws.resources.cloudfront.origin_access_identity import OriginAccessIdentity
from cloudrail.knowledge.context.aws.resources.ec2.security_group_rule import ConnectionType, SecurityGroupRule, SecurityGroupRulePropertyType
from cloudrail.knowledge.context.aws.resources_assigner_util import ResourcesAssignerUtil
from cloudrail.knowledge.context.aws.scanner.aws_scanner_context_builder import AwsScannerContextBuilder
from cloudrail.knowledge.context.environment_context.base_environment_context_builder import BaseEnvironmentContextBuilder
from cloudrail.knowledge.context.environment_context.business_logic.resource_invalidator import ResourceInvalidator
from cloudrail.knowledge.context.environment_context.environment_context_defaults_merger import EnvironmentContextDefaultsMerger
from cloudrail.knowledge.context.environment_context.environment_context_enrichment import EnvironmentContextEnrichment
from cloudrail.knowledge.context.environment_context.iac_context_builder import IacContextBuilder
from cloudrail.knowledge.context.environment_context.scanner_context_builder import ScannerContextBuilder
from cloudrail.knowledge.context.ip_protocol import IpProtocol


class AwsCloudformationEnvironmentContextBuilder(BaseEnvironmentContextBuilder):

    @classmethod
    def get_default_account_id(cls) -> str:
        return '000000000000'

    @classmethod
    def get_scanner_builder_type(cls) -> Type[ScannerContextBuilder]:
        return AwsScannerContextBuilder

    @classmethod
    def get_iac_builder_type(cls) -> Type[IacContextBuilder]:
        return AwsCloudformationContextBuilder

    @classmethod
    def get_defaults_merger_type(cls) -> Optional[Type[EnvironmentContextDefaultsMerger]]:
        return AwsEnvironmentContextDefaultsMerger

    @classmethod
    def get_context_enrichment_type(cls) -> Type[EnvironmentContextEnrichment]:
        return AwsEnvironmentContextEnrichment

    @classmethod
    def basic_enrich_before_merge(cls, scanner_ctx: AwsEnvironmentContext, iac_ctx: AwsEnvironmentContext):
        AwsCloudformationEnvironmentContextBuilder._add_security_group_with_no_vpc_data(scanner_ctx, iac_ctx)
        AwsCloudformationEnvironmentContextBuilder._assign_s3_canonical_id_to_origin_access\
            (scanner_ctx.origin_access_identity_list, iac_ctx.origin_access_identity_list)

    @staticmethod
    def _add_security_group_with_no_vpc_data(scanner_ctx: AwsEnvironmentContext, iac_ctx: AwsEnvironmentContext):
        for security_group in iac_ctx.security_groups:
            if not security_group.vpc_id:
                resource_tag_arn = next((tag_resource.resource_arn for tag_resource in scanner_ctx.resources_tagging_list
                        if tag_resource.tags.get('aws:cloudformation:logical-id') == security_group.iac_state.address), None)
                if resource_tag_arn:
                    security_group.security_group_id = resource_tag_arn.split('/')[1]
                default_vpc = ResourceInvalidator.get_by_logic(
                            lambda: ResourcesAssignerUtil.get_default_vpc(scanner_ctx.vpcs, security_group.account, security_group.region),
                            True,
                            security_group,
                            f'Could not find default vpc in the region {security_group.region} for account {security_group.account}')
                security_group.vpc_id = default_vpc.vpc_id
                security_group.outbound_permissions.append(SecurityGroupRule(0, 65535, IpProtocol('-1'),
                                                                            SecurityGroupRulePropertyType.IP_RANGES,
                                                                            '0.0.0.0/0', False,
                                                                            ConnectionType.OUTBOUND,
                                                                            security_group.security_group_id,
                                                                            security_group.region,
                                                                            security_group.account))

    @staticmethod
    def _assign_s3_canonical_id_to_origin_access(scanner_ctx: List[OriginAccessIdentity],
                                                 iac_ctx: List[OriginAccessIdentity]):
        for scanner_oai in scanner_ctx:
            iac_oai = next((oai for oai in iac_ctx if oai.oai_id == scanner_oai.oai_id), None)
            if iac_oai:
                iac_oai.s3_canonical_user_id = scanner_oai.s3_canonical_user_id
