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

class EventMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str',
            'message_with_params': 'str',
            'message_params': 'dict(str, object)',
            'documentation_uri': 'str',
            'resource_ur_is': 'list[str]'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'message_with_params': 'messageWithParams',
            'message_params': 'messageParams',
            'documentation_uri': 'documentationUri',
            'resource_ur_is': 'resourceURIs'
        }

        self._code = None
        self._message = None
        self._message_with_params = None
        self._message_params = None
        self._documentation_uri = None
        self._resource_ur_is = None

    @property
    def code(self):
        """
        Gets the code of this EventMessage.


        :return: The code of this EventMessage.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this EventMessage.


        :param code: The code of this EventMessage.
        :type: str
        """
        allowed_values = ["APPROACHING_CONTACT_LIMIT", "APPROACHING_DNC_LIST_PHONE_NUMBER_LIMIT", "APPROACHING_DNC_ORGANIZATION_PHONE_NUMBER_LIMIT", "APPROACHING_ENTITY_LIMIT", "AUTOMATIC_TIME_ZONE_ZIP_CODE_INVALID", "CAMPAIGN_CONTENT_TEMPLATE_SUBSTITUTION_MISMATCH", "CAMPAIGN_MESSAGE_CHARACTER_LIMIT_EXCEEDED", "CAMPAIGN_START_ERROR", "CAMPAIGN_RULE_START_ERROR", "CAMPAIGN_SET_DIALING_MODE_ERROR", "CAMPAIGN_STOPPED", "CAMPAIGN_THROTTLED", "CAMPAIGN_QUEUE_MEMBERS_LIMIT_EXCEEDED", "INVALID_CALLABLE_TIME_ZONE", "CALLBACK_CREATION_INVALID_NUMBER", "CALL_RULE_INVALID_CONTACT_COLUMN", "CALL_RULE_MISSING_DATA_ACTION_INPUT", "CALL_RULE_MISMATCH_TYPE", "CALL_RULE_INVALID_OPERATOR", "CALL_RULE_NO_DNC_LISTS_CONFIGURED", "CALL_RULE_UPDATED_PHONE_COLUMN", "CONTACT_LIST_FILTER_EVALUATION_FAILED", "CONTACT_LIST_FILTER_INTERNAL_ERROR", "CONTACT_COLUMNS_LIMIT_EXCEEDED", "CONTACT_COLUMN_LENGTH_LIMIT_EXCEEDED", "CONTACT_DATUM_LENGTH_LIMIT_EXCEEDED", "CONTACT_ZIP_CODE_COLUMN_VALUE_INVALID", "DATA_ACTION_EXECUTION_FAILED", "DATA_ACTION_AUTHENTICATION_FAILURE", "DATA_ACTION_NOT_FOUND", "DNC_AUTHENTICATION_FAILURE", "EXCEEDED_CONTACT_LIMIT", "EXCEEDED_DNC_RECORD_LIMIT", "INACTIVE_EDGES_FAILED_PLACE_CALLS", "INACTIVE_EDGES_TURNED_CAMPAIGN_OFF", "INVALID_PHONE_NUMBER", "IMPORT_FAILED_TO_READ_HEADERS", "IMPORT_COULD_NOT_PARSE_AN_ENTRY", "IMPORT_CONTACT_DOES_NOT_MATCH_LIST_FORMAT", "IMPORT_ENTRY_DOES_NOT_ALIGN_WITH_HEADERS", "IMPORT_INVALID_CUSTOM_ID", "IMPORT_INVALID_DATA", "IMPORT_COLUMN_EXCEEDS_LENGTH_LIMIT", "IMPORT_DATUM_EXCEEDS_LENGTH_LIMIT", "IMPORT_MISSING_CUSTOM_ID", "IMPORT_NO_COLUMNS_DEFINED", "IMPORT_COLUMNS_DO_NOT_EXIST_ON_LIST", "IMPORT_LIST_NO_LONGER_EXISTS", "IMPORT_FAILED_CONTACT_ZIP_CODE_COLUMN_VALUE_INVALID", "IMPORT_TOO_MANY_COLUMNS", "IMPORT_TOO_MANY_EXTRA_COLUMNS", "ORGANIZATION_HAS_NO_DOMAIN_SET", "RECYCLE_CAMPAIGN"]
        if code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for code -> " + code)
            self._code = "outdated_sdk_version"
        else:
            self._code = code

    @property
    def message(self):
        """
        Gets the message of this EventMessage.


        :return: The message of this EventMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this EventMessage.


        :param message: The message of this EventMessage.
        :type: str
        """
        
        self._message = message

    @property
    def message_with_params(self):
        """
        Gets the message_with_params of this EventMessage.


        :return: The message_with_params of this EventMessage.
        :rtype: str
        """
        return self._message_with_params

    @message_with_params.setter
    def message_with_params(self, message_with_params):
        """
        Sets the message_with_params of this EventMessage.


        :param message_with_params: The message_with_params of this EventMessage.
        :type: str
        """
        
        self._message_with_params = message_with_params

    @property
    def message_params(self):
        """
        Gets the message_params of this EventMessage.


        :return: The message_params of this EventMessage.
        :rtype: dict(str, object)
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params):
        """
        Sets the message_params of this EventMessage.


        :param message_params: The message_params of this EventMessage.
        :type: dict(str, object)
        """
        
        self._message_params = message_params

    @property
    def documentation_uri(self):
        """
        Gets the documentation_uri of this EventMessage.


        :return: The documentation_uri of this EventMessage.
        :rtype: str
        """
        return self._documentation_uri

    @documentation_uri.setter
    def documentation_uri(self, documentation_uri):
        """
        Sets the documentation_uri of this EventMessage.


        :param documentation_uri: The documentation_uri of this EventMessage.
        :type: str
        """
        
        self._documentation_uri = documentation_uri

    @property
    def resource_ur_is(self):
        """
        Gets the resource_ur_is of this EventMessage.


        :return: The resource_ur_is of this EventMessage.
        :rtype: list[str]
        """
        return self._resource_ur_is

    @resource_ur_is.setter
    def resource_ur_is(self, resource_ur_is):
        """
        Sets the resource_ur_is of this EventMessage.


        :param resource_ur_is: The resource_ur_is of this EventMessage.
        :type: list[str]
        """
        
        self._resource_ur_is = resource_ur_is

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

