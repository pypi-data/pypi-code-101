from __future__ import absolute_import
import logging

import jwt
from django.http import HttpResponseRedirect
from django.conf import settings

import liblynx


logger = logging.getLogger(__name__)


DEFAULT_HOST = "127.0.0.127"
IGNORE_HOST_PARAM = "_ll_ignore_host"
ALLOW_WAYF_PARAM = "_ll_allow_wayf"
LL_JWT_COOKIE = "lljwt"
LL_RESERVED_CLAIMS = {"llorg", "llaid", "jti", "known", "llref", "sub", "ip", "iat", "exp"}
ACCOUNT_PARAM = "LIBLYNX_ACCOUNT"
ACCOUNT_ID_PARAM = "LIBLYNX_ACCOUNT_ID"
PRODUCTS_PARAM = "LIBLYNX_PRODUCTS"


def get_ip_address_from_request(request):
    """Resolve ip address of connecting client"""
    ip_address = request.META.get("HTTP_X_REAL_IP") or request.META.get("REMOTE_ADDR")

    #  If we're behind a load balancer or proxy of our own
    #  assume app has set LIBLYNX_USE_X_FORWARDED_FOR to True
    #  and take the right most IP address from the list of IPs
    #  http://guide.liblynx.com/howto/iam/howto-get-ip-address.html
    if getattr(settings, "LIBLYNX_USE_X_FORWARDED_FOR", False):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if x_forwarded_for:
            # The client is behind a proxy and the last ip address is
            # the connecting ip address to be used for authentication
            ip_address = x_forwarded_for.split(",")[-1].strip()
    
    return ip_address


class LibLynxAuthMiddleware:
    def __init__(self, get_response=None, ll_client=None):
        self.ll = ll_client or liblynx.Connect()
        self.get_response = get_response
        self.product_cache = {}

    def authenticate(self, request):
        # when proxying, the paths can be awry, so allow overriding
        src_path = request.GET.get("src_path", request.get_full_path())

        if LL_JWT_COOKIE in request.COOKIES:
            known = self._set_jwtsession(request.COOKIES[LL_JWT_COOKIE], request)
            if known:
                # if account is known, we do not try to identify any further
                return

        identification = self.ll.new_identification(
            self._resolve_host(request),
            "https://%s%s" % (request.get_host(), src_path),
            self._request_user_agent(request),
        )
        logger.debug("%s identification: %s" % (self.__class__.__name__, identification))

        if identification["status"] == "wayf":  # Needs a redirect to authenticate
            wayf_href = identification["_links"]["wayf"]["href"]
            logger.debug("%s redirect: %s" % (self.__class__.__name__, wayf_href))
            # To allow COUNTER tracking to work, and allow anonymoous usage
            # set the user to the special id 'anon'
            # We also do not want to have middelware do excessive LL API calls,
            # when unauthenticated, so set the session as well
            identification = {"account": {"account_name": "", "id": "anon"}}
            self._set_session(identification, request)

            return HttpResponseRedirect(wayf_href)

        if identification["status"] == "identified":
            self._set_session(identification, request)

    def _request_user_agent(self, request):
        """Retrieve user agent from headers, includes fallback for very old Django installs"""
        try:
            return request.headers.get("User-Agent", "<unknown>")
        except AttributeError:
            return request.META.get("HTTP_USER_AGENT", "<unknown>")

    def _set_session(self, identification, request):
        request.session[ACCOUNT_PARAM] = identification["account"]["account_name"]
        request.session[ACCOUNT_ID_PARAM] = identification["account"]["id"]
        products = identification.get("authorizations")
        # Note, LL docs says that identification["authorizations"] returns a dict,
        # see: http://guide.liblynx.com/reference/api/identification/index.html
        # But if there are no authorizations, an empty list is returned
        if products:
            logger.debug("%s products: %s" % (self.__class__.__name__, products))
            request.session[PRODUCTS_PARAM] = list(products.keys())

    def _set_jwtsession(self, jwt, request):
        claims = self.ll.get_jwt_claims(jwt)
        if not claims or not claims.get("known"):
            # no aid/aname set if token claims are empty or account is not known
            # raises exception if token signature is invalid
            return False

        request.session[ACCOUNT_PARAM] = claims["llorg"]
        request.session[ACCOUNT_ID_PARAM] = claims["llaid"]
        products = {k: v for k,v in claims.items() if k not in LL_RESERVED_CLAIMS}

        if products:
            logger.debug("%s products: %s" % (self.__class__.__name__, products))
            request.session[PRODUCTS_PARAM] = list(products.keys())
        
        return True

    def _resolve_host(self, request):
        # If the request has a _ll_ignore_host parameter, ignore the host, thus forcing a WAYF identification
        # This enables us to allow anonynous access for users who do not wish to authenticate,
        # but still allow a "Login" button

        if IGNORE_HOST_PARAM in request.GET:
            # we do need to supply a valid IP address to the API
            return DEFAULT_HOST
        return get_ip_address_from_request(request)

    def _clear_session(self, request):
        if ACCOUNT_PARAM in request.session:
            del request.session[ACCOUNT_PARAM]

        if ACCOUNT_ID_PARAM in request.session:
            del request.session[ACCOUNT_ID_PARAM]

        if PRODUCTS_PARAM in request.session:
            del request.session[PRODUCTS_PARAM]

    def process_request(self, request):
        if IGNORE_HOST_PARAM in request.GET or ALLOW_WAYF_PARAM in request.GET:
            self._clear_session(request)

        if ACCOUNT_PARAM not in request.session:
            response = self.authenticate(request)
            if response is not None and ALLOW_WAYF_PARAM in request.GET:
                return response

        try:
            return self.get_response(request)
        except TypeError:
            return None

    def __call__(self, request):
        return self.process_request(request)

