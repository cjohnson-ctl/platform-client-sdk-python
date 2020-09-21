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

class QueueConversationSocialExpressionEventTopicCall(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationSocialExpressionEventTopicCall - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'recording': 'bool',
            'recording_state': 'str',
            'muted': 'bool',
            'confined': 'bool',
            'held': 'bool',
            'error_info': 'QueueConversationSocialExpressionEventTopicErrorDetails',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'direction': 'str',
            'document_id': 'str',
            'pcSelf': 'QueueConversationSocialExpressionEventTopicAddress',
            'other': 'QueueConversationSocialExpressionEventTopicAddress',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'disconnect_reasons': 'list[QueueConversationSocialExpressionEventTopicDisconnectReason]',
            'fax_status': 'QueueConversationSocialExpressionEventTopicFaxStatus',
            'uui_data': 'str',
            'wrapup': 'QueueConversationSocialExpressionEventTopicWrapup',
            'after_call_work': 'QueueConversationSocialExpressionEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'agent_assistant_id': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'recording': 'recording',
            'recording_state': 'recordingState',
            'muted': 'muted',
            'confined': 'confined',
            'held': 'held',
            'error_info': 'errorInfo',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'direction': 'direction',
            'document_id': 'documentId',
            'pcSelf': 'self',
            'other': 'other',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'disconnect_reasons': 'disconnectReasons',
            'fax_status': 'faxStatus',
            'uui_data': 'uuiData',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'agent_assistant_id': 'agentAssistantId',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._state = None
        self._recording = None
        self._recording_state = None
        self._muted = None
        self._confined = None
        self._held = None
        self._error_info = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._direction = None
        self._document_id = None
        self._pcSelf = None
        self._other = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._connected_time = None
        self._disconnected_time = None
        self._disconnect_reasons = None
        self._fax_status = None
        self._uui_data = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._agent_assistant_id = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this QueueConversationSocialExpressionEventTopicCall.


        :return: The id of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationSocialExpressionEventTopicCall.


        :param id: The id of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this QueueConversationSocialExpressionEventTopicCall.


        :return: The state of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this QueueConversationSocialExpressionEventTopicCall.


        :param state: The state of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        allowed_values = ["ALERTING", "DIALING", "CONTACTING", "OFFERING", "CONNECTED", "DISCONNECTED", "TERMINATED", "UPLOADING", "CONVERTING", "TRANSMITTING", "NONE"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def recording(self):
        """
        Gets the recording of this QueueConversationSocialExpressionEventTopicCall.


        :return: The recording of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: bool
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        """
        Sets the recording of this QueueConversationSocialExpressionEventTopicCall.


        :param recording: The recording of this QueueConversationSocialExpressionEventTopicCall.
        :type: bool
        """
        
        self._recording = recording

    @property
    def recording_state(self):
        """
        Gets the recording_state of this QueueConversationSocialExpressionEventTopicCall.


        :return: The recording_state of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._recording_state

    @recording_state.setter
    def recording_state(self, recording_state):
        """
        Sets the recording_state of this QueueConversationSocialExpressionEventTopicCall.


        :param recording_state: The recording_state of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        allowed_values = ["NONE", "ACTIVE", "PAUSED"]
        if recording_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for recording_state -> " + recording_state
            self._recording_state = "outdated_sdk_version"
        else:
            self._recording_state = recording_state

    @property
    def muted(self):
        """
        Gets the muted of this QueueConversationSocialExpressionEventTopicCall.


        :return: The muted of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """
        Sets the muted of this QueueConversationSocialExpressionEventTopicCall.


        :param muted: The muted of this QueueConversationSocialExpressionEventTopicCall.
        :type: bool
        """
        
        self._muted = muted

    @property
    def confined(self):
        """
        Gets the confined of this QueueConversationSocialExpressionEventTopicCall.


        :return: The confined of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: bool
        """
        return self._confined

    @confined.setter
    def confined(self, confined):
        """
        Sets the confined of this QueueConversationSocialExpressionEventTopicCall.


        :param confined: The confined of this QueueConversationSocialExpressionEventTopicCall.
        :type: bool
        """
        
        self._confined = confined

    @property
    def held(self):
        """
        Gets the held of this QueueConversationSocialExpressionEventTopicCall.


        :return: The held of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this QueueConversationSocialExpressionEventTopicCall.


        :param held: The held of this QueueConversationSocialExpressionEventTopicCall.
        :type: bool
        """
        
        self._held = held

    @property
    def error_info(self):
        """
        Gets the error_info of this QueueConversationSocialExpressionEventTopicCall.


        :return: The error_info of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicErrorDetails
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this QueueConversationSocialExpressionEventTopicCall.


        :param error_info: The error_info of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicErrorDetails
        """
        
        self._error_info = error_info

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this QueueConversationSocialExpressionEventTopicCall.


        :return: The disconnect_type of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this QueueConversationSocialExpressionEventTopicCall.


        :param disconnect_type: The disconnect_type of this QueueConversationSocialExpressionEventTopicCall.
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
        Gets the start_hold_time of this QueueConversationSocialExpressionEventTopicCall.


        :return: The start_hold_time of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this QueueConversationSocialExpressionEventTopicCall.


        :param start_hold_time: The start_hold_time of this QueueConversationSocialExpressionEventTopicCall.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def direction(self):
        """
        Gets the direction of this QueueConversationSocialExpressionEventTopicCall.


        :return: The direction of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this QueueConversationSocialExpressionEventTopicCall.


        :param direction: The direction of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        allowed_values = ["OUTBOUND", "INBOUND"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def document_id(self):
        """
        Gets the document_id of this QueueConversationSocialExpressionEventTopicCall.


        :return: The document_id of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this QueueConversationSocialExpressionEventTopicCall.


        :param document_id: The document_id of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._document_id = document_id

    @property
    def pcSelf(self):
        """
        Gets the pcSelf of this QueueConversationSocialExpressionEventTopicCall.


        :return: The pcSelf of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicAddress
        """
        return self._pcSelf

    @pcSelf.setter
    def pcSelf(self, pcSelf):
        """
        Sets the pcSelf of this QueueConversationSocialExpressionEventTopicCall.


        :param pcSelf: The pcSelf of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicAddress
        """
        
        self._pcSelf = pcSelf

    @property
    def other(self):
        """
        Gets the other of this QueueConversationSocialExpressionEventTopicCall.


        :return: The other of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicAddress
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this QueueConversationSocialExpressionEventTopicCall.


        :param other: The other of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicAddress
        """
        
        self._other = other

    @property
    def provider(self):
        """
        Gets the provider of this QueueConversationSocialExpressionEventTopicCall.


        :return: The provider of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this QueueConversationSocialExpressionEventTopicCall.


        :param provider: The provider of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this QueueConversationSocialExpressionEventTopicCall.


        :return: The script_id of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this QueueConversationSocialExpressionEventTopicCall.


        :param script_id: The script_id of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this QueueConversationSocialExpressionEventTopicCall.


        :return: The peer_id of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this QueueConversationSocialExpressionEventTopicCall.


        :param peer_id: The peer_id of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationSocialExpressionEventTopicCall.


        :return: The connected_time of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationSocialExpressionEventTopicCall.


        :param connected_time: The connected_time of this QueueConversationSocialExpressionEventTopicCall.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this QueueConversationSocialExpressionEventTopicCall.


        :return: The disconnected_time of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this QueueConversationSocialExpressionEventTopicCall.


        :param disconnected_time: The disconnected_time of this QueueConversationSocialExpressionEventTopicCall.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def disconnect_reasons(self):
        """
        Gets the disconnect_reasons of this QueueConversationSocialExpressionEventTopicCall.


        :return: The disconnect_reasons of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: list[QueueConversationSocialExpressionEventTopicDisconnectReason]
        """
        return self._disconnect_reasons

    @disconnect_reasons.setter
    def disconnect_reasons(self, disconnect_reasons):
        """
        Sets the disconnect_reasons of this QueueConversationSocialExpressionEventTopicCall.


        :param disconnect_reasons: The disconnect_reasons of this QueueConversationSocialExpressionEventTopicCall.
        :type: list[QueueConversationSocialExpressionEventTopicDisconnectReason]
        """
        
        self._disconnect_reasons = disconnect_reasons

    @property
    def fax_status(self):
        """
        Gets the fax_status of this QueueConversationSocialExpressionEventTopicCall.


        :return: The fax_status of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicFaxStatus
        """
        return self._fax_status

    @fax_status.setter
    def fax_status(self, fax_status):
        """
        Sets the fax_status of this QueueConversationSocialExpressionEventTopicCall.


        :param fax_status: The fax_status of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicFaxStatus
        """
        
        self._fax_status = fax_status

    @property
    def uui_data(self):
        """
        Gets the uui_data of this QueueConversationSocialExpressionEventTopicCall.


        :return: The uui_data of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._uui_data

    @uui_data.setter
    def uui_data(self, uui_data):
        """
        Sets the uui_data of this QueueConversationSocialExpressionEventTopicCall.


        :param uui_data: The uui_data of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._uui_data = uui_data

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationSocialExpressionEventTopicCall.


        :return: The wrapup of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationSocialExpressionEventTopicCall.


        :param wrapup: The wrapup of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this QueueConversationSocialExpressionEventTopicCall.


        :return: The after_call_work of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: QueueConversationSocialExpressionEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this QueueConversationSocialExpressionEventTopicCall.


        :param after_call_work: The after_call_work of this QueueConversationSocialExpressionEventTopicCall.
        :type: QueueConversationSocialExpressionEventTopicAfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self):
        """
        Gets the after_call_work_required of this QueueConversationSocialExpressionEventTopicCall.


        :return: The after_call_work_required of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required):
        """
        Sets the after_call_work_required of this QueueConversationSocialExpressionEventTopicCall.


        :param after_call_work_required: The after_call_work_required of this QueueConversationSocialExpressionEventTopicCall.
        :type: bool
        """
        
        self._after_call_work_required = after_call_work_required

    @property
    def agent_assistant_id(self):
        """
        Gets the agent_assistant_id of this QueueConversationSocialExpressionEventTopicCall.


        :return: The agent_assistant_id of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: str
        """
        return self._agent_assistant_id

    @agent_assistant_id.setter
    def agent_assistant_id(self, agent_assistant_id):
        """
        Sets the agent_assistant_id of this QueueConversationSocialExpressionEventTopicCall.


        :param agent_assistant_id: The agent_assistant_id of this QueueConversationSocialExpressionEventTopicCall.
        :type: str
        """
        
        self._agent_assistant_id = agent_assistant_id

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationSocialExpressionEventTopicCall.


        :return: The additional_properties of this QueueConversationSocialExpressionEventTopicCall.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationSocialExpressionEventTopicCall.


        :param additional_properties: The additional_properties of this QueueConversationSocialExpressionEventTopicCall.
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

