# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class PermissionDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PermissionDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'permissions': 'list[str]',
            'allows_current_user': 'bool',
            'enforced': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'permissions': 'permissions',
            'allows_current_user': 'allowsCurrentUser',
            'enforced': 'enforced'
        }

        self._type = None
        self._permissions = None
        self._allows_current_user = None
        self._enforced = None

    @property
    def type(self):
        """
        Gets the type of this PermissionDetails.
        The type of permission requirement

        :return: The type of this PermissionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PermissionDetails.
        The type of permission requirement

        :param type: The type of this PermissionDetails.
        :type: str
        """
        allowed_values = ["requiresCurrentUser", "requiresPermissions", "requiresDivisionPermissions", "requiresAnyDivisionPermissions", "requiresUserBeConversationParticipant"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def permissions(self):
        """
        Gets the permissions of this PermissionDetails.
        List of required permissions

        :return: The permissions of this PermissionDetails.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this PermissionDetails.
        List of required permissions

        :param permissions: The permissions of this PermissionDetails.
        :type: list[str]
        """
        
        self._permissions = permissions

    @property
    def allows_current_user(self):
        """
        Gets the allows_current_user of this PermissionDetails.
        Whether the current user can subscribe, when division permissions are otherwise required

        :return: The allows_current_user of this PermissionDetails.
        :rtype: bool
        """
        return self._allows_current_user

    @allows_current_user.setter
    def allows_current_user(self, allows_current_user):
        """
        Sets the allows_current_user of this PermissionDetails.
        Whether the current user can subscribe, when division permissions are otherwise required

        :param allows_current_user: The allows_current_user of this PermissionDetails.
        :type: bool
        """
        
        self._allows_current_user = allows_current_user

    @property
    def enforced(self):
        """
        Gets the enforced of this PermissionDetails.
        Whether or not this permission requirement is enforced

        :return: The enforced of this PermissionDetails.
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """
        Sets the enforced of this PermissionDetails.
        Whether or not this permission requirement is enforced

        :param enforced: The enforced of this PermissionDetails.
        :type: bool
        """
        
        self._enforced = enforced

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

