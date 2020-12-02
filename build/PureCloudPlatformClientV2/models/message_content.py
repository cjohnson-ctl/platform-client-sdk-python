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

class MessageContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_type': 'str',
            'location': 'ContentLocation',
            'attachment': 'ContentAttachment',
            'quick_reply': 'ContentQuickReply',
            'generic': 'ContentGeneric',
            'list': 'ContentList',
            'template': 'ContentNotificationTemplate',
            'reactions': 'list[ContentReaction]',
            'mention': 'MessagingRecipient',
            'postback': 'ContentPostback'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'location': 'location',
            'attachment': 'attachment',
            'quick_reply': 'quickReply',
            'generic': 'generic',
            'list': 'list',
            'template': 'template',
            'reactions': 'reactions',
            'mention': 'mention',
            'postback': 'postback'
        }

        self._content_type = None
        self._location = None
        self._attachment = None
        self._quick_reply = None
        self._generic = None
        self._list = None
        self._template = None
        self._reactions = None
        self._mention = None
        self._postback = None

    @property
    def content_type(self):
        """
        Gets the content_type of this MessageContent.
        Type of this content element. If contentType = \"Attachment\" only one item is allowed.

        :return: The content_type of this MessageContent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this MessageContent.
        Type of this content element. If contentType = \"Attachment\" only one item is allowed.

        :param content_type: The content_type of this MessageContent.
        :type: str
        """
        allowed_values = ["Attachment", "Location", "QuickReply", "Notification", "GenericTemplate", "ListTemplate", "Postback", "Reactions", "Mention"]
        if content_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for content_type -> " + content_type)
            self._content_type = "outdated_sdk_version"
        else:
            self._content_type = content_type

    @property
    def location(self):
        """
        Gets the location of this MessageContent.
        Location object

        :return: The location of this MessageContent.
        :rtype: ContentLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this MessageContent.
        Location object

        :param location: The location of this MessageContent.
        :type: ContentLocation
        """
        
        self._location = location

    @property
    def attachment(self):
        """
        Gets the attachment of this MessageContent.
        Attachment object

        :return: The attachment of this MessageContent.
        :rtype: ContentAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """
        Sets the attachment of this MessageContent.
        Attachment object

        :param attachment: The attachment of this MessageContent.
        :type: ContentAttachment
        """
        
        self._attachment = attachment

    @property
    def quick_reply(self):
        """
        Gets the quick_reply of this MessageContent.
        Quick reply object

        :return: The quick_reply of this MessageContent.
        :rtype: ContentQuickReply
        """
        return self._quick_reply

    @quick_reply.setter
    def quick_reply(self, quick_reply):
        """
        Sets the quick_reply of this MessageContent.
        Quick reply object

        :param quick_reply: The quick_reply of this MessageContent.
        :type: ContentQuickReply
        """
        
        self._quick_reply = quick_reply

    @property
    def generic(self):
        """
        Gets the generic of this MessageContent.
        Generic content object

        :return: The generic of this MessageContent.
        :rtype: ContentGeneric
        """
        return self._generic

    @generic.setter
    def generic(self, generic):
        """
        Sets the generic of this MessageContent.
        Generic content object

        :param generic: The generic of this MessageContent.
        :type: ContentGeneric
        """
        
        self._generic = generic

    @property
    def list(self):
        """
        Gets the list of this MessageContent.
        List content object

        :return: The list of this MessageContent.
        :rtype: ContentList
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this MessageContent.
        List content object

        :param list: The list of this MessageContent.
        :type: ContentList
        """
        
        self._list = list

    @property
    def template(self):
        """
        Gets the template of this MessageContent.
        Template notification object

        :return: The template of this MessageContent.
        :rtype: ContentNotificationTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this MessageContent.
        Template notification object

        :param template: The template of this MessageContent.
        :type: ContentNotificationTemplate
        """
        
        self._template = template

    @property
    def reactions(self):
        """
        Gets the reactions of this MessageContent.
        A list of reactions

        :return: The reactions of this MessageContent.
        :rtype: list[ContentReaction]
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions):
        """
        Sets the reactions of this MessageContent.
        A list of reactions

        :param reactions: The reactions of this MessageContent.
        :type: list[ContentReaction]
        """
        
        self._reactions = reactions

    @property
    def mention(self):
        """
        Gets the mention of this MessageContent.
        This is used to identify who the message is sent to, as well as who it was sent from. This information is channel specific - depends on capabilities to describe party by the platform

        :return: The mention of this MessageContent.
        :rtype: MessagingRecipient
        """
        return self._mention

    @mention.setter
    def mention(self, mention):
        """
        Sets the mention of this MessageContent.
        This is used to identify who the message is sent to, as well as who it was sent from. This information is channel specific - depends on capabilities to describe party by the platform

        :param mention: The mention of this MessageContent.
        :type: MessagingRecipient
        """
        
        self._mention = mention

    @property
    def postback(self):
        """
        Gets the postback of this MessageContent.
        The postback object result of a user clicking in a button

        :return: The postback of this MessageContent.
        :rtype: ContentPostback
        """
        return self._postback

    @postback.setter
    def postback(self, postback):
        """
        Sets the postback of this MessageContent.
        The postback object result of a user clicking in a button

        :param postback: The postback of this MessageContent.
        :type: ContentPostback
        """
        
        self._postback = postback

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

