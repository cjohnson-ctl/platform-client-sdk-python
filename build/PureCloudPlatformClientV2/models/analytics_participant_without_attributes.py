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

class AnalyticsParticipantWithoutAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsParticipantWithoutAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'participant_id': 'str',
            'participant_name': 'str',
            'user_id': 'str',
            'purpose': 'str',
            'external_contact_id': 'str',
            'external_organization_id': 'str',
            'flagged_reason': 'str',
            'team_id': 'str',
            'agent_assistant_ids': 'list[str]',
            'sessions': 'list[AnalyticsSession]'
        }

        self.attribute_map = {
            'participant_id': 'participantId',
            'participant_name': 'participantName',
            'user_id': 'userId',
            'purpose': 'purpose',
            'external_contact_id': 'externalContactId',
            'external_organization_id': 'externalOrganizationId',
            'flagged_reason': 'flaggedReason',
            'team_id': 'teamId',
            'agent_assistant_ids': 'agentAssistantIds',
            'sessions': 'sessions'
        }

        self._participant_id = None
        self._participant_name = None
        self._user_id = None
        self._purpose = None
        self._external_contact_id = None
        self._external_organization_id = None
        self._flagged_reason = None
        self._team_id = None
        self._agent_assistant_ids = None
        self._sessions = None

    @property
    def participant_id(self):
        """
        Gets the participant_id of this AnalyticsParticipantWithoutAttributes.
        Unique identifier for the participant

        :return: The participant_id of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """
        Sets the participant_id of this AnalyticsParticipantWithoutAttributes.
        Unique identifier for the participant

        :param participant_id: The participant_id of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._participant_id = participant_id

    @property
    def participant_name(self):
        """
        Gets the participant_name of this AnalyticsParticipantWithoutAttributes.
        A human readable name identifying the participant

        :return: The participant_name of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name):
        """
        Sets the participant_name of this AnalyticsParticipantWithoutAttributes.
        A human readable name identifying the participant

        :param participant_name: The participant_name of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._participant_name = participant_name

    @property
    def user_id(self):
        """
        Gets the user_id of this AnalyticsParticipantWithoutAttributes.
        If a user, then this will be the unique identifier for the user

        :return: The user_id of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AnalyticsParticipantWithoutAttributes.
        If a user, then this will be the unique identifier for the user

        :param user_id: The user_id of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def purpose(self):
        """
        Gets the purpose of this AnalyticsParticipantWithoutAttributes.
        The participant's purpose

        :return: The purpose of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this AnalyticsParticipantWithoutAttributes.
        The participant's purpose

        :param purpose: The purpose of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        allowed_values = ["manual", "dialer", "inbound", "acd", "ivr", "voicemail", "outbound", "agent", "user", "station", "group", "customer", "external", "fax", "workflow", "campaign", "api"]
        if purpose.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for purpose -> " + purpose
            self._purpose = "outdated_sdk_version"
        else:
            self._purpose = purpose

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this AnalyticsParticipantWithoutAttributes.
        External Contact Identifier

        :return: The external_contact_id of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this AnalyticsParticipantWithoutAttributes.
        External Contact Identifier

        :param external_contact_id: The external_contact_id of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def external_organization_id(self):
        """
        Gets the external_organization_id of this AnalyticsParticipantWithoutAttributes.
        External Organization Identifier

        :return: The external_organization_id of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._external_organization_id

    @external_organization_id.setter
    def external_organization_id(self, external_organization_id):
        """
        Sets the external_organization_id of this AnalyticsParticipantWithoutAttributes.
        External Organization Identifier

        :param external_organization_id: The external_organization_id of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._external_organization_id = external_organization_id

    @property
    def flagged_reason(self):
        """
        Gets the flagged_reason of this AnalyticsParticipantWithoutAttributes.
        Reason for which participant flagged conversation

        :return: The flagged_reason of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason):
        """
        Sets the flagged_reason of this AnalyticsParticipantWithoutAttributes.
        Reason for which participant flagged conversation

        :param flagged_reason: The flagged_reason of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        allowed_values = ["general"]
        if flagged_reason.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for flagged_reason -> " + flagged_reason
            self._flagged_reason = "outdated_sdk_version"
        else:
            self._flagged_reason = flagged_reason

    @property
    def team_id(self):
        """
        Gets the team_id of this AnalyticsParticipantWithoutAttributes.
        The team id the user is a member of

        :return: The team_id of this AnalyticsParticipantWithoutAttributes.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this AnalyticsParticipantWithoutAttributes.
        The team id the user is a member of

        :param team_id: The team_id of this AnalyticsParticipantWithoutAttributes.
        :type: str
        """
        
        self._team_id = team_id

    @property
    def agent_assistant_ids(self):
        """
        Gets the agent_assistant_ids of this AnalyticsParticipantWithoutAttributes.
        Unique identifiers of the active virtual agent assistants

        :return: The agent_assistant_ids of this AnalyticsParticipantWithoutAttributes.
        :rtype: list[str]
        """
        return self._agent_assistant_ids

    @agent_assistant_ids.setter
    def agent_assistant_ids(self, agent_assistant_ids):
        """
        Sets the agent_assistant_ids of this AnalyticsParticipantWithoutAttributes.
        Unique identifiers of the active virtual agent assistants

        :param agent_assistant_ids: The agent_assistant_ids of this AnalyticsParticipantWithoutAttributes.
        :type: list[str]
        """
        
        self._agent_assistant_ids = agent_assistant_ids

    @property
    def sessions(self):
        """
        Gets the sessions of this AnalyticsParticipantWithoutAttributes.
        List of sessions associated to this participant

        :return: The sessions of this AnalyticsParticipantWithoutAttributes.
        :rtype: list[AnalyticsSession]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """
        Sets the sessions of this AnalyticsParticipantWithoutAttributes.
        List of sessions associated to this participant

        :param sessions: The sessions of this AnalyticsParticipantWithoutAttributes.
        :type: list[AnalyticsSession]
        """
        
        self._sessions = sessions

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

