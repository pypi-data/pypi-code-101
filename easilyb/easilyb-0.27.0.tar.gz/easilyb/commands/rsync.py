#!/usr/bin/python3
import os
import argparse
DEFAULT_EXCLUDES = ['.git', '.idea']

class Rsync:
    def __init__(self, local_path, remote_host, remote_path, profiles_options=None, default_excludes=None,
                 ):
        self.local_path = local_path
        self.remote_host = remote_host
        self.remote_path = remote_path
        self.profiles_options = dict()
        default_excludes = default_excludes or DEFAULT_EXCLUDES
        self.add_profile('direct', excludes=default_excludes)
        self.add_profile('reverse', excludes=default_excludes, reverse=True)
        if profiles_options is not None:
            self.profiles_options.update(profiles_options)

    def add_profile(self, profile_name, flags="-avP", delete=False, parent=None, excludes=None, reverse=False,
                    remote_commands=None, local_commands=None, git_filter=True):
        self.profiles_options[profile_name] = {
            'flags': flags,
            'delete': delete,
            'reverse': reverse,
            'parent': parent,
            'excludes': excludes or list(),
            'remote_commands': remote_commands or list(),
            'local_commands': local_commands or list(),
            'git_filter': git_filter
        }

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--remote-path', default=self.remote_path)
        parser.add_argument('--remote-host', default=self.remote_host)
        parser.add_argument('--local-path', default=self.local_path)
        parser.add_argument('-r', '--reverse', action='store_true')
        parser.add_argument('--real', action='store_true')
        parser.add_argument('-p', '--profile', default=None)
        args = parser.parse_args()
        profile = args.profile or ('reverse' if args.reverse else 'direct')
        profile_obj = self.profiles_options[profile]

        local_path, remote_path, remote_host = args.local_path, args.remote_path, args.remote_host
        if not local_path.endswith('/'):
            local_path += '/'
        if not remote_path.endswith('/'):
            remote_path += '/'

        # flags
        cmd = f"rsync {profile_obj['flags']}"
        if not args.real:
            cmd += ' --dry-run'

        # excludes
        for e in profile_obj['excludes']:
            cmd += ' --exclude="%s"' % e

        if profile_obj['git_filter']:
            cmd += ' --filter=":- .gitignore"'

        # endpoints
        if profile_obj['reverse']:
            cmd += f"{remote_host}:{remote_path} {local_path}"
        else:
            cmd += f"{local_path} {remote_host}:{remote_path}"

        self._exec_cmd(cmd)

        # post commands
        for c in profile_obj['local_commands']:
            self._exec_cmd(cmd)

        for c in profile_obj['remote_commands']:
            self._exec_cmd(f"ssh {remote_host} {c}")

    def _exec_cmd(self, cmd):
        from easilyb.terminal import cprint
        cprint('$', cmd, color='green')
        os.system(cmd)

