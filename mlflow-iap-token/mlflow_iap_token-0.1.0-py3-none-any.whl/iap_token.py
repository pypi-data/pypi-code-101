from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider
import os, sys
from google.oauth2 import id_token
from google.auth.transport.requests import Request as AuthRequest

from pathlib import Path
from subprocess import check_output
import six
import requests
import logging
import functools

def get_token(request_uri: str = None):
    """Set valid service-account path to 'GOOGLE_APPLICATION_CREDENTIALS' envvar """
    try:
        redirect_response = requests.get(request_uri, allow_redirects=False)
        redirect_location = redirect_response.headers.get("location")
        parsed = six.moves.urllib.parse.urlparse(redirect_location)
        query_string = six.moves.urllib.parse.parse_qs(parsed.query)
        client_id = query_string["client_id"][0]

        response_id_token = id_token.fetch_id_token(
            AuthRequest(), client_id or os.environ.get("MLFLOW_OAUTH2_CLIENT_ID", "")
        )
        return response_id_token
    except Exception as e:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(e)
        logging.warning("Proceeding without authentication")

def fetch_mlflow_token(func):
    """Refetch IAP ID Token before executing the func"""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        os.environ["MLFLOW_TRACKING_TOKEN"] = get_token(os.environ["MLFLOW_TRACKING_URI"])
        return func(*args, **kwargs)
    return wrapper_decorator


class IdentityAwareProxyPluginRequestHeaderProvider(RequestHeaderProvider):
    """
    Provides request headers indicating the type of Identity Aware Proxy environment from which a request
    was made.
    """

    def in_context(self):
        if "MLFLOW_TRACKING_URI" in os.environ:
            print(f"### in_context: detected MLFLOW_TRACKING_URI: {MLFLOW_TRACKING_URI}")
            return True
        else:
            print(f"### in_context: 404 in_context: NO MLFLOW_TRACKING_URI ...")
            return False

    def request_headers(self):
        request_headers = {}
        if "MLFLOW_TRACKING_URI" in os.environ:
            print(f"### request_headers: detected MLFLOW_TRACKING_URI: {MLFLOW_TRACKING_URI}")
            request_headers["MLFLOW_TRACKING_TOKEN"] = get_token(os.environ["MLFLOW_TRACKING_URI"])
        else:
            print(f"### request_headers: 404 in_context: NO MLFLOW_TRACKING_URI ...")

        return request_headers
