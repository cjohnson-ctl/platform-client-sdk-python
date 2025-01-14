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

class MinerIntent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MinerIntent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'miner': 'Miner',
            'utterances': 'list[Utterance]',
            'analytic_volume_percent': 'float',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'miner': 'miner',
            'utterances': 'utterances',
            'analytic_volume_percent': 'analyticVolumePercent',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._miner = None
        self._utterances = None
        self._analytic_volume_percent = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this MinerIntent.
        The globally unique identifier for the object.

        :return: The id of this MinerIntent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MinerIntent.
        The globally unique identifier for the object.

        :param id: The id of this MinerIntent.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MinerIntent.
        Intent name.

        :return: The name of this MinerIntent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MinerIntent.
        Intent name.

        :param name: The name of this MinerIntent.
        :type: str
        """
        
        self._name = name

    @property
    def miner(self):
        """
        Gets the miner of this MinerIntent.
        The miner to which the intent belongs.

        :return: The miner of this MinerIntent.
        :rtype: Miner
        """
        return self._miner

    @miner.setter
    def miner(self, miner):
        """
        Sets the miner of this MinerIntent.
        The miner to which the intent belongs.

        :param miner: The miner of this MinerIntent.
        :type: Miner
        """
        
        self._miner = miner

    @property
    def utterances(self):
        """
        Gets the utterances of this MinerIntent.
        The utterances that are extracted for an Intent.

        :return: The utterances of this MinerIntent.
        :rtype: list[Utterance]
        """
        return self._utterances

    @utterances.setter
    def utterances(self, utterances):
        """
        Sets the utterances of this MinerIntent.
        The utterances that are extracted for an Intent.

        :param utterances: The utterances of this MinerIntent.
        :type: list[Utterance]
        """
        
        self._utterances = utterances

    @property
    def analytic_volume_percent(self):
        """
        Gets the analytic_volume_percent of this MinerIntent.
        Percentage of conversations belonging to the intent.

        :return: The analytic_volume_percent of this MinerIntent.
        :rtype: float
        """
        return self._analytic_volume_percent

    @analytic_volume_percent.setter
    def analytic_volume_percent(self, analytic_volume_percent):
        """
        Sets the analytic_volume_percent of this MinerIntent.
        Percentage of conversations belonging to the intent.

        :param analytic_volume_percent: The analytic_volume_percent of this MinerIntent.
        :type: float
        """
        
        self._analytic_volume_percent = analytic_volume_percent

    @property
    def self_uri(self):
        """
        Gets the self_uri of this MinerIntent.
        The URI for this object

        :return: The self_uri of this MinerIntent.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this MinerIntent.
        The URI for this object

        :param self_uri: The self_uri of this MinerIntent.
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

