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

class WfmHistoricalAdherenceQueryForUsers(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmHistoricalAdherenceQueryForUsers - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'time_zone': 'str',
            'user_ids': 'list[str]',
            'team_ids': 'list[str]',
            'include_exceptions': 'bool'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'time_zone': 'timeZone',
            'user_ids': 'userIds',
            'team_ids': 'teamIds',
            'include_exceptions': 'includeExceptions'
        }

        self._start_date = None
        self._end_date = None
        self._time_zone = None
        self._user_ids = None
        self._team_ids = None
        self._include_exceptions = None

    @property
    def start_date(self):
        """
        Gets the start_date of this WfmHistoricalAdherenceQueryForUsers.
        Beginning of the date range to query in ISO-8601 format

        :return: The start_date of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this WfmHistoricalAdherenceQueryForUsers.
        Beginning of the date range to query in ISO-8601 format

        :param start_date: The start_date of this WfmHistoricalAdherenceQueryForUsers.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this WfmHistoricalAdherenceQueryForUsers.
        End of the date range to query in ISO-8601 format. If it is not set, end date will be set to current time

        :return: The end_date of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this WfmHistoricalAdherenceQueryForUsers.
        End of the date range to query in ISO-8601 format. If it is not set, end date will be set to current time

        :param end_date: The end_date of this WfmHistoricalAdherenceQueryForUsers.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def time_zone(self):
        """
        Gets the time_zone of this WfmHistoricalAdherenceQueryForUsers.
        The time zone to use for returned results in olson format. If it is not set, the business unit time zone will be used to compute adherence

        :return: The time_zone of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this WfmHistoricalAdherenceQueryForUsers.
        The time zone to use for returned results in olson format. If it is not set, the business unit time zone will be used to compute adherence

        :param time_zone: The time_zone of this WfmHistoricalAdherenceQueryForUsers.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def user_ids(self):
        """
        Gets the user_ids of this WfmHistoricalAdherenceQueryForUsers.
        The userIds to report on. Note: Only one of [teamIds, userIds] can be requested

        :return: The user_ids of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """
        Sets the user_ids of this WfmHistoricalAdherenceQueryForUsers.
        The userIds to report on. Note: Only one of [teamIds, userIds] can be requested

        :param user_ids: The user_ids of this WfmHistoricalAdherenceQueryForUsers.
        :type: list[str]
        """
        
        self._user_ids = user_ids

    @property
    def team_ids(self):
        """
        Gets the team_ids of this WfmHistoricalAdherenceQueryForUsers.
        The teamIds to report on. Note: Only one of [teamIds, userIds] can be requested

        :return: The team_ids of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: list[str]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """
        Sets the team_ids of this WfmHistoricalAdherenceQueryForUsers.
        The teamIds to report on. Note: Only one of [teamIds, userIds] can be requested

        :param team_ids: The team_ids of this WfmHistoricalAdherenceQueryForUsers.
        :type: list[str]
        """
        
        self._team_ids = team_ids

    @property
    def include_exceptions(self):
        """
        Gets the include_exceptions of this WfmHistoricalAdherenceQueryForUsers.
        Whether user exceptions should be returned as part of the results

        :return: The include_exceptions of this WfmHistoricalAdherenceQueryForUsers.
        :rtype: bool
        """
        return self._include_exceptions

    @include_exceptions.setter
    def include_exceptions(self, include_exceptions):
        """
        Sets the include_exceptions of this WfmHistoricalAdherenceQueryForUsers.
        Whether user exceptions should be returned as part of the results

        :param include_exceptions: The include_exceptions of this WfmHistoricalAdherenceQueryForUsers.
        :type: bool
        """
        
        self._include_exceptions = include_exceptions

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

