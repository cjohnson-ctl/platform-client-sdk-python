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

class Group(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Group - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'date_modified': 'datetime',
            'member_count': 'int',
            'state': 'str',
            'version': 'int',
            'type': 'str',
            'images': 'list[UserImage]',
            'addresses': 'list[GroupContact]',
            'rules_visible': 'bool',
            'visibility': 'str',
            'owners': 'list[User]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'date_modified': 'dateModified',
            'member_count': 'memberCount',
            'state': 'state',
            'version': 'version',
            'type': 'type',
            'images': 'images',
            'addresses': 'addresses',
            'rules_visible': 'rulesVisible',
            'visibility': 'visibility',
            'owners': 'owners',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._date_modified = None
        self._member_count = None
        self._state = None
        self._version = None
        self._type = None
        self._images = None
        self._addresses = None
        self._rules_visible = None
        self._visibility = None
        self._owners = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Group.
        The globally unique identifier for the object.

        :return: The id of this Group.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Group.
        The globally unique identifier for the object.

        :param id: The id of this Group.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Group.
        The group name.

        :return: The name of this Group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Group.
        The group name.

        :param name: The name of this Group.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Group.


        :return: The description of this Group.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Group.


        :param description: The description of this Group.
        :type: str
        """
        
        self._description = description

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Group.
        Last modified date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Group.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Group.
        Last modified date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Group.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def member_count(self):
        """
        Gets the member_count of this Group.
        Number of members.

        :return: The member_count of this Group.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """
        Sets the member_count of this Group.
        Number of members.

        :param member_count: The member_count of this Group.
        :type: int
        """
        
        self._member_count = member_count

    @property
    def state(self):
        """
        Gets the state of this Group.
        Active, inactive, or deleted state.

        :return: The state of this Group.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Group.
        Active, inactive, or deleted state.

        :param state: The state of this Group.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def version(self):
        """
        Gets the version of this Group.
        Current version for this resource.

        :return: The version of this Group.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Group.
        Current version for this resource.

        :param version: The version of this Group.
        :type: int
        """
        
        self._version = version

    @property
    def type(self):
        """
        Gets the type of this Group.
        Type of group.

        :return: The type of this Group.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Group.
        Type of group.

        :param type: The type of this Group.
        :type: str
        """
        allowed_values = ["official", "social"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def images(self):
        """
        Gets the images of this Group.


        :return: The images of this Group.
        :rtype: list[UserImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Group.


        :param images: The images of this Group.
        :type: list[UserImage]
        """
        
        self._images = images

    @property
    def addresses(self):
        """
        Gets the addresses of this Group.


        :return: The addresses of this Group.
        :rtype: list[GroupContact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this Group.


        :param addresses: The addresses of this Group.
        :type: list[GroupContact]
        """
        
        self._addresses = addresses

    @property
    def rules_visible(self):
        """
        Gets the rules_visible of this Group.
        Are membership rules visible to the person requesting to view the group

        :return: The rules_visible of this Group.
        :rtype: bool
        """
        return self._rules_visible

    @rules_visible.setter
    def rules_visible(self, rules_visible):
        """
        Sets the rules_visible of this Group.
        Are membership rules visible to the person requesting to view the group

        :param rules_visible: The rules_visible of this Group.
        :type: bool
        """
        
        self._rules_visible = rules_visible

    @property
    def visibility(self):
        """
        Gets the visibility of this Group.
        Who can view this group

        :return: The visibility of this Group.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this Group.
        Who can view this group

        :param visibility: The visibility of this Group.
        :type: str
        """
        allowed_values = ["public", "owners", "members"]
        if visibility.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for visibility -> " + visibility)
            self._visibility = "outdated_sdk_version"
        else:
            self._visibility = visibility

    @property
    def owners(self):
        """
        Gets the owners of this Group.
        Owners of the group

        :return: The owners of this Group.
        :rtype: list[User]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this Group.
        Owners of the group

        :param owners: The owners of this Group.
        :type: list[User]
        """
        
        self._owners = owners

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Group.
        The URI for this object

        :return: The self_uri of this Group.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Group.
        The URI for this object

        :param self_uri: The self_uri of this Group.
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

