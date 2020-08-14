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

class QueueConversationEventTopicChat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationEventTopicChat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'room_id': 'str',
            'avatar_image_url': 'str',
            'held': 'bool',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'journey_context': 'QueueConversationEventTopicJourneyContext',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'after_call_work': 'QueueConversationEventTopicAfterCallWork',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'room_id': 'roomId',
            'avatar_image_url': 'avatarImageUrl',
            'held': 'held',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'journey_context': 'journeyContext',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'additional_properties': 'additionalProperties'
        }

        self._state = None
        self._id = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._room_id = None
        self._avatar_image_url = None
        self._held = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._journey_context = None
        self._wrapup = None
        self._after_call_work = None
        self._additional_properties = None

    @property
    def state(self):
        """
        Gets the state of this QueueConversationEventTopicChat.


        :return: The state of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this QueueConversationEventTopicChat.


        :param state: The state of this QueueConversationEventTopicChat.
        :type: str
        """
        allowed_values = ["ALERTING", "DIALING", "CONTACTING", "OFFERING", "CONNECTED", "DISCONNECTED", "TERMINATED", "NONE"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def id(self):
        """
        Gets the id of this QueueConversationEventTopicChat.


        :return: The id of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationEventTopicChat.


        :param id: The id of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._id = id

    @property
    def provider(self):
        """
        Gets the provider of this QueueConversationEventTopicChat.


        :return: The provider of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this QueueConversationEventTopicChat.


        :param provider: The provider of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this QueueConversationEventTopicChat.


        :return: The script_id of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this QueueConversationEventTopicChat.


        :param script_id: The script_id of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this QueueConversationEventTopicChat.


        :return: The peer_id of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this QueueConversationEventTopicChat.


        :param peer_id: The peer_id of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def room_id(self):
        """
        Gets the room_id of this QueueConversationEventTopicChat.


        :return: The room_id of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this QueueConversationEventTopicChat.


        :param room_id: The room_id of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._room_id = room_id

    @property
    def avatar_image_url(self):
        """
        Gets the avatar_image_url of this QueueConversationEventTopicChat.


        :return: The avatar_image_url of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._avatar_image_url

    @avatar_image_url.setter
    def avatar_image_url(self, avatar_image_url):
        """
        Sets the avatar_image_url of this QueueConversationEventTopicChat.


        :param avatar_image_url: The avatar_image_url of this QueueConversationEventTopicChat.
        :type: str
        """
        
        self._avatar_image_url = avatar_image_url

    @property
    def held(self):
        """
        Gets the held of this QueueConversationEventTopicChat.


        :return: The held of this QueueConversationEventTopicChat.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this QueueConversationEventTopicChat.


        :param held: The held of this QueueConversationEventTopicChat.
        :type: bool
        """
        
        self._held = held

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this QueueConversationEventTopicChat.


        :return: The disconnect_type of this QueueConversationEventTopicChat.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this QueueConversationEventTopicChat.


        :param disconnect_type: The disconnect_type of this QueueConversationEventTopicChat.
        :type: str
        """
        allowed_values = ["ENDPOINT", "CLIENT", "SYSTEM", "TIMEOUT", "TRANSFER", "TRANSFER_CONFERENCE", "TRANSFER_CONSULT", "TRANSFER_NOANSWER", "TRANSFER_NOTAVAILABLE", "TRANSFER_FORWARD", "TRANSPORT_FAILURE", "ERROR", "PEER", "OTHER", "SPAM", "UNCALLABLE"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this QueueConversationEventTopicChat.


        :return: The start_hold_time of this QueueConversationEventTopicChat.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this QueueConversationEventTopicChat.


        :param start_hold_time: The start_hold_time of this QueueConversationEventTopicChat.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationEventTopicChat.


        :return: The connected_time of this QueueConversationEventTopicChat.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationEventTopicChat.


        :param connected_time: The connected_time of this QueueConversationEventTopicChat.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this QueueConversationEventTopicChat.


        :return: The disconnected_time of this QueueConversationEventTopicChat.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this QueueConversationEventTopicChat.


        :param disconnected_time: The disconnected_time of this QueueConversationEventTopicChat.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def journey_context(self):
        """
        Gets the journey_context of this QueueConversationEventTopicChat.


        :return: The journey_context of this QueueConversationEventTopicChat.
        :rtype: QueueConversationEventTopicJourneyContext
        """
        return self._journey_context

    @journey_context.setter
    def journey_context(self, journey_context):
        """
        Sets the journey_context of this QueueConversationEventTopicChat.


        :param journey_context: The journey_context of this QueueConversationEventTopicChat.
        :type: QueueConversationEventTopicJourneyContext
        """
        
        self._journey_context = journey_context

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationEventTopicChat.


        :return: The wrapup of this QueueConversationEventTopicChat.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationEventTopicChat.


        :param wrapup: The wrapup of this QueueConversationEventTopicChat.
        :type: QueueConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this QueueConversationEventTopicChat.


        :return: The after_call_work of this QueueConversationEventTopicChat.
        :rtype: QueueConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this QueueConversationEventTopicChat.


        :param after_call_work: The after_call_work of this QueueConversationEventTopicChat.
        :type: QueueConversationEventTopicAfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationEventTopicChat.


        :return: The additional_properties of this QueueConversationEventTopicChat.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationEventTopicChat.


        :param additional_properties: The additional_properties of this QueueConversationEventTopicChat.
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

