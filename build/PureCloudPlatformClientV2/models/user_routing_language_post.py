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

class UserRoutingLanguagePost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserRoutingLanguagePost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'proficiency': 'float',
            'language_uri': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'proficiency': 'proficiency',
            'language_uri': 'languageUri',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._proficiency = None
        self._language_uri = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UserRoutingLanguagePost.
        The id of the existing routing language to add to the user

        :return: The id of this UserRoutingLanguagePost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserRoutingLanguagePost.
        The id of the existing routing language to add to the user

        :param id: The id of this UserRoutingLanguagePost.
        :type: str
        """
        
        self._id = id

    @property
    def proficiency(self):
        """
        Gets the proficiency of this UserRoutingLanguagePost.
        Proficiency is a rating from 0.0 to 5.0 on how competent an agent is for a particular language. It is used when a queue is set to \"Best available language\" mode to allow acd interactions to target agents with higher proficiency ratings.

        :return: The proficiency of this UserRoutingLanguagePost.
        :rtype: float
        """
        return self._proficiency

    @proficiency.setter
    def proficiency(self, proficiency):
        """
        Sets the proficiency of this UserRoutingLanguagePost.
        Proficiency is a rating from 0.0 to 5.0 on how competent an agent is for a particular language. It is used when a queue is set to \"Best available language\" mode to allow acd interactions to target agents with higher proficiency ratings.

        :param proficiency: The proficiency of this UserRoutingLanguagePost.
        :type: float
        """
        
        self._proficiency = proficiency

    @property
    def language_uri(self):
        """
        Gets the language_uri of this UserRoutingLanguagePost.
        URI to the organization language used by this user language.

        :return: The language_uri of this UserRoutingLanguagePost.
        :rtype: str
        """
        return self._language_uri

    @language_uri.setter
    def language_uri(self, language_uri):
        """
        Sets the language_uri of this UserRoutingLanguagePost.
        URI to the organization language used by this user language.

        :param language_uri: The language_uri of this UserRoutingLanguagePost.
        :type: str
        """
        
        self._language_uri = language_uri

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UserRoutingLanguagePost.
        The URI for this object

        :return: The self_uri of this UserRoutingLanguagePost.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UserRoutingLanguagePost.
        The URI for this object

        :param self_uri: The self_uri of this UserRoutingLanguagePost.
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

