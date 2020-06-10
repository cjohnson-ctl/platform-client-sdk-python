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

class CoachingAnnotation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CoachingAnnotation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_by': 'UserReference',
            'date_created': 'datetime',
            'modified_by': 'UserReference',
            'date_modified': 'datetime',
            'text': 'str',
            'is_deleted': 'bool',
            'access_type': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'modified_by': 'modifiedBy',
            'date_modified': 'dateModified',
            'text': 'text',
            'is_deleted': 'isDeleted',
            'access_type': 'accessType',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._created_by = None
        self._date_created = None
        self._modified_by = None
        self._date_modified = None
        self._text = None
        self._is_deleted = None
        self._access_type = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this CoachingAnnotation.
        The globally unique identifier for the object.

        :return: The id of this CoachingAnnotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CoachingAnnotation.
        The globally unique identifier for the object.

        :param id: The id of this CoachingAnnotation.
        :type: str
        """
        
        self._id = id

    @property
    def created_by(self):
        """
        Gets the created_by of this CoachingAnnotation.
        The user who created the annotation.

        :return: The created_by of this CoachingAnnotation.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this CoachingAnnotation.
        The user who created the annotation.

        :param created_by: The created_by of this CoachingAnnotation.
        :type: UserReference
        """
        
        self._created_by = created_by

    @property
    def date_created(self):
        """
        Gets the date_created of this CoachingAnnotation.
        The date/time the annotation was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this CoachingAnnotation.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this CoachingAnnotation.
        The date/time the annotation was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this CoachingAnnotation.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def modified_by(self):
        """
        Gets the modified_by of this CoachingAnnotation.
        The last user to modify the annotation.

        :return: The modified_by of this CoachingAnnotation.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this CoachingAnnotation.
        The last user to modify the annotation.

        :param modified_by: The modified_by of this CoachingAnnotation.
        :type: UserReference
        """
        
        self._modified_by = modified_by

    @property
    def date_modified(self):
        """
        Gets the date_modified of this CoachingAnnotation.
        The date/time the annotation was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this CoachingAnnotation.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this CoachingAnnotation.
        The date/time the annotation was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this CoachingAnnotation.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def text(self):
        """
        Gets the text of this CoachingAnnotation.
        The text of the annotation.

        :return: The text of this CoachingAnnotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this CoachingAnnotation.
        The text of the annotation.

        :param text: The text of this CoachingAnnotation.
        :type: str
        """
        
        self._text = text

    @property
    def is_deleted(self):
        """
        Gets the is_deleted of this CoachingAnnotation.
        Flag indicating whether the annotation is deleted.

        :return: The is_deleted of this CoachingAnnotation.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """
        Sets the is_deleted of this CoachingAnnotation.
        Flag indicating whether the annotation is deleted.

        :param is_deleted: The is_deleted of this CoachingAnnotation.
        :type: bool
        """
        
        self._is_deleted = is_deleted

    @property
    def access_type(self):
        """
        Gets the access_type of this CoachingAnnotation.
        Determines the permissions required to view this item.

        :return: The access_type of this CoachingAnnotation.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this CoachingAnnotation.
        Determines the permissions required to view this item.

        :param access_type: The access_type of this CoachingAnnotation.
        :type: str
        """
        allowed_values = ["Public", "Private"]
        if access_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for access_type -> " + access_type
            self._access_type = "outdated_sdk_version"
        else:
            self._access_type = access_type

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CoachingAnnotation.
        The URI for this object

        :return: The self_uri of this CoachingAnnotation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CoachingAnnotation.
        The URI for this object

        :param self_uri: The self_uri of this CoachingAnnotation.
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

