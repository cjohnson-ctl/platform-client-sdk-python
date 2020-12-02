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

class DialerContactlistfilterConfigChangeContactListFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerContactlistfilterConfigChangeContactListFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'contact_list': 'DialerContactlistfilterConfigChangeUriReference',
            'contact_list_columns': 'list[str]',
            'clauses': 'list[DialerContactlistfilterConfigChangeFilterClause]',
            'filter_type': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'contact_list': 'contactList',
            'contact_list_columns': 'contactListColumns',
            'clauses': 'clauses',
            'filter_type': 'filterType',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._contact_list = None
        self._contact_list_columns = None
        self._clauses = None
        self._filter_type = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The id of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DialerContactlistfilterConfigChangeContactListFilter.


        :param id: The id of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The name of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DialerContactlistfilterConfigChangeContactListFilter.


        :param name: The name of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The date_created of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DialerContactlistfilterConfigChangeContactListFilter.


        :param date_created: The date_created of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The date_modified of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this DialerContactlistfilterConfigChangeContactListFilter.


        :param date_modified: The date_modified of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The version of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DialerContactlistfilterConfigChangeContactListFilter.


        :param version: The version of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: int
        """
        
        self._version = version

    @property
    def contact_list(self):
        """
        Gets the contact_list of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The contact_list of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: DialerContactlistfilterConfigChangeUriReference
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this DialerContactlistfilterConfigChangeContactListFilter.


        :param contact_list: The contact_list of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: DialerContactlistfilterConfigChangeUriReference
        """
        
        self._contact_list = contact_list

    @property
    def contact_list_columns(self):
        """
        Gets the contact_list_columns of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The contact_list_columns of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: list[str]
        """
        return self._contact_list_columns

    @contact_list_columns.setter
    def contact_list_columns(self, contact_list_columns):
        """
        Sets the contact_list_columns of this DialerContactlistfilterConfigChangeContactListFilter.


        :param contact_list_columns: The contact_list_columns of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: list[str]
        """
        
        self._contact_list_columns = contact_list_columns

    @property
    def clauses(self):
        """
        Gets the clauses of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The clauses of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: list[DialerContactlistfilterConfigChangeFilterClause]
        """
        return self._clauses

    @clauses.setter
    def clauses(self, clauses):
        """
        Sets the clauses of this DialerContactlistfilterConfigChangeContactListFilter.


        :param clauses: The clauses of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: list[DialerContactlistfilterConfigChangeFilterClause]
        """
        
        self._clauses = clauses

    @property
    def filter_type(self):
        """
        Gets the filter_type of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The filter_type of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this DialerContactlistfilterConfigChangeContactListFilter.


        :param filter_type: The filter_type of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: str
        """
        allowed_values = ["AND", "OR"]
        if filter_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for filter_type -> " + filter_type)
            self._filter_type = "outdated_sdk_version"
        else:
            self._filter_type = filter_type

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerContactlistfilterConfigChangeContactListFilter.


        :return: The additional_properties of this DialerContactlistfilterConfigChangeContactListFilter.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerContactlistfilterConfigChangeContactListFilter.


        :param additional_properties: The additional_properties of this DialerContactlistfilterConfigChangeContactListFilter.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

