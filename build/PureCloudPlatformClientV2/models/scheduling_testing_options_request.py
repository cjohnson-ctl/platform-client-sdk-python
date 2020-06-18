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

class SchedulingTestingOptionsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SchedulingTestingOptionsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fast_scheduling': 'bool',
            'delay_scheduling': 'bool',
            'fail_scheduling': 'bool',
            'populate_warnings': 'bool'
        }

        self.attribute_map = {
            'fast_scheduling': 'fastScheduling',
            'delay_scheduling': 'delayScheduling',
            'fail_scheduling': 'failScheduling',
            'populate_warnings': 'populateWarnings'
        }

        self._fast_scheduling = None
        self._delay_scheduling = None
        self._fail_scheduling = None
        self._populate_warnings = None

    @property
    def fast_scheduling(self):
        """
        Gets the fast_scheduling of this SchedulingTestingOptionsRequest.
        Whether to enable fast scheduling

        :return: The fast_scheduling of this SchedulingTestingOptionsRequest.
        :rtype: bool
        """
        return self._fast_scheduling

    @fast_scheduling.setter
    def fast_scheduling(self, fast_scheduling):
        """
        Sets the fast_scheduling of this SchedulingTestingOptionsRequest.
        Whether to enable fast scheduling

        :param fast_scheduling: The fast_scheduling of this SchedulingTestingOptionsRequest.
        :type: bool
        """
        
        self._fast_scheduling = fast_scheduling

    @property
    def delay_scheduling(self):
        """
        Gets the delay_scheduling of this SchedulingTestingOptionsRequest.
        Whether to force delayed scheduling

        :return: The delay_scheduling of this SchedulingTestingOptionsRequest.
        :rtype: bool
        """
        return self._delay_scheduling

    @delay_scheduling.setter
    def delay_scheduling(self, delay_scheduling):
        """
        Sets the delay_scheduling of this SchedulingTestingOptionsRequest.
        Whether to force delayed scheduling

        :param delay_scheduling: The delay_scheduling of this SchedulingTestingOptionsRequest.
        :type: bool
        """
        
        self._delay_scheduling = delay_scheduling

    @property
    def fail_scheduling(self):
        """
        Gets the fail_scheduling of this SchedulingTestingOptionsRequest.
        Whether to force scheduling to fail

        :return: The fail_scheduling of this SchedulingTestingOptionsRequest.
        :rtype: bool
        """
        return self._fail_scheduling

    @fail_scheduling.setter
    def fail_scheduling(self, fail_scheduling):
        """
        Sets the fail_scheduling of this SchedulingTestingOptionsRequest.
        Whether to force scheduling to fail

        :param fail_scheduling: The fail_scheduling of this SchedulingTestingOptionsRequest.
        :type: bool
        """
        
        self._fail_scheduling = fail_scheduling

    @property
    def populate_warnings(self):
        """
        Gets the populate_warnings of this SchedulingTestingOptionsRequest.
        Whether to populate warnings in the generated schedule

        :return: The populate_warnings of this SchedulingTestingOptionsRequest.
        :rtype: bool
        """
        return self._populate_warnings

    @populate_warnings.setter
    def populate_warnings(self, populate_warnings):
        """
        Sets the populate_warnings of this SchedulingTestingOptionsRequest.
        Whether to populate warnings in the generated schedule

        :param populate_warnings: The populate_warnings of this SchedulingTestingOptionsRequest.
        :type: bool
        """
        
        self._populate_warnings = populate_warnings

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
