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

class UserScheduleAdherence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserScheduleAdherence - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'user': 'User',
            'management_unit': 'ManagementUnit',
            'scheduled_activity_category': 'str',
            'system_presence': 'str',
            'organization_secondary_presence_id': 'str',
            'routing_status': 'str',
            'actual_activity_category': 'str',
            'is_out_of_office': 'bool',
            'adherence_state': 'str',
            'impact': 'str',
            'time_of_adherence_change': 'datetime',
            'presence_update_time': 'datetime',
            'active_queues': 'list[QueueReference]',
            'active_queues_modified_time': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'user': 'user',
            'management_unit': 'managementUnit',
            'scheduled_activity_category': 'scheduledActivityCategory',
            'system_presence': 'systemPresence',
            'organization_secondary_presence_id': 'organizationSecondaryPresenceId',
            'routing_status': 'routingStatus',
            'actual_activity_category': 'actualActivityCategory',
            'is_out_of_office': 'isOutOfOffice',
            'adherence_state': 'adherenceState',
            'impact': 'impact',
            'time_of_adherence_change': 'timeOfAdherenceChange',
            'presence_update_time': 'presenceUpdateTime',
            'active_queues': 'activeQueues',
            'active_queues_modified_time': 'activeQueuesModifiedTime',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._user = None
        self._management_unit = None
        self._scheduled_activity_category = None
        self._system_presence = None
        self._organization_secondary_presence_id = None
        self._routing_status = None
        self._actual_activity_category = None
        self._is_out_of_office = None
        self._adherence_state = None
        self._impact = None
        self._time_of_adherence_change = None
        self._presence_update_time = None
        self._active_queues = None
        self._active_queues_modified_time = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UserScheduleAdherence.
        The globally unique identifier for the object.

        :return: The id of this UserScheduleAdherence.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserScheduleAdherence.
        The globally unique identifier for the object.

        :param id: The id of this UserScheduleAdherence.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UserScheduleAdherence.


        :return: The name of this UserScheduleAdherence.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserScheduleAdherence.


        :param name: The name of this UserScheduleAdherence.
        :type: str
        """
        
        self._name = name

    @property
    def user(self):
        """
        Gets the user of this UserScheduleAdherence.
        The user for whom this status applies

        :return: The user of this UserScheduleAdherence.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserScheduleAdherence.
        The user for whom this status applies

        :param user: The user of this UserScheduleAdherence.
        :type: User
        """
        
        self._user = user

    @property
    def management_unit(self):
        """
        Gets the management_unit of this UserScheduleAdherence.
        The management unit to which this user belongs

        :return: The management_unit of this UserScheduleAdherence.
        :rtype: ManagementUnit
        """
        return self._management_unit

    @management_unit.setter
    def management_unit(self, management_unit):
        """
        Sets the management_unit of this UserScheduleAdherence.
        The management unit to which this user belongs

        :param management_unit: The management_unit of this UserScheduleAdherence.
        :type: ManagementUnit
        """
        
        self._management_unit = management_unit

    @property
    def scheduled_activity_category(self):
        """
        Gets the scheduled_activity_category of this UserScheduleAdherence.
        Activity for which the user is scheduled

        :return: The scheduled_activity_category of this UserScheduleAdherence.
        :rtype: str
        """
        return self._scheduled_activity_category

    @scheduled_activity_category.setter
    def scheduled_activity_category(self, scheduled_activity_category):
        """
        Sets the scheduled_activity_category of this UserScheduleAdherence.
        Activity for which the user is scheduled

        :param scheduled_activity_category: The scheduled_activity_category of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if scheduled_activity_category.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for scheduled_activity_category -> " + scheduled_activity_category
            self._scheduled_activity_category = "outdated_sdk_version"
        else:
            self._scheduled_activity_category = scheduled_activity_category

    @property
    def system_presence(self):
        """
        Gets the system_presence of this UserScheduleAdherence.
        Actual underlying system presence value

        :return: The system_presence of this UserScheduleAdherence.
        :rtype: str
        """
        return self._system_presence

    @system_presence.setter
    def system_presence(self, system_presence):
        """
        Sets the system_presence of this UserScheduleAdherence.
        Actual underlying system presence value

        :param system_presence: The system_presence of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["Available", "Away", "Busy", "Offline", "Idle", "OnQueue", "Meal", "Training", "Meeting", "Break"]
        if system_presence.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for system_presence -> " + system_presence
            self._system_presence = "outdated_sdk_version"
        else:
            self._system_presence = system_presence

    @property
    def organization_secondary_presence_id(self):
        """
        Gets the organization_secondary_presence_id of this UserScheduleAdherence.
        Organization Secondary Presence Id.

        :return: The organization_secondary_presence_id of this UserScheduleAdherence.
        :rtype: str
        """
        return self._organization_secondary_presence_id

    @organization_secondary_presence_id.setter
    def organization_secondary_presence_id(self, organization_secondary_presence_id):
        """
        Sets the organization_secondary_presence_id of this UserScheduleAdherence.
        Organization Secondary Presence Id.

        :param organization_secondary_presence_id: The organization_secondary_presence_id of this UserScheduleAdherence.
        :type: str
        """
        
        self._organization_secondary_presence_id = organization_secondary_presence_id

    @property
    def routing_status(self):
        """
        Gets the routing_status of this UserScheduleAdherence.
        Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue

        :return: The routing_status of this UserScheduleAdherence.
        :rtype: str
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this UserScheduleAdherence.
        Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue

        :param routing_status: The routing_status of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["OFF_QUEUE", "IDLE", "INTERACTING", "NOT_RESPONDING", "COMMUNICATING"]
        if routing_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for routing_status -> " + routing_status
            self._routing_status = "outdated_sdk_version"
        else:
            self._routing_status = routing_status

    @property
    def actual_activity_category(self):
        """
        Gets the actual_activity_category of this UserScheduleAdherence.
        Activity in which the user is actually engaged

        :return: The actual_activity_category of this UserScheduleAdherence.
        :rtype: str
        """
        return self._actual_activity_category

    @actual_activity_category.setter
    def actual_activity_category(self, actual_activity_category):
        """
        Sets the actual_activity_category of this UserScheduleAdherence.
        Activity in which the user is actually engaged

        :param actual_activity_category: The actual_activity_category of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if actual_activity_category.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for actual_activity_category -> " + actual_activity_category
            self._actual_activity_category = "outdated_sdk_version"
        else:
            self._actual_activity_category = actual_activity_category

    @property
    def is_out_of_office(self):
        """
        Gets the is_out_of_office of this UserScheduleAdherence.
        Whether the user is marked OutOfOffice

        :return: The is_out_of_office of this UserScheduleAdherence.
        :rtype: bool
        """
        return self._is_out_of_office

    @is_out_of_office.setter
    def is_out_of_office(self, is_out_of_office):
        """
        Sets the is_out_of_office of this UserScheduleAdherence.
        Whether the user is marked OutOfOffice

        :param is_out_of_office: The is_out_of_office of this UserScheduleAdherence.
        :type: bool
        """
        
        self._is_out_of_office = is_out_of_office

    @property
    def adherence_state(self):
        """
        Gets the adherence_state of this UserScheduleAdherence.
        The user's current adherence state

        :return: The adherence_state of this UserScheduleAdherence.
        :rtype: str
        """
        return self._adherence_state

    @adherence_state.setter
    def adherence_state(self, adherence_state):
        """
        Sets the adherence_state of this UserScheduleAdherence.
        The user's current adherence state

        :param adherence_state: The adherence_state of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["InAdherence", "OutOfAdherence", "Unscheduled", "Unknown", "Ignored"]
        if adherence_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for adherence_state -> " + adherence_state
            self._adherence_state = "outdated_sdk_version"
        else:
            self._adherence_state = adherence_state

    @property
    def impact(self):
        """
        Gets the impact of this UserScheduleAdherence.
        The impact of the user's current adherenceState

        :return: The impact of this UserScheduleAdherence.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """
        Sets the impact of this UserScheduleAdherence.
        The impact of the user's current adherenceState

        :param impact: The impact of this UserScheduleAdherence.
        :type: str
        """
        allowed_values = ["Positive", "Negative", "Neutral", "Unknown"]
        if impact.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for impact -> " + impact
            self._impact = "outdated_sdk_version"
        else:
            self._impact = impact

    @property
    def time_of_adherence_change(self):
        """
        Gets the time_of_adherence_change of this UserScheduleAdherence.
        Time when the user entered the current adherenceState in ISO-8601 format

        :return: The time_of_adherence_change of this UserScheduleAdherence.
        :rtype: datetime
        """
        return self._time_of_adherence_change

    @time_of_adherence_change.setter
    def time_of_adherence_change(self, time_of_adherence_change):
        """
        Sets the time_of_adherence_change of this UserScheduleAdherence.
        Time when the user entered the current adherenceState in ISO-8601 format

        :param time_of_adherence_change: The time_of_adherence_change of this UserScheduleAdherence.
        :type: datetime
        """
        
        self._time_of_adherence_change = time_of_adherence_change

    @property
    def presence_update_time(self):
        """
        Gets the presence_update_time of this UserScheduleAdherence.
        Time when presence was last updated.  Used to calculate time in current status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The presence_update_time of this UserScheduleAdherence.
        :rtype: datetime
        """
        return self._presence_update_time

    @presence_update_time.setter
    def presence_update_time(self, presence_update_time):
        """
        Sets the presence_update_time of this UserScheduleAdherence.
        Time when presence was last updated.  Used to calculate time in current status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param presence_update_time: The presence_update_time of this UserScheduleAdherence.
        :type: datetime
        """
        
        self._presence_update_time = presence_update_time

    @property
    def active_queues(self):
        """
        Gets the active_queues of this UserScheduleAdherence.
        The list of queues to which this user is joined

        :return: The active_queues of this UserScheduleAdherence.
        :rtype: list[QueueReference]
        """
        return self._active_queues

    @active_queues.setter
    def active_queues(self, active_queues):
        """
        Sets the active_queues of this UserScheduleAdherence.
        The list of queues to which this user is joined

        :param active_queues: The active_queues of this UserScheduleAdherence.
        :type: list[QueueReference]
        """
        
        self._active_queues = active_queues

    @property
    def active_queues_modified_time(self):
        """
        Gets the active_queues_modified_time of this UserScheduleAdherence.
        Time when the list of active queues for this user was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The active_queues_modified_time of this UserScheduleAdherence.
        :rtype: datetime
        """
        return self._active_queues_modified_time

    @active_queues_modified_time.setter
    def active_queues_modified_time(self, active_queues_modified_time):
        """
        Sets the active_queues_modified_time of this UserScheduleAdherence.
        Time when the list of active queues for this user was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param active_queues_modified_time: The active_queues_modified_time of this UserScheduleAdherence.
        :type: datetime
        """
        
        self._active_queues_modified_time = active_queues_modified_time

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UserScheduleAdherence.
        The URI for this object

        :return: The self_uri of this UserScheduleAdherence.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UserScheduleAdherence.
        The URI for this object

        :param self_uri: The self_uri of this UserScheduleAdherence.
        :type: str
        """
        
        self._self_uri = self_uri

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

