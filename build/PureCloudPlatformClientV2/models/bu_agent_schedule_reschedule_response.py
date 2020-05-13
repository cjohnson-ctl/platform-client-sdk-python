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

class BuAgentScheduleRescheduleResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuAgentScheduleRescheduleResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'UserReference',
            'shifts': 'list[BuAgentScheduleShift]',
            'full_day_time_off_markers': 'list[BuFullDayTimeOffMarker]',
            'work_plan': 'WorkPlanReference'
        }

        self.attribute_map = {
            'user': 'user',
            'shifts': 'shifts',
            'full_day_time_off_markers': 'fullDayTimeOffMarkers',
            'work_plan': 'workPlan'
        }

        self._user = None
        self._shifts = None
        self._full_day_time_off_markers = None
        self._work_plan = None

    @property
    def user(self):
        """
        Gets the user of this BuAgentScheduleRescheduleResponse.
        The user to whom this agent schedule applies

        :return: The user of this BuAgentScheduleRescheduleResponse.
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this BuAgentScheduleRescheduleResponse.
        The user to whom this agent schedule applies

        :param user: The user of this BuAgentScheduleRescheduleResponse.
        :type: UserReference
        """
        
        self._user = user

    @property
    def shifts(self):
        """
        Gets the shifts of this BuAgentScheduleRescheduleResponse.
        The shift definitions for this agent schedule

        :return: The shifts of this BuAgentScheduleRescheduleResponse.
        :rtype: list[BuAgentScheduleShift]
        """
        return self._shifts

    @shifts.setter
    def shifts(self, shifts):
        """
        Sets the shifts of this BuAgentScheduleRescheduleResponse.
        The shift definitions for this agent schedule

        :param shifts: The shifts of this BuAgentScheduleRescheduleResponse.
        :type: list[BuAgentScheduleShift]
        """
        
        self._shifts = shifts

    @property
    def full_day_time_off_markers(self):
        """
        Gets the full_day_time_off_markers of this BuAgentScheduleRescheduleResponse.
        Full day time off markers which apply to this agent schedule

        :return: The full_day_time_off_markers of this BuAgentScheduleRescheduleResponse.
        :rtype: list[BuFullDayTimeOffMarker]
        """
        return self._full_day_time_off_markers

    @full_day_time_off_markers.setter
    def full_day_time_off_markers(self, full_day_time_off_markers):
        """
        Sets the full_day_time_off_markers of this BuAgentScheduleRescheduleResponse.
        Full day time off markers which apply to this agent schedule

        :param full_day_time_off_markers: The full_day_time_off_markers of this BuAgentScheduleRescheduleResponse.
        :type: list[BuFullDayTimeOffMarker]
        """
        
        self._full_day_time_off_markers = full_day_time_off_markers

    @property
    def work_plan(self):
        """
        Gets the work_plan of this BuAgentScheduleRescheduleResponse.
        The work plan for this user

        :return: The work_plan of this BuAgentScheduleRescheduleResponse.
        :rtype: WorkPlanReference
        """
        return self._work_plan

    @work_plan.setter
    def work_plan(self, work_plan):
        """
        Sets the work_plan of this BuAgentScheduleRescheduleResponse.
        The work plan for this user

        :param work_plan: The work_plan of this BuAgentScheduleRescheduleResponse.
        :type: WorkPlanReference
        """
        
        self._work_plan = work_plan

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

