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

class FlowVersion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FlowVersion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'commit_version': 'str',
            'configuration_version': 'str',
            'type': 'str',
            'secure': 'bool',
            'debug': 'bool',
            'created_by': 'User',
            'created_by_client': 'DomainEntityRef',
            'configuration_uri': 'str',
            'date_created': 'int',
            'generation_id': 'str',
            'publish_result_uri': 'str',
            'input_schema': 'JsonSchemaDocument',
            'output_schema': 'JsonSchemaDocument',
            'nlu_info': 'NluInfo',
            'supported_languages': 'list[SupportedLanguage]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'commit_version': 'commitVersion',
            'configuration_version': 'configurationVersion',
            'type': 'type',
            'secure': 'secure',
            'debug': 'debug',
            'created_by': 'createdBy',
            'created_by_client': 'createdByClient',
            'configuration_uri': 'configurationUri',
            'date_created': 'dateCreated',
            'generation_id': 'generationId',
            'publish_result_uri': 'publishResultUri',
            'input_schema': 'inputSchema',
            'output_schema': 'outputSchema',
            'nlu_info': 'nluInfo',
            'supported_languages': 'supportedLanguages',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._commit_version = None
        self._configuration_version = None
        self._type = None
        self._secure = None
        self._debug = None
        self._created_by = None
        self._created_by_client = None
        self._configuration_uri = None
        self._date_created = None
        self._generation_id = None
        self._publish_result_uri = None
        self._input_schema = None
        self._output_schema = None
        self._nlu_info = None
        self._supported_languages = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this FlowVersion.
        The flow version identifier

        :return: The id of this FlowVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FlowVersion.
        The flow version identifier

        :param id: The id of this FlowVersion.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FlowVersion.


        :return: The name of this FlowVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FlowVersion.


        :param name: The name of this FlowVersion.
        :type: str
        """
        
        self._name = name

    @property
    def commit_version(self):
        """
        Gets the commit_version of this FlowVersion.


        :return: The commit_version of this FlowVersion.
        :rtype: str
        """
        return self._commit_version

    @commit_version.setter
    def commit_version(self, commit_version):
        """
        Sets the commit_version of this FlowVersion.


        :param commit_version: The commit_version of this FlowVersion.
        :type: str
        """
        
        self._commit_version = commit_version

    @property
    def configuration_version(self):
        """
        Gets the configuration_version of this FlowVersion.


        :return: The configuration_version of this FlowVersion.
        :rtype: str
        """
        return self._configuration_version

    @configuration_version.setter
    def configuration_version(self, configuration_version):
        """
        Sets the configuration_version of this FlowVersion.


        :param configuration_version: The configuration_version of this FlowVersion.
        :type: str
        """
        
        self._configuration_version = configuration_version

    @property
    def type(self):
        """
        Gets the type of this FlowVersion.


        :return: The type of this FlowVersion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FlowVersion.


        :param type: The type of this FlowVersion.
        :type: str
        """
        allowed_values = ["PUBLISH", "CHECKIN", "SAVE"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def secure(self):
        """
        Gets the secure of this FlowVersion.


        :return: The secure of this FlowVersion.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """
        Sets the secure of this FlowVersion.


        :param secure: The secure of this FlowVersion.
        :type: bool
        """
        
        self._secure = secure

    @property
    def debug(self):
        """
        Gets the debug of this FlowVersion.


        :return: The debug of this FlowVersion.
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """
        Sets the debug of this FlowVersion.


        :param debug: The debug of this FlowVersion.
        :type: bool
        """
        
        self._debug = debug

    @property
    def created_by(self):
        """
        Gets the created_by of this FlowVersion.


        :return: The created_by of this FlowVersion.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this FlowVersion.


        :param created_by: The created_by of this FlowVersion.
        :type: User
        """
        
        self._created_by = created_by

    @property
    def created_by_client(self):
        """
        Gets the created_by_client of this FlowVersion.


        :return: The created_by_client of this FlowVersion.
        :rtype: DomainEntityRef
        """
        return self._created_by_client

    @created_by_client.setter
    def created_by_client(self, created_by_client):
        """
        Sets the created_by_client of this FlowVersion.


        :param created_by_client: The created_by_client of this FlowVersion.
        :type: DomainEntityRef
        """
        
        self._created_by_client = created_by_client

    @property
    def configuration_uri(self):
        """
        Gets the configuration_uri of this FlowVersion.


        :return: The configuration_uri of this FlowVersion.
        :rtype: str
        """
        return self._configuration_uri

    @configuration_uri.setter
    def configuration_uri(self, configuration_uri):
        """
        Sets the configuration_uri of this FlowVersion.


        :param configuration_uri: The configuration_uri of this FlowVersion.
        :type: str
        """
        
        self._configuration_uri = configuration_uri

    @property
    def date_created(self):
        """
        Gets the date_created of this FlowVersion.


        :return: The date_created of this FlowVersion.
        :rtype: int
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this FlowVersion.


        :param date_created: The date_created of this FlowVersion.
        :type: int
        """
        
        self._date_created = date_created

    @property
    def generation_id(self):
        """
        Gets the generation_id of this FlowVersion.


        :return: The generation_id of this FlowVersion.
        :rtype: str
        """
        return self._generation_id

    @generation_id.setter
    def generation_id(self, generation_id):
        """
        Sets the generation_id of this FlowVersion.


        :param generation_id: The generation_id of this FlowVersion.
        :type: str
        """
        
        self._generation_id = generation_id

    @property
    def publish_result_uri(self):
        """
        Gets the publish_result_uri of this FlowVersion.


        :return: The publish_result_uri of this FlowVersion.
        :rtype: str
        """
        return self._publish_result_uri

    @publish_result_uri.setter
    def publish_result_uri(self, publish_result_uri):
        """
        Sets the publish_result_uri of this FlowVersion.


        :param publish_result_uri: The publish_result_uri of this FlowVersion.
        :type: str
        """
        
        self._publish_result_uri = publish_result_uri

    @property
    def input_schema(self):
        """
        Gets the input_schema of this FlowVersion.


        :return: The input_schema of this FlowVersion.
        :rtype: JsonSchemaDocument
        """
        return self._input_schema

    @input_schema.setter
    def input_schema(self, input_schema):
        """
        Sets the input_schema of this FlowVersion.


        :param input_schema: The input_schema of this FlowVersion.
        :type: JsonSchemaDocument
        """
        
        self._input_schema = input_schema

    @property
    def output_schema(self):
        """
        Gets the output_schema of this FlowVersion.


        :return: The output_schema of this FlowVersion.
        :rtype: JsonSchemaDocument
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema):
        """
        Sets the output_schema of this FlowVersion.


        :param output_schema: The output_schema of this FlowVersion.
        :type: JsonSchemaDocument
        """
        
        self._output_schema = output_schema

    @property
    def nlu_info(self):
        """
        Gets the nlu_info of this FlowVersion.
        Information about the natural language understanding configuration for the flow version

        :return: The nlu_info of this FlowVersion.
        :rtype: NluInfo
        """
        return self._nlu_info

    @nlu_info.setter
    def nlu_info(self, nlu_info):
        """
        Sets the nlu_info of this FlowVersion.
        Information about the natural language understanding configuration for the flow version

        :param nlu_info: The nlu_info of this FlowVersion.
        :type: NluInfo
        """
        
        self._nlu_info = nlu_info

    @property
    def supported_languages(self):
        """
        Gets the supported_languages of this FlowVersion.
        List of supported languages for this version of the flow

        :return: The supported_languages of this FlowVersion.
        :rtype: list[SupportedLanguage]
        """
        return self._supported_languages

    @supported_languages.setter
    def supported_languages(self, supported_languages):
        """
        Sets the supported_languages of this FlowVersion.
        List of supported languages for this version of the flow

        :param supported_languages: The supported_languages of this FlowVersion.
        :type: list[SupportedLanguage]
        """
        
        self._supported_languages = supported_languages

    @property
    def self_uri(self):
        """
        Gets the self_uri of this FlowVersion.
        The URI for this object

        :return: The self_uri of this FlowVersion.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this FlowVersion.
        The URI for this object

        :param self_uri: The self_uri of this FlowVersion.
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

