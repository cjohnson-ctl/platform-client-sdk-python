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

class UpdateActionInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UpdateActionInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'name': 'str',
            'config': 'ActionConfig',
            'version': 'int'
        }

        self.attribute_map = {
            'category': 'category',
            'name': 'name',
            'config': 'config',
            'version': 'version'
        }

        self._category = None
        self._name = None
        self._config = None
        self._version = None

    @property
    def category(self):
        """
        Gets the category of this UpdateActionInput.
        Category of action

        :return: The category of this UpdateActionInput.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this UpdateActionInput.
        Category of action

        :param category: The category of this UpdateActionInput.
        :type: str
        """
        
        self._category = category

    @property
    def name(self):
        """
        Gets the name of this UpdateActionInput.
        Name of action

        :return: The name of this UpdateActionInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateActionInput.
        Name of action

        :param name: The name of this UpdateActionInput.
        :type: str
        """
        
        self._name = name

    @property
    def config(self):
        """
        Gets the config of this UpdateActionInput.
        Configuration to support request and response processing

        :return: The config of this UpdateActionInput.
        :rtype: ActionConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this UpdateActionInput.
        Configuration to support request and response processing

        :param config: The config of this UpdateActionInput.
        :type: ActionConfig
        """
        
        self._config = config

    @property
    def version(self):
        """
        Gets the version of this UpdateActionInput.
        Version of this action

        :return: The version of this UpdateActionInput.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateActionInput.
        Version of this action

        :param version: The version of this UpdateActionInput.
        :type: int
        """
        
        self._version = version

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

