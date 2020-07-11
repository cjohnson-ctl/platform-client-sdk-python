# coding: utf-8

"""
AuditApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AuditApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_audits_query_servicemapping(self, **kwargs):
        """
        Get service mapping information used in audits.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audits_query_servicemapping(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AuditQueryServiceMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audits_query_servicemapping" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/audits/query/servicemapping'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuditQueryServiceMapping',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_audits_query_transaction_id(self, transaction_id, **kwargs):
        """
        Get status of audit query execution
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audits_query_transaction_id(transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transaction_id: Transaction ID (required)
        :return: AuditQueryExecutionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audits_query_transaction_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `get_audits_query_transaction_id`")


        resource_path = '/api/v2/audits/query/{transactionId}'.replace('{format}', 'json')
        path_params = {}
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuditQueryExecutionStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_audits_query_transaction_id_results(self, transaction_id, **kwargs):
        """
        Get results of audit query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audits_query_transaction_id_results(transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transaction_id: Transaction ID (required)
        :param str cursor: Indicates where to resume query results (not required for first page)
        :param int page_size: Page size
        :param list[str] expand: Which fields, if any, to expand
        :return: AuditQueryExecutionResultsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id', 'cursor', 'page_size', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audits_query_transaction_id_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `get_audits_query_transaction_id_results`")


        resource_path = '/api/v2/audits/query/{transactionId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuditQueryExecutionResultsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_audits_query(self, body, **kwargs):
        """
        Create audit query execution
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_audits_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuditQueryRequest body: query (required)
        :return: AuditQueryExecutionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_audits_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_audits_query`")


        resource_path = '/api/v2/audits/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuditQueryExecutionStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_audits_query_realtime(self, body, **kwargs):
        """
        This endpoint will only retrieve 7 days worth of audits for certain services. Please use /query to get a full list and older audits.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_audits_query_realtime(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuditRealtimeQueryRequest body: query (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: AuditRealtimeQueryResultsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_audits_query_realtime" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_audits_query_realtime`")


        resource_path = '/api/v2/audits/query/realtime'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuditRealtimeQueryResultsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
