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

class OutboundDomain(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OutboundDomain - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'cname_verification_result': 'VerificationResult',
            'dkim_verification_result': 'VerificationResult',
            'from_email': 'EmailAddress',
            'reply_to_email': 'EmailAddress',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'cname_verification_result': 'cnameVerificationResult',
            'dkim_verification_result': 'dkimVerificationResult',
            'from_email': 'fromEmail',
            'reply_to_email': 'replyToEmail',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._cname_verification_result = None
        self._dkim_verification_result = None
        self._from_email = None
        self._reply_to_email = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this OutboundDomain.
        Unique Id of the domain such as: example.com

        :return: The id of this OutboundDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OutboundDomain.
        Unique Id of the domain such as: example.com

        :param id: The id of this OutboundDomain.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OutboundDomain.


        :return: The name of this OutboundDomain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OutboundDomain.


        :param name: The name of this OutboundDomain.
        :type: str
        """
        
        self._name = name

    @property
    def cname_verification_result(self):
        """
        Gets the cname_verification_result of this OutboundDomain.
        CNAME registration Status

        :return: The cname_verification_result of this OutboundDomain.
        :rtype: VerificationResult
        """
        return self._cname_verification_result

    @cname_verification_result.setter
    def cname_verification_result(self, cname_verification_result):
        """
        Sets the cname_verification_result of this OutboundDomain.
        CNAME registration Status

        :param cname_verification_result: The cname_verification_result of this OutboundDomain.
        :type: VerificationResult
        """
        
        self._cname_verification_result = cname_verification_result

    @property
    def dkim_verification_result(self):
        """
        Gets the dkim_verification_result of this OutboundDomain.
        DKIM registration Status

        :return: The dkim_verification_result of this OutboundDomain.
        :rtype: VerificationResult
        """
        return self._dkim_verification_result

    @dkim_verification_result.setter
    def dkim_verification_result(self, dkim_verification_result):
        """
        Sets the dkim_verification_result of this OutboundDomain.
        DKIM registration Status

        :param dkim_verification_result: The dkim_verification_result of this OutboundDomain.
        :type: VerificationResult
        """
        
        self._dkim_verification_result = dkim_verification_result

    @property
    def from_email(self):
        """
        Gets the from_email of this OutboundDomain.
        The email that is used to display sender informations

        :return: The from_email of this OutboundDomain.
        :rtype: EmailAddress
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """
        Sets the from_email of this OutboundDomain.
        The email that is used to display sender informations

        :param from_email: The from_email of this OutboundDomain.
        :type: EmailAddress
        """
        
        self._from_email = from_email

    @property
    def reply_to_email(self):
        """
        Gets the reply_to_email of this OutboundDomain.
        The email that is used if replies are expected

        :return: The reply_to_email of this OutboundDomain.
        :rtype: EmailAddress
        """
        return self._reply_to_email

    @reply_to_email.setter
    def reply_to_email(self, reply_to_email):
        """
        Sets the reply_to_email of this OutboundDomain.
        The email that is used if replies are expected

        :param reply_to_email: The reply_to_email of this OutboundDomain.
        :type: EmailAddress
        """
        
        self._reply_to_email = reply_to_email

    @property
    def self_uri(self):
        """
        Gets the self_uri of this OutboundDomain.
        The URI for this object

        :return: The self_uri of this OutboundDomain.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this OutboundDomain.
        The URI for this object

        :param self_uri: The self_uri of this OutboundDomain.
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

