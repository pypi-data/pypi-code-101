
import os
import platform
import re
import subprocess
import sys

__version__ = '0.0.4'
__appauthor__ = 'larryw3i & Contributors'



base_path = os.path.dirname(os.path.abspath(__file__))
mirrors_path = os.path.join(base_path, 'codium.mirrors')

sys_argv = ' '.join(sys.argv[1:])


mirror = (re.findall(r'--mirror=(\S*)', sys_argv))[0] \
    if ' --mirror=' in sys_argv else 'BFSU'

debug = ' -d ' in sys_argv or sys_argv.endswith(' -d') or sys_argv == '-d'

system = platform.system().lower()


_os_release = subprocess.check_output('cat /etc/os-release', shell=True)
os_release = re.findall(r'ID_LIKE=(\S*)\n', _os_release.decode())[0]

is_debian = os_release.lower() in ['debian', 'ubuntu']

try:
    subprocess.check_output('which curl', shell=True)
except:
    print('curl is not installed.')
    if is_debian:
        print('install curl: sudo apt-get install curl')
    exit()


def get_mirror_url():
    _mirrors = open(mirrors_path).read().split('\n')
    mirrors = [m for m in _mirrors if len(m) > 0]
    for m in mirrors:
        m_splits = m.split(' ')
        if m_splits[0] == mirror:
            return m_splits[-1]
    return mirrors[0].split(' ')[-1]


mirror_url = get_mirror_url()


def get_architecture():

    # default
    if system == 'linux':
        architecture = subprocess.check_output('uname -m', shell=True)\
            .decode().strip()
        return architecture in ['x86_64', 'amd64'] and 'amd64' or ''
    return 'amd64'


def get_pkgs():

    # default
    if system == 'linux':
        html = subprocess.check_output('curl ' + mirror_url, shell=True)
        _links = re.findall(r'href="(\S*)"', html.decode())
        links = [l for l in _links if '/' not in l]
        return links
    return []


def get_pkg_ext():

    if system == 'linux':
        return is_debian and 'deb' or ''
    return ''


def get_pkg_ur(pkg):

    # default
    return mirror_url + pkg


def get_installation_sh(pkg_ext, pkg):

    pkg_ur = get_pkg_ur(pkg)
    print('pkg_ur', '\n\t', pkg_ur, '\n')

    # default
    if pkg_ext in ['deb']:
        return \
            f'curl {pkg_ur} --output {pkg}; ' +\
            f'printf "\nsudo dpkg --install {pkg}\n\n";' +\
            f'sudo dpkg --install {pkg};' +\
            f'rm -rf {pkg}'


def run():

    architecture = get_architecture()
    pkg_ext = get_pkg_ext()
    pkgs = get_pkgs()

    if len(architecture) + len(pkgs) + len(pkg_ext) < 3:
        print('codium-mirror exit.')
        exit()

    print(
        '\n',
        'debug', '\n\t', debug, '\n',
        'system', '\n\t', system, '\n',
        'base_path', '\n\t', base_path, '\n',
        'sys_argv', '\n\t', sys_argv, '\n',
        'architecture', '\n\t', architecture, '\n',
        'mirror_url', '\n\t', mirror_url, '\n',
        'mirror', '\n\t', mirror, '\n',
        'pkg_ext', '\n\t', pkg_ext, '\n'
    )

    for p in pkgs:
        if architecture in p and p.endswith(pkg_ext):
            installation_sh = get_installation_sh(pkg_ext, p)

            if debug:
                print(installation_sh)
            else:
                os.system(installation_sh)
