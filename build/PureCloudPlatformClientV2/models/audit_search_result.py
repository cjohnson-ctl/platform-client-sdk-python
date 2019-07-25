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

class AuditSearchResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuditSearchResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'page_number': 'int',
            'page_size': 'int',
            'total': 'int',
            'page_count': 'int',
            'facet_info': 'list[FacetInfo]',
            'audit_messages': 'list[AuditMessage]'
        }

        self.attribute_map = {
            'page_number': 'pageNumber',
            'page_size': 'pageSize',
            'total': 'total',
            'page_count': 'pageCount',
            'facet_info': 'facetInfo',
            'audit_messages': 'auditMessages'
        }

        self._page_number = None
        self._page_size = None
        self._total = None
        self._page_count = None
        self._facet_info = None
        self._audit_messages = None

    @property
    def page_number(self):
        """
        Gets the page_number of this AuditSearchResult.
        Which page was returned.

        :return: The page_number of this AuditSearchResult.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this AuditSearchResult.
        Which page was returned.

        :param page_number: The page_number of this AuditSearchResult.
        :type: int
        """
        
        self._page_number = page_number

    @property
    def page_size(self):
        """
        Gets the page_size of this AuditSearchResult.
        The number of results in a page.

        :return: The page_size of this AuditSearchResult.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this AuditSearchResult.
        The number of results in a page.

        :param page_size: The page_size of this AuditSearchResult.
        :type: int
        """
        
        self._page_size = page_size

    @property
    def total(self):
        """
        Gets the total of this AuditSearchResult.
        The total number of results.

        :return: The total of this AuditSearchResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this AuditSearchResult.
        The total number of results.

        :param total: The total of this AuditSearchResult.
        :type: int
        """
        
        self._total = total

    @property
    def page_count(self):
        """
        Gets the page_count of this AuditSearchResult.
        The number of pages of results.

        :return: The page_count of this AuditSearchResult.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this AuditSearchResult.
        The number of pages of results.

        :param page_count: The page_count of this AuditSearchResult.
        :type: int
        """
        
        self._page_count = page_count

    @property
    def facet_info(self):
        """
        Gets the facet_info of this AuditSearchResult.


        :return: The facet_info of this AuditSearchResult.
        :rtype: list[FacetInfo]
        """
        return self._facet_info

    @facet_info.setter
    def facet_info(self, facet_info):
        """
        Sets the facet_info of this AuditSearchResult.


        :param facet_info: The facet_info of this AuditSearchResult.
        :type: list[FacetInfo]
        """
        
        self._facet_info = facet_info

    @property
    def audit_messages(self):
        """
        Gets the audit_messages of this AuditSearchResult.


        :return: The audit_messages of this AuditSearchResult.
        :rtype: list[AuditMessage]
        """
        return self._audit_messages

    @audit_messages.setter
    def audit_messages(self, audit_messages):
        """
        Sets the audit_messages of this AuditSearchResult.


        :param audit_messages: The audit_messages of this AuditSearchResult.
        :type: list[AuditMessage]
        """
        
        self._audit_messages = audit_messages

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

