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


class IntradayDataUpdateNotificationIntradayDataGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IntradayDataUpdateNotificationIntradayDataGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'media_type': 'str',
            'forecast_data_per_interval': 'list[IntradayDataUpdateNotificationForecastDataPerInterval]',
            'schedule_data_per_interval': 'list[IntradayDataUpdateNotificationScheduleDataPerInterval]',
            'historical_agent_data_per_interval': 'list[IntradayDataUpdateNotificationHistoricalAgentDataPerInterval]',
            'historical_queue_data_per_interval': 'list[IntradayDataUpdateNotificationHistoricalQueueDataPerInterval]',
            'performance_prediction_agent_data_per_interval': 'list[IntradayDataUpdateNotificationPerformancePredictionAgentDataPerInterval]',
            'performance_prediction_queue_data_per_interval': 'list[IntradayDataUpdateNotificationPerformancePredictionQueueDataPerInterval]'
        }

        self.attribute_map = {
            'media_type': 'mediaType',
            'forecast_data_per_interval': 'forecastDataPerInterval',
            'schedule_data_per_interval': 'scheduleDataPerInterval',
            'historical_agent_data_per_interval': 'historicalAgentDataPerInterval',
            'historical_queue_data_per_interval': 'historicalQueueDataPerInterval',
            'performance_prediction_agent_data_per_interval': 'performancePredictionAgentDataPerInterval',
            'performance_prediction_queue_data_per_interval': 'performancePredictionQueueDataPerInterval'
        }

        self._media_type = None
        self._forecast_data_per_interval = None
        self._schedule_data_per_interval = None
        self._historical_agent_data_per_interval = None
        self._historical_queue_data_per_interval = None
        self._performance_prediction_agent_data_per_interval = None
        self._performance_prediction_queue_data_per_interval = None

    @property
    def media_type(self):
        """
        Gets the media_type of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The media_type of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param media_type: The media_type of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: str
        """
        allowed_values = ["Voice", "Chat", "Email", "Callback", "Message"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for media_type -> " + media_type
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def forecast_data_per_interval(self):
        """
        Gets the forecast_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The forecast_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationForecastDataPerInterval]
        """
        return self._forecast_data_per_interval

    @forecast_data_per_interval.setter
    def forecast_data_per_interval(self, forecast_data_per_interval):
        """
        Sets the forecast_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param forecast_data_per_interval: The forecast_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationForecastDataPerInterval]
        """
        
        self._forecast_data_per_interval = forecast_data_per_interval

    @property
    def schedule_data_per_interval(self):
        """
        Gets the schedule_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The schedule_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationScheduleDataPerInterval]
        """
        return self._schedule_data_per_interval

    @schedule_data_per_interval.setter
    def schedule_data_per_interval(self, schedule_data_per_interval):
        """
        Sets the schedule_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param schedule_data_per_interval: The schedule_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationScheduleDataPerInterval]
        """
        
        self._schedule_data_per_interval = schedule_data_per_interval

    @property
    def historical_agent_data_per_interval(self):
        """
        Gets the historical_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The historical_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationHistoricalAgentDataPerInterval]
        """
        return self._historical_agent_data_per_interval

    @historical_agent_data_per_interval.setter
    def historical_agent_data_per_interval(self, historical_agent_data_per_interval):
        """
        Sets the historical_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param historical_agent_data_per_interval: The historical_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationHistoricalAgentDataPerInterval]
        """
        
        self._historical_agent_data_per_interval = historical_agent_data_per_interval

    @property
    def historical_queue_data_per_interval(self):
        """
        Gets the historical_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The historical_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationHistoricalQueueDataPerInterval]
        """
        return self._historical_queue_data_per_interval

    @historical_queue_data_per_interval.setter
    def historical_queue_data_per_interval(self, historical_queue_data_per_interval):
        """
        Sets the historical_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param historical_queue_data_per_interval: The historical_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationHistoricalQueueDataPerInterval]
        """
        
        self._historical_queue_data_per_interval = historical_queue_data_per_interval

    @property
    def performance_prediction_agent_data_per_interval(self):
        """
        Gets the performance_prediction_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The performance_prediction_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationPerformancePredictionAgentDataPerInterval]
        """
        return self._performance_prediction_agent_data_per_interval

    @performance_prediction_agent_data_per_interval.setter
    def performance_prediction_agent_data_per_interval(self, performance_prediction_agent_data_per_interval):
        """
        Sets the performance_prediction_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param performance_prediction_agent_data_per_interval: The performance_prediction_agent_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationPerformancePredictionAgentDataPerInterval]
        """
        
        self._performance_prediction_agent_data_per_interval = performance_prediction_agent_data_per_interval

    @property
    def performance_prediction_queue_data_per_interval(self):
        """
        Gets the performance_prediction_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :return: The performance_prediction_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :rtype: list[IntradayDataUpdateNotificationPerformancePredictionQueueDataPerInterval]
        """
        return self._performance_prediction_queue_data_per_interval

    @performance_prediction_queue_data_per_interval.setter
    def performance_prediction_queue_data_per_interval(self, performance_prediction_queue_data_per_interval):
        """
        Sets the performance_prediction_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.


        :param performance_prediction_queue_data_per_interval: The performance_prediction_queue_data_per_interval of this IntradayDataUpdateNotificationIntradayDataGroup.
        :type: list[IntradayDataUpdateNotificationPerformancePredictionQueueDataPerInterval]
        """
        
        self._performance_prediction_queue_data_per_interval = performance_prediction_queue_data_per_interval

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

