from __future__ import absolute_import, division, print_function
import logging
import inspect
import os
from iam_validator import Helper
from pathlib import Path
import json


def lineno():
    """Returns the current line number in our program."""
    return str(' - setup - line number: '+str(inspect.currentframe().f_back.f_lineno))


class Setup:
    """
    setup
    """

    def __init__(self, config_block):
        """
        Initialize setup
        :param config_block:
        """
        self.debug = None


        if config_block:
            self._config = config_block
        else:
            logging.error('config block was garbage')
            raise SystemError

        for key in self._config:
            self.__dict__[key] = self._config[key]

        self.helper = Helper(config_block)

    def setup(self):

        version = self.helper.get_version()
        if self.debug:
            print('current version: '+str(version))

        self.helper.check_package()

        if self.helper.check_if_config_directory_exists():
            print('directory exists'+lineno())
            if self.helper.check_if_config_file_exists():

                if self.debug:
                    print('config file exists'+lineno())
            else:
                if self.debug:
                    print('config file does not exists'+lineno())
                self.helper.get_user_input()
        else:
            if self.debug:
                print('config directory does not exist'+lineno())
            self.helper.create_config_directory()
            self.helper.get_user_input()

        # We should now have a ~/.iamv/config file with all the data.  However, we need
        # to check if all the variables required are in the config file
        self.helper.check_config_file()

        cwd = os.getcwd()
        if self.debug:
            print('cwd: '+str(cwd)+lineno())

        home = str(Path.home())

        parent_dir = self.helper.get_parent_directory()
        if self.debug:
            print('parent dir: '+str(parent_dir)+lineno())

        self.helper.copy_project_files(parent_dir+'/data_files')

        config_data = self.helper.get_config_data()

        # Create the backend.tf file
        if config_data['bootstrap'] == "true":
            self.helper.cleanup_old_files()

            if self.debug:
                print("Create backend.tf file with variables")
            template = "terraform {\n\tbackend \"local\" {}\n}"

            with open(home+'/.iamv/data/terraform_setup_s3_bucket/backend.tf', 'w') as myfile:
                myfile.write(template)

            if self.debug:
                print("Initialize the local Terraform backend")
                print('Running command "terraform init"')

            os.chdir(home+'/.iamv/data/terraform_setup_s3_bucket')
            lines, error_lines = self.helper.run_command('terraform init')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))

            os.chdir(cwd)

            if self.debug:
                print("Create vars.tfvars file")
            template = "bucket = \"" + str(config_data['bucket_name']) + "\"\n" + \
                       "dynamodb_table = \"" + str(config_data['dynamodb_table']) + "\"\n" + \
                       "key = \"" + str(config_data['key']) + "\"\n" + \
                       "profile = \"" + str(config_data['profile']) + "\"\n" + \
                       "region = \"" + str(config_data['region']) + "\"\n" + \
                       "bootstrap = \"true\"\n" + \
                       "operator = [\"" + str(config_data['username']) + "\"]"

            with open(home+'/.iamv/data/terraform_setup_s3_bucket/vars.tfvars','w') as myfile:
                myfile.write(template)

            if self.debug:
                print("Run terraform  apply")
            os.chdir(home+'/.iamv/data/terraform_setup_s3_bucket')
            lines, error_lines = self.helper.run_command('terraform apply -var-file=vars.tfvars -auto-approve')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))


            os.chdir(cwd)

            if self.debug:
                print('Write new backend.tf file')
            template = "terraform {\n\tbackend \"s3\" {\n\t\tbucket = \"" + str(config_data['bucket_name']) + "\"\n\t\tkey = \"" + \
                       str(config_data['key']) + "\"\n\t\tregion = \"" + str(config_data['region']) + "\"\n\t}\n}"
            with open(home+'/.iamv/data/terraform_setup_s3_bucket/backend.tf','w') as myfile:
                myfile.write(template)

            template = "terraform {\n\tbackend \"s3\" {\n\t\tbucket = \"" + str(config_data['bucket_name']) + "\"\n\t\tkey = \"terraform/terraform_setup_roles/terraform.tfstate" + \
                       "\"\n\t\tregion = \"" + str(config_data['region']) + "\"\n\t}\n}"
            with open(home+'/.iamv/data/terraform_setup_roles/backend.tf','w') as myfile:
                myfile.write(template)

            template = "terraform {\n\tbackend \"s3\" {\n\t\tbucket = \"" + str(config_data['bucket_name']) + "\"\n\t\tkey = \"terraform/terraform/terraform.tfstate" + \
                       "\"\n\t\tregion = \"" + str(config_data['region']) + "\"\n\t\tencrypt = true\n\t}\n}"
            with open(home+'/.iamv/data/terraform/backend.tf','w') as myfile:
                myfile.write(template)

            if self.debug:
                print("Update vars.tfvars file")
            template = "bucket = \""+str(config_data['bucket_name'])+"\"\n" + \
                        "dynamodb_table = \""+str(config_data['dynamodb_table'])+"\"\n"+ \
                        "key = \""+str(config_data['key'])+"\"\n"+ \
                        "profile = \""+str(config_data['profile'])+"\"\n"+ \
                        "region = \""+str(config_data['region'])+"\"\n"+ \
                       "subnet_id = \"" + str(config_data['subnet_id']) + "\"\n" + \
                       "bootstrap = \"false\"\n"
            with open(home+'/.iamv/data/terraform/vars.tfvars','w') as myfile:
                myfile.write(template)

            template = "bucket_name = \"" + str(config_data['bucket_name']) + "\"\n" + \
                       "department = \"" + str(config_data['department']) + "\"\n" + \
                       "user_name = \"" + str(config_data['username']) + "\"\n" + \
                       "aws_region = \"" + str(config_data['region']) + "\"\n" + \
                       "account_id = \""+str(config_data['account_id'])+"\"\n"

            with open(home+'/.iamv/data/terraform/vars.tfvars', 'w') as myfile:
                myfile.write(template)
            with open(home+'/.iamv/data/terraform_setup_roles/vars.tfvars', 'w') as myfile:
                myfile.write(template)

            if self.debug:
                print('Reinitializing with new backend.tf file')
            os.chdir(home+'/.iamv/data/terraform_setup_s3_bucket')

            lines, error_lines = self.helper.run_command('echo "yes" | terraform init -reconfigure')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))

            if self.debug:
                print('Terraform plan')
            lines, error_lines = self.helper.run_command('terraform plan -var-file=vars.tfvars')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))

            os.chdir(cwd)

            if self.debug:
                print('Change to terraform_setup_roles directory')
            os.chdir(home+'/.iamv/data/terraform_setup_roles')

            if self.debug:
                print("Initialize")
            lines, error_lines = self.helper.run_command('terraform init -var-file=vars.tfvars')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))


            if self.debug:
                print("Terraform apply")
            lines, error_lines = self.helper.run_command('terraform apply -var-file=vars.tfvars -auto-approve')
            print(json.dumps(lines, indent=2))
            print(json.dumps(error_lines, indent=2))

            # Check back to original directory
            os.chdir(cwd)

            print('### DONE ####')

        else:
            print('bootstrap is false'+lineno())


