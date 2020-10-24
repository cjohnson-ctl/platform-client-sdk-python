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

class BulkUpdateShiftTradeStateResultItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BulkUpdateShiftTradeStateResultItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'reviewed_by': 'UserReference',
            'reviewed_date': 'datetime',
            'failure_reason': 'str',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'reviewed_by': 'reviewedBy',
            'reviewed_date': 'reviewedDate',
            'failure_reason': 'failureReason',
            'metadata': 'metadata'
        }

        self._id = None
        self._state = None
        self._reviewed_by = None
        self._reviewed_date = None
        self._failure_reason = None
        self._metadata = None

    @property
    def id(self):
        """
        Gets the id of this BulkUpdateShiftTradeStateResultItem.
        The globally unique identifier for the object.

        :return: The id of this BulkUpdateShiftTradeStateResultItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BulkUpdateShiftTradeStateResultItem.
        The globally unique identifier for the object.

        :param id: The id of this BulkUpdateShiftTradeStateResultItem.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this BulkUpdateShiftTradeStateResultItem.
        The state of the shift trade after the update request is processed

        :return: The state of this BulkUpdateShiftTradeStateResultItem.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BulkUpdateShiftTradeStateResultItem.
        The state of the shift trade after the update request is processed

        :param state: The state of this BulkUpdateShiftTradeStateResultItem.
        :type: str
        """
        allowed_values = ["Unmatched", "Matched", "Approved", "Denied", "Expired", "Canceled"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def reviewed_by(self):
        """
        Gets the reviewed_by of this BulkUpdateShiftTradeStateResultItem.
        The user who reviewed the request, if applicable

        :return: The reviewed_by of this BulkUpdateShiftTradeStateResultItem.
        :rtype: UserReference
        """
        return self._reviewed_by

    @reviewed_by.setter
    def reviewed_by(self, reviewed_by):
        """
        Sets the reviewed_by of this BulkUpdateShiftTradeStateResultItem.
        The user who reviewed the request, if applicable

        :param reviewed_by: The reviewed_by of this BulkUpdateShiftTradeStateResultItem.
        :type: UserReference
        """
        
        self._reviewed_by = reviewed_by

    @property
    def reviewed_date(self):
        """
        Gets the reviewed_date of this BulkUpdateShiftTradeStateResultItem.
        The date the request was reviewed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The reviewed_date of this BulkUpdateShiftTradeStateResultItem.
        :rtype: datetime
        """
        return self._reviewed_date

    @reviewed_date.setter
    def reviewed_date(self, reviewed_date):
        """
        Sets the reviewed_date of this BulkUpdateShiftTradeStateResultItem.
        The date the request was reviewed, if applicable. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param reviewed_date: The reviewed_date of this BulkUpdateShiftTradeStateResultItem.
        :type: datetime
        """
        
        self._reviewed_date = reviewed_date

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this BulkUpdateShiftTradeStateResultItem.
        The reason the update failed, if applicable

        :return: The failure_reason of this BulkUpdateShiftTradeStateResultItem.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this BulkUpdateShiftTradeStateResultItem.
        The reason the update failed, if applicable

        :param failure_reason: The failure_reason of this BulkUpdateShiftTradeStateResultItem.
        :type: str
        """
        allowed_values = ["InitiatingAgentScheduleNotFound", "InitiatingAgentShiftHasExternalActivities", "InitiatingAgentShiftNotFound", "ReceivingAgentNotFound", "ReceivingAgentScheduleNotFound", "ReceivingAgentShiftHasExternalActivities", "ReceivingAgentShiftNotFound", "ScheduleNotPublished", "TransitionNotAllowed"]
        if failure_reason.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for failure_reason -> " + failure_reason
            self._failure_reason = "outdated_sdk_version"
        else:
            self._failure_reason = failure_reason

    @property
    def metadata(self):
        """
        Gets the metadata of this BulkUpdateShiftTradeStateResultItem.
        Version metadata for the shift trade

        :return: The metadata of this BulkUpdateShiftTradeStateResultItem.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this BulkUpdateShiftTradeStateResultItem.
        Version metadata for the shift trade

        :param metadata: The metadata of this BulkUpdateShiftTradeStateResultItem.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

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

