# -*- coding: utf-8 -*-
"""Some various utilities."""

# pylint: disable = unused-import
try:  # pragma: nocover
    from os import scandir, walk
except ImportError:  # pragma: nocover
    from scandir import scandir, walk  # noqa
# pylint: enable = unused-import
from os import makedirs
from os.path import basename, exists, join, isdir, getmtime, dirname
from os.path import commonprefix
from sys import version_info
from logging import getLogger
from shutil import copy2
from unicodedata import normalize, combining
from base64 import b64encode, b64decode
from hashlib import sha256, md5
from random import SystemRandom, randrange
from string import ascii_uppercase, digits
from re import UNICODE, sub as re_sub
from binascii import Error as BAError
from datetime import datetime
from filecmp import cmpfiles
from mimetypes import guess_type
from subprocess import PIPE, STDOUT, Popen, TimeoutExpired
from subprocess import SubprocessError
from bcrypt import hashpw, gensalt

from future.moves.urllib.parse import urlparse, urlunparse
from Crypto import Random
from Crypto.Cipher import AES
from docutils.core import publish_parts

from pyramid.asset import abspath_from_asset_spec

from .i18n import _, translate


LOG = getLogger(__name__)
EXCLUDED_FILES = (
    '.git', '.hg', '.svn', 'Thumbs.db', '.DS_Store', '_MACOSX', '__MACOSX',
    '__pycache__')


# =============================================================================
def tostr(text):
    """Make a conversion according to Python version.

    :type  text: :class:`str` or :class:`bytes`
    :param text:
        Text to convert.
    :rtype: str
    """
    return \
        (version_info > (3, 0) and isinstance(text, bytes) and
         text.decode('utf8')) or \
        (version_info > (3, 0) and text) or \
        text.encode('utf8')


# =============================================================================
def tounicode(text):
    """Make a conversion according to Python version.

    :type  text: :class:`str` or :class:`bytes`
    :param text:
        Text to convert.
    :rtype: :class:`str` (Python 3) or ``unicode`` (Python 2)
    """
    return \
        (version_info > (3, 0) and isinstance(text, bytes) and
         text.decode('utf8')) or \
        (version_info > (3, 0) and text) or \
        (isinstance(text, (str, bytes)) and text.decode('utf8')) or text


# =============================================================================
def load_guessing_encoding(filename):
    """Tries to open a file by guessing its encoding.

    :param str filename:
        Absolute path to the file.
    :rtype: :class:`str` (Python 3) or ``unicode`` (Python 2) or ``None``
    """
    guessed = False
    with open(filename, 'rb') as hdl:
        content = hdl.read()

    # UTF-8
    try:
        content = content.decode('utf_8')
        guessed = True
    except UnicodeDecodeError:
        pass

    # Latin 1
    if not guessed:
        try:
            content = content.decode('latin_1')
            guessed = True
        except UnicodeDecodeError:  # pragma: nocover
            pass

    return content if guessed else None


# =============================================================================
def copy_content(src_dir, dst_dir, exclude=None, force=False):
    """Copy the content of a ``src_dir`` directory into a ``dst_dir``
    directory.

    :param str src_dir:
        Source directory path.
    :param str dst_dir:
        Destination directory path.
    :param list exclude: (optional)
        List of files to exclude.
    :param bool force: (optional)
        Force copy even if the target file has the same date.
    """
    if not exists(dst_dir):
        makedirs(dst_dir)
    if exclude is None:
        exclude = EXCLUDED_FILES
    for entry in scandir(src_dir):
        if entry.name not in exclude:
            destination = join(dst_dir, tounicode(entry.name))
            if entry.is_dir():
                copy_content(entry.path, destination, exclude, force)
            elif force or not exists(destination) \
                    or getmtime(destination) != getmtime(entry.path):
                copy2(entry.path, destination)


