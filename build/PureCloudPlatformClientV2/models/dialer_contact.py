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

class DialerContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'contact_list_id': 'str',
            'data': 'dict(str, object)',
            'call_records': 'dict(str, CallRecord)',
            'callable': 'bool',
            'phone_number_status': 'dict(str, PhoneNumberStatus)',
            'contact_column_time_zones': 'dict(str, ContactColumnTimeZone)',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'contact_list_id': 'contactListId',
            'data': 'data',
            'call_records': 'callRecords',
            'callable': 'callable',
            'phone_number_status': 'phoneNumberStatus',
            'contact_column_time_zones': 'contactColumnTimeZones',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._contact_list_id = None
        self._data = None
        self._call_records = None
        self._callable = None
        self._phone_number_status = None
        self._contact_column_time_zones = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this DialerContact.
        The globally unique identifier for the object.

        :return: The id of this DialerContact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DialerContact.
        The globally unique identifier for the object.

        :param id: The id of this DialerContact.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DialerContact.


        :return: The name of this DialerContact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DialerContact.


        :param name: The name of this DialerContact.
        :type: str
        """
        
        self._name = name

    @property
    def contact_list_id(self):
        """
        Gets the contact_list_id of this DialerContact.
        The identifier of the contact list containing this contact.

        :return: The contact_list_id of this DialerContact.
        :rtype: str
        """
        return self._contact_list_id

    @contact_list_id.setter
    def contact_list_id(self, contact_list_id):
        """
        Sets the contact_list_id of this DialerContact.
        The identifier of the contact list containing this contact.

        :param contact_list_id: The contact_list_id of this DialerContact.
        :type: str
        """
        
        self._contact_list_id = contact_list_id

    @property
    def data(self):
        """
        Gets the data of this DialerContact.
        An ordered map of the contact's columns and corresponding values.

        :return: The data of this DialerContact.
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DialerContact.
        An ordered map of the contact's columns and corresponding values.

        :param data: The data of this DialerContact.
        :type: dict(str, object)
        """
        
        self._data = data

    @property
    def call_records(self):
        """
        Gets the call_records of this DialerContact.
        A map of call records for the contact phone columns.

        :return: The call_records of this DialerContact.
        :rtype: dict(str, CallRecord)
        """
        return self._call_records

    @call_records.setter
    def call_records(self, call_records):
        """
        Sets the call_records of this DialerContact.
        A map of call records for the contact phone columns.

        :param call_records: The call_records of this DialerContact.
        :type: dict(str, CallRecord)
        """
        
        self._call_records = call_records

    @property
    def callable(self):
        """
        Gets the callable of this DialerContact.
        Indicates whether or not the contact can be called.

        :return: The callable of this DialerContact.
        :rtype: bool
        """
        return self._callable

    @callable.setter
    def callable(self, callable):
        """
        Sets the callable of this DialerContact.
        Indicates whether or not the contact can be called.

        :param callable: The callable of this DialerContact.
        :type: bool
        """
        
        self._callable = callable

    @property
    def phone_number_status(self):
        """
        Gets the phone_number_status of this DialerContact.
        A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not.

        :return: The phone_number_status of this DialerContact.
        :rtype: dict(str, PhoneNumberStatus)
        """
        return self._phone_number_status

    @phone_number_status.setter
    def phone_number_status(self, phone_number_status):
        """
        Sets the phone_number_status of this DialerContact.
        A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not.

        :param phone_number_status: The phone_number_status of this DialerContact.
        :type: dict(str, PhoneNumberStatus)
        """
        
        self._phone_number_status = phone_number_status

    @property
    def contact_column_time_zones(self):
        """
        Gets the contact_column_time_zones of this DialerContact.
        Map containing data about the timezone the contact is mapped to. This will only be populated if the contact list has automatic timezone mapping turned on. The key is the column name. The value is the timezone it mapped to and the type of column: Phone or Zip

        :return: The contact_column_time_zones of this DialerContact.
        :rtype: dict(str, ContactColumnTimeZone)
        """
        return self._contact_column_time_zones

    @contact_column_time_zones.setter
    def contact_column_time_zones(self, contact_column_time_zones):
        """
        Sets the contact_column_time_zones of this DialerContact.
        Map containing data about the timezone the contact is mapped to. This will only be populated if the contact list has automatic timezone mapping turned on. The key is the column name. The value is the timezone it mapped to and the type of column: Phone or Zip

        :param contact_column_time_zones: The contact_column_time_zones of this DialerContact.
        :type: dict(str, ContactColumnTimeZone)
        """
        
        self._contact_column_time_zones = contact_column_time_zones

    @property
    def self_uri(self):
        """
        Gets the self_uri of this DialerContact.
        The URI for this object

        :return: The self_uri of this DialerContact.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this DialerContact.
        The URI for this object

        :param self_uri: The self_uri of this DialerContact.
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

