# Copyright 2021 Henix, henix.fr
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""opentf-ctl"""

import csv
import logging
import os
import re
import sys

from time import sleep
from urllib.parse import urlparse

import jwt
import yaml

import requests

########################################################################

# pylint: disable=broad-except

HEADERS = {}

WATCHED_EVENTS = (
    'ExecutionCommand',
    'ExecutionResult',
    'ProviderCommand',
    'GeneratorCommand',
)

WARMUP_DELAY = 5
REFRESH_DELAY = 10


########################################################################
# Help messages

GENERAL_HELP = '''opentf-ctl controls the OpenTestFactory orchestrators.

Basic Commands:
  run workflow {filename}      Start a workflow
  get workflow {workflow_id}   Get a workflow status
  kill workflow {workflow_id}  Cancel a running workflow

Token Commands:
  generate token using {key}   Interactively generate a signed token

Advanced Commands:
  get subscriptions            List active subscriptions

Usage:
  opentf-ctl <command> [options]

Use "opentf-ctl <command> --help" for more information about a given command.
Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''

OPTIONS_HELP = '''
The following options can be passed to any command:

  --token='': Bearer token for authentication to the orchestrator
  --user='': The name of the opentfconfig user to use
  --orchestrator='': The name of the opentfconfig orchestrator to use
  --context='': The name of the opentfconfig context to use
  --insecure-skip-tls-verify=false: If true, the server's certificate will not be checked for validity.  This will make your HTTPS connections insecure
  --opentfconfig='': Path to the opentfconfig file to use for CLI requests
'''

GET_SUBSCRIPTIONS_HELP = '''List active subscriptions on the eventbus

Example:
  # List the subscriptions
  opentf-ctl get subscriptions

Usage:
  opentf-ctl get subscriptions [options]

Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''

RUN_WORKFLOW_HELP = '''Start a workflow

Examples:
  # Start the workflow defined in my_workflow.yaml
  opentf-ctl run workflow my_workflow.yaml

  # Start the workflow and wait until it completes
  opentf-ctl run workflow my_workflow.yaml --wait

  # Start the workflow and define an environment variable
  opentf-ctl run workflow my_workflow.yaml -e TARGET=example.com

  # Start a workflow and provide environment variables defined in a file
  opentf-ctl run workflow my_workflow.yaml -e variables

  # Start the wokflow and provide a local file
  opentf-ctl run workflow mywf.yaml -f key=./access_key.pem

Options:
  -e var=value: 'var' will be defined in the workflow and while running commands in execution environment.
  -e path/to/file: variables defined in file will be defined in the workflow and while running commands in execution environment.  'file' must contain one variable definition per line, of the form 'var=value'.
  -f name=path/to/file: the specified local file will be available for use by the workflow.  'name' is the file name specified in the `ressources.files` part of the workflow.
  --wait: wait for workflow completion.

Usage:
  opentf-ctl run workflow NAME [-e var=value]... [-e path/to/file] [-f name=path/to/file]... [--wait] [options]

Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''

GET_WORKFLOW_HELP = '''Get a workflow status

Examples:
  # Get the current status of a workflow
  opentf-ctl get workflow 9ea3be45-ee90-4135-b47f-e66e4f793383

  # Get the status of a workflow and wait until its completion
  opentf-ctl get workflow 9ea3be45-ee90-4135-b47f-e66e4f793383 --watch

  # Get the status of a workflow, showing first-level nested steps
  opentf-ctl get workflow 9ea3be45-ee90-4135-b47f-e66e4f793383 --step_depth=2

Options:
  --step_depth=1: show nested steps to the given depth.
  --job_depth=1: show nested jobs to the given depth.
  --watch: wait until workflow completion or cancellation, displaying status updates as they occur.

Usage:
  opentf-ctl get workflow WORKFLOW_ID [--step_depth=value] [--job_depth=value] [--watch] [options]

Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''

KILL_WORKFLOW_HELP = '''Kill a running workflow

Example:
  # Kill the specified workflow
  opentf-ctl kill workflow 9ea3be45-ee90-4135-b47f-e66e4f793383

Usage:
  opentf-ctl kill workflow WORKFLOW_ID [options]

Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''

GENERATE_TOKEN_HELP = '''Generate a signed token

Example:
  # Generate token interactively
  opentf-ctl generate token using path/to/private.pem

Usage:
  opentf-ctl generate token using NAME [options]

Use "opentf-ctl options" for a list of global command-line options (applies to all commands).
'''


########################################################################
# Helpers


def _make_hostport(service):
    """Adjust server port for service."""
    server = CONFIG['orchestrator']['server']
    if 'ports' in CONFIG['orchestrator']:
        port = str(CONFIG['orchestrator']['ports'].get(service, ''))
        if port:
            url = urlparse(server)
            new = url._replace(netloc=url.netloc.split(':')[0] + ':' + port)
            server = new.geturl()
    return server.strip('/')


def _receptionist():
    return _make_hostport('receptionist')


def _eventbus():
    return _make_hostport('eventbus')


def _observer():
    return _make_hostport('observer')


def _killswitch():
    return _make_hostport('killswitch')


########################################################################
# Configuration

CONFIG = {}


def read_configuration():
    """Read configuration file.

    Configuration file is by default ~/.opentf/config, but this can be
    overridden by specifying the OPENTF_CONFIG environment variable or
    by using the `--opentfconfig=' command line parameter.

    Configuration file is a kubeconfig-like file, in YAML:

    ```yaml
    apiVersion: opentestfactory.org/v1alpha1
    kind: CtlConfig
    current-context: default
    contexts:
    - context:
        orchestrator: default
        user: default
      name: default
    orchestrators:
    - name: default
      orchestrator:
        insecure-skip-tls-verify: true
        server: http://localhost
        ports:
          receptionist: 7774
          observer: 7775
          killswitch: 7776
          eventbus: 38368
    users:
    - name: default
      user:
        token: ey...
    ```

    Optional command-line options:

    --token=''
    --user=''
    --orchestrator=''
    --context=''
    --insecure-skip-tls-verify=false|true
    --opentfconfig=''
    """

    def _get(kind, name):
        for item in config[f'{kind}s']:
            if item['name'] == name:
                return item[kind]
        return None

    conf = (
        _get_value('--opentfconfig=')
        or os.environ.get('OPENTF_CONFIG')
        or os.path.expanduser('~/.opentf/config')
    )
    try:
        with open(conf, 'r') as cnf:
            config = yaml.safe_load(cnf)
    except Exception as err:
        logging.error('Could not read configuration file %s: %s.', conf, err)
        sys.exit(2)

    context = _get_value('--context=') or config['current-context']
    orchestrator = (
        _get_value('--orchestrator=') or _get('context', context)['orchestrator']
    )
    user = _get_value('--user=') or _get('context', context)['user']

    try:
        CONFIG['token'] = _get_value('--token=') or _get('user', user)['token']
        CONFIG['orchestrator'] = _get('orchestrator', orchestrator)
        CONFIG['orchestrator']['insecure-skip-tls-verify'] = CONFIG['orchestrator'].get(
            'insecure-skip-tls-verify', False
        ) or (_get_value('--insecure-skip-tls-verify=') == 'true')
        HEADERS['Authorization'] = 'Bearer ' + CONFIG['token']
    except Exception as err:
        logging.error('Could not read configuration: %s.', err)
        sys.exit(2)


########################################################################
# Commands


def list_subscriptions():
    """List all active subscriptions.

    Outputs information in CSV format (using ',' as a column delimiter).

    # Raised exceptions

    Abort with an error code 1 if the orchestrator replied with a non-ok
    code.

    Abort with an error code 2 if another error occurred.
    """
    try:
        what = requests.get(
            _eventbus() + '/subscriptions',
            headers=HEADERS,
            verify=not CONFIG['orchestrator']['insecure-skip-tls-verify'],
        )
        if what.status_code == 200:
            what = what.json()
        else:
            logging.error(
                'Could not get subscription list, got %d: %s.',
                what.status_code,
                what.text,
            )
            sys.exit(1)
    except Exception as err:
        logging.error('Could not get subscription list: %s.', err)
        sys.exit(2)

    writer = csv.writer(sys.stdout)
    writer.writerow(('name', 'endpoint', 'creation', 'count', 'subscription'))
    for _, manifest in what['items'].items():
        metadata = manifest['metadata']
        spec = manifest['spec']
        writer.writerow(
            (
                metadata['name'],
                spec['subscriber']['endpoint'],
                metadata['creationTimestamp'][:22],
                manifest['status']['publicationCount'],
                ':'.join(metadata['annotations'].values()),
            )
        )


def _file_not_found(name, err):
    logging.error('File not found: %s.', name)
    logging.debug('Error is: %s.', err)
    sys.exit(2)


def _read_variables_file(file, variables):
    """Read file and add variables.

    Abort with an error code 2 if the file does not exist or contains
    invalid content.
    """
    try:
        with open(file, 'r', encoding='utf-8') as varfile:
            for line in varfile:
                if '=' not in line:
                    logging.error(
                        'Invalid format in file %s, was expecting var=value.',
                        file,
                    )
                    sys.exit(2)
                var, _, value = line.strip().partition('=')
                variables[var] = value
    except FileNotFoundError as err:
        _file_not_found(file, err)


def _add_files(args, files):
    """Handling -f file command-line options."""
    process = False
    for option in args:
        if option == '-f':
            process = True
            continue
        if process:
            process = False
            name, path = option.split('=')
            try:
                files[name] = open(path, 'rb')
            except FileNotFoundError as err:
                _file_not_found(path, err)


def _add_variables(args, files):
    """Handling -e file and -e var=value command-line options."""
    variables = {}
    process = False
    for option in args:
        if option == '-e':
            process = True
            continue
        if process:
            process = False
            if '=' in option:
                var, _, value = option.partition('=')
                variables[var] = value
            else:
                _read_variables_file(option, variables)
    if variables:
        files['variables'] = '\n'.join(f'{k}={v}' for k, v in variables.items())


def run_workflow(workflow_name):
    """Run a workflow.

    # Required parameters

    - workflow_name: a file name

    # Returned value

    Returns the workflow ID if everything was OK.

    # Raised exceptions

    Abort with an error code of 1 if the workflow was not properly
    received by the orchestrator.

    Abort with an error code of 2 if a parameter was invalid (file not
    found or invalid format).
    """
    try:
        files = {'workflow': open(workflow_name, 'r', encoding='utf-8')}
        _add_files(sys.argv[4:], files)
        _add_variables(sys.argv[4:], files)

        result = requests.post(
            _receptionist() + '/workflows',
            files=files,
            headers=HEADERS,
            verify=not CONFIG['orchestrator']['insecure-skip-tls-verify'],
        )
        if result.status_code == 201:
            print('Workflow', result.json()['details']['workflow_id'], 'is running.')
        else:
            logging.error(result.json()['message'])
            sys.exit(1)
    except FileNotFoundError as err:
        _file_not_found(workflow_name, err)
    except Exception as err:
        logging.error('Could not start workflow: %s.', err)
        sys.exit(2)

    if '--wait' in sys.argv:
        sleep(WARMUP_DELAY)
        get_workflow(result.json()['details']['workflow_id'], True)


def _show_events(items, step_depth, job_depth):
    """Show watched events.

    Can be used to show partial items.
    """
    cancelation_event = None
    for event in items:
        if event['kind'] == 'Workflow':
            print('Workflow', event['metadata']['name'])
            continue
        if event['kind'] == 'WorkflowCanceled':
            cancelation_event = event
        if event['kind'] not in WATCHED_EVENTS:
            continue

        if job_depth and len(event['metadata'].get('job_origin', [])) >= job_depth:
            continue
        if step_depth and len(event['metadata'].get('step_origin', [])) >= step_depth:
            continue

        if event['kind'] == 'ExecutionResult':
            for item in event.get('logs', []):
                print(item)
            if event['status'] == 0:
                continue
            logging.warning('Status code was: %d', event['status'])
            continue

        print(
            '[%s]' % event['metadata']['creationTimestamp'][:-7],
            '[job %s] ' % event['metadata']['job_id'],
            end='',
        )
        if event['kind'] == 'ExecutionCommand':
            if event['metadata']['step_sequence_id'] == -1:
                print(
                    'Requesting execution environment providing',
                    event['runs-on'],
                    'for job',
                    event['metadata']['name'],
                )
                continue
            if event['metadata']['step_sequence_id'] == -2:
                print(
                    'Releasing execution environment for job', event['metadata']['name']
                )
                continue
            print(' ' * (len(event['metadata'].get('step_origin', []))), end='')
            print('Running', event['scripts'])
            continue

        print(' ' * (len(event['metadata'].get('step_origin', []))), end='')
        print('Running', event['metadata']['name'])
    return cancelation_event


def _get_worflow_status(workflow_id):
    try:
        response = requests.get(
            _observer() + '/workflows/' + workflow_id + '/status',
            headers=HEADERS,
            verify=not CONFIG['orchestrator']['insecure-skip-tls-verify'],
        )
    except Exception as err:
        logging.error('Could not get workflow: %s.', err)
        sys.exit(2)

    if response.status_code == 404:
        logging.error(
            'Could not find workflow %s.  The ID is incorrect or too recent or too old.',
            workflow_id,
        )
        sys.exit(1)
    if response.status_code != 200:
        logging.error(
            'Could not get workflow %s.  Got status code %d (%s).',
            workflow_id,
            response.status_code,
            response.text,
        )
        sys.exit(1)

    return response.json()


def get_workflow(workflow_id, watch=False):
    """Get a workflow.

    # Required parameters

    - workflow_id: a string

    # Optional parameters

    - watch: a boolean (False by default)

    # Returned value

    The current workflow status.

    # Raised exceptions

    Abort with an error code 1 if the workflow could not be found on the
    orchestrator.

    Abort with an error code 2 if another error occurred.
    """
    ensure_uuid(workflow_id)

    status = _get_worflow_status(workflow_id)
    current_item = 0
    job_depth = int(_get_value('--job-depth=') or 1)
    step_depth = int(_get_value('--step-depth=') or 1)

    while True:
        cancelation_event = _show_events(
            status['details']['items'][current_item:],
            job_depth=job_depth,
            step_depth=step_depth,
        )
        if not watch:
            break
        if status['details']['status'] != 'RUNNING':
            break
        current_item = len(status['details']['items'])
        while len(status['details']['items']) <= current_item:
            sleep(REFRESH_DELAY)
            status = _get_worflow_status(workflow_id)

    workflow_status = status['details']['status']
    if workflow_status == 'DONE':
        print('Workflow completed successfully.')
    elif workflow_status == 'RUNNING':
        print('Workflow is running.')
    elif workflow_status == 'FAILED':
        if (
            cancelation_event
            and cancelation_event.get('details', {}).get('status') == 'cancelled'
        ):
            print('Workflow cancelled.')
        else:
            print('Workflow failed.')
    else:
        logging.warning(
            'Unexpected workflow status: %s (was expecting DONE, RUNNING, or FAILED).',
            workflow_status,
        )


def kill_workflow(workflow_id):
    """Kill workflow.

    # Required parameter

    - workflow_id: a non-empty string (an UUID)

    # Raised exceptions

    Abort with an error code 1 if the orchestrator replied with an
    unexpected status code (!= 200).

    Abort with an error code 2 if an error occurred while contacting the
    orchestrator.
    """
    ensure_uuid(workflow_id)
    try:
        response = requests.delete(
            _killswitch() + '/workflows/' + workflow_id,
            headers=HEADERS,
            verify=not CONFIG['orchestrator']['insecure-skip-tls-verify'],
        )
    except Exception as err:
        logging.error('Could not kill workflow: %s.', err)
        sys.exit(2)
    if response.status_code == 200:
        print('Killing workflow %s.' % workflow_id)
    else:
        logging.error(
            'Could not kill workflow %s.  Got status code %d (%s).',
            workflow_id,
            response.status_code,
            response.text,
        )
        sys.exit(1)


def generate_token(privatekey):
    """Generate JWT token.

    # Required parameters

    - privatekey: a non-empty string (a file name)

    # Raised exceptions

    Abort with an error code 2 if something went wrong.
    """
    try:
        with open(privatekey, 'r') as keyfile:
            pem = keyfile.read()
    except FileNotFoundError:
        logging.error('The specified private key could not be found: %s.', privatekey)
        sys.exit(2)

    algorithm = (
        input('Please specify an algorithm (RS512 if unspecified): ').strip() or 'RS512'
    )
    print('The specified algorithm is:', algorithm)
    while not (
        issuer := input(
            'Please enter the issuer (your company or department): '
        ).strip()
    ):
        logging.warning('The issuer cannot be empty.')
    while not (
        subject := input(
            'Please enter the subject (you or the person you are making this token for): '
        )
    ):
        logging.warning('The subject cannot be empty.')

    try:
        token = jwt.encode({'iss': issuer, 'sub': subject}, pem, algorithm=algorithm)
    except NotImplementedError:
        logging.error('Algorithm not supported: %s.', algorithm)
        sys.exit(2)
    except Exception as err:
        logging.error('Could not generate token: %s.', err)
        sys.exit(2)

    print('The signed token is:')
    print(token)


########################################################################
# Helpers


def _is_command(command, args):
    """Check if args matches command.

    `_` are placeholders.

    # Examples

    ```text
    _is_command('get job _', ['', 'get', 'job', 'foo'])  -> True
    _is_command('get   job  _', ['', 'get', 'job', 'foo'])  -> True
    _is_command('GET JOB _', ['', 'get', 'job', 'foo'])  -> False
    ```

    # Required parameters

    - command: a string
    - args: a list of strings

    # Returned value

    A boolean.
    """
    if len(args) <= len(command.split()):
        return False
    for pos, item in enumerate(command.split(), start=1):
        if item not in ('_', args[pos]):
            return False
    return True


def _get_value(prefix):
    for item in sys.argv[1:]:
        if item.startswith('--') and item.replace('_', '-').startswith(prefix):
            return item[len(prefix) :]
    return None


def ensure_uuid(parameter):
    """Ensure parameter is a valid UUID.

    Abort with error code 2 if `parameter` is not a valid UUID.
    """
    if not re.match(r'^[a-f0-9-]+$', parameter):
        logging.error('Parameter %s is not a valid UUID.', parameter)
        sys.exit(2)


def print_help(args):
    """Display help."""
    if _is_command('options', args):
        print(OPTIONS_HELP)
    elif _is_command('get subscriptions', args):
        print(GET_SUBSCRIPTIONS_HELP)
    elif _is_command('run workflow', args):
        print(RUN_WORKFLOW_HELP)
    elif _is_command('get workflow', args):
        print(GET_WORKFLOW_HELP)
    elif _is_command('kill workflow', args):
        print(KILL_WORKFLOW_HELP)
    elif _is_command('generate token', args):
        print(GENERATE_TOKEN_HELP)
    elif len(args) == 2:
        print(GENERAL_HELP)
    else:
        logging.error('Unknown command.  Use --help to list known commands.')
        sys.exit(1)


########################################################################
# Main


def main():
    """Process command."""
    if len(sys.argv) == 1:
        print(GENERAL_HELP)
        sys.exit(1)
    if sys.argv[-1] == '--help':
        print_help(sys.argv)
        sys.exit(0)

    if _is_command('generate token using _', sys.argv):
        generate_token(sys.argv[4])
        sys.exit(0)

    if _is_command('get subscriptions', sys.argv):
        read_configuration()
        list_subscriptions()
    elif _is_command('run workflow _', sys.argv):
        read_configuration()
        run_workflow(sys.argv[3])
    elif _is_command('get workflow _', sys.argv):
        read_configuration()
        get_workflow(sys.argv[3], '--watch' in sys.argv)
    elif _is_command('kill workflow _', sys.argv):
        read_configuration()
        kill_workflow(sys.argv[3])
    else:
        logging.error('Unknown command.  Use --help to list known commands.')
        sys.exit(1)


if __name__ == '__main__':
    main()
