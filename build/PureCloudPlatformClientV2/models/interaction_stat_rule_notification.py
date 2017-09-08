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


class InteractionStatRuleNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InteractionStatRuleNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'dimension': 'str',
            'dimension_value': 'str',
            'dimension_value_name': 'str',
            'metric': 'str',
            'media_type': 'str',
            'numeric_range': 'str',
            'statistic': 'str',
            'value': 'float',
            'in_alarm': 'bool',
            'enabled': 'bool',
            'notification_users': 'list[HeartBeatAlertNotificationNotificationUsers]',
            'alert_types': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'dimension': 'dimension',
            'dimension_value': 'dimensionValue',
            'dimension_value_name': 'dimensionValueName',
            'metric': 'metric',
            'media_type': 'mediaType',
            'numeric_range': 'numericRange',
            'statistic': 'statistic',
            'value': 'value',
            'in_alarm': 'inAlarm',
            'enabled': 'enabled',
            'notification_users': 'notificationUsers',
            'alert_types': 'alertTypes'
        }

        self._id = None
        self._name = None
        self._dimension = None
        self._dimension_value = None
        self._dimension_value_name = None
        self._metric = None
        self._media_type = None
        self._numeric_range = None
        self._statistic = None
        self._value = None
        self._in_alarm = None
        self._enabled = None
        self._notification_users = None
        self._alert_types = None

    @property
    def id(self):
        """
        Gets the id of this InteractionStatRuleNotification.


        :return: The id of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InteractionStatRuleNotification.


        :param id: The id of this InteractionStatRuleNotification.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InteractionStatRuleNotification.


        :return: The name of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InteractionStatRuleNotification.


        :param name: The name of this InteractionStatRuleNotification.
        :type: str
        """
        
        self._name = name

    @property
    def dimension(self):
        """
        Gets the dimension of this InteractionStatRuleNotification.


        :return: The dimension of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """
        Sets the dimension of this InteractionStatRuleNotification.


        :param dimension: The dimension of this InteractionStatRuleNotification.
        :type: str
        """
        allowed_values = ["queueId", "userId"]
        if dimension.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for dimension -> " + dimension
            self._dimension = "outdated_sdk_version"
        else:
            self._dimension = dimension

    @property
    def dimension_value(self):
        """
        Gets the dimension_value of this InteractionStatRuleNotification.


        :return: The dimension_value of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._dimension_value

    @dimension_value.setter
    def dimension_value(self, dimension_value):
        """
        Sets the dimension_value of this InteractionStatRuleNotification.


        :param dimension_value: The dimension_value of this InteractionStatRuleNotification.
        :type: str
        """
        
        self._dimension_value = dimension_value

    @property
    def dimension_value_name(self):
        """
        Gets the dimension_value_name of this InteractionStatRuleNotification.


        :return: The dimension_value_name of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._dimension_value_name

    @dimension_value_name.setter
    def dimension_value_name(self, dimension_value_name):
        """
        Sets the dimension_value_name of this InteractionStatRuleNotification.


        :param dimension_value_name: The dimension_value_name of this InteractionStatRuleNotification.
        :type: str
        """
        
        self._dimension_value_name = dimension_value_name

    @property
    def metric(self):
        """
        Gets the metric of this InteractionStatRuleNotification.


        :return: The metric of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this InteractionStatRuleNotification.


        :param metric: The metric of this InteractionStatRuleNotification.
        :type: str
        """
        allowed_values = ["tAbandon", "tAnswered", "tTalk", "nOffered", "tHandle", "nTransferred", "oServiceLevel", "tWait", "tHeld", "tAcw"]
        if metric.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for metric -> " + metric
            self._metric = "outdated_sdk_version"
        else:
            self._metric = metric

    @property
    def media_type(self):
        """
        Gets the media_type of this InteractionStatRuleNotification.


        :return: The media_type of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this InteractionStatRuleNotification.


        :param media_type: The media_type of this InteractionStatRuleNotification.
        :type: str
        """
        allowed_values = ["voice", "chat", "email", "callback", "sms"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for media_type -> " + media_type
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def numeric_range(self):
        """
        Gets the numeric_range of this InteractionStatRuleNotification.


        :return: The numeric_range of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._numeric_range

    @numeric_range.setter
    def numeric_range(self, numeric_range):
        """
        Sets the numeric_range of this InteractionStatRuleNotification.


        :param numeric_range: The numeric_range of this InteractionStatRuleNotification.
        :type: str
        """
        allowed_values = ["gt", "gte", "lt", "lte", "eq", "ne"]
        if numeric_range.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for numeric_range -> " + numeric_range
            self._numeric_range = "outdated_sdk_version"
        else:
            self._numeric_range = numeric_range

    @property
    def statistic(self):
        """
        Gets the statistic of this InteractionStatRuleNotification.


        :return: The statistic of this InteractionStatRuleNotification.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """
        Sets the statistic of this InteractionStatRuleNotification.


        :param statistic: The statistic of this InteractionStatRuleNotification.
        :type: str
        """
        allowed_values = ["count", "min", "ratio", "max"]
        if statistic.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for statistic -> " + statistic
            self._statistic = "outdated_sdk_version"
        else:
            self._statistic = statistic

    @property
    def value(self):
        """
        Gets the value of this InteractionStatRuleNotification.


        :return: The value of this InteractionStatRuleNotification.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this InteractionStatRuleNotification.


        :param value: The value of this InteractionStatRuleNotification.
        :type: float
        """
        
        self._value = value

    @property
    def in_alarm(self):
        """
        Gets the in_alarm of this InteractionStatRuleNotification.


        :return: The in_alarm of this InteractionStatRuleNotification.
        :rtype: bool
        """
        return self._in_alarm

    @in_alarm.setter
    def in_alarm(self, in_alarm):
        """
        Sets the in_alarm of this InteractionStatRuleNotification.


        :param in_alarm: The in_alarm of this InteractionStatRuleNotification.
        :type: bool
        """
        
        self._in_alarm = in_alarm

    @property
    def enabled(self):
        """
        Gets the enabled of this InteractionStatRuleNotification.


        :return: The enabled of this InteractionStatRuleNotification.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this InteractionStatRuleNotification.


        :param enabled: The enabled of this InteractionStatRuleNotification.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def notification_users(self):
        """
        Gets the notification_users of this InteractionStatRuleNotification.


        :return: The notification_users of this InteractionStatRuleNotification.
        :rtype: list[HeartBeatAlertNotificationNotificationUsers]
        """
        return self._notification_users

    @notification_users.setter
    def notification_users(self, notification_users):
        """
        Sets the notification_users of this InteractionStatRuleNotification.


        :param notification_users: The notification_users of this InteractionStatRuleNotification.
        :type: list[HeartBeatAlertNotificationNotificationUsers]
        """
        
        self._notification_users = notification_users

    @property
    def alert_types(self):
        """
        Gets the alert_types of this InteractionStatRuleNotification.


        :return: The alert_types of this InteractionStatRuleNotification.
        :rtype: list[str]
        """
        return self._alert_types

    @alert_types.setter
    def alert_types(self, alert_types):
        """
        Sets the alert_types of this InteractionStatRuleNotification.


        :param alert_types: The alert_types of this InteractionStatRuleNotification.
        :type: list[str]
        """
        
        self._alert_types = alert_types

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

