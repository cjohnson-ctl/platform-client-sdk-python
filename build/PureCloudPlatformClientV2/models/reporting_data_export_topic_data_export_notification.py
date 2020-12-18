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

class ReportingDataExportTopicDataExportNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportingDataExportTopicDataExportNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'run_id': 'str',
            'name': 'str',
            'status': 'str',
            'export_format': 'str',
            'download_url': 'str',
            'view_type': 'str',
            'export_error_messages_type': 'str',
            'read': 'bool',
            'created_date_time': 'datetime',
            'modified_date_time': 'datetime',
            'percentage_complete': 'float',
            'email_statuses': 'dict(str, str)',
            'email_error_description': 'str',
            'schedule_expression': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'run_id': 'runId',
            'name': 'name',
            'status': 'status',
            'export_format': 'exportFormat',
            'download_url': 'downloadUrl',
            'view_type': 'viewType',
            'export_error_messages_type': 'exportErrorMessagesType',
            'read': 'read',
            'created_date_time': 'createdDateTime',
            'modified_date_time': 'modifiedDateTime',
            'percentage_complete': 'percentageComplete',
            'email_statuses': 'emailStatuses',
            'email_error_description': 'emailErrorDescription',
            'schedule_expression': 'scheduleExpression'
        }

        self._id = None
        self._run_id = None
        self._name = None
        self._status = None
        self._export_format = None
        self._download_url = None
        self._view_type = None
        self._export_error_messages_type = None
        self._read = None
        self._created_date_time = None
        self._modified_date_time = None
        self._percentage_complete = None
        self._email_statuses = None
        self._email_error_description = None
        self._schedule_expression = None

    @property
    def id(self):
        """
        Gets the id of this ReportingDataExportTopicDataExportNotification.


        :return: The id of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportingDataExportTopicDataExportNotification.


        :param id: The id of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._id = id

    @property
    def run_id(self):
        """
        Gets the run_id of this ReportingDataExportTopicDataExportNotification.


        :return: The run_id of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this ReportingDataExportTopicDataExportNotification.


        :param run_id: The run_id of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._run_id = run_id

    @property
    def name(self):
        """
        Gets the name of this ReportingDataExportTopicDataExportNotification.


        :return: The name of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportingDataExportTopicDataExportNotification.


        :param name: The name of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this ReportingDataExportTopicDataExportNotification.


        :return: The status of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ReportingDataExportTopicDataExportNotification.


        :param status: The status of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        allowed_values = ["SUBMITTED", "RUNNING", "CANCELLING", "CANCELLED", "COMPLETED", "COMPLETED_WITH_PARTIAL_RESULTS", "FAILED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def export_format(self):
        """
        Gets the export_format of this ReportingDataExportTopicDataExportNotification.


        :return: The export_format of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        """
        Sets the export_format of this ReportingDataExportTopicDataExportNotification.


        :param export_format: The export_format of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        allowed_values = ["CSV", "PDF"]
        if export_format.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for export_format -> " + export_format)
            self._export_format = "outdated_sdk_version"
        else:
            self._export_format = export_format

    @property
    def download_url(self):
        """
        Gets the download_url of this ReportingDataExportTopicDataExportNotification.


        :return: The download_url of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ReportingDataExportTopicDataExportNotification.


        :param download_url: The download_url of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._download_url = download_url

    @property
    def view_type(self):
        """
        Gets the view_type of this ReportingDataExportTopicDataExportNotification.


        :return: The view_type of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """
        Sets the view_type of this ReportingDataExportTopicDataExportNotification.


        :param view_type: The view_type of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        allowed_values = ["QUEUE_PERFORMANCE_SUMMARY_VIEW", "QUEUE_PERFORMANCE_DETAIL_VIEW", "INTERACTION_SEARCH_VIEW", "AGENT_PERFORMANCE_SUMMARY_VIEW", "AGENT_PERFORMANCE_DETAIL_VIEW", "AGENT_STATUS_SUMMARY_VIEW", "AGENT_STATUS_DETAIL_VIEW", "AGENT_EVALUATION_SUMMARY_VIEW", "AGENT_EVALUATION_DETAIL_VIEW", "AGENT_QUEUE_DETAIL_VIEW", "AGENT_INTERACTION_DETAIL_VIEW", "ABANDON_INSIGHTS_VIEW", "SKILLS_PERFORMANCE_VIEW", "SURVEY_FORM_PERFORMANCE_SUMMARY_VIEW", "SURVEY_FORM_PERFORMANCE_DETAIL_VIEW", "DNIS_PERFORMANCE_SUMMARY_VIEW", "DNIS_PERFORMANCE_DETAIL_VIEW", "WRAP_UP_PERFORMANCE_SUMMARY_VIEW", "AGENT_WRAP_UP_PERFORMANCE_DETAIL_VIEW", "QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_ACTIVITY_DETAIL_VIEW", "AGENT_QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_AGENT_DETAIL_VIEW", "QUEUE_INTERACTION_DETAIL_VIEW", "AGENT_SCHEDULE_DETAIL_VIEW", "IVR_PERFORMANCE_SUMMARY_VIEW", "IVR_PERFORMANCE_DETAIL_VIEW", "ANSWER_INSIGHTS_VIEW", "HANDLE_INSIGHTS_VIEW", "TALK_INSIGHTS_VIEW", "HOLD_INSIGHTS_VIEW", "ACW_INSIGHTS_VIEW", "WAIT_INSIGHTS_VIEW", "AGENT_WRAP_UP_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_OUTCOME_SUMMARY_VIEW", "FLOW_OUTCOME_PERFORMANCE_DETAIL_VIEW", "FLOW_OUTCOME_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_DESTINATION_SUMMARY_VIEW", "FLOW_DESTINATION_DETAIL_VIEW", "SCHEDULED_CALLBACKS_VIEW", "CONTENT_SEARCH_VIEW"]
        if view_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for view_type -> " + view_type)
            self._view_type = "outdated_sdk_version"
        else:
            self._view_type = view_type

    @property
    def export_error_messages_type(self):
        """
        Gets the export_error_messages_type of this ReportingDataExportTopicDataExportNotification.


        :return: The export_error_messages_type of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._export_error_messages_type

    @export_error_messages_type.setter
    def export_error_messages_type(self, export_error_messages_type):
        """
        Sets the export_error_messages_type of this ReportingDataExportTopicDataExportNotification.


        :param export_error_messages_type: The export_error_messages_type of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        allowed_values = ["FAILED_CONVERTING_EXPORT_JOB", "FAILED_NO_DATA_EXPORT_JOB_FOUND", "FAILED_GETTING_DATA_FROM_SERVICE", "FAILED_GENERATING_TEMP_FILE", "FAILED_SAVING_FILE_TO_S3", "FAILED_NOTIFYING_SKYWALKER_OF_DOWNLOAD", "FAILED_BUILDING_DOWNLOAD_URL_FROM_SKYWALKER_RESPONSE", "EXPORT_TYPE_NOT_IMPLEMENTED", "REACHED_MAXIMUM_ATTEMPT_OF_RETRY", "FAILED_LONG_RUNNING_EXPORT", "TOO_MANY_REQUESTS_FROM_AN_ORGANIZATION"]
        if export_error_messages_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for export_error_messages_type -> " + export_error_messages_type)
            self._export_error_messages_type = "outdated_sdk_version"
        else:
            self._export_error_messages_type = export_error_messages_type

    @property
    def read(self):
        """
        Gets the read of this ReportingDataExportTopicDataExportNotification.


        :return: The read of this ReportingDataExportTopicDataExportNotification.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this ReportingDataExportTopicDataExportNotification.


        :param read: The read of this ReportingDataExportTopicDataExportNotification.
        :type: bool
        """
        
        self._read = read

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this ReportingDataExportTopicDataExportNotification.


        :return: The created_date_time of this ReportingDataExportTopicDataExportNotification.
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this ReportingDataExportTopicDataExportNotification.


        :param created_date_time: The created_date_time of this ReportingDataExportTopicDataExportNotification.
        :type: datetime
        """
        
        self._created_date_time = created_date_time

    @property
    def modified_date_time(self):
        """
        Gets the modified_date_time of this ReportingDataExportTopicDataExportNotification.


        :return: The modified_date_time of this ReportingDataExportTopicDataExportNotification.
        :rtype: datetime
        """
        return self._modified_date_time

    @modified_date_time.setter
    def modified_date_time(self, modified_date_time):
        """
        Sets the modified_date_time of this ReportingDataExportTopicDataExportNotification.


        :param modified_date_time: The modified_date_time of this ReportingDataExportTopicDataExportNotification.
        :type: datetime
        """
        
        self._modified_date_time = modified_date_time

    @property
    def percentage_complete(self):
        """
        Gets the percentage_complete of this ReportingDataExportTopicDataExportNotification.


        :return: The percentage_complete of this ReportingDataExportTopicDataExportNotification.
        :rtype: float
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        """
        Sets the percentage_complete of this ReportingDataExportTopicDataExportNotification.


        :param percentage_complete: The percentage_complete of this ReportingDataExportTopicDataExportNotification.
        :type: float
        """
        
        self._percentage_complete = percentage_complete

    @property
    def email_statuses(self):
        """
        Gets the email_statuses of this ReportingDataExportTopicDataExportNotification.


        :return: The email_statuses of this ReportingDataExportTopicDataExportNotification.
        :rtype: dict(str, str)
        """
        return self._email_statuses

    @email_statuses.setter
    def email_statuses(self, email_statuses):
        """
        Sets the email_statuses of this ReportingDataExportTopicDataExportNotification.


        :param email_statuses: The email_statuses of this ReportingDataExportTopicDataExportNotification.
        :type: dict(str, str)
        """
        
        self._email_statuses = email_statuses

    @property
    def email_error_description(self):
        """
        Gets the email_error_description of this ReportingDataExportTopicDataExportNotification.


        :return: The email_error_description of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._email_error_description

    @email_error_description.setter
    def email_error_description(self, email_error_description):
        """
        Sets the email_error_description of this ReportingDataExportTopicDataExportNotification.


        :param email_error_description: The email_error_description of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._email_error_description = email_error_description

    @property
    def schedule_expression(self):
        """
        Gets the schedule_expression of this ReportingDataExportTopicDataExportNotification.


        :return: The schedule_expression of this ReportingDataExportTopicDataExportNotification.
        :rtype: str
        """
        return self._schedule_expression

    @schedule_expression.setter
    def schedule_expression(self, schedule_expression):
        """
        Sets the schedule_expression of this ReportingDataExportTopicDataExportNotification.


        :param schedule_expression: The schedule_expression of this ReportingDataExportTopicDataExportNotification.
        :type: str
        """
        
        self._schedule_expression = schedule_expression

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

