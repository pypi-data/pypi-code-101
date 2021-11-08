import binascii
import filetype
import io
import json
import logging
from base64 import b64encode, b64decode
from datetime import datetime
from functools import singledispatch
from pathlib import Path
from json.decoder import JSONDecodeError
from typing import Any, Callable, Dict, List, Optional, Sequence, Union
from urllib.parse import urlparse

import requests
from backoff import expo, on_exception  # type: ignore
from requests.exceptions import RequestException

from .credentials import Credentials, guess_credentials


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
logger.addHandler(handler)

Content = Union[bytes, bytearray, str, Path, io.IOBase]
Queryparam = Union[str, List[str]]


def dictstrip(d):
    """Given a dict, return the dict with keys mapping to falsey values removed."""
    return {k: v for k, v in d.items() if v}


def _fatal_code(e):
    return 400 <= e.response.status_code < 500


def _json_decode(response):
    try:
        response.raise_for_status()
        return response.json()
    except JSONDecodeError as e:

        if response.status_code == 204:
            return {'Your request executed successfully': '204'}

        logger.error('Status code {} body:\n{}'.format(response.status_code, response.text))
        raise e
    except Exception as e:
        logger.error('Status code {} body:\n{}'.format(response.status_code, response.text))

        if response.status_code == 403 and 'Forbidden' in response.json().values():
            raise InvalidCredentialsException('Credentials provided are not valid.')

        if response.status_code == 429 and 'Too Many Requests' in response.json().values():
            raise TooManyRequestsException('You have reached the limit of requests per second.')

        if response.status_code == 429 and 'Limit Exceeded' in response.json().values():
            raise LimitExceededException('You have reached the limit of total requests per month.')

        raise e


def _guess_content_type(raw):
    guessed_type = filetype.guess(raw)
    assert guessed_type, 'Could not determine content type of document. ' \
                         'Please provide it by specifying content_type'
    return guessed_type.mime


@singledispatch
def parse_content(content, find_content_type=False):
    raise TypeError(
        '\n'.join([
            f'Could not parse content {content} of type {type(content)}',
            'Specify content by using one of the options below:',
            '1. Path to a file either as a string or as a Path object',
            '2. Bytes object with b64encoding',
            '3. Bytes object without b64encoding',
            '4. IO Stream of either bytes or text',
        ])
    )


@parse_content.register(str)
@parse_content.register(Path)
def _(content, find_content_type=False):
    raw = Path(content).read_bytes()
    content_type = _guess_content_type(raw) if find_content_type else None
    return b64encode(raw).decode(), content_type


@parse_content.register(bytes)
@parse_content.register(bytearray)
def _(content, find_content_type=False):
    try:
        raw = b64decode(content, validate=True)
    except binascii.Error:
        raw = content
    content_type = _guess_content_type(raw) if find_content_type else None
    return b64encode(raw).decode(), content_type


@parse_content.register(io.IOBase)
def _(content, find_content_type=False):
    raw = content.read()
    raw = raw.encode() if isinstance(raw, str) else raw
    content_type = _guess_content_type(raw) if find_content_type else None
    return b64encode(raw).decode(), content_type


class ClientException(Exception):
    """A ClientException is raised if the client refuses to
    send request due to incorrect usage or bad request data."""
    pass


class InvalidCredentialsException(ClientException):
    """An InvalidCredentialsException is raised if api key, access key id or secret access key is invalid."""
    pass


class TooManyRequestsException(ClientException):
    """A TooManyRequestsException is raised if you have reached the number of requests per second limit
    associated with your credentials."""
    pass


class LimitExceededException(ClientException):
    """A LimitExceededException is raised if you have reached the limit of total requests per month
    associated with your credentials."""
    pass


class FileFormatException(ClientException):
    """A FileFormatException is raised if the file format is not supported by the api."""
    pass