# =============================================================================
def copy_content_re(src_dir, dst_dir, exclude=None):
    """Copy the content of a ``src_dir`` directory into a ``dst_dir``
    directory.

    :param str src_dir:
        Source directory path.
    :param str dst_dir:
        Destination directory path.
    :param exclude: (optional)
        Regular expression to exclude files during the copy.
    """
    if not exists(dst_dir):
        makedirs(dst_dir)
    for entry in scandir(src_dir):
        if exclude is None or exclude.search(entry.name) is None:
            destination = join(dst_dir, entry.name)
            if entry.is_dir():
                copy_content_re(entry.path, destination, exclude)
            else:
                copy2(entry.path, destination)


# =============================================================================
def make_id(name, mode=None, truncate=None):
    """Make an ID with name.

    :param str name:
        Name to use.
    :param int truncate: (optional)
        If not ``None``, maximum length of the returned string.
    :param str mode: (optional)
        Strategy to make ID : 'standard', 'token', 'xmlid', 'class' or
        'no_accent'.
    :rtype: str

    Examples of transformation of `12Test___Té*t.;?!`:

    * mode = ``None``: `12test___té*t.;?!`
    * mode = 'standard': `12Test_Té_t._`
    * mode = 'token': `12test_te_t._`
    * mode = 'xmlid': `_12test_te_t._`
    * mode = 'class': `12Test_Te_t_`
    * mode = 'no_accent': `12Test___Te*t.;?!`
    """
    result = name.strip()
    if mode not in ('standard', 'class', 'no_accent'):
        result = result.lower()
    if mode in ('standard', 'token', 'xmlid', 'class'):
        result = re_sub(
            '_+', '_', re_sub('[  *?!;:,"\'/«»()\\[\\]–&]', '_', result))
    if mode in ('token', 'xmlid', 'class', 'no_accent'):
        result = normalize('NFKD', result.encode('utf8').decode('utf8'))
        result = ''.join([k for k in result if not combining(k)])
    if mode == 'xmlid' and result and result[0].isdigit():
        result = '_{0}'.format(result)
    if mode == 'class':
        result = re_sub('_+', '_', re_sub(r'\.', '_', result))
    return result[0:truncate] if truncate else result


# =============================================================================
def make_digest(name):
    """Create a digest key with name.

    :param str name:
        Name to use.
    """
    return md5(name.encode('utf8')).hexdigest()


# =============================================================================
def normalize_spaces(text, truncate=None):
    """Normalize spaces and, possibly, truncate result.

    :param str text:
        Text to normalize.
    :param int truncate: (optional)
        If not ``None``, maximum lenght of the returned string.
    :rtype: :class:`str` or ``None``
    """
    if text is None:
        return None
    text = ' '.join(text.replace(' ', ':~:').strip().split())\
        .replace(':~:', ' ')
    return text[0:truncate] if truncate else text


# =============================================================================
def camel_case(text):
    """Convert ``text`` in Camel Case.

    :param str text:
        Text to transform.

    Examples of transformation:

    xml2html -> Xml2Html
    laTeX -> LaTeX
    my_way -> MyWay
    my way -> MyWay
    my-way -> MyWay
    """
    return re_sub(
        r'(^\w|[-_ 0-9]+\w)',
        lambda m: m.group(0).replace('_', '').replace(' ', '').upper(),
        text, flags=UNICODE)


# =============================================================================
def shorten(text, width, placeholder='…'):
    """Collapse and truncate the given text to fit in the given width.

    :param str text:
        Text to shorten.
    :param int with:
        The result fits in the width.
    :param str placeholder: (default=…)
        Place holder to use if the size is too big.
    :rtype: str
    """
    text = normalize_spaces(text)
    return text if len(text) <= width else \
        '{0}{1}'.format(text[:width - len(placeholder)], placeholder)


# =============================================================================
def encrypt(value, key, init_vector=None):
    """Encryption function.

    :param bytes value:
        Value to encrypt.
    :param str key:
        Encryption key.
    :param bytes init_vector: (optional)
        Initialization vector for AES algorithm.
    :rtype: bytes
    :retrun:
        Encrypted value or ``None``.
    """
    if not value:
        return value
    bsize = AES.block_size
    if version_info > (3, 0) and not isinstance(value, bytes):
        value = bytes(value, 'utf8')  # pragma: nocover
    value = value + \
        (bsize - len(value) % bsize) * \
        chr(bsize - len(value) % bsize).encode('latin-1')
    if not isinstance(key, bytes):
        key = key.encode('utf8')
    key = sha256(key).digest()
    init_vector = init_vector or Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    return tostr(b64encode(init_vector + cipher.encrypt(value)))


