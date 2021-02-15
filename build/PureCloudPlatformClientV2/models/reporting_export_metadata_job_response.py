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

class ReportingExportMetadataJobResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportingExportMetadataJobResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'view_type': 'str',
            'date_limitations': 'str',
            'required_filters': 'list[str]',
            'supported_filters': 'list[str]',
            'required_column_ids': 'list[str]',
            'dependent_column_ids': 'dict(str, list[str])',
            'available_column_ids': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'view_type': 'viewType',
            'date_limitations': 'dateLimitations',
            'required_filters': 'requiredFilters',
            'supported_filters': 'supportedFilters',
            'required_column_ids': 'requiredColumnIds',
            'dependent_column_ids': 'dependentColumnIds',
            'available_column_ids': 'availableColumnIds',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._view_type = None
        self._date_limitations = None
        self._required_filters = None
        self._supported_filters = None
        self._required_column_ids = None
        self._dependent_column_ids = None
        self._available_column_ids = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this ReportingExportMetadataJobResponse.
        The globally unique identifier for the object.

        :return: The id of this ReportingExportMetadataJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportingExportMetadataJobResponse.
        The globally unique identifier for the object.

        :param id: The id of this ReportingExportMetadataJobResponse.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ReportingExportMetadataJobResponse.


        :return: The name of this ReportingExportMetadataJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportingExportMetadataJobResponse.


        :param name: The name of this ReportingExportMetadataJobResponse.
        :type: str
        """
        
        self._name = name

    @property
    def view_type(self):
        """
        Gets the view_type of this ReportingExportMetadataJobResponse.
        The view type of the export metadata

        :return: The view_type of this ReportingExportMetadataJobResponse.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """
        Sets the view_type of this ReportingExportMetadataJobResponse.
        The view type of the export metadata

        :param view_type: The view_type of this ReportingExportMetadataJobResponse.
        :type: str
        """
        allowed_values = ["QUEUE_PERFORMANCE_SUMMARY_VIEW", "QUEUE_PERFORMANCE_DETAIL_VIEW", "INTERACTION_SEARCH_VIEW", "AGENT_PERFORMANCE_SUMMARY_VIEW", "AGENT_PERFORMANCE_DETAIL_VIEW", "AGENT_STATUS_SUMMARY_VIEW", "AGENT_STATUS_DETAIL_VIEW", "AGENT_EVALUATION_SUMMARY_VIEW", "AGENT_EVALUATION_DETAIL_VIEW", "AGENT_QUEUE_DETAIL_VIEW", "AGENT_INTERACTION_DETAIL_VIEW", "ABANDON_INSIGHTS_VIEW", "SKILLS_PERFORMANCE_VIEW", "SURVEY_FORM_PERFORMANCE_SUMMARY_VIEW", "SURVEY_FORM_PERFORMANCE_DETAIL_VIEW", "DNIS_PERFORMANCE_SUMMARY_VIEW", "DNIS_PERFORMANCE_DETAIL_VIEW", "WRAP_UP_PERFORMANCE_SUMMARY_VIEW", "AGENT_WRAP_UP_PERFORMANCE_DETAIL_VIEW", "QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_ACTIVITY_DETAIL_VIEW", "AGENT_QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_AGENT_DETAIL_VIEW", "QUEUE_INTERACTION_DETAIL_VIEW", "AGENT_SCHEDULE_DETAIL_VIEW", "IVR_PERFORMANCE_SUMMARY_VIEW", "IVR_PERFORMANCE_DETAIL_VIEW", "ANSWER_INSIGHTS_VIEW", "HANDLE_INSIGHTS_VIEW", "TALK_INSIGHTS_VIEW", "HOLD_INSIGHTS_VIEW", "ACW_INSIGHTS_VIEW", "WAIT_INSIGHTS_VIEW", "AGENT_WRAP_UP_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_OUTCOME_SUMMARY_VIEW", "FLOW_OUTCOME_PERFORMANCE_DETAIL_VIEW", "FLOW_OUTCOME_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_DESTINATION_SUMMARY_VIEW", "FLOW_DESTINATION_DETAIL_VIEW", "API_USAGE_VIEW", "SCHEDULED_CALLBACKS_VIEW", "CONTENT_SEARCH_VIEW", "LANDING_PAGE", "DASHBOARD_SUMMARY", "DASHBOARD_DETAIL", "JOURNEY_ACTION_MAP_SUMMARY_VIEW", "JOURNEY_OUTCOME_SUMMARY_VIEW", "JOURNEY_SEGMENT_SUMMARY_VIEW", "AGENT_DEVELOPMENT_DETAIL_VIEW", "AGENT_DEVELOPMENT_DETAIL_ME_VIEW", "AGENT_DEVELOPMENT_SUMMARY_VIEW", "AGENT_PERFORMANCE_ME_VIEW", "AGENT_STATUS_ME_VIEW", "AGENT_EVALUATION_ME_VIEW"]
        if view_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for view_type -> " + view_type)
            self._view_type = "outdated_sdk_version"
        else:
            self._view_type = view_type

    @property
    def date_limitations(self):
        """
        Gets the date_limitations of this ReportingExportMetadataJobResponse.
        The date limitations of the export metadata

        :return: The date_limitations of this ReportingExportMetadataJobResponse.
        :rtype: str
        """
        return self._date_limitations

    @date_limitations.setter
    def date_limitations(self, date_limitations):
        """
        Sets the date_limitations of this ReportingExportMetadataJobResponse.
        The date limitations of the export metadata

        :param date_limitations: The date_limitations of this ReportingExportMetadataJobResponse.
        :type: str
        """
        
        self._date_limitations = date_limitations

    @property
    def required_filters(self):
        """
        Gets the required_filters of this ReportingExportMetadataJobResponse.
        The list of required filters for the export metadata

        :return: The required_filters of this ReportingExportMetadataJobResponse.
        :rtype: list[str]
        """
        return self._required_filters

    @required_filters.setter
    def required_filters(self, required_filters):
        """
        Sets the required_filters of this ReportingExportMetadataJobResponse.
        The list of required filters for the export metadata

        :param required_filters: The required_filters of this ReportingExportMetadataJobResponse.
        :type: list[str]
        """
        
        self._required_filters = required_filters

    @property
    def supported_filters(self):
        """
        Gets the supported_filters of this ReportingExportMetadataJobResponse.
        The list of supported filters for the export metadata

        :return: The supported_filters of this ReportingExportMetadataJobResponse.
        :rtype: list[str]
        """
        return self._supported_filters

    @supported_filters.setter
    def supported_filters(self, supported_filters):
        """
        Sets the supported_filters of this ReportingExportMetadataJobResponse.
        The list of supported filters for the export metadata

        :param supported_filters: The supported_filters of this ReportingExportMetadataJobResponse.
        :type: list[str]
        """
        
        self._supported_filters = supported_filters

    @property
    def required_column_ids(self):
        """
        Gets the required_column_ids of this ReportingExportMetadataJobResponse.
        The list of required column ids for the export metadata

        :return: The required_column_ids of this ReportingExportMetadataJobResponse.
        :rtype: list[str]
        """
        return self._required_column_ids

    @required_column_ids.setter
    def required_column_ids(self, required_column_ids):
        """
        Sets the required_column_ids of this ReportingExportMetadataJobResponse.
        The list of required column ids for the export metadata

        :param required_column_ids: The required_column_ids of this ReportingExportMetadataJobResponse.
        :type: list[str]
        """
        
        self._required_column_ids = required_column_ids

    @property
    def dependent_column_ids(self):
        """
        Gets the dependent_column_ids of this ReportingExportMetadataJobResponse.
        The list of dependent column ids for the export metadata

        :return: The dependent_column_ids of this ReportingExportMetadataJobResponse.
        :rtype: dict(str, list[str])
        """
        return self._dependent_column_ids

    @dependent_column_ids.setter
    def dependent_column_ids(self, dependent_column_ids):
        """
        Sets the dependent_column_ids of this ReportingExportMetadataJobResponse.
        The list of dependent column ids for the export metadata

        :param dependent_column_ids: The dependent_column_ids of this ReportingExportMetadataJobResponse.
        :type: dict(str, list[str])
        """
        
        self._dependent_column_ids = dependent_column_ids

    @property
    def available_column_ids(self):
        """
        Gets the available_column_ids of this ReportingExportMetadataJobResponse.
        The list of available column ids for the export metadata

        :return: The available_column_ids of this ReportingExportMetadataJobResponse.
        :rtype: list[str]
        """
        return self._available_column_ids

    @available_column_ids.setter
    def available_column_ids(self, available_column_ids):
        """
        Sets the available_column_ids of this ReportingExportMetadataJobResponse.
        The list of available column ids for the export metadata

        :param available_column_ids: The available_column_ids of this ReportingExportMetadataJobResponse.
        :type: list[str]
        """
        
        self._available_column_ids = available_column_ids

    @property
    def self_uri(self):
        """
        Gets the self_uri of this ReportingExportMetadataJobResponse.
        The URI for this object

        :return: The self_uri of this ReportingExportMetadataJobResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this ReportingExportMetadataJobResponse.
        The URI for this object

        :param self_uri: The self_uri of this ReportingExportMetadataJobResponse.
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

