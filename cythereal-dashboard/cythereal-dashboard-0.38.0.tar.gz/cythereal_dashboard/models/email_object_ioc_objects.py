# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 0.38.0
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailObjectIocObjects(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'str',
        'ioc_type': 'str',
        'file_children': 'list[EmailObjectFileChildren]',
        'related_iocs': 'list[str]',
        'upload_date': 'str'
    }

    attribute_map = {
        'value': 'value',
        'ioc_type': 'ioc_type',
        'file_children': 'file_children',
        'related_iocs': 'related_iocs',
        'upload_date': 'upload_date'
    }

    def __init__(self, value=None, ioc_type=None, file_children=None, related_iocs=None, upload_date=None):  # noqa: E501
        """EmailObjectIocObjects - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._ioc_type = None
        self._file_children = None
        self._related_iocs = None
        self._upload_date = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if ioc_type is not None:
            self.ioc_type = ioc_type
        if file_children is not None:
            self.file_children = file_children
        if related_iocs is not None:
            self.related_iocs = related_iocs
        if upload_date is not None:
            self.upload_date = upload_date

    @property
    def value(self):
        """Gets the value of this EmailObjectIocObjects.  # noqa: E501

        The actual IoC itself  # noqa: E501

        :return: The value of this EmailObjectIocObjects.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EmailObjectIocObjects.

        The actual IoC itself  # noqa: E501

        :param value: The value of this EmailObjectIocObjects.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def ioc_type(self):
        """Gets the ioc_type of this EmailObjectIocObjects.  # noqa: E501

        The type of the IoC  # noqa: E501

        :return: The ioc_type of this EmailObjectIocObjects.  # noqa: E501
        :rtype: str
        """
        return self._ioc_type

    @ioc_type.setter
    def ioc_type(self, ioc_type):
        """Sets the ioc_type of this EmailObjectIocObjects.

        The type of the IoC  # noqa: E501

        :param ioc_type: The ioc_type of this EmailObjectIocObjects.  # noqa: E501
        :type: str
        """
        allowed_values = ["hash", "url", "ip", "attachment"]  # noqa: E501
        if ioc_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ioc_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ioc_type, allowed_values)
            )

        self._ioc_type = ioc_type

    @property
    def file_children(self):
        """Gets the file_children of this EmailObjectIocObjects.  # noqa: E501

        The children of the IoC  # noqa: E501

        :return: The file_children of this EmailObjectIocObjects.  # noqa: E501
        :rtype: list[EmailObjectFileChildren]
        """
        return self._file_children

    @file_children.setter
    def file_children(self, file_children):
        """Sets the file_children of this EmailObjectIocObjects.

        The children of the IoC  # noqa: E501

        :param file_children: The file_children of this EmailObjectIocObjects.  # noqa: E501
        :type: list[EmailObjectFileChildren]
        """

        self._file_children = file_children

    @property
    def related_iocs(self):
        """Gets the related_iocs of this EmailObjectIocObjects.  # noqa: E501

        Connected IoCs  # noqa: E501

        :return: The related_iocs of this EmailObjectIocObjects.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_iocs

    @related_iocs.setter
    def related_iocs(self, related_iocs):
        """Sets the related_iocs of this EmailObjectIocObjects.

        Connected IoCs  # noqa: E501

        :param related_iocs: The related_iocs of this EmailObjectIocObjects.  # noqa: E501
        :type: list[str]
        """

        self._related_iocs = related_iocs

    @property
    def upload_date(self):
        """Gets the upload_date of this EmailObjectIocObjects.  # noqa: E501

        Date the IoC was first seen by our system  # noqa: E501

        :return: The upload_date of this EmailObjectIocObjects.  # noqa: E501
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """Sets the upload_date of this EmailObjectIocObjects.

        Date the IoC was first seen by our system  # noqa: E501

        :param upload_date: The upload_date of this EmailObjectIocObjects.  # noqa: E501
        :type: str
        """

        self._upload_date = upload_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EmailObjectIocObjects, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmailObjectIocObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
