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


class CallbackMediaParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CallbackMediaParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'address': 'str',
            'start_time': 'datetime',
            'connected_time': 'datetime',
            'end_time': 'datetime',
            'start_hold_time': 'datetime',
            'purpose': 'str',
            'state': 'str',
            'direction': 'str',
            'disconnect_type': 'str',
            'held': 'bool',
            'wrapup_required': 'bool',
            'wrapup_prompt': 'str',
            'user': 'UriReference',
            'queue': 'UriReference',
            'attributes': 'dict(str, str)',
            'error_info': 'ErrorBody',
            'script': 'UriReference',
            'wrapup_timeout_ms': 'int',
            'wrapup_skipped': 'bool',
            'alerting_timeout_ms': 'int',
            'provider': 'str',
            'external_contact': 'UriReference',
            'external_organization': 'UriReference',
            'wrapup': 'Wrapup',
            'peer': 'str',
            'flagged_reason': 'str',
            'journey_context': 'JourneyContext',
            'conversation_routing_data': 'ConversationRoutingData',
            'outbound_preview': 'DialerPreview',
            'voicemail': 'Voicemail',
            'callback_numbers': 'list[str]',
            'callback_user_name': 'str',
            'skip_enabled': 'bool',
            'timeout_seconds': 'int',
            'automated_callback_config_id': 'str',
            'callback_scheduled_time': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'start_time': 'startTime',
            'connected_time': 'connectedTime',
            'end_time': 'endTime',
            'start_hold_time': 'startHoldTime',
            'purpose': 'purpose',
            'state': 'state',
            'direction': 'direction',
            'disconnect_type': 'disconnectType',
            'held': 'held',
            'wrapup_required': 'wrapupRequired',
            'wrapup_prompt': 'wrapupPrompt',
            'user': 'user',
            'queue': 'queue',
            'attributes': 'attributes',
            'error_info': 'errorInfo',
            'script': 'script',
            'wrapup_timeout_ms': 'wrapupTimeoutMs',
            'wrapup_skipped': 'wrapupSkipped',
            'alerting_timeout_ms': 'alertingTimeoutMs',
            'provider': 'provider',
            'external_contact': 'externalContact',
            'external_organization': 'externalOrganization',
            'wrapup': 'wrapup',
            'peer': 'peer',
            'flagged_reason': 'flaggedReason',
            'journey_context': 'journeyContext',
            'conversation_routing_data': 'conversationRoutingData',
            'outbound_preview': 'outboundPreview',
            'voicemail': 'voicemail',
            'callback_numbers': 'callbackNumbers',
            'callback_user_name': 'callbackUserName',
            'skip_enabled': 'skipEnabled',
            'timeout_seconds': 'timeoutSeconds',
            'automated_callback_config_id': 'automatedCallbackConfigId',
            'callback_scheduled_time': 'callbackScheduledTime'
        }

        self._id = None
        self._name = None
        self._address = None
        self._start_time = None
        self._connected_time = None
        self._end_time = None
        self._start_hold_time = None
        self._purpose = None
        self._state = None
        self._direction = None
        self._disconnect_type = None
        self._held = None
        self._wrapup_required = None
        self._wrapup_prompt = None
        self._user = None
        self._queue = None
        self._attributes = None
        self._error_info = None
        self._script = None
        self._wrapup_timeout_ms = None
        self._wrapup_skipped = None
        self._alerting_timeout_ms = None
        self._provider = None
        self._external_contact = None
        self._external_organization = None
        self._wrapup = None
        self._peer = None
        self._flagged_reason = None
        self._journey_context = None
        self._conversation_routing_data = None
        self._outbound_preview = None
        self._voicemail = None
        self._callback_numbers = None
        self._callback_user_name = None
        self._skip_enabled = None
        self._timeout_seconds = None
        self._automated_callback_config_id = None
        self._callback_scheduled_time = None

    @property
    def id(self):
        """
        Gets the id of this CallbackMediaParticipant.
        The unique participant ID.

        :return: The id of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CallbackMediaParticipant.
        The unique participant ID.

        :param id: The id of this CallbackMediaParticipant.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CallbackMediaParticipant.
        The display friendly name of the participant.

        :return: The name of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CallbackMediaParticipant.
        The display friendly name of the participant.

        :param name: The name of this CallbackMediaParticipant.
        :type: str
        """
        
        self._name = name

    @property
    def address(self):
        """
        Gets the address of this CallbackMediaParticipant.
        The participant address.

        :return: The address of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this CallbackMediaParticipant.
        The participant address.

        :param address: The address of this CallbackMediaParticipant.
        :type: str
        """
        
        self._address = address

    @property
    def start_time(self):
        """
        Gets the start_time of this CallbackMediaParticipant.
        The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_time of this CallbackMediaParticipant.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this CallbackMediaParticipant.
        The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_time: The start_time of this CallbackMediaParticipant.
        :type: datetime
        """
        
        self._start_time = start_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this CallbackMediaParticipant.
        The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The connected_time of this CallbackMediaParticipant.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this CallbackMediaParticipant.
        The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param connected_time: The connected_time of this CallbackMediaParticipant.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def end_time(self):
        """
        Gets the end_time of this CallbackMediaParticipant.
        The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The end_time of this CallbackMediaParticipant.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this CallbackMediaParticipant.
        The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param end_time: The end_time of this CallbackMediaParticipant.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this CallbackMediaParticipant.
        The time when this participant's hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_hold_time of this CallbackMediaParticipant.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this CallbackMediaParticipant.
        The time when this participant's hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_hold_time: The start_hold_time of this CallbackMediaParticipant.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def purpose(self):
        """
        Gets the purpose of this CallbackMediaParticipant.
        The participant's purpose.  Values can be: 'agent', 'user', 'customer', 'external', 'acd', 'ivr

        :return: The purpose of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this CallbackMediaParticipant.
        The participant's purpose.  Values can be: 'agent', 'user', 'customer', 'external', 'acd', 'ivr

        :param purpose: The purpose of this CallbackMediaParticipant.
        :type: str
        """
        
        self._purpose = purpose

    @property
    def state(self):
        """
        Gets the state of this CallbackMediaParticipant.
        The participant's state.  Values can be: 'alerting', 'connected', 'disconnected', 'dialing', 'contacting

        :return: The state of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CallbackMediaParticipant.
        The participant's state.  Values can be: 'alerting', 'connected', 'disconnected', 'dialing', 'contacting

        :param state: The state of this CallbackMediaParticipant.
        :type: str
        """
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "converting", "uploading", "transmitting", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def direction(self):
        """
        Gets the direction of this CallbackMediaParticipant.
        The participant's direction.  Values can be: 'inbound' or 'outbound'

        :return: The direction of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this CallbackMediaParticipant.
        The participant's direction.  Values can be: 'inbound' or 'outbound'

        :param direction: The direction of this CallbackMediaParticipant.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this CallbackMediaParticipant.
        The reason the participant was disconnected from the conversation.

        :return: The disconnect_type of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this CallbackMediaParticipant.
        The reason the participant was disconnected from the conversation.

        :param disconnect_type: The disconnect_type of this CallbackMediaParticipant.
        :type: str
        """
        allowed_values = ["endpoint", "client", "system", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transport.failure", "error", "peer", "other", "spam"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def held(self):
        """
        Gets the held of this CallbackMediaParticipant.
        Value is true when the participant is on hold.

        :return: The held of this CallbackMediaParticipant.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this CallbackMediaParticipant.
        Value is true when the participant is on hold.

        :param held: The held of this CallbackMediaParticipant.
        :type: bool
        """
        
        self._held = held

    @property
    def wrapup_required(self):
        """
        Gets the wrapup_required of this CallbackMediaParticipant.
        Value is true when the participant requires wrap-up.

        :return: The wrapup_required of this CallbackMediaParticipant.
        :rtype: bool
        """
        return self._wrapup_required

    @wrapup_required.setter
    def wrapup_required(self, wrapup_required):
        """
        Sets the wrapup_required of this CallbackMediaParticipant.
        Value is true when the participant requires wrap-up.

        :param wrapup_required: The wrapup_required of this CallbackMediaParticipant.
        :type: bool
        """
        
        self._wrapup_required = wrapup_required

    @property
    def wrapup_prompt(self):
        """
        Gets the wrapup_prompt of this CallbackMediaParticipant.
        The wrap-up prompt indicating the type of wrap-up to be performed.

        :return: The wrapup_prompt of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._wrapup_prompt

    @wrapup_prompt.setter
    def wrapup_prompt(self, wrapup_prompt):
        """
        Sets the wrapup_prompt of this CallbackMediaParticipant.
        The wrap-up prompt indicating the type of wrap-up to be performed.

        :param wrapup_prompt: The wrapup_prompt of this CallbackMediaParticipant.
        :type: str
        """
        
        self._wrapup_prompt = wrapup_prompt

    @property
    def user(self):
        """
        Gets the user of this CallbackMediaParticipant.
        The PureCloud user for this participant.

        :return: The user of this CallbackMediaParticipant.
        :rtype: UriReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this CallbackMediaParticipant.
        The PureCloud user for this participant.

        :param user: The user of this CallbackMediaParticipant.
        :type: UriReference
        """
        
        self._user = user

    @property
    def queue(self):
        """
        Gets the queue of this CallbackMediaParticipant.
        The PureCloud queue for this participant.

        :return: The queue of this CallbackMediaParticipant.
        :rtype: UriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this CallbackMediaParticipant.
        The PureCloud queue for this participant.

        :param queue: The queue of this CallbackMediaParticipant.
        :type: UriReference
        """
        
        self._queue = queue

    @property
    def attributes(self):
        """
        Gets the attributes of this CallbackMediaParticipant.
        A list of ad-hoc attributes for the participant.

        :return: The attributes of this CallbackMediaParticipant.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this CallbackMediaParticipant.
        A list of ad-hoc attributes for the participant.

        :param attributes: The attributes of this CallbackMediaParticipant.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def error_info(self):
        """
        Gets the error_info of this CallbackMediaParticipant.
        If the conversation ends in error, contains additional error details.

        :return: The error_info of this CallbackMediaParticipant.
        :rtype: ErrorBody
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this CallbackMediaParticipant.
        If the conversation ends in error, contains additional error details.

        :param error_info: The error_info of this CallbackMediaParticipant.
        :type: ErrorBody
        """
        
        self._error_info = error_info

    @property
    def script(self):
        """
        Gets the script of this CallbackMediaParticipant.
        The Engage script that should be used by this participant.

        :return: The script of this CallbackMediaParticipant.
        :rtype: UriReference
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this CallbackMediaParticipant.
        The Engage script that should be used by this participant.

        :param script: The script of this CallbackMediaParticipant.
        :type: UriReference
        """
        
        self._script = script

    @property
    def wrapup_timeout_ms(self):
        """
        Gets the wrapup_timeout_ms of this CallbackMediaParticipant.
        The amount of time the participant has to complete wrap-up.

        :return: The wrapup_timeout_ms of this CallbackMediaParticipant.
        :rtype: int
        """
        return self._wrapup_timeout_ms

    @wrapup_timeout_ms.setter
    def wrapup_timeout_ms(self, wrapup_timeout_ms):
        """
        Sets the wrapup_timeout_ms of this CallbackMediaParticipant.
        The amount of time the participant has to complete wrap-up.

        :param wrapup_timeout_ms: The wrapup_timeout_ms of this CallbackMediaParticipant.
        :type: int
        """
        
        self._wrapup_timeout_ms = wrapup_timeout_ms

    @property
    def wrapup_skipped(self):
        """
        Gets the wrapup_skipped of this CallbackMediaParticipant.
        Value is true when the participant has skipped wrap-up.

        :return: The wrapup_skipped of this CallbackMediaParticipant.
        :rtype: bool
        """
        return self._wrapup_skipped

    @wrapup_skipped.setter
    def wrapup_skipped(self, wrapup_skipped):
        """
        Sets the wrapup_skipped of this CallbackMediaParticipant.
        Value is true when the participant has skipped wrap-up.

        :param wrapup_skipped: The wrapup_skipped of this CallbackMediaParticipant.
        :type: bool
        """
        
        self._wrapup_skipped = wrapup_skipped

    @property
    def alerting_timeout_ms(self):
        """
        Gets the alerting_timeout_ms of this CallbackMediaParticipant.
        Specifies how long the agent has to answer an interaction before being marked as not responding.

        :return: The alerting_timeout_ms of this CallbackMediaParticipant.
        :rtype: int
        """
        return self._alerting_timeout_ms

    @alerting_timeout_ms.setter
    def alerting_timeout_ms(self, alerting_timeout_ms):
        """
        Sets the alerting_timeout_ms of this CallbackMediaParticipant.
        Specifies how long the agent has to answer an interaction before being marked as not responding.

        :param alerting_timeout_ms: The alerting_timeout_ms of this CallbackMediaParticipant.
        :type: int
        """
        
        self._alerting_timeout_ms = alerting_timeout_ms

    @property
    def provider(self):
        """
        Gets the provider of this CallbackMediaParticipant.
        The source provider for the communication.

        :return: The provider of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this CallbackMediaParticipant.
        The source provider for the communication.

        :param provider: The provider of this CallbackMediaParticipant.
        :type: str
        """
        
        self._provider = provider

    @property
    def external_contact(self):
        """
        Gets the external_contact of this CallbackMediaParticipant.
        If this participant represents an external contact, then this will be the reference for the external contact.

        :return: The external_contact of this CallbackMediaParticipant.
        :rtype: UriReference
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact):
        """
        Sets the external_contact of this CallbackMediaParticipant.
        If this participant represents an external contact, then this will be the reference for the external contact.

        :param external_contact: The external_contact of this CallbackMediaParticipant.
        :type: UriReference
        """
        
        self._external_contact = external_contact

    @property
    def external_organization(self):
        """
        Gets the external_organization of this CallbackMediaParticipant.
        If this participant represents an external org, then this will be the reference for the external org.

        :return: The external_organization of this CallbackMediaParticipant.
        :rtype: UriReference
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization):
        """
        Sets the external_organization of this CallbackMediaParticipant.
        If this participant represents an external org, then this will be the reference for the external org.

        :param external_organization: The external_organization of this CallbackMediaParticipant.
        :type: UriReference
        """
        
        self._external_organization = external_organization

    @property
    def wrapup(self):
        """
        Gets the wrapup of this CallbackMediaParticipant.
        Wrapup for this participant, if it has been applied.

        :return: The wrapup of this CallbackMediaParticipant.
        :rtype: Wrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this CallbackMediaParticipant.
        Wrapup for this participant, if it has been applied.

        :param wrapup: The wrapup of this CallbackMediaParticipant.
        :type: Wrapup
        """
        
        self._wrapup = wrapup

    @property
    def peer(self):
        """
        Gets the peer of this CallbackMediaParticipant.
        The peer communication corresponding to a matching leg for this communication.

        :return: The peer of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        """
        Sets the peer of this CallbackMediaParticipant.
        The peer communication corresponding to a matching leg for this communication.

        :param peer: The peer of this CallbackMediaParticipant.
        :type: str
        """
        
        self._peer = peer

    @property
    def flagged_reason(self):
        """
        Gets the flagged_reason of this CallbackMediaParticipant.
        The reason specifying why participant flagged the conversation.

        :return: The flagged_reason of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason):
        """
        Sets the flagged_reason of this CallbackMediaParticipant.
        The reason specifying why participant flagged the conversation.

        :param flagged_reason: The flagged_reason of this CallbackMediaParticipant.
        :type: str
        """
        allowed_values = ["general"]
        if flagged_reason.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for flagged_reason -> " + flagged_reason
            self._flagged_reason = "outdated_sdk_version"
        else:
            self._flagged_reason = flagged_reason

    @property
    def journey_context(self):
        """
        Gets the journey_context of this CallbackMediaParticipant.
        Journey System data/context that is applicable to this communication.  When used for historical purposes, the context should be immutable.  When null, there is no applicable Journey System context.

        :return: The journey_context of this CallbackMediaParticipant.
        :rtype: JourneyContext
        """
        return self._journey_context

    @journey_context.setter
    def journey_context(self, journey_context):
        """
        Sets the journey_context of this CallbackMediaParticipant.
        Journey System data/context that is applicable to this communication.  When used for historical purposes, the context should be immutable.  When null, there is no applicable Journey System context.

        :param journey_context: The journey_context of this CallbackMediaParticipant.
        :type: JourneyContext
        """
        
        self._journey_context = journey_context

    @property
    def conversation_routing_data(self):
        """
        Gets the conversation_routing_data of this CallbackMediaParticipant.
        Information on how a communication should be routed to an agent.

        :return: The conversation_routing_data of this CallbackMediaParticipant.
        :rtype: ConversationRoutingData
        """
        return self._conversation_routing_data

    @conversation_routing_data.setter
    def conversation_routing_data(self, conversation_routing_data):
        """
        Sets the conversation_routing_data of this CallbackMediaParticipant.
        Information on how a communication should be routed to an agent.

        :param conversation_routing_data: The conversation_routing_data of this CallbackMediaParticipant.
        :type: ConversationRoutingData
        """
        
        self._conversation_routing_data = conversation_routing_data

    @property
    def outbound_preview(self):
        """
        Gets the outbound_preview of this CallbackMediaParticipant.
        The outbound preview associated with this callback.

        :return: The outbound_preview of this CallbackMediaParticipant.
        :rtype: DialerPreview
        """
        return self._outbound_preview

    @outbound_preview.setter
    def outbound_preview(self, outbound_preview):
        """
        Sets the outbound_preview of this CallbackMediaParticipant.
        The outbound preview associated with this callback.

        :param outbound_preview: The outbound_preview of this CallbackMediaParticipant.
        :type: DialerPreview
        """
        
        self._outbound_preview = outbound_preview

    @property
    def voicemail(self):
        """
        Gets the voicemail of this CallbackMediaParticipant.
        The voicemail associated with this callback.

        :return: The voicemail of this CallbackMediaParticipant.
        :rtype: Voicemail
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """
        Sets the voicemail of this CallbackMediaParticipant.
        The voicemail associated with this callback.

        :param voicemail: The voicemail of this CallbackMediaParticipant.
        :type: Voicemail
        """
        
        self._voicemail = voicemail

    @property
    def callback_numbers(self):
        """
        Gets the callback_numbers of this CallbackMediaParticipant.
        The list of phone number to use for this callback.

        :return: The callback_numbers of this CallbackMediaParticipant.
        :rtype: list[str]
        """
        return self._callback_numbers

    @callback_numbers.setter
    def callback_numbers(self, callback_numbers):
        """
        Sets the callback_numbers of this CallbackMediaParticipant.
        The list of phone number to use for this callback.

        :param callback_numbers: The callback_numbers of this CallbackMediaParticipant.
        :type: list[str]
        """
        
        self._callback_numbers = callback_numbers

    @property
    def callback_user_name(self):
        """
        Gets the callback_user_name of this CallbackMediaParticipant.
        The name of the callback target.

        :return: The callback_user_name of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._callback_user_name

    @callback_user_name.setter
    def callback_user_name(self, callback_user_name):
        """
        Sets the callback_user_name of this CallbackMediaParticipant.
        The name of the callback target.

        :param callback_user_name: The callback_user_name of this CallbackMediaParticipant.
        :type: str
        """
        
        self._callback_user_name = callback_user_name

    @property
    def skip_enabled(self):
        """
        Gets the skip_enabled of this CallbackMediaParticipant.
        If true, the callback can be skipped

        :return: The skip_enabled of this CallbackMediaParticipant.
        :rtype: bool
        """
        return self._skip_enabled

    @skip_enabled.setter
    def skip_enabled(self, skip_enabled):
        """
        Sets the skip_enabled of this CallbackMediaParticipant.
        If true, the callback can be skipped

        :param skip_enabled: The skip_enabled of this CallbackMediaParticipant.
        :type: bool
        """
        
        self._skip_enabled = skip_enabled

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this CallbackMediaParticipant.
        Duration in seconds before the callback will be auto-dialed.

        :return: The timeout_seconds of this CallbackMediaParticipant.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this CallbackMediaParticipant.
        Duration in seconds before the callback will be auto-dialed.

        :param timeout_seconds: The timeout_seconds of this CallbackMediaParticipant.
        :type: int
        """
        
        self._timeout_seconds = timeout_seconds

    @property
    def automated_callback_config_id(self):
        """
        Gets the automated_callback_config_id of this CallbackMediaParticipant.
        The id of the config for automatically placing the callback (and handling the disposition). If absent, the callback will not be placed automatically but routed to an agent as per normal.

        :return: The automated_callback_config_id of this CallbackMediaParticipant.
        :rtype: str
        """
        return self._automated_callback_config_id

    @automated_callback_config_id.setter
    def automated_callback_config_id(self, automated_callback_config_id):
        """
        Sets the automated_callback_config_id of this CallbackMediaParticipant.
        The id of the config for automatically placing the callback (and handling the disposition). If absent, the callback will not be placed automatically but routed to an agent as per normal.

        :param automated_callback_config_id: The automated_callback_config_id of this CallbackMediaParticipant.
        :type: str
        """
        
        self._automated_callback_config_id = automated_callback_config_id

    @property
    def callback_scheduled_time(self):
        """
        Gets the callback_scheduled_time of this CallbackMediaParticipant.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The callback_scheduled_time of this CallbackMediaParticipant.
        :rtype: datetime
        """
        return self._callback_scheduled_time

    @callback_scheduled_time.setter
    def callback_scheduled_time(self, callback_scheduled_time):
        """
        Sets the callback_scheduled_time of this CallbackMediaParticipant.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param callback_scheduled_time: The callback_scheduled_time of this CallbackMediaParticipant.
        :type: datetime
        """
        
        self._callback_scheduled_time = callback_scheduled_time

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

