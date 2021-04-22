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

class EdgeMetricsTopicEdgeMetricSubsystem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeMetricsTopicEdgeMetricSubsystem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'process_name': 'str',
            'delay_ms': 'int',
            'media_subsystem': 'EdgeMetricsTopicEdgeMetricSubsystemMedia'
        }

        self.attribute_map = {
            'process_name': 'processName',
            'delay_ms': 'delayMs',
            'media_subsystem': 'mediaSubsystem'
        }

        self._process_name = None
        self._delay_ms = None
        self._media_subsystem = None

    @property
    def process_name(self):
        """
        Gets the process_name of this EdgeMetricsTopicEdgeMetricSubsystem.


        :return: The process_name of this EdgeMetricsTopicEdgeMetricSubsystem.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """
        Sets the process_name of this EdgeMetricsTopicEdgeMetricSubsystem.


        :param process_name: The process_name of this EdgeMetricsTopicEdgeMetricSubsystem.
        :type: str
        """
        
        self._process_name = process_name

    @property
    def delay_ms(self):
        """
        Gets the delay_ms of this EdgeMetricsTopicEdgeMetricSubsystem.


        :return: The delay_ms of this EdgeMetricsTopicEdgeMetricSubsystem.
        :rtype: int
        """
        return self._delay_ms

    @delay_ms.setter
    def delay_ms(self, delay_ms):
        """
        Sets the delay_ms of this EdgeMetricsTopicEdgeMetricSubsystem.


        :param delay_ms: The delay_ms of this EdgeMetricsTopicEdgeMetricSubsystem.
        :type: int
        """
        
        self._delay_ms = delay_ms

    @property
    def media_subsystem(self):
        """
        Gets the media_subsystem of this EdgeMetricsTopicEdgeMetricSubsystem.


        :return: The media_subsystem of this EdgeMetricsTopicEdgeMetricSubsystem.
        :rtype: EdgeMetricsTopicEdgeMetricSubsystemMedia
        """
        return self._media_subsystem

    @media_subsystem.setter
    def media_subsystem(self, media_subsystem):
        """
        Sets the media_subsystem of this EdgeMetricsTopicEdgeMetricSubsystem.


        :param media_subsystem: The media_subsystem of this EdgeMetricsTopicEdgeMetricSubsystem.
        :type: EdgeMetricsTopicEdgeMetricSubsystemMedia
        """
        
        self._media_subsystem = media_subsystem

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
