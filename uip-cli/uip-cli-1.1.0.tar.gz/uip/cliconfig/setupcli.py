import argparse
import os
import sys

from colorama import init, deinit
from uip.cliconfig.customformatter import CustomHelpFormatter
from uip.config.configoptions import get_default_value as gdv
from uip.config.configoptions import get_env_var_name as gevn
from uip.config.configoptions import get_long_arg as gla
from uip.config.configoptions import get_short_arg as gsa
from uip.constants import constants
from uip.parsecli.parsecli import parse_cli_args
from uip.utils.formatting import wrap_text
from .. import UIP_CLI_VERSION

def add_example_epilog(cmd_arg, example_usage, title="examples"):
    """
    Adds examples section at the end of the help menu

    Parameters
    ----------
    cmd_arg : parser, subparser
        The parser or subparser to add the examples to
    example_usage : str
        The examples to add
    """
    # At this point, example_usage contains %(prog)s instead of the actual program name (which is substituted later).
    # Thus, effective_width needs to account for this as shown below.
    effective_width = 80 - (len(cmd_arg.prog) - len('%(prog)s'))
    wrapped_usage = wrap_text(example_usage, effective_width, initial_indent=2, subsequent_indent=4)
    title = wrap_text(title, effective_width, initial_indent=0, subsequent_indent=2)
    wrapped_usage = '\n%s: \n%s\n' % (title, wrapped_usage)
    cmd_arg.formatter_class = CustomHelpFormatter
    if cmd_arg.epilog:
        cmd_arg.epilog += wrapped_usage
    else:
        cmd_arg.epilog = wrapped_usage


def add_command_description(cmd_arg, description, title="description"):
    effective_width = 80
    wrapped_description = wrap_text(description, effective_width, initial_indent=2, subsequent_indent=2)
    title = wrap_text(title, effective_width, initial_indent=0, subsequent_indent=2)
    wrapped_description = '\n%s: \n%s\n' % (title, wrapped_description)
    cmd_arg.formatter_class = CustomHelpFormatter
    if cmd_arg.description:
        cmd_arg.description += wrapped_description
    else:
        cmd_arg.description = wrapped_description


def add_login_args(cmd_arg):
    """
    Adds login related arguments to cmd_arg

    Parameters
    ----------
    cmd_arg : parser, subparser
        The parser or subparser to add the login args to
    """
    login_group = cmd_arg.add_argument_group('login required arguments')

    login_group.add_argument(gsa('shared.userid'), gla('shared.userid'), metavar='<userid>',
                             type=str,
                             help='username used to log into Controller Web Services API (environment variable: %s)'
                                  % gevn('shared.userid'))
    login_group.add_argument(gsa('shared.password'), gla('shared.password'), metavar='<password>', type=str,
                             help='password used to log into Controller Web Services API (environment variable: %s)'
                                  % gevn('shared.password'))
    login_group.add_argument(gsa('shared.url'), gla('shared.url'), metavar='<url>', type=str,
                             help='url used to connect to the Controller (environment variable: %s)' % gevn(
                                 'shared.url'))


def setup_init_arg(cmd_subparsers):
    """
    Sets up the init command and it's arguments

    Parameters
    ----------
    cmd_subparsers : subparsers
        The subparser to add the init arg to
    """
    init_arg = cmd_subparsers.add_parser('init', help='initialize a new project with starter Extension templates')
    add_command_description(init_arg,
                            "The 'init' command provides starter Extension templates to start a new project")

    # Add positional arguments
    init_arg.add_argument('dir', metavar='<dir>', default=gdv('init.dir'), nargs='?', type=str,
                          help='where to initialize the Extension template (default: %(default)s)')

    # Add optional arguments
    init_arg.add_argument(gsa('init.extension_template'), gla('init.extension_template'), metavar='<name>',
                          default=gdv('init.extension_template'), type=str,
                          help='name of the Extension template to initialize in the specified directory. If no name is '
                               'specified, an empty .uip project will be created.')
    init_arg.add_argument(gsa('init.variables'), gla('init.variables'), metavar='<variables>',
                          default=gdv('init.variables'), action='append',
                          help='user defined variables used to configure templates before creating them. '
                               '(environment variable: %s)' % gevn('init.variables'))

    # Add examples
    add_example_epilog(init_arg, """
        {prog}
        {prog} {ietsa} sample-1 {itvsa} '{{"extension_name": "myext", "version": "1.0.0"}}'
        {prog} {ietsa} sample-1 {itvsa} 'extension_name=myext' {itvsa} 'version=1.0.0'
        {prog} {ietsa} sample-1 {itvsa} @vars.json
        {prog} {ietsa} sample-1 {itvsa} @vars.yml
    """.format(prog="%(prog)s", ietsa=gsa('init.extension_template'), itvsa=gsa('init.variables')))


def setup_template_list_arg(cmd_subparsers):
    """
    Sets up the init command and it's arguments

    Parameters
    ----------
    cmd_subparsers : subparsers
        The subparser to add the init arg to
    """
    template_list = cmd_subparsers.add_parser('template-list',
                                              help='list of available Extension templates')
    add_command_description(template_list, "List of available Extension templates")

    # Add positional arguments
    template_list.add_argument('extension_template_name', metavar="<extension template name>", nargs='?', type=str,
                               default=None, help='name of the Extension template to get more details of')

    # Add examples
    add_example_epilog(template_list, """
        %(prog)s
        %(prog)s sample-1
    """)


