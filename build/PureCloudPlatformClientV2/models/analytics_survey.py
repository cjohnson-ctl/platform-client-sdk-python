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

class AnalyticsSurvey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsSurvey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'survey_id': 'str',
            'survey_form_id': 'str',
            'survey_form_name': 'str',
            'survey_form_context_id': 'str',
            'event_time': 'datetime',
            'user_id': 'str',
            'queue_id': 'str',
            'survey_status': 'str',
            'survey_promoter_score': 'int',
            'survey_completed_date': 'datetime',
            'o_survey_total_score': 'int'
        }

        self.attribute_map = {
            'survey_id': 'surveyId',
            'survey_form_id': 'surveyFormId',
            'survey_form_name': 'surveyFormName',
            'survey_form_context_id': 'surveyFormContextId',
            'event_time': 'eventTime',
            'user_id': 'userId',
            'queue_id': 'queueId',
            'survey_status': 'surveyStatus',
            'survey_promoter_score': 'surveyPromoterScore',
            'survey_completed_date': 'surveyCompletedDate',
            'o_survey_total_score': 'oSurveyTotalScore'
        }

        self._survey_id = None
        self._survey_form_id = None
        self._survey_form_name = None
        self._survey_form_context_id = None
        self._event_time = None
        self._user_id = None
        self._queue_id = None
        self._survey_status = None
        self._survey_promoter_score = None
        self._survey_completed_date = None
        self._o_survey_total_score = None

    @property
    def survey_id(self):
        """
        Gets the survey_id of this AnalyticsSurvey.
        Unique identifier for the survey

        :return: The survey_id of this AnalyticsSurvey.
        :rtype: str
        """
        return self._survey_id

    @survey_id.setter
    def survey_id(self, survey_id):
        """
        Sets the survey_id of this AnalyticsSurvey.
        Unique identifier for the survey

        :param survey_id: The survey_id of this AnalyticsSurvey.
        :type: str
        """
        
        self._survey_id = survey_id

    @property
    def survey_form_id(self):
        """
        Gets the survey_form_id of this AnalyticsSurvey.
        Unique identifier for the survey form

        :return: The survey_form_id of this AnalyticsSurvey.
        :rtype: str
        """
        return self._survey_form_id

    @survey_form_id.setter
    def survey_form_id(self, survey_form_id):
        """
        Sets the survey_form_id of this AnalyticsSurvey.
        Unique identifier for the survey form

        :param survey_form_id: The survey_form_id of this AnalyticsSurvey.
        :type: str
        """
        
        self._survey_form_id = survey_form_id

    @property
    def survey_form_name(self):
        """
        Gets the survey_form_name of this AnalyticsSurvey.
        Name of the survey form

        :return: The survey_form_name of this AnalyticsSurvey.
        :rtype: str
        """
        return self._survey_form_name

    @survey_form_name.setter
    def survey_form_name(self, survey_form_name):
        """
        Sets the survey_form_name of this AnalyticsSurvey.
        Name of the survey form

        :param survey_form_name: The survey_form_name of this AnalyticsSurvey.
        :type: str
        """
        
        self._survey_form_name = survey_form_name

    @property
    def survey_form_context_id(self):
        """
        Gets the survey_form_context_id of this AnalyticsSurvey.
        Unique identifier for the survey form, regardless of version

        :return: The survey_form_context_id of this AnalyticsSurvey.
        :rtype: str
        """
        return self._survey_form_context_id

    @survey_form_context_id.setter
    def survey_form_context_id(self, survey_form_context_id):
        """
        Sets the survey_form_context_id of this AnalyticsSurvey.
        Unique identifier for the survey form, regardless of version

        :param survey_form_context_id: The survey_form_context_id of this AnalyticsSurvey.
        :type: str
        """
        
        self._survey_form_context_id = survey_form_context_id

    @property
    def event_time(self):
        """
        Gets the event_time of this AnalyticsSurvey.
        Specifies when a survey occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_time of this AnalyticsSurvey.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this AnalyticsSurvey.
        Specifies when a survey occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_time: The event_time of this AnalyticsSurvey.
        :type: datetime
        """
        
        self._event_time = event_time

    @property
    def user_id(self):
        """
        Gets the user_id of this AnalyticsSurvey.
        A unique identifier of the PureCloud user

        :return: The user_id of this AnalyticsSurvey.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AnalyticsSurvey.
        A unique identifier of the PureCloud user

        :param user_id: The user_id of this AnalyticsSurvey.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def queue_id(self):
        """
        Gets the queue_id of this AnalyticsSurvey.
        Unique identifier for the queue the conversation was on

        :return: The queue_id of this AnalyticsSurvey.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this AnalyticsSurvey.
        Unique identifier for the queue the conversation was on

        :param queue_id: The queue_id of this AnalyticsSurvey.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def survey_status(self):
        """
        Gets the survey_status of this AnalyticsSurvey.
        Survey status

        :return: The survey_status of this AnalyticsSurvey.
        :rtype: str
        """
        return self._survey_status

    @survey_status.setter
    def survey_status(self, survey_status):
        """
        Sets the survey_status of this AnalyticsSurvey.
        Survey status

        :param survey_status: The survey_status of this AnalyticsSurvey.
        :type: str
        """
        
        self._survey_status = survey_status

    @property
    def survey_promoter_score(self):
        """
        Gets the survey_promoter_score of this AnalyticsSurvey.
        Promoter score of the survey

        :return: The survey_promoter_score of this AnalyticsSurvey.
        :rtype: int
        """
        return self._survey_promoter_score

    @survey_promoter_score.setter
    def survey_promoter_score(self, survey_promoter_score):
        """
        Sets the survey_promoter_score of this AnalyticsSurvey.
        Promoter score of the survey

        :param survey_promoter_score: The survey_promoter_score of this AnalyticsSurvey.
        :type: int
        """
        
        self._survey_promoter_score = survey_promoter_score

    @property
    def survey_completed_date(self):
        """
        Gets the survey_completed_date of this AnalyticsSurvey.
        Completion date/time of the survey. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The survey_completed_date of this AnalyticsSurvey.
        :rtype: datetime
        """
        return self._survey_completed_date

    @survey_completed_date.setter
    def survey_completed_date(self, survey_completed_date):
        """
        Sets the survey_completed_date of this AnalyticsSurvey.
        Completion date/time of the survey. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param survey_completed_date: The survey_completed_date of this AnalyticsSurvey.
        :type: datetime
        """
        
        self._survey_completed_date = survey_completed_date

    @property
    def o_survey_total_score(self):
        """
        Gets the o_survey_total_score of this AnalyticsSurvey.


        :return: The o_survey_total_score of this AnalyticsSurvey.
        :rtype: int
        """
        return self._o_survey_total_score

    @o_survey_total_score.setter
    def o_survey_total_score(self, o_survey_total_score):
        """
        Sets the o_survey_total_score of this AnalyticsSurvey.


        :param o_survey_total_score: The o_survey_total_score of this AnalyticsSurvey.
        :type: int
        """
        
        self._o_survey_total_score = o_survey_total_score

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

