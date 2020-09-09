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

class SendAgentlessOutboundMessageResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SendAgentlessOutboundMessageResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'conversation_id': 'str',
            'from_address': 'str',
            'to_address': 'str',
            'messenger_type': 'str',
            'text_body': 'str',
            'timestamp': 'datetime',
            'self_uri': 'str',
            'user': 'AddressableEntityRef'
        }

        self.attribute_map = {
            'id': 'id',
            'conversation_id': 'conversationId',
            'from_address': 'fromAddress',
            'to_address': 'toAddress',
            'messenger_type': 'messengerType',
            'text_body': 'textBody',
            'timestamp': 'timestamp',
            'self_uri': 'selfUri',
            'user': 'user'
        }

        self._id = None
        self._conversation_id = None
        self._from_address = None
        self._to_address = None
        self._messenger_type = None
        self._text_body = None
        self._timestamp = None
        self._self_uri = None
        self._user = None

    @property
    def id(self):
        """
        Gets the id of this SendAgentlessOutboundMessageResponse.
        The globally unique identifier for the object.

        :return: The id of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SendAgentlessOutboundMessageResponse.
        The globally unique identifier for the object.

        :param id: The id of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._id = id

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this SendAgentlessOutboundMessageResponse.
        The identifier of the conversation.

        :return: The conversation_id of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this SendAgentlessOutboundMessageResponse.
        The identifier of the conversation.

        :param conversation_id: The conversation_id of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def from_address(self):
        """
        Gets the from_address of this SendAgentlessOutboundMessageResponse.
        The sender of the text message.

        :return: The from_address of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this SendAgentlessOutboundMessageResponse.
        The sender of the text message.

        :param from_address: The from_address of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._from_address = from_address

    @property
    def to_address(self):
        """
        Gets the to_address of this SendAgentlessOutboundMessageResponse.
        The recipient of the text message.

        :return: The to_address of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this SendAgentlessOutboundMessageResponse.
        The recipient of the text message.

        :param to_address: The to_address of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._to_address = to_address

    @property
    def messenger_type(self):
        """
        Gets the messenger_type of this SendAgentlessOutboundMessageResponse.
        Type of text messenger.

        :return: The messenger_type of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._messenger_type

    @messenger_type.setter
    def messenger_type(self, messenger_type):
        """
        Sets the messenger_type of this SendAgentlessOutboundMessageResponse.
        Type of text messenger.

        :param messenger_type: The messenger_type of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "webmessaging"]
        if messenger_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for messenger_type -> " + messenger_type
            self._messenger_type = "outdated_sdk_version"
        else:
            self._messenger_type = messenger_type

    @property
    def text_body(self):
        """
        Gets the text_body of this SendAgentlessOutboundMessageResponse.
        The body of the text message.

        :return: The text_body of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body):
        """
        Sets the text_body of this SendAgentlessOutboundMessageResponse.
        The body of the text message.

        :param text_body: The text_body of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._text_body = text_body

    @property
    def timestamp(self):
        """
        Gets the timestamp of this SendAgentlessOutboundMessageResponse.
        The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The timestamp of this SendAgentlessOutboundMessageResponse.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this SendAgentlessOutboundMessageResponse.
        The time when the message was sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param timestamp: The timestamp of this SendAgentlessOutboundMessageResponse.
        :type: datetime
        """
        
        self._timestamp = timestamp

    @property
    def self_uri(self):
        """
        Gets the self_uri of this SendAgentlessOutboundMessageResponse.
        The URI for this object

        :return: The self_uri of this SendAgentlessOutboundMessageResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this SendAgentlessOutboundMessageResponse.
        The URI for this object

        :param self_uri: The self_uri of this SendAgentlessOutboundMessageResponse.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def user(self):
        """
        Gets the user of this SendAgentlessOutboundMessageResponse.
        Details of the user created the job

        :return: The user of this SendAgentlessOutboundMessageResponse.
        :rtype: AddressableEntityRef
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this SendAgentlessOutboundMessageResponse.
        Details of the user created the job

        :param user: The user of this SendAgentlessOutboundMessageResponse.
        :type: AddressableEntityRef
        """
        
        self._user = user

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

