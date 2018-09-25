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


class DependencyObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DependencyObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version': 'str',
            'type': 'str',
            'deleted': 'bool',
            'updated': 'bool',
            'state_unknown': 'bool',
            'consumed_resources': 'list[Dependency]',
            'consuming_resources': 'list[Dependency]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version': 'version',
            'type': 'type',
            'deleted': 'deleted',
            'updated': 'updated',
            'state_unknown': 'stateUnknown',
            'consumed_resources': 'consumedResources',
            'consuming_resources': 'consumingResources',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._version = None
        self._type = None
        self._deleted = None
        self._updated = None
        self._state_unknown = None
        self._consumed_resources = None
        self._consuming_resources = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this DependencyObject.
        The globally unique identifier for the object.

        :return: The id of this DependencyObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DependencyObject.
        The globally unique identifier for the object.

        :param id: The id of this DependencyObject.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DependencyObject.


        :return: The name of this DependencyObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DependencyObject.


        :param name: The name of this DependencyObject.
        :type: str
        """
        
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this DependencyObject.


        :return: The version of this DependencyObject.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DependencyObject.


        :param version: The version of this DependencyObject.
        :type: str
        """
        
        self._version = version

    @property
    def type(self):
        """
        Gets the type of this DependencyObject.


        :return: The type of this DependencyObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DependencyObject.


        :param type: The type of this DependencyObject.
        :type: str
        """
        allowed_values = ["ACDLANGUAGE", "ACDSKILL", "ACDWRAPUPCODE", "BRIDGEACTION", "COMPOSERSCRIPT", "CONTACTLIST", "DATAACTION", "DATATABLE", "EMAILROUTE", "EMERGENCYGROUP", "FLOWOUTCOME", "GROUP", "INBOUNDCALLFLOW", "INBOUNDEMAILFLOW", "INBOUNDSHORTMESSAGEFLOW", "INQUEUECALLFLOW", "IVRCONFIGURATION", "LANGUAGE", "LEXBOT", "LEXBOTALIAS", "OUTBOUNDCALLFLOW", "QUEUE", "RECORDINGPOLICY", "RESPONSE", "SCHEDULE", "SCHEDULEGROUP", "SECUREACTION", "SECURECALLFLOW", "SURVEYINVITEFLOW", "SYSTEMPROMPT", "TTSENGINE", "TTSVOICE", "USER", "USERPROMPT", "VOICEXML", "WORKFLOW"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def deleted(self):
        """
        Gets the deleted of this DependencyObject.


        :return: The deleted of this DependencyObject.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this DependencyObject.


        :param deleted: The deleted of this DependencyObject.
        :type: bool
        """
        
        self._deleted = deleted

    @property
    def updated(self):
        """
        Gets the updated of this DependencyObject.


        :return: The updated of this DependencyObject.
        :rtype: bool
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this DependencyObject.


        :param updated: The updated of this DependencyObject.
        :type: bool
        """
        
        self._updated = updated

    @property
    def state_unknown(self):
        """
        Gets the state_unknown of this DependencyObject.


        :return: The state_unknown of this DependencyObject.
        :rtype: bool
        """
        return self._state_unknown

    @state_unknown.setter
    def state_unknown(self, state_unknown):
        """
        Sets the state_unknown of this DependencyObject.


        :param state_unknown: The state_unknown of this DependencyObject.
        :type: bool
        """
        
        self._state_unknown = state_unknown

    @property
    def consumed_resources(self):
        """
        Gets the consumed_resources of this DependencyObject.


        :return: The consumed_resources of this DependencyObject.
        :rtype: list[Dependency]
        """
        return self._consumed_resources

    @consumed_resources.setter
    def consumed_resources(self, consumed_resources):
        """
        Sets the consumed_resources of this DependencyObject.


        :param consumed_resources: The consumed_resources of this DependencyObject.
        :type: list[Dependency]
        """
        
        self._consumed_resources = consumed_resources

    @property
    def consuming_resources(self):
        """
        Gets the consuming_resources of this DependencyObject.


        :return: The consuming_resources of this DependencyObject.
        :rtype: list[Dependency]
        """
        return self._consuming_resources

    @consuming_resources.setter
    def consuming_resources(self, consuming_resources):
        """
        Sets the consuming_resources of this DependencyObject.


        :param consuming_resources: The consuming_resources of this DependencyObject.
        :type: list[Dependency]
        """
        
        self._consuming_resources = consuming_resources

    @property
    def self_uri(self):
        """
        Gets the self_uri of this DependencyObject.
        The URI for this object

        :return: The self_uri of this DependencyObject.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this DependencyObject.
        The URI for this object

        :param self_uri: The self_uri of this DependencyObject.
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

