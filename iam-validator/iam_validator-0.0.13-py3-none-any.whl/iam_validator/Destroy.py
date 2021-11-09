from __future__ import absolute_import, division, print_function
import logging
import inspect
import os
from pathlib import Path
from iam_validator import Helper



def lineno():
    """Returns the current line number in our program."""
    return str(' - destroy - line number: '+str(inspect.currentframe().f_back.f_lineno))


class Destroy:
    """
    destroy
    """

    def __init__(self, config_block):
        """
        Initialize destroy
        :param profile_definition:
        :param rule_directory:
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

    def destroy(self):
        print('destroy')

        home = str(Path.home())

        print('Changing to terraform_setup_roles directory')
        os.chdir(home + '/.iamv/data/terraform_setup_roles')

        print("Terraform init")
        self.helper.run_command('terraform init -var-file=vars.tfvars')

        print("Terraform destroy")
        self.helper.run_command('terraform destroy -var-file=vars.tfvars -auto-approve')

        print('Changing to terraform_setup_s3_bucket directory')
        os.chdir(home + '/.iamv/data/terraform_setup_s3_bucket')

        print("Terraform init")
        self.helper.run_command('terraform init -var-file=vars.tfvars')

        print("Terraform destroy")
        self.helper.run_command('terraform destroy -var-file=vars.tfvars -auto-approve')

        print('### DONE ####')

    def remove_orphans(self):
        print('destroy')

        home = str(Path.home())

        print('Changing to terraform_setup_roles directory')
        os.chdir(home + '/.iamv/data/terraform')

        print("Terraform init")
        self.helper.run_command('terraform init -var-file=vars.tfvars')

        print("Terraform destroy")
        self.helper.run_command('terraform destroy -var-file=vars.tfvars -auto-approve')

        print('### DONE ####')