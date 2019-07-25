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

class WebChatMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WebChatMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'conversation': 'WebChatConversation',
            'sender': 'WebChatMemberInfo',
            'body': 'str',
            'body_type': 'str',
            'timestamp': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'conversation': 'conversation',
            'sender': 'sender',
            'body': 'body',
            'body_type': 'bodyType',
            'timestamp': 'timestamp',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._conversation = None
        self._sender = None
        self._body = None
        self._body_type = None
        self._timestamp = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this WebChatMessage.
        The globally unique identifier for the object.

        :return: The id of this WebChatMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebChatMessage.
        The globally unique identifier for the object.

        :param id: The id of this WebChatMessage.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this WebChatMessage.


        :return: The name of this WebChatMessage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WebChatMessage.


        :param name: The name of this WebChatMessage.
        :type: str
        """
        
        self._name = name

    @property
    def conversation(self):
        """
        Gets the conversation of this WebChatMessage.
        The identifier of the conversation

        :return: The conversation of this WebChatMessage.
        :rtype: WebChatConversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this WebChatMessage.
        The identifier of the conversation

        :param conversation: The conversation of this WebChatMessage.
        :type: WebChatConversation
        """
        
        self._conversation = conversation

    @property
    def sender(self):
        """
        Gets the sender of this WebChatMessage.
        The member who sent the message

        :return: The sender of this WebChatMessage.
        :rtype: WebChatMemberInfo
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this WebChatMessage.
        The member who sent the message

        :param sender: The sender of this WebChatMessage.
        :type: WebChatMemberInfo
        """
        
        self._sender = sender

    @property
    def body(self):
        """
        Gets the body of this WebChatMessage.
        The message body.

        :return: The body of this WebChatMessage.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this WebChatMessage.
        The message body.

        :param body: The body of this WebChatMessage.
        :type: str
        """
        
        self._body = body

    @property
    def body_type(self):
        """
        Gets the body_type of this WebChatMessage.
        The purpose of the message within the conversation, such as a standard text entry versus a greeting.

        :return: The body_type of this WebChatMessage.
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """
        Sets the body_type of this WebChatMessage.
        The purpose of the message within the conversation, such as a standard text entry versus a greeting.

        :param body_type: The body_type of this WebChatMessage.
        :type: str
        """
        allowed_values = ["standard", "notice", "member-join", "member-leave", "media-request"]
        if body_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for body_type -> " + body_type
            self._body_type = "outdated_sdk_version"
        else:
            self._body_type = body_type

    @property
    def timestamp(self):
        """
        Gets the timestamp of this WebChatMessage.
        The timestamp of the message, in ISO-8601 format

        :return: The timestamp of this WebChatMessage.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WebChatMessage.
        The timestamp of the message, in ISO-8601 format

        :param timestamp: The timestamp of this WebChatMessage.
        :type: datetime
        """
        
        self._timestamp = timestamp

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WebChatMessage.
        The URI for this object

        :return: The self_uri of this WebChatMessage.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WebChatMessage.
        The URI for this object

        :param self_uri: The self_uri of this WebChatMessage.
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

