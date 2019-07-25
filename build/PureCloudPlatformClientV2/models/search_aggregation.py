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

class SearchAggregation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SearchAggregation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field': 'str',
            'name': 'str',
            'type': 'str',
            'value': 'str',
            'size': 'int',
            'order': 'list[str]'
        }

        self.attribute_map = {
            'field': 'field',
            'name': 'name',
            'type': 'type',
            'value': 'value',
            'size': 'size',
            'order': 'order'
        }

        self._field = None
        self._name = None
        self._type = None
        self._value = None
        self._size = None
        self._order = None

    @property
    def field(self):
        """
        Gets the field of this SearchAggregation.
        The field used for aggregation

        :return: The field of this SearchAggregation.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this SearchAggregation.
        The field used for aggregation

        :param field: The field of this SearchAggregation.
        :type: str
        """
        
        self._field = field

    @property
    def name(self):
        """
        Gets the name of this SearchAggregation.
        The name of the aggregation. The response aggregation uses this name.

        :return: The name of this SearchAggregation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchAggregation.
        The name of the aggregation. The response aggregation uses this name.

        :param name: The name of this SearchAggregation.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this SearchAggregation.
        The type of aggregation to perform

        :return: The type of this SearchAggregation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchAggregation.
        The type of aggregation to perform

        :param type: The type of this SearchAggregation.
        :type: str
        """
        allowed_values = ["COUNT", "SUM", "AVERAGE", "TERM", "CONTAINS", "STARTS_WITH", "ENDS_WITH"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def value(self):
        """
        Gets the value of this SearchAggregation.
        A value to use for aggregation

        :return: The value of this SearchAggregation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SearchAggregation.
        A value to use for aggregation

        :param value: The value of this SearchAggregation.
        :type: str
        """
        
        self._value = value

    @property
    def size(self):
        """
        Gets the size of this SearchAggregation.
        The number aggregations results to return out of the entire result set

        :return: The size of this SearchAggregation.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SearchAggregation.
        The number aggregations results to return out of the entire result set

        :param size: The size of this SearchAggregation.
        :type: int
        """
        
        self._size = size

    @property
    def order(self):
        """
        Gets the order of this SearchAggregation.
        The order in which aggregation results are sorted

        :return: The order of this SearchAggregation.
        :rtype: list[str]
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this SearchAggregation.
        The order in which aggregation results are sorted

        :param order: The order of this SearchAggregation.
        :type: list[str]
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

