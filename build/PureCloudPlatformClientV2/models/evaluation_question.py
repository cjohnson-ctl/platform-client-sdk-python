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

class EvaluationQuestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EvaluationQuestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'text': 'str',
            'help_text': 'str',
            'type': 'str',
            'na_enabled': 'bool',
            'comments_required': 'bool',
            'visibility_condition': 'VisibilityCondition',
            'answer_options': 'list[AnswerOption]',
            'is_critical': 'bool',
            'is_kill': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'help_text': 'helpText',
            'type': 'type',
            'na_enabled': 'naEnabled',
            'comments_required': 'commentsRequired',
            'visibility_condition': 'visibilityCondition',
            'answer_options': 'answerOptions',
            'is_critical': 'isCritical',
            'is_kill': 'isKill'
        }

        self._id = None
        self._text = None
        self._help_text = None
        self._type = None
        self._na_enabled = None
        self._comments_required = None
        self._visibility_condition = None
        self._answer_options = None
        self._is_critical = None
        self._is_kill = None

    @property
    def id(self):
        """
        Gets the id of this EvaluationQuestion.


        :return: The id of this EvaluationQuestion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EvaluationQuestion.


        :param id: The id of this EvaluationQuestion.
        :type: str
        """
        
        self._id = id

    @property
    def text(self):
        """
        Gets the text of this EvaluationQuestion.


        :return: The text of this EvaluationQuestion.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this EvaluationQuestion.


        :param text: The text of this EvaluationQuestion.
        :type: str
        """
        
        self._text = text

    @property
    def help_text(self):
        """
        Gets the help_text of this EvaluationQuestion.


        :return: The help_text of this EvaluationQuestion.
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """
        Sets the help_text of this EvaluationQuestion.


        :param help_text: The help_text of this EvaluationQuestion.
        :type: str
        """
        
        self._help_text = help_text

    @property
    def type(self):
        """
        Gets the type of this EvaluationQuestion.


        :return: The type of this EvaluationQuestion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EvaluationQuestion.


        :param type: The type of this EvaluationQuestion.
        :type: str
        """
        allowed_values = ["multipleChoiceQuestion", "freeTextQuestion", "npsQuestion", "readOnlyTextBlockQuestion"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def na_enabled(self):
        """
        Gets the na_enabled of this EvaluationQuestion.


        :return: The na_enabled of this EvaluationQuestion.
        :rtype: bool
        """
        return self._na_enabled

    @na_enabled.setter
    def na_enabled(self, na_enabled):
        """
        Sets the na_enabled of this EvaluationQuestion.


        :param na_enabled: The na_enabled of this EvaluationQuestion.
        :type: bool
        """
        
        self._na_enabled = na_enabled

    @property
    def comments_required(self):
        """
        Gets the comments_required of this EvaluationQuestion.


        :return: The comments_required of this EvaluationQuestion.
        :rtype: bool
        """
        return self._comments_required

    @comments_required.setter
    def comments_required(self, comments_required):
        """
        Sets the comments_required of this EvaluationQuestion.


        :param comments_required: The comments_required of this EvaluationQuestion.
        :type: bool
        """
        
        self._comments_required = comments_required

    @property
    def visibility_condition(self):
        """
        Gets the visibility_condition of this EvaluationQuestion.


        :return: The visibility_condition of this EvaluationQuestion.
        :rtype: VisibilityCondition
        """
        return self._visibility_condition

    @visibility_condition.setter
    def visibility_condition(self, visibility_condition):
        """
        Sets the visibility_condition of this EvaluationQuestion.


        :param visibility_condition: The visibility_condition of this EvaluationQuestion.
        :type: VisibilityCondition
        """
        
        self._visibility_condition = visibility_condition

    @property
    def answer_options(self):
        """
        Gets the answer_options of this EvaluationQuestion.
        Options from which to choose an answer for this question. Only used by Multiple Choice type questions.

        :return: The answer_options of this EvaluationQuestion.
        :rtype: list[AnswerOption]
        """
        return self._answer_options

    @answer_options.setter
    def answer_options(self, answer_options):
        """
        Sets the answer_options of this EvaluationQuestion.
        Options from which to choose an answer for this question. Only used by Multiple Choice type questions.

        :param answer_options: The answer_options of this EvaluationQuestion.
        :type: list[AnswerOption]
        """
        
        self._answer_options = answer_options

    @property
    def is_critical(self):
        """
        Gets the is_critical of this EvaluationQuestion.


        :return: The is_critical of this EvaluationQuestion.
        :rtype: bool
        """
        return self._is_critical

    @is_critical.setter
    def is_critical(self, is_critical):
        """
        Sets the is_critical of this EvaluationQuestion.


        :param is_critical: The is_critical of this EvaluationQuestion.
        :type: bool
        """
        
        self._is_critical = is_critical

    @property
    def is_kill(self):
        """
        Gets the is_kill of this EvaluationQuestion.


        :return: The is_kill of this EvaluationQuestion.
        :rtype: bool
        """
        return self._is_kill

    @is_kill.setter
    def is_kill(self, is_kill):
        """
        Sets the is_kill of this EvaluationQuestion.


        :param is_kill: The is_kill of this EvaluationQuestion.
        :type: bool
        """
        
        self._is_kill = is_kill

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

