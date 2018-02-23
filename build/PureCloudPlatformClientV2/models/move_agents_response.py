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


class MoveAgentsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MoveAgentsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'requesting_user': 'UserReference',
            'destination_management_unit': 'ManagementUnitReference',
            'results': 'list[MoveAgentResponse]'
        }

        self.attribute_map = {
            'requesting_user': 'requestingUser',
            'destination_management_unit': 'destinationManagementUnit',
            'results': 'results'
        }

        self._requesting_user = None
        self._destination_management_unit = None
        self._results = None

    @property
    def requesting_user(self):
        """
        Gets the requesting_user of this MoveAgentsResponse.
        The user that made the request

        :return: The requesting_user of this MoveAgentsResponse.
        :rtype: UserReference
        """
        return self._requesting_user

    @requesting_user.setter
    def requesting_user(self, requesting_user):
        """
        Sets the requesting_user of this MoveAgentsResponse.
        The user that made the request

        :param requesting_user: The requesting_user of this MoveAgentsResponse.
        :type: UserReference
        """
        
        self._requesting_user = requesting_user

    @property
    def destination_management_unit(self):
        """
        Gets the destination_management_unit of this MoveAgentsResponse.
        The management unit specified on the request

        :return: The destination_management_unit of this MoveAgentsResponse.
        :rtype: ManagementUnitReference
        """
        return self._destination_management_unit

    @destination_management_unit.setter
    def destination_management_unit(self, destination_management_unit):
        """
        Sets the destination_management_unit of this MoveAgentsResponse.
        The management unit specified on the request

        :param destination_management_unit: The destination_management_unit of this MoveAgentsResponse.
        :type: ManagementUnitReference
        """
        
        self._destination_management_unit = destination_management_unit

    @property
    def results(self):
        """
        Gets the results of this MoveAgentsResponse.
        The list containing the agent and result of the move operation

        :return: The results of this MoveAgentsResponse.
        :rtype: list[MoveAgentResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this MoveAgentsResponse.
        The list containing the agent and result of the move operation

        :param results: The results of this MoveAgentsResponse.
        :type: list[MoveAgentResponse]
        """
        
        self._results = results

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
