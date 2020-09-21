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

class QueueConversationEventTopicSocialExpression(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationEventTopicSocialExpression - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'social_media_id': 'str',
            'social_media_hub': 'str',
            'social_user_name': 'str',
            'preview_text': 'str',
            'recording_id': 'str',
            'held': 'bool',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'after_call_work': 'QueueConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'social_media_id': 'socialMediaId',
            'social_media_hub': 'socialMediaHub',
            'social_user_name': 'socialUserName',
            'preview_text': 'previewText',
            'recording_id': 'recordingId',
            'held': 'held',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'additional_properties': 'additionalProperties'
        }

        self._state = None
        self._id = None
        self._social_media_id = None
        self._social_media_hub = None
        self._social_user_name = None
        self._preview_text = None
        self._recording_id = None
        self._held = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._additional_properties = None

    @property
    def state(self):
        """
        Gets the state of this QueueConversationEventTopicSocialExpression.


        :return: The state of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this QueueConversationEventTopicSocialExpression.


        :param state: The state of this QueueConversationEventTopicSocialExpression.
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
        Gets the id of this QueueConversationEventTopicSocialExpression.


        :return: The id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationEventTopicSocialExpression.


        :param id: The id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._id = id

    @property
    def social_media_id(self):
        """
        Gets the social_media_id of this QueueConversationEventTopicSocialExpression.


        :return: The social_media_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_media_id

    @social_media_id.setter
    def social_media_id(self, social_media_id):
        """
        Sets the social_media_id of this QueueConversationEventTopicSocialExpression.


        :param social_media_id: The social_media_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._social_media_id = social_media_id

    @property
    def social_media_hub(self):
        """
        Gets the social_media_hub of this QueueConversationEventTopicSocialExpression.


        :return: The social_media_hub of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_media_hub

    @social_media_hub.setter
    def social_media_hub(self, social_media_hub):
        """
        Sets the social_media_hub of this QueueConversationEventTopicSocialExpression.


        :param social_media_hub: The social_media_hub of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._social_media_hub = social_media_hub

    @property
    def social_user_name(self):
        """
        Gets the social_user_name of this QueueConversationEventTopicSocialExpression.


        :return: The social_user_name of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_user_name

    @social_user_name.setter
    def social_user_name(self, social_user_name):
        """
        Sets the social_user_name of this QueueConversationEventTopicSocialExpression.


        :param social_user_name: The social_user_name of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._social_user_name = social_user_name

    @property
    def preview_text(self):
        """
        Gets the preview_text of this QueueConversationEventTopicSocialExpression.


        :return: The preview_text of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self, preview_text):
        """
        Sets the preview_text of this QueueConversationEventTopicSocialExpression.


        :param preview_text: The preview_text of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._preview_text = preview_text

    @property
    def recording_id(self):
        """
        Gets the recording_id of this QueueConversationEventTopicSocialExpression.


        :return: The recording_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id):
        """
        Sets the recording_id of this QueueConversationEventTopicSocialExpression.


        :param recording_id: The recording_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._recording_id = recording_id

    @property
    def held(self):
        """
        Gets the held of this QueueConversationEventTopicSocialExpression.


        :return: The held of this QueueConversationEventTopicSocialExpression.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this QueueConversationEventTopicSocialExpression.


        :param held: The held of this QueueConversationEventTopicSocialExpression.
        :type: bool
        """
        
        self._held = held

    @property
    def provider(self):
        """
        Gets the provider of this QueueConversationEventTopicSocialExpression.


        :return: The provider of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this QueueConversationEventTopicSocialExpression.


        :param provider: The provider of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this QueueConversationEventTopicSocialExpression.


        :return: The script_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this QueueConversationEventTopicSocialExpression.


        :param script_id: The script_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this QueueConversationEventTopicSocialExpression.


        :return: The peer_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this QueueConversationEventTopicSocialExpression.


        :param peer_id: The peer_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this QueueConversationEventTopicSocialExpression.


        :return: The disconnect_type of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this QueueConversationEventTopicSocialExpression.


        :param disconnect_type: The disconnect_type of this QueueConversationEventTopicSocialExpression.
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
        Gets the start_hold_time of this QueueConversationEventTopicSocialExpression.


        :return: The start_hold_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this QueueConversationEventTopicSocialExpression.


        :param start_hold_time: The start_hold_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationEventTopicSocialExpression.


        :return: The connected_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationEventTopicSocialExpression.


        :param connected_time: The connected_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this QueueConversationEventTopicSocialExpression.


        :return: The disconnected_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this QueueConversationEventTopicSocialExpression.


        :param disconnected_time: The disconnected_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationEventTopicSocialExpression.


        :return: The wrapup of this QueueConversationEventTopicSocialExpression.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationEventTopicSocialExpression.


        :param wrapup: The wrapup of this QueueConversationEventTopicSocialExpression.
        :type: QueueConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this QueueConversationEventTopicSocialExpression.


        :return: The after_call_work of this QueueConversationEventTopicSocialExpression.
        :rtype: QueueConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this QueueConversationEventTopicSocialExpression.


        :param after_call_work: The after_call_work of this QueueConversationEventTopicSocialExpression.
        :type: QueueConversationEventTopicAfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self):
        """
        Gets the after_call_work_required of this QueueConversationEventTopicSocialExpression.


        :return: The after_call_work_required of this QueueConversationEventTopicSocialExpression.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required):
        """
        Sets the after_call_work_required of this QueueConversationEventTopicSocialExpression.


        :param after_call_work_required: The after_call_work_required of this QueueConversationEventTopicSocialExpression.
        :type: bool
        """
        
        self._after_call_work_required = after_call_work_required

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationEventTopicSocialExpression.


        :return: The additional_properties of this QueueConversationEventTopicSocialExpression.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationEventTopicSocialExpression.


        :param additional_properties: The additional_properties of this QueueConversationEventTopicSocialExpression.
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

