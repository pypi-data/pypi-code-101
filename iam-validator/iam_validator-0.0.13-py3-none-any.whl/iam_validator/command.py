"""
The command line interface to terraform_validator.
"""
from __future__ import absolute_import, division, print_function
import sys
import click
import inspect
import subprocess
import iam_validator
from iam_validator import Setup
from iam_validator import Destroy
from iam_validator import Validator



def lineno():
    """Returns the current line number in our program."""
    return str(' - command- line number: '+str(inspect.currentframe().f_back.f_lineno))


@click.group()
@click.version_option(version='0.6.42')
def cli():
    pass

@cli.command()
@click.option('--debug',help='Turn on debugging', required=False, is_flag=True)
def remove_orphans(
        debug
    ):
    '''
    Remove orphaned AWS resources
    :param debug:
    :return:
    '''

    print('demo')
    remove_orphans( debug)



@cli.command()
@click.option('--resources-to-test', '-r', help='Comma delimited list of resources to test', required=True)
@click.option('--pypi-update-check/--no-pypi-update-check', help='Whether to enable pypi check', default=False, required=False)
@click.option('--debug',help='Turn on debugging', required=False, is_flag=True)
def demo(
        debug,
        pypi_update_check,
        resources_to_test
    ):
    '''
    demo
    :param debug:
    :param pypi_update_check
    :return:
    '''

    print('demo')
    start_demo( debug,pypi_update_check, resources_to_test)


@cli.command()
@click.option('--resources-to-test', '-r', help='Comma delimited list of resources to test', required=True)
@click.option('--pypi-update-check/--no-pypi-update-check', help='Whether to enable pypi check', default=False, required=False)
@click.option('--debug',help='Turn on debugging', required=False, is_flag=True)
def validate(
        debug,
        pypi_update_check,
        resources_to_test
    ):
    '''
    primary function for validating a IAM role
    :param debug:
    :param pypi_update_check
    :return:
    '''

    start_validate( debug,pypi_update_check, resources_to_test)


@cli.command()
@click.option('--pypi-update-check/--no-pypi-update-check', help='Whether to enable pypi check', default=False, required=False)
@click.option('--debug',help='Turn on debugging', required=False, is_flag=True)
def setup(
        debug,
        pypi_update_check
    ):
    """
    setup s3 bucket and testing roles
    :param debug:
    :return:
    """

    if debug:
        print('calling start_setup'+lineno())

    start_setup(debug=debug, pypi_update_check=pypi_update_check)


@cli.command()
@click.option('--pypi-update-check/--no-pypi-update-check', help='Whether to enable pypi check', default=False, required=False)
@click.option('--debug',help='Turn on debugging', required=False, is_flag=True)
def destroy(
        debug,
        pypi_update_check
    ):
    """
    destroy s3 bucket and testing roles
    :param debug:
    :return:
    """
    start_destroy(debug=debug, pypi_update_check=pypi_update_check)


@click.option('--version', '-v', help='Print version and exit', required=False, is_flag=True)
def version(version):
    """
    Get version
    :param version:
    :return:
    """
    myversion()

def myversion():
    '''
    Gets the current version
    :return: current version
    '''
    print('Version: ' + str(iam_validator.__version__))

def remove_orphans(
        debug
    ):
    '''
    Remove orphaned AWS resources
    :param debug:
    :return:
    '''
    if debug:
        print('command - remove_orphans' + lineno())

    config_dict = {}
    config_dict['debug'] = debug

    destroy = Destroy(config_dict)
    if debug:
        print('print have setup')
    if destroy.remove_orphans():
        if debug:
            print('setup complete')
    else:
        if debug:
            print('setup failed')


def start_setup(
        debug,
        pypi_update_check
    ):
    '''
    Starts setup of S3 bucket and testing roles
    :param debug:
    :return:
    '''
    if debug:
        print('command - start_setup' + lineno())

    if pypi_update_check:
        check_for_updates(debug=debug)

    config_dict = {}
    config_dict['debug'] = debug

    setup1 = Setup(config_dict)
    if debug:
        print('print have setup')
    if setup1.setup():
        if debug:
            print('setup complete')
    else:
        if debug:
            print('setup failed')


