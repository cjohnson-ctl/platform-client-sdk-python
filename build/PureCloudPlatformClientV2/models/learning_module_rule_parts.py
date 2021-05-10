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

class LearningModuleRuleParts(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LearningModuleRuleParts - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operation': 'str',
            'selector': 'str',
            'value': 'list[str]',
            'order': 'int'
        }

        self.attribute_map = {
            'operation': 'operation',
            'selector': 'selector',
            'value': 'value',
            'order': 'order'
        }

        self._operation = None
        self._selector = None
        self._value = None
        self._order = None

    @property
    def operation(self):
        """
        Gets the operation of this LearningModuleRuleParts.
        The learning module rule operation

        :return: The operation of this LearningModuleRuleParts.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this LearningModuleRuleParts.
        The learning module rule operation

        :param operation: The operation of this LearningModuleRuleParts.
        :type: str
        """
        allowed_values = ["Include", "Exclude"]
        if operation.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operation -> " + operation)
            self._operation = "outdated_sdk_version"
        else:
            self._operation = operation

    @property
    def selector(self):
        """
        Gets the selector of this LearningModuleRuleParts.
        The learning module rule selector

        :return: The selector of this LearningModuleRuleParts.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this LearningModuleRuleParts.
        The learning module rule selector

        :param selector: The selector of this LearningModuleRuleParts.
        :type: str
        """
        allowed_values = ["AcdSkills", "AgentName", "Division", "Group", "Location", "Queue", "Role", "Team"]
        if selector.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for selector -> " + selector)
            self._selector = "outdated_sdk_version"
        else:
            self._selector = selector

    @property
    def value(self):
        """
        Gets the value of this LearningModuleRuleParts.
        The value of rules

        :return: The value of this LearningModuleRuleParts.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LearningModuleRuleParts.
        The value of rules

        :param value: The value of this LearningModuleRuleParts.
        :type: list[str]
        """
        
        self._value = value

    @property
    def order(self):
        """
        Gets the order of this LearningModuleRuleParts.
        The order of rules in learning module rule

        :return: The order of this LearningModuleRuleParts.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this LearningModuleRuleParts.
        The order of rules in learning module rule

        :param order: The order of this LearningModuleRuleParts.
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

