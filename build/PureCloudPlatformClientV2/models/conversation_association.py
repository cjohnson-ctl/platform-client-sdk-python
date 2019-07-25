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

class ConversationAssociation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationAssociation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'external_contact_id': 'str',
            'conversation_id': 'str',
            'communication_id': 'str',
            'media_type': 'str'
        }

        self.attribute_map = {
            'external_contact_id': 'externalContactId',
            'conversation_id': 'conversationId',
            'communication_id': 'communicationId',
            'media_type': 'mediaType'
        }

        self._external_contact_id = None
        self._conversation_id = None
        self._communication_id = None
        self._media_type = None

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this ConversationAssociation.
        External Contact ID

        :return: The external_contact_id of this ConversationAssociation.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this ConversationAssociation.
        External Contact ID

        :param external_contact_id: The external_contact_id of this ConversationAssociation.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this ConversationAssociation.
        Conversation ID

        :return: The conversation_id of this ConversationAssociation.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this ConversationAssociation.
        Conversation ID

        :param conversation_id: The conversation_id of this ConversationAssociation.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def communication_id(self):
        """
        Gets the communication_id of this ConversationAssociation.
        Communication ID

        :return: The communication_id of this ConversationAssociation.
        :rtype: str
        """
        return self._communication_id

    @communication_id.setter
    def communication_id(self, communication_id):
        """
        Sets the communication_id of this ConversationAssociation.
        Communication ID

        :param communication_id: The communication_id of this ConversationAssociation.
        :type: str
        """
        
        self._communication_id = communication_id

    @property
    def media_type(self):
        """
        Gets the media_type of this ConversationAssociation.
        Media type

        :return: The media_type of this ConversationAssociation.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this ConversationAssociation.
        Media type

        :param media_type: The media_type of this ConversationAssociation.
        :type: str
        """
        allowed_values = ["CALL", "CALLBACK", "CHAT", "COBROWSE", "EMAIL", "MESSAGE", "SOCIAL_EXPRESSION", "VIDEO", "SCREENSHARE"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for media_type -> " + media_type
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

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

