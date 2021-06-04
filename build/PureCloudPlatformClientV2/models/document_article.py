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

class DocumentArticle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentArticle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str',
            'content': 'ArticleContent',
            'alternatives': 'list[str]'
        }

        self.attribute_map = {
            'title': 'title',
            'content': 'content',
            'alternatives': 'alternatives'
        }

        self._title = None
        self._content = None
        self._alternatives = None

    @property
    def title(self):
        """
        Gets the title of this DocumentArticle.
        The title of the Article.

        :return: The title of this DocumentArticle.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DocumentArticle.
        The title of the Article.

        :param title: The title of this DocumentArticle.
        :type: str
        """
        
        self._title = title

    @property
    def content(self):
        """
        Gets the content of this DocumentArticle.
        The content of the Article.

        :return: The content of this DocumentArticle.
        :rtype: ArticleContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this DocumentArticle.
        The content of the Article.

        :param content: The content of this DocumentArticle.
        :type: ArticleContent
        """
        
        self._content = content

    @property
    def alternatives(self):
        """
        Gets the alternatives of this DocumentArticle.
        List of Alternative questions related to the title which helps in improving the likelihood of a match to user query.

        :return: The alternatives of this DocumentArticle.
        :rtype: list[str]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives):
        """
        Sets the alternatives of this DocumentArticle.
        List of Alternative questions related to the title which helps in improving the likelihood of a match to user query.

        :param alternatives: The alternatives of this DocumentArticle.
        :type: list[str]
        """
        
        self._alternatives = alternatives

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

