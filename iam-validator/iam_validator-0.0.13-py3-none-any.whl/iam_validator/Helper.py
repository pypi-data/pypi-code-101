import logging
import iam_validator
from pathlib import Path
import subprocess
import sys
import os
import json
import inspect
import shutil
import urllib.request as urllib2
import re
import botocore
import time




def lineno():
    """Returns the current line number in our program."""
    return str(' - helper - line number: '+str(inspect.currentframe().f_back.f_lineno))


class Helper:
    """
    destroy
    """

    def __init__(self, config_block):
        """
        Initialize helper
        :param profile_definition:
        :param rule_directory:
        """

        self.debug = None
        self.permissions_boundary_arn = None
        self.positive_department = None
        self.negative_department = None

        if config_block:
            self._config = config_block
        else:
            logging.error('config block was garbage')
            raise SystemError

        for key in self._config:
            self.__dict__[key] = self._config[key]

    def get_version(self):
        """
        Get the installed version
        :return:
        """
        if self.debug:
            print('get_version'+lineno())

        return iam_validator.__version__


    def get_latest_version_from_list(self, data):

        major_versions = []
        minor_versions = []
        patch_versions = []

        version_data = {}
        for d in data:
            (major, minor, patch) = d.split('.')

            version_data[d] = {}
            version_data[d]['major'] = int(major)
            version_data[d]['minor'] = int(minor)
            version_data[d]['patch'] = int(patch)

            major_versions.append(int(major))

        major_versions = list(dict.fromkeys(major_versions))
        target_major_version = max(major_versions)

        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                minor_versions.append(version_data[d]['minor'])

        minor_versions = list(dict.fromkeys(minor_versions))
        target_minor_version = max(minor_versions)


        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                if version_data[d]['minor'] == target_minor_version:
                    patch_versions.append(version_data[d]['patch'])

        patch_versions = list(dict.fromkeys(patch_versions))

        target_patch_version = max(patch_versions)

        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                if version_data[d]['minor'] == target_minor_version:
                    if version_data[d]['patch'] == target_patch_version:
                        latest_version = d

        if self.debug:
            print('latest version: ' + str(latest_version)+lineno())

        return latest_version

    def check_package(self):
        """
        Check if the installed package is the most current version
        :return:
        """
        if self.debug:
            print("Checking for current version of pdl"+lineno())

        version = self.get_version()

        if self.debug:
            print('Current version: '+str(version)+lineno())

        url = "https://pypi.org/pypi/%s/json" % ('iam-validator',)
        data = json.load(urllib2.urlopen(urllib2.Request(url)))
        versions = list(data["releases"].keys())

        if self.debug:
            print(str(versions)+lineno())

        latest_version = self.get_latest_version_from_list(versions)

        if self.debug:
            print('latest version: '+str(latest_version)+lineno())

        if latest_version != version.strip():
            if self.debug:
                print('Need to install new version of iam-validator'+lineno())
                print('Latest version: '+str(latest_version)+lineno())
                print('Current version: '+str(version)+lineno())
            self.upgrade_pdl()
            print('###############################################################')
            print('###############################################################')
            print('### Just updated to the most current version - please restart')
            print('###############################################################')
            print('###############################################################')
            sys.exit(1)
        else:
            if self.debug:
                print('Version is up-to-date'+lineno())


    def upgrade_pdl(self):
        """
        Upgrade pdl to most current version
        :return:
        """

        if self.debug:
            print('upgrading iam-validator'+lineno())

        wd = os.getcwd()
        home = str(Path.home())
        os.chdir(home)
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'install', 'iam-validator','--upgrade'])
        os.chdir(wd)

        if self.debug:
            print(str(reqs.decode("utf-8"))+lineno())


    def check_if_config_directory_exists(self):
        """
        Check if config directory exists in home directory
        :return:
        """
        # Windows WindowsPath('C:/Users/XXX')

        if self.debug:
            print('check if config directory exists'+lineno())

        try:
            home = str(Path.home())
            if os.path.exists(str(home) + '/.iamv'):
                if self.debug:
                    print('path exists' + lineno())
                if os.path.isdir(str(home) + '/.iamv'):
                    if self.debug:
                        print('Found config directory')
                    if os.path.exists(str(home) + '/.iamv/data'):
                        if self.debug:
                            print('path exists' + lineno())
                        if os.path.isdir(str(home) + '/.iamv/data'):
                            if self.debug:
                                print('Found data directory')
                            return True

            return False
        except:
            return False

    def check_if_config_file_exists(self):
        """
        Check if config file exists
        :return:
        """
        # Windows WindowsPath('C:/Users/XXX')

        if self.debug:
            print('check if config file exists'+lineno())

        try:
            home = str(Path.home())
            if Path(home+'/.iamv/config').is_file():
                if self.debug:
                    print('Found config file')
                return True
            return False
        except:
            return False

    def yes_or_no(self, question):
        """
        Prompt user for yes/no questions
        :param question:
        :return:
        """

        answer = input(question + "(y/n): ").lower().strip()
        print("")
        while not (answer == "y" or answer == "yes" or \
                   answer == "n" or answer == "no"):
            print("Input yes or no")
            answer = input(question + "(y/n):").lower().strip()
            print("")
        if answer[0] == "y":
            return True
        else:
            return False

    def print_menu(self):  ## Your menu design here
        """
        Print user menu
        :return:
        """
        print(30 * "-", "MENU", 30 * "-")
        print("1. Setup AWS Account ID (example: 123456789012)")
        print("2. Setup AWS username (example: my_username)")
        print("3. Setup AWS region (example: us-east-1)")
        print("4. Setup AWS S3 bucket name for terraform state files (Must be unique)")
        print("5. Set AWS profile (example: default)")
        print("6. Department name. (example: infrastructure)")
        print("7. Subnet id for canary resources.")
        print("8. Exit")
        print(67 * "-")

    def check_config_file(self):

        config_data = self.get_config_data()

        loop = True
        account_id = None
        username = None
        region = None
        bucket_name = None
        profile = None
        department = None
        subnet_id = None

        missing_parameters = []
        for item in config_data:
            if item == 'account_id':
                account_id = config_data[item]
            elif item == 'username':
                username = config_data[item]
            elif item == 'region':
                region = config_data[item]
            elif item == 'bucket_name':
                bucket_name = config_data[item]
            elif item == "profile":
                profile = config_data[item]
            elif item == "department":
                department = config_data[item]
            elif item == 'subnet_id':
                subnet_id = config_data[item]

        if  not account_id:
            missing_parameters.append('account_id')
        if not username:
            missing_parameters.append('username')
        if not region:
            missing_parameters.append('region')
        if not bucket_name:
            missing_parameters.append('bucket_name')
        if not profile:
            missing_parameters.append('profile')
        if not department:
            missing_parameters.append('department')
        if not subnet_id:
            missing_parameters.append('subnet_id')


        if len(missing_parameters)>0:
            print("############################################")
            print("# Need to enter information for: "+str(missing_parameters))
            print("############################################\n")

            while loop:
                self.print_menu()
                choice = input("Enter your choice [1-8]: ")

                if choice == "1":
                    account_id = input("Enter AWS Account ID (example: 123456789012): ")

                elif choice == "2":
                    username = input("Enter AWS username (example: my_username): ")

                elif choice == "3":
                    region = input("Enter AWS region (example: us-east-1): ")

                elif choice == "4":
                    bucket_name = input("Enter AWS S3 bucket name for terraform state files (Must be unique): ")

                elif choice == "5":
                    profile = input("Enter AWS profile name(example: default): ")

                elif choice == "6":
                    department = input("Enter department name. (example: infrastructure): ")

                elif choice == "7":
                    subnet_id = input("Enter subnet id for canary resources: ")

                elif choice == "8":

                    if not account_id:
                        print("Must enter account id")
                    elif not username:
                        print("Must enter username")
                    elif not region:
                        print("Must enter region")
                    elif not bucket_name:
                        print("Must enter bucket name")
                    elif not profile:
                        print("Must enter profile")
                    elif not department:
                        print("Must enter department")
                    elif not subnet_id:
                        print("Must enter subnet_id")
                    else:
                        print("Bye")
                        ## You can add your code or functions here
                        loop = False  # This will make the while loop to end as not value of loop is set to False
                else:
                    # Any integer inputs other than values 1-5 we print an error message
                    input("Wrong option selection. Enter any key to try again..")

                self.create_config_file(subnet_id=subnet_id, department=department, profile=profile,
                                        account_id=account_id, username=username, region=region,
                                        bucket_name=bucket_name)

    def get_user_input(self):
        """
        Get user input for config file
        :return:
        """

        loop = True
        account_id = None
        username = None
        region = None
        bucket_name = None
        profile = None
        department = None
        subnet_id = None

        while loop:
            self.print_menu()
            choice = input("Enter your choice [1-8]: ")

            if choice == "1":
                account_id = input("Enter AWS Account ID (example: 123456789012): ")

            elif choice == "2":
                username = input("Enter AWS username (example: my_username): ")

            elif choice == "3":
                region = input("Enter AWS region (example: us-east-1): ")

            elif choice == "4":
                bucket_name = input("Enter AWS S3 bucket name for terraform state files (Must be unique): ")

            elif choice == "5":
                profile = input("Enter AWS profile name(example: default): ")

            elif choice == "6":
                department = input("Enter department name. (example: infrastructure): ")

            elif choice == "7":
                subnet_id = input("Enter subnet id for canary resources: ")

            elif choice == "8":

                if not account_id:
                    print("Must enter account id")
                elif not username:
                    print("Must enter username")
                elif not region:
                    print("Must enter region")
                elif not bucket_name:
                    print("Must enter bucket name")
                elif not profile:
                    print("Must enter profile")
                elif not department:
                    print("Must enter department")
                elif not subnet_id:
                    print("Must enter subnet_id")
                else:
                    print("Bye")
                    ## You can add your code or functions here
                    loop = False  # This will make the while loop to end as not value of loop is set to False
            else:
                # Any integer inputs other than values 1-5 we print an error message
                input("Wrong option selection. Enter any key to try again..")

            self.create_config_file(subnet_id=subnet_id, department=department, profile=profile, account_id=account_id, username=username, region=region, bucket_name=bucket_name)

    def create_config_file(self,
                           account_id,
                           username,
                           region,
                           bucket_name,
                           profile,
                           department,
                           subnet_id
                           ):
        """
        Create the config file
        :return:
        """
        home = str(Path.home())
        f = open(str(home)+"/.iamv/config", "w")
        f.write("[data]\n")
        f.write("account_id="+str(account_id)+"\n")
        f.write("username="+str(username)+"\n")
        f.write("region="+str(region)+"\n")
        f.write("bucket_name="+str(bucket_name)+"\n")
        f.write("bootstrap=true"+"\n")
        f.write("profile="+str(profile)+"\n")
        f.write("dynamodb_table=TerraformStateLock"+"\n")
        f.write("key=terraform/setup_s3_tfstate/terraform.tfstate\n")
        f.write("department="+str(department)+"\n")
        f.write("subnet_id="+str(subnet_id))

        f.close()

    def get_parent_directory(self):
        """
        Get parent directory
        :return:
        """
        two_up = os.path.abspath(os.path.join(__file__, "../.."))

        return two_up

    def copy_project_files(self, data_file_path):
        """
        copy project files
        :param data_file_path:
        :return:
        """

        if self.debug:
            print('data_file_path: '+str(data_file_path)+lineno())
        # Copy the content of
        # source to destination

        home = str(Path.home())

        if os.path.exists(home+'/.iamv/data'):
            shutil.rmtree(home+'/.iamv/data')
        shutil.copytree(data_file_path, home+'/.iamv/data')

    def get_config_data(self):
        """
        Get data from config file
        :return:
        """
        if self.debug:
            print('get config data'+lineno())

        home = str(Path.home())

        if sys.platform == 'win32':
            file = open(home+'/.iamv/config','r', encoding='utf-16le')
            content = file.readlines()
        else:
            file = open(home+'/.iamv/config')
            content = file.readlines()

        data = {}
        for line in content:
            if self.debug:
                print('line: '+str(line)+lineno())

            if '=' in line:
                (key_name, key_value) = line.split('=')
                if self.debug:
                    print('name: '+str(key_name)+lineno())
                    print('value: '+str(key_value)+lineno())

                data[key_name.strip()] = key_value.strip()

        return data


    def create_config_directory(self):
        """
        Create the configuration directory
        :return:
        """
        if self.debug:
            print('create_config_directory'+lineno())

        home = str(Path.home())

        if os.path.exists(str(home)+'/.iamv'):
            if self.debug:
                print('path exists'+lineno())
            if os.path.isdir(str(home)+'/.iamv'):
                if self.debug:
                    print('is a directory'+lineno())
                # Check if data directory exists
                if os.path.exists(str(home) + '/.iamv/data'):
                    if self.debug:
                        print('path exists' + lineno())
                    if os.path.isdir(str(home) + '/.iamv/data'):
                        if self.debug:
                            print('is a directory' + lineno())
                    else:
                        if self.debug:
                            print('is not a directory - please delete file' + lineno())
                else:
                    os.mkdir(str(home) + '/.iamv/data')
            else:
                if self.debug:
                    print('is not a directory - please delete file'+lineno())
        else:
            if self.debug:
                print('path does not exists'+lineno())
            os.mkdir(str(home)+'/.iamv')
            os.mkdir(str(home)+'/.iamv/data')


    def run_command(self, command, timeout=600, encoding='UTF-8'):
        """
        Run command in subprocess
        :param command:
        :return:
        """

        try:

            print('subprocess_cmd')
            print('command: ' + str(self.obfuscate_string(command)))

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            proc_stdout, proc_stderr = process.communicate(timeout=timeout)

            lines = []

            for line in proc_stdout.decode().split("\n"):
                if self.debug:
                    print(self.obfuscate_string(line))
                if len(line) > 0:
                    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?\*[ -/]*[@-~])')
                    result = ansi_escape.sub('', line)
                    result = result.replace(u"\u2502","")
                    result = result.replace(u"\u2577","")
                    result = result.replace(u"\u2500","")
                    result = result.replace(u"\u2575", "")
                    lines.append(result)

            error_lines = []
            for line in proc_stderr.decode().split("\n"):
                if self.debug:
                    print(self.obfuscate_string(line))
                if len(line) > 0:
                    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?\*[ -/]*[@-~])')
                    result = ansi_escape.sub('', line)
                    result = result.replace(u"\u2502","")
                    result = result.replace(u"\u2577","")
                    result = result.replace(u"\u2500","")
                    result = result.replace(u"\u2575","")
                    error_lines.append(result)

            if self.debug:
                print(str(lines))
                print(str(error_lines))

            return [lines, error_lines]

        except subprocess.TimeoutExpired:
            process.kill()
            outs, errs = process.communicate()
            sys.exit(1)

        except:
            error = sys.exc_info()
            print(str(error))

    def cleanup_old_files(self):
        """
        Cleanup old terraform files in directory
        :return:
        """

        home = str(Path.home())

        paths_to_clean = [home+'/.iamv/data/terraform', home+'/.iamv/data/terraform_setup_roles',
                          home+'/.iamv/data/terraform_setup_s3_bucket']
        for mypath in paths_to_clean:
            for files in os.listdir(mypath):
                files_to_remove = ['.terraform.lock.hcl', 'terraform.tfstate.backup', 'terraform.tfstate', '.terraform']

                if files in files_to_remove:
                    if os.path.exists(mypath + '/' + files):
                        if self.debug:
                            print('path exists'+lineno())
                        if os.path.isfile(mypath + '/' + files):
                            if self.debug:
                                print('is file'+lineno())
                            os.remove(os.path.join(str(mypath), files))
                        else:
                            if self.debug:
                                print('is directory'+lineno())
                            shutil.rmtree(os.path.join(str(mypath), files))

    def sanitize_testing_roles(self, client):
        """
        Sanitize the positive and negative testing roles
        :return:
        """

        try:
            print('sanitize_testing_role'+lineno())
            tags = self.get_role_tags('DeveloperTestingRole', client)

            policies = self.get_policies_for_role('DeveloperTestingRole', client)

            for policy in policies['DeveloperTestingRole']:
                self.detach_policy_from_role('NegativeTestingRole', policy['PolicyArn'], client)

            for policy in policies['DeveloperTestingRole']:
                self.detach_policy_from_role('PositiveTestingRole', policy['PolicyArn'], client)

            tag_keys = []
            for item in tags:
                tag_keys.append(item['Key'])

            self.untag_role('PositiveTestingRole', tag_keys, client)
            self.untag_role('NegativeTestingRole', tag_keys, client)

            self.delete_role_permissions_boundary('PositiveTestingRole', client)
            self.delete_role_permissions_boundary('NegativeTestingRole', client)

        except:
            error = sys.exc_info()
            print(str(error)+lineno())

    def set_account_id(self, client):
        """
        Set the AWS account id
        :param client:
        :return:
        """
        try:
            return client.get_caller_identity()["Account"]

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

    def get_role_tags(self, name, client):
        """
        Get role tags
        :param name:
        :param client:
        :return:
        """

        try:

            print('get_role_tags for '+str(name)+lineno())
            tags = []

            response = client.list_role_tags(
                RoleName=name
            )

            print(json.dumps(response,indent=2))

            if 'Tags' in response:
                for tag in response['Tags']:
                    print('tag: '+str(tag)+lineno())
                    if tag['Key'] not in ['name','NAME','Name']:
                        tags.append(tag)

                return tags
            return tags

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())
            return []


    def untag_role(self, name, tags, client):
        """
        Untag role
        :param name:
        :param client:
        :return:
        """

        try:
            print('untag_role'+lineno())
            response = client.untag_role(
                RoleName = name,
                TagKeys = tags
            )

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())


    def tag_role(self, name, tags, client):
        """
        Tag role
        :param name:
        :param tags:
        :param client:
        :return:
        """

        try:

            response = client.tag_role(
                RoleName=name,
                Tags = tags
            )

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

    def get_policies_for_role(self, name, client):
        """
        Get polices for role
        :param name:
        :param client:
        :return:
        """

        try:
            print('get_polices_for_role'+lineno())

            policies = {}

            policy_paginator = client.get_paginator('list_attached_role_policies')

            role_policies = []

            for response in policy_paginator.paginate(RoleName=name):
                if 'Error' in response:
                    print(str(response)+lineno())

                role_policies.extend(response.get('AttachedPolicies'))

                policies.update({name: role_policies})
            return policies
        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

    def attach_role_policy(self, name, arn, client):
        """
        Attach policy to role
        :param name:
        :param arn:
        :param client:
        :return:
        """

        try:

            print('attach_role_policy '+str(name)+' arn: '+str(arn)+lineno())
            response = client.attach_role_policy(
                RoleName=name,
                PolicyArn=arn
            )

            time.sleep(5)

            if 'ResponseMetaData' in response and response['ResponseMetaData']['HTTPStatusCode'] == 200:
                return True

            return False

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())
            return False

    def detach_policy_from_role(self, name, arn, client):
        """
        Detach policy from role
        :param name:
        :param arn:
        :param client:
        :return:
        """

        try:
            print('detach_policy_from_role'+lineno())
            response = client.detach_role_policy(
                RoleName = name,
                PolicyArn = arn
            )

            return True
        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())
            return False

    def put_permissions_boundary_on_role(self, name, arn, client):
        """
        Put permissions boundary on role
        :param name:
        :param arn:
        :param client:
        :return:
        """
        try:

            print('put_permissions_boundary_on_role'+lineno())
            print('name: '+str(name)+lineno())
            print('arn: '+str(arn)+lineno())
            response = client.put_role_permissions_boundary(
                RoleName=name,
                PermissionsBoundary=arn
            )

            # Wait for permissions boundary to get applied
            time.sleep(15)

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

    def delete_role_permissions_boundary(self, name, client):
        """
        Delete role permissions boundary
        :param name:
        :param client:
        :return:
        """
        try:
            response = client.delete_role_permissions_boundary(
                RoleName=name
            )

            return True

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

            return False

    def copy_policies_to_role(self, original_role_name, new_role_name, policies, client):
        """
        Copy polices to role
        :param name:
        :param policies:
        :param client:
        :return:
        """

        try:

            print('copy_policies_to_role'+lineno())
            for policy in polices[original_role_name]:

                if 'PolicyArn' in policy:
                    print('FIXME'+lineno())

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())

    def setup_testing_roles(self, client, role_name='DeveloperTestingRole'):
        """
        Setup the postive and negative testing roles
        :return:
        """

        try:

            policies = self.get_policies_for_role(role_name, client)

            if self.debug:
                print(str(policies))

            for policy in policies[role_name]:
                self.attach_role_policy('NegativeTestingRole', policy['PolicyArn'], client)

            for policy in policies[role_name]:
                self.attach_role_policy('PositiveTestingRole', policy['PolicyArn'], client)

            self.permissions_boundary_arn = self.get_role_permissions_boundary('DeveloperTestingRole', client)

            if self.debug:
                print('permissions_boundary_arn: '+str(self.permissions_boundary_arn)+lineno())

            if self.permissions_boundary_arn:
                self.put_permissions_boundary_on_role('PositiveTestingRole', self.permissions_boundary_arn, client)
                self.put_permissions_boundary_on_role('NegativeTestingRole', self.permissions_boundary_arn, client)

            # Get the tags from the developer testing role and copy to positive and negative testing role
            tags = self.get_role_tags(role_name, client)
            if self.debug:
                print(str(tags))

            for item in tags:
                if item['Key'] == 'Department':
                    self.positive_department = item['Value']
                    self.negative_department = self.reverse_string(item['Value'])

            self.tag_role('PositiveTestingRole', tags, client)

            negative_tags = []

            for item in tags:
                tmp = {}
                tmp['Key'] = item['Key']
                tmp['Value'] = self.reverse_string(item['Value'])

                negative_tags.append(tmp)

            if self.debug:
                print(tags)
                print(negative_tags)

            self.tag_role('NegativeTestingRole', negative_tags, client)

        except:
            error = sys.exc_info()
            print(str(error))

    def reverse_string(self, text):
        """
        Reverse string
        :param text:
        :return:
        """

        return text[::-1]


    def get_role_permissions_boundary(self, name, client):
        """
        Get permissions boundary for role
        :param name:
        :param client:
        :return:
        """

        try:

            print('get_role_permissions_boundary'+lineno())
            response = client.get_role(
                RoleName=name
            )

            if self.debug:
                print(str(response)+lineno())

            if 'Role' in response:
                if 'PermissionsBoundary' in response['Role']:
                    return response['Role']['PermissionsBoundary']['PermissionsBoundaryArn']
            return None

        except botocore.exceptions.ClientError as error:
            print('### Exception'+lineno())
            print(str(error)+lineno())
            return None

    def obfuscate_string(self, string):

        new_string = re.sub(r'AWS_ACCESS_KEY_ID=[^\s]+', 'AWS_ACCESS_KEY_ID=xxx', string)
        new_string = re.sub(r'AWS_SECRET_ACCESS_KEY=[^\s]+', 'AWS_SECRET_ACCESS_KEY=xxx', new_string)
        new_string = re.sub(r'AWS_SESSION_TOKEN=[^\s]+', 'AWS_SESSION_TOKEN=xxx', new_string)
        new_string = re.sub(r'::[0-9]+:','::123456789012:', new_string)

        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?\*[ -/]*[@-~])')
        result = ansi_escape.sub('', new_string)

        return result