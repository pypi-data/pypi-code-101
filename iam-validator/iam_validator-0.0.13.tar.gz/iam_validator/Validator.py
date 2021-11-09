from __future__ import absolute_import, division, print_function
import logging
import inspect
import os
import boto3
from iam_validator import Helper
import json
from pathlib import Path



def lineno():
    """Returns the current line number in our program."""
    return str(' - validator - line number: '+str(inspect.currentframe().f_back.f_lineno))


class Validator:
    """
    Validator
    """

    def __init__(self, config_block):
        """
        Initialize validator
        :param config_block:
        """
        self.debug = None
        self.resources_to_test = None
        self.account_id = None


        if config_block:
            self._config = config_block
        else:
            logging.error('config block was garbage')
            raise SystemError

        for key in self._config:
            self.__dict__[key] = self._config[key]

        self.helper = Helper(config_block)


    def validate(self):
        print('validate')
        print('resources to test: '+str(self.resources_to_test)+lineno())

        self.helper.check_package()

        config_data = self.helper.get_config_data()
        home = str(Path.home())


        if 'AWS_ACCESS_KEY_ID' in os.environ:
            user_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
            user_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
        else:
            # Get the access key from the profile
            session = boto3.session.Session(profile_name=config_data['profile'])
            credentials = session.get_credentials()

            user_access_key_id = credentials.access_key
            user_secret_access_key = credentials.secret_key

            os.environ['AWS_ACCESS_KEY_ID'] = user_access_key_id
            os.environ['AWS_SECRET_ACCESS_KEY'] = user_secret_access_key
            os.environ['AWS_REGION']= config_data['region']

        # Setup the needed clients
        iam_client = boto3.client('iam')
        s3_client = boto3.client('s3')
        s3_resource = boto3.resource('s3')
        sts_client = boto3.client('sts')

        # Get the account id
        self.account_id = self.helper.set_account_id(sts_client)

        parent_dir = self.helper.get_parent_directory()
        if self.debug:
            print('parent_dir: ' + str(parent_dir)+lineno())

        current_directory = os.getcwd()
        if self.debug:
            print('current directory: ' + str(current_directory)+lineno())

        results = {
                "positive_role": {
                    "apply_errors": None,
                    "destroy_errors": None
                },
                "negative_role": {
                    "apply_errors": None,
                    "destroy_errors": None
                }
        }

        try:
            self.helper.setup_testing_roles(iam_client)

            # Assume positive testing role
            print("\n\n###################################")
            print("## Positive Testing Role")
            print("###################################\n\n")

            assumed_role = sts_client.assume_role(
                RoleArn='arn:aws:iam::' + str(config_data['account_id']) + ':role/PositiveTestingRole',
                RoleSessionName='AssumeRole'
            )

            self.helper.permissions_boundary_arn = self.helper.get_role_permissions_boundary('PositiveTestingRole',iam_client)

            os.chdir(home+'/.iamv/data/terraform')
            (lines, error_lines) = self.helper.run_command('AWS_ACCESS_KEY_ID=' + str(
                assumed_role['Credentials']['AccessKeyId']) + ' AWS_SECRET_ACCESS_KEY=' + str(
                assumed_role['Credentials']['SecretAccessKey']) + ' AWS_SESSION_TOKEN=' + str(
                assumed_role['Credentials']['SessionToken']) + ' terraform init')

            command = 'TF_VAR_resources=' + self.resources_to_test + \
                      ' AWS_ACCESS_KEY_ID=' + \
                      str(assumed_role['Credentials']['AccessKeyId']) + \
                      ' AWS_SECRET_ACCESS_KEY=' + \
                      str(assumed_role['Credentials']['SecretAccessKey']) + \
                      ' AWS_SESSION_TOKEN=' + \
                      str(assumed_role['Credentials']['SessionToken'])

            if self.helper.positive_department:
                command = 'TF_VAR_subnet_id='+str(config_data['subnet_id'])+' TF_VAR_tag_value=' + str(self.helper.positive_department) + ' ' + command

            if self.helper.permissions_boundary_arn:
                command = 'TF_VAR_permissions_boundary_arn=' + str(self.helper.permissions_boundary_arn) + ' ' + command

            # Try to apply and destroy terraform
            (lines, error_lines) = self.helper.run_command('echo \'yes\' | ' + command + ' terraform apply')
            results["positive_role"]["apply_errors"] = error_lines
            (lines, error_lines) = self.helper.run_command('echo \'yes\' | ' + command + ' terraform destroy')
            results["positive_role"]["destroy_errors"] = error_lines

            # Assume negative testing role

            print("\n\n###################################")
            print("## Negative Testing Role")
            print("###################################\n\n")

            assumed_role = sts_client.assume_role(
                RoleArn='arn:aws:iam::' + str(config_data['account_id']) + ':role/NegativeTestingRole',
                RoleSessionName='AssumeRole'
            )

            self.helper.permissions_boundary_arn = self.helper.get_role_permissions_boundary('NegativeTestingRole',
                                                                                   iam_client)

            os.chdir(home+'/.iamv/data/terraform')
            (lines, error_lines) = self.helper.run_command('AWS_ACCESS_KEY_ID=' + str(
                assumed_role['Credentials']['AccessKeyId']) + ' AWS_SECRET_ACCESS_KEY=' + str(
                assumed_role['Credentials']['SecretAccessKey']) + ' AWS_SESSION_TOKEN=' + str(
                assumed_role['Credentials']['SessionToken']) + ' terraform init')

            command = 'TF_VAR_resources=' + self.resources_to_test + \
                      ' AWS_ACCESS_KEY_ID=' + \
                      str(assumed_role['Credentials']['AccessKeyId']) + \
                      ' AWS_SECRET_ACCESS_KEY=' + \
                      str(assumed_role['Credentials']['SecretAccessKey']) + \
                      ' AWS_SESSION_TOKEN=' + \
                      str(assumed_role['Credentials']['SessionToken'])

            if self.helper.positive_department:
                command = 'TF_VAR_subnet_id='+str(config_data['subnet_id'])+' TF_VAR_tag_value=' + str(self.helper.negative_department) + ' ' + command

            if self.helper.permissions_boundary_arn:
                command = 'TF_VAR_permissions_boundary_arn=' + str(self.helper.permissions_boundary_arn) + ' ' + command

            # Try to apply and destroy terraform
            (lines, error_lines) = self.helper.run_command('echo \'yes\' | ' + command + ' terraform apply')
            results["negative_role"]["apply_errors"] = error_lines
            (lines, error_lines) = self.helper.run_command('echo \'yes\' | ' + command + ' terraform destroy')
            results["negative_role"]["destroy_errors"] = error_lines

            if self.debug:
                print('Changing back to original directory and begin teardown'+lineno())
            os.chdir(current_directory)

            os.environ["AWS_ACCESS_KEY_ID"] = user_access_key_id
            os.environ["AWS_SECRET_ACCESS_KEY"] = user_secret_access_key
            iam_client = boto3.client('iam')
            self.helper.sanitize_testing_roles(iam_client)

            print(json.dumps(results, indent=4))
        except Exception as e:
            print("Error ", e.__class__, "occurred.")

            os.environ["AWS_ACCESS_KEY_ID"] = user_access_key_id
            os.environ["AWS_SECRET_ACCESS_KEY"] = user_secret_access_key
            iam_client = boto3.client('iam')
            self.helper.sanitize_testing_roles(iam_client)
