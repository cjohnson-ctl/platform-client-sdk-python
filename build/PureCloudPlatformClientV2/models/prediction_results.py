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

class PredictionResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PredictionResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'intent': 'str',
            'formula': 'str',
            'estimated_wait_time_seconds': 'int'
        }

        self.attribute_map = {
            'intent': 'intent',
            'formula': 'formula',
            'estimated_wait_time_seconds': 'estimatedWaitTimeSeconds'
        }

        self._intent = None
        self._formula = None
        self._estimated_wait_time_seconds = None

    @property
    def intent(self):
        """
        Gets the intent of this PredictionResults.
        Indicates the media type scope of this estimated wait time

        :return: The intent of this PredictionResults.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """
        Sets the intent of this PredictionResults.
        Indicates the media type scope of this estimated wait time

        :param intent: The intent of this PredictionResults.
        :type: str
        """
        allowed_values = ["ALL", "CALL", "CALLBACK", "CHAT", "EMAIL", "SOCIALEXPRESSION", "VIDEOCOMM", "MESSAGE"]
        if intent.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for intent -> " + intent)
            self._intent = "outdated_sdk_version"
        else:
            self._intent = intent

    @property
    def formula(self):
        """
        Gets the formula of this PredictionResults.
        Indicates the estimated wait time Formula

        :return: The formula of this PredictionResults.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this PredictionResults.
        Indicates the estimated wait time Formula

        :param formula: The formula of this PredictionResults.
        :type: str
        """
        allowed_values = ["BEST", "SIMPLE", "ABANDON", "PATIENCE_ABANDON"]
        if formula.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for formula -> " + formula)
            self._formula = "outdated_sdk_version"
        else:
            self._formula = formula

    @property
    def estimated_wait_time_seconds(self):
        """
        Gets the estimated_wait_time_seconds of this PredictionResults.
        Estimated wait time in seconds

        :return: The estimated_wait_time_seconds of this PredictionResults.
        :rtype: int
        """
        return self._estimated_wait_time_seconds

    @estimated_wait_time_seconds.setter
    def estimated_wait_time_seconds(self, estimated_wait_time_seconds):
        """
        Sets the estimated_wait_time_seconds of this PredictionResults.
        Estimated wait time in seconds

        :param estimated_wait_time_seconds: The estimated_wait_time_seconds of this PredictionResults.
        :type: int
        """
        
        self._estimated_wait_time_seconds = estimated_wait_time_seconds

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

