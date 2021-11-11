"""FTP library."""

from sys import version_info
from os import makedirs
from os.path import join, exists, getsize, splitext, basename
from ftplib import FTP, FTP_TLS, all_errors

from .i18n import _
from .utils import EXCLUDED_FILES, tounicode, tostr


# =============================================================================
class Ftp(object):
    """Class to manage FTP.

    :param log_error:
        Function to record errors.
    """

    # -------------------------------------------------------------------------
    def __init__(self, log_error):
        """Constructor method."""
        self._log_error = log_error
        self.connection = None

    # -------------------------------------------------------------------------
    def connect(self, values):
        """FTP connection using ``values`` to get FTP information.

        :param dict values:
            FTP values.
        :rtype: bool
        """
        # Previous connection?
        self.quit()

        # Check FTP arguments
        host = values.get('ftp_host')
        user = values.get('ftp_user', 'anonymous')
        password = values.get('ftp_password', 'anonymous@')
        if host is None:
            self._log_error(_('FTP error: bad arguments!'))
            return False

        # Connection
        self.connection = FTP_TLS() if values.get('ftp_tls') else FTP()
        try:
            self.connection.connect(host, values.get('ftp_port', 21))
            self.connection.login(user, password)
        except all_errors as error:
            self.connection = None
            self._log_ftp_error(error)
            return False
        self.connection.set_pasv(values.get('ftp_pasv', False))

        # Change to root directory
        if values.get('ftp_path') and not self.cwd(values['ftp_path']):
            self.quit()
            return False

        return True

    # -------------------------------------------------------------------------
    def cwd(self, directory):
        """Change working directory.

        :param str directory:
            Directory.
        :rtype: bool
        """
        try:
            self.connection.cwd(directory)
        except all_errors as error:
            self._log_ftp_error(error)
            return False
        return True

    # -------------------------------------------------------------------------
    def mkdir(self, directory):
        """Make a directory.

        :param str directory:
            Directory.
        :rtype: bool
        """
        try:
            self.connection.mkd(directory)
        except all_errors as error:  # pragma: nocover
            self._log_ftp_error(error)
            return False
        return True

    # -------------------------------------------------------------------------
    def list_directory(self):
        """Return the list of files in the current FTP directory.

        :rtype: tuple
        :return:
           A tuple such as ``(dirs_infos, files_infos)``.
        """
        listing = []
        try:
            self.connection.retrlines('MLSD', listing.append)
        except all_errors as error:  # pragma: nocover
            self._log_ftp_error(error)
            return {}, {}

        dirs = {}
        files = {}
        for item in listing:
            item = item.partition(' ')
            infos = {
                k.split('=')[0].lower():  k.split('=')[1]
                for k in item[0].split(';') if k}
            name = item[2]
            if infos['type'] == 'dir':
                dirs[name] = infos
            elif infos['type'] == 'file':
                files[name] = infos

        return dirs, files

    # -------------------------------------------------------------------------
    def delete(self, filename):
        """Delete the file ``filename``.

        :rtype: bool
        """
        try:
            self.connection.delete(filename)
        except all_errors as error:  # pragma: nocover
            self._log_ftp_error(error)
            return False
        return True

    # -------------------------------------------------------------------------
    def rmtree(self, directory):
        """Remove the directory ``directory``.

        :rtype: bool
        """
        if not self.cwd(directory):
            return False

        dirs, files = self.list_directory()
        for name in files:
            if not self.delete(name):
                return False  # pragma: nocover
        for name in dirs:
            if not self.rmtree(name):
                return False  # pragma: nocover

        self.connection.cwd('..')
        try:
            self.connection.rmd(directory)
        except all_errors as error:  # pragma: nocover
            self._log_ftp_error(error)
            return False

        return True

    # -------------------------------------------------------------------------
    def download(self, destination, exclude=None):
        """Transfer the current FTP directory into the ``destination``
        directory.

        :rtype: bool
        :return:
            ``True`` if the download completed.
        :param list exclude: (optional)
            List of files to exclude.
        """
        # pylint: disable = too-many-branches
        dirs, files = self.list_directory()
        if not dirs and not files:
            return True

        if not exists(destination):
            makedirs(destination)
        if exclude is None:
            exclude = EXCLUDED_FILES

        completed = True
        for name, infos in files.items():
            if name in exclude:
                continue
            if splitext(name)[1] in ('.part', '.filepart'):
                completed = False
                continue
            try:
                fullname = join(destination, tounicode(name))
            except UnicodeDecodeError as error:  # pragma: nocover
                self._log_ftp_error(error)
                continue
            if not exists(fullname) or \
               getsize(fullname) != int(infos['size']):
                with open(fullname, 'wb') as hdl:
                    self.connection.retrbinary(
                        tostr('RETR {0}'.format(tounicode(name))),
                        hdl.write)
                completed = False

        for name in dirs:
            if name in exclude:
                continue
            try:
                self.connection.cwd(name)
            except all_errors as error:  # pragma: nocover
                self._log_ftp_error(error)
                continue
            try:
                new_destination = join(destination, tounicode(name))
            except UnicodeDecodeError as error:  # pragma: nocover
                self._log_ftp_error(error)
                continue
            if not exists(new_destination):
                makedirs(new_destination)
            completed &= self.download(new_destination)
            self.connection.cwd('..')

        return completed

    # -------------------------------------------------------------------------
    def upload(self, filename, upload_name=None):
        """Upload a file in the current directory.

        :param str filename:
            Absolute path to the file to upload.
        :param str upload_name: (optional)
            Name of the uploaded file.
        """
        stor = 'STOR {0}'.format(upload_name or basename(filename))
        stor = stor.encode('utf8') if version_info < (3, 0) else stor
        with open(filename, 'rb') as hdl:
            self.connection.storbinary(stor, hdl)

    # -------------------------------------------------------------------------
    def quit(self):
        """Quit the FTP connection."""
        if self.connection is not None:
            try:
                self.connection.quit()
                self.connection.close()
            except all_errors as error:  # pragma: nocover
                self._log_ftp_error(error)
            self.connection = None

    # -------------------------------------------------------------------------
    def _log_ftp_error(self, error):
        """Add an error message in the log cache.

        :param str text:
            Error.
        """
        self._log_error(_('FTP error: ${e}', {'e': tounicode(error)}))
