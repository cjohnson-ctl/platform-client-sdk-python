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


class GDPRSubject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GDPRSubject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'user_id': 'str',
            'external_contact_id': 'str',
            'dialer_contact_id': 'DialerContactId',
            'addresses': 'list[str]',
            'phone_numbers': 'list[str]',
            'email_addresses': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'user_id': 'userId',
            'external_contact_id': 'externalContactId',
            'dialer_contact_id': 'dialerContactId',
            'addresses': 'addresses',
            'phone_numbers': 'phoneNumbers',
            'email_addresses': 'emailAddresses'
        }

        self._name = None
        self._user_id = None
        self._external_contact_id = None
        self._dialer_contact_id = None
        self._addresses = None
        self._phone_numbers = None
        self._email_addresses = None

    @property
    def name(self):
        """
        Gets the name of this GDPRSubject.


        :return: The name of this GDPRSubject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GDPRSubject.


        :param name: The name of this GDPRSubject.
        :type: str
        """
        
        self._name = name

    @property
    def user_id(self):
        """
        Gets the user_id of this GDPRSubject.


        :return: The user_id of this GDPRSubject.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this GDPRSubject.


        :param user_id: The user_id of this GDPRSubject.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this GDPRSubject.


        :return: The external_contact_id of this GDPRSubject.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this GDPRSubject.


        :param external_contact_id: The external_contact_id of this GDPRSubject.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def dialer_contact_id(self):
        """
        Gets the dialer_contact_id of this GDPRSubject.


        :return: The dialer_contact_id of this GDPRSubject.
        :rtype: DialerContactId
        """
        return self._dialer_contact_id

    @dialer_contact_id.setter
    def dialer_contact_id(self, dialer_contact_id):
        """
        Sets the dialer_contact_id of this GDPRSubject.


        :param dialer_contact_id: The dialer_contact_id of this GDPRSubject.
        :type: DialerContactId
        """
        
        self._dialer_contact_id = dialer_contact_id

    @property
    def addresses(self):
        """
        Gets the addresses of this GDPRSubject.


        :return: The addresses of this GDPRSubject.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this GDPRSubject.


        :param addresses: The addresses of this GDPRSubject.
        :type: list[str]
        """
        
        self._addresses = addresses

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this GDPRSubject.


        :return: The phone_numbers of this GDPRSubject.
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this GDPRSubject.


        :param phone_numbers: The phone_numbers of this GDPRSubject.
        :type: list[str]
        """
        
        self._phone_numbers = phone_numbers

    @property
    def email_addresses(self):
        """
        Gets the email_addresses of this GDPRSubject.


        :return: The email_addresses of this GDPRSubject.
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """
        Sets the email_addresses of this GDPRSubject.


        :param email_addresses: The email_addresses of this GDPRSubject.
        :type: list[str]
        """
        
        self._email_addresses = email_addresses

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

