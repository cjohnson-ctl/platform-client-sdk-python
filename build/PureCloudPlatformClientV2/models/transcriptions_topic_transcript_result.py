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

class TranscriptionsTopicTranscriptResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TranscriptionsTopicTranscriptResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'utterance_id': 'str',
            'is_final': 'bool',
            'channel': 'str',
            'alternatives': 'list[TranscriptionsTopicTranscriptAlternative]',
            'agent_assistant_id': 'str',
            'engine_id': 'str',
            'dialect': 'str',
            'speech_text_analytics_program_id': 'str',
            'start_time_ms': 'int',
            'offset_ms': 'int',
            'duration_ms': 'int',
            'agent_assist_enabled': 'bool',
            'voice_transcription_enabled': 'bool'
        }

        self.attribute_map = {
            'utterance_id': 'utteranceId',
            'is_final': 'isFinal',
            'channel': 'channel',
            'alternatives': 'alternatives',
            'agent_assistant_id': 'agentAssistantId',
            'engine_id': 'engineId',
            'dialect': 'dialect',
            'speech_text_analytics_program_id': 'speechTextAnalyticsProgramId',
            'start_time_ms': 'startTimeMs',
            'offset_ms': 'offsetMs',
            'duration_ms': 'durationMs',
            'agent_assist_enabled': 'agentAssistEnabled',
            'voice_transcription_enabled': 'voiceTranscriptionEnabled'
        }

        self._utterance_id = None
        self._is_final = None
        self._channel = None
        self._alternatives = None
        self._agent_assistant_id = None
        self._engine_id = None
        self._dialect = None
        self._speech_text_analytics_program_id = None
        self._start_time_ms = None
        self._offset_ms = None
        self._duration_ms = None
        self._agent_assist_enabled = None
        self._voice_transcription_enabled = None

    @property
    def utterance_id(self):
        """
        Gets the utterance_id of this TranscriptionsTopicTranscriptResult.


        :return: The utterance_id of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._utterance_id

    @utterance_id.setter
    def utterance_id(self, utterance_id):
        """
        Sets the utterance_id of this TranscriptionsTopicTranscriptResult.


        :param utterance_id: The utterance_id of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        
        self._utterance_id = utterance_id

    @property
    def is_final(self):
        """
        Gets the is_final of this TranscriptionsTopicTranscriptResult.


        :return: The is_final of this TranscriptionsTopicTranscriptResult.
        :rtype: bool
        """
        return self._is_final

    @is_final.setter
    def is_final(self, is_final):
        """
        Sets the is_final of this TranscriptionsTopicTranscriptResult.


        :param is_final: The is_final of this TranscriptionsTopicTranscriptResult.
        :type: bool
        """
        
        self._is_final = is_final

    @property
    def channel(self):
        """
        Gets the channel of this TranscriptionsTopicTranscriptResult.


        :return: The channel of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this TranscriptionsTopicTranscriptResult.


        :param channel: The channel of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        allowed_values = ["UNKNOWN", "INTERNAL", "EXTERNAL", "BOTH"]
        if channel.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for channel -> " + channel)
            self._channel = "outdated_sdk_version"
        else:
            self._channel = channel

    @property
    def alternatives(self):
        """
        Gets the alternatives of this TranscriptionsTopicTranscriptResult.


        :return: The alternatives of this TranscriptionsTopicTranscriptResult.
        :rtype: list[TranscriptionsTopicTranscriptAlternative]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives):
        """
        Sets the alternatives of this TranscriptionsTopicTranscriptResult.


        :param alternatives: The alternatives of this TranscriptionsTopicTranscriptResult.
        :type: list[TranscriptionsTopicTranscriptAlternative]
        """
        
        self._alternatives = alternatives

    @property
    def agent_assistant_id(self):
        """
        Gets the agent_assistant_id of this TranscriptionsTopicTranscriptResult.


        :return: The agent_assistant_id of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._agent_assistant_id

    @agent_assistant_id.setter
    def agent_assistant_id(self, agent_assistant_id):
        """
        Sets the agent_assistant_id of this TranscriptionsTopicTranscriptResult.


        :param agent_assistant_id: The agent_assistant_id of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        
        self._agent_assistant_id = agent_assistant_id

    @property
    def engine_id(self):
        """
        Gets the engine_id of this TranscriptionsTopicTranscriptResult.


        :return: The engine_id of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """
        Sets the engine_id of this TranscriptionsTopicTranscriptResult.


        :param engine_id: The engine_id of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        
        self._engine_id = engine_id

    @property
    def dialect(self):
        """
        Gets the dialect of this TranscriptionsTopicTranscriptResult.


        :return: The dialect of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """
        Sets the dialect of this TranscriptionsTopicTranscriptResult.


        :param dialect: The dialect of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        
        self._dialect = dialect

    @property
    def speech_text_analytics_program_id(self):
        """
        Gets the speech_text_analytics_program_id of this TranscriptionsTopicTranscriptResult.


        :return: The speech_text_analytics_program_id of this TranscriptionsTopicTranscriptResult.
        :rtype: str
        """
        return self._speech_text_analytics_program_id

    @speech_text_analytics_program_id.setter
    def speech_text_analytics_program_id(self, speech_text_analytics_program_id):
        """
        Sets the speech_text_analytics_program_id of this TranscriptionsTopicTranscriptResult.


        :param speech_text_analytics_program_id: The speech_text_analytics_program_id of this TranscriptionsTopicTranscriptResult.
        :type: str
        """
        
        self._speech_text_analytics_program_id = speech_text_analytics_program_id

    @property
    def start_time_ms(self):
        """
        Gets the start_time_ms of this TranscriptionsTopicTranscriptResult.


        :return: The start_time_ms of this TranscriptionsTopicTranscriptResult.
        :rtype: int
        """
        return self._start_time_ms

    @start_time_ms.setter
    def start_time_ms(self, start_time_ms):
        """
        Sets the start_time_ms of this TranscriptionsTopicTranscriptResult.


        :param start_time_ms: The start_time_ms of this TranscriptionsTopicTranscriptResult.
        :type: int
        """
        
        self._start_time_ms = start_time_ms

    @property
    def offset_ms(self):
        """
        Gets the offset_ms of this TranscriptionsTopicTranscriptResult.


        :return: The offset_ms of this TranscriptionsTopicTranscriptResult.
        :rtype: int
        """
        return self._offset_ms

    @offset_ms.setter
    def offset_ms(self, offset_ms):
        """
        Sets the offset_ms of this TranscriptionsTopicTranscriptResult.


        :param offset_ms: The offset_ms of this TranscriptionsTopicTranscriptResult.
        :type: int
        """
        
        self._offset_ms = offset_ms

    @property
    def duration_ms(self):
        """
        Gets the duration_ms of this TranscriptionsTopicTranscriptResult.


        :return: The duration_ms of this TranscriptionsTopicTranscriptResult.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """
        Sets the duration_ms of this TranscriptionsTopicTranscriptResult.


        :param duration_ms: The duration_ms of this TranscriptionsTopicTranscriptResult.
        :type: int
        """
        
        self._duration_ms = duration_ms

    @property
    def agent_assist_enabled(self):
        """
        Gets the agent_assist_enabled of this TranscriptionsTopicTranscriptResult.


        :return: The agent_assist_enabled of this TranscriptionsTopicTranscriptResult.
        :rtype: bool
        """
        return self._agent_assist_enabled

    @agent_assist_enabled.setter
    def agent_assist_enabled(self, agent_assist_enabled):
        """
        Sets the agent_assist_enabled of this TranscriptionsTopicTranscriptResult.


        :param agent_assist_enabled: The agent_assist_enabled of this TranscriptionsTopicTranscriptResult.
        :type: bool
        """
        
        self._agent_assist_enabled = agent_assist_enabled

    @property
    def voice_transcription_enabled(self):
        """
        Gets the voice_transcription_enabled of this TranscriptionsTopicTranscriptResult.


        :return: The voice_transcription_enabled of this TranscriptionsTopicTranscriptResult.
        :rtype: bool
        """
        return self._voice_transcription_enabled

    @voice_transcription_enabled.setter
    def voice_transcription_enabled(self, voice_transcription_enabled):
        """
        Sets the voice_transcription_enabled of this TranscriptionsTopicTranscriptResult.


        :param voice_transcription_enabled: The voice_transcription_enabled of this TranscriptionsTopicTranscriptResult.
        :type: bool
        """
        
        self._voice_transcription_enabled = voice_transcription_enabled

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

