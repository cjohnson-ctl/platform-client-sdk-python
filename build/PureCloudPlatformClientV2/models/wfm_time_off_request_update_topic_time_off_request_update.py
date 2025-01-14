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

class WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user': 'WfmTimeOffRequestUpdateTopicUserReference',
            'is_full_day_request': 'bool',
            'marked_as_read': 'bool',
            'activity_code_id': 'str',
            'paid': 'bool',
            'status': 'str',
            'substatus': 'str',
            'partial_day_start_date_times': 'list[str]',
            'full_day_management_unit_dates': 'list[str]',
            'daily_duration_minutes': 'int',
            'notes': 'str',
            'reviewed_date': 'str',
            'reviewed_by': 'str',
            'submitted_date': 'str',
            'submitted_by': 'str',
            'modified_date': 'str',
            'modified_by': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'is_full_day_request': 'isFullDayRequest',
            'marked_as_read': 'markedAsRead',
            'activity_code_id': 'activityCodeId',
            'paid': 'paid',
            'status': 'status',
            'substatus': 'substatus',
            'partial_day_start_date_times': 'partialDayStartDateTimes',
            'full_day_management_unit_dates': 'fullDayManagementUnitDates',
            'daily_duration_minutes': 'dailyDurationMinutes',
            'notes': 'notes',
            'reviewed_date': 'reviewedDate',
            'reviewed_by': 'reviewedBy',
            'submitted_date': 'submittedDate',
            'submitted_by': 'submittedBy',
            'modified_date': 'modifiedDate',
            'modified_by': 'modifiedBy'
        }

        self._id = None
        self._user = None
        self._is_full_day_request = None
        self._marked_as_read = None
        self._activity_code_id = None
        self._paid = None
        self._status = None
        self._substatus = None
        self._partial_day_start_date_times = None
        self._full_day_management_unit_dates = None
        self._daily_duration_minutes = None
        self._notes = None
        self._reviewed_date = None
        self._reviewed_by = None
        self._submitted_date = None
        self._submitted_by = None
        self._modified_date = None
        self._modified_by = None

    @property
    def id(self):
        """
        Gets the id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param id: The id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._id = id

    @property
    def user(self):
        """
        Gets the user of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The user of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: WfmTimeOffRequestUpdateTopicUserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param user: The user of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: WfmTimeOffRequestUpdateTopicUserReference
        """
        
        self._user = user

    @property
    def is_full_day_request(self):
        """
        Gets the is_full_day_request of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The is_full_day_request of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: bool
        """
        return self._is_full_day_request

    @is_full_day_request.setter
    def is_full_day_request(self, is_full_day_request):
        """
        Sets the is_full_day_request of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param is_full_day_request: The is_full_day_request of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: bool
        """
        
        self._is_full_day_request = is_full_day_request

    @property
    def marked_as_read(self):
        """
        Gets the marked_as_read of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The marked_as_read of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: bool
        """
        return self._marked_as_read

    @marked_as_read.setter
    def marked_as_read(self, marked_as_read):
        """
        Sets the marked_as_read of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param marked_as_read: The marked_as_read of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: bool
        """
        
        self._marked_as_read = marked_as_read

    @property
    def activity_code_id(self):
        """
        Gets the activity_code_id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The activity_code_id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id):
        """
        Sets the activity_code_id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param activity_code_id: The activity_code_id of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._activity_code_id = activity_code_id

    @property
    def paid(self):
        """
        Gets the paid of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The paid of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """
        Sets the paid of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param paid: The paid of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: bool
        """
        
        self._paid = paid

    @property
    def status(self):
        """
        Gets the status of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The status of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param status: The status of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        allowed_values = ["PENDING", "APPROVED", "DENIED", "CANCELED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def substatus(self):
        """
        Gets the substatus of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The substatus of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._substatus

    @substatus.setter
    def substatus(self, substatus):
        """
        Sets the substatus of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param substatus: The substatus of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        allowed_values = ["AdvanceTimeElapsed", "AutoApproved", "InvalidDailyDuration", "OutsideShift", "RemovedFromWaitlist", "Waitlisted"]
        if substatus.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for substatus -> " + substatus)
            self._substatus = "outdated_sdk_version"
        else:
            self._substatus = substatus

    @property
    def partial_day_start_date_times(self):
        """
        Gets the partial_day_start_date_times of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The partial_day_start_date_times of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: list[str]
        """
        return self._partial_day_start_date_times

    @partial_day_start_date_times.setter
    def partial_day_start_date_times(self, partial_day_start_date_times):
        """
        Sets the partial_day_start_date_times of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param partial_day_start_date_times: The partial_day_start_date_times of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: list[str]
        """
        
        self._partial_day_start_date_times = partial_day_start_date_times

    @property
    def full_day_management_unit_dates(self):
        """
        Gets the full_day_management_unit_dates of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The full_day_management_unit_dates of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: list[str]
        """
        return self._full_day_management_unit_dates

    @full_day_management_unit_dates.setter
    def full_day_management_unit_dates(self, full_day_management_unit_dates):
        """
        Sets the full_day_management_unit_dates of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param full_day_management_unit_dates: The full_day_management_unit_dates of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: list[str]
        """
        
        self._full_day_management_unit_dates = full_day_management_unit_dates

    @property
    def daily_duration_minutes(self):
        """
        Gets the daily_duration_minutes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The daily_duration_minutes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: int
        """
        return self._daily_duration_minutes

    @daily_duration_minutes.setter
    def daily_duration_minutes(self, daily_duration_minutes):
        """
        Sets the daily_duration_minutes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param daily_duration_minutes: The daily_duration_minutes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: int
        """
        
        self._daily_duration_minutes = daily_duration_minutes

    @property
    def notes(self):
        """
        Gets the notes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The notes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param notes: The notes of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._notes = notes

    @property
    def reviewed_date(self):
        """
        Gets the reviewed_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The reviewed_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._reviewed_date

    @reviewed_date.setter
    def reviewed_date(self, reviewed_date):
        """
        Sets the reviewed_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param reviewed_date: The reviewed_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._reviewed_date = reviewed_date

    @property
    def reviewed_by(self):
        """
        Gets the reviewed_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The reviewed_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._reviewed_by

    @reviewed_by.setter
    def reviewed_by(self, reviewed_by):
        """
        Sets the reviewed_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param reviewed_by: The reviewed_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._reviewed_by = reviewed_by

    @property
    def submitted_date(self):
        """
        Gets the submitted_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The submitted_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """
        Sets the submitted_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param submitted_date: The submitted_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._submitted_date = submitted_date

    @property
    def submitted_by(self):
        """
        Gets the submitted_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The submitted_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        """
        Sets the submitted_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param submitted_by: The submitted_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._submitted_by = submitted_by

    @property
    def modified_date(self):
        """
        Gets the modified_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The modified_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param modified_date: The modified_date of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._modified_date = modified_date

    @property
    def modified_by(self):
        """
        Gets the modified_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :return: The modified_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.


        :param modified_by: The modified_by of this WfmTimeOffRequestUpdateTopicTimeOffRequestUpdate.
        :type: str
        """
        
        self._modified_by = modified_by

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

