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

class HistoricalAdherenceExceptionInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HistoricalAdherenceExceptionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_offset_seconds': 'int',
            'end_offset_seconds': 'int',
            'scheduled_activity_code_id': 'str',
            'scheduled_activity_category': 'str',
            'actual_activity_category': 'str',
            'system_presence': 'str',
            'routing_status': 'RoutingStatus',
            'impact': 'str',
            'secondary_presence_lookup_id': 'str'
        }

        self.attribute_map = {
            'start_offset_seconds': 'startOffsetSeconds',
            'end_offset_seconds': 'endOffsetSeconds',
            'scheduled_activity_code_id': 'scheduledActivityCodeId',
            'scheduled_activity_category': 'scheduledActivityCategory',
            'actual_activity_category': 'actualActivityCategory',
            'system_presence': 'systemPresence',
            'routing_status': 'routingStatus',
            'impact': 'impact',
            'secondary_presence_lookup_id': 'secondaryPresenceLookupId'
        }

        self._start_offset_seconds = None
        self._end_offset_seconds = None
        self._scheduled_activity_code_id = None
        self._scheduled_activity_category = None
        self._actual_activity_category = None
        self._system_presence = None
        self._routing_status = None
        self._impact = None
        self._secondary_presence_lookup_id = None

    @property
    def start_offset_seconds(self):
        """
        Gets the start_offset_seconds of this HistoricalAdherenceExceptionInfo.
        Exception start offset in seconds relative to query start time

        :return: The start_offset_seconds of this HistoricalAdherenceExceptionInfo.
        :rtype: int
        """
        return self._start_offset_seconds

    @start_offset_seconds.setter
    def start_offset_seconds(self, start_offset_seconds):
        """
        Sets the start_offset_seconds of this HistoricalAdherenceExceptionInfo.
        Exception start offset in seconds relative to query start time

        :param start_offset_seconds: The start_offset_seconds of this HistoricalAdherenceExceptionInfo.
        :type: int
        """
        
        self._start_offset_seconds = start_offset_seconds

    @property
    def end_offset_seconds(self):
        """
        Gets the end_offset_seconds of this HistoricalAdherenceExceptionInfo.
        Exception end offset in seconds relative to query start time

        :return: The end_offset_seconds of this HistoricalAdherenceExceptionInfo.
        :rtype: int
        """
        return self._end_offset_seconds

    @end_offset_seconds.setter
    def end_offset_seconds(self, end_offset_seconds):
        """
        Sets the end_offset_seconds of this HistoricalAdherenceExceptionInfo.
        Exception end offset in seconds relative to query start time

        :param end_offset_seconds: The end_offset_seconds of this HistoricalAdherenceExceptionInfo.
        :type: int
        """
        
        self._end_offset_seconds = end_offset_seconds

    @property
    def scheduled_activity_code_id(self):
        """
        Gets the scheduled_activity_code_id of this HistoricalAdherenceExceptionInfo.
        The ID of the scheduled activity for this user

        :return: The scheduled_activity_code_id of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._scheduled_activity_code_id

    @scheduled_activity_code_id.setter
    def scheduled_activity_code_id(self, scheduled_activity_code_id):
        """
        Sets the scheduled_activity_code_id of this HistoricalAdherenceExceptionInfo.
        The ID of the scheduled activity for this user

        :param scheduled_activity_code_id: The scheduled_activity_code_id of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        
        self._scheduled_activity_code_id = scheduled_activity_code_id

    @property
    def scheduled_activity_category(self):
        """
        Gets the scheduled_activity_category of this HistoricalAdherenceExceptionInfo.
        Activity for which the user is scheduled

        :return: The scheduled_activity_category of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._scheduled_activity_category

    @scheduled_activity_category.setter
    def scheduled_activity_category(self, scheduled_activity_category):
        """
        Sets the scheduled_activity_category of this HistoricalAdherenceExceptionInfo.
        Activity for which the user is scheduled

        :param scheduled_activity_category: The scheduled_activity_category of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if scheduled_activity_category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for scheduled_activity_category -> " + scheduled_activity_category)
            self._scheduled_activity_category = "outdated_sdk_version"
        else:
            self._scheduled_activity_category = scheduled_activity_category

    @property
    def actual_activity_category(self):
        """
        Gets the actual_activity_category of this HistoricalAdherenceExceptionInfo.
        Activity for which the user is actually engaged

        :return: The actual_activity_category of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._actual_activity_category

    @actual_activity_category.setter
    def actual_activity_category(self, actual_activity_category):
        """
        Sets the actual_activity_category of this HistoricalAdherenceExceptionInfo.
        Activity for which the user is actually engaged

        :param actual_activity_category: The actual_activity_category of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if actual_activity_category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for actual_activity_category -> " + actual_activity_category)
            self._actual_activity_category = "outdated_sdk_version"
        else:
            self._actual_activity_category = actual_activity_category

    @property
    def system_presence(self):
        """
        Gets the system_presence of this HistoricalAdherenceExceptionInfo.
        Actual underlying system presence value

        :return: The system_presence of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._system_presence

    @system_presence.setter
    def system_presence(self, system_presence):
        """
        Sets the system_presence of this HistoricalAdherenceExceptionInfo.
        Actual underlying system presence value

        :param system_presence: The system_presence of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        allowed_values = ["Available", "Away", "Busy", "Offline", "Idle", "OnQueue", "Meal", "Training", "Meeting", "Break"]
        if system_presence.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for system_presence -> " + system_presence)
            self._system_presence = "outdated_sdk_version"
        else:
            self._system_presence = system_presence

    @property
    def routing_status(self):
        """
        Gets the routing_status of this HistoricalAdherenceExceptionInfo.
        Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue

        :return: The routing_status of this HistoricalAdherenceExceptionInfo.
        :rtype: RoutingStatus
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this HistoricalAdherenceExceptionInfo.
        Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue

        :param routing_status: The routing_status of this HistoricalAdherenceExceptionInfo.
        :type: RoutingStatus
        """
        
        self._routing_status = routing_status

    @property
    def impact(self):
        """
        Gets the impact of this HistoricalAdherenceExceptionInfo.
        The impact of the current adherence state for this user

        :return: The impact of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """
        Sets the impact of this HistoricalAdherenceExceptionInfo.
        The impact of the current adherence state for this user

        :param impact: The impact of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        allowed_values = ["Positive", "Negative", "Neutral", "Unknown"]
        if impact.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for impact -> " + impact)
            self._impact = "outdated_sdk_version"
        else:
            self._impact = impact

    @property
    def secondary_presence_lookup_id(self):
        """
        Gets the secondary_presence_lookup_id of this HistoricalAdherenceExceptionInfo.
        The lookup ID used to retrieve secondary status from map of lookup ID to corresponding secondary presence ID

        :return: The secondary_presence_lookup_id of this HistoricalAdherenceExceptionInfo.
        :rtype: str
        """
        return self._secondary_presence_lookup_id

    @secondary_presence_lookup_id.setter
    def secondary_presence_lookup_id(self, secondary_presence_lookup_id):
        """
        Sets the secondary_presence_lookup_id of this HistoricalAdherenceExceptionInfo.
        The lookup ID used to retrieve secondary status from map of lookup ID to corresponding secondary presence ID

        :param secondary_presence_lookup_id: The secondary_presence_lookup_id of this HistoricalAdherenceExceptionInfo.
        :type: str
        """
        
        self._secondary_presence_lookup_id = secondary_presence_lookup_id

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

