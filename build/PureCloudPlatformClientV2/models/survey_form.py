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


class SurveyForm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SurveyForm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'modified_date': 'datetime',
            'published': 'bool',
            'disabled': 'bool',
            'context_id': 'str',
            'header': 'str',
            'footer': 'str',
            'question_groups': 'list[QuestionGroup]',
            'published_versions': 'DomainEntityListingSurveyForm',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'modified_date': 'modifiedDate',
            'published': 'published',
            'disabled': 'disabled',
            'context_id': 'contextId',
            'header': 'header',
            'footer': 'footer',
            'question_groups': 'questionGroups',
            'published_versions': 'publishedVersions',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._modified_date = None
        self._published = None
        self._disabled = None
        self._context_id = None
        self._header = None
        self._footer = None
        self._question_groups = None
        self._published_versions = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this SurveyForm.
        The globally unique identifier for the object.

        :return: The id of this SurveyForm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SurveyForm.
        The globally unique identifier for the object.

        :param id: The id of this SurveyForm.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SurveyForm.
        The survey form name

        :return: The name of this SurveyForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SurveyForm.
        The survey form name

        :param name: The name of this SurveyForm.
        :type: str
        """
        
        self._name = name

    @property
    def modified_date(self):
        """
        Gets the modified_date of this SurveyForm.
        Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The modified_date of this SurveyForm.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this SurveyForm.
        Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param modified_date: The modified_date of this SurveyForm.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def published(self):
        """
        Gets the published of this SurveyForm.
        Is this form published

        :return: The published of this SurveyForm.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this SurveyForm.
        Is this form published

        :param published: The published of this SurveyForm.
        :type: bool
        """
        
        self._published = published

    @property
    def disabled(self):
        """
        Gets the disabled of this SurveyForm.
        Is this form disabled

        :return: The disabled of this SurveyForm.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this SurveyForm.
        Is this form disabled

        :param disabled: The disabled of this SurveyForm.
        :type: bool
        """
        
        self._disabled = disabled

    @property
    def context_id(self):
        """
        Gets the context_id of this SurveyForm.
        Unique Id for all versions of this form

        :return: The context_id of this SurveyForm.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this SurveyForm.
        Unique Id for all versions of this form

        :param context_id: The context_id of this SurveyForm.
        :type: str
        """
        
        self._context_id = context_id

    @property
    def header(self):
        """
        Gets the header of this SurveyForm.
        Id of the header image appearing at the top of the form.

        :return: The header of this SurveyForm.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this SurveyForm.
        Id of the header image appearing at the top of the form.

        :param header: The header of this SurveyForm.
        :type: str
        """
        
        self._header = header

    @property
    def footer(self):
        """
        Gets the footer of this SurveyForm.
        Markdown text for the bottom of the form.

        :return: The footer of this SurveyForm.
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """
        Sets the footer of this SurveyForm.
        Markdown text for the bottom of the form.

        :param footer: The footer of this SurveyForm.
        :type: str
        """
        
        self._footer = footer

    @property
    def question_groups(self):
        """
        Gets the question_groups of this SurveyForm.
        A list of question groups

        :return: The question_groups of this SurveyForm.
        :rtype: list[QuestionGroup]
        """
        return self._question_groups

    @question_groups.setter
    def question_groups(self, question_groups):
        """
        Sets the question_groups of this SurveyForm.
        A list of question groups

        :param question_groups: The question_groups of this SurveyForm.
        :type: list[QuestionGroup]
        """
        
        self._question_groups = question_groups

    @property
    def published_versions(self):
        """
        Gets the published_versions of this SurveyForm.
        List of published version of this form

        :return: The published_versions of this SurveyForm.
        :rtype: DomainEntityListingSurveyForm
        """
        return self._published_versions

    @published_versions.setter
    def published_versions(self, published_versions):
        """
        Sets the published_versions of this SurveyForm.
        List of published version of this form

        :param published_versions: The published_versions of this SurveyForm.
        :type: DomainEntityListingSurveyForm
        """
        
        self._published_versions = published_versions

    @property
    def self_uri(self):
        """
        Gets the self_uri of this SurveyForm.
        The URI for this object

        :return: The self_uri of this SurveyForm.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this SurveyForm.
        The URI for this object

        :param self_uri: The self_uri of this SurveyForm.
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

