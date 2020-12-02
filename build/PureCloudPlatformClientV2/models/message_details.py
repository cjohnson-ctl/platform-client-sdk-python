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

class MessageDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message_id': 'str',
            'message_uri': 'str',
            'message_status': 'str',
            'message_segment_count': 'int',
            'message_time': 'datetime',
            'media': 'list[MessageMedia]',
            'stickers': 'list[MessageSticker]'
        }

        self.attribute_map = {
            'message_id': 'messageId',
            'message_uri': 'messageURI',
            'message_status': 'messageStatus',
            'message_segment_count': 'messageSegmentCount',
            'message_time': 'messageTime',
            'media': 'media',
            'stickers': 'stickers'
        }

        self._message_id = None
        self._message_uri = None
        self._message_status = None
        self._message_segment_count = None
        self._message_time = None
        self._media = None
        self._stickers = None

    @property
    def message_id(self):
        """
        Gets the message_id of this MessageDetails.
        UUID identifying the message media.

        :return: The message_id of this MessageDetails.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this MessageDetails.
        UUID identifying the message media.

        :param message_id: The message_id of this MessageDetails.
        :type: str
        """
        
        self._message_id = message_id

    @property
    def message_uri(self):
        """
        Gets the message_uri of this MessageDetails.
        A URI for this message entity.

        :return: The message_uri of this MessageDetails.
        :rtype: str
        """
        return self._message_uri

    @message_uri.setter
    def message_uri(self, message_uri):
        """
        Sets the message_uri of this MessageDetails.
        A URI for this message entity.

        :param message_uri: The message_uri of this MessageDetails.
        :type: str
        """
        
        self._message_uri = message_uri

    @property
    def message_status(self):
        """
        Gets the message_status of this MessageDetails.
        Indicates the delivery status of the message.

        :return: The message_status of this MessageDetails.
        :rtype: str
        """
        return self._message_status

    @message_status.setter
    def message_status(self, message_status):
        """
        Sets the message_status of this MessageDetails.
        Indicates the delivery status of the message.

        :param message_status: The message_status of this MessageDetails.
        :type: str
        """
        allowed_values = ["queued", "sent", "failed", "received", "delivery-success", "delivery-failed", "read"]
        if message_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_status -> " + message_status)
            self._message_status = "outdated_sdk_version"
        else:
            self._message_status = message_status

    @property
    def message_segment_count(self):
        """
        Gets the message_segment_count of this MessageDetails.
        The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits.

        :return: The message_segment_count of this MessageDetails.
        :rtype: int
        """
        return self._message_segment_count

    @message_segment_count.setter
    def message_segment_count(self, message_segment_count):
        """
        Sets the message_segment_count of this MessageDetails.
        The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits.

        :param message_segment_count: The message_segment_count of this MessageDetails.
        :type: int
        """
        
        self._message_segment_count = message_segment_count

    @property
    def message_time(self):
        """
        Gets the message_time of this MessageDetails.
        The time when the message was sent or received. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The message_time of this MessageDetails.
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time):
        """
        Sets the message_time of this MessageDetails.
        The time when the message was sent or received. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param message_time: The message_time of this MessageDetails.
        :type: datetime
        """
        
        self._message_time = message_time

    @property
    def media(self):
        """
        Gets the media of this MessageDetails.
        The media (images, files, etc) associated with this message, if any

        :return: The media of this MessageDetails.
        :rtype: list[MessageMedia]
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this MessageDetails.
        The media (images, files, etc) associated with this message, if any

        :param media: The media of this MessageDetails.
        :type: list[MessageMedia]
        """
        
        self._media = media

    @property
    def stickers(self):
        """
        Gets the stickers of this MessageDetails.
        One or more stickers associated with this message, if any

        :return: The stickers of this MessageDetails.
        :rtype: list[MessageSticker]
        """
        return self._stickers

    @stickers.setter
    def stickers(self, stickers):
        """
        Sets the stickers of this MessageDetails.
        One or more stickers associated with this message, if any

        :param stickers: The stickers of this MessageDetails.
        :type: list[MessageSticker]
        """
        
        self._stickers = stickers

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

