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

class AuditQueryExecutionStatusResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuditQueryExecutionStatusResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'start_date': 'datetime',
            'interval': 'str',
            'service_name': 'str',
            'filters': 'list[AuditQueryFilter]',
            'sort': 'list[AuditQuerySort]'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'start_date': 'startDate',
            'interval': 'interval',
            'service_name': 'serviceName',
            'filters': 'filters',
            'sort': 'sort'
        }

        self._id = None
        self._state = None
        self._start_date = None
        self._interval = None
        self._service_name = None
        self._filters = None
        self._sort = None

    @property
    def id(self):
        """
        Gets the id of this AuditQueryExecutionStatusResponse.
        Id of the audit query execution request.

        :return: The id of this AuditQueryExecutionStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditQueryExecutionStatusResponse.
        Id of the audit query execution request.

        :param id: The id of this AuditQueryExecutionStatusResponse.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this AuditQueryExecutionStatusResponse.
        Status of the audit query execution request.

        :return: The state of this AuditQueryExecutionStatusResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AuditQueryExecutionStatusResponse.
        Status of the audit query execution request.

        :param state: The state of this AuditQueryExecutionStatusResponse.
        :type: str
        """
        allowed_values = ["Queued", "Running", "Succeeded", "Failed", "Cancelled"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def start_date(self):
        """
        Gets the start_date of this AuditQueryExecutionStatusResponse.
        Start date and time of the audit query execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_date of this AuditQueryExecutionStatusResponse.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this AuditQueryExecutionStatusResponse.
        Start date and time of the audit query execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_date: The start_date of this AuditQueryExecutionStatusResponse.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def interval(self):
        """
        Gets the interval of this AuditQueryExecutionStatusResponse.
        Interval for the audit query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this AuditQueryExecutionStatusResponse.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this AuditQueryExecutionStatusResponse.
        Interval for the audit query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this AuditQueryExecutionStatusResponse.
        :type: str
        """
        
        self._interval = interval

    @property
    def service_name(self):
        """
        Gets the service_name of this AuditQueryExecutionStatusResponse.
        Service name for the audit query.

        :return: The service_name of this AuditQueryExecutionStatusResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this AuditQueryExecutionStatusResponse.
        Service name for the audit query.

        :param service_name: The service_name of this AuditQueryExecutionStatusResponse.
        :type: str
        """
        allowed_values = ["AnalyticsReporting", "Architect", "Coaching", "ContactCenter", "ContentManagement", "Datatables", "Gamification", "Groups", "Integrations", "LanguageUnderstanding", "Limits", "Outbound", "PeoplePermissions", "Performance", "PredictiveEngagement", "Presence", "Quality", "ResponseManagement", "Routing", "SpeechAndTextAnalytics", "Telephony", "TopicsDefinitions", "Triggers", "WebDeployments", "Webhooks", "WorkforceManagement", "Messaging"]
        if service_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for service_name -> " + service_name)
            self._service_name = "outdated_sdk_version"
        else:
            self._service_name = service_name

    @property
    def filters(self):
        """
        Gets the filters of this AuditQueryExecutionStatusResponse.
        Filters for the audit query.

        :return: The filters of this AuditQueryExecutionStatusResponse.
        :rtype: list[AuditQueryFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this AuditQueryExecutionStatusResponse.
        Filters for the audit query.

        :param filters: The filters of this AuditQueryExecutionStatusResponse.
        :type: list[AuditQueryFilter]
        """
        
        self._filters = filters

    @property
    def sort(self):
        """
        Gets the sort of this AuditQueryExecutionStatusResponse.
        Sort parameter for the audit query.

        :return: The sort of this AuditQueryExecutionStatusResponse.
        :rtype: list[AuditQuerySort]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this AuditQueryExecutionStatusResponse.
        Sort parameter for the audit query.

        :param sort: The sort of this AuditQueryExecutionStatusResponse.
        :type: list[AuditQuerySort]
        """
        
        self._sort = sort

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

