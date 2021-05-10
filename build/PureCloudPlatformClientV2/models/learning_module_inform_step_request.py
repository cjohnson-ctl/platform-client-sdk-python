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

class LearningModuleInformStepRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LearningModuleInformStepRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'value': 'str',
            'sharing_uri': 'str',
            'content_type': 'str',
            'order': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'value': 'value',
            'sharing_uri': 'sharingUri',
            'content_type': 'contentType',
            'order': 'order'
        }

        self._type = None
        self._name = None
        self._value = None
        self._sharing_uri = None
        self._content_type = None
        self._order = None

    @property
    def type(self):
        """
        Gets the type of this LearningModuleInformStepRequest.
        The learning module inform step type

        :return: The type of this LearningModuleInformStepRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LearningModuleInformStepRequest.
        The learning module inform step type

        :param type: The type of this LearningModuleInformStepRequest.
        :type: str
        """
        allowed_values = ["Url", "Content"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def name(self):
        """
        Gets the name of this LearningModuleInformStepRequest.
        The name of the inform step or content

        :return: The name of this LearningModuleInformStepRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LearningModuleInformStepRequest.
        The name of the inform step or content

        :param name: The name of this LearningModuleInformStepRequest.
        :type: str
        """
        
        self._name = name

    @property
    def value(self):
        """
        Gets the value of this LearningModuleInformStepRequest.
        The value for inform step

        :return: The value of this LearningModuleInformStepRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LearningModuleInformStepRequest.
        The value for inform step

        :param value: The value of this LearningModuleInformStepRequest.
        :type: str
        """
        
        self._value = value

    @property
    def sharing_uri(self):
        """
        Gets the sharing_uri of this LearningModuleInformStepRequest.
        The sharing uri for Content type inform step

        :return: The sharing_uri of this LearningModuleInformStepRequest.
        :rtype: str
        """
        return self._sharing_uri

    @sharing_uri.setter
    def sharing_uri(self, sharing_uri):
        """
        Sets the sharing_uri of this LearningModuleInformStepRequest.
        The sharing uri for Content type inform step

        :param sharing_uri: The sharing_uri of this LearningModuleInformStepRequest.
        :type: str
        """
        
        self._sharing_uri = sharing_uri

    @property
    def content_type(self):
        """
        Gets the content_type of this LearningModuleInformStepRequest.
        The document type for Content type Inform step

        :return: The content_type of this LearningModuleInformStepRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this LearningModuleInformStepRequest.
        The document type for Content type Inform step

        :param content_type: The content_type of this LearningModuleInformStepRequest.
        :type: str
        """
        
        self._content_type = content_type

    @property
    def order(self):
        """
        Gets the order of this LearningModuleInformStepRequest.
        The order of inform step in a learning module

        :return: The order of this LearningModuleInformStepRequest.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this LearningModuleInformStepRequest.
        The order of inform step in a learning module

        :param order: The order of this LearningModuleInformStepRequest.
        :type: int
        """
        
        self._order = order

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

