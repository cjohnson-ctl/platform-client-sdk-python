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

class Greeting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Greeting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'owner_type': 'str',
            'owner': 'DomainEntity',
            'audio_file': 'GreetingAudioFile',
            'audio_tts': 'str',
            'created_date': 'datetime',
            'created_by': 'str',
            'modified_date': 'datetime',
            'modified_by': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'owner_type': 'ownerType',
            'owner': 'owner',
            'audio_file': 'audioFile',
            'audio_tts': 'audioTTS',
            'created_date': 'createdDate',
            'created_by': 'createdBy',
            'modified_date': 'modifiedDate',
            'modified_by': 'modifiedBy',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._type = None
        self._owner_type = None
        self._owner = None
        self._audio_file = None
        self._audio_tts = None
        self._created_date = None
        self._created_by = None
        self._modified_date = None
        self._modified_by = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Greeting.
        The globally unique identifier for the object.

        :return: The id of this Greeting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Greeting.
        The globally unique identifier for the object.

        :param id: The id of this Greeting.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Greeting.


        :return: The name of this Greeting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Greeting.


        :param name: The name of this Greeting.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Greeting.
        Greeting type

        :return: The type of this Greeting.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Greeting.
        Greeting type

        :param type: The type of this Greeting.
        :type: str
        """
        allowed_values = ["STATION", "VOICEMAIL", "NAME"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def owner_type(self):
        """
        Gets the owner_type of this Greeting.
        Greeting owner type

        :return: The owner_type of this Greeting.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """
        Sets the owner_type of this Greeting.
        Greeting owner type

        :param owner_type: The owner_type of this Greeting.
        :type: str
        """
        allowed_values = ["USER", "ORGANIZATION", "GROUP"]
        if owner_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for owner_type -> " + owner_type
            self._owner_type = "outdated_sdk_version"
        else:
            self._owner_type = owner_type

    @property
    def owner(self):
        """
        Gets the owner of this Greeting.
        Greeting owner

        :return: The owner of this Greeting.
        :rtype: DomainEntity
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Greeting.
        Greeting owner

        :param owner: The owner of this Greeting.
        :type: DomainEntity
        """
        
        self._owner = owner

    @property
    def audio_file(self):
        """
        Gets the audio_file of this Greeting.


        :return: The audio_file of this Greeting.
        :rtype: GreetingAudioFile
        """
        return self._audio_file

    @audio_file.setter
    def audio_file(self, audio_file):
        """
        Sets the audio_file of this Greeting.


        :param audio_file: The audio_file of this Greeting.
        :type: GreetingAudioFile
        """
        
        self._audio_file = audio_file

    @property
    def audio_tts(self):
        """
        Gets the audio_tts of this Greeting.


        :return: The audio_tts of this Greeting.
        :rtype: str
        """
        return self._audio_tts

    @audio_tts.setter
    def audio_tts(self, audio_tts):
        """
        Sets the audio_tts of this Greeting.


        :param audio_tts: The audio_tts of this Greeting.
        :type: str
        """
        
        self._audio_tts = audio_tts

    @property
    def created_date(self):
        """
        Gets the created_date of this Greeting.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The created_date of this Greeting.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Greeting.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param created_date: The created_date of this Greeting.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def created_by(self):
        """
        Gets the created_by of this Greeting.


        :return: The created_by of this Greeting.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Greeting.


        :param created_by: The created_by of this Greeting.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def modified_date(self):
        """
        Gets the modified_date of this Greeting.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The modified_date of this Greeting.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this Greeting.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param modified_date: The modified_date of this Greeting.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def modified_by(self):
        """
        Gets the modified_by of this Greeting.


        :return: The modified_by of this Greeting.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this Greeting.


        :param modified_by: The modified_by of this Greeting.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Greeting.
        The URI for this object

        :return: The self_uri of this Greeting.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Greeting.
        The URI for this object

        :param self_uri: The self_uri of this Greeting.
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

