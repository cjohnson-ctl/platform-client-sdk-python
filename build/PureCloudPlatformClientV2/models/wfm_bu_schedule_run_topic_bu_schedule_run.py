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

class WfmBuScheduleRunTopicBuScheduleRun(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmBuScheduleRunTopicBuScheduleRun - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'percent_complete': 'float',
            'intraday_rescheduling': 'bool',
            'state': 'str',
            'week_count': 'int',
            'schedule': 'WfmBuScheduleRunTopicBuScheduleReference',
            'scheduling_canceled_by': 'WfmBuScheduleRunTopicUserReference',
            'scheduling_completed_time': 'str',
            'message_count': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'percent_complete': 'percentComplete',
            'intraday_rescheduling': 'intradayRescheduling',
            'state': 'state',
            'week_count': 'weekCount',
            'schedule': 'schedule',
            'scheduling_canceled_by': 'schedulingCanceledBy',
            'scheduling_completed_time': 'schedulingCompletedTime',
            'message_count': 'messageCount'
        }

        self._id = None
        self._percent_complete = None
        self._intraday_rescheduling = None
        self._state = None
        self._week_count = None
        self._schedule = None
        self._scheduling_canceled_by = None
        self._scheduling_completed_time = None
        self._message_count = None

    @property
    def id(self):
        """
        Gets the id of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The id of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmBuScheduleRunTopicBuScheduleRun.


        :param id: The id of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: str
        """
        
        self._id = id

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The percent_complete of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WfmBuScheduleRunTopicBuScheduleRun.


        :param percent_complete: The percent_complete of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: float
        """
        
        self._percent_complete = percent_complete

    @property
    def intraday_rescheduling(self):
        """
        Gets the intraday_rescheduling of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The intraday_rescheduling of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: bool
        """
        return self._intraday_rescheduling

    @intraday_rescheduling.setter
    def intraday_rescheduling(self, intraday_rescheduling):
        """
        Sets the intraday_rescheduling of this WfmBuScheduleRunTopicBuScheduleRun.


        :param intraday_rescheduling: The intraday_rescheduling of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: bool
        """
        
        self._intraday_rescheduling = intraday_rescheduling

    @property
    def state(self):
        """
        Gets the state of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The state of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this WfmBuScheduleRunTopicBuScheduleRun.


        :param state: The state of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: str
        """
        allowed_values = ["None", "Queued", "Scheduling", "Canceled", "Failed", "Complete"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def week_count(self):
        """
        Gets the week_count of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The week_count of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count):
        """
        Sets the week_count of this WfmBuScheduleRunTopicBuScheduleRun.


        :param week_count: The week_count of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: int
        """
        
        self._week_count = week_count

    @property
    def schedule(self):
        """
        Gets the schedule of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The schedule of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: WfmBuScheduleRunTopicBuScheduleReference
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this WfmBuScheduleRunTopicBuScheduleRun.


        :param schedule: The schedule of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: WfmBuScheduleRunTopicBuScheduleReference
        """
        
        self._schedule = schedule

    @property
    def scheduling_canceled_by(self):
        """
        Gets the scheduling_canceled_by of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The scheduling_canceled_by of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: WfmBuScheduleRunTopicUserReference
        """
        return self._scheduling_canceled_by

    @scheduling_canceled_by.setter
    def scheduling_canceled_by(self, scheduling_canceled_by):
        """
        Sets the scheduling_canceled_by of this WfmBuScheduleRunTopicBuScheduleRun.


        :param scheduling_canceled_by: The scheduling_canceled_by of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: WfmBuScheduleRunTopicUserReference
        """
        
        self._scheduling_canceled_by = scheduling_canceled_by

    @property
    def scheduling_completed_time(self):
        """
        Gets the scheduling_completed_time of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The scheduling_completed_time of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: str
        """
        return self._scheduling_completed_time

    @scheduling_completed_time.setter
    def scheduling_completed_time(self, scheduling_completed_time):
        """
        Sets the scheduling_completed_time of this WfmBuScheduleRunTopicBuScheduleRun.


        :param scheduling_completed_time: The scheduling_completed_time of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: str
        """
        
        self._scheduling_completed_time = scheduling_completed_time

    @property
    def message_count(self):
        """
        Gets the message_count of this WfmBuScheduleRunTopicBuScheduleRun.


        :return: The message_count of this WfmBuScheduleRunTopicBuScheduleRun.
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count):
        """
        Sets the message_count of this WfmBuScheduleRunTopicBuScheduleRun.


        :param message_count: The message_count of this WfmBuScheduleRunTopicBuScheduleRun.
        :type: int
        """
        
        self._message_count = message_count

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

