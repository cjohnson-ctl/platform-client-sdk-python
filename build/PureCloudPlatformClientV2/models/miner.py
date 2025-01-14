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

class Miner(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Miner - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'language': 'str',
            'date_created': 'datetime',
            'status': 'str',
            'conversations_date_range_start': 'date',
            'conversations_date_range_end': 'date',
            'date_completed': 'datetime',
            'message': 'str',
            'conversation_data_uploaded': 'bool',
            'media_type': 'str',
            'queue_ids': 'list[str]',
            'date_triggered': 'datetime',
            'date_modified': 'datetime',
            'latest_draft_version': 'Draft',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'language': 'language',
            'date_created': 'dateCreated',
            'status': 'status',
            'conversations_date_range_start': 'conversationsDateRangeStart',
            'conversations_date_range_end': 'conversationsDateRangeEnd',
            'date_completed': 'dateCompleted',
            'message': 'message',
            'conversation_data_uploaded': 'conversationDataUploaded',
            'media_type': 'mediaType',
            'queue_ids': 'queueIds',
            'date_triggered': 'dateTriggered',
            'date_modified': 'dateModified',
            'latest_draft_version': 'latestDraftVersion',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._language = None
        self._date_created = None
        self._status = None
        self._conversations_date_range_start = None
        self._conversations_date_range_end = None
        self._date_completed = None
        self._message = None
        self._conversation_data_uploaded = None
        self._media_type = None
        self._queue_ids = None
        self._date_triggered = None
        self._date_modified = None
        self._latest_draft_version = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Miner.
        The globally unique identifier for the object.

        :return: The id of this Miner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Miner.
        The globally unique identifier for the object.

        :param id: The id of this Miner.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Miner.
        Chat Corpus Name.

        :return: The name of this Miner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Miner.
        Chat Corpus Name.

        :param name: The name of this Miner.
        :type: str
        """
        
        self._name = name

    @property
    def language(self):
        """
        Gets the language of this Miner.
        Language Localization code.

        :return: The language of this Miner.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Miner.
        Language Localization code.

        :param language: The language of this Miner.
        :type: str
        """
        allowed_values = ["en-us"]
        if language.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language -> " + language)
            self._language = "outdated_sdk_version"
        else:
            self._language = language

    @property
    def date_created(self):
        """
        Gets the date_created of this Miner.
        Date when the miner was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Miner.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Miner.
        Date when the miner was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Miner.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def status(self):
        """
        Gets the status of this Miner.
        Status of the miner.

        :return: The status of this Miner.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Miner.
        Status of the miner.

        :param status: The status of this Miner.
        :type: str
        """
        allowed_values = ["NotStarted", "FetchingConversationIds", "ConversationIdsFetched", "ConversationIdsFetchError", "FetchingConversations", "ConversationsFetched", "ConversationsFetchError", "Queued", "QueuingError", "MiningStarted", "MaskingUtterances", "MaskingError", "ComputingAnalytics", "ComputingAnalyticsError", "MiningCompleted", "MiningError", "ModelValidationError", "Deleted"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def conversations_date_range_start(self):
        """
        Gets the conversations_date_range_start of this Miner.
        Date from which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The conversations_date_range_start of this Miner.
        :rtype: date
        """
        return self._conversations_date_range_start

    @conversations_date_range_start.setter
    def conversations_date_range_start(self, conversations_date_range_start):
        """
        Sets the conversations_date_range_start of this Miner.
        Date from which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param conversations_date_range_start: The conversations_date_range_start of this Miner.
        :type: date
        """
        
        self._conversations_date_range_start = conversations_date_range_start

    @property
    def conversations_date_range_end(self):
        """
        Gets the conversations_date_range_end of this Miner.
        Date till which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The conversations_date_range_end of this Miner.
        :rtype: date
        """
        return self._conversations_date_range_end

    @conversations_date_range_end.setter
    def conversations_date_range_end(self, conversations_date_range_end):
        """
        Sets the conversations_date_range_end of this Miner.
        Date till which the conversations need to be taken for mining. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param conversations_date_range_end: The conversations_date_range_end of this Miner.
        :type: date
        """
        
        self._conversations_date_range_end = conversations_date_range_end

    @property
    def date_completed(self):
        """
        Gets the date_completed of this Miner.
        Date when the mining process was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_completed of this Miner.
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """
        Sets the date_completed of this Miner.
        Date when the mining process was completed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_completed: The date_completed of this Miner.
        :type: datetime
        """
        
        self._date_completed = date_completed

    @property
    def message(self):
        """
        Gets the message of this Miner.
        Mining message if present.

        :return: The message of this Miner.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Miner.
        Mining message if present.

        :param message: The message of this Miner.
        :type: str
        """
        
        self._message = message

    @property
    def conversation_data_uploaded(self):
        """
        Gets the conversation_data_uploaded of this Miner.
        Flag to indicate whether data file to be mined was uploaded.

        :return: The conversation_data_uploaded of this Miner.
        :rtype: bool
        """
        return self._conversation_data_uploaded

    @conversation_data_uploaded.setter
    def conversation_data_uploaded(self, conversation_data_uploaded):
        """
        Sets the conversation_data_uploaded of this Miner.
        Flag to indicate whether data file to be mined was uploaded.

        :param conversation_data_uploaded: The conversation_data_uploaded of this Miner.
        :type: bool
        """
        
        self._conversation_data_uploaded = conversation_data_uploaded

    @property
    def media_type(self):
        """
        Gets the media_type of this Miner.
        Media type for filtering conversations.

        :return: The media_type of this Miner.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this Miner.
        Media type for filtering conversations.

        :param media_type: The media_type of this Miner.
        :type: str
        """
        allowed_values = ["Chat", "Call"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def queue_ids(self):
        """
        Gets the queue_ids of this Miner.
        List of queue IDs for filtering conversations.

        :return: The queue_ids of this Miner.
        :rtype: list[str]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids):
        """
        Sets the queue_ids of this Miner.
        List of queue IDs for filtering conversations.

        :param queue_ids: The queue_ids of this Miner.
        :type: list[str]
        """
        
        self._queue_ids = queue_ids

    @property
    def date_triggered(self):
        """
        Gets the date_triggered of this Miner.
        Date when the miner started execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_triggered of this Miner.
        :rtype: datetime
        """
        return self._date_triggered

    @date_triggered.setter
    def date_triggered(self, date_triggered):
        """
        Sets the date_triggered of this Miner.
        Date when the miner started execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_triggered: The date_triggered of this Miner.
        :type: datetime
        """
        
        self._date_triggered = date_triggered

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Miner.
        Date when the miner was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Miner.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Miner.
        Date when the miner was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Miner.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def latest_draft_version(self):
        """
        Gets the latest_draft_version of this Miner.
        Latest draft details of the miner.

        :return: The latest_draft_version of this Miner.
        :rtype: Draft
        """
        return self._latest_draft_version

    @latest_draft_version.setter
    def latest_draft_version(self, latest_draft_version):
        """
        Sets the latest_draft_version of this Miner.
        Latest draft details of the miner.

        :param latest_draft_version: The latest_draft_version of this Miner.
        :type: Draft
        """
        
        self._latest_draft_version = latest_draft_version

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Miner.
        The URI for this object

        :return: The self_uri of this Miner.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Miner.
        The URI for this object

        :param self_uri: The self_uri of this Miner.
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

