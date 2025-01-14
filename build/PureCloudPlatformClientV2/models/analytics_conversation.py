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

class AnalyticsConversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsConversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'conversation_end': 'datetime',
            'conversation_id': 'str',
            'conversation_start': 'datetime',
            'division_ids': 'list[str]',
            'external_tag': 'str',
            'media_stats_min_conversation_mos': 'float',
            'media_stats_min_conversation_r_factor': 'float',
            'originating_direction': 'str',
            'evaluations': 'list[AnalyticsEvaluation]',
            'surveys': 'list[AnalyticsSurvey]',
            'resolutions': 'list[AnalyticsResolution]',
            'participants': 'list[AnalyticsParticipant]'
        }

        self.attribute_map = {
            'conversation_end': 'conversationEnd',
            'conversation_id': 'conversationId',
            'conversation_start': 'conversationStart',
            'division_ids': 'divisionIds',
            'external_tag': 'externalTag',
            'media_stats_min_conversation_mos': 'mediaStatsMinConversationMos',
            'media_stats_min_conversation_r_factor': 'mediaStatsMinConversationRFactor',
            'originating_direction': 'originatingDirection',
            'evaluations': 'evaluations',
            'surveys': 'surveys',
            'resolutions': 'resolutions',
            'participants': 'participants'
        }

        self._conversation_end = None
        self._conversation_id = None
        self._conversation_start = None
        self._division_ids = None
        self._external_tag = None
        self._media_stats_min_conversation_mos = None
        self._media_stats_min_conversation_r_factor = None
        self._originating_direction = None
        self._evaluations = None
        self._surveys = None
        self._resolutions = None
        self._participants = None

    @property
    def conversation_end(self):
        """
        Gets the conversation_end of this AnalyticsConversation.
        The end time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The conversation_end of this AnalyticsConversation.
        :rtype: datetime
        """
        return self._conversation_end

    @conversation_end.setter
    def conversation_end(self, conversation_end):
        """
        Sets the conversation_end of this AnalyticsConversation.
        The end time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param conversation_end: The conversation_end of this AnalyticsConversation.
        :type: datetime
        """
        
        self._conversation_end = conversation_end

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this AnalyticsConversation.
        Unique identifier for the conversation

        :return: The conversation_id of this AnalyticsConversation.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this AnalyticsConversation.
        Unique identifier for the conversation

        :param conversation_id: The conversation_id of this AnalyticsConversation.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def conversation_start(self):
        """
        Gets the conversation_start of this AnalyticsConversation.
        The start time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The conversation_start of this AnalyticsConversation.
        :rtype: datetime
        """
        return self._conversation_start

    @conversation_start.setter
    def conversation_start(self, conversation_start):
        """
        Sets the conversation_start of this AnalyticsConversation.
        The start time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param conversation_start: The conversation_start of this AnalyticsConversation.
        :type: datetime
        """
        
        self._conversation_start = conversation_start

    @property
    def division_ids(self):
        """
        Gets the division_ids of this AnalyticsConversation.
        Identifier(s) of division(s) associated with a conversation

        :return: The division_ids of this AnalyticsConversation.
        :rtype: list[str]
        """
        return self._division_ids

    @division_ids.setter
    def division_ids(self, division_ids):
        """
        Sets the division_ids of this AnalyticsConversation.
        Identifier(s) of division(s) associated with a conversation

        :param division_ids: The division_ids of this AnalyticsConversation.
        :type: list[str]
        """
        
        self._division_ids = division_ids

    @property
    def external_tag(self):
        """
        Gets the external_tag of this AnalyticsConversation.
        External tag for the conversation

        :return: The external_tag of this AnalyticsConversation.
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag):
        """
        Sets the external_tag of this AnalyticsConversation.
        External tag for the conversation

        :param external_tag: The external_tag of this AnalyticsConversation.
        :type: str
        """
        
        self._external_tag = external_tag

    @property
    def media_stats_min_conversation_mos(self):
        """
        Gets the media_stats_min_conversation_mos of this AnalyticsConversation.
        The lowest estimated average MOS among all the audio streams belonging to this conversation

        :return: The media_stats_min_conversation_mos of this AnalyticsConversation.
        :rtype: float
        """
        return self._media_stats_min_conversation_mos

    @media_stats_min_conversation_mos.setter
    def media_stats_min_conversation_mos(self, media_stats_min_conversation_mos):
        """
        Sets the media_stats_min_conversation_mos of this AnalyticsConversation.
        The lowest estimated average MOS among all the audio streams belonging to this conversation

        :param media_stats_min_conversation_mos: The media_stats_min_conversation_mos of this AnalyticsConversation.
        :type: float
        """
        
        self._media_stats_min_conversation_mos = media_stats_min_conversation_mos

    @property
    def media_stats_min_conversation_r_factor(self):
        """
        Gets the media_stats_min_conversation_r_factor of this AnalyticsConversation.
        The lowest R-factor value among all of the audio streams belonging to this conversation

        :return: The media_stats_min_conversation_r_factor of this AnalyticsConversation.
        :rtype: float
        """
        return self._media_stats_min_conversation_r_factor

    @media_stats_min_conversation_r_factor.setter
    def media_stats_min_conversation_r_factor(self, media_stats_min_conversation_r_factor):
        """
        Sets the media_stats_min_conversation_r_factor of this AnalyticsConversation.
        The lowest R-factor value among all of the audio streams belonging to this conversation

        :param media_stats_min_conversation_r_factor: The media_stats_min_conversation_r_factor of this AnalyticsConversation.
        :type: float
        """
        
        self._media_stats_min_conversation_r_factor = media_stats_min_conversation_r_factor

    @property
    def originating_direction(self):
        """
        Gets the originating_direction of this AnalyticsConversation.
        The original direction of the conversation

        :return: The originating_direction of this AnalyticsConversation.
        :rtype: str
        """
        return self._originating_direction

    @originating_direction.setter
    def originating_direction(self, originating_direction):
        """
        Sets the originating_direction of this AnalyticsConversation.
        The original direction of the conversation

        :param originating_direction: The originating_direction of this AnalyticsConversation.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if originating_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for originating_direction -> " + originating_direction)
            self._originating_direction = "outdated_sdk_version"
        else:
            self._originating_direction = originating_direction

    @property
    def evaluations(self):
        """
        Gets the evaluations of this AnalyticsConversation.
        Evaluations associated with this conversation

        :return: The evaluations of this AnalyticsConversation.
        :rtype: list[AnalyticsEvaluation]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        """
        Sets the evaluations of this AnalyticsConversation.
        Evaluations associated with this conversation

        :param evaluations: The evaluations of this AnalyticsConversation.
        :type: list[AnalyticsEvaluation]
        """
        
        self._evaluations = evaluations

    @property
    def surveys(self):
        """
        Gets the surveys of this AnalyticsConversation.
        Surveys associated with this conversation

        :return: The surveys of this AnalyticsConversation.
        :rtype: list[AnalyticsSurvey]
        """
        return self._surveys

    @surveys.setter
    def surveys(self, surveys):
        """
        Sets the surveys of this AnalyticsConversation.
        Surveys associated with this conversation

        :param surveys: The surveys of this AnalyticsConversation.
        :type: list[AnalyticsSurvey]
        """
        
        self._surveys = surveys

    @property
    def resolutions(self):
        """
        Gets the resolutions of this AnalyticsConversation.
        Resolutions associated with this conversation

        :return: The resolutions of this AnalyticsConversation.
        :rtype: list[AnalyticsResolution]
        """
        return self._resolutions

    @resolutions.setter
    def resolutions(self, resolutions):
        """
        Sets the resolutions of this AnalyticsConversation.
        Resolutions associated with this conversation

        :param resolutions: The resolutions of this AnalyticsConversation.
        :type: list[AnalyticsResolution]
        """
        
        self._resolutions = resolutions

    @property
    def participants(self):
        """
        Gets the participants of this AnalyticsConversation.
        Participants in the conversation

        :return: The participants of this AnalyticsConversation.
        :rtype: list[AnalyticsParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """
        Sets the participants of this AnalyticsConversation.
        Participants in the conversation

        :param participants: The participants of this AnalyticsConversation.
        :type: list[AnalyticsParticipant]
        """
        
        self._participants = participants

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

