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


class WebChatMessageEntityList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WebChatMessageEntityList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'page_size': 'int',
            'entities': 'list[WebChatMessage]',
            'previous_page': 'str',
            'next': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'page_size': 'pageSize',
            'entities': 'entities',
            'previous_page': 'previousPage',
            'next': 'next',
            'self_uri': 'selfUri'
        }

        self._page_size = None
        self._entities = None
        self._previous_page = None
        self._next = None
        self._self_uri = None

    @property
    def page_size(self):
        """
        Gets the page_size of this WebChatMessageEntityList.


        :return: The page_size of this WebChatMessageEntityList.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this WebChatMessageEntityList.


        :param page_size: The page_size of this WebChatMessageEntityList.
        :type: int
        """
        
        self._page_size = page_size

    @property
    def entities(self):
        """
        Gets the entities of this WebChatMessageEntityList.


        :return: The entities of this WebChatMessageEntityList.
        :rtype: list[WebChatMessage]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this WebChatMessageEntityList.


        :param entities: The entities of this WebChatMessageEntityList.
        :type: list[WebChatMessage]
        """
        
        self._entities = entities

    @property
    def previous_page(self):
        """
        Gets the previous_page of this WebChatMessageEntityList.


        :return: The previous_page of this WebChatMessageEntityList.
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """
        Sets the previous_page of this WebChatMessageEntityList.


        :param previous_page: The previous_page of this WebChatMessageEntityList.
        :type: str
        """
        
        self._previous_page = previous_page

    @property
    def next(self):
        """
        Gets the next of this WebChatMessageEntityList.


        :return: The next of this WebChatMessageEntityList.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this WebChatMessageEntityList.


        :param next: The next of this WebChatMessageEntityList.
        :type: str
        """
        
        self._next = next

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WebChatMessageEntityList.


        :return: The self_uri of this WebChatMessageEntityList.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WebChatMessageEntityList.


        :param self_uri: The self_uri of this WebChatMessageEntityList.
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
