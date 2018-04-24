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


class Message(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Message - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'held': 'bool',
            'segments': 'list[Segment]',
            'direction': 'str',
            'recording_id': 'str',
            'error_info': 'ErrorBody',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'provider': 'str',
            'type': 'str',
            'recipient_country': 'str',
            'recipient_type': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'to_address': 'Address',
            'from_address': 'Address',
            'messages': 'list[MessageDetails]'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'held': 'held',
            'segments': 'segments',
            'direction': 'direction',
            'recording_id': 'recordingId',
            'error_info': 'errorInfo',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'provider': 'provider',
            'type': 'type',
            'recipient_country': 'recipientCountry',
            'recipient_type': 'recipientType',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'to_address': 'toAddress',
            'from_address': 'fromAddress',
            'messages': 'messages'
        }

        self._state = None
        self._id = None
        self._held = None
        self._segments = None
        self._direction = None
        self._recording_id = None
        self._error_info = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._provider = None
        self._type = None
        self._recipient_country = None
        self._recipient_type = None
        self._script_id = None
        self._peer_id = None
        self._to_address = None
        self._from_address = None
        self._messages = None

    @property
    def state(self):
        """
        Gets the state of this Message.
        The connection state of this communication.

        :return: The state of this Message.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Message.
        The connection state of this communication.

        :param state: The state of this Message.
        :type: str
        """
        allowed_values = ["alerting", "connected", "disconnected"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def id(self):
        """
        Gets the id of this Message.
        A globally unique identifier for this communication.

        :return: The id of this Message.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Message.
        A globally unique identifier for this communication.

        :param id: The id of this Message.
        :type: str
        """
        
        self._id = id

    @property
    def held(self):
        """
        Gets the held of this Message.
        True if this call is held and the person on this side hears silence.

        :return: The held of this Message.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this Message.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this Message.
        :type: bool
        """
        
        self._held = held

    @property
    def segments(self):
        """
        Gets the segments of this Message.
        The time line of the participant's message, divided into activity segments.

        :return: The segments of this Message.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this Message.
        The time line of the participant's message, divided into activity segments.

        :param segments: The segments of this Message.
        :type: list[Segment]
        """
        
        self._segments = segments

    @property
    def direction(self):
        """
        Gets the direction of this Message.
        The direction of the message.

        :return: The direction of this Message.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Message.
        The direction of the message.

        :param direction: The direction of this Message.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def recording_id(self):
        """
        Gets the recording_id of this Message.
        A globally unique identifier for the recording associated with this message.

        :return: The recording_id of this Message.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id):
        """
        Sets the recording_id of this Message.
        A globally unique identifier for the recording associated with this message.

        :param recording_id: The recording_id of this Message.
        :type: str
        """
        
        self._recording_id = recording_id

    @property
    def error_info(self):
        """
        Gets the error_info of this Message.


        :return: The error_info of this Message.
        :rtype: ErrorBody
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this Message.


        :param error_info: The error_info of this Message.
        :type: ErrorBody
        """
        
        self._error_info = error_info

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this Message.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this Message.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this Message.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this Message.
        :type: str
        """
        allowed_values = ["endpoint", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this Message.
        The timestamp the message was placed on hold in the cloud clock if the message is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_hold_time of this Message.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this Message.
        The timestamp the message was placed on hold in the cloud clock if the message is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_hold_time: The start_hold_time of this Message.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this Message.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The connected_time of this Message.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this Message.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param connected_time: The connected_time of this Message.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this Message.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The disconnected_time of this Message.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this Message.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param disconnected_time: The disconnected_time of this Message.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def provider(self):
        """
        Gets the provider of this Message.
        The source provider for the message.

        :return: The provider of this Message.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this Message.
        The source provider for the message.

        :param provider: The provider of this Message.
        :type: str
        """
        
        self._provider = provider

    @property
    def type(self):
        """
        Gets the type of this Message.
        Indicates the type of message platform from which the message originated.

        :return: The type of this Message.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Message.
        Indicates the type of message platform from which the message originated.

        :param type: The type of this Message.
        :type: str
        """
        allowed_values = ["sms", "twitter", "facebook", "line"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def recipient_country(self):
        """
        Gets the recipient_country of this Message.
        Indicates the country where the recipient is associated in ISO 3166-1 alpha-2 format.

        :return: The recipient_country of this Message.
        :rtype: str
        """
        return self._recipient_country

    @recipient_country.setter
    def recipient_country(self, recipient_country):
        """
        Sets the recipient_country of this Message.
        Indicates the country where the recipient is associated in ISO 3166-1 alpha-2 format.

        :param recipient_country: The recipient_country of this Message.
        :type: str
        """
        
        self._recipient_country = recipient_country

    @property
    def recipient_type(self):
        """
        Gets the recipient_type of this Message.
        The type of the recipient. Eg: Provisioned phoneNumber is the recipient for sms message type.

        :return: The recipient_type of this Message.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """
        Sets the recipient_type of this Message.
        The type of the recipient. Eg: Provisioned phoneNumber is the recipient for sms message type.

        :param recipient_type: The recipient_type of this Message.
        :type: str
        """
        
        self._recipient_type = recipient_type

    @property
    def script_id(self):
        """
        Gets the script_id of this Message.
        The UUID of the script to use.

        :return: The script_id of this Message.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this Message.
        The UUID of the script to use.

        :param script_id: The script_id of this Message.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this Message.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this Message.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this Message.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this Message.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def to_address(self):
        """
        Gets the to_address of this Message.
        Address and name data for a call endpoint.

        :return: The to_address of this Message.
        :rtype: Address
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this Message.
        Address and name data for a call endpoint.

        :param to_address: The to_address of this Message.
        :type: Address
        """
        
        self._to_address = to_address

    @property
    def from_address(self):
        """
        Gets the from_address of this Message.
        Address and name data for a call endpoint.

        :return: The from_address of this Message.
        :rtype: Address
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this Message.
        Address and name data for a call endpoint.

        :param from_address: The from_address of this Message.
        :type: Address
        """
        
        self._from_address = from_address

    @property
    def messages(self):
        """
        Gets the messages of this Message.
        The messages sent on this communication channel.

        :return: The messages of this Message.
        :rtype: list[MessageDetails]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this Message.
        The messages sent on this communication channel.

        :param messages: The messages of this Message.
        :type: list[MessageDetails]
        """
        
        self._messages = messages

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

