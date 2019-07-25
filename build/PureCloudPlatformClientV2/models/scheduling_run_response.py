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

class SchedulingRunResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SchedulingRunResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'run_id': 'str',
            'scheduler_run_id': 'str',
            'intraday_rescheduling': 'bool',
            'state': 'str',
            'percent_complete': 'float',
            'target_week': 'str',
            'schedule_id': 'str',
            'schedule_description': 'str',
            'scheduling_start_time': 'datetime',
            'scheduling_started_by': 'UserReference',
            'scheduling_canceled_by': 'UserReference',
            'scheduling_completed_time': 'datetime',
            'rescheduling_options': 'ReschedulingOptionsResponse',
            'rescheduling_result_expiration': 'datetime',
            'applied': 'bool',
            'unscheduled_agents': 'list[UnscheduledAgentWarning]'
        }

        self.attribute_map = {
            'run_id': 'runId',
            'scheduler_run_id': 'schedulerRunId',
            'intraday_rescheduling': 'intradayRescheduling',
            'state': 'state',
            'percent_complete': 'percentComplete',
            'target_week': 'targetWeek',
            'schedule_id': 'scheduleId',
            'schedule_description': 'scheduleDescription',
            'scheduling_start_time': 'schedulingStartTime',
            'scheduling_started_by': 'schedulingStartedBy',
            'scheduling_canceled_by': 'schedulingCanceledBy',
            'scheduling_completed_time': 'schedulingCompletedTime',
            'rescheduling_options': 'reschedulingOptions',
            'rescheduling_result_expiration': 'reschedulingResultExpiration',
            'applied': 'applied',
            'unscheduled_agents': 'unscheduledAgents'
        }

        self._run_id = None
        self._scheduler_run_id = None
        self._intraday_rescheduling = None
        self._state = None
        self._percent_complete = None
        self._target_week = None
        self._schedule_id = None
        self._schedule_description = None
        self._scheduling_start_time = None
        self._scheduling_started_by = None
        self._scheduling_canceled_by = None
        self._scheduling_completed_time = None
        self._rescheduling_options = None
        self._rescheduling_result_expiration = None
        self._applied = None
        self._unscheduled_agents = None

    @property
    def run_id(self):
        """
        Gets the run_id of this SchedulingRunResponse.
        ID of the schedule run

        :return: The run_id of this SchedulingRunResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """
        Sets the run_id of this SchedulingRunResponse.
        ID of the schedule run

        :param run_id: The run_id of this SchedulingRunResponse.
        :type: str
        """
        
        self._run_id = run_id

    @property
    def scheduler_run_id(self):
        """
        Gets the scheduler_run_id of this SchedulingRunResponse.
        The runId from scheduler service.  Useful for debugging schedule errors

        :return: The scheduler_run_id of this SchedulingRunResponse.
        :rtype: str
        """
        return self._scheduler_run_id

    @scheduler_run_id.setter
    def scheduler_run_id(self, scheduler_run_id):
        """
        Sets the scheduler_run_id of this SchedulingRunResponse.
        The runId from scheduler service.  Useful for debugging schedule errors

        :param scheduler_run_id: The scheduler_run_id of this SchedulingRunResponse.
        :type: str
        """
        
        self._scheduler_run_id = scheduler_run_id

    @property
    def intraday_rescheduling(self):
        """
        Gets the intraday_rescheduling of this SchedulingRunResponse.
        Whether this is the result of a rescheduling request

        :return: The intraday_rescheduling of this SchedulingRunResponse.
        :rtype: bool
        """
        return self._intraday_rescheduling

    @intraday_rescheduling.setter
    def intraday_rescheduling(self, intraday_rescheduling):
        """
        Sets the intraday_rescheduling of this SchedulingRunResponse.
        Whether this is the result of a rescheduling request

        :param intraday_rescheduling: The intraday_rescheduling of this SchedulingRunResponse.
        :type: bool
        """
        
        self._intraday_rescheduling = intraday_rescheduling

    @property
    def state(self):
        """
        Gets the state of this SchedulingRunResponse.
        Status of the schedule run

        :return: The state of this SchedulingRunResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this SchedulingRunResponse.
        Status of the schedule run

        :param state: The state of this SchedulingRunResponse.
        :type: str
        """
        allowed_values = ["None", "Queued", "Scheduling", "Canceled", "Failed", "Complete"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this SchedulingRunResponse.
        Completion percentage of the schedule run

        :return: The percent_complete of this SchedulingRunResponse.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this SchedulingRunResponse.
        Completion percentage of the schedule run

        :param percent_complete: The percent_complete of this SchedulingRunResponse.
        :type: float
        """
        
        self._percent_complete = percent_complete

    @property
    def target_week(self):
        """
        Gets the target_week of this SchedulingRunResponse.
        The start date of the week for which the scheduling is done in yyyy-MM-dd format

        :return: The target_week of this SchedulingRunResponse.
        :rtype: str
        """
        return self._target_week

    @target_week.setter
    def target_week(self, target_week):
        """
        Sets the target_week of this SchedulingRunResponse.
        The start date of the week for which the scheduling is done in yyyy-MM-dd format

        :param target_week: The target_week of this SchedulingRunResponse.
        :type: str
        """
        
        self._target_week = target_week

    @property
    def schedule_id(self):
        """
        Gets the schedule_id of this SchedulingRunResponse.
        ID of the schedule. Does not apply to reschedule, see reschedulingOptions.existingScheduleId

        :return: The schedule_id of this SchedulingRunResponse.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """
        Sets the schedule_id of this SchedulingRunResponse.
        ID of the schedule. Does not apply to reschedule, see reschedulingOptions.existingScheduleId

        :param schedule_id: The schedule_id of this SchedulingRunResponse.
        :type: str
        """
        
        self._schedule_id = schedule_id

    @property
    def schedule_description(self):
        """
        Gets the schedule_description of this SchedulingRunResponse.
        Description of the schedule

        :return: The schedule_description of this SchedulingRunResponse.
        :rtype: str
        """
        return self._schedule_description

    @schedule_description.setter
    def schedule_description(self, schedule_description):
        """
        Sets the schedule_description of this SchedulingRunResponse.
        Description of the schedule

        :param schedule_description: The schedule_description of this SchedulingRunResponse.
        :type: str
        """
        
        self._schedule_description = schedule_description

    @property
    def scheduling_start_time(self):
        """
        Gets the scheduling_start_time of this SchedulingRunResponse.
        Start time of the schedule run. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The scheduling_start_time of this SchedulingRunResponse.
        :rtype: datetime
        """
        return self._scheduling_start_time

    @scheduling_start_time.setter
    def scheduling_start_time(self, scheduling_start_time):
        """
        Sets the scheduling_start_time of this SchedulingRunResponse.
        Start time of the schedule run. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param scheduling_start_time: The scheduling_start_time of this SchedulingRunResponse.
        :type: datetime
        """
        
        self._scheduling_start_time = scheduling_start_time

    @property
    def scheduling_started_by(self):
        """
        Gets the scheduling_started_by of this SchedulingRunResponse.
        User that started the schedule run

        :return: The scheduling_started_by of this SchedulingRunResponse.
        :rtype: UserReference
        """
        return self._scheduling_started_by

    @scheduling_started_by.setter
    def scheduling_started_by(self, scheduling_started_by):
        """
        Sets the scheduling_started_by of this SchedulingRunResponse.
        User that started the schedule run

        :param scheduling_started_by: The scheduling_started_by of this SchedulingRunResponse.
        :type: UserReference
        """
        
        self._scheduling_started_by = scheduling_started_by

    @property
    def scheduling_canceled_by(self):
        """
        Gets the scheduling_canceled_by of this SchedulingRunResponse.
        User that canceled the schedule run

        :return: The scheduling_canceled_by of this SchedulingRunResponse.
        :rtype: UserReference
        """
        return self._scheduling_canceled_by

    @scheduling_canceled_by.setter
    def scheduling_canceled_by(self, scheduling_canceled_by):
        """
        Sets the scheduling_canceled_by of this SchedulingRunResponse.
        User that canceled the schedule run

        :param scheduling_canceled_by: The scheduling_canceled_by of this SchedulingRunResponse.
        :type: UserReference
        """
        
        self._scheduling_canceled_by = scheduling_canceled_by

    @property
    def scheduling_completed_time(self):
        """
        Gets the scheduling_completed_time of this SchedulingRunResponse.
        Time at which the scheduling run was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The scheduling_completed_time of this SchedulingRunResponse.
        :rtype: datetime
        """
        return self._scheduling_completed_time

    @scheduling_completed_time.setter
    def scheduling_completed_time(self, scheduling_completed_time):
        """
        Sets the scheduling_completed_time of this SchedulingRunResponse.
        Time at which the scheduling run was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param scheduling_completed_time: The scheduling_completed_time of this SchedulingRunResponse.
        :type: datetime
        """
        
        self._scheduling_completed_time = scheduling_completed_time

    @property
    def rescheduling_options(self):
        """
        Gets the rescheduling_options of this SchedulingRunResponse.
        The selected options for the reschedule request. Will always be null if intradayRescheduling is false

        :return: The rescheduling_options of this SchedulingRunResponse.
        :rtype: ReschedulingOptionsResponse
        """
        return self._rescheduling_options

    @rescheduling_options.setter
    def rescheduling_options(self, rescheduling_options):
        """
        Sets the rescheduling_options of this SchedulingRunResponse.
        The selected options for the reschedule request. Will always be null if intradayRescheduling is false

        :param rescheduling_options: The rescheduling_options of this SchedulingRunResponse.
        :type: ReschedulingOptionsResponse
        """
        
        self._rescheduling_options = rescheduling_options

    @property
    def rescheduling_result_expiration(self):
        """
        Gets the rescheduling_result_expiration of this SchedulingRunResponse.
        When the rescheduling result data will expire. Results are kept temporarily as they should be applied as soon as possible after the run finishes.  Will always be null if intradayRescheduling is false. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The rescheduling_result_expiration of this SchedulingRunResponse.
        :rtype: datetime
        """
        return self._rescheduling_result_expiration

    @rescheduling_result_expiration.setter
    def rescheduling_result_expiration(self, rescheduling_result_expiration):
        """
        Sets the rescheduling_result_expiration of this SchedulingRunResponse.
        When the rescheduling result data will expire. Results are kept temporarily as they should be applied as soon as possible after the run finishes.  Will always be null if intradayRescheduling is false. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param rescheduling_result_expiration: The rescheduling_result_expiration of this SchedulingRunResponse.
        :type: datetime
        """
        
        self._rescheduling_result_expiration = rescheduling_result_expiration

    @property
    def applied(self):
        """
        Gets the applied of this SchedulingRunResponse.
        Whether the rescheduling run has been marked applied

        :return: The applied of this SchedulingRunResponse.
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """
        Sets the applied of this SchedulingRunResponse.
        Whether the rescheduling run has been marked applied

        :param applied: The applied of this SchedulingRunResponse.
        :type: bool
        """
        
        self._applied = applied

    @property
    def unscheduled_agents(self):
        """
        Gets the unscheduled_agents of this SchedulingRunResponse.
        Agents that were not scheduled in the rescheduling operation. Will always be null if intradayRescheduling is false

        :return: The unscheduled_agents of this SchedulingRunResponse.
        :rtype: list[UnscheduledAgentWarning]
        """
        return self._unscheduled_agents

    @unscheduled_agents.setter
    def unscheduled_agents(self, unscheduled_agents):
        """
        Sets the unscheduled_agents of this SchedulingRunResponse.
        Agents that were not scheduled in the rescheduling operation. Will always be null if intradayRescheduling is false

        :param unscheduled_agents: The unscheduled_agents of this SchedulingRunResponse.
        :type: list[UnscheduledAgentWarning]
        """
        
        self._unscheduled_agents = unscheduled_agents

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

