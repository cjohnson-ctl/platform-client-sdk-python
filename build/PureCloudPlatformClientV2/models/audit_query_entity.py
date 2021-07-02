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

class AuditQueryEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuditQueryEntity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'actions': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'actions': 'actions'
        }

        self._name = None
        self._actions = None

    @property
    def name(self):
        """
        Gets the name of this AuditQueryEntity.
        Name of the Entity

        :return: The name of this AuditQueryEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuditQueryEntity.
        Name of the Entity

        :param name: The name of this AuditQueryEntity.
        :type: str
        """
        allowed_values = ["AccessToken", "ActionMap", "ActionTemplate", "Annotation", "Appointment", "AttemptLimits", "AuthOrganization", "AuthUser", "Bulk", "BulkActions", "Calibration", "CallableTimeSet", "CallAnalysisResponseSet", "Campaign", "CampaignRule", "CampaignSchedule", "ChangeRequest", "ClickstreamSettings", "Configuration", "ConfigurationVersion", "ContactList", "ContactListFilter", "ConversationAccount", "ConversationDefaultSupportedContent", "ConversationPhoneNumber", "ConversationRecipient", "ConversationThreadingWindow", "DashboardSettings", "DependencyTrackingBuild", "Deployment", "DID", "DIDPool", "DNCList", "Document", "Edge", "EdgeGroup", "EdgeLog", "EdgeLogZip", "EdgePcaps", "EdgePreferences", "EdgeTraceLevel", "EmergencyGroup", "Evaluation", "EvaluationForm", "EventType", "Exports", "Extension", "ExtensionPool", "ExternalMetricsData", "ExternalMetricsDefinition", "Feedback", "Flow", "FlowMilestone", "FlowOutcome", "Forecast", "HistoricalData", "InsightSettings", "Integration", "IVR", "Line", "LineBase", "MaxOrgRoutingUtilizationCapacity", "MediaDiagnosticsTraceFile", "MessagingCampaign", "Metric", "NumberPlan", "OAuthClient", "OAuthClientAuthorization", "OrganizationAuthorizationTrust", "OrganizationAuthorizationUserTrust", "OrganizationFeature", "OrganizationIntegrationsAccess", "OrganizationSettings", "OrphanedRecording", "OutboundRoute", "Outcome", "Pcaps", "Phone", "PhoneBase", "Policy", "Predictor", "Product", "Program", "Prompt", "PromptResource", "Queue", "Recording", "RecordingAnnotation", "RecordingSettings", "Response", "Role", "Row", "RoutingTranscriptionSettings", "RuleSet", "Schedule", "ScheduledExports", "ScheduleGroup", "Schema", "ScreenRecording", "Segment", "SentimentFeedback", "Sequence", "SequenceSchedule", "SessionType", "Site", "SpeechTextAnalyticsSettings", "Status", "SupportedContent", "SupportFile", "Survey", "SurveyForm", "Team", "Topic", "TranscriptionSettings", "Trigger", "Trunk", "TrunkBase", "User", "UserPresence", "VoicemailPolicy", "VoicemailUserPolicy", "Webhook", "WorkPlan", "Workspace", "WrapupCode", "WrapUpCodeMapping"]
        if name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for name -> " + name)
            self._name = "outdated_sdk_version"
        else:
            self._name = name

    @property
    def actions(self):
        """
        Gets the actions of this AuditQueryEntity.
        List of Actions

        :return: The actions of this AuditQueryEntity.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this AuditQueryEntity.
        List of Actions

        :param actions: The actions of this AuditQueryEntity.
        :type: list[str]
        """
        
        self._actions = actions

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

