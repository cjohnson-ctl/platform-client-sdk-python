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

class QueueMediaAssociation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueMediaAssociation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'queue': 'QueueReference',
            'media_types': 'list[str]',
            'delete': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'queue': 'queue',
            'media_types': 'mediaTypes',
            'delete': 'delete'
        }

        self._id = None
        self._queue = None
        self._media_types = None
        self._delete = None

    @property
    def id(self):
        """
        Gets the id of this QueueMediaAssociation.
        The reference ID for this QueueMediaAssociation

        :return: The id of this QueueMediaAssociation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueMediaAssociation.
        The reference ID for this QueueMediaAssociation

        :param id: The id of this QueueMediaAssociation.
        :type: str
        """
        
        self._id = id

    @property
    def queue(self):
        """
        Gets the queue of this QueueMediaAssociation.
        The queue to associate with the service goal group

        :return: The queue of this QueueMediaAssociation.
        :rtype: QueueReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this QueueMediaAssociation.
        The queue to associate with the service goal group

        :param queue: The queue of this QueueMediaAssociation.
        :type: QueueReference
        """
        
        self._queue = queue

    @property
    def media_types(self):
        """
        Gets the media_types of this QueueMediaAssociation.
        The media types of the given queue to associate with the service goal group

        :return: The media_types of this QueueMediaAssociation.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """
        Sets the media_types of this QueueMediaAssociation.
        The media types of the given queue to associate with the service goal group

        :param media_types: The media_types of this QueueMediaAssociation.
        :type: list[str]
        """
        
        self._media_types = media_types

    @property
    def delete(self):
        """
        Gets the delete of this QueueMediaAssociation.
        If marked true on a PATCH, this QueueMediaAssociation will be permanently deleted

        :return: The delete of this QueueMediaAssociation.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this QueueMediaAssociation.
        If marked true on a PATCH, this QueueMediaAssociation will be permanently deleted

        :param delete: The delete of this QueueMediaAssociation.
        :type: bool
        """
        
        self._delete = delete

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