def start_destroy(
        debug,
        pypi_update_check
    ):
    '''
    Starts setup of S3 bucket and testing roles
    :param debug:
    :return:
    '''
    if debug:
        print('command - start_destroy' + lineno())

    if pypi_update_check:
        check_for_updates(debug=debug)

    config_dict = {}
    config_dict['debug'] = debug

    destroy = Destroy(config_dict)
    if debug:
        print('print have destroy')
    if destroy.destroy():
        if debug:
            print('destroy complete')
    else:
        if debug:
            print('destroy failed')

def start_validate(
        debug,
        pypi_update_check,
        resources_to_test
    ):
    '''
    Starts the validation
    :param debug:
    :param pypi_update_check:
    :return:
    '''
    if debug:
        print('command - start_validate'+lineno())
        print('pypi update checK: '+str(pypi_update_check))

    if pypi_update_check:
        check_for_updates(debug=debug)


    config_dict = {}
    config_dict['debug'] = debug
    config_dict['resources_to_test'] = resources_to_test
    validator = Validator(config_dict)
    if debug:
        print('print have validator')
    if validator.validate():
        if debug:
            print('validated')
    else:
        if debug:
            print('not validated')

def start_demo(
        debug,
        pypi_update_check,
        resources_to_test
    ):
    '''
    Starts the demo
    :param debug:
    :param pypi_update_check:
    :return:
    '''
    if debug:
        print('command - start_demo'+lineno())
        print('pypi update checK: '+str(pypi_update_check))

    if pypi_update_check:
        check_for_updates(debug=debug)

    # Setup
    config_dict = {}
    config_dict['debug'] = debug
    setup1 = Setup(config_dict)
    if setup1.setup():
        if debug:
            print('setup complete')
    else:
        if debug:
            print('setup failed')


    # Validate
    config_dict = {}
    config_dict['debug'] = debug
    config_dict['resources_to_test'] = resources_to_test
    validator = Validator(config_dict)
    if validator.validate():
        if debug:
            print('validated')
    else:
        if debug:
            print('not validated')

    # Destroy
    config_dict = {}
    config_dict['debug'] = debug
    destroy = Destroy(config_dict)
    if destroy.destroy():
        if debug:
            print('destroy complete')
    else:
        if debug:
            print('destroy failed')


def get_current_pip_version(debug=False):

    try:
        command = 'pip search iam-validator | grep iamvalidator | cut -d\' \' -f 2 |  sed -e "s/^(//" -e "s/)//"'
        if debug:
            print('command: '+str(command))
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if stdout:
            current_pip_version = str(stdout).rstrip('\n').strip()
            return current_pip_version
        if stderr:
            print('Error setting up build number')
            elines = stderr.splitlines()
            for e in elines:
                print((e))

    except Exception as e:
        print('Error trying to determine the current iam-validator version')
        return 0

def check_for_updates(debug=False):
    """
    Checking for any pypi updates
    :param debug:
    :return:
    """

    if debug:
        print('check_for_updates'+lineno())
    try:

        if sys.version_info[0] < 3:
            current_pip_version = get_current_pip_version(debug=debug).decode("utf-8")
            current_local_version = str(iam_validator.__version__).rstrip('\n').strip().decode("utf-8")

        else:
            current_pip_version = get_current_pip_version(debug=debug)
            current_local_version = str(iam_validator.__version__).rstrip('\n').strip()

        if debug:
            print('current pypi version: '+str(current_pip_version))
            print('current local version: '+str(current_local_version))

        if current_pip_version == 0:
            raise Exception
        elif current_pip_version != current_local_version:
            print('#########################################################################################')
            print('There is a more current version of iam-validator. You should update ')
            print('iam-validator with pip install -U iam-validator')
            print('#########################################################################################')
            sys.exit(1)
        else:
            if debug:
                print('iam-validator is the most current version')
    except Exception as e:
        print('Error trying to determine the current iam-validator version')