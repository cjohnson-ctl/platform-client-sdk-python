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

class IntradayHistoricalQueueData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IntradayHistoricalQueueData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'offered': 'int',
            'completed': 'int',
            'answered': 'int',
            'abandoned': 'int',
            'average_talk_time_seconds': 'float',
            'average_after_call_work_seconds': 'float',
            'service_level_percent': 'float',
            'average_speed_of_answer_seconds': 'float'
        }

        self.attribute_map = {
            'offered': 'offered',
            'completed': 'completed',
            'answered': 'answered',
            'abandoned': 'abandoned',
            'average_talk_time_seconds': 'averageTalkTimeSeconds',
            'average_after_call_work_seconds': 'averageAfterCallWorkSeconds',
            'service_level_percent': 'serviceLevelPercent',
            'average_speed_of_answer_seconds': 'averageSpeedOfAnswerSeconds'
        }

        self._offered = None
        self._completed = None
        self._answered = None
        self._abandoned = None
        self._average_talk_time_seconds = None
        self._average_after_call_work_seconds = None
        self._service_level_percent = None
        self._average_speed_of_answer_seconds = None

    @property
    def offered(self):
        """
        Gets the offered of this IntradayHistoricalQueueData.
        The number of interactions routed into the queue for the given media type(s) for an agent to answer

        :return: The offered of this IntradayHistoricalQueueData.
        :rtype: int
        """
        return self._offered

    @offered.setter
    def offered(self, offered):
        """
        Sets the offered of this IntradayHistoricalQueueData.
        The number of interactions routed into the queue for the given media type(s) for an agent to answer

        :param offered: The offered of this IntradayHistoricalQueueData.
        :type: int
        """
        
        self._offered = offered

    @property
    def completed(self):
        """
        Gets the completed of this IntradayHistoricalQueueData.
        The number of interactions completed

        :return: The completed of this IntradayHistoricalQueueData.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this IntradayHistoricalQueueData.
        The number of interactions completed

        :param completed: The completed of this IntradayHistoricalQueueData.
        :type: int
        """
        
        self._completed = completed

    @property
    def answered(self):
        """
        Gets the answered of this IntradayHistoricalQueueData.
        The number of interactions answered by an agent in a given period

        :return: The answered of this IntradayHistoricalQueueData.
        :rtype: int
        """
        return self._answered

    @answered.setter
    def answered(self, answered):
        """
        Sets the answered of this IntradayHistoricalQueueData.
        The number of interactions answered by an agent in a given period

        :param answered: The answered of this IntradayHistoricalQueueData.
        :type: int
        """
        
        self._answered = answered

    @property
    def abandoned(self):
        """
        Gets the abandoned of this IntradayHistoricalQueueData.
        The number of customers who disconnect before connecting with an agent

        :return: The abandoned of this IntradayHistoricalQueueData.
        :rtype: int
        """
        return self._abandoned

    @abandoned.setter
    def abandoned(self, abandoned):
        """
        Sets the abandoned of this IntradayHistoricalQueueData.
        The number of customers who disconnect before connecting with an agent

        :param abandoned: The abandoned of this IntradayHistoricalQueueData.
        :type: int
        """
        
        self._abandoned = abandoned

    @property
    def average_talk_time_seconds(self):
        """
        Gets the average_talk_time_seconds of this IntradayHistoricalQueueData.
        The average time in seconds an agent spends interacting with a customer per talk segment for a defined period of time

        :return: The average_talk_time_seconds of this IntradayHistoricalQueueData.
        :rtype: float
        """
        return self._average_talk_time_seconds

    @average_talk_time_seconds.setter
    def average_talk_time_seconds(self, average_talk_time_seconds):
        """
        Sets the average_talk_time_seconds of this IntradayHistoricalQueueData.
        The average time in seconds an agent spends interacting with a customer per talk segment for a defined period of time

        :param average_talk_time_seconds: The average_talk_time_seconds of this IntradayHistoricalQueueData.
        :type: float
        """
        
        self._average_talk_time_seconds = average_talk_time_seconds

    @property
    def average_after_call_work_seconds(self):
        """
        Gets the average_after_call_work_seconds of this IntradayHistoricalQueueData.
        The average time in seconds spent in after-call work. After-call work is the work that an agent performs immediately following an interaction

        :return: The average_after_call_work_seconds of this IntradayHistoricalQueueData.
        :rtype: float
        """
        return self._average_after_call_work_seconds

    @average_after_call_work_seconds.setter
    def average_after_call_work_seconds(self, average_after_call_work_seconds):
        """
        Sets the average_after_call_work_seconds of this IntradayHistoricalQueueData.
        The average time in seconds spent in after-call work. After-call work is the work that an agent performs immediately following an interaction

        :param average_after_call_work_seconds: The average_after_call_work_seconds of this IntradayHistoricalQueueData.
        :type: float
        """
        
        self._average_after_call_work_seconds = average_after_call_work_seconds

    @property
    def service_level_percent(self):
        """
        Gets the service_level_percent of this IntradayHistoricalQueueData.
        Percent of interactions answered in X seconds, where X is the service level objective configured in the service goal group matching this intraday group

        :return: The service_level_percent of this IntradayHistoricalQueueData.
        :rtype: float
        """
        return self._service_level_percent

    @service_level_percent.setter
    def service_level_percent(self, service_level_percent):
        """
        Sets the service_level_percent of this IntradayHistoricalQueueData.
        Percent of interactions answered in X seconds, where X is the service level objective configured in the service goal group matching this intraday group

        :param service_level_percent: The service_level_percent of this IntradayHistoricalQueueData.
        :type: float
        """
        
        self._service_level_percent = service_level_percent

    @property
    def average_speed_of_answer_seconds(self):
        """
        Gets the average_speed_of_answer_seconds of this IntradayHistoricalQueueData.
        The average time in seconds it takes to answer an interaction once the interaction becomes available to be routed

        :return: The average_speed_of_answer_seconds of this IntradayHistoricalQueueData.
        :rtype: float
        """
        return self._average_speed_of_answer_seconds

    @average_speed_of_answer_seconds.setter
    def average_speed_of_answer_seconds(self, average_speed_of_answer_seconds):
        """
        Sets the average_speed_of_answer_seconds of this IntradayHistoricalQueueData.
        The average time in seconds it takes to answer an interaction once the interaction becomes available to be routed

        :param average_speed_of_answer_seconds: The average_speed_of_answer_seconds of this IntradayHistoricalQueueData.
        :type: float
        """
        
        self._average_speed_of_answer_seconds = average_speed_of_answer_seconds

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

