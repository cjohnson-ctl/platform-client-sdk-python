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

class MediaSetting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MediaSetting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alerting_timeout_seconds': 'int',
            'service_level': 'ServiceLevel'
        }

        self.attribute_map = {
            'alerting_timeout_seconds': 'alertingTimeoutSeconds',
            'service_level': 'serviceLevel'
        }

        self._alerting_timeout_seconds = None
        self._service_level = None

    @property
    def alerting_timeout_seconds(self):
        """
        Gets the alerting_timeout_seconds of this MediaSetting.


        :return: The alerting_timeout_seconds of this MediaSetting.
        :rtype: int
        """
        return self._alerting_timeout_seconds

    @alerting_timeout_seconds.setter
    def alerting_timeout_seconds(self, alerting_timeout_seconds):
        """
        Sets the alerting_timeout_seconds of this MediaSetting.


        :param alerting_timeout_seconds: The alerting_timeout_seconds of this MediaSetting.
        :type: int
        """
        
        self._alerting_timeout_seconds = alerting_timeout_seconds

    @property
    def service_level(self):
        """
        Gets the service_level of this MediaSetting.


        :return: The service_level of this MediaSetting.
        :rtype: ServiceLevel
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """
        Sets the service_level of this MediaSetting.


        :param service_level: The service_level of this MediaSetting.
        :type: ServiceLevel
        """
        
        self._service_level = service_level

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

