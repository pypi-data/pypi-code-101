
import os
import platform
import re
import subprocess
import sys

__version__ = '0.0.3'
__appauthor__ = 'larryw3i & Contributors'

base_path = os.path.dirname(os.path.abspath(__file__))
bash_path = os.path.join(base_path, 'codium_mirror.bash')
mirrors_path = os.path.join(base_path, 'codium.mirrors')

sys_argv = sys.argv[1:]
sys_argv = ' '.join(sys_argv)


_mirror = re.findall(r'--mirror=(\S*)', sys_argv)
mirror = _mirror[0] if len(_mirror) > 0 else 'TUNA'

system = platform.system().lower()


def get_architecture():

    # default
    if system == 'linux':
        architecture = subprocess.check_output('uname -m', shell=True)\
            .decode().strip()
        return architecture in ['x86_64'] and 'amd64' or ''
    return ''


def get_mirror_url():
    mirrors = open(mirrors_path).read().split('\n')
    mirrors = [m for m in mirrors if len(m) > 0]
    for m in mirrors:
        m_splits = m.split(' ')
        if m_splits[0] == mirror:
            return m_splits[-1]
    return mirrors[0].split(' ')[-1]


mirror_url = get_mirror_url()


def get_pkgs():

    # default
    if system == 'linux':
        html = subprocess.check_output('curl ' + mirror_url, shell=True)
        links = re.findall(r'href="(\S*)"', html.decode())
        links = [l for l in links if '/' not in l]
        return links
    return []


def get_os_release():

    if system == 'linux':
        os_release = subprocess.check_output('cat /etc/os-release', shell=True)
        os_release = re.findall(r'ID_LIKE=(\S*)\n', os_release.decode())[0]
        return os_release.lower() in ['debian', 'ubuntu'] and 'deb' or ''
    return ''


def get_pkg_ur(pkg):

    # default
    return mirror_url + pkg


def get_installation_sh(os_release, pkg):
    pkg_ur = get_pkg_ur(pkg)

    # default
    if os_release in ['deb']:
        return \
            f'curl {pkg_ur} --output {pkg}; ' +\
            f'echo "sudo dpkg --install {pkg}";' +\
            f'sudo dpkg --install {pkg};' +\
            f'rm -rf {pkg}'


def run():

    architecture = get_architecture()
    os_release = get_os_release()
    pkgs = get_pkgs()

    if len(architecture) + len(pkgs) + len(os_release) < 3:
        print('codium-mirror exit.')

    for p in pkgs:
        if os_release in p and architecture in p and p.endswith(os_release):
            os.system(get_installation_sh(os_release, p))


print('\n',
      'system', '\n\t', system, '\n',
      'base_path', '\n\t', base_path, '\n',
      'bash_path', '\n\t', bash_path, '\n',
      'sys_argv', '\n\t', sys_argv, '\n',
      'get_architecture', '\n\t', get_architecture(), '\n',
      'get_mirror', '\n\t', get_mirror_url(), '\n',
      'mirror', '\n\t', mirror, '\n',
      'get_os_release', '\n\t', get_os_release(), '\n'
      )
