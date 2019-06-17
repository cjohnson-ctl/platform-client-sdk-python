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


class Manager(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Manager - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'display_name': 'str',
            'active': 'bool',
            'user_name': 'str',
            'password': 'str',
            'title': 'str',
            'phone_numbers': 'list[ScimPhoneNumber]',
            'emails': 'list[ScimEmail]',
            'photos': 'list[Photo]',
            'groups': 'list[ScimV2GroupReference]',
            'meta': 'ScimMetadata',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'ScimV2EnterpriseUser',
            'value': 'str',
            'ref': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'active': 'active',
            'user_name': 'userName',
            'password': 'password',
            'title': 'title',
            'phone_numbers': 'phoneNumbers',
            'emails': 'emails',
            'photos': 'photos',
            'groups': 'groups',
            'meta': 'meta',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User',
            'value': 'value',
            'ref': '$ref'
        }

        self._display_name = None
        self._active = None
        self._user_name = None
        self._password = None
        self._title = None
        self._phone_numbers = None
        self._emails = None
        self._photos = None
        self._groups = None
        self._meta = None
        self._urnietfparamsscimschemasextensionenterprise2_0_user = None
        self._value = None
        self._ref = None

    @property
    def display_name(self):
        """
        Gets the display_name of this Manager.
        Display Name

        :return: The display_name of this Manager.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Manager.
        Display Name

        :param display_name: The display_name of this Manager.
        :type: str
        """
        
        self._display_name = display_name

    @property
    def active(self):
        """
        Gets the active of this Manager.
        Active flag

        :return: The active of this Manager.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Manager.
        Active flag

        :param active: The active of this Manager.
        :type: bool
        """
        
        self._active = active

    @property
    def user_name(self):
        """
        Gets the user_name of this Manager.
        User Name (Must be Unique) maps to PureCloud e-mail address

        :return: The user_name of this Manager.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this Manager.
        User Name (Must be Unique) maps to PureCloud e-mail address

        :param user_name: The user_name of this Manager.
        :type: str
        """
        
        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this Manager.
        Password (updateOnly)

        :return: The password of this Manager.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Manager.
        Password (updateOnly)

        :param password: The password of this Manager.
        :type: str
        """
        
        self._password = password

    @property
    def title(self):
        """
        Gets the title of this Manager.
        Title

        :return: The title of this Manager.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Manager.
        Title

        :param title: The title of this Manager.
        :type: str
        """
        
        self._title = title

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this Manager.
        Phone numbers

        :return: The phone_numbers of this Manager.
        :rtype: list[ScimPhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this Manager.
        Phone numbers

        :param phone_numbers: The phone_numbers of this Manager.
        :type: list[ScimPhoneNumber]
        """
        
        self._phone_numbers = phone_numbers

    @property
    def emails(self):
        """
        Gets the emails of this Manager.
        Emails

        :return: The emails of this Manager.
        :rtype: list[ScimEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this Manager.
        Emails

        :param emails: The emails of this Manager.
        :type: list[ScimEmail]
        """
        
        self._emails = emails

    @property
    def photos(self):
        """
        Gets the photos of this Manager.
        Photos

        :return: The photos of this Manager.
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """
        Sets the photos of this Manager.
        Photos

        :param photos: The photos of this Manager.
        :type: list[Photo]
        """
        
        self._photos = photos

    @property
    def groups(self):
        """
        Gets the groups of this Manager.
        Group References

        :return: The groups of this Manager.
        :rtype: list[ScimV2GroupReference]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this Manager.
        Group References

        :param groups: The groups of this Manager.
        :type: list[ScimV2GroupReference]
        """
        
        self._groups = groups

    @property
    def meta(self):
        """
        Gets the meta of this Manager.


        :return: The meta of this Manager.
        :rtype: ScimMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this Manager.


        :param meta: The meta of this Manager.
        :type: ScimMetadata
        """
        
        self._meta = meta

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self):
        """
        Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this Manager.


        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this Manager.
        :rtype: ScimV2EnterpriseUser
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user):
        """
        Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this Manager.


        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this Manager.
        :type: ScimV2EnterpriseUser
        """
        
        self._urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def value(self):
        """
        Gets the value of this Manager.
        Identifier of the Manager

        :return: The value of this Manager.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Manager.
        Identifier of the Manager

        :param value: The value of this Manager.
        :type: str
        """
        
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this Manager.
        Ref to entity

        :return: The ref of this Manager.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this Manager.
        Ref to entity

        :param ref: The ref of this Manager.
        :type: str
        """
        
        self._ref = ref

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
