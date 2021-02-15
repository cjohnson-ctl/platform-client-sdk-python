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

class AuditLogMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuditLogMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_home_org_id': 'str',
            'user': 'DomainEntityRef',
            'client': 'AddressableEntityRef',
            'remote_ip': 'list[str]',
            'service_name': 'str',
            'event_date': 'datetime',
            'message': 'MessageInfo',
            'action': 'str',
            'entity': 'DomainEntityRef',
            'entity_type': 'str',
            'property_changes': 'list[PropertyChange]',
            'context': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'user_home_org_id': 'userHomeOrgId',
            'user': 'user',
            'client': 'client',
            'remote_ip': 'remoteIp',
            'service_name': 'serviceName',
            'event_date': 'eventDate',
            'message': 'message',
            'action': 'action',
            'entity': 'entity',
            'entity_type': 'entityType',
            'property_changes': 'propertyChanges',
            'context': 'context'
        }

        self._id = None
        self._user_home_org_id = None
        self._user = None
        self._client = None
        self._remote_ip = None
        self._service_name = None
        self._event_date = None
        self._message = None
        self._action = None
        self._entity = None
        self._entity_type = None
        self._property_changes = None
        self._context = None

    @property
    def id(self):
        """
        Gets the id of this AuditLogMessage.
        Id of the audit message.

        :return: The id of this AuditLogMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditLogMessage.
        Id of the audit message.

        :param id: The id of this AuditLogMessage.
        :type: str
        """
        
        self._id = id

    @property
    def user_home_org_id(self):
        """
        Gets the user_home_org_id of this AuditLogMessage.
        Home Organization Id associated with this audit message.

        :return: The user_home_org_id of this AuditLogMessage.
        :rtype: str
        """
        return self._user_home_org_id

    @user_home_org_id.setter
    def user_home_org_id(self, user_home_org_id):
        """
        Sets the user_home_org_id of this AuditLogMessage.
        Home Organization Id associated with this audit message.

        :param user_home_org_id: The user_home_org_id of this AuditLogMessage.
        :type: str
        """
        
        self._user_home_org_id = user_home_org_id

    @property
    def user(self):
        """
        Gets the user of this AuditLogMessage.
        User associated with this audit message.

        :return: The user of this AuditLogMessage.
        :rtype: DomainEntityRef
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AuditLogMessage.
        User associated with this audit message.

        :param user: The user of this AuditLogMessage.
        :type: DomainEntityRef
        """
        
        self._user = user

    @property
    def client(self):
        """
        Gets the client of this AuditLogMessage.
        Client associated with this audit message.

        :return: The client of this AuditLogMessage.
        :rtype: AddressableEntityRef
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this AuditLogMessage.
        Client associated with this audit message.

        :param client: The client of this AuditLogMessage.
        :type: AddressableEntityRef
        """
        
        self._client = client

    @property
    def remote_ip(self):
        """
        Gets the remote_ip of this AuditLogMessage.
        List of IP addresses of systems that originated or handled the request.

        :return: The remote_ip of this AuditLogMessage.
        :rtype: list[str]
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """
        Sets the remote_ip of this AuditLogMessage.
        List of IP addresses of systems that originated or handled the request.

        :param remote_ip: The remote_ip of this AuditLogMessage.
        :type: list[str]
        """
        
        self._remote_ip = remote_ip

    @property
    def service_name(self):
        """
        Gets the service_name of this AuditLogMessage.
        Name of the service that logged this audit message.

        :return: The service_name of this AuditLogMessage.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this AuditLogMessage.
        Name of the service that logged this audit message.

        :param service_name: The service_name of this AuditLogMessage.
        :type: str
        """
        allowed_values = ["Architect", "ContactCenter", "ContentManagement", "PeoplePermissions", "Presence", "Quality", "LanguageUnderstanding", "TopicsDefinitions", "PredictiveEngagement", "WorkforceManagement", "Triggers", "ResponseManagement", "Groups", "Telephony", "Outbound", "SpeechAndTextAnalytics"]
        if service_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for service_name -> " + service_name)
            self._service_name = "outdated_sdk_version"
        else:
            self._service_name = service_name

    @property
    def event_date(self):
        """
        Gets the event_date of this AuditLogMessage.
        Date and time of when the audit message was logged. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_date of this AuditLogMessage.
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """
        Sets the event_date of this AuditLogMessage.
        Date and time of when the audit message was logged. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_date: The event_date of this AuditLogMessage.
        :type: datetime
        """
        
        self._event_date = event_date

    @property
    def message(self):
        """
        Gets the message of this AuditLogMessage.
        Message describing the event being audited.

        :return: The message of this AuditLogMessage.
        :rtype: MessageInfo
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AuditLogMessage.
        Message describing the event being audited.

        :param message: The message of this AuditLogMessage.
        :type: MessageInfo
        """
        
        self._message = message

    @property
    def action(self):
        """
        Gets the action of this AuditLogMessage.
        Action that took place.

        :return: The action of this AuditLogMessage.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AuditLogMessage.
        Action that took place.

        :param action: The action of this AuditLogMessage.
        :type: str
        """
        allowed_values = ["Create", "View", "Update", "Delete", "Download", "Upload", "MemberAdd", "MemberUpdate", "MemberRemove", "Read", "ApplyProtection", "RevokeProtection", "UpdateRetention", "ReadAll", "Execute", "Publish", "Unpublish", "Activate", "Checkin", "Checkout", "Deactivate", "Debug", "Save", "Revert", "Transcode", "Enable", "Disable", "Authorize", "Deauthorize", "Authenticate", "ChangePassword", "Revoke", "Export", "Append", "Recycle"]
        if action.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action -> " + action)
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def entity(self):
        """
        Gets the entity of this AuditLogMessage.
        Entity that was impacted.

        :return: The entity of this AuditLogMessage.
        :rtype: DomainEntityRef
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this AuditLogMessage.
        Entity that was impacted.

        :param entity: The entity of this AuditLogMessage.
        :type: DomainEntityRef
        """
        
        self._entity = entity

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AuditLogMessage.
        Type of the entity that was impacted.

        :return: The entity_type of this AuditLogMessage.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AuditLogMessage.
        Type of the entity that was impacted.

        :param entity_type: The entity_type of this AuditLogMessage.
        :type: str
        """
        allowed_values = ["Document", "Queue", "Recording", "Role", "VoicemailUserPolicy", "UserPresence", "WrapupCode", "MaxOrgRoutingUtilizationCapacity", "AccessToken", "OAuthClient", "OAuthClientAuthorization", "AuthOrganization", "AuthUser", "OrganizationAuthorizationTrust", "OrganizationAuthorizationUserTrust", "BulkActions", "Feedback", "Topic", "Program", "Segment", "Outcome", "SessionType", "EventType", "ClickstreamSettings", "Schedule", "ScheduleGroup", "EmergencyGroup", "IVR", "Trigger", "Response", "DependencyTrackingBuild", "Flow", "Prompt", "PromptResource", "FlowOutcome", "FlowMilestone", "Team", "Edge", "EdgeGroup", "Trunk", "TrunkBase", "DID", "DIDPool", "Extension", "ExtensionPool", "Phone", "PhoneBase", "Line", "LineBase", "OutboundRoute", "NumberPlan", "Site", "AttemptLimits", "CallableTimeSet", "Campaign", "CampaignRule", "Sequence", "ContactList", "ContactListFilter", "DNCList", "CallAnalysisResponseSet", "RuleSet", "TranscriptionSettings", "SpeechTextAnalyticsSettings"]
        if entity_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for entity_type -> " + entity_type)
            self._entity_type = "outdated_sdk_version"
        else:
            self._entity_type = entity_type

    @property
    def property_changes(self):
        """
        Gets the property_changes of this AuditLogMessage.
        List of properties that were changed and changes made to those properties.

        :return: The property_changes of this AuditLogMessage.
        :rtype: list[PropertyChange]
        """
        return self._property_changes

    @property_changes.setter
    def property_changes(self, property_changes):
        """
        Sets the property_changes of this AuditLogMessage.
        List of properties that were changed and changes made to those properties.

        :param property_changes: The property_changes of this AuditLogMessage.
        :type: list[PropertyChange]
        """
        
        self._property_changes = property_changes

    @property
    def context(self):
        """
        Gets the context of this AuditLogMessage.
        Additional context for this message.

        :return: The context of this AuditLogMessage.
        :rtype: dict(str, str)
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this AuditLogMessage.
        Additional context for this message.

        :param context: The context of this AuditLogMessage.
        :type: dict(str, str)
        """
        
        self._context = context

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

