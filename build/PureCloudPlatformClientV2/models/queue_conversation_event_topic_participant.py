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


class QueueConversationEventTopicParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationEventTopicParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'connected_time': 'datetime',
            'end_time': 'datetime',
            'user_id': 'str',
            'external_contact_id': 'str',
            'external_organization_id': 'str',
            'name': 'str',
            'queue_id': 'str',
            'group_id': 'str',
            'purpose': 'str',
            'consult_participant_id': 'str',
            'address': 'str',
            'wrapup_required': 'bool',
            'wrapup_expected': 'bool',
            'wrapup_prompt': 'str',
            'wrapup_timeout_ms': 'int',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'alerting_timeout_ms': 'int',
            'monitored_participant_id': 'str',
            'screen_recording_state': 'str',
            'flagged_reason': 'str',
            'attributes': 'dict(str, str)',
            'calls': 'list[QueueConversationEventTopicCall]',
            'callbacks': 'list[QueueConversationEventTopicCallback]',
            'chats': 'list[QueueConversationEventTopicChat]',
            'cobrowsesessions': 'list[QueueConversationEventTopicCobrowse]',
            'emails': 'list[QueueConversationEventTopicEmail]',
            'messages': 'list[QueueConversationEventTopicMessage]',
            'screenshares': 'list[QueueConversationEventTopicScreenshare]',
            'social_expressions': 'list[QueueConversationEventTopicSocialExpression]',
            'videos': 'list[QueueConversationEventTopicVideo]',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'connected_time': 'connectedTime',
            'end_time': 'endTime',
            'user_id': 'userId',
            'external_contact_id': 'externalContactId',
            'external_organization_id': 'externalOrganizationId',
            'name': 'name',
            'queue_id': 'queueId',
            'group_id': 'groupId',
            'purpose': 'purpose',
            'consult_participant_id': 'consultParticipantId',
            'address': 'address',
            'wrapup_required': 'wrapupRequired',
            'wrapup_expected': 'wrapupExpected',
            'wrapup_prompt': 'wrapupPrompt',
            'wrapup_timeout_ms': 'wrapupTimeoutMs',
            'wrapup': 'wrapup',
            'alerting_timeout_ms': 'alertingTimeoutMs',
            'monitored_participant_id': 'monitoredParticipantId',
            'screen_recording_state': 'screenRecordingState',
            'flagged_reason': 'flaggedReason',
            'attributes': 'attributes',
            'calls': 'calls',
            'callbacks': 'callbacks',
            'chats': 'chats',
            'cobrowsesessions': 'cobrowsesessions',
            'emails': 'emails',
            'messages': 'messages',
            'screenshares': 'screenshares',
            'social_expressions': 'socialExpressions',
            'videos': 'videos',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._connected_time = None
        self._end_time = None
        self._user_id = None
        self._external_contact_id = None
        self._external_organization_id = None
        self._name = None
        self._queue_id = None
        self._group_id = None
        self._purpose = None
        self._consult_participant_id = None
        self._address = None
        self._wrapup_required = None
        self._wrapup_expected = None
        self._wrapup_prompt = None
        self._wrapup_timeout_ms = None
        self._wrapup = None
        self._alerting_timeout_ms = None
        self._monitored_participant_id = None
        self._screen_recording_state = None
        self._flagged_reason = None
        self._attributes = None
        self._calls = None
        self._callbacks = None
        self._chats = None
        self._cobrowsesessions = None
        self._emails = None
        self._messages = None
        self._screenshares = None
        self._social_expressions = None
        self._videos = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this QueueConversationEventTopicParticipant.


        :return: The id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationEventTopicParticipant.


        :param id: The id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._id = id

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationEventTopicParticipant.


        :return: The connected_time of this QueueConversationEventTopicParticipant.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationEventTopicParticipant.


        :param connected_time: The connected_time of this QueueConversationEventTopicParticipant.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def end_time(self):
        """
        Gets the end_time of this QueueConversationEventTopicParticipant.


        :return: The end_time of this QueueConversationEventTopicParticipant.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this QueueConversationEventTopicParticipant.


        :param end_time: The end_time of this QueueConversationEventTopicParticipant.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def user_id(self):
        """
        Gets the user_id of this QueueConversationEventTopicParticipant.


        :return: The user_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this QueueConversationEventTopicParticipant.


        :param user_id: The user_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this QueueConversationEventTopicParticipant.


        :return: The external_contact_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this QueueConversationEventTopicParticipant.


        :param external_contact_id: The external_contact_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def external_organization_id(self):
        """
        Gets the external_organization_id of this QueueConversationEventTopicParticipant.


        :return: The external_organization_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._external_organization_id

    @external_organization_id.setter
    def external_organization_id(self, external_organization_id):
        """
        Sets the external_organization_id of this QueueConversationEventTopicParticipant.


        :param external_organization_id: The external_organization_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._external_organization_id = external_organization_id

    @property
    def name(self):
        """
        Gets the name of this QueueConversationEventTopicParticipant.


        :return: The name of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QueueConversationEventTopicParticipant.


        :param name: The name of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._name = name

    @property
    def queue_id(self):
        """
        Gets the queue_id of this QueueConversationEventTopicParticipant.


        :return: The queue_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this QueueConversationEventTopicParticipant.


        :param queue_id: The queue_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def group_id(self):
        """
        Gets the group_id of this QueueConversationEventTopicParticipant.


        :return: The group_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this QueueConversationEventTopicParticipant.


        :param group_id: The group_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._group_id = group_id

    @property
    def purpose(self):
        """
        Gets the purpose of this QueueConversationEventTopicParticipant.


        :return: The purpose of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this QueueConversationEventTopicParticipant.


        :param purpose: The purpose of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._purpose = purpose

    @property
    def consult_participant_id(self):
        """
        Gets the consult_participant_id of this QueueConversationEventTopicParticipant.


        :return: The consult_participant_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._consult_participant_id

    @consult_participant_id.setter
    def consult_participant_id(self, consult_participant_id):
        """
        Sets the consult_participant_id of this QueueConversationEventTopicParticipant.


        :param consult_participant_id: The consult_participant_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._consult_participant_id = consult_participant_id

    @property
    def address(self):
        """
        Gets the address of this QueueConversationEventTopicParticipant.


        :return: The address of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this QueueConversationEventTopicParticipant.


        :param address: The address of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._address = address

    @property
    def wrapup_required(self):
        """
        Gets the wrapup_required of this QueueConversationEventTopicParticipant.


        :return: The wrapup_required of this QueueConversationEventTopicParticipant.
        :rtype: bool
        """
        return self._wrapup_required

    @wrapup_required.setter
    def wrapup_required(self, wrapup_required):
        """
        Sets the wrapup_required of this QueueConversationEventTopicParticipant.


        :param wrapup_required: The wrapup_required of this QueueConversationEventTopicParticipant.
        :type: bool
        """
        
        self._wrapup_required = wrapup_required

    @property
    def wrapup_expected(self):
        """
        Gets the wrapup_expected of this QueueConversationEventTopicParticipant.


        :return: The wrapup_expected of this QueueConversationEventTopicParticipant.
        :rtype: bool
        """
        return self._wrapup_expected

    @wrapup_expected.setter
    def wrapup_expected(self, wrapup_expected):
        """
        Sets the wrapup_expected of this QueueConversationEventTopicParticipant.


        :param wrapup_expected: The wrapup_expected of this QueueConversationEventTopicParticipant.
        :type: bool
        """
        
        self._wrapup_expected = wrapup_expected

    @property
    def wrapup_prompt(self):
        """
        Gets the wrapup_prompt of this QueueConversationEventTopicParticipant.


        :return: The wrapup_prompt of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._wrapup_prompt

    @wrapup_prompt.setter
    def wrapup_prompt(self, wrapup_prompt):
        """
        Sets the wrapup_prompt of this QueueConversationEventTopicParticipant.


        :param wrapup_prompt: The wrapup_prompt of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._wrapup_prompt = wrapup_prompt

    @property
    def wrapup_timeout_ms(self):
        """
        Gets the wrapup_timeout_ms of this QueueConversationEventTopicParticipant.


        :return: The wrapup_timeout_ms of this QueueConversationEventTopicParticipant.
        :rtype: int
        """
        return self._wrapup_timeout_ms

    @wrapup_timeout_ms.setter
    def wrapup_timeout_ms(self, wrapup_timeout_ms):
        """
        Sets the wrapup_timeout_ms of this QueueConversationEventTopicParticipant.


        :param wrapup_timeout_ms: The wrapup_timeout_ms of this QueueConversationEventTopicParticipant.
        :type: int
        """
        
        self._wrapup_timeout_ms = wrapup_timeout_ms

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationEventTopicParticipant.


        :return: The wrapup of this QueueConversationEventTopicParticipant.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationEventTopicParticipant.


        :param wrapup: The wrapup of this QueueConversationEventTopicParticipant.
        :type: QueueConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def alerting_timeout_ms(self):
        """
        Gets the alerting_timeout_ms of this QueueConversationEventTopicParticipant.


        :return: The alerting_timeout_ms of this QueueConversationEventTopicParticipant.
        :rtype: int
        """
        return self._alerting_timeout_ms

    @alerting_timeout_ms.setter
    def alerting_timeout_ms(self, alerting_timeout_ms):
        """
        Sets the alerting_timeout_ms of this QueueConversationEventTopicParticipant.


        :param alerting_timeout_ms: The alerting_timeout_ms of this QueueConversationEventTopicParticipant.
        :type: int
        """
        
        self._alerting_timeout_ms = alerting_timeout_ms

    @property
    def monitored_participant_id(self):
        """
        Gets the monitored_participant_id of this QueueConversationEventTopicParticipant.


        :return: The monitored_participant_id of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._monitored_participant_id

    @monitored_participant_id.setter
    def monitored_participant_id(self, monitored_participant_id):
        """
        Sets the monitored_participant_id of this QueueConversationEventTopicParticipant.


        :param monitored_participant_id: The monitored_participant_id of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._monitored_participant_id = monitored_participant_id

    @property
    def screen_recording_state(self):
        """
        Gets the screen_recording_state of this QueueConversationEventTopicParticipant.


        :return: The screen_recording_state of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._screen_recording_state

    @screen_recording_state.setter
    def screen_recording_state(self, screen_recording_state):
        """
        Sets the screen_recording_state of this QueueConversationEventTopicParticipant.


        :param screen_recording_state: The screen_recording_state of this QueueConversationEventTopicParticipant.
        :type: str
        """
        allowed_values = ["REQUESTED", "ACTIVE", "PAUSED", "STOPPED", "ERROR", "TIMEOUT"]
        if screen_recording_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for screen_recording_state -> " + screen_recording_state
            self._screen_recording_state = "outdated_sdk_version"
        else:
            self._screen_recording_state = screen_recording_state

    @property
    def flagged_reason(self):
        """
        Gets the flagged_reason of this QueueConversationEventTopicParticipant.


        :return: The flagged_reason of this QueueConversationEventTopicParticipant.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason):
        """
        Sets the flagged_reason of this QueueConversationEventTopicParticipant.


        :param flagged_reason: The flagged_reason of this QueueConversationEventTopicParticipant.
        :type: str
        """
        
        self._flagged_reason = flagged_reason

    @property
    def attributes(self):
        """
        Gets the attributes of this QueueConversationEventTopicParticipant.


        :return: The attributes of this QueueConversationEventTopicParticipant.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this QueueConversationEventTopicParticipant.


        :param attributes: The attributes of this QueueConversationEventTopicParticipant.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def calls(self):
        """
        Gets the calls of this QueueConversationEventTopicParticipant.


        :return: The calls of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicCall]
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """
        Sets the calls of this QueueConversationEventTopicParticipant.


        :param calls: The calls of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicCall]
        """
        
        self._calls = calls

    @property
    def callbacks(self):
        """
        Gets the callbacks of this QueueConversationEventTopicParticipant.


        :return: The callbacks of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicCallback]
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """
        Sets the callbacks of this QueueConversationEventTopicParticipant.


        :param callbacks: The callbacks of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicCallback]
        """
        
        self._callbacks = callbacks

    @property
    def chats(self):
        """
        Gets the chats of this QueueConversationEventTopicParticipant.


        :return: The chats of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicChat]
        """
        return self._chats

    @chats.setter
    def chats(self, chats):
        """
        Sets the chats of this QueueConversationEventTopicParticipant.


        :param chats: The chats of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicChat]
        """
        
        self._chats = chats

    @property
    def cobrowsesessions(self):
        """
        Gets the cobrowsesessions of this QueueConversationEventTopicParticipant.


        :return: The cobrowsesessions of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicCobrowse]
        """
        return self._cobrowsesessions

    @cobrowsesessions.setter
    def cobrowsesessions(self, cobrowsesessions):
        """
        Sets the cobrowsesessions of this QueueConversationEventTopicParticipant.


        :param cobrowsesessions: The cobrowsesessions of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicCobrowse]
        """
        
        self._cobrowsesessions = cobrowsesessions

    @property
    def emails(self):
        """
        Gets the emails of this QueueConversationEventTopicParticipant.


        :return: The emails of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this QueueConversationEventTopicParticipant.


        :param emails: The emails of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicEmail]
        """
        
        self._emails = emails

    @property
    def messages(self):
        """
        Gets the messages of this QueueConversationEventTopicParticipant.


        :return: The messages of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this QueueConversationEventTopicParticipant.


        :param messages: The messages of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicMessage]
        """
        
        self._messages = messages

    @property
    def screenshares(self):
        """
        Gets the screenshares of this QueueConversationEventTopicParticipant.


        :return: The screenshares of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicScreenshare]
        """
        return self._screenshares

    @screenshares.setter
    def screenshares(self, screenshares):
        """
        Sets the screenshares of this QueueConversationEventTopicParticipant.


        :param screenshares: The screenshares of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicScreenshare]
        """
        
        self._screenshares = screenshares

    @property
    def social_expressions(self):
        """
        Gets the social_expressions of this QueueConversationEventTopicParticipant.


        :return: The social_expressions of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicSocialExpression]
        """
        return self._social_expressions

    @social_expressions.setter
    def social_expressions(self, social_expressions):
        """
        Sets the social_expressions of this QueueConversationEventTopicParticipant.


        :param social_expressions: The social_expressions of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicSocialExpression]
        """
        
        self._social_expressions = social_expressions

    @property
    def videos(self):
        """
        Gets the videos of this QueueConversationEventTopicParticipant.


        :return: The videos of this QueueConversationEventTopicParticipant.
        :rtype: list[QueueConversationEventTopicVideo]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """
        Sets the videos of this QueueConversationEventTopicParticipant.


        :param videos: The videos of this QueueConversationEventTopicParticipant.
        :type: list[QueueConversationEventTopicVideo]
        """
        
        self._videos = videos

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationEventTopicParticipant.


        :return: The additional_properties of this QueueConversationEventTopicParticipant.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationEventTopicParticipant.


        :param additional_properties: The additional_properties of this QueueConversationEventTopicParticipant.
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
