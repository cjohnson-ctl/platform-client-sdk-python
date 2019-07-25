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

class EdgeMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeMetrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'edge': 'UriReference',
            'event_time': 'datetime',
            'up_time_msec': 'int',
            'processors': 'list[EdgeMetricsProcessor]',
            'memory': 'list[EdgeMetricsMemory]',
            'disks': 'list[EdgeMetricsDisk]',
            'subsystems': 'list[EdgeMetricsSubsystem]',
            'networks': 'list[EdgeMetricsNetwork]'
        }

        self.attribute_map = {
            'edge': 'edge',
            'event_time': 'eventTime',
            'up_time_msec': 'upTimeMsec',
            'processors': 'processors',
            'memory': 'memory',
            'disks': 'disks',
            'subsystems': 'subsystems',
            'networks': 'networks'
        }

        self._edge = None
        self._event_time = None
        self._up_time_msec = None
        self._processors = None
        self._memory = None
        self._disks = None
        self._subsystems = None
        self._networks = None

    @property
    def edge(self):
        """
        Gets the edge of this EdgeMetrics.


        :return: The edge of this EdgeMetrics.
        :rtype: UriReference
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        """
        Sets the edge of this EdgeMetrics.


        :param edge: The edge of this EdgeMetrics.
        :type: UriReference
        """
        
        self._edge = edge

    @property
    def event_time(self):
        """
        Gets the event_time of this EdgeMetrics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The event_time of this EdgeMetrics.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this EdgeMetrics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param event_time: The event_time of this EdgeMetrics.
        :type: datetime
        """
        
        self._event_time = event_time

    @property
    def up_time_msec(self):
        """
        Gets the up_time_msec of this EdgeMetrics.


        :return: The up_time_msec of this EdgeMetrics.
        :rtype: int
        """
        return self._up_time_msec

    @up_time_msec.setter
    def up_time_msec(self, up_time_msec):
        """
        Sets the up_time_msec of this EdgeMetrics.


        :param up_time_msec: The up_time_msec of this EdgeMetrics.
        :type: int
        """
        
        self._up_time_msec = up_time_msec

    @property
    def processors(self):
        """
        Gets the processors of this EdgeMetrics.


        :return: The processors of this EdgeMetrics.
        :rtype: list[EdgeMetricsProcessor]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """
        Sets the processors of this EdgeMetrics.


        :param processors: The processors of this EdgeMetrics.
        :type: list[EdgeMetricsProcessor]
        """
        
        self._processors = processors

    @property
    def memory(self):
        """
        Gets the memory of this EdgeMetrics.


        :return: The memory of this EdgeMetrics.
        :rtype: list[EdgeMetricsMemory]
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this EdgeMetrics.


        :param memory: The memory of this EdgeMetrics.
        :type: list[EdgeMetricsMemory]
        """
        
        self._memory = memory

    @property
    def disks(self):
        """
        Gets the disks of this EdgeMetrics.


        :return: The disks of this EdgeMetrics.
        :rtype: list[EdgeMetricsDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this EdgeMetrics.


        :param disks: The disks of this EdgeMetrics.
        :type: list[EdgeMetricsDisk]
        """
        
        self._disks = disks

    @property
    def subsystems(self):
        """
        Gets the subsystems of this EdgeMetrics.


        :return: The subsystems of this EdgeMetrics.
        :rtype: list[EdgeMetricsSubsystem]
        """
        return self._subsystems

    @subsystems.setter
    def subsystems(self, subsystems):
        """
        Sets the subsystems of this EdgeMetrics.


        :param subsystems: The subsystems of this EdgeMetrics.
        :type: list[EdgeMetricsSubsystem]
        """
        
        self._subsystems = subsystems

    @property
    def networks(self):
        """
        Gets the networks of this EdgeMetrics.


        :return: The networks of this EdgeMetrics.
        :rtype: list[EdgeMetricsNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """
        Sets the networks of this EdgeMetrics.


        :param networks: The networks of this EdgeMetrics.
        :type: list[EdgeMetricsNetwork]
        """
        
        self._networks = networks

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

