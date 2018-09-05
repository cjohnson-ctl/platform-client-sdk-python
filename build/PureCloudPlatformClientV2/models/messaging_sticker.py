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


class MessagingSticker(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessagingSticker - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'provider_sticker_id': 'int',
            'provider_package_id': 'int',
            'package_name': 'str',
            'messenger_type': 'str',
            'sticker_type': 'str',
            'provider_version': 'int',
            'uri_location': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'provider_sticker_id': 'providerStickerId',
            'provider_package_id': 'providerPackageId',
            'package_name': 'packageName',
            'messenger_type': 'messengerType',
            'sticker_type': 'stickerType',
            'provider_version': 'providerVersion',
            'uri_location': 'uriLocation',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._provider_sticker_id = None
        self._provider_package_id = None
        self._package_name = None
        self._messenger_type = None
        self._sticker_type = None
        self._provider_version = None
        self._uri_location = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this MessagingSticker.
        The globally unique identifier for the object.

        :return: The id of this MessagingSticker.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessagingSticker.
        The globally unique identifier for the object.

        :param id: The id of this MessagingSticker.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MessagingSticker.


        :return: The name of this MessagingSticker.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessagingSticker.


        :param name: The name of this MessagingSticker.
        :type: str
        """
        
        self._name = name

    @property
    def provider_sticker_id(self):
        """
        Gets the provider_sticker_id of this MessagingSticker.
        The sticker Id of the sticker, assigned by the sticker provider.

        :return: The provider_sticker_id of this MessagingSticker.
        :rtype: int
        """
        return self._provider_sticker_id

    @provider_sticker_id.setter
    def provider_sticker_id(self, provider_sticker_id):
        """
        Sets the provider_sticker_id of this MessagingSticker.
        The sticker Id of the sticker, assigned by the sticker provider.

        :param provider_sticker_id: The provider_sticker_id of this MessagingSticker.
        :type: int
        """
        
        self._provider_sticker_id = provider_sticker_id

    @property
    def provider_package_id(self):
        """
        Gets the provider_package_id of this MessagingSticker.
        The package Id of the sticker, assigned by the sticker provider.

        :return: The provider_package_id of this MessagingSticker.
        :rtype: int
        """
        return self._provider_package_id

    @provider_package_id.setter
    def provider_package_id(self, provider_package_id):
        """
        Sets the provider_package_id of this MessagingSticker.
        The package Id of the sticker, assigned by the sticker provider.

        :param provider_package_id: The provider_package_id of this MessagingSticker.
        :type: int
        """
        
        self._provider_package_id = provider_package_id

    @property
    def package_name(self):
        """
        Gets the package_name of this MessagingSticker.
        The package name of the sticker, assigned by the sticker provider.

        :return: The package_name of this MessagingSticker.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """
        Sets the package_name of this MessagingSticker.
        The package name of the sticker, assigned by the sticker provider.

        :param package_name: The package_name of this MessagingSticker.
        :type: str
        """
        
        self._package_name = package_name

    @property
    def messenger_type(self):
        """
        Gets the messenger_type of this MessagingSticker.
        The type of the messenger provider.

        :return: The messenger_type of this MessagingSticker.
        :rtype: str
        """
        return self._messenger_type

    @messenger_type.setter
    def messenger_type(self, messenger_type):
        """
        Sets the messenger_type of this MessagingSticker.
        The type of the messenger provider.

        :param messenger_type: The messenger_type of this MessagingSticker.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "telegram", "kakao"]
        if messenger_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for messenger_type -> " + messenger_type
            self._messenger_type = "outdated_sdk_version"
        else:
            self._messenger_type = messenger_type

    @property
    def sticker_type(self):
        """
        Gets the sticker_type of this MessagingSticker.
        The type of the sticker.

        :return: The sticker_type of this MessagingSticker.
        :rtype: str
        """
        return self._sticker_type

    @sticker_type.setter
    def sticker_type(self, sticker_type):
        """
        Sets the sticker_type of this MessagingSticker.
        The type of the sticker.

        :param sticker_type: The sticker_type of this MessagingSticker.
        :type: str
        """
        allowed_values = ["standard", "free", "paid"]
        if sticker_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for sticker_type -> " + sticker_type
            self._sticker_type = "outdated_sdk_version"
        else:
            self._sticker_type = sticker_type

    @property
    def provider_version(self):
        """
        Gets the provider_version of this MessagingSticker.
        The version of the sticker, assigned by the provider.

        :return: The provider_version of this MessagingSticker.
        :rtype: int
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """
        Sets the provider_version of this MessagingSticker.
        The version of the sticker, assigned by the provider.

        :param provider_version: The provider_version of this MessagingSticker.
        :type: int
        """
        
        self._provider_version = provider_version

    @property
    def uri_location(self):
        """
        Gets the uri_location of this MessagingSticker.


        :return: The uri_location of this MessagingSticker.
        :rtype: str
        """
        return self._uri_location

    @uri_location.setter
    def uri_location(self, uri_location):
        """
        Sets the uri_location of this MessagingSticker.


        :param uri_location: The uri_location of this MessagingSticker.
        :type: str
        """
        
        self._uri_location = uri_location

    @property
    def self_uri(self):
        """
        Gets the self_uri of this MessagingSticker.
        The URI for this object

        :return: The self_uri of this MessagingSticker.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this MessagingSticker.
        The URI for this object

        :param self_uri: The self_uri of this MessagingSticker.
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

