# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_file.configuration import Configuration


class FileFileAlternateContentSource(object):
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
        'name': 'str',
        'last_refreshed': 'datetime',
        'paths': 'list[str]',
        'remote': 'str'
    }

    attribute_map = {
        'name': 'name',
        'last_refreshed': 'last_refreshed',
        'paths': 'paths',
        'remote': 'remote'
    }

    def __init__(self, name=None, last_refreshed=None, paths=None, remote=None, local_vars_configuration=None):  # noqa: E501
        """FileFileAlternateContentSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._last_refreshed = None
        self._paths = None
        self._remote = None
        self.discriminator = None

        self.name = name
        self.last_refreshed = last_refreshed
        if paths is not None:
            self.paths = paths
        self.remote = remote

    @property
    def name(self):
        """Gets the name of this FileFileAlternateContentSource.  # noqa: E501

        Name of Alternate Content Source.  # noqa: E501

        :return: The name of this FileFileAlternateContentSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileFileAlternateContentSource.

        Name of Alternate Content Source.  # noqa: E501

        :param name: The name of this FileFileAlternateContentSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_refreshed(self):
        """Gets the last_refreshed of this FileFileAlternateContentSource.  # noqa: E501

        Date of last refresh of AlternateContentSource.  # noqa: E501

        :return: The last_refreshed of this FileFileAlternateContentSource.  # noqa: E501
        :rtype: datetime
        """
        return self._last_refreshed

    @last_refreshed.setter
    def last_refreshed(self, last_refreshed):
        """Sets the last_refreshed of this FileFileAlternateContentSource.

        Date of last refresh of AlternateContentSource.  # noqa: E501

        :param last_refreshed: The last_refreshed of this FileFileAlternateContentSource.  # noqa: E501
        :type: datetime
        """

        self._last_refreshed = last_refreshed

    @property
    def paths(self):
        """Gets the paths of this FileFileAlternateContentSource.  # noqa: E501

        List of paths that will be appended to the Remote url when searching for content.  # noqa: E501

        :return: The paths of this FileFileAlternateContentSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this FileFileAlternateContentSource.

        List of paths that will be appended to the Remote url when searching for content.  # noqa: E501

        :param paths: The paths of this FileFileAlternateContentSource.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def remote(self):
        """Gets the remote of this FileFileAlternateContentSource.  # noqa: E501

        The remote to provide alternate content source.  # noqa: E501

        :return: The remote of this FileFileAlternateContentSource.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this FileFileAlternateContentSource.

        The remote to provide alternate content source.  # noqa: E501

        :param remote: The remote of this FileFileAlternateContentSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and remote is None:  # noqa: E501
            raise ValueError("Invalid value for `remote`, must not be `None`")  # noqa: E501

        self._remote = remote

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
        if not isinstance(other, FileFileAlternateContentSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileFileAlternateContentSource):
            return True

        return self.to_dict() != other.to_dict()
