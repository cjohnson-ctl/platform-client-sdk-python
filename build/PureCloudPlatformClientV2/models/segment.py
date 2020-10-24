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

class Segment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Segment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_time': 'datetime',
            'end_time': 'datetime',
            'type': 'str',
            'how_ended': 'str',
            'disconnect_type': 'str'
        }

        self.attribute_map = {
            'start_time': 'startTime',
            'end_time': 'endTime',
            'type': 'type',
            'how_ended': 'howEnded',
            'disconnect_type': 'disconnectType'
        }

        self._start_time = None
        self._end_time = None
        self._type = None
        self._how_ended = None
        self._disconnect_type = None

    @property
    def start_time(self):
        """
        Gets the start_time of this Segment.
        The timestamp when this segment began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_time of this Segment.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this Segment.
        The timestamp when this segment began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_time: The start_time of this Segment.
        :type: datetime
        """
        
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this Segment.
        The timestamp when this segment ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_time of this Segment.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this Segment.
        The timestamp when this segment ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_time: The end_time of this Segment.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def type(self):
        """
        Gets the type of this Segment.
        The activity taking place for the participant in the segment.

        :return: The type of this Segment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Segment.
        The activity taking place for the participant in the segment.

        :param type: The type of this Segment.
        :type: str
        """
        
        self._type = type

    @property
    def how_ended(self):
        """
        Gets the how_ended of this Segment.
        A description of the event that ended the segment.

        :return: The how_ended of this Segment.
        :rtype: str
        """
        return self._how_ended

    @how_ended.setter
    def how_ended(self, how_ended):
        """
        Sets the how_ended of this Segment.
        A description of the event that ended the segment.

        :param how_ended: The how_ended of this Segment.
        :type: str
        """
        
        self._how_ended = how_ended

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this Segment.
        A description of the event that disconnected the segment

        :return: The disconnect_type of this Segment.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this Segment.
        A description of the event that disconnected the segment

        :param disconnect_type: The disconnect_type of this Segment.
        :type: str
        """
        
        self._disconnect_type = disconnect_type

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

