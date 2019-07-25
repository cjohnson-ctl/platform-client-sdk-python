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

class DomainPermissionPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainPermissionPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'domain': 'str',
            'entity_name': 'str',
            'policy_name': 'str',
            'policy_description': 'str',
            'action_set': 'list[str]',
            'named_resources': 'list[str]',
            'allow_conditions': 'bool',
            'resource_condition_node': 'DomainResourceConditionNode'
        }

        self.attribute_map = {
            'domain': 'domain',
            'entity_name': 'entityName',
            'policy_name': 'policyName',
            'policy_description': 'policyDescription',
            'action_set': 'actionSet',
            'named_resources': 'namedResources',
            'allow_conditions': 'allowConditions',
            'resource_condition_node': 'resourceConditionNode'
        }

        self._domain = None
        self._entity_name = None
        self._policy_name = None
        self._policy_description = None
        self._action_set = None
        self._named_resources = None
        self._allow_conditions = None
        self._resource_condition_node = None

    @property
    def domain(self):
        """
        Gets the domain of this DomainPermissionPolicy.


        :return: The domain of this DomainPermissionPolicy.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this DomainPermissionPolicy.


        :param domain: The domain of this DomainPermissionPolicy.
        :type: str
        """
        
        self._domain = domain

    @property
    def entity_name(self):
        """
        Gets the entity_name of this DomainPermissionPolicy.


        :return: The entity_name of this DomainPermissionPolicy.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this DomainPermissionPolicy.


        :param entity_name: The entity_name of this DomainPermissionPolicy.
        :type: str
        """
        
        self._entity_name = entity_name

    @property
    def policy_name(self):
        """
        Gets the policy_name of this DomainPermissionPolicy.


        :return: The policy_name of this DomainPermissionPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this DomainPermissionPolicy.


        :param policy_name: The policy_name of this DomainPermissionPolicy.
        :type: str
        """
        
        self._policy_name = policy_name

    @property
    def policy_description(self):
        """
        Gets the policy_description of this DomainPermissionPolicy.


        :return: The policy_description of this DomainPermissionPolicy.
        :rtype: str
        """
        return self._policy_description

    @policy_description.setter
    def policy_description(self, policy_description):
        """
        Sets the policy_description of this DomainPermissionPolicy.


        :param policy_description: The policy_description of this DomainPermissionPolicy.
        :type: str
        """
        
        self._policy_description = policy_description

    @property
    def action_set(self):
        """
        Gets the action_set of this DomainPermissionPolicy.


        :return: The action_set of this DomainPermissionPolicy.
        :rtype: list[str]
        """
        return self._action_set

    @action_set.setter
    def action_set(self, action_set):
        """
        Sets the action_set of this DomainPermissionPolicy.


        :param action_set: The action_set of this DomainPermissionPolicy.
        :type: list[str]
        """
        
        self._action_set = action_set

    @property
    def named_resources(self):
        """
        Gets the named_resources of this DomainPermissionPolicy.


        :return: The named_resources of this DomainPermissionPolicy.
        :rtype: list[str]
        """
        return self._named_resources

    @named_resources.setter
    def named_resources(self, named_resources):
        """
        Sets the named_resources of this DomainPermissionPolicy.


        :param named_resources: The named_resources of this DomainPermissionPolicy.
        :type: list[str]
        """
        
        self._named_resources = named_resources

    @property
    def allow_conditions(self):
        """
        Gets the allow_conditions of this DomainPermissionPolicy.


        :return: The allow_conditions of this DomainPermissionPolicy.
        :rtype: bool
        """
        return self._allow_conditions

    @allow_conditions.setter
    def allow_conditions(self, allow_conditions):
        """
        Sets the allow_conditions of this DomainPermissionPolicy.


        :param allow_conditions: The allow_conditions of this DomainPermissionPolicy.
        :type: bool
        """
        
        self._allow_conditions = allow_conditions

    @property
    def resource_condition_node(self):
        """
        Gets the resource_condition_node of this DomainPermissionPolicy.


        :return: The resource_condition_node of this DomainPermissionPolicy.
        :rtype: DomainResourceConditionNode
        """
        return self._resource_condition_node

    @resource_condition_node.setter
    def resource_condition_node(self, resource_condition_node):
        """
        Sets the resource_condition_node of this DomainPermissionPolicy.


        :param resource_condition_node: The resource_condition_node of this DomainPermissionPolicy.
        :type: DomainResourceConditionNode
        """
        
        self._resource_condition_node = resource_condition_node

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

