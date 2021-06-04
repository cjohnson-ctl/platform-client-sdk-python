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

class KnowledgeSearchDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        KnowledgeSearchDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'language_code': 'str',
            'type': 'str',
            'faq': 'DocumentFaq',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'categories': 'list[KnowledgeCategory]',
            'knowledge_base': 'KnowledgeBase',
            'external_url': 'str',
            'article': 'DocumentArticle',
            'confidence': 'float',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'language_code': 'languageCode',
            'type': 'type',
            'faq': 'faq',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'categories': 'categories',
            'knowledge_base': 'knowledgeBase',
            'external_url': 'externalUrl',
            'article': 'article',
            'confidence': 'confidence',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._language_code = None
        self._type = None
        self._faq = None
        self._date_created = None
        self._date_modified = None
        self._categories = None
        self._knowledge_base = None
        self._external_url = None
        self._article = None
        self._confidence = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this KnowledgeSearchDocument.
        The globally unique identifier for the object.

        :return: The id of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KnowledgeSearchDocument.
        The globally unique identifier for the object.

        :param id: The id of this KnowledgeSearchDocument.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this KnowledgeSearchDocument.


        :return: The name of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this KnowledgeSearchDocument.


        :param name: The name of this KnowledgeSearchDocument.
        :type: str
        """
        
        self._name = name

    @property
    def language_code(self):
        """
        Gets the language_code of this KnowledgeSearchDocument.
        Language of the document

        :return: The language_code of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this KnowledgeSearchDocument.
        Language of the document

        :param language_code: The language_code of this KnowledgeSearchDocument.
        :type: str
        """
        allowed_values = ["en-US", "de-DE"]
        if language_code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language_code -> " + language_code)
            self._language_code = "outdated_sdk_version"
        else:
            self._language_code = language_code

    @property
    def type(self):
        """
        Gets the type of this KnowledgeSearchDocument.
        Document type

        :return: The type of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this KnowledgeSearchDocument.
        Document type

        :param type: The type of this KnowledgeSearchDocument.
        :type: str
        """
        allowed_values = ["Faq", "Article"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def faq(self):
        """
        Gets the faq of this KnowledgeSearchDocument.
        FAQ document details

        :return: The faq of this KnowledgeSearchDocument.
        :rtype: DocumentFaq
        """
        return self._faq

    @faq.setter
    def faq(self, faq):
        """
        Sets the faq of this KnowledgeSearchDocument.
        FAQ document details

        :param faq: The faq of this KnowledgeSearchDocument.
        :type: DocumentFaq
        """
        
        self._faq = faq

    @property
    def date_created(self):
        """
        Gets the date_created of this KnowledgeSearchDocument.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this KnowledgeSearchDocument.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this KnowledgeSearchDocument.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this KnowledgeSearchDocument.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this KnowledgeSearchDocument.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this KnowledgeSearchDocument.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this KnowledgeSearchDocument.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this KnowledgeSearchDocument.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def categories(self):
        """
        Gets the categories of this KnowledgeSearchDocument.
        Document categories

        :return: The categories of this KnowledgeSearchDocument.
        :rtype: list[KnowledgeCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this KnowledgeSearchDocument.
        Document categories

        :param categories: The categories of this KnowledgeSearchDocument.
        :type: list[KnowledgeCategory]
        """
        
        self._categories = categories

    @property
    def knowledge_base(self):
        """
        Gets the knowledge_base of this KnowledgeSearchDocument.
        Knowledge base which document does belong to

        :return: The knowledge_base of this KnowledgeSearchDocument.
        :rtype: KnowledgeBase
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base):
        """
        Sets the knowledge_base of this KnowledgeSearchDocument.
        Knowledge base which document does belong to

        :param knowledge_base: The knowledge_base of this KnowledgeSearchDocument.
        :type: KnowledgeBase
        """
        
        self._knowledge_base = knowledge_base

    @property
    def external_url(self):
        """
        Gets the external_url of this KnowledgeSearchDocument.
        External URL to the document

        :return: The external_url of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """
        Sets the external_url of this KnowledgeSearchDocument.
        External URL to the document

        :param external_url: The external_url of this KnowledgeSearchDocument.
        :type: str
        """
        
        self._external_url = external_url

    @property
    def article(self):
        """
        Gets the article of this KnowledgeSearchDocument.
        Article

        :return: The article of this KnowledgeSearchDocument.
        :rtype: DocumentArticle
        """
        return self._article

    @article.setter
    def article(self, article):
        """
        Sets the article of this KnowledgeSearchDocument.
        Article

        :param article: The article of this KnowledgeSearchDocument.
        :type: DocumentArticle
        """
        
        self._article = article

    @property
    def confidence(self):
        """
        Gets the confidence of this KnowledgeSearchDocument.
        The confidence associated with a document with respect to a search query

        :return: The confidence of this KnowledgeSearchDocument.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this KnowledgeSearchDocument.
        The confidence associated with a document with respect to a search query

        :param confidence: The confidence of this KnowledgeSearchDocument.
        :type: float
        """
        
        self._confidence = confidence

    @property
    def self_uri(self):
        """
        Gets the self_uri of this KnowledgeSearchDocument.
        The URI for this object

        :return: The self_uri of this KnowledgeSearchDocument.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this KnowledgeSearchDocument.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeSearchDocument.
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