def setup_build_arg(cmd_subparsers):
    """
    Sets up the build command and it's arguments

    Parameters
    ----------
    cmd_subparsers : subparsers
        The subparser to add the build arg to
    """
    build_arg = cmd_subparsers.add_parser('build', help='used to build Extension or full package')
    add_command_description(build_arg,
                            "The 'build' command is used to build the Extension or the full package. By default, "
                            "only the Extension will be built.")

    # Add optional arguments
    build_arg.add_argument(gsa('build.all'), gla('build.all'), default=None,
                           action='store_true', help='if specified, the full package will be built '
                                                     '(environment variable: %s)' % gevn('build.all'))

    # Add examples
    add_example_epilog(build_arg, """
        {prog} 
        {prog} {basa}
    """.format(prog="%(prog)s", basa=gsa('build.all')))


def setup_upload_arg(cmd_subparsers):
    upload_arg = cmd_subparsers.add_parser('upload', help='upload Extension (or full package) to the Controller')
    add_command_description(upload_arg, "upload Extension (or full package) to the Controller. By default, only the "
                                        "Extension will be uploaded.")

    # Add optional arguments
    upload_arg.add_argument(gsa('upload.all'), gla('upload.all'), default=None,
                            action='store_true', help='if specified, the full package will be uploaded '
                                                      '(environment variable: %s)' % gevn('upload.all'))
    # Add required arguments related to login
    add_login_args(upload_arg)

    # Add examples
    add_example_epilog(upload_arg, """
        {prog}
        {prog} {uala}
    """.format(prog="%(prog)s", uala=gla('upload.all')))


def setup_push_arg(cmd_subparsers):
    push_arg = cmd_subparsers.add_parser('push', help='build and upload Extension (or full package) to the Controller')
    add_command_description(push_arg,
                            "build and upload Extension (or full package) to the Controller. By default, only the "
                            "Extension will be built and uploaded.")

    # Add optional arguments
    push_arg.add_argument(gsa('push.all'), gla('push.all'), default=None,
                          action='store_true', help='if specified, the full package will be built and uploaded '
                                                    '(environment variable: %s)' % gevn('push.all'))
    # Add required arguments related to login
    add_login_args(push_arg)

    # Add examples
    add_example_epilog(push_arg, """
        {prog}
        {prog} {pala}
    """.format(prog="%(prog)s", pala=gla('push.all')))


def setup_pull_arg(cmd_subparsers):
    pull_arg = cmd_subparsers.add_parser('pull',
                                         help='pulls the latest template.json (and template_icon.png, if present)')
    add_command_description(pull_arg, "pulls the latest template.json (and template_icon.png, if present)")

    # Add required arguments related to login
    add_login_args(pull_arg)

    # Add examples
    add_example_epilog(pull_arg, """
        {prog}
        {prog} {sula} admin {spla} admin
    """.format(prog="%(prog)s", sula=gla('shared.userid'), spla=gla('shared.password')))


def setup_download_arg(cmd_subparsers):
    download_arg = cmd_subparsers.add_parser('download', help='downloads the full Universal Template package')
    add_command_description(download_arg,
                            'downloads the full Universal Template package and saves the zip in the "dist" folder')

    # Add optional arguments
    download_arg.add_argument(gsa('download.template_name'), gla('download.template_name'), type=str,
                              metavar='<name>',
                              help='name used within the Controller to identify the Universal Template'
                                   ' (environment variable: %s)' % gevn('download.template_name'))

    # Add required arguments related to login
    add_login_args(download_arg)

    # Add examples
    add_example_epilog(download_arg, """
          {prog} {dtnsa} sample-1
          {prog} {susa} admin {spsa} admin
      """.format(prog="%(prog)s", dtnsa=gsa('download.template_name'), susa=gsa('shared.userid'),
                 spsa=gsa('shared.password')))


def setup_cli_args():
    """
    Sets up the cli arguments
    """
    # set help menu wrap limit to 82 characters which effectively results in 80 as argparse subtracts 2 internally
    os.environ['COLUMNS'] = constants.ADJUSTED_WRAP_LIMIT

    parser = argparse.ArgumentParser()

    add_example_epilog(parser, """
        %(prog)s <command>
        %(prog)s init
        %(prog)s download           
    """)

    parser.add_argument('-v', '--version', action='version', version=UIP_CLI_VERSION)

    cmd_type_subparsers = parser.add_subparsers(title="commands", dest='command_type', metavar='<command>')
    cmd_type_subparsers.required = True

    # init command setup
    setup_init_arg(cmd_type_subparsers)

    # template-list command setup
    setup_template_list_arg(cmd_type_subparsers)

    # build command setup
    setup_build_arg(cmd_type_subparsers)

    # upload command setup
    setup_upload_arg(cmd_type_subparsers)

    # push command setup
    setup_push_arg(cmd_type_subparsers)

    # pull command setup
    setup_pull_arg(cmd_type_subparsers)

    # download command setup
    setup_download_arg(cmd_type_subparsers)

    num_args = len(sys.argv)
    if num_args == 1:
        parser.print_help()
    else:
        init()
        args = parser.parse_args()
        parse_cli_args(args)
        deinit()
