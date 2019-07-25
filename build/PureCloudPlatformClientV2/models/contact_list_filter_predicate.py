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

class ContactListFilterPredicate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContactListFilterPredicate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'column': 'str',
            'column_type': 'str',
            'operator': 'str',
            'value': 'str',
            'range': 'ContactListFilterRange',
            'inverted': 'bool'
        }

        self.attribute_map = {
            'column': 'column',
            'column_type': 'columnType',
            'operator': 'operator',
            'value': 'value',
            'range': 'range',
            'inverted': 'inverted'
        }

        self._column = None
        self._column_type = None
        self._operator = None
        self._value = None
        self._range = None
        self._inverted = None

    @property
    def column(self):
        """
        Gets the column of this ContactListFilterPredicate.
        Contact list column from the ContactListFilter's contactList.

        :return: The column of this ContactListFilterPredicate.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this ContactListFilterPredicate.
        Contact list column from the ContactListFilter's contactList.

        :param column: The column of this ContactListFilterPredicate.
        :type: str
        """
        
        self._column = column

    @property
    def column_type(self):
        """
        Gets the column_type of this ContactListFilterPredicate.
        The type of data in the contact column.

        :return: The column_type of this ContactListFilterPredicate.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """
        Sets the column_type of this ContactListFilterPredicate.
        The type of data in the contact column.

        :param column_type: The column_type of this ContactListFilterPredicate.
        :type: str
        """
        allowed_values = ["numeric", "alphabetic"]
        if column_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for column_type -> " + column_type
            self._column_type = "outdated_sdk_version"
        else:
            self._column_type = column_type

    @property
    def operator(self):
        """
        Gets the operator of this ContactListFilterPredicate.
        The operator for this ContactListFilterPredicate.

        :return: The operator of this ContactListFilterPredicate.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this ContactListFilterPredicate.
        The operator for this ContactListFilterPredicate.

        :param operator: The operator of this ContactListFilterPredicate.
        :type: str
        """
        allowed_values = ["EQUALS", "LESS_THAN", "LESS_THAN_EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "BEFORE", "AFTER", "BETWEEN", "IN"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for operator -> " + operator
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def value(self):
        """
        Gets the value of this ContactListFilterPredicate.
        Value with which to compare the contact's data. This could be text, a number, or a relative time. A value for relative time should follow the format PxxDTyyHzzM, where xx, yy, and zz specify the days, hours and minutes. For example, a value of P01DT08H30M corresponds to 1 day, 8 hours, and 30 minutes from now. To specify a time in the past, include a negative sign before each numeric value. For example, a value of P-01DT-08H-30M corresponds to 1 day, 8 hours, and 30 minutes in the past. You can also do things like P01DT00H-30M, which would correspond to 23 hours and 30 minutes from now (1 day - 30 minutes).

        :return: The value of this ContactListFilterPredicate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ContactListFilterPredicate.
        Value with which to compare the contact's data. This could be text, a number, or a relative time. A value for relative time should follow the format PxxDTyyHzzM, where xx, yy, and zz specify the days, hours and minutes. For example, a value of P01DT08H30M corresponds to 1 day, 8 hours, and 30 minutes from now. To specify a time in the past, include a negative sign before each numeric value. For example, a value of P-01DT-08H-30M corresponds to 1 day, 8 hours, and 30 minutes in the past. You can also do things like P01DT00H-30M, which would correspond to 23 hours and 30 minutes from now (1 day - 30 minutes).

        :param value: The value of this ContactListFilterPredicate.
        :type: str
        """
        
        self._value = value

    @property
    def range(self):
        """
        Gets the range of this ContactListFilterPredicate.
        A range of values. Required for operators BETWEEN and IN.

        :return: The range of this ContactListFilterPredicate.
        :rtype: ContactListFilterRange
        """
        return self._range

    @range.setter
    def range(self, range):
        """
        Sets the range of this ContactListFilterPredicate.
        A range of values. Required for operators BETWEEN and IN.

        :param range: The range of this ContactListFilterPredicate.
        :type: ContactListFilterRange
        """
        
        self._range = range

    @property
    def inverted(self):
        """
        Gets the inverted of this ContactListFilterPredicate.
        Inverts the result of the predicate (i.e., if the predicate returns true, inverting it will return false).

        :return: The inverted of this ContactListFilterPredicate.
        :rtype: bool
        """
        return self._inverted

    @inverted.setter
    def inverted(self, inverted):
        """
        Sets the inverted of this ContactListFilterPredicate.
        Inverts the result of the predicate (i.e., if the predicate returns true, inverting it will return false).

        :param inverted: The inverted of this ContactListFilterPredicate.
        :type: bool
        """
        
        self._inverted = inverted

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

