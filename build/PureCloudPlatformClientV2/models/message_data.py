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

class MessageData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'provider_message_id': 'str',
            'timestamp': 'datetime',
            'from_address': 'str',
            'to_address': 'str',
            'direction': 'str',
            'messenger_type': 'str',
            'text_body': 'str',
            'status': 'str',
            'media': 'list[MessageMedia]',
            'stickers': 'list[MessageSticker]',
            'created_by': 'User',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'provider_message_id': 'providerMessageId',
            'timestamp': 'timestamp',
            'from_address': 'fromAddress',
            'to_address': 'toAddress',
            'direction': 'direction',
            'messenger_type': 'messengerType',
            'text_body': 'textBody',
            'status': 'status',
            'media': 'media',
            'stickers': 'stickers',
            'created_by': 'createdBy',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._provider_message_id = None
        self._timestamp = None
        self._from_address = None
        self._to_address = None
        self._direction = None
        self._messenger_type = None
        self._text_body = None
        self._status = None
        self._media = None
        self._stickers = None
        self._created_by = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this MessageData.
        The globally unique identifier for the object.

        :return: The id of this MessageData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessageData.
        The globally unique identifier for the object.

        :param id: The id of this MessageData.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MessageData.


        :return: The name of this MessageData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessageData.


        :param name: The name of this MessageData.
        :type: str
        """
        
        self._name = name

    @property
    def provider_message_id(self):
        """
        Gets the provider_message_id of this MessageData.
        The unique identifier of the message from provider

        :return: The provider_message_id of this MessageData.
        :rtype: str
        """
        return self._provider_message_id

    @provider_message_id.setter
    def provider_message_id(self, provider_message_id):
        """
        Sets the provider_message_id of this MessageData.
        The unique identifier of the message from provider

        :param provider_message_id: The provider_message_id of this MessageData.
        :type: str
        """
        
        self._provider_message_id = provider_message_id

    @property
    def timestamp(self):
        """
        Gets the timestamp of this MessageData.
        The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The timestamp of this MessageData.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this MessageData.
        The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param timestamp: The timestamp of this MessageData.
        :type: datetime
        """
        
        self._timestamp = timestamp

    @property
    def from_address(self):
        """
        Gets the from_address of this MessageData.
        The sender of the text message.

        :return: The from_address of this MessageData.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this MessageData.
        The sender of the text message.

        :param from_address: The from_address of this MessageData.
        :type: str
        """
        
        self._from_address = from_address

    @property
    def to_address(self):
        """
        Gets the to_address of this MessageData.
        The recipient of the text message.

        :return: The to_address of this MessageData.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this MessageData.
        The recipient of the text message.

        :param to_address: The to_address of this MessageData.
        :type: str
        """
        
        self._to_address = to_address

    @property
    def direction(self):
        """
        Gets the direction of this MessageData.
        The direction of the message.

        :return: The direction of this MessageData.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this MessageData.
        The direction of the message.

        :param direction: The direction of this MessageData.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def messenger_type(self):
        """
        Gets the messenger_type of this MessageData.
        Type of text messenger.

        :return: The messenger_type of this MessageData.
        :rtype: str
        """
        return self._messenger_type

    @messenger_type.setter
    def messenger_type(self, messenger_type):
        """
        Sets the messenger_type of this MessageData.
        Type of text messenger.

        :param messenger_type: The messenger_type of this MessageData.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "webmessaging", "open"]
        if messenger_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for messenger_type -> " + messenger_type)
            self._messenger_type = "outdated_sdk_version"
        else:
            self._messenger_type = messenger_type

    @property
    def text_body(self):
        """
        Gets the text_body of this MessageData.
        The body of the text message.

        :return: The text_body of this MessageData.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body):
        """
        Sets the text_body of this MessageData.
        The body of the text message.

        :param text_body: The text_body of this MessageData.
        :type: str
        """
        
        self._text_body = text_body

    @property
    def status(self):
        """
        Gets the status of this MessageData.
        The status of the message.

        :return: The status of this MessageData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MessageData.
        The status of the message.

        :param status: The status of this MessageData.
        :type: str
        """
        allowed_values = ["queued", "sent", "failed", "received", "delivery-success", "delivery-failed", "read"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def media(self):
        """
        Gets the media of this MessageData.
        The media details associated to a message.

        :return: The media of this MessageData.
        :rtype: list[MessageMedia]
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this MessageData.
        The media details associated to a message.

        :param media: The media of this MessageData.
        :type: list[MessageMedia]
        """
        
        self._media = media

    @property
    def stickers(self):
        """
        Gets the stickers of this MessageData.
        The sticker details associated to a message.

        :return: The stickers of this MessageData.
        :rtype: list[MessageSticker]
        """
        return self._stickers

    @stickers.setter
    def stickers(self, stickers):
        """
        Sets the stickers of this MessageData.
        The sticker details associated to a message.

        :param stickers: The stickers of this MessageData.
        :type: list[MessageSticker]
        """
        
        self._stickers = stickers

    @property
    def created_by(self):
        """
        Gets the created_by of this MessageData.
        User who sent this message.

        :return: The created_by of this MessageData.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this MessageData.
        User who sent this message.

        :param created_by: The created_by of this MessageData.
        :type: User
        """
        
        self._created_by = created_by

    @property
    def self_uri(self):
        """
        Gets the self_uri of this MessageData.
        The URI for this object

        :return: The self_uri of this MessageData.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this MessageData.
        The URI for this object

        :param self_uri: The self_uri of this MessageData.
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