# =============================================================================
def decrypt(value, key):
    """Encryption function with padding.

    :param bytes value:
        String to encrypt.
    :param str key:
        Encryption key.
    :param str init_vector: (optional)
        Initialization vector for AES algorithm.
    :rtype: str
    :return:
        Encrypted value or ``None``.
    """
    if not value:
        return value
    try:
        value = b64decode(value)
    except (TypeError, BAError):
        return None
    if not isinstance(key, bytes):
        key = key.encode('utf8')
    key = sha256(key).digest()
    init_vector = value[:AES.block_size]
    if len(init_vector) != AES.block_size:
        return None
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    try:
        value = cipher.decrypt(value[AES.block_size:])
    except ValueError:  # pragma: nocover
        return None
    try:
        return value[:-ord(value[len(value) - 1:])].decode('utf8')
    except UnicodeDecodeError:  # pragma: nocover
        return None


# =============================================================================
def token(length=None):
    """Generate a token of length ``length`` or with a length between 8 an 16
    characters.

    :param int length: (optional)
        Length of the token.
    :rtype: str
    :return:
        Token.
    """
    if length is None:
        length = randrange(8, 16)
    return ''.join(
        SystemRandom().choice(ascii_uppercase + digits) for _ in range(length))


# =============================================================================
def execute(command, cwd=None, no_exit_code=False, timeout=None, **kwargs):
    """Run the command described by command. Wait for command to complete.
    If the return code is not zero, return output and an error message.

    :param list command:
        Splitted command to execute.
    :param str cwd: (optional)
        If it is not ``None``, the current directory will be changed to ``cwd``
        before it is executed.
    :param bool no_exit_code: (default=False)
        If the command is known to exit with code 0 even if there is an error,
        assign this argument to ``True``.
    :param float timeout: (default=None)
        If set and the process hasn't finished in that time (in seconds),
        exits with error. The process is not killed.
    :param dict kwargs: (optional)
        Dictionary of keyword arguments.
    :rtype: tuple
    :return:
        An error message such as ``(output, error)`` where ``output`` is a
        string and ``error`` a :class:`pyramid.i18n.TranslationString`.
    """
    # pylint: disable = consider-using-with
    try:
        process = Popen(command, cwd=cwd, stderr=STDOUT, stdout=PIPE, **kwargs)
    except (OSError, ValueError, SubprocessError) as error:
        return '', _('"${c}" failed: ${e}', {'c': command, 'e': error})
    if command[0] == 'nice':
        command = command[1:]
    command = basename(command[0])
    try:
        output = process.communicate(timeout=timeout)[0]
        if process.poll() or (no_exit_code and output):
            try:
                return output[0:102400].decode('utf8').strip(), \
                    _('"${c}" failed', {'c': command})
            except UnicodeDecodeError:  # pragma: nocover
                return output[0:102400].decode('latin1').strip(), \
                    _('"${c}" failed', {'c': command})
    except (OSError, TimeoutExpired) as error:  # pragma: nocover
        return '', _('"${c}" failed: ${e}', {'c': command, 'e': error})
    output = output[0:102400]
    try:
        output = output.decode('utf8')
    except UnicodeDecodeError:  # pragma: nocover
        pass
    return output.strip(), ''


# =============================================================================
def full_url(url, user=None, password=None):
    """Return an URL with ``user`` and possibly ``password``.

    :param str url:
        URL to update.
    :param str user:
        User for VCS access.
    :param str password:
        Password for VCS access.
    :rtype: str
    :return:
        Full URL.
    """
    if not user:
        return url
    scheme, netloc, path, params, query, fragment = urlparse(str(url))
    netloc = '{0}{1}@{2}'.format(
        user, password and ':{0}'.format(password) or '',
        netloc.rpartition('@')[2])
    return urlunparse((scheme, netloc, path, params, query, fragment))


