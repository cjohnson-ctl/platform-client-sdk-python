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

class BuShortTermForecast(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuShortTermForecast - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'week_date': 'date',
            'week_count': 'int',
            'creation_method': 'str',
            'description': 'str',
            'legacy': 'bool',
            'metadata': 'WfmVersionedEntityMetadata',
            'reference_start_date': 'datetime',
            'source_days': 'list[ForecastSourceDayPointer]',
            'modifications': 'list[BuForecastModification]',
            'generation_results': 'BuForecastGenerationResult',
            'time_zone': 'str',
            'planning_groups_version': 'int',
            'planning_groups': 'ForecastPlanningGroupsResponse',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'week_date': 'weekDate',
            'week_count': 'weekCount',
            'creation_method': 'creationMethod',
            'description': 'description',
            'legacy': 'legacy',
            'metadata': 'metadata',
            'reference_start_date': 'referenceStartDate',
            'source_days': 'sourceDays',
            'modifications': 'modifications',
            'generation_results': 'generationResults',
            'time_zone': 'timeZone',
            'planning_groups_version': 'planningGroupsVersion',
            'planning_groups': 'planningGroups',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._week_date = None
        self._week_count = None
        self._creation_method = None
        self._description = None
        self._legacy = None
        self._metadata = None
        self._reference_start_date = None
        self._source_days = None
        self._modifications = None
        self._generation_results = None
        self._time_zone = None
        self._planning_groups_version = None
        self._planning_groups = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this BuShortTermForecast.
        The globally unique identifier for the object.

        :return: The id of this BuShortTermForecast.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuShortTermForecast.
        The globally unique identifier for the object.

        :param id: The id of this BuShortTermForecast.
        :type: str
        """
        
        self._id = id

    @property
    def week_date(self):
        """
        Gets the week_date of this BuShortTermForecast.
        The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The week_date of this BuShortTermForecast.
        :rtype: date
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date):
        """
        Sets the week_date of this BuShortTermForecast.
        The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param week_date: The week_date of this BuShortTermForecast.
        :type: date
        """
        
        self._week_date = week_date

    @property
    def week_count(self):
        """
        Gets the week_count of this BuShortTermForecast.
        The number of weeks this forecast covers

        :return: The week_count of this BuShortTermForecast.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count):
        """
        Sets the week_count of this BuShortTermForecast.
        The number of weeks this forecast covers

        :param week_count: The week_count of this BuShortTermForecast.
        :type: int
        """
        
        self._week_count = week_count

    @property
    def creation_method(self):
        """
        Gets the creation_method of this BuShortTermForecast.
        The method by which this forecast was created

        :return: The creation_method of this BuShortTermForecast.
        :rtype: str
        """
        return self._creation_method

    @creation_method.setter
    def creation_method(self, creation_method):
        """
        Sets the creation_method of this BuShortTermForecast.
        The method by which this forecast was created

        :param creation_method: The creation_method of this BuShortTermForecast.
        :type: str
        """
        allowed_values = ["Import", "ImportedHistoricalWeightedAverage", "HistoricalWeightedAverage", "Advanced"]
        if creation_method.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for creation_method -> " + creation_method
            self._creation_method = "outdated_sdk_version"
        else:
            self._creation_method = creation_method

    @property
    def description(self):
        """
        Gets the description of this BuShortTermForecast.
        The description of this forecast

        :return: The description of this BuShortTermForecast.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuShortTermForecast.
        The description of this forecast

        :param description: The description of this BuShortTermForecast.
        :type: str
        """
        
        self._description = description

    @property
    def legacy(self):
        """
        Gets the legacy of this BuShortTermForecast.
        Whether this forecast contains modifications on legacy metrics

        :return: The legacy of this BuShortTermForecast.
        :rtype: bool
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy):
        """
        Sets the legacy of this BuShortTermForecast.
        Whether this forecast contains modifications on legacy metrics

        :param legacy: The legacy of this BuShortTermForecast.
        :type: bool
        """
        
        self._legacy = legacy

    @property
    def metadata(self):
        """
        Gets the metadata of this BuShortTermForecast.
        Metadata for this forecast

        :return: The metadata of this BuShortTermForecast.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this BuShortTermForecast.
        Metadata for this forecast

        :param metadata: The metadata of this BuShortTermForecast.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

    @property
    def reference_start_date(self):
        """
        Gets the reference_start_date of this BuShortTermForecast.
        The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The reference_start_date of this BuShortTermForecast.
        :rtype: datetime
        """
        return self._reference_start_date

    @reference_start_date.setter
    def reference_start_date(self, reference_start_date):
        """
        Sets the reference_start_date of this BuShortTermForecast.
        The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param reference_start_date: The reference_start_date of this BuShortTermForecast.
        :type: datetime
        """
        
        self._reference_start_date = reference_start_date

    @property
    def source_days(self):
        """
        Gets the source_days of this BuShortTermForecast.
        The source day pointers for this forecast

        :return: The source_days of this BuShortTermForecast.
        :rtype: list[ForecastSourceDayPointer]
        """
        return self._source_days

    @source_days.setter
    def source_days(self, source_days):
        """
        Sets the source_days of this BuShortTermForecast.
        The source day pointers for this forecast

        :param source_days: The source_days of this BuShortTermForecast.
        :type: list[ForecastSourceDayPointer]
        """
        
        self._source_days = source_days

    @property
    def modifications(self):
        """
        Gets the modifications of this BuShortTermForecast.
        Any manual modifications applied to this forecast

        :return: The modifications of this BuShortTermForecast.
        :rtype: list[BuForecastModification]
        """
        return self._modifications

    @modifications.setter
    def modifications(self, modifications):
        """
        Sets the modifications of this BuShortTermForecast.
        Any manual modifications applied to this forecast

        :param modifications: The modifications of this BuShortTermForecast.
        :type: list[BuForecastModification]
        """
        
        self._modifications = modifications

    @property
    def generation_results(self):
        """
        Gets the generation_results of this BuShortTermForecast.
        Generation result metadata

        :return: The generation_results of this BuShortTermForecast.
        :rtype: BuForecastGenerationResult
        """
        return self._generation_results

    @generation_results.setter
    def generation_results(self, generation_results):
        """
        Sets the generation_results of this BuShortTermForecast.
        Generation result metadata

        :param generation_results: The generation_results of this BuShortTermForecast.
        :type: BuForecastGenerationResult
        """
        
        self._generation_results = generation_results

    @property
    def time_zone(self):
        """
        Gets the time_zone of this BuShortTermForecast.
        The time zone for this forecast

        :return: The time_zone of this BuShortTermForecast.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this BuShortTermForecast.
        The time zone for this forecast

        :param time_zone: The time_zone of this BuShortTermForecast.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def planning_groups_version(self):
        """
        Gets the planning_groups_version of this BuShortTermForecast.
        The version of the planning groups that was used for this forecast

        :return: The planning_groups_version of this BuShortTermForecast.
        :rtype: int
        """
        return self._planning_groups_version

    @planning_groups_version.setter
    def planning_groups_version(self, planning_groups_version):
        """
        Sets the planning_groups_version of this BuShortTermForecast.
        The version of the planning groups that was used for this forecast

        :param planning_groups_version: The planning_groups_version of this BuShortTermForecast.
        :type: int
        """
        
        self._planning_groups_version = planning_groups_version

    @property
    def planning_groups(self):
        """
        Gets the planning_groups of this BuShortTermForecast.
        A snapshot of the planning groups used for this forecast as of the version number indicated

        :return: The planning_groups of this BuShortTermForecast.
        :rtype: ForecastPlanningGroupsResponse
        """
        return self._planning_groups

    @planning_groups.setter
    def planning_groups(self, planning_groups):
        """
        Sets the planning_groups of this BuShortTermForecast.
        A snapshot of the planning groups used for this forecast as of the version number indicated

        :param planning_groups: The planning_groups of this BuShortTermForecast.
        :type: ForecastPlanningGroupsResponse
        """
        
        self._planning_groups = planning_groups

    @property
    def self_uri(self):
        """
        Gets the self_uri of this BuShortTermForecast.
        The URI for this object

        :return: The self_uri of this BuShortTermForecast.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this BuShortTermForecast.
        The URI for this object

        :param self_uri: The self_uri of this BuShortTermForecast.
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

