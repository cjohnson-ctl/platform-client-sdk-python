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


class CreateOutboundMessagingConversationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateOutboundMessagingConversationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue_id': 'str',
            'to_address': 'str',
            'to_address_messenger_type': 'str',
            'use_existing_conversation': 'bool',
            'external_contact_id': 'str',
            'external_organization_id': 'str'
        }

        self.attribute_map = {
            'queue_id': 'queueId',
            'to_address': 'toAddress',
            'to_address_messenger_type': 'toAddressMessengerType',
            'use_existing_conversation': 'useExistingConversation',
            'external_contact_id': 'externalContactId',
            'external_organization_id': 'externalOrganizationId'
        }

        self._queue_id = None
        self._to_address = None
        self._to_address_messenger_type = None
        self._use_existing_conversation = None
        self._external_contact_id = None
        self._external_organization_id = None

    @property
    def queue_id(self):
        """
        Gets the queue_id of this CreateOutboundMessagingConversationRequest.
        The ID of the queue to be associated with the message. This will determine the fromAddress of the message.

        :return: The queue_id of this CreateOutboundMessagingConversationRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this CreateOutboundMessagingConversationRequest.
        The ID of the queue to be associated with the message. This will determine the fromAddress of the message.

        :param queue_id: The queue_id of this CreateOutboundMessagingConversationRequest.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def to_address(self):
        """
        Gets the to_address of this CreateOutboundMessagingConversationRequest.
        The messaging address of the recipient of the message.

        :return: The to_address of this CreateOutboundMessagingConversationRequest.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this CreateOutboundMessagingConversationRequest.
        The messaging address of the recipient of the message.

        :param to_address: The to_address of this CreateOutboundMessagingConversationRequest.
        :type: str
        """
        
        self._to_address = to_address

    @property
    def to_address_messenger_type(self):
        """
        Gets the to_address_messenger_type of this CreateOutboundMessagingConversationRequest.
        The messaging address messenger type.

        :return: The to_address_messenger_type of this CreateOutboundMessagingConversationRequest.
        :rtype: str
        """
        return self._to_address_messenger_type

    @to_address_messenger_type.setter
    def to_address_messenger_type(self, to_address_messenger_type):
        """
        Sets the to_address_messenger_type of this CreateOutboundMessagingConversationRequest.
        The messaging address messenger type.

        :param to_address_messenger_type: The to_address_messenger_type of this CreateOutboundMessagingConversationRequest.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "telegram", "kakao"]
        if to_address_messenger_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for to_address_messenger_type -> " + to_address_messenger_type
            self._to_address_messenger_type = "outdated_sdk_version"
        else:
            self._to_address_messenger_type = to_address_messenger_type

    @property
    def use_existing_conversation(self):
        """
        Gets the use_existing_conversation of this CreateOutboundMessagingConversationRequest.
        An override to use an existing conversation.  If set to true, an existing conversation will be used if there is one within the conversation window.  If set to false, create request fails if there is a conversation within the conversation window.

        :return: The use_existing_conversation of this CreateOutboundMessagingConversationRequest.
        :rtype: bool
        """
        return self._use_existing_conversation

    @use_existing_conversation.setter
    def use_existing_conversation(self, use_existing_conversation):
        """
        Sets the use_existing_conversation of this CreateOutboundMessagingConversationRequest.
        An override to use an existing conversation.  If set to true, an existing conversation will be used if there is one within the conversation window.  If set to false, create request fails if there is a conversation within the conversation window.

        :param use_existing_conversation: The use_existing_conversation of this CreateOutboundMessagingConversationRequest.
        :type: bool
        """
        
        self._use_existing_conversation = use_existing_conversation

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this CreateOutboundMessagingConversationRequest.
        The external contact Id of the recipient of the message.

        :return: The external_contact_id of this CreateOutboundMessagingConversationRequest.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this CreateOutboundMessagingConversationRequest.
        The external contact Id of the recipient of the message.

        :param external_contact_id: The external_contact_id of this CreateOutboundMessagingConversationRequest.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def external_organization_id(self):
        """
        Gets the external_organization_id of this CreateOutboundMessagingConversationRequest.
        The external organization Id of the recipient of the message.

        :return: The external_organization_id of this CreateOutboundMessagingConversationRequest.
        :rtype: str
        """
        return self._external_organization_id

    @external_organization_id.setter
    def external_organization_id(self, external_organization_id):
        """
        Sets the external_organization_id of this CreateOutboundMessagingConversationRequest.
        The external organization Id of the recipient of the message.

        :param external_organization_id: The external_organization_id of this CreateOutboundMessagingConversationRequest.
        :type: str
        """
        
        self._external_organization_id = external_organization_id

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

