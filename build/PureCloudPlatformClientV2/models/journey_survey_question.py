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


class JourneySurveyQuestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JourneySurveyQuestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'label': 'str',
            'customer_property': 'str',
            'choices': 'list[str]',
            'is_mandatory': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'label': 'label',
            'customer_property': 'customerProperty',
            'choices': 'choices',
            'is_mandatory': 'isMandatory'
        }

        self._type = None
        self._label = None
        self._customer_property = None
        self._choices = None
        self._is_mandatory = None

    @property
    def type(self):
        """
        Gets the type of this JourneySurveyQuestion.
        Type of survey question.

        :return: The type of this JourneySurveyQuestion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this JourneySurveyQuestion.
        Type of survey question.

        :param type: The type of this JourneySurveyQuestion.
        :type: str
        """
        allowed_values = ["text", "hidden", "select", "checkbox", "textarea"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def label(self):
        """
        Gets the label of this JourneySurveyQuestion.
        Label of question.

        :return: The label of this JourneySurveyQuestion.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this JourneySurveyQuestion.
        Label of question.

        :param label: The label of this JourneySurveyQuestion.
        :type: str
        """
        
        self._label = label

    @property
    def customer_property(self):
        """
        Gets the customer_property of this JourneySurveyQuestion.
        The customer property that the answer maps to.

        :return: The customer_property of this JourneySurveyQuestion.
        :rtype: str
        """
        return self._customer_property

    @customer_property.setter
    def customer_property(self, customer_property):
        """
        Sets the customer_property of this JourneySurveyQuestion.
        The customer property that the answer maps to.

        :param customer_property: The customer_property of this JourneySurveyQuestion.
        :type: str
        """
        allowed_values = ["givenName", "familyName", "email", "phone", "gender", "companyName"]
        if customer_property.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for customer_property -> " + customer_property
            self._customer_property = "outdated_sdk_version"
        else:
            self._customer_property = customer_property

    @property
    def choices(self):
        """
        Gets the choices of this JourneySurveyQuestion.
        Choices available to user.

        :return: The choices of this JourneySurveyQuestion.
        :rtype: list[str]
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """
        Sets the choices of this JourneySurveyQuestion.
        Choices available to user.

        :param choices: The choices of this JourneySurveyQuestion.
        :type: list[str]
        """
        
        self._choices = choices

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this JourneySurveyQuestion.
        Whether answering this question is mandatory.

        :return: The is_mandatory of this JourneySurveyQuestion.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this JourneySurveyQuestion.
        Whether answering this question is mandatory.

        :param is_mandatory: The is_mandatory of this JourneySurveyQuestion.
        :type: bool
        """
        
        self._is_mandatory = is_mandatory

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
