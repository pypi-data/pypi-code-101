"""Functions to manage RESTful API."""

from datetime import datetime
from json import loads, dumps
from math import fabs
from http.client import BadStatusLine

from future.moves.urllib.parse import urlencode
from future.moves.urllib.request import urlopen
from future.moves.urllib.error import URLError

from .i18n import _
from .utils import encrypt, decrypt
from ..models.dbuser import DBUser


TOKEN_TTL = 1.0


# =============================================================================
def restful_call(url, login, key, data=None):
    """RESTful call.

    :param str url:
        RESTful URL to call.
    :param str login:
        Login of an authorized user.
    :param str key:
        Key to decrypt the token.
    :param dict data: (optional)
        Data to transfer.
    :rtype: tuple
    :return:
        A tuple such as ``(response, error)``.
    """
    if data is None:
        data = {}
    for k in data:
        if isinstance(data[k], (tuple, list, dict)):
            data[k] = dumps(data[k])
    data['login'] = login
    data['token'] = encrypt(datetime.utcnow().isoformat(), key or '-')
    data = urlencode(data).encode('ascii')

    try:
        with urlopen(url, data) as hdl:
            response = loads(hdl.read().decode('utf8'))
    except (URLError, ValueError, BadStatusLine) as error:
        return None, str(error)

    if response['error'] is not None:
        return None, response['error']

    return response, None


# =============================================================================
def restful_login(request, key, token_ttl=None):
    """Login during a RESTful call.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str key:
        Key to decrypt the token.
    :param float token_ttl: (optional)
        Validity period in seconds for the token.
    :rtype: str
    :return:
        Translated error message or ``None``.
    """
    if 'user' in request.session:
        return None

    # Check the token
    token = request.params.get('token')
    if not token:
        return request.localizer.translate(_('Token is missing.'))
    token = decrypt(token, key or '-')
    if not token:
        return request.localizer.translate(_('Token is invalid.'))
    token = datetime.strptime(token, '%Y-%m-%dT%H:%M:%S.%f')
    delta = (datetime.utcnow() - token).total_seconds()
    if fabs(delta) > float(token_ttl or TOKEN_TTL):
        return request.localizer.translate(_('Token has expired.'))

    # Set up user session
    dbuser = DBUser.get(request, request.params.get('login'))[0]
    if dbuser is None:
        return request.localizer.translate(_('Access denied.'))
    dbuser.set_session(request)

    return None
