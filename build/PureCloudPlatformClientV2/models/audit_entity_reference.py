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

class AuditEntityReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuditEntityReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'self_uri': 'str',
            'type': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'self_uri': 'selfUri',
            'type': 'type',
            'action': 'action'
        }

        self._id = None
        self._name = None
        self._self_uri = None
        self._type = None
        self._action = None

    @property
    def id(self):
        """
        Gets the id of this AuditEntityReference.


        :return: The id of this AuditEntityReference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditEntityReference.


        :param id: The id of this AuditEntityReference.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AuditEntityReference.


        :return: The name of this AuditEntityReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuditEntityReference.


        :param name: The name of this AuditEntityReference.
        :type: str
        """
        
        self._name = name

    @property
    def self_uri(self):
        """
        Gets the self_uri of this AuditEntityReference.


        :return: The self_uri of this AuditEntityReference.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this AuditEntityReference.


        :param self_uri: The self_uri of this AuditEntityReference.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def type(self):
        """
        Gets the type of this AuditEntityReference.


        :return: The type of this AuditEntityReference.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuditEntityReference.


        :param type: The type of this AuditEntityReference.
        :type: str
        """
        allowed_values = ["ATTRIBUTE", "ATTRIBUTE_GROUP_INSTANCE", "DOCUMENT", "DOWNLOAD", "FAX", "GROUP", "RECORDING", "TAG", "WORKSPACE", "USER", "PUBLIC"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def action(self):
        """
        Gets the action of this AuditEntityReference.


        :return: The action of this AuditEntityReference.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AuditEntityReference.


        :param action: The action of this AuditEntityReference.
        :type: str
        """
        
        self._action = action

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

