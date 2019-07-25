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

class DialerOutboundSettingsConfigChangeOutboundSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerOutboundSettingsConfigChangeOutboundSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'max_calls_per_agent': 'int',
            'max_line_utilization': 'float',
            'abandon_seconds': 'float',
            'compliance_abandon_rate_denominator': 'str',
            'automatic_time_zone_mapping': 'DialerOutboundSettingsConfigChangeAutomaticTimeZoneMappingSettings'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'max_calls_per_agent': 'maxCallsPerAgent',
            'max_line_utilization': 'maxLineUtilization',
            'abandon_seconds': 'abandonSeconds',
            'compliance_abandon_rate_denominator': 'complianceAbandonRateDenominator',
            'automatic_time_zone_mapping': 'automaticTimeZoneMapping'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._max_calls_per_agent = None
        self._max_line_utilization = None
        self._abandon_seconds = None
        self._compliance_abandon_rate_denominator = None
        self._automatic_time_zone_mapping = None

    @property
    def id(self):
        """
        Gets the id of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The id of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param id: The id of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The name of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param name: The name of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The date_created of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param date_created: The date_created of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The date_modified of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param date_modified: The date_modified of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The version of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param version: The version of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: int
        """
        
        self._version = version

    @property
    def max_calls_per_agent(self):
        """
        Gets the max_calls_per_agent of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The max_calls_per_agent of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: int
        """
        return self._max_calls_per_agent

    @max_calls_per_agent.setter
    def max_calls_per_agent(self, max_calls_per_agent):
        """
        Sets the max_calls_per_agent of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param max_calls_per_agent: The max_calls_per_agent of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: int
        """
        
        self._max_calls_per_agent = max_calls_per_agent

    @property
    def max_line_utilization(self):
        """
        Gets the max_line_utilization of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The max_line_utilization of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: float
        """
        return self._max_line_utilization

    @max_line_utilization.setter
    def max_line_utilization(self, max_line_utilization):
        """
        Sets the max_line_utilization of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param max_line_utilization: The max_line_utilization of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: float
        """
        
        self._max_line_utilization = max_line_utilization

    @property
    def abandon_seconds(self):
        """
        Gets the abandon_seconds of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The abandon_seconds of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: float
        """
        return self._abandon_seconds

    @abandon_seconds.setter
    def abandon_seconds(self, abandon_seconds):
        """
        Sets the abandon_seconds of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param abandon_seconds: The abandon_seconds of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: float
        """
        
        self._abandon_seconds = abandon_seconds

    @property
    def compliance_abandon_rate_denominator(self):
        """
        Gets the compliance_abandon_rate_denominator of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The compliance_abandon_rate_denominator of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: str
        """
        return self._compliance_abandon_rate_denominator

    @compliance_abandon_rate_denominator.setter
    def compliance_abandon_rate_denominator(self, compliance_abandon_rate_denominator):
        """
        Sets the compliance_abandon_rate_denominator of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param compliance_abandon_rate_denominator: The compliance_abandon_rate_denominator of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: str
        """
        allowed_values = ["ALL_CALLS", "CALLS_THAT_REACHED_QUEUE"]
        if compliance_abandon_rate_denominator.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for compliance_abandon_rate_denominator -> " + compliance_abandon_rate_denominator
            self._compliance_abandon_rate_denominator = "outdated_sdk_version"
        else:
            self._compliance_abandon_rate_denominator = compliance_abandon_rate_denominator

    @property
    def automatic_time_zone_mapping(self):
        """
        Gets the automatic_time_zone_mapping of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :return: The automatic_time_zone_mapping of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :rtype: DialerOutboundSettingsConfigChangeAutomaticTimeZoneMappingSettings
        """
        return self._automatic_time_zone_mapping

    @automatic_time_zone_mapping.setter
    def automatic_time_zone_mapping(self, automatic_time_zone_mapping):
        """
        Sets the automatic_time_zone_mapping of this DialerOutboundSettingsConfigChangeOutboundSettings.


        :param automatic_time_zone_mapping: The automatic_time_zone_mapping of this DialerOutboundSettingsConfigChangeOutboundSettings.
        :type: DialerOutboundSettingsConfigChangeAutomaticTimeZoneMappingSettings
        """
        
        self._automatic_time_zone_mapping = automatic_time_zone_mapping

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

