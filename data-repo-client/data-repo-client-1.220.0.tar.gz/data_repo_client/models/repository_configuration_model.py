# coding: utf-8

"""
    Data Repository API

    This document defines the REST API for Data Repository. **Status: design in progress** There are four top-level endpoints (besides some used by swagger):  * /swagger-ui.html - generated by swagger: swagger API page that provides this documentation and a live UI for      submitting REST requests  * /status - provides the operational status of the service  * /api    - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The overall API (/api) currently supports two interfaces:  * Repository - a general and default interface for initial setup, managing ingest and repository metadata  * Resource - an interface for managing billing accounts and resources  The API endpoints are organized by interface. Each interface is separately versioned. ## Notes on Naming All of the reference items are suffixed with \"Model\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. ## Editing and debugging I have found it best to edit this file directly to make changes and then use the swagger-editor to validate. The errors out of swagger-codegen are not that helpful. In the swagger-editor, it gives you nice errors and links to the place in the YAML where the errors are. But... the swagger-editor has been a bit of a pain for me to run. I tried the online website and was not able to load my YAML. Instead, I run it locally in a docker container, like this: ``` docker pull swaggerapi/swagger-editor docker run -p 9090:8080 swaggerapi/swagger-editor ``` Then navigate to localhost:9090 in your browser. I have not been able to get the file upload to work. It is a bit of a PITA, but I copy-paste the source code, replacing what is in the editor. Then make any fixes. Then copy-paste the resulting, valid file back into our source code. Not elegant, but easier than playing detective with the swagger-codegen errors. This might be something about my browser or environment, so give it a try yourself and see how it goes. ## Merging the DRS standard swagger into this swagger ## The merging is done in three sections:  1. Merging the security definitions into our security definitions  2. This section of paths. We make all paths explicit (prefixed with /ga4gh/drs/v1)     All standard DRS definitions and parameters are prefixed with 'DRS' to separate them     from our native definitions and parameters. We remove the x-swagger-router-controller lines.  3. A separate part of the definitions section for the DRS definitions  NOTE: the code here does not relect the DRS spec anymore. See DR-409.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class RepositoryConfigurationModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'client_id': 'str',
        'active_profiles': 'list[str]',
        'sem_ver': 'str',
        'git_hash': 'str',
        'terra_url': 'str',
        'sam_url': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'active_profiles': 'activeProfiles',
        'sem_ver': 'semVer',
        'git_hash': 'gitHash',
        'terra_url': 'terraUrl',
        'sam_url': 'samUrl'
    }

    def __init__(self, client_id=None, active_profiles=None, sem_ver=None, git_hash=None, terra_url=None, sam_url=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryConfigurationModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._active_profiles = None
        self._sem_ver = None
        self._git_hash = None
        self._terra_url = None
        self._sam_url = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if active_profiles is not None:
            self.active_profiles = active_profiles
        if sem_ver is not None:
            self.sem_ver = sem_ver
        if git_hash is not None:
            self.git_hash = git_hash
        if terra_url is not None:
            self.terra_url = terra_url
        if sam_url is not None:
            self.sam_url = sam_url

    @property
    def client_id(self):
        """Gets the client_id of this RepositoryConfigurationModel.  # noqa: E501

        the google defined client id for the repository  # noqa: E501

        :return: The client_id of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RepositoryConfigurationModel.

        the google defined client id for the repository  # noqa: E501

        :param client_id: The client_id of this RepositoryConfigurationModel.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def active_profiles(self):
        """Gets the active_profiles of this RepositoryConfigurationModel.  # noqa: E501

        the active profiles for this instance  # noqa: E501

        :return: The active_profiles of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._active_profiles

    @active_profiles.setter
    def active_profiles(self, active_profiles):
        """Sets the active_profiles of this RepositoryConfigurationModel.

        the active profiles for this instance  # noqa: E501

        :param active_profiles: The active_profiles of this RepositoryConfigurationModel.  # noqa: E501
        :type: list[str]
        """

        self._active_profiles = active_profiles

    @property
    def sem_ver(self):
        """Gets the sem_ver of this RepositoryConfigurationModel.  # noqa: E501

        the semantic version of the data repository  # noqa: E501

        :return: The sem_ver of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._sem_ver

    @sem_ver.setter
    def sem_ver(self, sem_ver):
        """Sets the sem_ver of this RepositoryConfigurationModel.

        the semantic version of the data repository  # noqa: E501

        :param sem_ver: The sem_ver of this RepositoryConfigurationModel.  # noqa: E501
        :type: str
        """

        self._sem_ver = sem_ver

    @property
    def git_hash(self):
        """Gets the git_hash of this RepositoryConfigurationModel.  # noqa: E501

        the git hash of the data repository  # noqa: E501

        :return: The git_hash of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._git_hash

    @git_hash.setter
    def git_hash(self, git_hash):
        """Sets the git_hash of this RepositoryConfigurationModel.

        the git hash of the data repository  # noqa: E501

        :param git_hash: The git_hash of this RepositoryConfigurationModel.  # noqa: E501
        :type: str
        """

        self._git_hash = git_hash

    @property
    def terra_url(self):
        """Gets the terra_url of this RepositoryConfigurationModel.  # noqa: E501

        the url to the corresponding terra environment  # noqa: E501

        :return: The terra_url of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._terra_url

    @terra_url.setter
    def terra_url(self, terra_url):
        """Sets the terra_url of this RepositoryConfigurationModel.

        the url to the corresponding terra environment  # noqa: E501

        :param terra_url: The terra_url of this RepositoryConfigurationModel.  # noqa: E501
        :type: str
        """

        self._terra_url = terra_url

    @property
    def sam_url(self):
        """Gets the sam_url of this RepositoryConfigurationModel.  # noqa: E501

        the URI of SAM this instance uses  # noqa: E501

        :return: The sam_url of this RepositoryConfigurationModel.  # noqa: E501
        :rtype: str
        """
        return self._sam_url

    @sam_url.setter
    def sam_url(self, sam_url):
        """Sets the sam_url of this RepositoryConfigurationModel.

        the URI of SAM this instance uses  # noqa: E501

        :param sam_url: The sam_url of this RepositoryConfigurationModel.  # noqa: E501
        :type: str
        """

        self._sam_url = sam_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryConfigurationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryConfigurationModel):
            return True

        return self.to_dict() != other.to_dict()
