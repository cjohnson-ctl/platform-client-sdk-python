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

class ReportingExportJobResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportingExportJobResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'run_id': 'str',
            'status': 'str',
            'time_zone': 'str',
            'export_format': 'str',
            'interval': 'str',
            'download_url': 'str',
            'view_type': 'str',
            'export_error_messages_type': 'str',
            'period': 'str',
            'filter': 'ViewFilter',
            'read': 'bool',
            'created_date_time': 'datetime',
            'modified_date_time': 'datetime',
            'locale': 'str',
            'percentage_complete': 'float',
            'has_format_durations': 'bool',
            'has_split_filters': 'bool',
            'exclude_empty_rows': 'bool',
            'has_split_by_media': 'bool',
            'has_summary_row': 'bool',
            'csv_delimiter': 'str',
            'selected_columns': 'list[SelectedColumns]',
            'has_custom_participant_attributes': 'bool',
            'recipient_emails': 'list[str]',
            'email_statuses': 'dict(str, str)',
            'email_error_description': 'str',
            'enabled': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'run_id': 'runId',
            'status': 'status',
            'time_zone': 'timeZone',
            'export_format': 'exportFormat',
            'interval': 'interval',
            'download_url': 'downloadUrl',
            'view_type': 'viewType',
            'export_error_messages_type': 'exportErrorMessagesType',
            'period': 'period',
            'filter': 'filter',
            'read': 'read',
            'created_date_time': 'createdDateTime',
            'modified_date_time': 'modifiedDateTime',
            'locale': 'locale',
            'percentage_complete': 'percentageComplete',
            'has_format_durations': 'hasFormatDurations',
            'has_split_filters': 'hasSplitFilters',
            'exclude_empty_rows': 'excludeEmptyRows',
            'has_split_by_media': 'hasSplitByMedia',
            'has_summary_row': 'hasSummaryRow',
            'csv_delimiter': 'csvDelimiter',
            'selected_columns': 'selectedColumns',
            'has_custom_participant_attributes': 'hasCustomParticipantAttributes',
            'recipient_emails': 'recipientEmails',
            'email_statuses': 'emailStatuses',
            'email_error_description': 'emailErrorDescription',
            'enabled': 'enabled',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._run_id = None
        self._status = None
        self._time_zone = None
        self._export_format = None
        self._interval = None
        self._download_url = None
        self._view_type = None
        self._export_error_messages_type = None
        self._period = None
        self._filter = None
        self._read = None
        self._created_date_time = None
        self._modified_date_time = None
        self._locale = None
        self._percentage_complete = None
        self._has_format_durations = None
        self._has_split_filters = None
        self._exclude_empty_rows = None
        self._has_split_by_media = None
        self._has_summary_row = None
        self._csv_delimiter = None
        self._selected_columns = None
        self._has_custom_participant_attributes = None
        self._recipient_emails = None
        self._email_statuses = None
        self._email_error_description = None
        self._enabled = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this ReportingExportJobResponse.
        The globally unique identifier for the object.

        :return: The id of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportingExportJobResponse.
        The globally unique identifier for the object.

        :param id: The id of this ReportingExportJobResponse.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ReportingExportJobResponse.


        :return: The name of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportingExportJobResponse.


        :param name: The name of this ReportingExportJobResponse.
        :type: str
        """
        
        self._name = name

    @property
    def run_id(self):
        """
        Gets the run_id of this ReportingExportJobResponse.
        The unique run id of the export schedule execute

        :return: The run_id of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this ReportingExportJobResponse.
        The unique run id of the export schedule execute

        :param run_id: The run_id of this ReportingExportJobResponse.
        :type: str
        """
        
        self._run_id = run_id

    @property
    def status(self):
        """
        Gets the status of this ReportingExportJobResponse.
        The current status of the export request

        :return: The status of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ReportingExportJobResponse.
        The current status of the export request

        :param status: The status of this ReportingExportJobResponse.
        :type: str
        """
        allowed_values = ["SUBMITTED", "RUNNING", "CANCELLING", "CANCELLED", "COMPLETED", "COMPLETED_WITH_PARTIAL_RESULTS", "FAILED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ReportingExportJobResponse.
        The requested timezone of the exported data. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :return: The time_zone of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ReportingExportJobResponse.
        The requested timezone of the exported data. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :param time_zone: The time_zone of this ReportingExportJobResponse.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def export_format(self):
        """
        Gets the export_format of this ReportingExportJobResponse.
        The requested format of the exported data

        :return: The export_format of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        """
        Sets the export_format of this ReportingExportJobResponse.
        The requested format of the exported data

        :param export_format: The export_format of this ReportingExportJobResponse.
        :type: str
        """
        allowed_values = ["CSV", "PDF"]
        if export_format.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for export_format -> " + export_format)
            self._export_format = "outdated_sdk_version"
        else:
            self._export_format = export_format

    @property
    def interval(self):
        """
        Gets the interval of this ReportingExportJobResponse.
        The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ReportingExportJobResponse.
        The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this ReportingExportJobResponse.
        :type: str
        """
        
        self._interval = interval

    @property
    def download_url(self):
        """
        Gets the download_url of this ReportingExportJobResponse.
        The url to download the request if it's status is completed

        :return: The download_url of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ReportingExportJobResponse.
        The url to download the request if it's status is completed

        :param download_url: The download_url of this ReportingExportJobResponse.
        :type: str
        """
        
        self._download_url = download_url

    @property
    def view_type(self):
        """
        Gets the view_type of this ReportingExportJobResponse.
        The type of view export job to be created

        :return: The view_type of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """
        Sets the view_type of this ReportingExportJobResponse.
        The type of view export job to be created

        :param view_type: The view_type of this ReportingExportJobResponse.
        :type: str
        """
        allowed_values = ["QUEUE_PERFORMANCE_SUMMARY_VIEW", "QUEUE_PERFORMANCE_DETAIL_VIEW", "INTERACTION_SEARCH_VIEW", "AGENT_PERFORMANCE_SUMMARY_VIEW", "AGENT_PERFORMANCE_DETAIL_VIEW", "AGENT_STATUS_SUMMARY_VIEW", "AGENT_STATUS_DETAIL_VIEW", "AGENT_EVALUATION_SUMMARY_VIEW", "AGENT_EVALUATION_DETAIL_VIEW", "AGENT_QUEUE_DETAIL_VIEW", "AGENT_INTERACTION_DETAIL_VIEW", "ABANDON_INSIGHTS_VIEW", "SKILLS_PERFORMANCE_VIEW", "SURVEY_FORM_PERFORMANCE_SUMMARY_VIEW", "SURVEY_FORM_PERFORMANCE_DETAIL_VIEW", "DNIS_PERFORMANCE_SUMMARY_VIEW", "DNIS_PERFORMANCE_DETAIL_VIEW", "WRAP_UP_PERFORMANCE_SUMMARY_VIEW", "AGENT_WRAP_UP_PERFORMANCE_DETAIL_VIEW", "QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_ACTIVITY_DETAIL_VIEW", "AGENT_QUEUE_ACTIVITY_SUMMARY_VIEW", "QUEUE_AGENT_DETAIL_VIEW", "QUEUE_INTERACTION_DETAIL_VIEW", "AGENT_SCHEDULE_DETAIL_VIEW", "IVR_PERFORMANCE_SUMMARY_VIEW", "IVR_PERFORMANCE_DETAIL_VIEW", "ANSWER_INSIGHTS_VIEW", "HANDLE_INSIGHTS_VIEW", "TALK_INSIGHTS_VIEW", "HOLD_INSIGHTS_VIEW", "ACW_INSIGHTS_VIEW", "WAIT_INSIGHTS_VIEW", "AGENT_WRAP_UP_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_OUTCOME_SUMMARY_VIEW", "FLOW_OUTCOME_PERFORMANCE_DETAIL_VIEW", "FLOW_OUTCOME_PERFORMANCE_INTERVAL_DETAIL_VIEW", "FLOW_DESTINATION_SUMMARY_VIEW", "FLOW_DESTINATION_DETAIL_VIEW", "API_USAGE_VIEW", "SCHEDULED_CALLBACKS_VIEW", "CONTENT_SEARCH_VIEW", "LANDING_PAGE", "DASHBOARD_SUMMARY", "DASHBOARD_DETAIL", "JOURNEY_ACTION_MAP_SUMMARY_VIEW", "JOURNEY_OUTCOME_SUMMARY_VIEW", "JOURNEY_SEGMENT_SUMMARY_VIEW", "AGENT_DEVELOPMENT_DETAIL_VIEW", "AGENT_DEVELOPMENT_DETAIL_ME_VIEW", "AGENT_DEVELOPMENT_SUMMARY_VIEW", "AGENT_PERFORMANCE_ME_VIEW", "AGENT_STATUS_ME_VIEW", "AGENT_EVALUATION_ME_VIEW", "AGENT_SCORECARD_VIEW", "AGENT_SCORECARD_ME_VIEW", "AGENT_GAMIFICATION_LEADERSHIP_VIEW", "AGENT_SCHEDULE_ME_VIEW"]
        if view_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for view_type -> " + view_type)
            self._view_type = "outdated_sdk_version"
        else:
            self._view_type = view_type

    @property
    def export_error_messages_type(self):
        """
        Gets the export_error_messages_type of this ReportingExportJobResponse.
        The error message in case the export request failed

        :return: The export_error_messages_type of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._export_error_messages_type

    @export_error_messages_type.setter
    def export_error_messages_type(self, export_error_messages_type):
        """
        Sets the export_error_messages_type of this ReportingExportJobResponse.
        The error message in case the export request failed

        :param export_error_messages_type: The export_error_messages_type of this ReportingExportJobResponse.
        :type: str
        """
        allowed_values = ["FAILED_CONVERTING_EXPORT_JOB", "FAILED_NO_DATA_EXPORT_JOB_FOUND", "FAILED_GETTING_DATA_FROM_SERVICE", "FAILED_GENERATING_TEMP_FILE", "FAILED_SAVING_FILE_TO_S3", "FAILED_NOTIFYING_SKYWALKER_OF_DOWNLOAD", "FAILED_BUILDING_DOWNLOAD_URL_FROM_SKYWALKER_RESPONSE", "FAILED_CONVERTING_EXPORT_JOB_TO_QUEUE_PERFORMANCE_JOB", "EXPORT_TYPE_NOT_IMPLEMENTED", "REACHED_MAXIMUM_ATTEMPT_OF_RETRY", "FAILED_LONG_RUNNING_EXPORT", "TOO_MANY_REQUESTS_FROM_AN_ORGANIZATION", "FAILED_AS_EXPORT_FILE_SIZE_IS_GREATER_THAN_10MB", "NOT_AUTHORIZED_TO_VIEW_EXPORT"]
        if export_error_messages_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for export_error_messages_type -> " + export_error_messages_type)
            self._export_error_messages_type = "outdated_sdk_version"
        else:
            self._export_error_messages_type = export_error_messages_type

    @property
    def period(self):
        """
        Gets the period of this ReportingExportJobResponse.
        The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The period of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this ReportingExportJobResponse.
        The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param period: The period of this ReportingExportJobResponse.
        :type: str
        """
        
        self._period = period

    @property
    def filter(self):
        """
        Gets the filter of this ReportingExportJobResponse.
        Filters to apply to create the view

        :return: The filter of this ReportingExportJobResponse.
        :rtype: ViewFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this ReportingExportJobResponse.
        Filters to apply to create the view

        :param filter: The filter of this ReportingExportJobResponse.
        :type: ViewFilter
        """
        
        self._filter = filter

    @property
    def read(self):
        """
        Gets the read of this ReportingExportJobResponse.
        Indicates if the request has been marked as read

        :return: The read of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this ReportingExportJobResponse.
        Indicates if the request has been marked as read

        :param read: The read of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._read = read

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this ReportingExportJobResponse.
        The created date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date_time of this ReportingExportJobResponse.
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this ReportingExportJobResponse.
        The created date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date_time: The created_date_time of this ReportingExportJobResponse.
        :type: datetime
        """
        
        self._created_date_time = created_date_time

    @property
    def modified_date_time(self):
        """
        Gets the modified_date_time of this ReportingExportJobResponse.
        The last modified date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date_time of this ReportingExportJobResponse.
        :rtype: datetime
        """
        return self._modified_date_time

    @modified_date_time.setter
    def modified_date_time(self, modified_date_time):
        """
        Sets the modified_date_time of this ReportingExportJobResponse.
        The last modified date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date_time: The modified_date_time of this ReportingExportJobResponse.
        :type: datetime
        """
        
        self._modified_date_time = modified_date_time

    @property
    def locale(self):
        """
        Gets the locale of this ReportingExportJobResponse.
        The locale use for localization of the exported data, i.e. en-us, es-mx  

        :return: The locale of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this ReportingExportJobResponse.
        The locale use for localization of the exported data, i.e. en-us, es-mx  

        :param locale: The locale of this ReportingExportJobResponse.
        :type: str
        """
        
        self._locale = locale

    @property
    def percentage_complete(self):
        """
        Gets the percentage_complete of this ReportingExportJobResponse.
        The percentage of the job that has completed processing

        :return: The percentage_complete of this ReportingExportJobResponse.
        :rtype: float
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        """
        Sets the percentage_complete of this ReportingExportJobResponse.
        The percentage of the job that has completed processing

        :param percentage_complete: The percentage_complete of this ReportingExportJobResponse.
        :type: float
        """
        
        self._percentage_complete = percentage_complete

    @property
    def has_format_durations(self):
        """
        Gets the has_format_durations of this ReportingExportJobResponse.
        Indicates if durations are formatted in hh:mm:ss format instead of ms

        :return: The has_format_durations of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._has_format_durations

    @has_format_durations.setter
    def has_format_durations(self, has_format_durations):
        """
        Sets the has_format_durations of this ReportingExportJobResponse.
        Indicates if durations are formatted in hh:mm:ss format instead of ms

        :param has_format_durations: The has_format_durations of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._has_format_durations = has_format_durations

    @property
    def has_split_filters(self):
        """
        Gets the has_split_filters of this ReportingExportJobResponse.
        Indicates if filters will be split in aggregate detail exports

        :return: The has_split_filters of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._has_split_filters

    @has_split_filters.setter
    def has_split_filters(self, has_split_filters):
        """
        Sets the has_split_filters of this ReportingExportJobResponse.
        Indicates if filters will be split in aggregate detail exports

        :param has_split_filters: The has_split_filters of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._has_split_filters = has_split_filters

    @property
    def exclude_empty_rows(self):
        """
        Gets the exclude_empty_rows of this ReportingExportJobResponse.
        Excludes empty rows from the exports

        :return: The exclude_empty_rows of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._exclude_empty_rows

    @exclude_empty_rows.setter
    def exclude_empty_rows(self, exclude_empty_rows):
        """
        Sets the exclude_empty_rows of this ReportingExportJobResponse.
        Excludes empty rows from the exports

        :param exclude_empty_rows: The exclude_empty_rows of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._exclude_empty_rows = exclude_empty_rows

    @property
    def has_split_by_media(self):
        """
        Gets the has_split_by_media of this ReportingExportJobResponse.
        Indicates if media type will be split in aggregate detail exports

        :return: The has_split_by_media of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._has_split_by_media

    @has_split_by_media.setter
    def has_split_by_media(self, has_split_by_media):
        """
        Sets the has_split_by_media of this ReportingExportJobResponse.
        Indicates if media type will be split in aggregate detail exports

        :param has_split_by_media: The has_split_by_media of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._has_split_by_media = has_split_by_media

    @property
    def has_summary_row(self):
        """
        Gets the has_summary_row of this ReportingExportJobResponse.
        Indicates if summary row needs to be present in exports

        :return: The has_summary_row of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._has_summary_row

    @has_summary_row.setter
    def has_summary_row(self, has_summary_row):
        """
        Sets the has_summary_row of this ReportingExportJobResponse.
        Indicates if summary row needs to be present in exports

        :param has_summary_row: The has_summary_row of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._has_summary_row = has_summary_row

    @property
    def csv_delimiter(self):
        """
        Gets the csv_delimiter of this ReportingExportJobResponse.
        The user supplied csv delimiter string value either of type 'comma' or 'semicolon' permitted for the export request

        :return: The csv_delimiter of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._csv_delimiter

    @csv_delimiter.setter
    def csv_delimiter(self, csv_delimiter):
        """
        Sets the csv_delimiter of this ReportingExportJobResponse.
        The user supplied csv delimiter string value either of type 'comma' or 'semicolon' permitted for the export request

        :param csv_delimiter: The csv_delimiter of this ReportingExportJobResponse.
        :type: str
        """
        allowed_values = ["SEMICOLON", "COMMA"]
        if csv_delimiter.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for csv_delimiter -> " + csv_delimiter)
            self._csv_delimiter = "outdated_sdk_version"
        else:
            self._csv_delimiter = csv_delimiter

    @property
    def selected_columns(self):
        """
        Gets the selected_columns of this ReportingExportJobResponse.
        The list of ordered selected columns from the export view by the user

        :return: The selected_columns of this ReportingExportJobResponse.
        :rtype: list[SelectedColumns]
        """
        return self._selected_columns

    @selected_columns.setter
    def selected_columns(self, selected_columns):
        """
        Sets the selected_columns of this ReportingExportJobResponse.
        The list of ordered selected columns from the export view by the user

        :param selected_columns: The selected_columns of this ReportingExportJobResponse.
        :type: list[SelectedColumns]
        """
        
        self._selected_columns = selected_columns

    @property
    def has_custom_participant_attributes(self):
        """
        Gets the has_custom_participant_attributes of this ReportingExportJobResponse.
        Indicates if custom participant attributes will be exported

        :return: The has_custom_participant_attributes of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._has_custom_participant_attributes

    @has_custom_participant_attributes.setter
    def has_custom_participant_attributes(self, has_custom_participant_attributes):
        """
        Sets the has_custom_participant_attributes of this ReportingExportJobResponse.
        Indicates if custom participant attributes will be exported

        :param has_custom_participant_attributes: The has_custom_participant_attributes of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._has_custom_participant_attributes = has_custom_participant_attributes

    @property
    def recipient_emails(self):
        """
        Gets the recipient_emails of this ReportingExportJobResponse.
        The list of email recipients for the exports

        :return: The recipient_emails of this ReportingExportJobResponse.
        :rtype: list[str]
        """
        return self._recipient_emails

    @recipient_emails.setter
    def recipient_emails(self, recipient_emails):
        """
        Sets the recipient_emails of this ReportingExportJobResponse.
        The list of email recipients for the exports

        :param recipient_emails: The recipient_emails of this ReportingExportJobResponse.
        :type: list[str]
        """
        
        self._recipient_emails = recipient_emails

    @property
    def email_statuses(self):
        """
        Gets the email_statuses of this ReportingExportJobResponse.
        The status of individual email addresses as a map

        :return: The email_statuses of this ReportingExportJobResponse.
        :rtype: dict(str, str)
        """
        return self._email_statuses

    @email_statuses.setter
    def email_statuses(self, email_statuses):
        """
        Sets the email_statuses of this ReportingExportJobResponse.
        The status of individual email addresses as a map

        :param email_statuses: The email_statuses of this ReportingExportJobResponse.
        :type: dict(str, str)
        """
        
        self._email_statuses = email_statuses

    @property
    def email_error_description(self):
        """
        Gets the email_error_description of this ReportingExportJobResponse.
        The optional error message in case the export fail to email

        :return: The email_error_description of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._email_error_description

    @email_error_description.setter
    def email_error_description(self, email_error_description):
        """
        Sets the email_error_description of this ReportingExportJobResponse.
        The optional error message in case the export fail to email

        :param email_error_description: The email_error_description of this ReportingExportJobResponse.
        :type: str
        """
        
        self._email_error_description = email_error_description

    @property
    def enabled(self):
        """
        Gets the enabled of this ReportingExportJobResponse.


        :return: The enabled of this ReportingExportJobResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ReportingExportJobResponse.


        :param enabled: The enabled of this ReportingExportJobResponse.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def self_uri(self):
        """
        Gets the self_uri of this ReportingExportJobResponse.
        The URI for this object

        :return: The self_uri of this ReportingExportJobResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this ReportingExportJobResponse.
        The URI for this object

        :param self_uri: The self_uri of this ReportingExportJobResponse.
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

