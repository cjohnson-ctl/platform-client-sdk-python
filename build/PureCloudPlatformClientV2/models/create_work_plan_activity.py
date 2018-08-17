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


class CreateWorkPlanActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateWorkPlanActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_code_id': 'str',
            'description': 'str',
            'length_minutes': 'int',
            'start_time_is_relative_to_shift_start': 'bool',
            'flexible_start_time': 'bool',
            'earliest_start_time_minutes': 'int',
            'latest_start_time_minutes': 'int',
            'exact_start_time_minutes': 'int',
            'start_time_increment_minutes': 'int',
            'counts_as_paid_time': 'bool',
            'counts_as_contiguous_work_time': 'bool'
        }

        self.attribute_map = {
            'activity_code_id': 'activityCodeId',
            'description': 'description',
            'length_minutes': 'lengthMinutes',
            'start_time_is_relative_to_shift_start': 'startTimeIsRelativeToShiftStart',
            'flexible_start_time': 'flexibleStartTime',
            'earliest_start_time_minutes': 'earliestStartTimeMinutes',
            'latest_start_time_minutes': 'latestStartTimeMinutes',
            'exact_start_time_minutes': 'exactStartTimeMinutes',
            'start_time_increment_minutes': 'startTimeIncrementMinutes',
            'counts_as_paid_time': 'countsAsPaidTime',
            'counts_as_contiguous_work_time': 'countsAsContiguousWorkTime'
        }

        self._activity_code_id = None
        self._description = None
        self._length_minutes = None
        self._start_time_is_relative_to_shift_start = None
        self._flexible_start_time = None
        self._earliest_start_time_minutes = None
        self._latest_start_time_minutes = None
        self._exact_start_time_minutes = None
        self._start_time_increment_minutes = None
        self._counts_as_paid_time = None
        self._counts_as_contiguous_work_time = None

    @property
    def activity_code_id(self):
        """
        Gets the activity_code_id of this CreateWorkPlanActivity.
        ID of the activity code associated with this activity

        :return: The activity_code_id of this CreateWorkPlanActivity.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id):
        """
        Sets the activity_code_id of this CreateWorkPlanActivity.
        ID of the activity code associated with this activity

        :param activity_code_id: The activity_code_id of this CreateWorkPlanActivity.
        :type: str
        """
        
        self._activity_code_id = activity_code_id

    @property
    def description(self):
        """
        Gets the description of this CreateWorkPlanActivity.
        Description of the activity

        :return: The description of this CreateWorkPlanActivity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateWorkPlanActivity.
        Description of the activity

        :param description: The description of this CreateWorkPlanActivity.
        :type: str
        """
        
        self._description = description

    @property
    def length_minutes(self):
        """
        Gets the length_minutes of this CreateWorkPlanActivity.
        Length of the activity in minutes

        :return: The length_minutes of this CreateWorkPlanActivity.
        :rtype: int
        """
        return self._length_minutes

    @length_minutes.setter
    def length_minutes(self, length_minutes):
        """
        Sets the length_minutes of this CreateWorkPlanActivity.
        Length of the activity in minutes

        :param length_minutes: The length_minutes of this CreateWorkPlanActivity.
        :type: int
        """
        
        self._length_minutes = length_minutes

    @property
    def start_time_is_relative_to_shift_start(self):
        """
        Gets the start_time_is_relative_to_shift_start of this CreateWorkPlanActivity.
        Whether the start time of the activity is relative to the start time of the shift it belongs to

        :return: The start_time_is_relative_to_shift_start of this CreateWorkPlanActivity.
        :rtype: bool
        """
        return self._start_time_is_relative_to_shift_start

    @start_time_is_relative_to_shift_start.setter
    def start_time_is_relative_to_shift_start(self, start_time_is_relative_to_shift_start):
        """
        Sets the start_time_is_relative_to_shift_start of this CreateWorkPlanActivity.
        Whether the start time of the activity is relative to the start time of the shift it belongs to

        :param start_time_is_relative_to_shift_start: The start_time_is_relative_to_shift_start of this CreateWorkPlanActivity.
        :type: bool
        """
        
        self._start_time_is_relative_to_shift_start = start_time_is_relative_to_shift_start

    @property
    def flexible_start_time(self):
        """
        Gets the flexible_start_time of this CreateWorkPlanActivity.
        Whether the start time of the activity is flexible

        :return: The flexible_start_time of this CreateWorkPlanActivity.
        :rtype: bool
        """
        return self._flexible_start_time

    @flexible_start_time.setter
    def flexible_start_time(self, flexible_start_time):
        """
        Sets the flexible_start_time of this CreateWorkPlanActivity.
        Whether the start time of the activity is flexible

        :param flexible_start_time: The flexible_start_time of this CreateWorkPlanActivity.
        :type: bool
        """
        
        self._flexible_start_time = flexible_start_time

    @property
    def earliest_start_time_minutes(self):
        """
        Gets the earliest_start_time_minutes of this CreateWorkPlanActivity.
        Earliest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :return: The earliest_start_time_minutes of this CreateWorkPlanActivity.
        :rtype: int
        """
        return self._earliest_start_time_minutes

    @earliest_start_time_minutes.setter
    def earliest_start_time_minutes(self, earliest_start_time_minutes):
        """
        Sets the earliest_start_time_minutes of this CreateWorkPlanActivity.
        Earliest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :param earliest_start_time_minutes: The earliest_start_time_minutes of this CreateWorkPlanActivity.
        :type: int
        """
        
        self._earliest_start_time_minutes = earliest_start_time_minutes

    @property
    def latest_start_time_minutes(self):
        """
        Gets the latest_start_time_minutes of this CreateWorkPlanActivity.
        Latest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :return: The latest_start_time_minutes of this CreateWorkPlanActivity.
        :rtype: int
        """
        return self._latest_start_time_minutes

    @latest_start_time_minutes.setter
    def latest_start_time_minutes(self, latest_start_time_minutes):
        """
        Sets the latest_start_time_minutes of this CreateWorkPlanActivity.
        Latest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :param latest_start_time_minutes: The latest_start_time_minutes of this CreateWorkPlanActivity.
        :type: int
        """
        
        self._latest_start_time_minutes = latest_start_time_minutes

    @property
    def exact_start_time_minutes(self):
        """
        Gets the exact_start_time_minutes of this CreateWorkPlanActivity.
        Exact activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == false

        :return: The exact_start_time_minutes of this CreateWorkPlanActivity.
        :rtype: int
        """
        return self._exact_start_time_minutes

    @exact_start_time_minutes.setter
    def exact_start_time_minutes(self, exact_start_time_minutes):
        """
        Sets the exact_start_time_minutes of this CreateWorkPlanActivity.
        Exact activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == false

        :param exact_start_time_minutes: The exact_start_time_minutes of this CreateWorkPlanActivity.
        :type: int
        """
        
        self._exact_start_time_minutes = exact_start_time_minutes

    @property
    def start_time_increment_minutes(self):
        """
        Gets the start_time_increment_minutes of this CreateWorkPlanActivity.
        Increment in offset minutes that would contribute to different possible start times for the activity

        :return: The start_time_increment_minutes of this CreateWorkPlanActivity.
        :rtype: int
        """
        return self._start_time_increment_minutes

    @start_time_increment_minutes.setter
    def start_time_increment_minutes(self, start_time_increment_minutes):
        """
        Sets the start_time_increment_minutes of this CreateWorkPlanActivity.
        Increment in offset minutes that would contribute to different possible start times for the activity

        :param start_time_increment_minutes: The start_time_increment_minutes of this CreateWorkPlanActivity.
        :type: int
        """
        
        self._start_time_increment_minutes = start_time_increment_minutes

    @property
    def counts_as_paid_time(self):
        """
        Gets the counts_as_paid_time of this CreateWorkPlanActivity.
        Whether the activity is paid

        :return: The counts_as_paid_time of this CreateWorkPlanActivity.
        :rtype: bool
        """
        return self._counts_as_paid_time

    @counts_as_paid_time.setter
    def counts_as_paid_time(self, counts_as_paid_time):
        """
        Sets the counts_as_paid_time of this CreateWorkPlanActivity.
        Whether the activity is paid

        :param counts_as_paid_time: The counts_as_paid_time of this CreateWorkPlanActivity.
        :type: bool
        """
        
        self._counts_as_paid_time = counts_as_paid_time

    @property
    def counts_as_contiguous_work_time(self):
        """
        Gets the counts_as_contiguous_work_time of this CreateWorkPlanActivity.
        Whether the activity duration is counted towards contiguous work time

        :return: The counts_as_contiguous_work_time of this CreateWorkPlanActivity.
        :rtype: bool
        """
        return self._counts_as_contiguous_work_time

    @counts_as_contiguous_work_time.setter
    def counts_as_contiguous_work_time(self, counts_as_contiguous_work_time):
        """
        Sets the counts_as_contiguous_work_time of this CreateWorkPlanActivity.
        Whether the activity duration is counted towards contiguous work time

        :param counts_as_contiguous_work_time: The counts_as_contiguous_work_time of this CreateWorkPlanActivity.
        :type: bool
        """
        
        self._counts_as_contiguous_work_time = counts_as_contiguous_work_time

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
