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


class Survey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Survey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'conversation': 'Conversation',
            'survey_form': 'SurveyForm',
            'agent': 'UriReference',
            'status': 'str',
            'queue': 'QueueReference',
            'answers': 'SurveyScoringSet',
            'completed_date': 'datetime',
            'survey_error_details': 'SurveyErrorDetails',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'conversation': 'conversation',
            'survey_form': 'surveyForm',
            'agent': 'agent',
            'status': 'status',
            'queue': 'queue',
            'answers': 'answers',
            'completed_date': 'completedDate',
            'survey_error_details': 'surveyErrorDetails',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._conversation = None
        self._survey_form = None
        self._agent = None
        self._status = None
        self._queue = None
        self._answers = None
        self._completed_date = None
        self._survey_error_details = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Survey.
        The globally unique identifier for the object.

        :return: The id of this Survey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Survey.
        The globally unique identifier for the object.

        :param id: The id of this Survey.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Survey.


        :return: The name of this Survey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Survey.


        :param name: The name of this Survey.
        :type: str
        """
        
        self._name = name

    @property
    def conversation(self):
        """
        Gets the conversation of this Survey.


        :return: The conversation of this Survey.
        :rtype: Conversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this Survey.


        :param conversation: The conversation of this Survey.
        :type: Conversation
        """
        
        self._conversation = conversation

    @property
    def survey_form(self):
        """
        Gets the survey_form of this Survey.
        Survey form used for this survey.

        :return: The survey_form of this Survey.
        :rtype: SurveyForm
        """
        return self._survey_form

    @survey_form.setter
    def survey_form(self, survey_form):
        """
        Sets the survey_form of this Survey.
        Survey form used for this survey.

        :param survey_form: The survey_form of this Survey.
        :type: SurveyForm
        """
        
        self._survey_form = survey_form

    @property
    def agent(self):
        """
        Gets the agent of this Survey.


        :return: The agent of this Survey.
        :rtype: UriReference
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """
        Sets the agent of this Survey.


        :param agent: The agent of this Survey.
        :type: UriReference
        """
        
        self._agent = agent

    @property
    def status(self):
        """
        Gets the status of this Survey.


        :return: The status of this Survey.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Survey.


        :param status: The status of this Survey.
        :type: str
        """
        allowed_values = ["Pending", "Sent", "InProgress", "Finished", "OptOut", "Error", "Expired"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def queue(self):
        """
        Gets the queue of this Survey.


        :return: The queue of this Survey.
        :rtype: QueueReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this Survey.


        :param queue: The queue of this Survey.
        :type: QueueReference
        """
        
        self._queue = queue

    @property
    def answers(self):
        """
        Gets the answers of this Survey.


        :return: The answers of this Survey.
        :rtype: SurveyScoringSet
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """
        Sets the answers of this Survey.


        :param answers: The answers of this Survey.
        :type: SurveyScoringSet
        """
        
        self._answers = answers

    @property
    def completed_date(self):
        """
        Gets the completed_date of this Survey.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The completed_date of this Survey.
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """
        Sets the completed_date of this Survey.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param completed_date: The completed_date of this Survey.
        :type: datetime
        """
        
        self._completed_date = completed_date

    @property
    def survey_error_details(self):
        """
        Gets the survey_error_details of this Survey.
        Additional information about what happened when the survey is in Error status.

        :return: The survey_error_details of this Survey.
        :rtype: SurveyErrorDetails
        """
        return self._survey_error_details

    @survey_error_details.setter
    def survey_error_details(self, survey_error_details):
        """
        Sets the survey_error_details of this Survey.
        Additional information about what happened when the survey is in Error status.

        :param survey_error_details: The survey_error_details of this Survey.
        :type: SurveyErrorDetails
        """
        
        self._survey_error_details = survey_error_details

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Survey.
        The URI for this object

        :return: The self_uri of this Survey.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Survey.
        The URI for this object

        :param self_uri: The self_uri of this Survey.
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

