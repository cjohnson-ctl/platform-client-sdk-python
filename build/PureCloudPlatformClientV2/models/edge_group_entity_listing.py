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

class EdgeGroupEntityListing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeGroupEntityListing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities': 'list[EdgeGroup]',
            'page_size': 'int',
            'page_number': 'int',
            'total': 'int',
            'first_uri': 'str',
            'previous_uri': 'str',
            'self_uri': 'str',
            'next_uri': 'str',
            'last_uri': 'str',
            'page_count': 'int'
        }

        self.attribute_map = {
            'entities': 'entities',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'total': 'total',
            'first_uri': 'firstUri',
            'previous_uri': 'previousUri',
            'self_uri': 'selfUri',
            'next_uri': 'nextUri',
            'last_uri': 'lastUri',
            'page_count': 'pageCount'
        }

        self._entities = None
        self._page_size = None
        self._page_number = None
        self._total = None
        self._first_uri = None
        self._previous_uri = None
        self._self_uri = None
        self._next_uri = None
        self._last_uri = None
        self._page_count = None

    @property
    def entities(self):
        """
        Gets the entities of this EdgeGroupEntityListing.


        :return: The entities of this EdgeGroupEntityListing.
        :rtype: list[EdgeGroup]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this EdgeGroupEntityListing.


        :param entities: The entities of this EdgeGroupEntityListing.
        :type: list[EdgeGroup]
        """
        
        self._entities = entities

    @property
    def page_size(self):
        """
        Gets the page_size of this EdgeGroupEntityListing.


        :return: The page_size of this EdgeGroupEntityListing.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this EdgeGroupEntityListing.


        :param page_size: The page_size of this EdgeGroupEntityListing.
        :type: int
        """
        
        self._page_size = page_size

    @property
    def page_number(self):
        """
        Gets the page_number of this EdgeGroupEntityListing.


        :return: The page_number of this EdgeGroupEntityListing.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this EdgeGroupEntityListing.


        :param page_number: The page_number of this EdgeGroupEntityListing.
        :type: int
        """
        
        self._page_number = page_number

    @property
    def total(self):
        """
        Gets the total of this EdgeGroupEntityListing.


        :return: The total of this EdgeGroupEntityListing.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this EdgeGroupEntityListing.


        :param total: The total of this EdgeGroupEntityListing.
        :type: int
        """
        
        self._total = total

    @property
    def first_uri(self):
        """
        Gets the first_uri of this EdgeGroupEntityListing.


        :return: The first_uri of this EdgeGroupEntityListing.
        :rtype: str
        """
        return self._first_uri

    @first_uri.setter
    def first_uri(self, first_uri):
        """
        Sets the first_uri of this EdgeGroupEntityListing.


        :param first_uri: The first_uri of this EdgeGroupEntityListing.
        :type: str
        """
        
        self._first_uri = first_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this EdgeGroupEntityListing.


        :return: The previous_uri of this EdgeGroupEntityListing.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this EdgeGroupEntityListing.


        :param previous_uri: The previous_uri of this EdgeGroupEntityListing.
        :type: str
        """
        
        self._previous_uri = previous_uri

    @property
    def self_uri(self):
        """
        Gets the self_uri of this EdgeGroupEntityListing.


        :return: The self_uri of this EdgeGroupEntityListing.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this EdgeGroupEntityListing.


        :param self_uri: The self_uri of this EdgeGroupEntityListing.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def next_uri(self):
        """
        Gets the next_uri of this EdgeGroupEntityListing.


        :return: The next_uri of this EdgeGroupEntityListing.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this EdgeGroupEntityListing.


        :param next_uri: The next_uri of this EdgeGroupEntityListing.
        :type: str
        """
        
        self._next_uri = next_uri

    @property
    def last_uri(self):
        """
        Gets the last_uri of this EdgeGroupEntityListing.


        :return: The last_uri of this EdgeGroupEntityListing.
        :rtype: str
        """
        return self._last_uri

    @last_uri.setter
    def last_uri(self, last_uri):
        """
        Sets the last_uri of this EdgeGroupEntityListing.


        :param last_uri: The last_uri of this EdgeGroupEntityListing.
        :type: str
        """
        
        self._last_uri = last_uri

    @property
    def page_count(self):
        """
        Gets the page_count of this EdgeGroupEntityListing.


        :return: The page_count of this EdgeGroupEntityListing.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this EdgeGroupEntityListing.


        :param page_count: The page_count of this EdgeGroupEntityListing.
        :type: int
        """
        
        self._page_count = page_count

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

