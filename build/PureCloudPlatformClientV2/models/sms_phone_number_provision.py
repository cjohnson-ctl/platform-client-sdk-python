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

class SmsPhoneNumberProvision(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SmsPhoneNumberProvision - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'phone_number': 'str',
            'phone_number_type': 'str',
            'country_code': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'phone_number': 'phoneNumber',
            'phone_number_type': 'phoneNumberType',
            'country_code': 'countryCode',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._phone_number = None
        self._phone_number_type = None
        self._country_code = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this SmsPhoneNumberProvision.
        The globally unique identifier for the object.

        :return: The id of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SmsPhoneNumberProvision.
        The globally unique identifier for the object.

        :param id: The id of this SmsPhoneNumberProvision.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SmsPhoneNumberProvision.


        :return: The name of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SmsPhoneNumberProvision.


        :param name: The name of this SmsPhoneNumberProvision.
        :type: str
        """
        
        self._name = name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this SmsPhoneNumberProvision.
        A phone number to be used for SMS communications. E.g. +13175555555 or +34234234234

        :return: The phone_number of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this SmsPhoneNumberProvision.
        A phone number to be used for SMS communications. E.g. +13175555555 or +34234234234

        :param phone_number: The phone_number of this SmsPhoneNumberProvision.
        :type: str
        """
        
        self._phone_number = phone_number

    @property
    def phone_number_type(self):
        """
        Gets the phone_number_type of this SmsPhoneNumberProvision.
        Type of the phone number provisioned.

        :return: The phone_number_type of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._phone_number_type

    @phone_number_type.setter
    def phone_number_type(self, phone_number_type):
        """
        Sets the phone_number_type of this SmsPhoneNumberProvision.
        Type of the phone number provisioned.

        :param phone_number_type: The phone_number_type of this SmsPhoneNumberProvision.
        :type: str
        """
        allowed_values = ["local", "mobile", "tollfree", "shortcode"]
        if phone_number_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for phone_number_type -> " + phone_number_type
            self._phone_number_type = "outdated_sdk_version"
        else:
            self._phone_number_type = phone_number_type

    @property
    def country_code(self):
        """
        Gets the country_code of this SmsPhoneNumberProvision.
        The ISO 3166-1 alpha-2 country code of the country this phone number is associated with.

        :return: The country_code of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this SmsPhoneNumberProvision.
        The ISO 3166-1 alpha-2 country code of the country this phone number is associated with.

        :param country_code: The country_code of this SmsPhoneNumberProvision.
        :type: str
        """
        
        self._country_code = country_code

    @property
    def self_uri(self):
        """
        Gets the self_uri of this SmsPhoneNumberProvision.
        The URI for this object

        :return: The self_uri of this SmsPhoneNumberProvision.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this SmsPhoneNumberProvision.
        The URI for this object

        :param self_uri: The self_uri of this SmsPhoneNumberProvision.
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

