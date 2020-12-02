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

class WemCoachingAppointmentTopicCoachingAppointmentNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WemCoachingAppointmentTopicCoachingAppointmentNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_start': 'datetime',
            'length_in_minutes': 'int',
            'status': 'str',
            'facilitator': 'WemCoachingAppointmentTopicUserReference',
            'attendees': 'list[WemCoachingAppointmentTopicUserReference]',
            'created_by': 'WemCoachingAppointmentTopicUserReference',
            'date_created': 'datetime',
            'modified_by': 'WemCoachingAppointmentTopicUserReference',
            'date_modified': 'datetime',
            'conversations': 'list[WemCoachingAppointmentTopicCoachingAppointmentConversation]',
            'documents': 'list[WemCoachingAppointmentTopicCoachingAppointmentDocument]',
            'change_type': 'str',
            'date_completed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_start': 'dateStart',
            'length_in_minutes': 'lengthInMinutes',
            'status': 'status',
            'facilitator': 'facilitator',
            'attendees': 'attendees',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'modified_by': 'modifiedBy',
            'date_modified': 'dateModified',
            'conversations': 'conversations',
            'documents': 'documents',
            'change_type': 'changeType',
            'date_completed': 'dateCompleted'
        }

        self._id = None
        self._name = None
        self._date_start = None
        self._length_in_minutes = None
        self._status = None
        self._facilitator = None
        self._attendees = None
        self._created_by = None
        self._date_created = None
        self._modified_by = None
        self._date_modified = None
        self._conversations = None
        self._documents = None
        self._change_type = None
        self._date_completed = None

    @property
    def id(self):
        """
        Gets the id of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The id of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param id: The id of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The name of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param name: The name of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: str
        """
        
        self._name = name

    @property
    def date_start(self):
        """
        Gets the date_start of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The date_start of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """
        Sets the date_start of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param date_start: The date_start of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: datetime
        """
        
        self._date_start = date_start

    @property
    def length_in_minutes(self):
        """
        Gets the length_in_minutes of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The length_in_minutes of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes):
        """
        Sets the length_in_minutes of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param length_in_minutes: The length_in_minutes of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: int
        """
        
        self._length_in_minutes = length_in_minutes

    @property
    def status(self):
        """
        Gets the status of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The status of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param status: The status of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: str
        """
        allowed_values = ["Scheduled", "InProgress", "Completed", "InvalidSchedule"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def facilitator(self):
        """
        Gets the facilitator of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The facilitator of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: WemCoachingAppointmentTopicUserReference
        """
        return self._facilitator

    @facilitator.setter
    def facilitator(self, facilitator):
        """
        Sets the facilitator of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param facilitator: The facilitator of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: WemCoachingAppointmentTopicUserReference
        """
        
        self._facilitator = facilitator

    @property
    def attendees(self):
        """
        Gets the attendees of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The attendees of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: list[WemCoachingAppointmentTopicUserReference]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """
        Sets the attendees of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param attendees: The attendees of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: list[WemCoachingAppointmentTopicUserReference]
        """
        
        self._attendees = attendees

    @property
    def created_by(self):
        """
        Gets the created_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The created_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: WemCoachingAppointmentTopicUserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param created_by: The created_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: WemCoachingAppointmentTopicUserReference
        """
        
        self._created_by = created_by

    @property
    def date_created(self):
        """
        Gets the date_created of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The date_created of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param date_created: The date_created of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def modified_by(self):
        """
        Gets the modified_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The modified_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: WemCoachingAppointmentTopicUserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param modified_by: The modified_by of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: WemCoachingAppointmentTopicUserReference
        """
        
        self._modified_by = modified_by

    @property
    def date_modified(self):
        """
        Gets the date_modified of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The date_modified of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param date_modified: The date_modified of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def conversations(self):
        """
        Gets the conversations of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The conversations of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: list[WemCoachingAppointmentTopicCoachingAppointmentConversation]
        """
        return self._conversations

    @conversations.setter
    def conversations(self, conversations):
        """
        Sets the conversations of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param conversations: The conversations of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: list[WemCoachingAppointmentTopicCoachingAppointmentConversation]
        """
        
        self._conversations = conversations

    @property
    def documents(self):
        """
        Gets the documents of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The documents of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: list[WemCoachingAppointmentTopicCoachingAppointmentDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param documents: The documents of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: list[WemCoachingAppointmentTopicCoachingAppointmentDocument]
        """
        
        self._documents = documents

    @property
    def change_type(self):
        """
        Gets the change_type of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The change_type of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """
        Sets the change_type of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param change_type: The change_type of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: str
        """
        allowed_values = ["Create", "Update", "Delete", "Invalidate"]
        if change_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for change_type -> " + change_type)
            self._change_type = "outdated_sdk_version"
        else:
            self._change_type = change_type

    @property
    def date_completed(self):
        """
        Gets the date_completed of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :return: The date_completed of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """
        Sets the date_completed of this WemCoachingAppointmentTopicCoachingAppointmentNotification.


        :param date_completed: The date_completed of this WemCoachingAppointmentTopicCoachingAppointmentNotification.
        :type: datetime
        """
        
        self._date_completed = date_completed

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

