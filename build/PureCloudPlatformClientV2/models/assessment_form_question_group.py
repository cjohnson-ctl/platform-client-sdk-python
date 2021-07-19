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

class AssessmentFormQuestionGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AssessmentFormQuestionGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'default_answers_to_highest': 'bool',
            'default_answers_to_na': 'bool',
            'na_enabled': 'bool',
            'weight': 'float',
            'manual_weight': 'bool',
            'questions': 'list[AssessmentFormQuestion]',
            'visibility_condition': 'VisibilityCondition',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'default_answers_to_highest': 'defaultAnswersToHighest',
            'default_answers_to_na': 'defaultAnswersToNA',
            'na_enabled': 'naEnabled',
            'weight': 'weight',
            'manual_weight': 'manualWeight',
            'questions': 'questions',
            'visibility_condition': 'visibilityCondition',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._type = None
        self._default_answers_to_highest = None
        self._default_answers_to_na = None
        self._na_enabled = None
        self._weight = None
        self._manual_weight = None
        self._questions = None
        self._visibility_condition = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this AssessmentFormQuestionGroup.
        The ID of the question group,

        :return: The id of this AssessmentFormQuestionGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssessmentFormQuestionGroup.
        The ID of the question group,

        :param id: The id of this AssessmentFormQuestionGroup.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AssessmentFormQuestionGroup.
        The question group name

        :return: The name of this AssessmentFormQuestionGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssessmentFormQuestionGroup.
        The question group name

        :param name: The name of this AssessmentFormQuestionGroup.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this AssessmentFormQuestionGroup.
        The question group type

        :return: The type of this AssessmentFormQuestionGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AssessmentFormQuestionGroup.
        The question group type

        :param type: The type of this AssessmentFormQuestionGroup.
        :type: str
        """
        
        self._type = type

    @property
    def default_answers_to_highest(self):
        """
        Gets the default_answers_to_highest of this AssessmentFormQuestionGroup.


        :return: The default_answers_to_highest of this AssessmentFormQuestionGroup.
        :rtype: bool
        """
        return self._default_answers_to_highest

    @default_answers_to_highest.setter
    def default_answers_to_highest(self, default_answers_to_highest):
        """
        Sets the default_answers_to_highest of this AssessmentFormQuestionGroup.


        :param default_answers_to_highest: The default_answers_to_highest of this AssessmentFormQuestionGroup.
        :type: bool
        """
        
        self._default_answers_to_highest = default_answers_to_highest

    @property
    def default_answers_to_na(self):
        """
        Gets the default_answers_to_na of this AssessmentFormQuestionGroup.


        :return: The default_answers_to_na of this AssessmentFormQuestionGroup.
        :rtype: bool
        """
        return self._default_answers_to_na

    @default_answers_to_na.setter
    def default_answers_to_na(self, default_answers_to_na):
        """
        Sets the default_answers_to_na of this AssessmentFormQuestionGroup.


        :param default_answers_to_na: The default_answers_to_na of this AssessmentFormQuestionGroup.
        :type: bool
        """
        
        self._default_answers_to_na = default_answers_to_na

    @property
    def na_enabled(self):
        """
        Gets the na_enabled of this AssessmentFormQuestionGroup.


        :return: The na_enabled of this AssessmentFormQuestionGroup.
        :rtype: bool
        """
        return self._na_enabled

    @na_enabled.setter
    def na_enabled(self, na_enabled):
        """
        Sets the na_enabled of this AssessmentFormQuestionGroup.


        :param na_enabled: The na_enabled of this AssessmentFormQuestionGroup.
        :type: bool
        """
        
        self._na_enabled = na_enabled

    @property
    def weight(self):
        """
        Gets the weight of this AssessmentFormQuestionGroup.


        :return: The weight of this AssessmentFormQuestionGroup.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this AssessmentFormQuestionGroup.


        :param weight: The weight of this AssessmentFormQuestionGroup.
        :type: float
        """
        
        self._weight = weight

    @property
    def manual_weight(self):
        """
        Gets the manual_weight of this AssessmentFormQuestionGroup.


        :return: The manual_weight of this AssessmentFormQuestionGroup.
        :rtype: bool
        """
        return self._manual_weight

    @manual_weight.setter
    def manual_weight(self, manual_weight):
        """
        Sets the manual_weight of this AssessmentFormQuestionGroup.


        :param manual_weight: The manual_weight of this AssessmentFormQuestionGroup.
        :type: bool
        """
        
        self._manual_weight = manual_weight

    @property
    def questions(self):
        """
        Gets the questions of this AssessmentFormQuestionGroup.
        The list of questions for this question group

        :return: The questions of this AssessmentFormQuestionGroup.
        :rtype: list[AssessmentFormQuestion]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """
        Sets the questions of this AssessmentFormQuestionGroup.
        The list of questions for this question group

        :param questions: The questions of this AssessmentFormQuestionGroup.
        :type: list[AssessmentFormQuestion]
        """
        
        self._questions = questions

    @property
    def visibility_condition(self):
        """
        Gets the visibility_condition of this AssessmentFormQuestionGroup.


        :return: The visibility_condition of this AssessmentFormQuestionGroup.
        :rtype: VisibilityCondition
        """
        return self._visibility_condition

    @visibility_condition.setter
    def visibility_condition(self, visibility_condition):
        """
        Sets the visibility_condition of this AssessmentFormQuestionGroup.


        :param visibility_condition: The visibility_condition of this AssessmentFormQuestionGroup.
        :type: VisibilityCondition
        """
        
        self._visibility_condition = visibility_condition

    @property
    def self_uri(self):
        """
        Gets the self_uri of this AssessmentFormQuestionGroup.
        The URI for this object

        :return: The self_uri of this AssessmentFormQuestionGroup.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this AssessmentFormQuestionGroup.
        The URI for this object

        :param self_uri: The self_uri of this AssessmentFormQuestionGroup.
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
