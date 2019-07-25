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

class QueueConversationVideoEventTopicAttachment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationVideoEventTopicAttachment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_id': 'str',
            'name': 'str',
            'content_uri': 'str',
            'content_type': 'str',
            'content_length': 'int',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'attachment_id': 'attachmentId',
            'name': 'name',
            'content_uri': 'contentUri',
            'content_type': 'contentType',
            'content_length': 'contentLength',
            'additional_properties': 'additionalProperties'
        }

        self._attachment_id = None
        self._name = None
        self._content_uri = None
        self._content_type = None
        self._content_length = None
        self._additional_properties = None

    @property
    def attachment_id(self):
        """
        Gets the attachment_id of this QueueConversationVideoEventTopicAttachment.


        :return: The attachment_id of this QueueConversationVideoEventTopicAttachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """
        Sets the attachment_id of this QueueConversationVideoEventTopicAttachment.


        :param attachment_id: The attachment_id of this QueueConversationVideoEventTopicAttachment.
        :type: str
        """
        
        self._attachment_id = attachment_id

    @property
    def name(self):
        """
        Gets the name of this QueueConversationVideoEventTopicAttachment.


        :return: The name of this QueueConversationVideoEventTopicAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QueueConversationVideoEventTopicAttachment.


        :param name: The name of this QueueConversationVideoEventTopicAttachment.
        :type: str
        """
        
        self._name = name

    @property
    def content_uri(self):
        """
        Gets the content_uri of this QueueConversationVideoEventTopicAttachment.


        :return: The content_uri of this QueueConversationVideoEventTopicAttachment.
        :rtype: str
        """
        return self._content_uri

    @content_uri.setter
    def content_uri(self, content_uri):
        """
        Sets the content_uri of this QueueConversationVideoEventTopicAttachment.


        :param content_uri: The content_uri of this QueueConversationVideoEventTopicAttachment.
        :type: str
        """
        
        self._content_uri = content_uri

    @property
    def content_type(self):
        """
        Gets the content_type of this QueueConversationVideoEventTopicAttachment.


        :return: The content_type of this QueueConversationVideoEventTopicAttachment.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this QueueConversationVideoEventTopicAttachment.


        :param content_type: The content_type of this QueueConversationVideoEventTopicAttachment.
        :type: str
        """
        
        self._content_type = content_type

    @property
    def content_length(self):
        """
        Gets the content_length of this QueueConversationVideoEventTopicAttachment.


        :return: The content_length of this QueueConversationVideoEventTopicAttachment.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """
        Sets the content_length of this QueueConversationVideoEventTopicAttachment.


        :param content_length: The content_length of this QueueConversationVideoEventTopicAttachment.
        :type: int
        """
        
        self._content_length = content_length

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationVideoEventTopicAttachment.


        :return: The additional_properties of this QueueConversationVideoEventTopicAttachment.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationVideoEventTopicAttachment.


        :param additional_properties: The additional_properties of this QueueConversationVideoEventTopicAttachment.
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

