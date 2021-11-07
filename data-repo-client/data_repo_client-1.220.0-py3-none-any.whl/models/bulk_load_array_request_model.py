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


class BulkLoadArrayRequestModel(object):
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
        'profile_id': 'str',
        'load_tag': 'str',
        'max_failed_file_loads': 'int',
        'load_array': 'list[BulkLoadFileModel]'
    }

    attribute_map = {
        'profile_id': 'profileId',
        'load_tag': 'loadTag',
        'max_failed_file_loads': 'maxFailedFileLoads',
        'load_array': 'loadArray'
    }

    def __init__(self, profile_id=None, load_tag=None, max_failed_file_loads=0, load_array=None, local_vars_configuration=None):  # noqa: E501
        """BulkLoadArrayRequestModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile_id = None
        self._load_tag = None
        self._max_failed_file_loads = None
        self._load_array = None
        self.discriminator = None

        self.profile_id = profile_id
        self.load_tag = load_tag
        if max_failed_file_loads is not None:
            self.max_failed_file_loads = max_failed_file_loads
        self.load_array = load_array

    @property
    def profile_id(self):
        """Gets the profile_id of this BulkLoadArrayRequestModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The profile_id of this BulkLoadArrayRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this BulkLoadArrayRequestModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param profile_id: The profile_id of this BulkLoadArrayRequestModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def load_tag(self):
        """Gets the load_tag of this BulkLoadArrayRequestModel.  # noqa: E501

        client-specified tag for a data or file load. If no id is specified, we use the string form of the job create time as the tag.   # noqa: E501

        :return: The load_tag of this BulkLoadArrayRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._load_tag

    @load_tag.setter
    def load_tag(self, load_tag):
        """Sets the load_tag of this BulkLoadArrayRequestModel.

        client-specified tag for a data or file load. If no id is specified, we use the string form of the job create time as the tag.   # noqa: E501

        :param load_tag: The load_tag of this BulkLoadArrayRequestModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and load_tag is None:  # noqa: E501
            raise ValueError("Invalid value for `load_tag`, must not be `None`")  # noqa: E501

        self._load_tag = load_tag

    @property
    def max_failed_file_loads(self):
        """Gets the max_failed_file_loads of this BulkLoadArrayRequestModel.  # noqa: E501

        max number of failed file loads before stopping; if -1, allow any number of errors  # noqa: E501

        :return: The max_failed_file_loads of this BulkLoadArrayRequestModel.  # noqa: E501
        :rtype: int
        """
        return self._max_failed_file_loads

    @max_failed_file_loads.setter
    def max_failed_file_loads(self, max_failed_file_loads):
        """Sets the max_failed_file_loads of this BulkLoadArrayRequestModel.

        max number of failed file loads before stopping; if -1, allow any number of errors  # noqa: E501

        :param max_failed_file_loads: The max_failed_file_loads of this BulkLoadArrayRequestModel.  # noqa: E501
        :type: int
        """

        self._max_failed_file_loads = max_failed_file_loads

    @property
    def load_array(self):
        """Gets the load_array of this BulkLoadArrayRequestModel.  # noqa: E501

        Array files to load  # noqa: E501

        :return: The load_array of this BulkLoadArrayRequestModel.  # noqa: E501
        :rtype: list[BulkLoadFileModel]
        """
        return self._load_array

    @load_array.setter
    def load_array(self, load_array):
        """Sets the load_array of this BulkLoadArrayRequestModel.

        Array files to load  # noqa: E501

        :param load_array: The load_array of this BulkLoadArrayRequestModel.  # noqa: E501
        :type: list[BulkLoadFileModel]
        """
        if self.local_vars_configuration.client_side_validation and load_array is None:  # noqa: E501
            raise ValueError("Invalid value for `load_array`, must not be `None`")  # noqa: E501

        self._load_array = load_array

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
        if not isinstance(other, BulkLoadArrayRequestModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkLoadArrayRequestModel):
            return True

        return self.to_dict() != other.to_dict()
