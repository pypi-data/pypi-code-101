import os
import sys
from subprocess import check_call, CalledProcessError


def checkinstallation():
    from . import checkInstallationIP


def recuparchives():
    from . import recupArchives


def importdata():
    from . import import_data


def exportdata():
    from . import export_data


def rename():
    from . import change_name


def removeldap():
    from . import remove_ldap


def push_doc():
    from . import pushdoc


def ip_clean():
    from . import ipclean


def ldap_search():
    from . import ldapsearch


def countfiles():
    from . import count_files


def reset_admin():
    from . import reset_admin_password


def dopatch():
    from . import patch


def properties_merger():
    args = sys.argv[1:]
    args.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/shell/properties-merger/properties-merger.sh")
    try:
        check_call(args)
    except CalledProcessError:
        pass
