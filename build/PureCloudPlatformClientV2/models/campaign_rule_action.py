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

class CampaignRuleAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignRuleAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'parameters': 'CampaignRuleParameters',
            'action_type': 'str',
            'campaign_rule_action_entities': 'CampaignRuleActionEntities'
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters',
            'action_type': 'actionType',
            'campaign_rule_action_entities': 'campaignRuleActionEntities'
        }

        self._id = None
        self._parameters = None
        self._action_type = None
        self._campaign_rule_action_entities = None

    @property
    def id(self):
        """
        Gets the id of this CampaignRuleAction.


        :return: The id of this CampaignRuleAction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignRuleAction.


        :param id: The id of this CampaignRuleAction.
        :type: str
        """
        
        self._id = id

    @property
    def parameters(self):
        """
        Gets the parameters of this CampaignRuleAction.
        The parameters for the CampaignRuleAction. Required for certain actionTypes.

        :return: The parameters of this CampaignRuleAction.
        :rtype: CampaignRuleParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CampaignRuleAction.
        The parameters for the CampaignRuleAction. Required for certain actionTypes.

        :param parameters: The parameters of this CampaignRuleAction.
        :type: CampaignRuleParameters
        """
        
        self._parameters = parameters

    @property
    def action_type(self):
        """
        Gets the action_type of this CampaignRuleAction.
        The action to take on the campaignRuleActionEntities.

        :return: The action_type of this CampaignRuleAction.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this CampaignRuleAction.
        The action to take on the campaignRuleActionEntities.

        :param action_type: The action_type of this CampaignRuleAction.
        :type: str
        """
        allowed_values = ["turnOnCampaign", "turnOffCampaign", "turnOnSequence", "turnOffSequence", "setCampaignPriority", "recycleCampaign", "setCampaignDialingMode"]
        if action_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for action_type -> " + action_type
            self._action_type = "outdated_sdk_version"
        else:
            self._action_type = action_type

    @property
    def campaign_rule_action_entities(self):
        """
        Gets the campaign_rule_action_entities of this CampaignRuleAction.
        The list of entities that this action will apply to.

        :return: The campaign_rule_action_entities of this CampaignRuleAction.
        :rtype: CampaignRuleActionEntities
        """
        return self._campaign_rule_action_entities

    @campaign_rule_action_entities.setter
    def campaign_rule_action_entities(self, campaign_rule_action_entities):
        """
        Sets the campaign_rule_action_entities of this CampaignRuleAction.
        The list of entities that this action will apply to.

        :param campaign_rule_action_entities: The campaign_rule_action_entities of this CampaignRuleAction.
        :type: CampaignRuleActionEntities
        """
        
        self._campaign_rule_action_entities = campaign_rule_action_entities

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

