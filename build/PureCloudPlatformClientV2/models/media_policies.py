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


class MediaPolicies(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MediaPolicies - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'call_policy': 'CallMediaPolicy',
            'chat_policy': 'ChatMediaPolicy',
            'email_policy': 'EmailMediaPolicy',
            'message_policy': 'MessageMediaPolicy'
        }

        self.attribute_map = {
            'call_policy': 'callPolicy',
            'chat_policy': 'chatPolicy',
            'email_policy': 'emailPolicy',
            'message_policy': 'messagePolicy'
        }

        self._call_policy = None
        self._chat_policy = None
        self._email_policy = None
        self._message_policy = None

    @property
    def call_policy(self):
        """
        Gets the call_policy of this MediaPolicies.
        Conditions and actions for calls

        :return: The call_policy of this MediaPolicies.
        :rtype: CallMediaPolicy
        """
        return self._call_policy

    @call_policy.setter
    def call_policy(self, call_policy):
        """
        Sets the call_policy of this MediaPolicies.
        Conditions and actions for calls

        :param call_policy: The call_policy of this MediaPolicies.
        :type: CallMediaPolicy
        """
        
        self._call_policy = call_policy

    @property
    def chat_policy(self):
        """
        Gets the chat_policy of this MediaPolicies.
        Conditions and actions for chats

        :return: The chat_policy of this MediaPolicies.
        :rtype: ChatMediaPolicy
        """
        return self._chat_policy

    @chat_policy.setter
    def chat_policy(self, chat_policy):
        """
        Sets the chat_policy of this MediaPolicies.
        Conditions and actions for chats

        :param chat_policy: The chat_policy of this MediaPolicies.
        :type: ChatMediaPolicy
        """
        
        self._chat_policy = chat_policy

    @property
    def email_policy(self):
        """
        Gets the email_policy of this MediaPolicies.
        Conditions and actions for emails

        :return: The email_policy of this MediaPolicies.
        :rtype: EmailMediaPolicy
        """
        return self._email_policy

    @email_policy.setter
    def email_policy(self, email_policy):
        """
        Sets the email_policy of this MediaPolicies.
        Conditions and actions for emails

        :param email_policy: The email_policy of this MediaPolicies.
        :type: EmailMediaPolicy
        """
        
        self._email_policy = email_policy

    @property
    def message_policy(self):
        """
        Gets the message_policy of this MediaPolicies.
        Conditions and actions for messages

        :return: The message_policy of this MediaPolicies.
        :rtype: MessageMediaPolicy
        """
        return self._message_policy

    @message_policy.setter
    def message_policy(self, message_policy):
        """
        Sets the message_policy of this MediaPolicies.
        Conditions and actions for messages

        :param message_policy: The message_policy of this MediaPolicies.
        :type: MessageMediaPolicy
        """
        
        self._message_policy = message_policy

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

