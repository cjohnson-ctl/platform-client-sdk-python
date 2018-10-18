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


class AnalyticsEvaluation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsEvaluation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'evaluation_id': 'str',
            'evaluator_id': 'str',
            'user_id': 'str',
            'event_time': 'datetime',
            'queue_id': 'str',
            'form_id': 'str',
            'context_id': 'str',
            'form_name': 'str',
            'geto_total_score': 'int',
            'geto_total_critical_score': 'int'
        }

        self.attribute_map = {
            'evaluation_id': 'evaluationId',
            'evaluator_id': 'evaluatorId',
            'user_id': 'userId',
            'event_time': 'eventTime',
            'queue_id': 'queueId',
            'form_id': 'formId',
            'context_id': 'contextId',
            'form_name': 'formName',
            'geto_total_score': 'getoTotalScore',
            'geto_total_critical_score': 'getoTotalCriticalScore'
        }

        self._evaluation_id = None
        self._evaluator_id = None
        self._user_id = None
        self._event_time = None
        self._queue_id = None
        self._form_id = None
        self._context_id = None
        self._form_name = None
        self._geto_total_score = None
        self._geto_total_critical_score = None

    @property
    def evaluation_id(self):
        """
        Gets the evaluation_id of this AnalyticsEvaluation.
        Unique identifier for the evaluation

        :return: The evaluation_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, evaluation_id):
        """
        Sets the evaluation_id of this AnalyticsEvaluation.
        Unique identifier for the evaluation

        :param evaluation_id: The evaluation_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._evaluation_id = evaluation_id

    @property
    def evaluator_id(self):
        """
        Gets the evaluator_id of this AnalyticsEvaluation.
        A unique identifier of the PureCloud user who evaluated the interaction

        :return: The evaluator_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        """
        Sets the evaluator_id of this AnalyticsEvaluation.
        A unique identifier of the PureCloud user who evaluated the interaction

        :param evaluator_id: The evaluator_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._evaluator_id = evaluator_id

    @property
    def user_id(self):
        """
        Gets the user_id of this AnalyticsEvaluation.
        Unique identifier for the user being evaluated

        :return: The user_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AnalyticsEvaluation.
        Unique identifier for the user being evaluated

        :param user_id: The user_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def event_time(self):
        """
        Gets the event_time of this AnalyticsEvaluation.
        Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The event_time of this AnalyticsEvaluation.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this AnalyticsEvaluation.
        Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param event_time: The event_time of this AnalyticsEvaluation.
        :type: datetime
        """
        
        self._event_time = event_time

    @property
    def queue_id(self):
        """
        Gets the queue_id of this AnalyticsEvaluation.
        Unique identifier for the queue the conversation was on

        :return: The queue_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this AnalyticsEvaluation.
        Unique identifier for the queue the conversation was on

        :param queue_id: The queue_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def form_id(self):
        """
        Gets the form_id of this AnalyticsEvaluation.
        Unique identifier for the form used to evaluate the conversation/agent

        :return: The form_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """
        Sets the form_id of this AnalyticsEvaluation.
        Unique identifier for the form used to evaluate the conversation/agent

        :param form_id: The form_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._form_id = form_id

    @property
    def context_id(self):
        """
        Gets the context_id of this AnalyticsEvaluation.
        A unique identifier for an evaluation form, regardless of version

        :return: The context_id of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this AnalyticsEvaluation.
        A unique identifier for an evaluation form, regardless of version

        :param context_id: The context_id of this AnalyticsEvaluation.
        :type: str
        """
        
        self._context_id = context_id

    @property
    def form_name(self):
        """
        Gets the form_name of this AnalyticsEvaluation.
        Name of the evaluation form

        :return: The form_name of this AnalyticsEvaluation.
        :rtype: str
        """
        return self._form_name

    @form_name.setter
    def form_name(self, form_name):
        """
        Sets the form_name of this AnalyticsEvaluation.
        Name of the evaluation form

        :param form_name: The form_name of this AnalyticsEvaluation.
        :type: str
        """
        
        self._form_name = form_name

    @property
    def geto_total_score(self):
        """
        Gets the geto_total_score of this AnalyticsEvaluation.
        The total evaluation for interactions

        :return: The geto_total_score of this AnalyticsEvaluation.
        :rtype: int
        """
        return self._geto_total_score

    @geto_total_score.setter
    def geto_total_score(self, geto_total_score):
        """
        Sets the geto_total_score of this AnalyticsEvaluation.
        The total evaluation for interactions

        :param geto_total_score: The geto_total_score of this AnalyticsEvaluation.
        :type: int
        """
        
        self._geto_total_score = geto_total_score

    @property
    def geto_total_critical_score(self):
        """
        Gets the geto_total_critical_score of this AnalyticsEvaluation.
        The score for critical evaluation questions

        :return: The geto_total_critical_score of this AnalyticsEvaluation.
        :rtype: int
        """
        return self._geto_total_critical_score

    @geto_total_critical_score.setter
    def geto_total_critical_score(self, geto_total_critical_score):
        """
        Sets the geto_total_critical_score of this AnalyticsEvaluation.
        The score for critical evaluation questions

        :param geto_total_critical_score: The geto_total_critical_score of this AnalyticsEvaluation.
        :type: int
        """
        
        self._geto_total_critical_score = geto_total_critical_score

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

