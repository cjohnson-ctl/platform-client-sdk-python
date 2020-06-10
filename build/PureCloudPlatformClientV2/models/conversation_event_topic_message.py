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

class ConversationEventTopicMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationEventTopicMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'held': 'bool',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'to_address': 'ConversationEventTopicAddress',
            'from_address': 'ConversationEventTopicAddress',
            'messages': 'list[ConversationEventTopicMessageDetails]',
            'messages_transcript_uri': 'str',
            'type': 'str',
            'recipient_country': 'str',
            'recipient_type': 'str',
            'wrapup': 'ConversationEventTopicWrapup',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'held': 'held',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'to_address': 'toAddress',
            'from_address': 'fromAddress',
            'messages': 'messages',
            'messages_transcript_uri': 'messagesTranscriptUri',
            'type': 'type',
            'recipient_country': 'recipientCountry',
            'recipient_type': 'recipientType',
            'wrapup': 'wrapup',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._state = None
        self._held = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._to_address = None
        self._from_address = None
        self._messages = None
        self._messages_transcript_uri = None
        self._type = None
        self._recipient_country = None
        self._recipient_type = None
        self._wrapup = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this ConversationEventTopicMessage.


        :return: The id of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationEventTopicMessage.


        :param id: The id of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this ConversationEventTopicMessage.


        :return: The state of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ConversationEventTopicMessage.


        :param state: The state of this ConversationEventTopicMessage.
        :type: str
        """
        allowed_values = ["ALERTING", "CONNECTED", "DISCONNECTED"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def held(self):
        """
        Gets the held of this ConversationEventTopicMessage.


        :return: The held of this ConversationEventTopicMessage.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this ConversationEventTopicMessage.


        :param held: The held of this ConversationEventTopicMessage.
        :type: bool
        """
        
        self._held = held

    @property
    def provider(self):
        """
        Gets the provider of this ConversationEventTopicMessage.


        :return: The provider of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this ConversationEventTopicMessage.


        :param provider: The provider of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this ConversationEventTopicMessage.


        :return: The script_id of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this ConversationEventTopicMessage.


        :param script_id: The script_id of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this ConversationEventTopicMessage.


        :return: The peer_id of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this ConversationEventTopicMessage.


        :param peer_id: The peer_id of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this ConversationEventTopicMessage.


        :return: The disconnect_type of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this ConversationEventTopicMessage.


        :param disconnect_type: The disconnect_type of this ConversationEventTopicMessage.
        :type: str
        """
        allowed_values = ["ENDPOINT", "CLIENT", "SYSTEM", "TIMEOUT", "TRANSFER", "TRANSFER_CONFERENCE", "TRANSFER_CONSULT", "TRANSFER_FORWARD", "TRANSFER_NOANSWER", "TRANSFER_NOTAVAILABLE", "TRANSPORT_FAILURE", "ERROR", "PEER", "OTHER", "SPAM", "UNCALLABLE"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this ConversationEventTopicMessage.


        :return: The start_hold_time of this ConversationEventTopicMessage.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this ConversationEventTopicMessage.


        :param start_hold_time: The start_hold_time of this ConversationEventTopicMessage.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this ConversationEventTopicMessage.


        :return: The connected_time of this ConversationEventTopicMessage.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this ConversationEventTopicMessage.


        :param connected_time: The connected_time of this ConversationEventTopicMessage.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this ConversationEventTopicMessage.


        :return: The disconnected_time of this ConversationEventTopicMessage.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this ConversationEventTopicMessage.


        :param disconnected_time: The disconnected_time of this ConversationEventTopicMessage.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def to_address(self):
        """
        Gets the to_address of this ConversationEventTopicMessage.


        :return: The to_address of this ConversationEventTopicMessage.
        :rtype: ConversationEventTopicAddress
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this ConversationEventTopicMessage.


        :param to_address: The to_address of this ConversationEventTopicMessage.
        :type: ConversationEventTopicAddress
        """
        
        self._to_address = to_address

    @property
    def from_address(self):
        """
        Gets the from_address of this ConversationEventTopicMessage.


        :return: The from_address of this ConversationEventTopicMessage.
        :rtype: ConversationEventTopicAddress
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this ConversationEventTopicMessage.


        :param from_address: The from_address of this ConversationEventTopicMessage.
        :type: ConversationEventTopicAddress
        """
        
        self._from_address = from_address

    @property
    def messages(self):
        """
        Gets the messages of this ConversationEventTopicMessage.


        :return: The messages of this ConversationEventTopicMessage.
        :rtype: list[ConversationEventTopicMessageDetails]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this ConversationEventTopicMessage.


        :param messages: The messages of this ConversationEventTopicMessage.
        :type: list[ConversationEventTopicMessageDetails]
        """
        
        self._messages = messages

    @property
    def messages_transcript_uri(self):
        """
        Gets the messages_transcript_uri of this ConversationEventTopicMessage.


        :return: The messages_transcript_uri of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._messages_transcript_uri

    @messages_transcript_uri.setter
    def messages_transcript_uri(self, messages_transcript_uri):
        """
        Sets the messages_transcript_uri of this ConversationEventTopicMessage.


        :param messages_transcript_uri: The messages_transcript_uri of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._messages_transcript_uri = messages_transcript_uri

    @property
    def type(self):
        """
        Gets the type of this ConversationEventTopicMessage.


        :return: The type of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConversationEventTopicMessage.


        :param type: The type of this ConversationEventTopicMessage.
        :type: str
        """
        allowed_values = ["SMS", "TWITTER", "FACEBOOK", "LINE", "VIBER", "WECHAT", "WHATSAPP", "TELEGRAM", "KAKAO"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def recipient_country(self):
        """
        Gets the recipient_country of this ConversationEventTopicMessage.


        :return: The recipient_country of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._recipient_country

    @recipient_country.setter
    def recipient_country(self, recipient_country):
        """
        Sets the recipient_country of this ConversationEventTopicMessage.


        :param recipient_country: The recipient_country of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._recipient_country = recipient_country

    @property
    def recipient_type(self):
        """
        Gets the recipient_type of this ConversationEventTopicMessage.


        :return: The recipient_type of this ConversationEventTopicMessage.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """
        Sets the recipient_type of this ConversationEventTopicMessage.


        :param recipient_type: The recipient_type of this ConversationEventTopicMessage.
        :type: str
        """
        
        self._recipient_type = recipient_type

    @property
    def wrapup(self):
        """
        Gets the wrapup of this ConversationEventTopicMessage.


        :return: The wrapup of this ConversationEventTopicMessage.
        :rtype: ConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this ConversationEventTopicMessage.


        :param wrapup: The wrapup of this ConversationEventTopicMessage.
        :type: ConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ConversationEventTopicMessage.


        :return: The additional_properties of this ConversationEventTopicMessage.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ConversationEventTopicMessage.


        :param additional_properties: The additional_properties of this ConversationEventTopicMessage.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

