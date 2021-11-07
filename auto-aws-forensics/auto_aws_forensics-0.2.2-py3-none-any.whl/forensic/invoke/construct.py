from aws_cdk import (
    core as cdk,
    aws_iam as iam,
    aws_stepfunctions as stepfunctions,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as events_targets
)
import pathlib
from typing import Union


class InvokeConstruct(cdk.Construct):
    def __init__(self, scope: cdk.Construct,
                 id: str,
                 automation_role: Union[iam.Role, iam.IRole],
                 forensic_sfn: stepfunctions.StateMachine):
        """
        Invoke construct builds the resources that will monitor for an event and generate
        the execution.
        :param automation_role:
        :param forensic_sfn:
        """
        super().__init__(scope, id=id)
        self.automation_role = automation_role
        self.forensic_sfn = forensic_sfn
        self.securityhub_event = None
        self.guardduty_event = None
        self.disk_process = self.build_disk_process_lambda()
        # self.invoke_from_securityhub()
        self.invoke_from_guardduty()

    def build_disk_process_lambda(self) -> _lambda.Function:
        """
        Build the lambda function that will initiate the Step Functions.
        This lambda function uses an event JSON generated by security hub.
        https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-syntax.html
        :return:
        """
        role = iam.Role(self, "DiskForensicInvokePolicy",
                        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                        description="Disk Forensic Automation Role to provide access for Lambda to invoke disk collection step function")
        role.add_to_policy(iam.PolicyStatement(
            sid='SFNPermissions',
            actions=['states:StartExecution'],
            effect=iam.Effect.ALLOW,
            resources=["*"]  # TODO - Make this specific to the step function later
        ))
        role.add_to_policy(iam.PolicyStatement(
            sid="LogsPermissions",
            actions=['logs:CreateLogGroup',
                     'logs:CreateLogStream',
                     'logs:DescribeLogGroups',
                     'logs:DescribeLogStreams',
                     'logs:GetLogEvents',
                     'logs:PutLogEvents'],
            effect=iam.Effect.ALLOW,
            resources=["*"]

        ))

        lambda_function = _lambda.Function(self, f"DiskInvokeGuardDuty",
                                           runtime=_lambda.Runtime.PYTHON_3_8,
                                           description="Lambda used to Invoke Forensics Step Function",
                                           handler="disk_invoke_guardduty.lambda_handler",
                                           code=_lambda.Code.from_asset(
                                               str(pathlib.Path(__file__).parents[0] / 'assets/')),
                                           timeout=cdk.Duration.seconds(180),
                                           role=role,
                                           environment={"ForensicSFNARN": self.forensic_sfn.state_machine_arn}
                                           )
        return lambda_function

    def invoke_from_securityhub(self) -> None:
        """
        Creates a log rule that looks for security hub identifying a critical or high resource.

        Built based on the  DiskForensicsEventRule resource in diskForensicInvoke.yaml

        The original event is based on Security Hub publishing.  But, that is adding too much
        complexity.  So, going to look for GuardDuty right away.

        For testing, we are only looking at Critical.
        TODO - Allow the builder to determine the lowest level of security hub alert from which to invoke
        the lambda function
        :return:
        """

        """
        This is for monitoring a security hub finding of a GuardDuty action. 
        detail_type = ["GuardDuty Finding"]
        """

        # source = ["aws.securityhub"]
        detail_type = ["Security Hub Findings - Imported"]
        detail = {"findings": {"aws/securityhub/SeverityLabel": ["CRITICAL"],
                               "aws/securityhub/ProductName": ["GuardDuty"]}}
        source = ["aws.securityhub"]

        if self.securityhub_event is None:
            self.securityhub_event = events.Rule(self, "SecurityHubTriggerRule",
                                                 description="SecurityHub Trigger Rule",
                                                 event_pattern=events.EventPattern(
                                                   detail_type=detail_type,
                                                   source=source,
                                                   detail=detail
                                                   ),
                                                 enabled=True,
                                                 )
            self.securityhub_event.add_target(events_targets.LambdaFunction(self.disk_process))
        else:
            print("Already been built")

    def invoke_from_guardduty(self)->None:
        """
        Creates a log rule that looks for guardduty identifying a critical or high resource.

        Built based on the  DiskForensicsEventRule resource in diskForensicInvoke.yaml

        The original event is based on Security Hub publishing.  But, that is adding too much
        complexity.  So, going to look for GuardDuty right away.

        For testing, we are only looking at Critical.
        TODO - Allow the builder to determine the lowest level of security hub alert from which to invoke
        the lambda function

        Findings are described at https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindings.html#API_GetFindings_ResponseSyntax
        :return:
        """

        """
        This is for monitoring a security hub finding of a GuardDuty action. 
        detail_type = ["GuardDuty Finding"]
        """

        """
        Monitoring a GuardDuty directly
        # Severity Levels for critical are betweein 7.0 and 8.9.  But range doesn't do floats, so we are creating in two steps
        """

        severity_levels = range(40, 89, 1)
        severity_levels = list(map(lambda x: x / 10, severity_levels))
        severity_levels = [
                              4,
                              4.0,
                              4.1,
                              4.2,
                              4.3,
                              4.4,
                              4.5,
                              4.6,
                              4.7,
                              4.8,
                              4.9,
                              5,
                              5.0,
                              5.1,
                              5.2,
                              5.3,
                              5.4,
                              5.5,
                              5.6,
                              5.7,
                              5.8,
                              5.9,
                              6,
                              6.0,
                              6.1,
                              6.2,
                              6.3,
                              6.4,
                              6.5,
                              6.6,
                              6.7,
                              6.8,
                              6.9,
                              7,
                              7.0,
                              7.1,
                              7.2,
                              7.3,
                              7.4,
                              7.5,
                              7.6,
                              7.7,
                              7.8,
                              7.9,
                              8,
                              8.0,
                              8.1,
                              8.2,
                              8.3,
                              8.4,
                              8.5,
                              8.6,
                              8.7,
                              8.8,
                              8.9
                            ]
        detail_type = ["GuardDuty Finding"]
        # We could monitor just from security levels, but type might work better
        detail = {"severity": severity_levels}
        detail = {"type": ["Backdoor:EC2/C&CActivity.B!DNS"]}
        source = ["aws.guardduty"]

        self.guardduty_event = events.Rule(self, "GuardDutyTriggerRule",
                                             description="GuardDuty Trigger Rule",
                                             event_pattern=events.EventPattern(
                                               detail_type=detail_type,
                                               source=source,
                                               detail=detail
                                               ),
                                             enabled=True,
                                             )
        self.guardduty_event.add_target(events_targets.LambdaFunction(self.disk_process))
        cdk.CfnOutput(self, "InvokeLambdaArn", value=self.disk_process.function_arn, export_name="InvokeLambdaArn",
                      description="The arn of the Lambda used to invoke the workflow")
        cdk.CfnOutput(self, "InvokeLambdaName", value=self.disk_process.function_name, export_name="InvokeLambdaName",
                      description="The name of the Lambda used to invoke the workflow")