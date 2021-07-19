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

class CalendarUrlResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CalendarUrlResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'calendar_url': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'calendar_url': 'calendarUrl',
            'self_uri': 'selfUri'
        }

        self._calendar_url = None
        self._self_uri = None

    @property
    def calendar_url(self):
        """
        Gets the calendar_url of this CalendarUrlResponse.
        The calendar url for the user to subscribe with supported clients

        :return: The calendar_url of this CalendarUrlResponse.
        :rtype: str
        """
        return self._calendar_url

    @calendar_url.setter
    def calendar_url(self, calendar_url):
        """
        Sets the calendar_url of this CalendarUrlResponse.
        The calendar url for the user to subscribe with supported clients

        :param calendar_url: The calendar_url of this CalendarUrlResponse.
        :type: str
        """
        
        self._calendar_url = calendar_url

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CalendarUrlResponse.
        The URI for this object

        :return: The self_uri of this CalendarUrlResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CalendarUrlResponse.
        The URI for this object

        :param self_uri: The self_uri of this CalendarUrlResponse.
        :type: str
        """
        
        self._self_uri = self_uri

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
