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

class PhoneStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PhoneStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'operational_status': 'str',
            'edges_status': 'str',
            'event_creation_time': 'str',
            'provision': 'ProvisionInfo',
            'line_statuses': 'list[LineStatus]',
            'phone_assignment_to_edge_type': 'str',
            'edge': 'UriReference',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'operational_status': 'operationalStatus',
            'edges_status': 'edgesStatus',
            'event_creation_time': 'eventCreationTime',
            'provision': 'provision',
            'line_statuses': 'lineStatuses',
            'phone_assignment_to_edge_type': 'phoneAssignmentToEdgeType',
            'edge': 'edge',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._operational_status = None
        self._edges_status = None
        self._event_creation_time = None
        self._provision = None
        self._line_statuses = None
        self._phone_assignment_to_edge_type = None
        self._edge = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this PhoneStatus.
        The globally unique identifier for the object.

        :return: The id of this PhoneStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PhoneStatus.
        The globally unique identifier for the object.

        :param id: The id of this PhoneStatus.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PhoneStatus.


        :return: The name of this PhoneStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PhoneStatus.


        :param name: The name of this PhoneStatus.
        :type: str
        """
        
        self._name = name

    @property
    def operational_status(self):
        """
        Gets the operational_status of this PhoneStatus.
        The Operational Status of this phone

        :return: The operational_status of this PhoneStatus.
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """
        Sets the operational_status of this PhoneStatus.
        The Operational Status of this phone

        :param operational_status: The operational_status of this PhoneStatus.
        :type: str
        """
        allowed_values = ["OPERATIONAL", "DEGRADED", "OFFLINE"]
        if operational_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for operational_status -> " + operational_status
            self._operational_status = "outdated_sdk_version"
        else:
            self._operational_status = operational_status

    @property
    def edges_status(self):
        """
        Gets the edges_status of this PhoneStatus.
        The status of the primary or secondary Edges assigned to the phone lines.

        :return: The edges_status of this PhoneStatus.
        :rtype: str
        """
        return self._edges_status

    @edges_status.setter
    def edges_status(self, edges_status):
        """
        Sets the edges_status of this PhoneStatus.
        The status of the primary or secondary Edges assigned to the phone lines.

        :param edges_status: The edges_status of this PhoneStatus.
        :type: str
        """
        allowed_values = ["IN_SERVICE", "MIXED_SERVICE", "OUT_OF_SERVICE", "NO_EDGES"]
        if edges_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for edges_status -> " + edges_status
            self._edges_status = "outdated_sdk_version"
        else:
            self._edges_status = edges_status

    @property
    def event_creation_time(self):
        """
        Gets the event_creation_time of this PhoneStatus.
        Event Creation Time represents an ISO-8601 string. For example: UTC, UTC+01:00, or Europe/London

        :return: The event_creation_time of this PhoneStatus.
        :rtype: str
        """
        return self._event_creation_time

    @event_creation_time.setter
    def event_creation_time(self, event_creation_time):
        """
        Sets the event_creation_time of this PhoneStatus.
        Event Creation Time represents an ISO-8601 string. For example: UTC, UTC+01:00, or Europe/London

        :param event_creation_time: The event_creation_time of this PhoneStatus.
        :type: str
        """
        
        self._event_creation_time = event_creation_time

    @property
    def provision(self):
        """
        Gets the provision of this PhoneStatus.
        Provision information for this phone

        :return: The provision of this PhoneStatus.
        :rtype: ProvisionInfo
        """
        return self._provision

    @provision.setter
    def provision(self, provision):
        """
        Sets the provision of this PhoneStatus.
        Provision information for this phone

        :param provision: The provision of this PhoneStatus.
        :type: ProvisionInfo
        """
        
        self._provision = provision

    @property
    def line_statuses(self):
        """
        Gets the line_statuses of this PhoneStatus.
        A list of LineStatus information for each of the lines of this phone

        :return: The line_statuses of this PhoneStatus.
        :rtype: list[LineStatus]
        """
        return self._line_statuses

    @line_statuses.setter
    def line_statuses(self, line_statuses):
        """
        Sets the line_statuses of this PhoneStatus.
        A list of LineStatus information for each of the lines of this phone

        :param line_statuses: The line_statuses of this PhoneStatus.
        :type: list[LineStatus]
        """
        
        self._line_statuses = line_statuses

    @property
    def phone_assignment_to_edge_type(self):
        """
        Gets the phone_assignment_to_edge_type of this PhoneStatus.
        The phone status's edge assignment type.

        :return: The phone_assignment_to_edge_type of this PhoneStatus.
        :rtype: str
        """
        return self._phone_assignment_to_edge_type

    @phone_assignment_to_edge_type.setter
    def phone_assignment_to_edge_type(self, phone_assignment_to_edge_type):
        """
        Sets the phone_assignment_to_edge_type of this PhoneStatus.
        The phone status's edge assignment type.

        :param phone_assignment_to_edge_type: The phone_assignment_to_edge_type of this PhoneStatus.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY"]
        if phone_assignment_to_edge_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for phone_assignment_to_edge_type -> " + phone_assignment_to_edge_type
            self._phone_assignment_to_edge_type = "outdated_sdk_version"
        else:
            self._phone_assignment_to_edge_type = phone_assignment_to_edge_type

    @property
    def edge(self):
        """
        Gets the edge of this PhoneStatus.
        The URI of the edge that provided this status information.

        :return: The edge of this PhoneStatus.
        :rtype: UriReference
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        """
        Sets the edge of this PhoneStatus.
        The URI of the edge that provided this status information.

        :param edge: The edge of this PhoneStatus.
        :type: UriReference
        """
        
        self._edge = edge

    @property
    def self_uri(self):
        """
        Gets the self_uri of this PhoneStatus.
        The URI for this object

        :return: The self_uri of this PhoneStatus.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this PhoneStatus.
        The URI for this object

        :param self_uri: The self_uri of this PhoneStatus.
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

