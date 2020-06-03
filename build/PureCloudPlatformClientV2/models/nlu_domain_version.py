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

class NluDomainVersion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NluDomainVersion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'domain': 'NluDomain',
            'description': 'str',
            'language': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'date_trained': 'datetime',
            'date_published': 'datetime',
            'training_status': 'str',
            'intents': 'list[IntentDefinition]',
            'entity_types': 'list[NamedEntityTypeDefinition]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'domain': 'domain',
            'description': 'description',
            'language': 'language',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'date_trained': 'dateTrained',
            'date_published': 'datePublished',
            'training_status': 'trainingStatus',
            'intents': 'intents',
            'entity_types': 'entityTypes',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._domain = None
        self._description = None
        self._language = None
        self._date_created = None
        self._date_modified = None
        self._date_trained = None
        self._date_published = None
        self._training_status = None
        self._intents = None
        self._entity_types = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this NluDomainVersion.
        The globally unique identifier for the object.

        :return: The id of this NluDomainVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NluDomainVersion.
        The globally unique identifier for the object.

        :param id: The id of this NluDomainVersion.
        :type: str
        """
        
        self._id = id

    @property
    def domain(self):
        """
        Gets the domain of this NluDomainVersion.
        The NLU domain of the version.

        :return: The domain of this NluDomainVersion.
        :rtype: NluDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this NluDomainVersion.
        The NLU domain of the version.

        :param domain: The domain of this NluDomainVersion.
        :type: NluDomain
        """
        
        self._domain = domain

    @property
    def description(self):
        """
        Gets the description of this NluDomainVersion.
        The description of the NLU domain version.

        :return: The description of this NluDomainVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NluDomainVersion.
        The description of the NLU domain version.

        :param description: The description of this NluDomainVersion.
        :type: str
        """
        
        self._description = description

    @property
    def language(self):
        """
        Gets the language of this NluDomainVersion.
        The language that the NLU domain version supports.

        :return: The language of this NluDomainVersion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this NluDomainVersion.
        The language that the NLU domain version supports.

        :param language: The language of this NluDomainVersion.
        :type: str
        """
        
        self._language = language

    @property
    def date_created(self):
        """
        Gets the date_created of this NluDomainVersion.
        The date when the NLU domain version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this NluDomainVersion.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this NluDomainVersion.
        The date when the NLU domain version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this NluDomainVersion.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this NluDomainVersion.
        The date when the NLU domain version was updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this NluDomainVersion.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this NluDomainVersion.
        The date when the NLU domain version was updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this NluDomainVersion.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def date_trained(self):
        """
        Gets the date_trained of this NluDomainVersion.
        The date when the NLU domain version was trained. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_trained of this NluDomainVersion.
        :rtype: datetime
        """
        return self._date_trained

    @date_trained.setter
    def date_trained(self, date_trained):
        """
        Sets the date_trained of this NluDomainVersion.
        The date when the NLU domain version was trained. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_trained: The date_trained of this NluDomainVersion.
        :type: datetime
        """
        
        self._date_trained = date_trained

    @property
    def date_published(self):
        """
        Gets the date_published of this NluDomainVersion.
        The date when the NLU domain version was published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_published of this NluDomainVersion.
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """
        Sets the date_published of this NluDomainVersion.
        The date when the NLU domain version was published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_published: The date_published of this NluDomainVersion.
        :type: datetime
        """
        
        self._date_published = date_published

    @property
    def training_status(self):
        """
        Gets the training_status of this NluDomainVersion.
        The training status of the NLU domain version.

        :return: The training_status of this NluDomainVersion.
        :rtype: str
        """
        return self._training_status

    @training_status.setter
    def training_status(self, training_status):
        """
        Sets the training_status of this NluDomainVersion.
        The training status of the NLU domain version.

        :param training_status: The training_status of this NluDomainVersion.
        :type: str
        """
        allowed_values = ["Untrained", "Training", "Trained", "Error", "Unknown"]
        if training_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for training_status -> " + training_status
            self._training_status = "outdated_sdk_version"
        else:
            self._training_status = training_status

    @property
    def intents(self):
        """
        Gets the intents of this NluDomainVersion.
        The intents defined for this NLU domain version.

        :return: The intents of this NluDomainVersion.
        :rtype: list[IntentDefinition]
        """
        return self._intents

    @intents.setter
    def intents(self, intents):
        """
        Sets the intents of this NluDomainVersion.
        The intents defined for this NLU domain version.

        :param intents: The intents of this NluDomainVersion.
        :type: list[IntentDefinition]
        """
        
        self._intents = intents

    @property
    def entity_types(self):
        """
        Gets the entity_types of this NluDomainVersion.
        The entity types defined for this NLU domain version.

        :return: The entity_types of this NluDomainVersion.
        :rtype: list[NamedEntityTypeDefinition]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """
        Sets the entity_types of this NluDomainVersion.
        The entity types defined for this NLU domain version.

        :param entity_types: The entity_types of this NluDomainVersion.
        :type: list[NamedEntityTypeDefinition]
        """
        
        self._entity_types = entity_types

    @property
    def self_uri(self):
        """
        Gets the self_uri of this NluDomainVersion.
        The URI for this object

        :return: The self_uri of this NluDomainVersion.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this NluDomainVersion.
        The URI for this object

        :param self_uri: The self_uri of this NluDomainVersion.
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