class Client:
    """A low level client to invoke api methods from Lucidtech AI Services."""
    def __init__(self, credentials: Optional[Credentials] = None):
        """:param credentials: Credentials to use, instance of :py:class:`~las.Credentials`
        :type credentials: Credentials"""
        self.credentials = credentials or guess_credentials()
        self.endpoint = self.credentials.api_endpoint

    @on_exception(expo, TooManyRequestsException, max_tries=4)
    @on_exception(expo, RequestException, max_tries=3, giveup=_fatal_code)
    def _make_request(
        self,
        requests_fn: Callable,
        signing_path: str,
        body: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> Dict:
        """Make signed headers, use them to make a HTTP request of arbitrary form and return the result
        as decoded JSON. Optionally pass a payload to JSON-dump and parameters for the request call."""

        kwargs = {'params': params}
        None if body is None else kwargs.update({'data': json.dumps(body)})
        uri = urlparse(f'{self.endpoint}{signing_path}')
        headers = {
            'Authorization': f'Bearer {self.credentials.access_token}',
            'Content-Type': 'application/json',
        }
        response = requests_fn(
            url=uri.geturl(),
            headers=headers,
            **kwargs,
        )
        return _json_decode(response)

    def create_app_client(
        self,
        generate_secret=True,
        logout_urls=None,
        callback_urls=None,
        login_urls=None,
        default_login_url=None,
        **optional_args
    ) -> Dict:
        """Creates an appClient, calls the POST /appClients endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.create_app_client(name='<name>', description='<description>')

        :param name: Name of the appClient
        :type name: str, optional
        :param description: Description of the appClient
        :type description: str, optional
        :param generate_secret: Set to False to ceate a Public app client, default: True
        :type generate_secret: Boolean
        :param logout_urls: List of logout urls
        :type logout_urls: List[str]
        :param callback_urls: List of callback urls
        :type callback_urls: List[str]
        :param login_urls: List of login urls
        :type login_urls: List[str]
        :param default_login_url: Default login url
        :type default_login_url: str
        :return: AppClient response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'logoutUrls': logout_urls,
            'callbackUrls': callback_urls,
            'loginUrls': login_urls,
            'defaultLoginUrl': default_login_url,
            **optional_args,
        })
        body['generateSecret'] = generate_secret
        return self._make_request(requests.post, '/appClients', body=body)

    def list_app_clients(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List appClients available, calls the GET /appClients endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_app_clients()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: AppClients response from REST API without the content of each appClient
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/appClients', params=params)

    def update_app_client(self, app_client_id, **optional_args) -> Dict:
        """Updates an appClient, calls the PATCH /appClients/{appClientId} endpoint.

        :param app_client_id: Id of the appClient
        :type app_client_id: str
        :param name: Name of the appClient
        :type name: str, optional
        :param description: Description of the appClient
        :type description: str, optional
        :return: AppClient response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.patch, f'/appClients/{app_client_id}', body=optional_args)

    def delete_app_client(self, app_client_id: str) -> Dict:
        """Delete the appClient with the provided appClientId, calls the DELETE /appClients/{appClientId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_app_client('<app_client_id>')

        :param app_client_id: Id of the appClient
        :type app_client_id: str
        :return: AppClient response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/appClients/{app_client_id}')

    def create_asset(self, content: Content, **optional_args) -> Dict:
        """Creates an asset, calls the POST /assets endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.create_asset(b'<bytes data>')

        :param content: Content to POST
        :type content: Content
        :param name: Name of the asset
        :type name: str, optional
        :param description: Description of the asset
        :type description: str, optional
        :return: Asset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        content, _ = parse_content(content)
        body = {
            'content': content,
            **optional_args,
        }
        return self._make_request(requests.post, '/assets', body=body)

    def list_assets(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List assets available, calls the GET /assets endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_assets()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Assets response from REST API without the content of each asset
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/assets', params=params)

    def get_asset(self, asset_id: str) -> Dict:
        """Get asset, calls the GET /assets/{assetId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_asset(asset_id='<asset id>')

        :param asset_id: Id of the asset
        :type asset_id: str
        :return: Asset response from REST API with content
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/assets/{asset_id}')

    def update_asset(self, asset_id: str, **optional_args) -> Dict:
        """Updates an asset, calls the PATCH /assets/{assetId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.update_asset('<asset id>', content=b'<bytes data>')

        :param asset_id: Id of the asset
        :type asset_id: str
        :param content: Content to PATCH
        :type content: Content, optional
        :param name: Name of the asset
        :type name: str, optional
        :param description: Description of the asset
        :type description: str, optional
        :return: Asset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        content = optional_args.get('content')

        if content:
            parsed_content, _ = parse_content(content)
            optional_args['content'] = parsed_content

        return self._make_request(requests.patch, f'/assets/{asset_id}', body=optional_args)

    def delete_asset(self, asset_id: str) -> Dict:
        """Delete the asset with the provided asset_id, calls the DELETE /assets/{assetId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_asset('<asset_id>')

        :param asset_id: Id of the asset
        :type asset_id: str
        :return: Asset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/assets/{asset_id}')

    def create_dataset(self, **optional_args) -> Dict:
        """Creates a dataset, calls the POST /datasets endpoint.

        :param name: Name of the dataset
        :type name: str, optional
        :param description: Description of the dataset
        :type description: str, optional
        :return: Dataset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.post, '/datasets', body=optional_args)

    def list_datasets(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List datasets available, calls the GET /datasets endpoint.

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Datasets response from REST API without the content of each dataset
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/datasets', params=params)

    def get_dataset(self, dataset_id: str) -> Dict:
        """Get dataset, calls the GET /datasets/{datasetId} endpoint.

        :param dataset_id: Id of the dataset
        :type dataset_id: str
        :return: Dataset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/datasets/{dataset_id}')

    def update_dataset(self, dataset_id, **optional_args) -> Dict:
        """Updates a dataset, calls the PATCH /datasets/{datasetId} endpoint.

        :param dataset_id: Id of the dataset
        :type dataset_id: str
        :param name: Name of the dataset
        :type name: str, optional
        :param description: Description of the dataset
        :type description: str, optional
        :return: Dataset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.patch, f'/datasets/{dataset_id}', body=optional_args)

    def delete_dataset(self, dataset_id: str, delete_documents: bool = False) -> Dict:
        """Delete the dataset with the provided dataset_id, calls the DELETE /datasets/{datasetId} endpoint.

        :param dataset_id: Id of the dataset
        :type dataset_id: str
        :param delete_documents: Set to true to delete documents in dataset before deleting dataset
        :type delete_documents: bool
        :return: Dataset response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        if delete_documents:
            self.delete_documents(dataset_id=dataset_id, delete_all=True)

        return self._make_request(requests.delete, f'/datasets/{dataset_id}')

    def create_document(
        self,
        content: Content,
        content_type: str = None,
        *,
        consent_id: Optional[str] = None,
        dataset_id: str = None,
        ground_truth: Sequence[Dict[str, str]] = None,
        retention_in_days: int = None,
    ) -> Dict:
        """Creates a document, calls the POST /documents endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.create_document(b'<bytes data>', 'image/jpeg', consent_id='<consent id>')

        :param content: Content to POST
        :type content: Content
        :param content_type: MIME type for the document
        :type content_type: str
        :param consent_id: Id of the consent that marks the owner of the document
        :type consent_id: str, optional
        :param dataset_id: Id of the associated dataset
        :type dataset_id: str, optional
        :param ground_truth: List of items {'label': label, 'value': value} \
            representing the ground truth values for the document
        :type ground_truth: Sequence [ Dict [ str, Union [ str, bool ]  ] ], optional
        :return: Document response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        content_bytes, guessed_content_type = parse_content(content, True)

        if content_type and content_type != guessed_content_type:
            logger.warning(f'The specified content type does not match the observed content type:'
                           f' {content_type} != {guessed_content_type}')

        body = {
            'content': content_bytes,
            'contentType': content_type or guessed_content_type,
            'consentId': consent_id,
            'datasetId': dataset_id,
            'groundTruth': ground_truth,
            'retentionInDays': retention_in_days,
        }
        return self._make_request(requests.post, '/documents', body=dictstrip(body))

    def list_documents(
        self,
        *,
        consent_id: Optional[Queryparam] = None,
        dataset_id: Optional[Queryparam] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> Dict:
        """List documents available for inference, calls the GET /documents endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_documents(consent_id='<consent_id>')

        :param consent_id: Ids of the consents that marks the owner of the document
        :type consent_id: Queryparam, optional
        :param dataset_id: Ids of datasets that contains the documents of interest
        :type dataset_id: Queryparam, optional
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Documents response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'consentId': consent_id,
            'datasetId': dataset_id,
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/documents', params=params)

    def delete_documents(
        self,
        *,
        consent_id: Optional[Queryparam] = None,
        dataset_id: Optional[Queryparam] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        delete_all: Optional[bool] = False,
    ) -> Dict:
        """Delete documents with the provided consent_id, calls the DELETE /documents endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_documents(consent_id='<consent id>')

        :param consent_id: Ids of the consents that marks the owner of the document
        :type consent_id: Queryparam, optional
        :param dataset_id: Ids of the datasets to be deleted
        :type dataset_id: Queryparam, optional
        :param max_results: Maximum number of documents that will be deleted
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :param delete_all: Delete all documents that match the given parameters doing multiple API calls if necessary. \
            Will throw an error if parameter max_results is also specified.
        :type delete_all: bool, optional
        :return: Documents response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = dictstrip({
            'consentId': consent_id,
            'datasetId': dataset_id,
            'nextToken': next_token,
            'maxResults': max_results,
        })

        if delete_all and max_results:
            raise ValueError('Cannot specify max results when delete_all=True')

        response = self._make_request(requests.delete, '/documents', params=params)

        if delete_all:
            params['nextToken'] = response['nextToken']

            while params['nextToken']:
                intermediate_response = self._make_request(requests.delete, '/documents', params=params)
                response['documents'].extend(intermediate_response.get('documents'))
                params['nextToken'] = intermediate_response['nextToken']
                logger.info(f'Deleted {len(response["documents"])} documents so far')

        return response

    def get_document(self, document_id: str) -> Dict:
        """Get document, calls the GET /documents/{documentId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_document('<document id>')

        :param document_id: Id of the document
        :type document_id: str
        :return: Document response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/documents/{document_id}')

    def update_document(
        self,
        document_id: str,
        ground_truth: Sequence[Dict[str, Union[Optional[str], bool]]] = None, # For backwards compatibility reasons, this is placed before the *
        *,
        dataset_id: str = None,
    ) -> Dict:
        """Update ground truth for a document, calls the PATCH /documents/{documentId} endpoint.
        Updating ground truth means adding the ground truth data for the particular document.
        This enables the API to learn from past mistakes.

        :param document_id: Id of the document
        :type document_id: str
        :param dataset_id: Id of the dataset you want to associate your document with
        :type dataset_id: str, optional
        :param ground_truth: List of items {label: value} representing the ground truth values for the document
        :type ground_truth: Sequence [ Dict [ str, Union [ str, bool ]  ] ], optional
        :return: Document response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = {
            'groundTruth': ground_truth,
            'datasetId': dataset_id,
        }
        return self._make_request(requests.patch, f'/documents/{document_id}', body=dictstrip(body))

    def delete_document(self, document_id: str) -> Dict:
        """Delete the document with the provided document_id, calls the DELETE /documents/{documentId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_document('<document_id>')

        :param document_id: Id of the document
        :type document_id: str
        :return: Model response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/documents/{document_id}')

    def list_logs(
        self,
        *,
        workflow_id: Optional[str] = None,
        workflow_execution_id: Optional[str] = None,
        transition_id: Optional[str] = None,
        transition_execution_id: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> Dict:
        """List logs, calls the GET /logs endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_logs()

        :param workflow_id: Only show logs from this workflow
        :type workflow_id: str, optional
        :param workflow_execution_id: Only show logs from this workflow execution
        :type workflow_execution_id: str, optional
        :param transition_id: Only show logs from this transition
        :type transition_id: str, optional
        :param transition_execution_id: Only show logs from this transition execution
        :type transition_execution_id: str, optional
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Logs response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = '/logs'
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
            'workflowId': workflow_id,
            'workflowExecutionId': workflow_execution_id,
            'transitionId': transition_id,
            'transitionExecutionId': transition_execution_id,
        }

        return self._make_request(requests.get, url, params=dictstrip(params))

    def get_log(self, log_id) -> Dict:
        """get log, calls the GET /logs/{logId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_log('<log_id>')

        :param log_id: Id of the log
        :type log_id: str
        :return: Log response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/logs/{log_id}')

    def create_model(
        self,
        width: int,
        height: int,
        field_config: dict,
        *,
        preprocess_config: Optional[dict] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **optional_args,
    ) -> Dict:
        """Creates a model, calls the POST /models endpoint.

        :param width: The number of pixels to be used for the input image width of your model
        :type width: int
        :param height: The number of pixels to be used for the input image height of your model
        :type height: int
        :param field_config: Specification of the fields that the model is going to predict
        :type field_config: dict
        :param preprocess_config: Specification of the processing steps prior to the prediction of an image
        :type preprocess_config: dict
        :param name: Name of the model
        :type name: str, optionalQ
        :param description: Description of the model
        :type description: str, optional
        :return: Model response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'width': width,
            'height': height,
            'fieldConfig': field_config,
            'preprocessConfig': preprocess_config,
            'name': name,
            'description': description,
        })
        body.update(**optional_args)
        return self._make_request(requests.post, '/models', body=body)

    def list_models(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List models available, calls the GET /models endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_models()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Models response from REST API without the content of each model
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/models', params=params)

    def get_model(self, model_id: str) -> Dict:
        """Get a model, calls the GET /models/{modelId} endpoint.

        :param model_id: The Id of the model
        :type model_id: str
        :return: Model response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/models/{model_id}')

    def update_model(
        self,
        model_id: str,
        *,
        width: Optional[int] = None,
        height: Optional[int] = None,
        field_config: Optional[dict] = None,
        preprocess_config: Optional[dict] = None,
        status: Optional[str] = None,
        **optional_args,
    ) -> Dict:
        """Updates a model, calls the PATCH /models/{modelId} endpoint.

        :param model_id: The Id of the model
        :type model_id: str, optional
        :param width: The number of pixels to be used for the input image width of your model
        :type width: int, optional
        :param height: The number of pixels to be used for the input image height of your model
        :type height: int, optional
        :param field_config: Specification of the fields that the model is going to predict
        :type field_config: dict
        :param preprocess_config: Specification of the processing steps prior to the prediction of an image
        :type preprocess_config: dict
        :param status: New status for the model
        :type status: str, optional
        :param name: Name of the model
        :type name: str, optional
        :param description: Description of the model
        :type description: str, optional
        :return: Model response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'width': width,
            'height': height,
            'fieldConfig': field_config,
            'preprocessConfig': preprocess_config,
            'status': status,
        })
        body.update(**optional_args)
        return self._make_request(requests.patch, f'/models/{model_id}', body=body)

    def delete_model(self, model_id: str) -> Dict:
        """Delete the model with the provided model_id, calls the DELETE /models/{modelId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_model('<model_id>')

        :param model_id: Id of the model
        :type model_id: str
        :return: Model response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/models/{model_id}')

    def create_data_bundle(self, model_id, dataset_ids, **optional_args) -> Dict:
        """Creates a data bundle, calls the POST /models/{modelId}/dataBundles endpoint.

        :param model_id: Id of the model
        :type model_id: str
        :param dataset_ids: Dataset Ids that will be included in the data bundle
        :type dataset_ids: List[str]
        :param name: Name of the data bundle
        :type name: str, optional
        :param description: Description of the data bundle
        :type description: str, optional
        :return: Data Bundle response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """

        body = {'datasetIds': dataset_ids}
        body.update(**optional_args)
        return self._make_request(requests.post, f'/models/{model_id}/dataBundles', body=body)

    def list_data_bundles(
        self,
        model_id,
        *,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> Dict:
        """List data bundles available, calls the GET /models/{modelId}/dataBundles endpoint.

        :param model_id: Id of the model
        :type model_id: str
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Data Bundles response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, f'/models/{model_id}/dataBundles', params=params)

    def update_data_bundle(
        self,
        model_id: str,
        data_bundle_id: str,
        **optional_args,
    ) -> Dict:
        """Updates a data bundle, calls the PATCH /models/{modelId}/dataBundles/{dataBundleId} endpoint.

        :param model_id: Id of the model
        :type model_id: str
        :param data_bundle_id: Id of the data bundle
        :type data_bundle_id: str
        :param name: Name of the data bundle
        :type name: str, optional
        :param description: Description of the data bundle
        :type description: str, optional
        :return: Data Bundle response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.patch, f'/models/{model_id}/dataBundles/{data_bundle_id}', body=optional_args)

    def delete_data_bundle(self, model_id: str, data_bundle_id: str) -> Dict:
        """Delete the data bundle with the provided data_bundle_id,
        calls the DELETE /models/{modelId}/dataBundles/{dataBundleId} endpoint.

        :param model_id: Id of the model
        :type model_id: str
        :param data_bundle_id: Id of the data bundle
        :type data_bundle_id: str
        :return: Data Bundle response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/models/{model_id}/dataBundles/{data_bundle_id}')

    def get_organization(self, organization_id: str) -> Dict:
        """Get an organization, calls the GET /organizations/{organizationId} endpoint.

        :param organization_id: The Id of the organization
        :type organization_id: str
        :return: Organization response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/organizations/{organization_id}')

    def update_organization(
        self,
        organization_id: str,
        **optional_args,
    ) -> Dict:
        """Updates an organization, calls the PATCH /organizations/{organizationId} endpoint.

        :param organization_id: The Id of the organization
        :type organization_id: str, optional
        :param name: Name of the organization
        :type name: str, optional
        :param description: Description of the organization
        :type description: str, optional
        :return: Organization response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.patch, f'/organizations/{organization_id}', body=optional_args)

    def create_prediction(
        self,
        document_id: str,
        model_id: str,
        *,
        max_pages: Optional[int] = None,
        auto_rotate: Optional[bool] = None,
        image_quality: Optional[str] = None,
        postprocess_config: Optional[dict] = None,
    ) -> Dict:
        """Create a prediction on a document using specified model, calls the POST /predictions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.create_prediction(document_id='<document id>', model_id='<model id>')

        :param document_id: Id of the document to run inference and create a prediction on
        :type document_id: str
        :param model_id: Id of the model to use for inference
        :type model_id: str
        :param max_pages: Maximum number of pages to run predictions on
        :type max_pages: int, optional
        :param auto_rotate: Whether or not to let the API try different rotations on\
            the document when running predictions
        :type auto_rotate: bool, optional
        :param image_quality: Image quality for prediction "LOW|HIGH". \
            high quality could give better result but will also take longer time.
        :type image_quality: int, optional
        :param postprocess_config: Post processing configuration for prediction.
            {
                'strategy': 'BEST_FIRST' | 'BEST_N_PAGES',  (required)
                'parameters': {                             (required if strategy=BEST_N_PAGES, omit otherwise)
                    'n': int,                               (required if strategy=BEST_N_PAGES, omit otherwise)
                    'collapse': True | False                (optional if strategy=BEST_N_PAGES, omit otherwise)
                }
            }
            Examples:
            {'strategy': 'BEST_FIRST'}
            {'strategy': 'BEST_N_PAGES', 'parameters': {'n': 3}}
            {'strategy': 'BEST_N_PAGES', 'parameters': {'n': 3, 'collapse': False}}
        :type postprocess_config: dict, optional
        :return: Prediction response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = {
            'documentId': document_id,
            'modelId': model_id,
            'maxPages': max_pages,
            'autoRotate': auto_rotate,
            'imageQuality': image_quality,
            'postprocessConfig': postprocess_config,
        }
        return self._make_request(requests.post, '/predictions', body=dictstrip(body))

    def list_predictions(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List predictions available, calls the GET /predictions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_predictions()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Predictions response from REST API without the content of each prediction
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/predictions', params=params)

    def create_secret(self, data: dict, **optional_args) -> Dict:
        """Creates an secret, calls the POST /secrets endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> data = {'username': '<username>', 'password': '<password>'}
        >>> client.create_secret(data, description='<description>')

        :param data: Dict containing the data you want to keep secret
        :type data: str
        :param name: Name of the secret
        :type name: str, optional
        :param description: Description of the secret
        :type description: str, optional
        :return: Secret response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = {
            'data': data,
            **optional_args,
        }
        return self._make_request(requests.post, '/secrets', body=body)

    def list_secrets(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List secrets available, calls the GET /secrets endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_secrets()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Secrets response from REST API without the username of each secret
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/secrets', params=params)

    def update_secret(self, secret_id: str, *, data: Optional[dict] = None, **optional_args) -> Dict:
        """Updates an secret, calls the PATCH /secrets/secretId endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> data = {'username': '<username>', 'password': '<password>'}
        >>> client.update_secret('<secret id>', data, description='<description>')

        :param secret_id: Id of the secret
        :type secret_id: str
        :param data: Dict containing the data you want to keep secret
        :type data: dict, optional
        :param name: Name of the secret
        :type name: str, optional
        :param description: Description of the secret
        :type description: str, optional
        :return: Secret response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({'data': data})
        body.update(**optional_args)
        return self._make_request(requests.patch, f'/secrets/{secret_id}', body=body)

    def delete_secret(self, secret_id: str) -> Dict:
        """Delete the secret with the provided secret_id, calls the DELETE /secrets/{secretId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_secret('<secret_id>')

        :param secret_id: Id of the secret
        :type secret_id: str
        :return: Secret response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/secrets/{secret_id}')

    def create_transition(
        self,
        transition_type: str,
        *,
        in_schema: Optional[dict] = None,
        out_schema: Optional[dict] = None,
        parameters: Optional[dict] = None,
        **optional_args,
    ) -> Dict:
        """Creates a transition, calls the POST /transitions endpoint.

        >>> import json
        >>> from pathlib import Path
        >>> from las.client import Client
        >>> client = Client()
        >>> in_schema = {'$schema': 'https://json-schema.org/draft-04/schema#', 'title': 'in', 'properties': {...} }
        >>> out_schema = {'$schema': 'https://json-schema.org/draft-04/schema#', 'title': 'out', 'properties': {...} }
        >>> # A typical docker transition
        >>> docker_params = {
        >>>     'imageUrl': '<image_url>',
        >>>     'credentials': {'username': '<username>', 'password': '<password>'}
        >>> }
        >>> client.create_transition('docker', in_schema=in_schema, out_schema=out_schema, params=docker_params)
        >>> # A manual transition with UI
        >>> assets = {'jsRemoteComponent': 'las:asset:<hex-uuid>', '<other asset name>': 'las:asset:<hex-uuid>'}
        >>> manual_params = {'assets': assets}
        >>> client.create_transition('manual', in_schema=in_schema, out_schema=out_schema, params=manual_params)

        :param transition_type: Type of transition "docker"|"manual"
        :type transition_type: str
        :param in_schema: Json-schema that defines the input to the transition
        :type in_schema: dict, optional
        :param out_schema: Json-schema that defines the output of the transition
        :type out_schema: dict, optional
        :param name: Name of the transition
        :type name: str, optional
        :param parameters: Parameters to the corresponding transition type
        :type parameters: dict, optional
        :param description: Description of the transition
        :type description: str, optional
        :return: Transition response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'inputJsonSchema': in_schema,
            'outputJsonSchema': out_schema,
            'transitionType': transition_type,
            'parameters': parameters,
        })
        body.update(**optional_args)
        return self._make_request(requests.post, '/transitions', body=body)

    def list_transitions(
        self,
        *,
        transition_type: Optional[Queryparam] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> Dict:
        """List transitions, calls the GET /transitions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_transitions('<transition_type>')

        :param transition_type: Types of transitions
        :type transition_type: Queryparam, optional
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Transitions response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = '/transitions'
        params = {
            'transitionType': transition_type,
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, url, params=dictstrip(params))

    def get_transition(self, transition_id: str) -> Dict:
        """Get the transition with the provided transition_id, calls the GET /transitions/{transitionId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_transition('<transition_id>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :return: Transition response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/transitions/{transition_id}')

    def update_transition(
        self,
        transition_id: str,
        *,
        in_schema: Optional[dict] = None,
        out_schema: Optional[dict] = None,
        assets: Optional[dict] = None,
        environment: Optional[dict] = None,
        environment_secrets: Optional[list] = None,
        **optional_args,
    ) -> Dict:
        """Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.

        >>> import json
        >>> from pathlib import Path
        >>> from las.client import Client
        >>> client = Client()
        >>> client.update_transition('<transition-id>', name='<name>', description='<description>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :param name: Name of the transition
        :type name: str, optional
        :param description: Description of the transition
        :type description: str, optional
        :param in_schema: Json-schema that defines the input to the transition
        :type in_schema: dict, optional
        :param out_schema: Json-schema that defines the output of the transition
        :type out_schema: dict, optional
        :param assets: A dictionary where the values are assetIds that can be used in a manual transition
        :type assets: dict, optional
        :param environment: Environment variables to use for a docker transition
        :type environment: dict, optional
        :param environment_secrets: \
            A list of secretIds that contains environment variables to use for a docker transition
        :type environment_secrets: list, optional
        :return: Transition response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'inputJsonSchema': in_schema,
            'outputJsonSchema': out_schema,
            'assets': assets,
            'environment': environment,
            'environmentSecrets': environment_secrets,
        })
        body.update(**optional_args)
        return self._make_request(requests.patch, f'/transitions/{transition_id}', body=body)

    def execute_transition(self, transition_id: str) -> Dict:
        """Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.execute_transition('<transition_id>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :return: Transition execution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        endpoint = f'/transitions/{transition_id}/executions'
        return self._make_request(requests.post, endpoint, body={})

    def delete_transition(self, transition_id: str) -> Dict:
        """Delete the transition with the provided transition_id, calls the DELETE /transitions/{transitionId} endpoint.
           Will fail if transition is in use by one or more workflows.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_transition('<transition_id>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :return: Transition response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/transitions/{transition_id}')

    def list_transition_executions(
        self,
        transition_id: str,
        *,
        status: Optional[Queryparam] = None,
        execution_id: Optional[Queryparam] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = None,
    ) -> Dict:
        """List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_transition_executions('<transition_id>', '<status>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :param status: Statuses of the executions
        :type status: Queryparam, optional
        :param order: Order of the executions, either 'ascending' or 'descending'
        :type order: str, optional
        :param sort_by: the sorting variable of the executions, either 'endTime', or 'startTime'
        :type sort_by: str, optional
        :param execution_id: Ids of the executions
        :type execution_id: Queryparam, optional
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Transition executions responses from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = f'/transitions/{transition_id}/executions'
        params = {
            'status': status,
            'executionId': execution_id,
            'maxResults': max_results,
            'nextToken': next_token,
            'order': order,
            'sortBy': sort_by,
        }
        return self._make_request(requests.get, url, params=dictstrip(params))

    def get_transition_execution(self, transition_id: str, execution_id: str) -> Dict:
        """Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_transition_execution('<transition_id>', '<execution_id>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :param execution_id: Id of the executions
        :type execution_id: str
        :return: Transition execution responses from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = f'/transitions/{transition_id}/executions/{execution_id}'
        return self._make_request(requests.get, url)

    def update_transition_execution(
        self,
        transition_id: str,
        execution_id: str,
        status: str,
        *,
        output: Optional[dict] = None,
        error: Optional[dict] = None,
        start_time: Optional[Union[str, datetime]] = None,
    ) -> Dict:
        """Ends the processing of the transition execution,
        calls the PATCH /transitions/{transition_id}/executions/{execution_id} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> output = {...}
        >>> client.update_transition_execution('<transition_id>', '<execution_id>', 'succeeded', output)
        >>> error = {"message": 'The execution could not be processed due to ...'}
        >>> client.update_transition_execution('<transition_id>', '<execution_id>', 'failed', error)

        :param transition_id: Id of the transition that performs the execution
        :type transition_id: str
        :param execution_id: Id of the execution to update
        :type execution_id: str
        :param status: Status of the execution 'succeeded|failed'
        :type status: str
        :param output: Output from the execution, required when status is 'succeded'
        :type output: dict, optional
        :param error: Error from the execution, required when status is 'failed', needs to contain 'message'
        :type error: dict, optional
        :param start_time: start time that will replace the original start time of the execution
        :type start_time: str, optional
        :return: Transition execution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        if isinstance(start_time, datetime):
            if not start_time.tzinfo:
                start_time = start_time.astimezone()
            start_time = start_time.isoformat()

        url = f'/transitions/{transition_id}/executions/{execution_id}'
        body = {
            'status': status,
            'output': output,
            'error': error,
            'startTime': start_time,
        }
        return self._make_request(requests.patch, url, body=dictstrip(body))

    def send_heartbeat(self, transition_id: str, execution_id: str) -> Dict:
        """Send heartbeat for a manual execution to signal that we are still working on it.
        Must be done at minimum once every 60 seconds or the transition execution will time out,
        calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.send_heartbeat('<transition_id>', '<execution_id>')

        :param transition_id: Id of the transition
        :type transition_id: str
        :param execution_id: Id of the transition execution
        :type execution_id: str
        :return: Empty response
        :rtype: None

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        endpoint = f'/transitions/{transition_id}/executions/{execution_id}/heartbeats'
        return self._make_request(requests.post, endpoint, body={})

    def create_user(self, email: str, *, app_client_id, **optional_args) -> Dict:
        """Creates a new user, calls the POST /users endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.create_user('<email>', name='John Doe')

        :param email: Email to the new user
        :type email: str
        :param name: Name of the user
        :type name: str, optional
        :param avatar: base64 encoded JPEG avatar of the user
        :type avatar: str, optional
        :return: User response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = {
            'email': email,
            'appClientId': app_client_id,
            **optional_args,
        }
        return self._make_request(requests.post, '/users', body=dictstrip(body))

    def list_users(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List users, calls the GET /users endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_users()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Users response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/users', params=params)

    def get_user(self, user_id: str) -> Dict:
        """Get information about a specific user, calls the GET /users/{user_id} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_user('<user_id>')

        :param user_id: Id of the user
        :type user_id: str
        :return: User response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/users/{user_id}')

    def update_user(self, user_id: str, **optional_args) -> Dict:
        """Updates a user, calls the PATCH /users/{userId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.update_user('<user id>', name='John Doe')

        :param user_id: Id of the user
        :type user_id: str
        :param name: Name of the user
        :type name: str, optional
        :param avatar: base64 encoded JPEG avatar of the user
        :type avatar: str, optional
        :return: User response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """

        return self._make_request(requests.patch, f'/users/{user_id}', body=optional_args)

    def delete_user(self, user_id: str) -> Dict:
        """Delete the user with the provided user_id, calls the DELETE /users/{userId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_user('<user_id>')

        :param user_id: Id of the user
        :type user_id: str
        :return: User response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/users/{user_id}')

    def create_workflow(
        self,
        specification: dict,
        *,
        error_config: Optional[dict] = None,
        completed_config: Optional[dict] = None,
        **optional_args,
    ) -> Dict:
        """Creates a new workflow, calls the POST /workflows endpoint.
        Check out Lucidtech's tutorials for more info on how to create a workflow.

        >>> from las.client import Client
        >>> from pathlib import Path
        >>> client = Client()
        >>> specification = {'language': 'ASL', 'version': '1.0.0', 'definition': {...}}
        >>> error_config = {'email': '<error-recipient>'}
        >>> client.create_workflow(specification, error_config=error_config)

        :param specification: Specification of the workflow, \
            currently supporting ASL: https://states-language.net/spec.html
        :type specification: dict
        :param name: Name of the workflow
        :type name: str, optional
        :param description: Description of the workflow
        :type description: str, optional
        :param error_config: Configuration of error handler
        :type error_config: dict, optional
        :param completed_config: Configuration of a job to run whenever a workflow execution ends
        :type completed_config: dict, optional
        :return: Workflow response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'specification': specification,
            'errorConfig': error_config,
            'completedConfig': completed_config,
        })
        body.update(**optional_args)

        return self._make_request(requests.post, '/workflows', body=body)

    def list_workflows(self, *, max_results: Optional[int] = None, next_token: Optional[str] = None) -> Dict:
        """List workflows, calls the GET /workflows endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_workflows()

        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Workflows response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        params = {
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, '/workflows', params=params)

    def get_workflow(self, workflow_id: str) -> Dict:
        """Get the workflow with the provided workflow_id, calls the GET /workflows/{workflowId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_workflow('<workflow_id>')

        :param workflow_id: Id of the workflow
        :type workflow_id: str
        :return: Workflow response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.get, f'/workflows/{workflow_id}')

    def update_workflow(
        self,
        workflow_id: str,
        *,
        error_config: Optional[dict] = None,
        completed_config: Optional[dict] = None,
        **optional_args,
    ) -> Dict:
        """Updates a workflow, calls the PATCH /workflows/{workflowId} endpoint.

        >>> import json
        >>> from pathlib import Path
        >>> from las.client import Client
        >>> client = Client()
        >>> client.update_workflow('<workflow-id>', name='<name>', description='<description>')

        :param workflow_id: Id of the workflow
        :type name: str
        :param name: Name of the workflow
        :type name: str, optional
        :param description: Description of the workflow
        :type description: str, optional
        :param error_config: Configuration of error handler
        :type error_config: dict, optional
        :param completed_config: Configuration of a job to run whenever a workflow execution ends
        :type completed_config: dict, optional
        :return: Workflow response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        body = dictstrip({
            'errorConfig': error_config,
            'completedConfig': completed_config,
        })
        body.update(**optional_args)
        return self._make_request(requests.patch, f'/workflows/{workflow_id}', body=body)

    def delete_workflow(self, workflow_id: str) -> Dict:
        """Delete the workflow with the provided workflow_id, calls the DELETE /workflows/{workflowId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_workflow('<workflow_id>')

        :param workflow_id: Id of the workflow
        :type workflow_id: str
        :return: Workflow response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/workflows/{workflow_id}')

    def execute_workflow(self, workflow_id: str, content: dict) -> Dict:
        """Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

        >>> from las.client import Client
        >>> from pathlib import Path
        >>> client = Client()
        >>> content = {...}
        >>> client.execute_workflow('<workflow_id>', content)

        :param workflow_id: Id of the workflow
        :type workflow_id: str
        :param content: Input to the first step of the workflow
        :type content: dict
        :return: Workflow execution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        endpoint = f'/workflows/{workflow_id}/executions'
        return self._make_request(requests.post, endpoint, body={'input': content})

    def list_workflow_executions(
            self,
            workflow_id: str,
            *,
            status: Optional[Queryparam] = None,
            sort_by: Optional[str] = None,
            order: Optional[str] = None,
            max_results: Optional[int] = None,
            next_token: Optional[str] = None,
    ) -> Dict:
        """List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.list_workflow_executions('<workflow_id>', '<status>')

        :param workflow_id: Id of the workflow
        :type workflow_id: str
        :param order: Order of the executions, either 'ascending' or 'descending'
        :type order: str, optional
        :param sort_by: the sorting variable of the executions, either 'endTime', or 'startTime'
        :type sort_by: str, optional
        :param status: Statuses of the executions
        :type status: Queryparam, optional
        :param max_results: Maximum number of results to be returned
        :type max_results: int, optional
        :param next_token: A unique token for each page, use the returned token to retrieve the next page.
        :type next_token: str, optional
        :return: Workflow executions responses from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = f'/workflows/{workflow_id}/executions'
        params = {
            'status': status,
            'order': order,
            'sortBy': sort_by,
            'maxResults': max_results,
            'nextToken': next_token,
        }
        return self._make_request(requests.get, url, params=params)

    def get_workflow_execution(self, workflow_id: str, execution_id: str) -> Dict:
        """Get a workflow execution, calls the GET /workflows/{workflow_id}/executions/{execution_id} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.get_workflow_execution('<workflow_id>', '<execution_id>')

        :param workflow_id: Id of the workflow that performs the execution
        :type workflow_id: str
        :param execution_id: Id of the execution to get
        :type execution_id: str
        :return: Workflow execution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = f'/workflows/{workflow_id}/executions/{execution_id}'
        return self._make_request(requests.get, url)

    def update_workflow_execution(
        self,
        workflow_id: str,
        execution_id: str,
        next_transition_id: str,
    ) -> Dict:
        """Retry or end the processing of a workflow execution,
        calls the PATCH /workflows/{workflow_id}/executions/{execution_id} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.update_workflow_execution('<workflow_id>', '<execution_id>', '<next_transition_id>')

        :param workflow_id: Id of the workflow that performs the execution
        :type workflow_id: str
        :param execution_id: Id of the execution to update
        :type execution_id: str
        :param next_transition_id: the next transition to transition into, to end the workflow-execution, \
        use: las:transition:commons-failed
        :type next_transition_id: str
        :return: Workflow execution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        url = f'/workflows/{workflow_id}/executions/{execution_id}'
        body = {
            'nextTransitionId': next_transition_id,
        }
        return self._make_request(requests.patch, url, body=dictstrip(body))

    def delete_workflow_execution(self, workflow_id: str, execution_id: str) -> Dict:
        """Deletes the execution with the provided execution_id from workflow_id,
        calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

        >>> from las.client import Client
        >>> client = Client()
        >>> client.delete_workflow_execution('<workflow_id>', '<execution_id>')

        :param workflow_id: Id of the workflow
        :type workflow_id: str
        :param execution_id: Id of the execution
        :type execution_id: str
        :return: WorkflowExecution response from REST API
        :rtype: dict

        :raises: :py:class:`~las.InvalidCredentialsException`, :py:class:`~las.TooManyRequestsException`,\
 :py:class:`~las.LimitExceededException`, :py:class:`requests.exception.RequestException`
        """
        return self._make_request(requests.delete, f'/workflows/{workflow_id}/executions/{execution_id}')
