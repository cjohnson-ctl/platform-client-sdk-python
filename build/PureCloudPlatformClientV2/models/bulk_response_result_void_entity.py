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

class BulkResponseResultVoidEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BulkResponseResultVoidEntity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'success': 'bool',
            'entity': 'Void',
            'error': 'BulkErrorEntity'
        }

        self.attribute_map = {
            'id': 'id',
            'success': 'success',
            'entity': 'entity',
            'error': 'error'
        }

        self._id = None
        self._success = None
        self._entity = None
        self._error = None

    @property
    def id(self):
        """
        Gets the id of this BulkResponseResultVoidEntity.


        :return: The id of this BulkResponseResultVoidEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BulkResponseResultVoidEntity.


        :param id: The id of this BulkResponseResultVoidEntity.
        :type: str
        """
        
        self._id = id

    @property
    def success(self):
        """
        Gets the success of this BulkResponseResultVoidEntity.


        :return: The success of this BulkResponseResultVoidEntity.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this BulkResponseResultVoidEntity.


        :param success: The success of this BulkResponseResultVoidEntity.
        :type: bool
        """
        
        self._success = success

    @property
    def entity(self):
        """
        Gets the entity of this BulkResponseResultVoidEntity.


        :return: The entity of this BulkResponseResultVoidEntity.
        :rtype: Void
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this BulkResponseResultVoidEntity.


        :param entity: The entity of this BulkResponseResultVoidEntity.
        :type: Void
        """
        
        self._entity = entity

    @property
    def error(self):
        """
        Gets the error of this BulkResponseResultVoidEntity.


        :return: The error of this BulkResponseResultVoidEntity.
        :rtype: BulkErrorEntity
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this BulkResponseResultVoidEntity.


        :param error: The error of this BulkResponseResultVoidEntity.
        :type: BulkErrorEntity
        """
        
        self._error = error

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

