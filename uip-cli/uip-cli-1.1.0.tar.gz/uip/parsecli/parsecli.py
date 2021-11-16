import argparse
import os
import sys

from colorama import Fore
from uip.cliapis import apis
from uip.config.mergeconfig import get_merged_config
from uip.exceptions import customexceptions
from uip.uipproject import uipproject
from uip.uiptemplates import template
from uip.utils import formatting, io


def pack_login_info(userid, password, url):
    """
    Packs the login information into a tuple

    Parameters
    ----------
    userid : str
        Username used to log into the Controller
    password : str
        Password used to log into the Controller
    url : str
        Url used to connect to the Controller

    Returns
    -------
    3-tuple
        Consists of userid, password, url in that order
    """
    return userid, password, url


def call_func(func, *args, **kwargs):
    if func is None:
        return

    try:
        return_dict = func(*args, **kwargs)
        if return_dict and return_dict.get('msg', ''):
            print(Fore.GREEN + return_dict.get('msg'))
    except Exception as e:
        message = formatting.format_error_style(e)
        print(Fore.RED + message)


def parse_init_command(args):
    """
    Parses the init command and performs
    actions accordingly.

    Parameters
    ----------
    args : argparse.Namespace
        The args read by argparser
    """
    mc = get_merged_config('init', args)
    msg = uipproject.initialize_uip(mc.extension_template, mc.variables, mc.dir)
    return {
        'msg': msg
    }


def parse_template_list_command(args):
    mc = get_merged_config('template_list', args)
    chosen_template_name = mc.extension_template_name

    if chosen_template_name:
        extension_templates = template.get_extension_templates([chosen_template_name])
        if len(extension_templates) == 0:
            raise customexceptions.InvalidValueError(502, chosen_template_name)
    else:
        extension_templates = template.get_all_extension_templates()
    table_data = []
    table_headers = None
    separate_each_entry = True
    for extension_template in extension_templates:
        template_name = extension_template.get('template_name')
        template_path = extension_template.get('template_path')
        template_details = template.get_extension_template_details(template_path)
        template_description = template_details['template_description']

        if chosen_template_name == template_name:
            for template_variable in template_details.get('user_defined_variables'):
                variable_name = list(template_variable.keys())[0]
                variable_default = template_variable[variable_name]['default']
                variable_description = template_variable[variable_name]['description']
                table_data.append([variable_name, variable_default, variable_description])
            table_headers = ['Variable Name', 'Default', 'Description']
            separate_each_entry = False
            break
        else:
            table_data.append([template_name, template_description])
            table_headers = ['Extension Template', 'Description'] if table_headers is None else table_headers

    formatting.print_table(table_headers, table_data, separate_each_entry=separate_each_entry)


def parse_build_command(args):
    mc = get_merged_config('build', args)
    generated_file = uipproject.generate_build(build_all=mc.all)
    filename = os.path.basename(generated_file)
    buildpath = os.path.relpath(os.path.dirname(generated_file))

    msg = formatting.format_list_for_printing([filename],
                                              header='The following files were built in "%s"' % buildpath)
    return {
        'msg': msg
    }


def parse_upload_command(args):
    mc = get_merged_config('upload', args)
    login_info = pack_login_info(mc.userid, mc.password, mc.url)

    return_dict = {}
    if mc.all:
        full_package_zip_path = uipproject.get_built_full_package_zip_path()
        return_dict = apis.import_template(template=full_package_zip_path, login_info=login_info)
    else:
        extension_zip_path = uipproject.get_built_extension_zip_path()
        template_name = uipproject.get_template_name_from_template_json()
        return_dict = apis.upload_extension(name=template_name, extension=extension_zip_path,
                                            login_info=login_info)
    return return_dict


def parse_push_command(args):
    mc = get_merged_config('push', args)
    login_info = pack_login_info(mc.userid, mc.password, mc.url)

    generated_file = uipproject.generate_build(build_all=mc.all)

    return_dict = {}
    if mc.all:
        full_package_zip_path = uipproject.get_built_full_package_zip_path()
        return_dict = apis.import_template(template=full_package_zip_path, login_info=login_info)
    else:
        extension_zip_path = uipproject.get_built_extension_zip_path()
        template_name = uipproject.get_template_name_from_template_json()
        return_dict = apis.upload_extension(name=template_name, extension=extension_zip_path,
                                            login_info=login_info)
    return return_dict


def parse_pull_command(args):
    mc = get_merged_config('pull', args)
    login_info = pack_login_info(mc.userid, mc.password, mc.url)

    pull_download_dir = uipproject.get_pull_command_save_dir()
    if pull_download_dir:
        template_name = uipproject.get_template_name_from_template_json()
        return_dict = apis.export_template(name=template_name, login_info=login_info, exclude=True,
                                           save_dir=pull_download_dir)
        if return_dict:
            template_fullpath = return_dict.get('template_fullpath', None)
            if template_fullpath:
                io.extract_zip(template_fullpath, pull_download_dir)
                io.remove_file(template_fullpath)
                changes = uipproject.move_template_json_icon(move_from=pull_download_dir)

                msg = ''

                if not changes['updated_files'] and not changes['new_files']:
                    msg += 'Local files are already up to date'
                else:
                    if changes['updated_files']:
                        msg += formatting.format_list_for_printing(changes['updated_files'],
                                                                   header='The following files were updated')
                    if changes['new_files']:
                        msg += '\n'
                        msg += formatting.format_list_for_printing(changes['new_files'],
                                                                   header='The following new files were pulled')

                return {
                    'msg': msg
                }


def parse_download_command(args):
    mc = get_merged_config('download', args)
    login_info = pack_login_info(mc.userid, mc.password, mc.url)

    temporary_save_dir = uipproject.get_temporary_save_dir()

    if mc.template_name is None:
        mc.template_name = uipproject.get_template_name_from_template_json()

    if temporary_save_dir:
        return_dict = apis.export_template(name=mc.template_name, login_info=login_info, exclude=False,
                                           save_dir=temporary_save_dir)
        if return_dict:
            template_fullpath = return_dict.get('template_fullpath', None)
            changes = uipproject.move_full_package(full_package_path=template_fullpath)
            msg = ''

            if not changes['updated_file'] and not changes['new_file']:
                msg += '"%s" is already up to date' % changes['unchanged_file']
            elif changes['updated_file']:
                msg += formatting.format_list_for_printing([changes['updated_file']],
                                                           header='The following files were updated')
            elif changes['new_file']:
                msg += formatting.format_list_for_printing([changes['new_file']],
                                                           header='The following new files were downloaded')

            return {
                'msg': msg
            }


def parse_cli_args(args):
    """
    Parses the cli arguments based on the command_type
    argument which is guaranteed to be one of 'extension'
    or 'template', and calls the appropriate function with
    the name 'parse_%s_command' where %s is one of 'extension'
    or 'template'

    Note that this restricts all command_type related arguments
    to be of the form 'parse_%s_commmand'

    Parameters
    ----------
    args : argparse.Namespace
        The args read by argparser
    """
    command = args.command_type
    function_name = 'parse_%s_command' % command
    function_name = function_name.replace('-', '_')
    func = getattr(sys.modules[__name__], function_name, None)
    call_func(func, args)
