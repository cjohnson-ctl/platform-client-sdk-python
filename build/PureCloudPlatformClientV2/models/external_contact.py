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

class ExternalContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ExternalContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'salutation': 'str',
            'title': 'str',
            'work_phone': 'PhoneNumber',
            'cell_phone': 'PhoneNumber',
            'home_phone': 'PhoneNumber',
            'other_phone': 'PhoneNumber',
            'work_email': 'str',
            'personal_email': 'str',
            'other_email': 'str',
            'address': 'ContactAddress',
            'twitter_id': 'TwitterId',
            'line_id': 'LineId',
            'whats_app_id': 'WhatsAppId',
            'facebook_id': 'FacebookId',
            'modify_date': 'datetime',
            'create_date': 'datetime',
            'external_organization': 'ExternalOrganization',
            'survey_opt_out': 'bool',
            'external_system_url': 'str',
            'schema': 'DataSchema',
            'custom_fields': 'dict(str, object)',
            'external_data_sources': 'list[ExternalDataSource]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'middle_name': 'middleName',
            'last_name': 'lastName',
            'salutation': 'salutation',
            'title': 'title',
            'work_phone': 'workPhone',
            'cell_phone': 'cellPhone',
            'home_phone': 'homePhone',
            'other_phone': 'otherPhone',
            'work_email': 'workEmail',
            'personal_email': 'personalEmail',
            'other_email': 'otherEmail',
            'address': 'address',
            'twitter_id': 'twitterId',
            'line_id': 'lineId',
            'whats_app_id': 'whatsAppId',
            'facebook_id': 'facebookId',
            'modify_date': 'modifyDate',
            'create_date': 'createDate',
            'external_organization': 'externalOrganization',
            'survey_opt_out': 'surveyOptOut',
            'external_system_url': 'externalSystemUrl',
            'schema': 'schema',
            'custom_fields': 'customFields',
            'external_data_sources': 'externalDataSources',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._salutation = None
        self._title = None
        self._work_phone = None
        self._cell_phone = None
        self._home_phone = None
        self._other_phone = None
        self._work_email = None
        self._personal_email = None
        self._other_email = None
        self._address = None
        self._twitter_id = None
        self._line_id = None
        self._whats_app_id = None
        self._facebook_id = None
        self._modify_date = None
        self._create_date = None
        self._external_organization = None
        self._survey_opt_out = None
        self._external_system_url = None
        self._schema = None
        self._custom_fields = None
        self._external_data_sources = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this ExternalContact.
        The globally unique identifier for the object.

        :return: The id of this ExternalContact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalContact.
        The globally unique identifier for the object.

        :param id: The id of this ExternalContact.
        :type: str
        """
        
        self._id = id

    @property
    def first_name(self):
        """
        Gets the first_name of this ExternalContact.
        The first name of the contact.

        :return: The first_name of this ExternalContact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this ExternalContact.
        The first name of the contact.

        :param first_name: The first_name of this ExternalContact.
        :type: str
        """
        
        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this ExternalContact.


        :return: The middle_name of this ExternalContact.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this ExternalContact.


        :param middle_name: The middle_name of this ExternalContact.
        :type: str
        """
        
        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this ExternalContact.
        The last name of the contact.

        :return: The last_name of this ExternalContact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this ExternalContact.
        The last name of the contact.

        :param last_name: The last_name of this ExternalContact.
        :type: str
        """
        
        self._last_name = last_name

    @property
    def salutation(self):
        """
        Gets the salutation of this ExternalContact.


        :return: The salutation of this ExternalContact.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """
        Sets the salutation of this ExternalContact.


        :param salutation: The salutation of this ExternalContact.
        :type: str
        """
        
        self._salutation = salutation

    @property
    def title(self):
        """
        Gets the title of this ExternalContact.


        :return: The title of this ExternalContact.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ExternalContact.


        :param title: The title of this ExternalContact.
        :type: str
        """
        
        self._title = title

    @property
    def work_phone(self):
        """
        Gets the work_phone of this ExternalContact.


        :return: The work_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """
        Sets the work_phone of this ExternalContact.


        :param work_phone: The work_phone of this ExternalContact.
        :type: PhoneNumber
        """
        
        self._work_phone = work_phone

    @property
    def cell_phone(self):
        """
        Gets the cell_phone of this ExternalContact.


        :return: The cell_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._cell_phone

    @cell_phone.setter
    def cell_phone(self, cell_phone):
        """
        Sets the cell_phone of this ExternalContact.


        :param cell_phone: The cell_phone of this ExternalContact.
        :type: PhoneNumber
        """
        
        self._cell_phone = cell_phone

    @property
    def home_phone(self):
        """
        Gets the home_phone of this ExternalContact.


        :return: The home_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """
        Sets the home_phone of this ExternalContact.


        :param home_phone: The home_phone of this ExternalContact.
        :type: PhoneNumber
        """
        
        self._home_phone = home_phone

    @property
    def other_phone(self):
        """
        Gets the other_phone of this ExternalContact.


        :return: The other_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._other_phone

    @other_phone.setter
    def other_phone(self, other_phone):
        """
        Sets the other_phone of this ExternalContact.


        :param other_phone: The other_phone of this ExternalContact.
        :type: PhoneNumber
        """
        
        self._other_phone = other_phone

    @property
    def work_email(self):
        """
        Gets the work_email of this ExternalContact.


        :return: The work_email of this ExternalContact.
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email):
        """
        Sets the work_email of this ExternalContact.


        :param work_email: The work_email of this ExternalContact.
        :type: str
        """
        
        self._work_email = work_email

    @property
    def personal_email(self):
        """
        Gets the personal_email of this ExternalContact.


        :return: The personal_email of this ExternalContact.
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """
        Sets the personal_email of this ExternalContact.


        :param personal_email: The personal_email of this ExternalContact.
        :type: str
        """
        
        self._personal_email = personal_email

    @property
    def other_email(self):
        """
        Gets the other_email of this ExternalContact.


        :return: The other_email of this ExternalContact.
        :rtype: str
        """
        return self._other_email

    @other_email.setter
    def other_email(self, other_email):
        """
        Sets the other_email of this ExternalContact.


        :param other_email: The other_email of this ExternalContact.
        :type: str
        """
        
        self._other_email = other_email

    @property
    def address(self):
        """
        Gets the address of this ExternalContact.


        :return: The address of this ExternalContact.
        :rtype: ContactAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ExternalContact.


        :param address: The address of this ExternalContact.
        :type: ContactAddress
        """
        
        self._address = address

    @property
    def twitter_id(self):
        """
        Gets the twitter_id of this ExternalContact.


        :return: The twitter_id of this ExternalContact.
        :rtype: TwitterId
        """
        return self._twitter_id

    @twitter_id.setter
    def twitter_id(self, twitter_id):
        """
        Sets the twitter_id of this ExternalContact.


        :param twitter_id: The twitter_id of this ExternalContact.
        :type: TwitterId
        """
        
        self._twitter_id = twitter_id

    @property
    def line_id(self):
        """
        Gets the line_id of this ExternalContact.


        :return: The line_id of this ExternalContact.
        :rtype: LineId
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """
        Sets the line_id of this ExternalContact.


        :param line_id: The line_id of this ExternalContact.
        :type: LineId
        """
        
        self._line_id = line_id

    @property
    def whats_app_id(self):
        """
        Gets the whats_app_id of this ExternalContact.


        :return: The whats_app_id of this ExternalContact.
        :rtype: WhatsAppId
        """
        return self._whats_app_id

    @whats_app_id.setter
    def whats_app_id(self, whats_app_id):
        """
        Sets the whats_app_id of this ExternalContact.


        :param whats_app_id: The whats_app_id of this ExternalContact.
        :type: WhatsAppId
        """
        
        self._whats_app_id = whats_app_id

    @property
    def facebook_id(self):
        """
        Gets the facebook_id of this ExternalContact.


        :return: The facebook_id of this ExternalContact.
        :rtype: FacebookId
        """
        return self._facebook_id

    @facebook_id.setter
    def facebook_id(self, facebook_id):
        """
        Sets the facebook_id of this ExternalContact.


        :param facebook_id: The facebook_id of this ExternalContact.
        :type: FacebookId
        """
        
        self._facebook_id = facebook_id

    @property
    def modify_date(self):
        """
        Gets the modify_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modify_date of this ExternalContact.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modify_date: The modify_date of this ExternalContact.
        :type: datetime
        """
        
        self._modify_date = modify_date

    @property
    def create_date(self):
        """
        Gets the create_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The create_date of this ExternalContact.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param create_date: The create_date of this ExternalContact.
        :type: datetime
        """
        
        self._create_date = create_date

    @property
    def external_organization(self):
        """
        Gets the external_organization of this ExternalContact.


        :return: The external_organization of this ExternalContact.
        :rtype: ExternalOrganization
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization):
        """
        Sets the external_organization of this ExternalContact.


        :param external_organization: The external_organization of this ExternalContact.
        :type: ExternalOrganization
        """
        
        self._external_organization = external_organization

    @property
    def survey_opt_out(self):
        """
        Gets the survey_opt_out of this ExternalContact.


        :return: The survey_opt_out of this ExternalContact.
        :rtype: bool
        """
        return self._survey_opt_out

    @survey_opt_out.setter
    def survey_opt_out(self, survey_opt_out):
        """
        Sets the survey_opt_out of this ExternalContact.


        :param survey_opt_out: The survey_opt_out of this ExternalContact.
        :type: bool
        """
        
        self._survey_opt_out = survey_opt_out

    @property
    def external_system_url(self):
        """
        Gets the external_system_url of this ExternalContact.
        A string that identifies an external system-of-record resource that may have more detailed information on the contact. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :return: The external_system_url of this ExternalContact.
        :rtype: str
        """
        return self._external_system_url

    @external_system_url.setter
    def external_system_url(self, external_system_url):
        """
        Sets the external_system_url of this ExternalContact.
        A string that identifies an external system-of-record resource that may have more detailed information on the contact. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :param external_system_url: The external_system_url of this ExternalContact.
        :type: str
        """
        
        self._external_system_url = external_system_url

    @property
    def schema(self):
        """
        Gets the schema of this ExternalContact.
        The schema defining custom fields for this contact

        :return: The schema of this ExternalContact.
        :rtype: DataSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this ExternalContact.
        The schema defining custom fields for this contact

        :param schema: The schema of this ExternalContact.
        :type: DataSchema
        """
        
        self._schema = schema

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this ExternalContact.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :return: The custom_fields of this ExternalContact.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this ExternalContact.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :param custom_fields: The custom_fields of this ExternalContact.
        :type: dict(str, object)
        """
        
        self._custom_fields = custom_fields

    @property
    def external_data_sources(self):
        """
        Gets the external_data_sources of this ExternalContact.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :return: The external_data_sources of this ExternalContact.
        :rtype: list[ExternalDataSource]
        """
        return self._external_data_sources

    @external_data_sources.setter
    def external_data_sources(self, external_data_sources):
        """
        Sets the external_data_sources of this ExternalContact.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :param external_data_sources: The external_data_sources of this ExternalContact.
        :type: list[ExternalDataSource]
        """
        
        self._external_data_sources = external_data_sources

    @property
    def self_uri(self):
        """
        Gets the self_uri of this ExternalContact.
        The URI for this object

        :return: The self_uri of this ExternalContact.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this ExternalContact.
        The URI for this object

        :param self_uri: The self_uri of this ExternalContact.
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

