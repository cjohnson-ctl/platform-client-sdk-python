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

class CallbackBasic(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CallbackBasic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'segments': 'list[Segment]',
            'direction': 'str',
            'held': 'bool',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'dialer_preview': 'DialerPreview',
            'voicemail': 'Voicemail',
            'callback_numbers': 'list[str]',
            'callback_user_name': 'str',
            'script_id': 'str',
            'external_campaign': 'bool',
            'skip_enabled': 'bool',
            'timeout_seconds': 'int',
            'start_alerting_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'callback_scheduled_time': 'datetime',
            'automated_callback_config_id': 'str',
            'provider': 'str',
            'peer_id': 'str',
            'wrapup': 'Wrapup',
            'after_call_work': 'AfterCallWork',
            'after_call_work_required': 'bool'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'segments': 'segments',
            'direction': 'direction',
            'held': 'held',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'dialer_preview': 'dialerPreview',
            'voicemail': 'voicemail',
            'callback_numbers': 'callbackNumbers',
            'callback_user_name': 'callbackUserName',
            'script_id': 'scriptId',
            'external_campaign': 'externalCampaign',
            'skip_enabled': 'skipEnabled',
            'timeout_seconds': 'timeoutSeconds',
            'start_alerting_time': 'startAlertingTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'callback_scheduled_time': 'callbackScheduledTime',
            'automated_callback_config_id': 'automatedCallbackConfigId',
            'provider': 'provider',
            'peer_id': 'peerId',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired'
        }

        self._state = None
        self._id = None
        self._segments = None
        self._direction = None
        self._held = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._dialer_preview = None
        self._voicemail = None
        self._callback_numbers = None
        self._callback_user_name = None
        self._script_id = None
        self._external_campaign = None
        self._skip_enabled = None
        self._timeout_seconds = None
        self._start_alerting_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._callback_scheduled_time = None
        self._automated_callback_config_id = None
        self._provider = None
        self._peer_id = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None

    @property
    def state(self):
        """
        Gets the state of this CallbackBasic.
        The connection state of this communication.

        :return: The state of this CallbackBasic.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CallbackBasic.
        The connection state of this communication.

        :param state: The state of this CallbackBasic.
        :type: str
        """
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "scheduled", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def id(self):
        """
        Gets the id of this CallbackBasic.
        A globally unique identifier for this communication.

        :return: The id of this CallbackBasic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CallbackBasic.
        A globally unique identifier for this communication.

        :param id: The id of this CallbackBasic.
        :type: str
        """
        
        self._id = id

    @property
    def segments(self):
        """
        Gets the segments of this CallbackBasic.
        The time line of the participant's callback, divided into activity segments.

        :return: The segments of this CallbackBasic.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this CallbackBasic.
        The time line of the participant's callback, divided into activity segments.

        :param segments: The segments of this CallbackBasic.
        :type: list[Segment]
        """
        
        self._segments = segments

    @property
    def direction(self):
        """
        Gets the direction of this CallbackBasic.
        The direction of the call

        :return: The direction of this CallbackBasic.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this CallbackBasic.
        The direction of the call

        :param direction: The direction of this CallbackBasic.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def held(self):
        """
        Gets the held of this CallbackBasic.
        True if this call is held and the person on this side hears silence.

        :return: The held of this CallbackBasic.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this CallbackBasic.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this CallbackBasic.
        :type: bool
        """
        
        self._held = held

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this CallbackBasic.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this CallbackBasic.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this CallbackBasic.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this CallbackBasic.
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
        Gets the start_hold_time of this CallbackBasic.
        The timestamp the callback was placed on hold in the cloud clock if the callback is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_hold_time of this CallbackBasic.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this CallbackBasic.
        The timestamp the callback was placed on hold in the cloud clock if the callback is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_hold_time: The start_hold_time of this CallbackBasic.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def dialer_preview(self):
        """
        Gets the dialer_preview of this CallbackBasic.
        The preview data to be used when this callback is a Preview.

        :return: The dialer_preview of this CallbackBasic.
        :rtype: DialerPreview
        """
        return self._dialer_preview

    @dialer_preview.setter
    def dialer_preview(self, dialer_preview):
        """
        Sets the dialer_preview of this CallbackBasic.
        The preview data to be used when this callback is a Preview.

        :param dialer_preview: The dialer_preview of this CallbackBasic.
        :type: DialerPreview
        """
        
        self._dialer_preview = dialer_preview

    @property
    def voicemail(self):
        """
        Gets the voicemail of this CallbackBasic.
        The voicemail data to be used when this callback is an ACD voicemail.

        :return: The voicemail of this CallbackBasic.
        :rtype: Voicemail
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """
        Sets the voicemail of this CallbackBasic.
        The voicemail data to be used when this callback is an ACD voicemail.

        :param voicemail: The voicemail of this CallbackBasic.
        :type: Voicemail
        """
        
        self._voicemail = voicemail

    @property
    def callback_numbers(self):
        """
        Gets the callback_numbers of this CallbackBasic.
        The phone number(s) to use to place the callback.

        :return: The callback_numbers of this CallbackBasic.
        :rtype: list[str]
        """
        return self._callback_numbers

    @callback_numbers.setter
    def callback_numbers(self, callback_numbers):
        """
        Sets the callback_numbers of this CallbackBasic.
        The phone number(s) to use to place the callback.

        :param callback_numbers: The callback_numbers of this CallbackBasic.
        :type: list[str]
        """
        
        self._callback_numbers = callback_numbers

    @property
    def callback_user_name(self):
        """
        Gets the callback_user_name of this CallbackBasic.
        The name of the user requesting a callback.

        :return: The callback_user_name of this CallbackBasic.
        :rtype: str
        """
        return self._callback_user_name

    @callback_user_name.setter
    def callback_user_name(self, callback_user_name):
        """
        Sets the callback_user_name of this CallbackBasic.
        The name of the user requesting a callback.

        :param callback_user_name: The callback_user_name of this CallbackBasic.
        :type: str
        """
        
        self._callback_user_name = callback_user_name

    @property
    def script_id(self):
        """
        Gets the script_id of this CallbackBasic.
        The UUID of the script to use.

        :return: The script_id of this CallbackBasic.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this CallbackBasic.
        The UUID of the script to use.

        :param script_id: The script_id of this CallbackBasic.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def external_campaign(self):
        """
        Gets the external_campaign of this CallbackBasic.
        True if the call for the callback uses external dialing.

        :return: The external_campaign of this CallbackBasic.
        :rtype: bool
        """
        return self._external_campaign

    @external_campaign.setter
    def external_campaign(self, external_campaign):
        """
        Sets the external_campaign of this CallbackBasic.
        True if the call for the callback uses external dialing.

        :param external_campaign: The external_campaign of this CallbackBasic.
        :type: bool
        """
        
        self._external_campaign = external_campaign

    @property
    def skip_enabled(self):
        """
        Gets the skip_enabled of this CallbackBasic.
        True if the ability to skip a callback should be enabled.

        :return: The skip_enabled of this CallbackBasic.
        :rtype: bool
        """
        return self._skip_enabled

    @skip_enabled.setter
    def skip_enabled(self, skip_enabled):
        """
        Sets the skip_enabled of this CallbackBasic.
        True if the ability to skip a callback should be enabled.

        :param skip_enabled: The skip_enabled of this CallbackBasic.
        :type: bool
        """
        
        self._skip_enabled = skip_enabled

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this CallbackBasic.
        The number of seconds before the system automatically places a call for a callback.  0 means the automatic placement is disabled.

        :return: The timeout_seconds of this CallbackBasic.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this CallbackBasic.
        The number of seconds before the system automatically places a call for a callback.  0 means the automatic placement is disabled.

        :param timeout_seconds: The timeout_seconds of this CallbackBasic.
        :type: int
        """
        
        self._timeout_seconds = timeout_seconds

    @property
    def start_alerting_time(self):
        """
        Gets the start_alerting_time of this CallbackBasic.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_alerting_time of this CallbackBasic.
        :rtype: datetime
        """
        return self._start_alerting_time

    @start_alerting_time.setter
    def start_alerting_time(self, start_alerting_time):
        """
        Sets the start_alerting_time of this CallbackBasic.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_alerting_time: The start_alerting_time of this CallbackBasic.
        :type: datetime
        """
        
        self._start_alerting_time = start_alerting_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this CallbackBasic.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The connected_time of this CallbackBasic.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this CallbackBasic.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param connected_time: The connected_time of this CallbackBasic.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this CallbackBasic.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The disconnected_time of this CallbackBasic.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this CallbackBasic.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param disconnected_time: The disconnected_time of this CallbackBasic.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def callback_scheduled_time(self):
        """
        Gets the callback_scheduled_time of this CallbackBasic.
        The timestamp when this communication is scheduled in the provider clock. If this value is missing it indicates the callback will be placed immediately. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The callback_scheduled_time of this CallbackBasic.
        :rtype: datetime
        """
        return self._callback_scheduled_time

    @callback_scheduled_time.setter
    def callback_scheduled_time(self, callback_scheduled_time):
        """
        Sets the callback_scheduled_time of this CallbackBasic.
        The timestamp when this communication is scheduled in the provider clock. If this value is missing it indicates the callback will be placed immediately. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param callback_scheduled_time: The callback_scheduled_time of this CallbackBasic.
        :type: datetime
        """
        
        self._callback_scheduled_time = callback_scheduled_time

    @property
    def automated_callback_config_id(self):
        """
        Gets the automated_callback_config_id of this CallbackBasic.
        The id of the config for automatically placing the callback (and handling the disposition). If null, the callback will not be placed automatically but routed to an agent as per normal.

        :return: The automated_callback_config_id of this CallbackBasic.
        :rtype: str
        """
        return self._automated_callback_config_id

    @automated_callback_config_id.setter
    def automated_callback_config_id(self, automated_callback_config_id):
        """
        Sets the automated_callback_config_id of this CallbackBasic.
        The id of the config for automatically placing the callback (and handling the disposition). If null, the callback will not be placed automatically but routed to an agent as per normal.

        :param automated_callback_config_id: The automated_callback_config_id of this CallbackBasic.
        :type: str
        """
        
        self._automated_callback_config_id = automated_callback_config_id

    @property
    def provider(self):
        """
        Gets the provider of this CallbackBasic.
        The source provider for the callback.

        :return: The provider of this CallbackBasic.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this CallbackBasic.
        The source provider for the callback.

        :param provider: The provider of this CallbackBasic.
        :type: str
        """
        
        self._provider = provider

    @property
    def peer_id(self):
        """
        Gets the peer_id of this CallbackBasic.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this CallbackBasic.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this CallbackBasic.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this CallbackBasic.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def wrapup(self):
        """
        Gets the wrapup of this CallbackBasic.
        Call wrap up or disposition data.

        :return: The wrapup of this CallbackBasic.
        :rtype: Wrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this CallbackBasic.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this CallbackBasic.
        :type: Wrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this CallbackBasic.
        After-call work for the communication.

        :return: The after_call_work of this CallbackBasic.
        :rtype: AfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this CallbackBasic.
        After-call work for the communication.

        :param after_call_work: The after_call_work of this CallbackBasic.
        :type: AfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self):
        """
        Gets the after_call_work_required of this CallbackBasic.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this CallbackBasic.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required):
        """
        Sets the after_call_work_required of this CallbackBasic.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this CallbackBasic.
        :type: bool
        """
        
        self._after_call_work_required = after_call_work_required

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

