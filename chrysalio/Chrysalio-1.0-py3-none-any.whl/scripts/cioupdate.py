#!/usr/bin/env python
"""Console script to backup and update Chrysalio sites."""

from sys import executable
from logging import getLogger
from os import chown, makedirs, setgid, setuid, environ
from os.path import join, exists, dirname, expanduser, abspath, normpath
from os.path import relpath
from argparse import REMAINDER, ArgumentParser
from pwd import getpwnam
from getpass import getuser
from compileall import compile_dir
from configparser import ConfigParser
from zipfile import ZIP_DEFLATED, ZipFile

from git import Repo
from git.exc import GitCommandError

from ..lib.i18n import _, translate
from ..lib.utils import walk, scandir
from ..lib.config import config_get, config_get_namespace
from ..lib.log import setup_logging
from ..lib.utils import tounicode, encrypt, decrypt, execute, full_url


LOG = getLogger(__name__)
SECTION_PREFIX = 'Update'


# =============================================================================
def main(args=None):
    """Main function."""
    # Parse arguments
    parser = ArgumentParser('Backup and update Chrysalio sites.')
    parser.add_argument(
        'conf_file', help='configuration file (e.g. cioupdate.ini)')
    parser.add_argument(
        'sites', nargs='*', help='only update these sites (optional)')
    parser.add_argument('--lang', dest='lang', help='user language')
    parser.add_argument(
        '--encrypt', dest='password', help='encrypt password and exit')
    parser.add_argument(
        '--encrypt-key', dest='key', help='optional key for encryption')
    parser.add_argument(
        '--no-backup', dest='no_backup', help='do not backup instance',
        action='store_true')
    parser.add_argument(
        '--no-update', dest='no_update', help='do not update instance',
        action='store_true')
    parser.add_argument(
        '--drop-tables', dest='drop_tables', help='drop existing tables',
        action='store_true')
    parser.add_argument(
        '--remove-locks', dest='remove_locks', action='store_true',
        help='remove locks directory')
    parser.add_argument(
        '--remove-builds', dest='remove_builds', action='store_true',
        help='remove builds directory')
    parser.add_argument(
        '--skip-refresh', dest='skip_refresh', action='store_true',
        help='skip refreshment step')
    parser.add_argument(
        '--recreate-thumbnails', dest='recreate_thumbnails',
        action='store_true', help='recreate thumbnails')
    parser.add_argument(
        '--reindex', dest='reindex', action='store_true',
        help='recreate indexes')
    parser.add_argument(
        '--log-level', dest='log_level', help='log level', default='INFO',
        choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'))
    parser.add_argument('--log-file', dest='log_file', help='log file')
    parser.add_argument('extra', nargs=REMAINDER, help='extra options')
    args = parser.parse_args(args)
    conf_file = expanduser(args.conf_file)
    if not exists(conf_file):
        parser.print_usage()
        return
    setup_logging(args.log_level, args.log_file)

    # Backup and update
    CioUpdate(args, conf_file).start(args.sites)


# =============================================================================
class CioUpdate(object):
    """Class to backup and update Chrysalio sites."""

    # -------------------------------------------------------------------------
    def __init__(self, args, conf_file):
        """Constructor method."""
        self._args = args
        self._config = ConfigParser({'here': dirname(abspath(conf_file))})
        self._config.read(tounicode(conf_file), encoding='utf8')
        self._key = args.key or self._config_get('Code', 'key', '-')
        self._cookiecutters = self._config_get('Code', 'cookiecutters')
        if self._cookiecutters:
            self._cookiecutters = expanduser(self._cookiecutters)

    # -------------------------------------------------------------------------
    def start(self, sites=None):
        """Start backup and update.

        :param list sites: (optional)
            Chrysalio sites to backup and update. If empty, this method
            processes all Chrysalio sites defined in configuration file.
        :rtype: bool
        """
        # Only encrypt password
        if self._args.password:
            LOG.info(
                '%s = %s', self._args.password,
                encrypt(self._args.password.encode('utf8'), self._key))
            return True

        # List of sites to update
        if not sites:
            sites = [
                k[len(SECTION_PREFIX):] for k in self._config.sections()
                if k.startswith(SECTION_PREFIX)]
        if 'Code' not in sites:
            sites.insert(0, 'Code')

        # Backup web sites
        is_ok = True
        if not self._args.no_backup:
            LOG.info('{0:=^60}'.format(self._translate(_(' Backup '))))
            for site in sites:
                is_ok &= self._backup(site)
        if not is_ok or self._args.no_update:
            return is_ok

        # Update and compile sources
        LOG.info('{0:=^60}'.format(self._translate(_(' Update '))))
        for site in sites:
            is_ok &= self._update_sources(site)
        if not is_ok:
            return is_ok

        # Populate web sites
        is_ok = True
        LOG.info('{0:=^60}'.format(self._translate(_(' Populating '))))
        for site in sites:
            is_ok &= self._populate(site)
        if not is_ok:
            return is_ok

        # Restart Apache
        if self._config_get('Code', 'reload'):  # pragma: nocover
            LOG.info('{0:-^60}'.format(
                self._translate(_(' Restarting server '))))
            error = execute(self._config_get('Code', 'reload').split())
            LOG.info(self._translate(error[0]))
            if error[1]:
                LOG.error(self._translate(error[1]))
                return False

        return True

    # -------------------------------------------------------------------------
    def _backup(self, site):
        """Backup a Chrysalio site.

        :param str site:
            Name of Chrysalio site to backup.
        :rtype: bool
        """
        # Something to do?
        conf_uri = self._config_get(site, 'conf_uri')
        if conf_uri is None or not exists(conf_uri.partition('#')[0]):
            return True
        directory = self._config_get(site, 'backup.directory')
        command = self._config_get(site, 'backup.command')
        if directory is None or command is None:
            return True
        args = self._config_get(site, 'backup.args')
        user, env = self._user_ids_and_env(self._config_get(site, 'user'))

        # Backup
        LOG.info('%s %s', command, site)
        cmd = [executable, join(dirname(executable), command)]
        cmd = cmd + ['--lang', self._args.lang] if self._args.lang else cmd
        cmd = cmd + ['--log-file', self._args.log_file] \
            if self._args.log_file else cmd
        cmd = cmd + args.split() if args else cmd
        cmd += ['--log-level', self._args.log_level, conf_uri, directory]
        cmd += self._args.extra
        output, error = execute(cmd, preexec_fn=self._demote(*user), env=env)
        if error:
            LOG.error(translate(
                error[33:] or _('"${c}" failed', {'c': command})))
            return False
        if output:
            LOG.warning(output[33:])

        return True

    # -------------------------------------------------------------------------
    def _update_sources(self, site):
        """Update and possibly compile sources.

        :param str site:
            Name of Chrysalio site to backup.
        :rtype: bool
        """
        sources = config_get_namespace(
            self._config, '{0}{1}'.format(SECTION_PREFIX, site), 'source')

        is_ok = True
        for source in sources:
            if not source.endswith('repository'):
                continue
            repository = normpath(self._config_get(
                site, 'source.{0}'.format(source.replace('_', '.'))))
            LOG.info(repository)
            error = self._recursive_chown(repository, getuser())
            if error:  # pragma: nocover
                LOG.error(error)
                is_ok = False
                continue

            error = self._git_pull(repository, site)
            if error:
                LOG.error(self._translate(error))
                is_ok = False
                continue

            code = self._config_get(
                site, 'source.{0}.code'.format(source[:-11]))
            if code is not None and exists(code):
                compile_dir(code, quiet=True)

            cookiecutters = self._config_get(
                site, 'source.{0}.cookiecutters'.format(source[:-11]))
            if self._cookiecutters and cookiecutters is not None \
               and exists(cookiecutters):
                self._zip_cookiecutters(cookiecutters)

            error = self._recursive_chown(
                repository, self._config_get(site, 'user'))
            if error:
                LOG.error(error)
                is_ok = False

        if self._cookiecutters and exists(self._cookiecutters):
            self._recursive_chown(
                self._cookiecutters, self._config_get('Code', 'user'))

        return is_ok

    # -------------------------------------------------------------------------
    def _populate(self, site):
        """Populate a Chrysalio site.

        :param str site:
            Name of Chrysalio site to populate.
        :rtype: bool
        """
        # Something to do?
        conf_uri = self._config_get(site, 'conf_uri')
        if conf_uri is None or not exists(conf_uri.partition('#')[0]):
            return True
        command = self._config_get(site, 'populate.command')
        if command is None:
            return True
        args = self._config_get(site, 'populate.args')
        drop_tables = self._args.drop_tables or \
            self._config_get(site, 'populate.drop_tables') == 'true'
        user, env = self._user_ids_and_env(self._config_get(site, 'user'))
        env['PWD'] = dirname(conf_uri.partition('#')[0])

        # Populate
        LOG.info('###### %s %s ######', command, site)
        cmd = [executable, join(dirname(executable), command)]
        cmd = cmd + ['--drop-tables'] if drop_tables else cmd
        cmd = cmd + ['--remove-locks'] if self._args.remove_locks else cmd
        cmd = cmd + ['--remove-builds'] if self._args.remove_builds else cmd
        cmd = cmd + ['--skip-refresh'] if self._args.skip_refresh else cmd
        cmd = cmd + ['--recreate-thumbnails'] \
            if self._args.recreate_thumbnails else cmd
        cmd = cmd + ['--reindex'] if self._args.reindex else cmd
        cmd = cmd + ['--lang', self._args.lang] if self._args.lang else cmd
        cmd = cmd + ['--log-file', self._args.log_file] \
            if self._args.log_file else cmd
        cmd = cmd + args.split() if args else cmd
        cmd += ['--log-level', self._args.log_level, conf_uri]
        cmd += self._args.extra
        output, error = execute(
            cmd, cwd=env['PWD'], preexec_fn=self._demote(*user), env=env)
        if error:
            LOG.error(translate(output or _('"${c}" failed', {'c': command})))
            return False
        LOG.info(output[33:])

        return True

    # -------------------------------------------------------------------------
    def _git_pull(self, repo_path, site):
        """Pull and update a Git repository.

        :param str repo_path:
            Absolute path to of the repository.
        :param str site:
            Name of Chrysalio site to backup.
        :rtype: pyramid.i18n.TranslationString
        :return:
            Error message or ``None``.
        """
        if not exists(join(repo_path, '.git', 'config')):
            return _('This directory is not a Git repository.')

        gituser = self._config_get(site, 'gituser', 'gituser')
        gitpassword = decrypt(
            self._config_get(site, 'gitpassword', ''), self._key)
        repo = Repo(repo_path)
        if not repo.remotes:  # pragma: nocover
            return _('No remote repository')
        url = repo.remotes.origin.url
        fullurl = full_url(url, gituser, gitpassword)
        try:
            repo.remotes.origin.set_url(fullurl)
            repo.remotes.origin.pull()
        except GitCommandError as error:  # pragma: nocover
            return str(error).replace(fullurl, url)
        finally:
            repo.remotes.origin.set_url(url)
        return None

    # -------------------------------------------------------------------------
    @classmethod
    def _recursive_chown(cls, path, user):
        """Change owner of directory ``path`` recursively.

        :param str path:
            Absolute path to directory to process.
        :param str user:
            User name.
        :rtype: str
        :return:
            Error message or ``None``.
        """
        if not user:
            return None
        try:
            user = getpwnam(user)
        except KeyError as error:
            return error

        try:
            chown(path, user.pw_uid, user.pw_gid)
        except OSError as error:  # pragma: nocover
            return error

        for root, dirs, files in walk(path.encode('utf8')):
            for name in dirs:
                if name == b'.tox':
                    dirs.remove(name)  # pragma: nocover
                else:
                    chown(join(root, name), user.pw_uid, user.pw_gid)
            for name in files:
                chown(join(root, name), user.pw_uid, user.pw_gid)
        return None

    # -------------------------------------------------------------------------
    def _zip_cookiecutters(self, cookiecutters):
        """Zip each cookiecutter found in ``cookiecutters`` directory.

        :param str cookiecutters:
            Absolute path to cookiecutters directory.
        """
        if not exists(self._cookiecutters):
            makedirs(self._cookiecutters)

        for entry in scandir(cookiecutters):
            if not exists(join(entry.path, 'cookiecutter.json')):
                continue  # pragma: nocover
            filename = join(self._cookiecutters, '{0}.zip'.format(entry.name))
            with ZipFile(filename, 'w', ZIP_DEFLATED) as zip_file:
                root = normpath(join(entry.path, '..'))
                zip_file.write(entry.path, entry.name)
                for path, unused_, files in walk(entry.path):
                    for name in files:
                        name = join(path, name)
                        zip_file.write(name, relpath(name, root))
            LOG.info(self._translate(
                _('${n} -> ${f}', {'n': entry.name, 'f': filename})))

    # -------------------------------------------------------------------------
    @classmethod
    def _user_ids_and_env(cls, user=None):
        """Return a tuple such as ``((uid, group), env)``.

        :param str user: (optional)
            User log name.
        :rtype: tuple
        """
        log_name = user or getuser()
        try:
            pw_record = getpwnam(log_name)
        except KeyError:
            pw_record = getpwnam(getuser())

        env = environ.copy()
        env.update({
            'HOME': pw_record.pw_dir, 'LOGNAME': pw_record.pw_name,
            'USER': pw_record.pw_name})
        return (pw_record.pw_uid, pw_record.pw_gid), env

    # -------------------------------------------------------------------------
    @classmethod
    def _demote(cls, user_uid, user_gid):
        """Demote the current user.

        :param int user_uid:
            User UID.
        :param int user_gid:
            User group.
        """
        def result():  # pragma: nocover
            """Change user."""
            setgid(user_gid)
            setuid(user_uid)
        return result

    # -------------------------------------------------------------------------
    def _config_get(self, section, option, default=None):
        """Retrieve a value from the `cioupdate` configuration file.

        :param str section:
            Section name.
        :param str option:
            Option name.
        :param str default: (optional)
            Default value
        :rtype: str
        """
        return config_get(
            self._config, '{0}{1}'.format(SECTION_PREFIX, section), option,
            default)

    # -------------------------------------------------------------------------
    def _translate(self, text):
        """Return ``text`` translated.

        :param str text:
            Text to translate.
        :rtype: str
        """
        return translate(text, self._args.lang)