# =============================================================================
def mimetype_get(full_path):
    """Return the mime type of ``full_path``.

    :param str full_path:
        Absolute path to the file.
    :rtype: tuple
    :return:
        A tuple such as ``(mimetype, subtype)``. For instance:
        ``('text/plain', 'plain')``.
    """
    if isdir(full_path):
        return 'directory', 'directory'
    mimetype = guess_type(tostr(full_path), False)[0]
    if mimetype is None:
        return 'unknown', 'unknown'
    subtype = mimetype.partition('/')[2]
    return mimetype, subtype or mimetype


# =============================================================================
def deltatime_label(seconds=0, minutes=0, hours=0, days=0, lang=None):
    """Return a translated label for a delta time.

    :param int seconds:
        Number of seconds.
    :param int minutes:
        Number of minutes.
    :param int hours:
        Number of hours.
    :param int days:
        Number of days.
    :param str lang: (optional)
        Language to use.
    :rtype: pyramid.i18n.TranslationString
    :return:
        Return a human reading translation string.
    """
    delta = seconds + 60 * minutes + 3600 * hours + 86400 * days
    if delta <= 0:
        return translate(_('0 second'), lang)

    days = int(delta // 86400)
    delta = delta % 86400
    hours = int(delta // 3600)
    delta = delta % 3600
    minutes = int(delta // 60)
    seconds = delta % 60
    label = ''

    if days:
        label = translate(
            _('1 day') if days == 1 else
            _('${d} days', {'d': days}), lang)
    if hours:
        label = '{0} '.format(label) if label else ''
        label += translate(
            _('1 hour') if hours == 1 else
            _('${h} hours', {'h': hours}), lang)
    if minutes:
        label = '{0} '.format(label) if label else ''
        label += translate(
            _('1 minute') if minutes == 1 else
            _('${m} minutes', {'m': minutes}), lang)
    if seconds:
        label = '{0} '.format(label) if label else ''
        label += translate(
            _('1 second') if seconds == 1 else
            _('${s} seconds', {'s': seconds}), lang)

    return label


# =============================================================================
def age(mtime):
    """Return an age in minutes, hours, days or a date.

    :param datetime mtime:
        Modification time.
    :rtype: pyramid.i18n.TranslationString
    :return:
        Return an age or a date if ``mtime`` is older than a year.
    """
    # pylint: disable = too-many-return-statements
    if not mtime:
        return ''
    delta = datetime.now() - mtime

    if delta.days < 0:
        return _('0 second')
    if delta.days == 0 and delta.seconds < 60:
        return _('1 second') if delta.seconds <= 1 \
            else _('${s} seconds', {'s': delta.seconds})
    if delta.days == 0 and delta.seconds < 3600:
        minutes = int(round(delta.seconds / 60))
        return _('1 minute') if minutes == 1 \
            else _('${m} minutes', {'m': minutes})
    if delta.days == 0:
        hours = int(round(delta.seconds / 3600))
        return _('1 hour') if hours == 1 \
            else _('${h} hours', {'h': hours})
    if delta.days < 7:
        return _('1 day') if delta.days == 1 \
            else _('${d} days', {'d': delta.days})
    if delta.days < 30:
        weeks = int(round(delta.days / 7))
        return _('1 week') if weeks == 1 \
            else _('${w} weeks', {'w': weeks})
    if delta.days < 365:
        months = int(round(delta.days / 30))
        return _('1 month') if months == 1 else \
            _('${m} months', {'m': months})

    return str(mtime.replace(microsecond=0))[0:-9]


# =============================================================================
def size_label(size, is_dir=False):
    """Return a size in o, Kio, Mio or Gio.

    :param int size:
        Size in figures.
    :param bool is_dir: (optional)
        ``True`` if it is about a directory.
    :rtype: :class:`str` or :class:`pyramid.i18n.TranslationString`
    """
    # For a directory
    if is_dir:
        return _('${n} items', {'n': size}) if size > 1 else \
            _('${n} item', {'n': size})

    # For a file
    if size >= 1073741824:
        return '{0:.1f} Gio'.format(round(size / 1073741824.0, 1))
    if size >= 1048576:
        return '{0:.1f} Mio'.format(round(size / 1048576.0, 1))
    if size >= 1024:
        return '{0:.1f} Kio'.format(round(size / 1024.0, 1))
    return '{0} o'.format(size)


# =============================================================================
def convert_value(type_, value):
    """Convert a string value according to type ``type_``.

    :param str type_:
        Type of the value.
    :rtype: :class:`str`, :class:`bool`, :class:`int`, :class:`float` or
        :class:`datetime.date`
    """
    if type_ == 'boolean':
        value = value not in (None, '', 'false', 'False', '0')
    elif type_ == 'integer':
        value = int(value) if value and value.isdigit() else 0
    elif type_ == 'decimal':
        try:
            value = float(value)
        except ValueError:
            value = 0
    elif type_ == 'datetime':
        try:
            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S').replace(
                microsecond=0, tzinfo=None)
        except ValueError:
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                value = None
    elif type_ == 'date':
        try:
            value = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            value = None
    return value


# =============================================================================
def check_chrysalio_js(js_dir):
    """Check if the ``chrysalio.js`` file exists in ``js_dir`` directory and if
    it is the last version and possibly update them.

    :param str js_dir:
        Directory for Javascript files.
    """
    js_dir = abspath_from_asset_spec(js_dir)
    if not exists(js_dir):
        return

    cio_js_dir = join(dirname(__file__), '..', 'Static', 'Js')
    js_files = (
        'jquery.js', 'js.cookie.js', 'jquery-ui.js',
        'jquery-ui-datepicker-fr.js', 'chrysalio.js',
        'chrysalio-datepicker.js', 'chrysalio-filter.js')
    for name in cmpfiles(cio_js_dir, js_dir, js_files)[1]:
        try:
            copy2(join(cio_js_dir, name), js_dir)
        except IOError:  # pragma: nocover
            LOG.warning('"%s" is not up to date.', name)


# =============================================================================
def check_chrysalio_css(css_dir):
    """Check if the Chrysalio CSS file exists in ``css_dir`` directory
    and if it is the last version and possibly update them.

    :param str css_dir:
        Directory for CSS files.
    """
    css_dir = abspath_from_asset_spec(css_dir)
    if not exists(css_dir):
        return
    cio_css_dir = join(dirname(__file__), '..', 'Static', 'Css')
    css_files = ('jquery-ui.css',)
    for name in cmpfiles(cio_css_dir, css_dir, css_files)[1]:
        try:
            copy2(join(cio_css_dir, name), css_dir)
        except IOError:  # pragma: nocover
            LOG.warning('"%s" is not up to date.', name)


# =============================================================================
def common_directory(files):
    """Return the common directory of the list of files.

    :param list files:
        List of files to analyse.
    :rtype: str
    """
    if not files:
        return None
    directory = commonprefix(files)
    if not isdir(directory):
        directory = dirname(directory)
    return directory if isdir(directory) else None


# =============================================================================
def hash_admin_password(project_dir, files, password):
    """Add hashed password for administrator in each file of the ``files`` list
    contained in ``project_dir`` directory.

    :param str project_dir:
        Project directory containing INI files.
    :param tuple files:
        List of files to process.
    :param str password:
        Clear password.
    """
    hashed = hashpw(password.encode('utf8'), gensalt()).decode('utf8')
    for filename in files:
        filename = join(project_dir, filename)
        with open(filename, 'r') as hdl:
            content = hdl.read()
        content = content.replace(
            'admin.password = {0}'.format(password),
            '#admin.password = {0}\nadmin.password = {1}'.format(
                password, hashed))
        with open(filename, 'w') as hdl:
            hdl.write(content)


# =============================================================================
def rst2html(rst):
    """Transform a reStructuredText into HTML.

    :param str rst:
        reStructuredText.
    :rtype: str
    :return:
        XHTML.
    """
    html = publish_parts(rst, writer_name='html')['body'] if rst else None
    return re_sub('(^<p>|</p>\n)', '', html) \
        if rst and 'ERROR/' not in html else rst
