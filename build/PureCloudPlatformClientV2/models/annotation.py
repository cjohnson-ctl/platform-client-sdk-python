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

class Annotation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Annotation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'location': 'int',
            'duration_ms': 'int',
            'absolute_location': 'int',
            'absolute_duration_ms': 'int',
            'recording_location': 'int',
            'recording_duration_ms': 'int',
            'user': 'User',
            'description': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'location': 'location',
            'duration_ms': 'durationMs',
            'absolute_location': 'absoluteLocation',
            'absolute_duration_ms': 'absoluteDurationMs',
            'recording_location': 'recordingLocation',
            'recording_duration_ms': 'recordingDurationMs',
            'user': 'user',
            'description': 'description',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._type = None
        self._location = None
        self._duration_ms = None
        self._absolute_location = None
        self._absolute_duration_ms = None
        self._recording_location = None
        self._recording_duration_ms = None
        self._user = None
        self._description = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Annotation.
        The globally unique identifier for the object.

        :return: The id of this Annotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Annotation.
        The globally unique identifier for the object.

        :param id: The id of this Annotation.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Annotation.


        :return: The name of this Annotation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Annotation.


        :param name: The name of this Annotation.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Annotation.


        :return: The type of this Annotation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Annotation.


        :param type: The type of this Annotation.
        :type: str
        """
        
        self._type = type

    @property
    def location(self):
        """
        Gets the location of this Annotation.
        Offset of annotation in milliseconds.

        :return: The location of this Annotation.
        :rtype: int
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Annotation.
        Offset of annotation in milliseconds.

        :param location: The location of this Annotation.
        :type: int
        """
        
        self._location = location

    @property
    def duration_ms(self):
        """
        Gets the duration_ms of this Annotation.
        Duration of annotation in milliseconds.

        :return: The duration_ms of this Annotation.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """
        Sets the duration_ms of this Annotation.
        Duration of annotation in milliseconds.

        :param duration_ms: The duration_ms of this Annotation.
        :type: int
        """
        
        self._duration_ms = duration_ms

    @property
    def absolute_location(self):
        """
        Gets the absolute_location of this Annotation.
        Offset of annotation (milliseconds) from start of recording.

        :return: The absolute_location of this Annotation.
        :rtype: int
        """
        return self._absolute_location

    @absolute_location.setter
    def absolute_location(self, absolute_location):
        """
        Sets the absolute_location of this Annotation.
        Offset of annotation (milliseconds) from start of recording.

        :param absolute_location: The absolute_location of this Annotation.
        :type: int
        """
        
        self._absolute_location = absolute_location

    @property
    def absolute_duration_ms(self):
        """
        Gets the absolute_duration_ms of this Annotation.
        Duration of annotation (milliseconds).

        :return: The absolute_duration_ms of this Annotation.
        :rtype: int
        """
        return self._absolute_duration_ms

    @absolute_duration_ms.setter
    def absolute_duration_ms(self, absolute_duration_ms):
        """
        Sets the absolute_duration_ms of this Annotation.
        Duration of annotation (milliseconds).

        :param absolute_duration_ms: The absolute_duration_ms of this Annotation.
        :type: int
        """
        
        self._absolute_duration_ms = absolute_duration_ms

    @property
    def recording_location(self):
        """
        Gets the recording_location of this Annotation.
        Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts

        :return: The recording_location of this Annotation.
        :rtype: int
        """
        return self._recording_location

    @recording_location.setter
    def recording_location(self, recording_location):
        """
        Sets the recording_location of this Annotation.
        Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts

        :param recording_location: The recording_location of this Annotation.
        :type: int
        """
        
        self._recording_location = recording_location

    @property
    def recording_duration_ms(self):
        """
        Gets the recording_duration_ms of this Annotation.
        Duration of annotation (milliseconds), adjusted for any recording cuts.

        :return: The recording_duration_ms of this Annotation.
        :rtype: int
        """
        return self._recording_duration_ms

    @recording_duration_ms.setter
    def recording_duration_ms(self, recording_duration_ms):
        """
        Sets the recording_duration_ms of this Annotation.
        Duration of annotation (milliseconds), adjusted for any recording cuts.

        :param recording_duration_ms: The recording_duration_ms of this Annotation.
        :type: int
        """
        
        self._recording_duration_ms = recording_duration_ms

    @property
    def user(self):
        """
        Gets the user of this Annotation.
        User that created this annotation (if any).

        :return: The user of this Annotation.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Annotation.
        User that created this annotation (if any).

        :param user: The user of this Annotation.
        :type: User
        """
        
        self._user = user

    @property
    def description(self):
        """
        Gets the description of this Annotation.
        Text of annotation.

        :return: The description of this Annotation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Annotation.
        Text of annotation.

        :param description: The description of this Annotation.
        :type: str
        """
        
        self._description = description

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Annotation.
        The URI for this object

        :return: The self_uri of this Annotation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Annotation.
        The URI for this object

        :param self_uri: The self_uri of this Annotation.
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

