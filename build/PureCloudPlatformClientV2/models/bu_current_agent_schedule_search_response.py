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

class BuCurrentAgentScheduleSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuCurrentAgentScheduleSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agent_schedules': 'list[BuAgentScheduleSearchResponse]',
            'business_unit_time_zone': 'str',
            'published_schedules': 'list[BuAgentSchedulePublishedScheduleReference]',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'updates': 'list[BuAgentScheduleUpdate]'
        }

        self.attribute_map = {
            'agent_schedules': 'agentSchedules',
            'business_unit_time_zone': 'businessUnitTimeZone',
            'published_schedules': 'publishedSchedules',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'updates': 'updates'
        }

        self._agent_schedules = None
        self._business_unit_time_zone = None
        self._published_schedules = None
        self._start_date = None
        self._end_date = None
        self._updates = None

    @property
    def agent_schedules(self):
        """
        Gets the agent_schedules of this BuCurrentAgentScheduleSearchResponse.
        The requested agent schedules

        :return: The agent_schedules of this BuCurrentAgentScheduleSearchResponse.
        :rtype: list[BuAgentScheduleSearchResponse]
        """
        return self._agent_schedules

    @agent_schedules.setter
    def agent_schedules(self, agent_schedules):
        """
        Sets the agent_schedules of this BuCurrentAgentScheduleSearchResponse.
        The requested agent schedules

        :param agent_schedules: The agent_schedules of this BuCurrentAgentScheduleSearchResponse.
        :type: list[BuAgentScheduleSearchResponse]
        """
        
        self._agent_schedules = agent_schedules

    @property
    def business_unit_time_zone(self):
        """
        Gets the business_unit_time_zone of this BuCurrentAgentScheduleSearchResponse.
        The time zone configured for the business unit to which this schedule applies

        :return: The business_unit_time_zone of this BuCurrentAgentScheduleSearchResponse.
        :rtype: str
        """
        return self._business_unit_time_zone

    @business_unit_time_zone.setter
    def business_unit_time_zone(self, business_unit_time_zone):
        """
        Sets the business_unit_time_zone of this BuCurrentAgentScheduleSearchResponse.
        The time zone configured for the business unit to which this schedule applies

        :param business_unit_time_zone: The business_unit_time_zone of this BuCurrentAgentScheduleSearchResponse.
        :type: str
        """
        
        self._business_unit_time_zone = business_unit_time_zone

    @property
    def published_schedules(self):
        """
        Gets the published_schedules of this BuCurrentAgentScheduleSearchResponse.
        References to all published week schedules overlapping the start/end date query parameters

        :return: The published_schedules of this BuCurrentAgentScheduleSearchResponse.
        :rtype: list[BuAgentSchedulePublishedScheduleReference]
        """
        return self._published_schedules

    @published_schedules.setter
    def published_schedules(self, published_schedules):
        """
        Sets the published_schedules of this BuCurrentAgentScheduleSearchResponse.
        References to all published week schedules overlapping the start/end date query parameters

        :param published_schedules: The published_schedules of this BuCurrentAgentScheduleSearchResponse.
        :type: list[BuAgentSchedulePublishedScheduleReference]
        """
        
        self._published_schedules = published_schedules

    @property
    def start_date(self):
        """
        Gets the start_date of this BuCurrentAgentScheduleSearchResponse.
        The start date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_date of this BuCurrentAgentScheduleSearchResponse.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this BuCurrentAgentScheduleSearchResponse.
        The start date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_date: The start_date of this BuCurrentAgentScheduleSearchResponse.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this BuCurrentAgentScheduleSearchResponse.
        The end date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The end_date of this BuCurrentAgentScheduleSearchResponse.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this BuCurrentAgentScheduleSearchResponse.
        The end date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param end_date: The end_date of this BuCurrentAgentScheduleSearchResponse.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def updates(self):
        """
        Gets the updates of this BuCurrentAgentScheduleSearchResponse.
        The list of updates for the schedule. Only used in notifications

        :return: The updates of this BuCurrentAgentScheduleSearchResponse.
        :rtype: list[BuAgentScheduleUpdate]
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """
        Sets the updates of this BuCurrentAgentScheduleSearchResponse.
        The list of updates for the schedule. Only used in notifications

        :param updates: The updates of this BuCurrentAgentScheduleSearchResponse.
        :type: list[BuAgentScheduleUpdate]
        """
        
        self._updates = updates

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

