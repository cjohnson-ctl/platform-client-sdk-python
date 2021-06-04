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

class BuForecastTimeSeriesResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuForecastTimeSeriesResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metric': 'str',
            'forecasting_method': 'str'
        }

        self.attribute_map = {
            'metric': 'metric',
            'forecasting_method': 'forecastingMethod'
        }

        self._metric = None
        self._forecasting_method = None

    @property
    def metric(self):
        """
        Gets the metric of this BuForecastTimeSeriesResult.
        The metric this result applies to

        :return: The metric of this BuForecastTimeSeriesResult.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this BuForecastTimeSeriesResult.
        The metric this result applies to

        :param metric: The metric of this BuForecastTimeSeriesResult.
        :type: str
        """
        allowed_values = ["Offered", "AverageHandleTimeSeconds"]
        if metric.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for metric -> " + metric)
            self._metric = "outdated_sdk_version"
        else:
            self._metric = metric

    @property
    def forecasting_method(self):
        """
        Gets the forecasting_method of this BuForecastTimeSeriesResult.
        The forecasting method that was used for this metric

        :return: The forecasting_method of this BuForecastTimeSeriesResult.
        :rtype: str
        """
        return self._forecasting_method

    @forecasting_method.setter
    def forecasting_method(self, forecasting_method):
        """
        Sets the forecasting_method of this BuForecastTimeSeriesResult.
        The forecasting method that was used for this metric

        :param forecasting_method: The forecasting_method of this BuForecastTimeSeriesResult.
        :type: str
        """
        allowed_values = ["AutoRegressiveIntegratedMovingAverage", "MovingAverage", "SingleExponentialSmoothing", "RandomWalk", "DecompositionUsingAdditiveSeasonality", "DecompositionUsingMultiplicativeSeasonality", "HoltWintersAdditiveSeasonality", "HoltWintersAdditiveSeasonalityWithDampedTrend", "HoltWintersMultiplicativeSeasonality", "HoltWintersMultiplicativeSeasonalityWithDampedTrend", "DampedLinearExponentialSmoothing", "DoubleExponentialSmoothing", "DoubleMovingAverage", "LinearExponentialSmoothing", "LinearWeightedMovingAverage", "PointEstimateUsingDampedLinearExponentialSmoothing", "PointEstimateUsingDoubleExponentialSmoothing", "PointEstimateUsingLatestWeek", "PointEstimateUsingLinearExponentialSmoothing", "PointEstimateUsingWeightedAverage", "CurveFit", "MultiLinearRegression", "DynamicHarmonicRegression", "Theta", "Other"]
        if forecasting_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for forecasting_method -> " + forecasting_method)
            self._forecasting_method = "outdated_sdk_version"
        else:
            self._forecasting_method = forecasting_method

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

