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

class RecordingJobsQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RecordingJobsQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'action_date': 'datetime',
            'conversation_query': 'AsyncConversationQuery'
        }

        self.attribute_map = {
            'action': 'action',
            'action_date': 'actionDate',
            'conversation_query': 'conversationQuery'
        }

        self._action = None
        self._action_date = None
        self._conversation_query = None

    @property
    def action(self):
        """
        Gets the action of this RecordingJobsQuery.
        Operation to perform bulk task

        :return: The action of this RecordingJobsQuery.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this RecordingJobsQuery.
        Operation to perform bulk task

        :param action: The action of this RecordingJobsQuery.
        :type: str
        """
        allowed_values = ["DELETE"]
        if action.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for action -> " + action
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def action_date(self):
        """
        Gets the action_date of this RecordingJobsQuery.
        The date when the action will be performed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The action_date of this RecordingJobsQuery.
        :rtype: datetime
        """
        return self._action_date

    @action_date.setter
    def action_date(self, action_date):
        """
        Sets the action_date of this RecordingJobsQuery.
        The date when the action will be performed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param action_date: The action_date of this RecordingJobsQuery.
        :type: datetime
        """
        
        self._action_date = action_date

    @property
    def conversation_query(self):
        """
        Gets the conversation_query of this RecordingJobsQuery.
        Conversation Query. Note: After the recording is created, it might take up to 48 hours for the recording to be included in the submitted job query.

        :return: The conversation_query of this RecordingJobsQuery.
        :rtype: AsyncConversationQuery
        """
        return self._conversation_query

    @conversation_query.setter
    def conversation_query(self, conversation_query):
        """
        Sets the conversation_query of this RecordingJobsQuery.
        Conversation Query. Note: After the recording is created, it might take up to 48 hours for the recording to be included in the submitted job query.

        :param conversation_query: The conversation_query of this RecordingJobsQuery.
        :type: AsyncConversationQuery
        """
        
        self._conversation_query = conversation_query

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

