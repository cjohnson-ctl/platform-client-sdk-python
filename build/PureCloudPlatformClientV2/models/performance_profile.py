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

class PerformanceProfile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PerformanceProfile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'description': 'str',
            'metric_orders': 'list[str]',
            'date_created': 'datetime',
            'reporting_intervals': 'list[ReportingInterval]',
            'active': 'bool',
            'max_leaderboard_rank_size': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'metric_orders': 'metricOrders',
            'date_created': 'dateCreated',
            'reporting_intervals': 'reportingIntervals',
            'active': 'active',
            'max_leaderboard_rank_size': 'maxLeaderboardRankSize',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._metric_orders = None
        self._date_created = None
        self._reporting_intervals = None
        self._active = None
        self._max_leaderboard_rank_size = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this PerformanceProfile.
        The globally unique identifier for the object.

        :return: The id of this PerformanceProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PerformanceProfile.
        The globally unique identifier for the object.

        :param id: The id of this PerformanceProfile.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PerformanceProfile.
        A name for this performance profile

        :return: The name of this PerformanceProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PerformanceProfile.
        A name for this performance profile

        :param name: The name of this PerformanceProfile.
        :type: str
        """
        
        self._name = name

    @property
    def division(self):
        """
        Gets the division of this PerformanceProfile.
        The division for this performance profile associate to

        :return: The division of this PerformanceProfile.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this PerformanceProfile.
        The division for this performance profile associate to

        :param division: The division of this PerformanceProfile.
        :type: Division
        """
        
        self._division = division

    @property
    def description(self):
        """
        Gets the description of this PerformanceProfile.
        A description about this performance profile

        :return: The description of this PerformanceProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PerformanceProfile.
        A description about this performance profile

        :param description: The description of this PerformanceProfile.
        :type: str
        """
        
        self._description = description

    @property
    def metric_orders(self):
        """
        Gets the metric_orders of this PerformanceProfile.
        Order of the associated metrics. The list should contain valid ids for metrics

        :return: The metric_orders of this PerformanceProfile.
        :rtype: list[str]
        """
        return self._metric_orders

    @metric_orders.setter
    def metric_orders(self, metric_orders):
        """
        Sets the metric_orders of this PerformanceProfile.
        Order of the associated metrics. The list should contain valid ids for metrics

        :param metric_orders: The metric_orders of this PerformanceProfile.
        :type: list[str]
        """
        
        self._metric_orders = metric_orders

    @property
    def date_created(self):
        """
        Gets the date_created of this PerformanceProfile.
        Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this PerformanceProfile.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this PerformanceProfile.
        Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this PerformanceProfile.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def reporting_intervals(self):
        """
        Gets the reporting_intervals of this PerformanceProfile.
        The reporting interval periods for this performance profile

        :return: The reporting_intervals of this PerformanceProfile.
        :rtype: list[ReportingInterval]
        """
        return self._reporting_intervals

    @reporting_intervals.setter
    def reporting_intervals(self, reporting_intervals):
        """
        Sets the reporting_intervals of this PerformanceProfile.
        The reporting interval periods for this performance profile

        :param reporting_intervals: The reporting_intervals of this PerformanceProfile.
        :type: list[ReportingInterval]
        """
        
        self._reporting_intervals = reporting_intervals

    @property
    def active(self):
        """
        Gets the active of this PerformanceProfile.
        The flag for active profiles

        :return: The active of this PerformanceProfile.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PerformanceProfile.
        The flag for active profiles

        :param active: The active of this PerformanceProfile.
        :type: bool
        """
        
        self._active = active

    @property
    def max_leaderboard_rank_size(self):
        """
        Gets the max_leaderboard_rank_size of this PerformanceProfile.
        The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries

        :return: The max_leaderboard_rank_size of this PerformanceProfile.
        :rtype: int
        """
        return self._max_leaderboard_rank_size

    @max_leaderboard_rank_size.setter
    def max_leaderboard_rank_size(self, max_leaderboard_rank_size):
        """
        Sets the max_leaderboard_rank_size of this PerformanceProfile.
        The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries

        :param max_leaderboard_rank_size: The max_leaderboard_rank_size of this PerformanceProfile.
        :type: int
        """
        
        self._max_leaderboard_rank_size = max_leaderboard_rank_size

    @property
    def self_uri(self):
        """
        Gets the self_uri of this PerformanceProfile.
        The URI for this object

        :return: The self_uri of this PerformanceProfile.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this PerformanceProfile.
        The URI for this object

        :param self_uri: The self_uri of this PerformanceProfile.
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

