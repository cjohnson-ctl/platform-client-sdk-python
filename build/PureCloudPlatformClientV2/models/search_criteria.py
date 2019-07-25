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

class SearchCriteria(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SearchCriteria - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_value': 'str',
            'values': 'list[str]',
            'start_value': 'str',
            'fields': 'list[str]',
            'value': 'str',
            'operator': 'str',
            'group': 'list[SearchCriteria]',
            'type': 'str'
        }

        self.attribute_map = {
            'end_value': 'endValue',
            'values': 'values',
            'start_value': 'startValue',
            'fields': 'fields',
            'value': 'value',
            'operator': 'operator',
            'group': 'group',
            'type': 'type'
        }

        self._end_value = None
        self._values = None
        self._start_value = None
        self._fields = None
        self._value = None
        self._operator = None
        self._group = None
        self._type = None

    @property
    def end_value(self):
        """
        Gets the end_value of this SearchCriteria.
        The end value of the range. This field is used for range search types.

        :return: The end_value of this SearchCriteria.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this SearchCriteria.
        The end value of the range. This field is used for range search types.

        :param end_value: The end_value of this SearchCriteria.
        :type: str
        """
        
        self._end_value = end_value

    @property
    def values(self):
        """
        Gets the values of this SearchCriteria.
        A list of values for the search to match against

        :return: The values of this SearchCriteria.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this SearchCriteria.
        A list of values for the search to match against

        :param values: The values of this SearchCriteria.
        :type: list[str]
        """
        
        self._values = values

    @property
    def start_value(self):
        """
        Gets the start_value of this SearchCriteria.
        The start value of the range. This field is used for range search types.

        :return: The start_value of this SearchCriteria.
        :rtype: str
        """
        return self._start_value

    @start_value.setter
    def start_value(self, start_value):
        """
        Sets the start_value of this SearchCriteria.
        The start value of the range. This field is used for range search types.

        :param start_value: The start_value of this SearchCriteria.
        :type: str
        """
        
        self._start_value = start_value

    @property
    def fields(self):
        """
        Gets the fields of this SearchCriteria.
        Field names to search against

        :return: The fields of this SearchCriteria.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this SearchCriteria.
        Field names to search against

        :param fields: The fields of this SearchCriteria.
        :type: list[str]
        """
        
        self._fields = fields

    @property
    def value(self):
        """
        Gets the value of this SearchCriteria.
        A value for the search to match against

        :return: The value of this SearchCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SearchCriteria.
        A value for the search to match against

        :param value: The value of this SearchCriteria.
        :type: str
        """
        
        self._value = value

    @property
    def operator(self):
        """
        Gets the operator of this SearchCriteria.
        How to apply this search criteria against other criteria

        :return: The operator of this SearchCriteria.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this SearchCriteria.
        How to apply this search criteria against other criteria

        :param operator: The operator of this SearchCriteria.
        :type: str
        """
        allowed_values = ["AND", "OR", "NOT"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for operator -> " + operator
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def group(self):
        """
        Gets the group of this SearchCriteria.
        Groups multiple conditions

        :return: The group of this SearchCriteria.
        :rtype: list[SearchCriteria]
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this SearchCriteria.
        Groups multiple conditions

        :param group: The group of this SearchCriteria.
        :type: list[SearchCriteria]
        """
        
        self._group = group

    @property
    def type(self):
        """
        Gets the type of this SearchCriteria.


        :return: The type of this SearchCriteria.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchCriteria.


        :param type: The type of this SearchCriteria.
        :type: str
        """
        allowed_values = ["EXACT", "CONTAINS", "STARTS_WITH", "REQUIRED_FIELDS", "RANGE", "DATE_RANGE", "LESS_THAN", "LESS_THAN_EQUAL_TO", "GREATER_THAN", "GREATER_THAN_EQUAL_TO", "SIMPLE", "TERM", "TERMS", "QUERY_STRING", "MATCH_ALL"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

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

