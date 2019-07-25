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

class PolicyConditions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PolicyConditions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'for_users': 'list[User]',
            'directions': 'list[str]',
            'date_ranges': 'list[str]',
            'media_types': 'list[str]',
            'for_queues': 'list[Queue]',
            'duration': 'DurationCondition',
            'wrapup_codes': 'list[WrapupCode]',
            'time_allowed': 'TimeAllowed'
        }

        self.attribute_map = {
            'for_users': 'forUsers',
            'directions': 'directions',
            'date_ranges': 'dateRanges',
            'media_types': 'mediaTypes',
            'for_queues': 'forQueues',
            'duration': 'duration',
            'wrapup_codes': 'wrapupCodes',
            'time_allowed': 'timeAllowed'
        }

        self._for_users = None
        self._directions = None
        self._date_ranges = None
        self._media_types = None
        self._for_queues = None
        self._duration = None
        self._wrapup_codes = None
        self._time_allowed = None

    @property
    def for_users(self):
        """
        Gets the for_users of this PolicyConditions.


        :return: The for_users of this PolicyConditions.
        :rtype: list[User]
        """
        return self._for_users

    @for_users.setter
    def for_users(self, for_users):
        """
        Sets the for_users of this PolicyConditions.


        :param for_users: The for_users of this PolicyConditions.
        :type: list[User]
        """
        
        self._for_users = for_users

    @property
    def directions(self):
        """
        Gets the directions of this PolicyConditions.


        :return: The directions of this PolicyConditions.
        :rtype: list[str]
        """
        return self._directions

    @directions.setter
    def directions(self, directions):
        """
        Sets the directions of this PolicyConditions.


        :param directions: The directions of this PolicyConditions.
        :type: list[str]
        """
        
        self._directions = directions

    @property
    def date_ranges(self):
        """
        Gets the date_ranges of this PolicyConditions.


        :return: The date_ranges of this PolicyConditions.
        :rtype: list[str]
        """
        return self._date_ranges

    @date_ranges.setter
    def date_ranges(self, date_ranges):
        """
        Sets the date_ranges of this PolicyConditions.


        :param date_ranges: The date_ranges of this PolicyConditions.
        :type: list[str]
        """
        
        self._date_ranges = date_ranges

    @property
    def media_types(self):
        """
        Gets the media_types of this PolicyConditions.


        :return: The media_types of this PolicyConditions.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """
        Sets the media_types of this PolicyConditions.


        :param media_types: The media_types of this PolicyConditions.
        :type: list[str]
        """
        
        self._media_types = media_types

    @property
    def for_queues(self):
        """
        Gets the for_queues of this PolicyConditions.


        :return: The for_queues of this PolicyConditions.
        :rtype: list[Queue]
        """
        return self._for_queues

    @for_queues.setter
    def for_queues(self, for_queues):
        """
        Sets the for_queues of this PolicyConditions.


        :param for_queues: The for_queues of this PolicyConditions.
        :type: list[Queue]
        """
        
        self._for_queues = for_queues

    @property
    def duration(self):
        """
        Gets the duration of this PolicyConditions.


        :return: The duration of this PolicyConditions.
        :rtype: DurationCondition
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this PolicyConditions.


        :param duration: The duration of this PolicyConditions.
        :type: DurationCondition
        """
        
        self._duration = duration

    @property
    def wrapup_codes(self):
        """
        Gets the wrapup_codes of this PolicyConditions.


        :return: The wrapup_codes of this PolicyConditions.
        :rtype: list[WrapupCode]
        """
        return self._wrapup_codes

    @wrapup_codes.setter
    def wrapup_codes(self, wrapup_codes):
        """
        Sets the wrapup_codes of this PolicyConditions.


        :param wrapup_codes: The wrapup_codes of this PolicyConditions.
        :type: list[WrapupCode]
        """
        
        self._wrapup_codes = wrapup_codes

    @property
    def time_allowed(self):
        """
        Gets the time_allowed of this PolicyConditions.


        :return: The time_allowed of this PolicyConditions.
        :rtype: TimeAllowed
        """
        return self._time_allowed

    @time_allowed.setter
    def time_allowed(self, time_allowed):
        """
        Sets the time_allowed of this PolicyConditions.


        :param time_allowed: The time_allowed of this PolicyConditions.
        :type: TimeAllowed
        """
        
        self._time_allowed = time_allowed

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

