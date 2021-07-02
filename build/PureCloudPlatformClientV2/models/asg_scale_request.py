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

class AsgScaleRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsgScaleRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'desired_capacity': 'int',
            'minimum_capacity': 'int'
        }

        self.attribute_map = {
            'desired_capacity': 'desiredCapacity',
            'minimum_capacity': 'minimumCapacity'
        }

        self._desired_capacity = None
        self._minimum_capacity = None

    @property
    def desired_capacity(self):
        """
        Gets the desired_capacity of this AsgScaleRequest.
        The desired capacity of the ASG

        :return: The desired_capacity of this AsgScaleRequest.
        :rtype: int
        """
        return self._desired_capacity

    @desired_capacity.setter
    def desired_capacity(self, desired_capacity):
        """
        Sets the desired_capacity of this AsgScaleRequest.
        The desired capacity of the ASG

        :param desired_capacity: The desired_capacity of this AsgScaleRequest.
        :type: int
        """
        
        self._desired_capacity = desired_capacity

    @property
    def minimum_capacity(self):
        """
        Gets the minimum_capacity of this AsgScaleRequest.
        The minimum capacity of the ASG

        :return: The minimum_capacity of this AsgScaleRequest.
        :rtype: int
        """
        return self._minimum_capacity

    @minimum_capacity.setter
    def minimum_capacity(self, minimum_capacity):
        """
        Sets the minimum_capacity of this AsgScaleRequest.
        The minimum capacity of the ASG

        :param minimum_capacity: The minimum_capacity of this AsgScaleRequest.
        :type: int
        """
        
        self._minimum_capacity = minimum_capacity

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

