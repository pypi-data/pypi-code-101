from gladier import GladierBaseTool


def tar(**data):
    import os
    import tarfile
    import pathlib

    tar_input = pathlib.Path(data['tar_input']).expanduser()
    tar_output = data.get('tar_output', f'{tar_input}.tgz')

    # Move to the parent directory before archiving. This ensures the
    # archive does not contain unnecessary path hierarchy.
    os.chdir(tar_input.parent)
    with tarfile.open(tar_output, 'w:gz') as tf:
        tf.add(tar_input.name)

    return tar_output


class Tar(GladierBaseTool):
    """
    The Tar tool makes it possible to create Tar archives from folders.

    :param tar_input: Input directory to archive.
    :param tar_output: (optional) output file to save the new archive. Defaults to the original
                       input file with an extension (myfile.tgz) if not given.
    :param funcx_endpoint_compute: By default, uses the ``compute`` funcx endpoint.
    :returns path: The name of the newly created archive.
    """

    # Custom flow definition to set 'ExceptionOnActionFailure' to True. We don't
    # want a transfer to start if tarring fails
    flow_definition = {
        'Comment': 'Flow with states: Tar a given folder',
        'StartAt': 'Tar',
        'States': {
            'Tar': {
                'ActionUrl': 'https://automate.funcx.org',
                'ActionScope': 'https://auth.globus.org/scopes/'
                               'b3db7e59-a6f1-4947-95c2-59d6b7a70f8c/action_all',
                'Comment': None,
                'ExceptionOnActionFailure': True,
                'Parameters': {
                    'tasks': [
                        {
                            'endpoint.$': '$.input.funcx_endpoint_compute',
                            'function.$': '$.input.tar_funcx_id',
                            'payload.$': '$.input'
                        }
                    ]
                },
                'ResultPath': '$.Tar',
                'Type': 'Action',
                'WaitTime': 300,
                'End': True,
            },
        }
    }

    funcx_functions = [tar]
    required_input = [
        'tar_input',
        'funcx_endpoint_compute',
    ]
