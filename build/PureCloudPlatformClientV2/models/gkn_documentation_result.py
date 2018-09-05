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


class GKNDocumentationResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GKNDocumentationResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'str',
            'link': 'str',
            'title': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'link': 'link',
            'title': 'title',
            'type': '_type'
        }

        self._content = None
        self._link = None
        self._title = None
        self._type = None

    @property
    def content(self):
        """
        Gets the content of this GKNDocumentationResult.
        The text or html content for the documentation entity. Will be returned in responses for certain entities.

        :return: The content of this GKNDocumentationResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this GKNDocumentationResult.
        The text or html content for the documentation entity. Will be returned in responses for certain entities.

        :param content: The content of this GKNDocumentationResult.
        :type: str
        """
        
        self._content = content

    @property
    def link(self):
        """
        Gets the link of this GKNDocumentationResult.
        URL link for the documentation entity. Will be returned in responses for certain entities.

        :return: The link of this GKNDocumentationResult.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this GKNDocumentationResult.
        URL link for the documentation entity. Will be returned in responses for certain entities.

        :param link: The link of this GKNDocumentationResult.
        :type: str
        """
        
        self._link = link

    @property
    def title(self):
        """
        Gets the title of this GKNDocumentationResult.
        The title of the documentation entity. Will be returned in responses for certain entities.

        :return: The title of this GKNDocumentationResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this GKNDocumentationResult.
        The title of the documentation entity. Will be returned in responses for certain entities.

        :param title: The title of this GKNDocumentationResult.
        :type: str
        """
        
        self._title = title

    @property
    def type(self):
        """
        Gets the type of this GKNDocumentationResult.
        The search type. Will be returned in responses for certain entities.

        :return: The type of this GKNDocumentationResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GKNDocumentationResult.
        The search type. Will be returned in responses for certain entities.

        :param type: The type of this GKNDocumentationResult.
        :type: str
        """
        
        self._type = type

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

