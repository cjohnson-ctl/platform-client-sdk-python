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

class BatchDownloadJobStatusResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BatchDownloadJobStatusResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'job_id': 'str',
            'expected_result_count': 'int',
            'result_count': 'int',
            'error_count': 'int',
            'results': 'list[BatchDownloadJobResult]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'job_id': 'jobId',
            'expected_result_count': 'expectedResultCount',
            'result_count': 'resultCount',
            'error_count': 'errorCount',
            'results': 'results',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._job_id = None
        self._expected_result_count = None
        self._result_count = None
        self._error_count = None
        self._results = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this BatchDownloadJobStatusResult.
        The globally unique identifier for the object.

        :return: The id of this BatchDownloadJobStatusResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BatchDownloadJobStatusResult.
        The globally unique identifier for the object.

        :param id: The id of this BatchDownloadJobStatusResult.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BatchDownloadJobStatusResult.


        :return: The name of this BatchDownloadJobStatusResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BatchDownloadJobStatusResult.


        :param name: The name of this BatchDownloadJobStatusResult.
        :type: str
        """
        
        self._name = name

    @property
    def job_id(self):
        """
        Gets the job_id of this BatchDownloadJobStatusResult.
        JobId returned when job was initially submitted

        :return: The job_id of this BatchDownloadJobStatusResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this BatchDownloadJobStatusResult.
        JobId returned when job was initially submitted

        :param job_id: The job_id of this BatchDownloadJobStatusResult.
        :type: str
        """
        
        self._job_id = job_id

    @property
    def expected_result_count(self):
        """
        Gets the expected_result_count of this BatchDownloadJobStatusResult.
        Number of results expected when job is completed

        :return: The expected_result_count of this BatchDownloadJobStatusResult.
        :rtype: int
        """
        return self._expected_result_count

    @expected_result_count.setter
    def expected_result_count(self, expected_result_count):
        """
        Sets the expected_result_count of this BatchDownloadJobStatusResult.
        Number of results expected when job is completed

        :param expected_result_count: The expected_result_count of this BatchDownloadJobStatusResult.
        :type: int
        """
        
        self._expected_result_count = expected_result_count

    @property
    def result_count(self):
        """
        Gets the result_count of this BatchDownloadJobStatusResult.
        Current number of results available

        :return: The result_count of this BatchDownloadJobStatusResult.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """
        Sets the result_count of this BatchDownloadJobStatusResult.
        Current number of results available

        :param result_count: The result_count of this BatchDownloadJobStatusResult.
        :type: int
        """
        
        self._result_count = result_count

    @property
    def error_count(self):
        """
        Gets the error_count of this BatchDownloadJobStatusResult.
        Number of error results produced so far

        :return: The error_count of this BatchDownloadJobStatusResult.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """
        Sets the error_count of this BatchDownloadJobStatusResult.
        Number of error results produced so far

        :param error_count: The error_count of this BatchDownloadJobStatusResult.
        :type: int
        """
        
        self._error_count = error_count

    @property
    def results(self):
        """
        Gets the results of this BatchDownloadJobStatusResult.
        Current set of results for the job

        :return: The results of this BatchDownloadJobStatusResult.
        :rtype: list[BatchDownloadJobResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this BatchDownloadJobStatusResult.
        Current set of results for the job

        :param results: The results of this BatchDownloadJobStatusResult.
        :type: list[BatchDownloadJobResult]
        """
        
        self._results = results

    @property
    def self_uri(self):
        """
        Gets the self_uri of this BatchDownloadJobStatusResult.
        The URI for this object

        :return: The self_uri of this BatchDownloadJobStatusResult.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this BatchDownloadJobStatusResult.
        The URI for this object

        :param self_uri: The self_uri of this BatchDownloadJobStatusResult.
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

